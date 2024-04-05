from rply import ParserGenerator
import ast_1

class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SUM', 'SUB', 'DIV', 'MUL', 'IDENTIFIER', 'OPEN_CURL_BRACE', 'CLOSE_CURL_BRACE',
             'TERMINATOR', 'COMMA', 'IF', 'ELSE', 'WHILE', 'RETURN', 'TYPE_INT', 'TYPE_VOID', 'TYPE_BOOLEAN', 
             'EQUALS', 'NOT_EQUALS', 'ASSIGN', 'TRUE', 'FALSE', 'GREATER_THAN', 'LESS_THAN', 'GREATER_THAN_EQUALS',
             'LESS_THAN_EQUALS'
             ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf
        self.AST_statements = []

    def parse(self):
        @self.pg.production('program : statements')
        def program(p):
            self.AST_statements.append(p[0])
            return self.remove_duplicates(self.AST_statements)
        
        @self.pg.production('statements : statement statements')
        @self.pg.production('statements : statement')
        def statements(p):
            if len(p) == 1:
                self.AST_statements.append(p[0])
            else:
                self.AST_statements.append(p[0])
                self.AST_statements.append(p[1][0])
            return self.remove_duplicates(self.AST_statements)
        
        @self.pg.production('block_statements : block_statement block_statements')
        @self.pg.production('block_statements : block_statement')
        def block_statements(p):
            if len(p) == 1:
                return [p[0]]
            else:
                return self.remove_duplicates([p[0]] + [p[1]])
            
        @self.pg.production('block_statement : assignment')
        @self.pg.production('block_statement : if_statement')
        @self.pg.production('block_statement : while_statement')
        @self.pg.production('block_statement : return_statement')
        @self.pg.production('block_statement : print_statement')
        @self.pg.production('block_statement : var_declaration')
        @self.pg.production('block_statement : initialization')
        @self.pg.production('statement : function_call')
        def block_statement(p):
            return p[0]
        
        @self.pg.production('statement : assignment')
        @self.pg.production('statement : if_statement')
        @self.pg.production('statement : while_statement')
        @self.pg.production('statement : return_statement')
        @self.pg.production('statement : print_statement')
        @self.pg.production('statement : var_declaration')
        @self.pg.production('statement : initialization')
        @self.pg.production('statement : function_declaration')
        @self.pg.production('statement : function_call')
        def statement(p):
            return p[0]
    
        @self.pg.production('function_declaration : data_type IDENTIFIER OPEN_PAREN parameters CLOSE_PAREN OPEN_CURL_BRACE block_statements CLOSE_CURL_BRACE')
        @self.pg.production('function_declaration : data_type IDENTIFIER OPEN_PAREN CLOSE_PAREN OPEN_CURL_BRACE block_statements CLOSE_CURL_BRACE')
        def function_declaration(p):
            parameters = p[3] if len(p) == 8 else []
            return ast_1.FunctionDeclaration(self.module, p[0], p[1].getstr(), parameters, p[-2])
        
        @self.pg.production('parameters : parameter COMMA parameters')
        @self.pg.production('parameters : parameter')
        def parameters(p):
            if len(p) == 1:
                return [p[0]]
            else:
                return self.remove_duplicates([p[0]] + [p[2]])
        
        @self.pg.production('parameter : data_type IDENTIFIER')
        def parameter(p):
            return ast_1.Parameter(p[0], p[1].getstr())
        
        @self.pg.production('function_call : IDENTIFIER OPEN_PAREN arguments CLOSE_PAREN TERMINATOR')
        @self.pg.production('function_call : IDENTIFIER OPEN_PAREN CLOSE_PAREN TERMINATOR')
        def function_call(p):
            if(len(p) == 4):
                return ast_1.FunctionCall(self.builder, self.module, p[0])
            else:
                return ast_1.FunctionCall(self.builder, self.module, p[0], p[2])
            
        @self.pg.production('arguments : arguments COMMA arguments')
        @self.pg.production('arguments : argument')
        def arguments(p):
            if len(p) == 1:
                return [p[0]]
            else:
                return self.remove_duplicates([p[0]] + [p[2]])
        
        @self.pg.production('argument : expression')
        def argument(p):
            return p[0]
            
        @self.pg.production('data_type : TYPE_INT')
        @self.pg.production('data_type : TYPE_VOID')
        @self.pg.production('data_type : TYPE_BOOLEAN')
        def data_type(p):
            return p[0].getstr()
        
        @self.pg.production('assignment : IDENTIFIER ASSIGN expression TERMINATOR')
        @self.pg.production('assignment : IDENTIFIER ASSIGN function_call')
        def assignment_statement(p):
            return ast_1.Assignment(self.builder, self.module, p[0], p[2])
        
        @self.pg.production('initialization : data_type IDENTIFIER ASSIGN expression TERMINATOR')
        @self.pg.production('initialization : data_type IDENTIFIER ASSIGN function_call')
        def initialization_statement(p):
            return ast_1.Initialization(self.builder, self.module, p[0], p[1].getstr(), p[3])

        @self.pg.production('if_statement : IF OPEN_PAREN conditional_expression CLOSE_PAREN OPEN_CURL_BRACE block_statements CLOSE_CURL_BRACE')
        @self.pg.production('if_statement : IF OPEN_PAREN conditional_expression CLOSE_PAREN OPEN_CURL_BRACE block_statements CLOSE_CURL_BRACE ELSE OPEN_CURL_BRACE block_statements CLOSE_CURL_BRACE')
        def if_statement(p):
            if len(p) == 7:
                return ast_1.IfStatement(self.builder, self.module, p[2], p[5])
            else:
                return ast_1.IfElseStatement(self.builder, self.module, p[2], p[5], p[9])

        @self.pg.production('while_statement : WHILE OPEN_PAREN conditional_expression CLOSE_PAREN OPEN_CURL_BRACE statements CLOSE_CURL_BRACE')
        def while_statement(p):
            return ast_1.WhileStatement(self.builder, self.module, p[2], p[5])
        
        @self.pg.production('var_declaration : data_type IDENTIFIER TERMINATOR')
        def var_declaration(p):
            return ast_1.VarDeclaration(self.builder, p[0], p[1].getstr())
        
        @self.pg.production('return_statement : RETURN expression TERMINATOR')
        def return_statement(p):
            return ast_1.ReturnStatement(self.builder, self.module, p[1])

        @self.pg.production('print_statement : PRINT OPEN_PAREN expression CLOSE_PAREN TERMINATOR')
        def print_statement(p):
            return ast_1.Print(self.builder, self.module, self.printf, p[2])
        
        @self.pg.production('conditional_expression : expression GREATER_THAN expression')
        @self.pg.production('conditional_expression : expression LESS_THAN expression')
        @self.pg.production('conditional_expression : expression GREATER_THAN_EQUALS expression')
        @self.pg.production('conditional_expression : expression LESS_THAN_EQUALS expression')
        @self.pg.production('conditional_expression : expression EQUALS expression')
        @self.pg.production('conditional_expression : expression NOT_EQUALS expression')
        @self.pg.production('expression : conditional_expression')
        def conditional_expression(p):
            if len(p) == 1:
                return p[0]
            else:
                left = p[0]
                right = p[2]
                operator = p[1].value
                return ast_1.RelationalStatement(self.builder, self.module, left, right, operator)
            
        @self.pg.production('conditional_expression : TRUE')
        @self.pg.production('conditional_expression : FALSE')
        def boolean_expression(p):
            if (p[0].value == 'fax'):
                return ast_1.Number(self.builder, self.module, 1)
            elif (p[0].value == 'cap'):
                return ast_1.Number(self.builder, self.module, 0)

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return ast_1.Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return ast_1.Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MUL':
                return ast_1.Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return ast_1.Div(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return ast_1.Number(self.builder, self.module, p[0].value)
        
        @self.pg.production('expression : IDENTIFIER')
        def identifier(p):
            return ast_1.Identifier(self.builder, self.module, p[0].value)
        
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def parenthesized_expression(p):
            return p[1]
        
        @self.pg.error
        def error_handle(token):
            raise SyntaxError(f"SYNTAX ERROR at line {token.source_pos.lineno}, column {token.source_pos.colno}: Unexpected token '{token.gettokentype()}'")

    def get_parser(self):
        return self.pg.build()
    
    def remove_duplicates(self, lst):
        flattened_list = self.flatten_list(lst)
        new_list = []
        for item in flattened_list:
            if item not in new_list:
                new_list.append(item)
        return new_list

    def flatten_list(self, lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(self.flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list
