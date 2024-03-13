
from rply import ParserGenerator
from ast import Number, Sum, Sub, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['PRINT', 'FLOAT' ,'INT', 'NUM' , 'STRING', 'CHAR', 'OPN_BRC','CLSD_BRC', 'OPN_C_BRC', 'CLSD_C_BRC',
             'TERMINATOR', 'SQUOTE', 'DQUOTE','INT_SEPARATOR','SEPARATOR', 'EQUAL', 'MULTIPLY', 
             'DIVIDE', 'ADD', 'SUB','TRUE', 'FALSE', 'IF', 
             'THEN', 'ELSE', 'RETURN','CHAR_TYPE', 'INT_TYPE', 'STRING_TYPE', 'FLOAT_TYPE']
        )

    def parse(self):
                
        @self.pg.production('program-dec : identifier OPN_C_BRC statements return-statement CLSD_C_BRC')
        def program_dec(p):
            # Implementation of program-dec rule
            pass
        @self.pg.production('identifier : STRING') #1 shift/reduce conflicts
        
        @self.pg.production('literal : DQUOTE STRING DQUOTE | bool | num-literal')
        
        @self.pg.production('num-literal : FLOAT | INT') #2 shift/reduce conflicts
        
        
        @self.pg.production('bool : TRUE | FALSE') #3 shift/reduce conflicts
        
        @self.pg.production('binary_operator : EQUAL | MULTIPLY | DIVIDE| ADD| SUB')
        
        @self.pg.production('type : STRING_TYPE | INT_TYPE | CHAR_TYPE | FLOAT_TYPE')
        
        
        @self.pg.production('statements : statement TERMINATOR')
        
        @self.pg.production('statements : statement statements')
        
        
        @self.pg.production('statement : selection-statement | return-statement | declaration-statement | expression')
        
        @self.pg.production('selection-statement : if-selection')
        
        @self.pg.production('declaration-statement : type-declaration TERMINATOR | function-declaration')
        
        @self.pg.production('return-statement : RETURN TERMINATOR | identifier RETURN TERMINATOR | literal RETURN TERMINATOR')
    
        @self.pg.production('expression : math-expression TERMINATOR | function-expression TERMINATOR | print-expression TERMINATOR')    
        
        @self.pg.production('parameter : num-literal | identifier')    
          
        
        @self.pg.production('math-expression : parameter binary_operator parameter')
        
        @self.pg.production('function-expression : identifier OPN_BRC parameter CLSD_BRC')

        @self.pg.production('print-expression : PRINT OPN_BRC parameter CLSD_BRC')
        
        @self.pg.production('type-declaration : type identifier TERMINATOR | type identifier EQUAL literal TERMINATOR')
        
        @self.pg.production('function-declaration : type identifier  OPN_BRC type-declaration CLSD_BRC OPN_C_BRC statements return-statement CLSD_C_BRC ')
        @self.pg.production('function-declaration : type identifier  OPN_BRC type-declaration SEPARATOR type-declaration CLSD_BRC OPN_C_BRC statements return-statement CLSD_C_BRC ')
        
          
        @self.pg.production('if-selection : IF OPN_BRC statements CLSD_BRC THEN OPN_C_BRC statement CLSD_C_BRC | IF OPN_BRC statements CLSD_BRC THEN OPN_C_BRC statements CLSD_C_BRC ELSE OPN_C_BRC statements CLSD_C_BRC')
        
        
        def program(p):
            return Print(p[2])

        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'ADD':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()