from llvmlite import ir
import random

class VarDeclaration():
    def __init__(self, builder, module, data_type, target):
        self.builder = builder
        self.module = module
        self.data_type = data_type
        self.target = target

    def eval(self):
        llvm_type = self.get_llvm_type(self.data_type)
        ptr = self.builder.alloca(llvm_type)
        self.module.globals[self.target] = ptr

    def get_llvm_type(self, data_type):
        if data_type == "int":
            return ir.IntType(32)
        elif data_type == "boolean":
            return ir.IntType(1)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")


class FunctionDeclaration():
    def __init__(self, builder, module, return_type, name, parameters, body):
        self.builder = builder
        self.module = module
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body

    def eval(self):
        # Define function signature
        llvm_return_type = self.get_llvm_type(self.return_type)
        param_types = [self.get_llvm_type(param.data_type) for param in self.parameters]
        func_type = ir.FunctionType(llvm_return_type, param_types)
        function = ir.Function(self.module, func_type, name=self.name)

        # Create entry block
        block = function.append_basic_block(name="entry")
        self.builder.position_at_start(block)

        # Evaluate function body
        return_statement_seen = False
        print("body", self.body)
        for statement in self.body:
            statement.eval()
            if isinstance(statement, ReturnStatement):
                return_statement_seen = True

        # Ensure return statement for non-void functions
        if llvm_return_type != ir.VoidType() and not return_statement_seen:
            raise ValueError(f"Function '{self.name}' must have a return statement")

        # Ensure the last instruction is a terminator
        if not self.builder.block.is_terminated:
            if llvm_return_type == ir.VoidType():
                self.builder.ret_void()

        print("Function", function)
        return function

    def get_llvm_type(self, data_type):
        if data_type == "void":
            return ir.VoidType()
        elif data_type == "int":
            return ir.IntType(32)
        elif data_type == "bool":
            return ir.IntType(1)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
        
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
        self.target = target
        self.value = value

    def eval(self):
        value = self.value.eval()
        if isinstance(self.target, ir.Value):
            # If target is an LLVM value, assign directly
            self.builder.store(value, self.target)
        else:
            # If target is an identifier, lookup its LLVM value and assign
            ptr = self.builder.alloca(value.type)
            self.builder.store(value, ptr)
            self.module.globals[self.target] = ptr

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
        ptr = self.builder.alloca(llvm_type)
        self.builder.store(value, ptr)
        self.module.globals[self.target] = ptr

    def get_llvm_type(self, data_type):
        if data_type == "int":
            return ir.IntType(32)
        elif data_type == "bool":
            return ir.IntType(1)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
        
class RelationalStatement():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right

    def eval(self):
        # Implement evaluation logic based on the specific relational operator
        # For example, for greater than: self.builder.icmp_signed('>', self.left.eval(), self.right.eval(), 'compare')
        raise NotImplementedError("Relational statements evaluation is not implemented")


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
