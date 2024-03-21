from tokenize import Token
from llvmlite import ir
import random

class VarDeclaration():
    def __init__(self, builder, data_type, target):
        self.builder = builder
        self.data_type = data_type
        self.target = target

    def eval(self):
        llvm_type = self.get_llvm_type(self.data_type)
        variable_name = self.target
        # Check if variable is already declared (local to function)
        for bb in self.builder.function.blocks:
            for instr in bb.instructions:
                if isinstance(instr, ir.AllocaInstr) and instr.name == variable_name:
                    raise ValueError(f"Variable '{variable_name}' is already declared in the function")
        # Allocate memory for the variable
        ptr = self.builder.alloca(llvm_type, name=variable_name)
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
        # Define function signature
        print("Paramters", self.parameters)
        llvm_return_type = self.get_llvm_type(self.return_type)
        param_types = [self.get_llvm_type(param.data_type) for param in self.parameters]
        func_type = ir.FunctionType(llvm_return_type, param_types)
        function = ir.Function(self.module, func_type, name=self.name)

        # Create entry block
        block = function.append_basic_block(name="function")
        builder = ir.IRBuilder(block)

        # Evaluate function body
        return_statement_seen = False
        print("body", self.body)
        for statement in self.body:
            # TODO: Find a better way to pass function builder for nested AST nodes
            statement.builder = builder
            statement.eval()
            if isinstance(statement, ReturnStatement):
                return_statement_seen = True

        # Ensure return statement for non-void functions
        if llvm_return_type != ir.VoidType() and not return_statement_seen:
            raise ValueError(f"Function '{self.name}' must have a return statement")

        # Ensure the last instruction is a terminator
        if not builder.block.is_terminated:
            if llvm_return_type == ir.VoidType():
                builder.ret_void()

        print("Function", function)
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
            target_name = self.target
            found = False
            for bb in self.builder.function.blocks:
                for instr in bb.instructions:
                    if isinstance(instr, ir.AllocaInstr) and instr.name == target_name:
                        ptr = instr
                        found = True
                        break
                if found:
                    break
            if not found:
                raise ValueError(f"Variable '{target_name}' not declared before assignment")
            self.builder.store(value, ptr)


class Initialization():
    def __init__(self, builder, module, data_type, target, value):
        self.builder = builder
        self.module = module
        self.data_type = data_type
        self.target = target
        self.value = value

    def eval(self):
        llvm_type = self.get_llvm_type(self.data_type)
        value = self.value.eval()

        # Check if the variable is already declared
        target_name = self.target
        for bb in self.builder.function.blocks:
            for instr in bb.instructions:
                if isinstance(instr, ir.AllocaInstr) and instr.name == target_name:
                    raise ValueError(f"Variable '{target_name}' is already declared")

        # Allocate memory for the variable
        ptr = self.builder.alloca(llvm_type, name=target_name)
        self.builder.store(value, ptr)

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
        self.module = module
        self.condition = condition
        self.body = body

    def eval(self):
        preheader_block = self.builder.block

        loop = self.builder.append_basic_block('loop')
        self.builder.branch(loop)
        self.builder.position_at_start(loop)

        cond = self.condition.eval()
        self.builder.cbranch(cond, loop, self.builder.block)

        self.builder.position_at_start(self.builder.block)

        for statement in self.body:
            statement.eval()

        self.builder.branch(loop)

        new_block = self.builder.append_basic_block('afterloop')
        self.builder.position_at_start(new_block)


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


class Sum(BinaryOp):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i
class Sub(BinaryOp):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i
    
class Mul(BinaryOp):
    def eval(self):
        i = self.builder.mul(self.left.eval(), self.right.eval())
        return i

class Div(BinaryOp):
    def eval(self):
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
