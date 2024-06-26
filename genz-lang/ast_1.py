from llvmlite import ir
import random

stack = [{}]
program_builder = [None]
class SymbolTable:
    def push_scope(self):
        stack.append({})

    def push_builder(self, builder):
        program_builder.append(builder)
       
    def pop_scope(self):
        stack.pop()

    def pop_builder(self):
        program_builder.pop()
        
    def declare_variable(self, name, llvm_type):
        current_scope = stack[-1]
        if name in current_scope:
            raise ValueError(f"Variable '{name}' already declared in this scope")
        current_scope[name] = llvm_type

    def lookup_variable(self, name):
        for scope in reversed(stack):
            if name in scope:
                return scope[name]
        raise ValueError(f"Variable '{name}' not found")

class VarDeclaration():
    def __init__(self, builder, data_type, target):
        self.builder = builder
        self.data_type = data_type
        self.target = target

    def eval(self):
        symbol_table = SymbolTable()
        llvm_type = self.get_llvm_type(self.data_type)
        variable_name = self.target
        # Check if variable is already declared (local to function)
        for bb in self.builder.function.blocks:
            for instr in bb.instructions:
                if isinstance(instr, ir.AllocaInstr) and instr.name == variable_name:
                    raise ValueError(f"Variable '{variable_name}' is already declared in the function")
        # Allocate memory for the variable
        ptr = self.builder.alloca(llvm_type, name=variable_name)
        symbol_table.declare_variable(variable_name, ptr)
        return ptr

    def get_llvm_type(self, data_type):
        if data_type == "int":
            return ir.IntType(8)
        elif data_type == "boolean":
            return ir.IntType(1)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")


class FunctionDeclaration():
    def __init__(self, module, return_type, name, parameters, body):
        self.module = module
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body

    def eval(self):
        symbol_table = SymbolTable()
        symbol_table.push_scope()

        # Define function signature
        llvm_return_type = self.get_llvm_type(self.return_type)
        param_types = [self.get_llvm_type(param.data_type) for param in self.parameters]
        func_type = ir.FunctionType(llvm_return_type, param_types)
        function = ir.Function(self.module, func_type, name=self.name)

        # Create entry block
        block = function.append_basic_block(name="function")
        builder = ir.IRBuilder(block)

        symbol_table.push_builder(builder)
        
        # Allocate space for parameters and store their values
        arg_values = []

        for llvm_arg, param in zip(function.args, self.parameters):
            llvm_arg.name = param.name
            arg_values.append(llvm_arg)
            # Allocate space for parameter and store its value
            alloca = builder.alloca(llvm_arg.type)
            builder.store(llvm_arg, alloca)
            symbol_table.declare_variable(param.name, alloca)
            
        # Evaluate function body
        return_statement_seen = False
        print("function body", self.body)
        for statement in self.body:
            # TODO: Find a better way to pass function builder for nested AST nodes
            statement.builder = builder
            statement.eval()
            if isinstance(statement, ReturnStatement):
                return_statement_seen = True
        
        symbol_table.pop_scope()

        # Ensure return statement for non-void functions
        if llvm_return_type != ir.VoidType() and not return_statement_seen:
            raise ValueError(f"Function '{self.name}' must have a return statement")

        # Ensure the last instruction is a terminator
        if not builder.block.is_terminated:
            if llvm_return_type == ir.VoidType():
                builder.ret_void()
        return function

    def get_llvm_type(self, data_type):
        if data_type == "void":
            return ir.VoidType()
        elif data_type == "int":
            return ir.IntType(8)
        elif data_type == "bool":
            return ir.IntType(1)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
        
class FunctionCall:
    def __init__(self, builder, module, name, arguments = None):
        self.builder = builder
        self.module = module
        self.name = name.getstr()
        self.arguments = arguments

    def eval(self):
        # Retrieve the function from the module
        function = self.module.get_global(self.name)

        if function is None:
            raise ValueError(f"Function '{self.name}' does not exist")

        if (self.arguments):
            # Ensure the number of arguments matches the function signature
            if len(self.arguments) != len(function.function_type.args):
                raise ValueError(f"Number of arguments mismatch for function '{self.name}'")

            # Prepare the arguments
            llvm_arguments = [arg.eval() for arg in self.arguments]

            # Generate the method call instruction
            return self.builder.call(function, llvm_arguments)
        return self.builder.call(function, [])
        
class Parameter():
    def __init__(self, data_type, name):
        self.data_type = data_type
        self.name = name

class ReturnStatement():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        self.value.builder = self.builder
        if self.value:
            return_value = self.value.eval()
            self.builder.ret(return_value)
        else:
            self.builder.ret_void()
            
class Assignment():
    def __init__(self, builder, module, target, value):
        self.builder = builder
        self.module = module
        self.target = target.getstr()
        self.value = value

    def eval(self):
        value = self.value.eval()
        if isinstance(self.target, ir.Value):
            self.builder.store(value, self.target)
        else:
            # If target is an identifier, lookup its LLVM value and assign
            symbol_table = SymbolTable()
            ptr = symbol_table.lookup_variable(self.target)
            if isinstance(ptr, ir.AllocaInstr):
                self.builder.store(value, ptr)
            else:
                raise ValueError(f"Variable '{self.target}' not declared before assignment")

class Initialization():
    def __init__(self, builder, module, data_type, target, value):
        self.builder = builder
        self.module = module
        self.data_type = data_type
        self.target = target
        self.value = value

    def eval(self):
        symbol_table = SymbolTable()
        llvm_type = self.get_llvm_type(self.data_type)
        value = self.value.eval()

        # Check if the variable is already declared
        target_name = self.target
        if target_name in stack[-1]:  # Check in the current scope
            raise ValueError(f"Variable '{target_name}' is already declared")

        # Allocate memory for the variable
        ptr = self.builder.alloca(llvm_type, name=target_name)
        self.builder.store(value, ptr)
        symbol_table.declare_variable(target_name, ptr)

    def get_llvm_type(self, data_type):
        if data_type == "int":
            return ir.IntType(8)
        elif data_type == "bool":
            return ir.IntType(1)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
        
class RelationalStatement():
    def __init__(self, builder, module, left, right, operator):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right
        self.operator = operator

    def eval(self):
        left_value = self.left.eval()
        right_value = None
        if self.right:
            right_value = self.right.eval()

        if self.operator == '>':
            return self.builder.icmp_signed('>', left_value, right_value, 'compare_gt')
        elif self.operator == '<':
            return self.builder.icmp_signed('<', left_value, right_value, 'compare_lt')
        elif self.operator == '>=':
            return self.builder.icmp_signed('>=', left_value, right_value, 'compare_ge')
        elif self.operator == '<=':
            return self.builder.icmp_signed('<=', left_value, right_value, 'compare_le')
        elif self.operator == '==':
            return self.builder.icmp_signed('==', left_value, right_value, 'compare_eq')
        elif self.operator == '!=':
            return self.builder.icmp_signed('!=', left_value, right_value, 'compare_ne')
        elif self.operator == 'and':
            return self.builder.and_(left_value, right_value)
        elif self.operator == 'or':
            return self.builder.or_(left_value, right_value)
        elif self.operator == 'not':
            return self.builder.not_(left_value)

        else:
            raise ValueError(f"Unsupported relational operator: {self.operator}")
        
class IfStatement():
    def __init__(self, builder, module, condition, body):
        self.builder = builder
        self.module = module
        self.condition = condition
        self.body = body

    def eval(self):
        cond = self.condition.eval()
        with self.builder.if_then(cond) as then:
            for statement in self.body:
                statement.eval()

class IfElseStatement():
    def __init__(self, builder, module, condition, body, else_body):
        self.builder = builder
        self.module = module
        self.condition = condition
        self.body = body
        self.else_body = else_body

    def eval(self):
        cond = self.condition.eval()

        with self.builder.if_else(cond) as (then, otherwise):
            with then:
                for statement in self.body:
                    statement.eval()

            with otherwise:
                for statement in self.else_body:
                    statement.eval()

class WhileStatement():
    def __init__(self, builder, module, condition, body):
        self.builder = builder
        self.condition = condition
        self.body = body

    def eval(self):
        loop = self.builder.append_basic_block('loop')
        body_block = self.builder.append_basic_block('body')
        afterloop_block = self.builder.append_basic_block('afterloop')

        # Branch to the loop condition evaluation
        self.builder.branch(loop)
        self.builder.position_at_start(loop)

        # Evaluate the loop condition
        self.builder.position_at_end(loop)
        cond = self.condition.eval()

        # Branch to the body or afterloop based on the condition
        self.builder.cbranch(cond, body_block, afterloop_block)

        # Generate code for the loop body
        self.builder.position_at_start(body_block)
        for statement in self.body:
            statement.eval()

        # Branch back to the loop condition evaluation
        self.builder.branch(loop)

        # Move to afterloop
        self.builder.position_at_start(afterloop_block)

class Identifier():
    def __init__(self, builder, module, name):
        self.builder = builder
        self.module = module
        self.name = name

    def eval(self):
        symbol_table = SymbolTable()
        # Look for alloca instruction of the identifier
        ptr = symbol_table.lookup_variable(self.name)

        if isinstance(ptr, ir.AllocaInstr):
            return self.builder.load(ptr)
        else:
            raise ValueError(f"Identifier '{self.name}' not declared in the current scope")

class BooleanVal():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(1), int(self.value))
        return i
    
class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.value))
        return i
class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right
    
    def set_builder(self):
        if(program_builder[-1]):
            self.builder = program_builder[-1]
            self.left.builder = program_builder[-1]
            self.right.builder = program_builder[-1]

class Sum(BinaryOp):
    def eval(self):
        self.set_builder()
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i
class Sub(BinaryOp):
    def eval(self):
        self.set_builder()
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i
    
class Mul(BinaryOp):
    def eval(self):
        self.set_builder()
        i = self.builder.mul(self.left.eval(), self.right.eval())
        return i

class Div(BinaryOp):
    def eval(self):
        self.set_builder()
        i = self.builder.sdiv(self.left.eval(), self.right.eval())
        return i

class Print():
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        self.value.builder = self.builder
        value = self.value.eval()

        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        # TODO: Find a better way instead of using global vars for each print func
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=f"fstr-${random.randint(0, 99999)}")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, value])
