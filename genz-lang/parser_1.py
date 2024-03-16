from rply import ParserGenerator
import ast_1

class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SUM', 'SUB', 'DIV', 'MUL', 'IDENTIFIER', 'OPEN_CURL_BRACE', 'CLOSE_CURL_BRACE',
             'TERMINATOR', 'COMMA', 'IF', 'WHILE', 'RETURN', 'INT', 'VOID', 'EQUALS'
             ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : statements')
        @self.pg.production('program : function_declaration')
        def program(p):
            return p[0]
        
        @self.pg.production('statements : statement')
        @self.pg.production('statements : statement statements')
        def statements(p):
            if len(p) == 1:
                return p[0]  
            else:
                return [p[0]] + p[1]
        
        @self.pg.production('statement : assignment')
        @self.pg.production('statement : if_statement')
        @self.pg.production('statement : while_statement')
        @self.pg.production('statement : return_statement')
        @self.pg.production('statement : print_statement')
        def statement(p):
            return p[0]
        
        @self.pg.production('function_declaration : data_type IDENTIFIER OPEN_PAREN parameters CLOSE_PAREN OPEN_CURL_BRACE statements CLOSE_CURL_BRACE')
        def function_declaration(p):
            return None
        
        @self.pg.production('parameters : parameter COMMA')
        @self.pg.production('parameters : parameter COMMA parameters')
        def parameters(p):
            return None
        
        @self.pg.production('parameter : IDENTIFIER')
        def parameter(p):
            return None
        
        @self.pg.production('data_type : INT')
        @self.pg.production('data_type : VOID')
        def data_type(p):
            return None
        
        @self.pg.production('assignment : IDENTIFIER EQUALS expression')
        def assignment_statement(p):
            return None
        
        @self.pg.production('if_statement : IF OPEN_PAREN expression CLOSE_PAREN OPEN_CURL_BRACE statements CLOSE_CURL_BRACE')
        def if_statement(p):
            return None
        
        @self.pg.production('while_statement : WHILE OPEN_PAREN expression CLOSE_PAREN OPEN_CURL_BRACE statements CLOSE_CURL_BRACE')
        def while_statement(p):
            return None
        
        @self.pg.production('return_statement : RETURN expression TERMINATOR')
        def return_statement(p):
            return None

        @self.pg.production('print_statement : PRINT OPEN_PAREN expression CLOSE_PAREN TERMINATOR')
        def print_statement(p):
            return ast_1.Print(self.builder, self.module, self.printf, p[2])

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
        
        @self.pg.production('identifier : IDENTIFIER')
        @self.pg.production('expression : identifier')
        def identifier(p):
            return None
        
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def parenthesized_expression(p):
            return p[1]
        
        @self.pg.error
        def error_handle(token):
            raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

    def get_parser(self):
        return self.pg.build()
