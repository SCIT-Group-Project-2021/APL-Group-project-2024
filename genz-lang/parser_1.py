from rply import ParserGenerator
import ast_1

class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'DIV', 'MUL']
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
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

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
