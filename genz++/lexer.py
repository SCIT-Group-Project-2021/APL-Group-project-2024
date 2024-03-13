from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        
        self.lexer.add('STRING_TYPE', r'string')
        self.lexer.add('INT_TYPE', r'int')
        self.lexer.add('CHAR_TYPE', r'char')
        self.lexer.add('FLOAT_TYPE', r'float')
        
        self.lexer.add('PRINT', r'print')
        self.lexer.add('TRUE', r'fax')
        self.lexer.add('FALSE', r'cap')
        
        self.lexer.add('IF', r'isItReally')
        self.lexer.add('THEN', r'bet')
        self.lexer.add('ELSE', r'orIsIt')
        
        self.lexer.add('RETURN', r'sayLess')
        # Ignore spaces
        self.lexer.ignore('\s+')
        
        
        
        self.lexer.add('FLOAT', 'NUM+.NUM+')
        self.lexer.add('INT', 'NUM+')
        self.lexer.add('NUM', '\d')
        self.lexer.add('STRING', "[a-zA-Z_][a-zA-Z0-9_]+")
        self.lexer.add('CHAR', "[a-zA-Z_]")
        
        
        self.lexer.add('OPN_BRC', r'\(')
        self.lexer.add('CLSD_BRC', r'\)')
        
        self.lexer.add('OPN_C_BRC', r'\{')
        self.lexer.add('CLSD_C_BRC', r'\}')
        
        self.lexer.add('TERMINATOR', r'\.')
        
        self.lexer.add('SQUOTE', r'\'')
        
        self.lexer.add('DQUOTE', r'\"')
        
        self.lexer.add('INT_SEPARATOR', r'\.')
        
        self.lexer.add('SEPARATOR', r'\,')
        
        self.lexer.add('EQUAL', r'\=')
        self.lexer.add('MULTIPLY', r'\*')
        self.lexer.add('DIVIDE', r'\/')
        self.lexer.add('ADD', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('GREATER', r'\>')
        self.lexer.add('LESS', r'\<')
        
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()