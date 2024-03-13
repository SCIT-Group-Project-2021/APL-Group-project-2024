
from rply import ParserGenerator
from ast import Number, Sum, Sub, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['PRINT', 'FLOAT' ,'INT' , 'STRING', 'CHAR', 'OPN_BRC','CLSD_BRC', 'OPN_C_BRC', 'CLSD_C_BRC',
             'TERMINATOR', 'DQUOTE','SEPERATOR', 'EQUAL', 'MULTIPLY', 
             'DIVIDE', 'ADD', 'SUB','GREATER', 'LESS', 'TRUE', 'FALSE', 'IF', 
             'THEN', 'ELSE', 'RETURN','CHAR_TYPE', 'INT_TYPE', 'STRING_TYPE', 'FLOAT_TYPE'],

            precedence=[ 
                ('left', ['<statement>',]), 
                ('left', ['EQUAL',]),  
                ('left', ['SEPERATOR',]), 
                ('left', ['OPN_BRC','CLSD_BRC', 'OPN_C_BRC', 'CLSD_C_BRC']), 
                ('left', ['IF', 'THEN', 'ELSE']), 
                ('left', ['GREATER', 'LESS']), 
                ('left', ['MULTIPLY','DIVIDE', 'ADD', 'SUB'])
            ]
        
        )

    def parse(self):
                
        @self.pg.production('<program-dec> : <identifier> OPN_C_BRC <statements> <return-statement> CLSD_C_BRC')
        def program_dec(p):
            # Implementation of program-dec rule
            pass
        
        #literals
        
        @self.pg.production('<identifier> : STRING | CHAR')
        
        @self.pg.production('<type> : STRING_TYPE | INT_TYPE | CHAR_TYPE | FLOAT_TYPE')
        
        @self.pg.production('<literal> : DQUOTE STRING DQUOTE | <bool> | <num-literal>')
        
        @self.pg.production('<num-literal> : FLOAT | INT')
        
        @self.pg.production('<bool> : TRUE | FALSE')
        
        @self.pg.production('<binary_operator> : EQUAL | MULTIPLY | DIVIDE| ADD | SUB | GREATER | LESS')
        
        @self.pg.production('<parameter> : <identifier> | <bool> | <num-literal>')
        @self.pg.production('<parameters> : <parameter> SEPERATOR <parameters>')
        @self.pg.production('<parameters> : <parameter>')
        
        #Statements
        
        @self.pg.production('<statement> : <selection-statement> | <return-statement> | <declaration-statement> | <expression>')
        def statement(p):
            pass
        @self.pg.production('<statements> : <statement> <statements> | <statement> TERMINATOR')
        
        @self.pg.production('<selection-statement> : <if-selection>')
        
        @self.pg.production('<declaration-statement> : <type-declaration> TERMINATOR | <function-declaration>')
        
        @self.pg.production('<return-statement> : RETURN TERMINATOR | <parameter> RETURN TERMINATOR')
    
        #Expressions
    
        @self.pg.production('<expression> : <math-expression> TERMINATOR | <function-expression> TERMINATOR | <print-expression> TERMINATOR ')       
        def expression(p):
            pass
        
        @self.pg.production('<math-expression> : <parameter> | <parameter> <binary_operator> <parameter> | <parameter> <binary_operator> OPN_BRC <math-expression> CLSD_BRC')
        
        @self.pg.production('<function-expression> : <identifier> OPN_BRC <parameters> CLSD_BRC')
        
        @self.pg.production('<print-expression> : PRINT OPN_BRC <expression> CLSD_BRC | PRINT OPN_BRC STRING CLSD_BRC')
        #Declarations
        
        @self.pg.production('<type-declaration> : <type> <identifier> TERMINATOR | <type> <identifier> EQUAL <literal> TERMINATOR')
        @self.pg.production('<type-declarations> : <type-declaration> SEPERATOR <type-declarations> | <type-declaration>')
        
        @self.pg.production('<function-declaration> : <type> <identifier>  OPN_BRC <type-declarations> CLSD_BRC OPN_C_BRC <statements> <return-statement> CLSD_C_BRC ')
          
        @self.pg.production('<if-selection> : IF OPN_BRC <statement> CLSD_BRC THEN OPN_C_BRC <statement> CLSD_C_BRC | IF OPN_BRC <statement> CLSD_BRC THEN OPN_C_BRC <statement> CLSD_C_BRC ELSE OPN_C_BRC <statement> CLSD_C_BRC')
    

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()