from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Curl Braces
        self.lexer.add('OPEN_CURL_BRACE', r'\{')
        self.lexer.add('CLOSE_CURL_BRACE', r'\}')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Symbols
        self.lexer.add('TERMINATOR', r'\.')
        self.lexer.add('COMMA', r',')
        self.lexer.add('EQUALS', r'=')

        # Constructs
        self.lexer.add('IF', r'isItReally')
        self.lexer.add('WHILE', r'while')

        # Return Statement
        self.lexer.add('RETURN', r'sayLess')

        # Data Types
        self.lexer.add('INT', r'int')
        self.lexer.add('VOID', r'void')

        # Identifier 
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
    
    def print_tokens(self, text_input):
        lexer = self.get_lexer()
        for token in lexer.lex(text_input):
            print(f"Token: {token.name}, Value: {token.value}")
