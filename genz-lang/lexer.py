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

        # Comparisons
        self.lexer.add('TRUE', r'fax')
        self.lexer.add('FALSE', r'cap')
        self.lexer.add('EQUALS', r'==')
        self.lexer.add('NOT_EQUALS', r'!=')
        self.lexer.add('GREATER_THAN_EQUALS', r'>=')
        self.lexer.add('LESS_THAN_EQUALS', r'<=')
        self.lexer.add('GREATER_THAN', r'>')
        self.lexer.add('LESS_THAN', r'<')

        # Symbols
        self.lexer.add('TERMINATOR', r'\.')
        self.lexer.add('COMMA', r',')
        self.lexer.add('ASSIGN', r'=')

        # Constructs
        self.lexer.add('IF', r'isItReally')
        self.lexer.add('ELSE', r'orIsIt')
        self.lexer.add('WHILE', r'while')

        # Return Statement
        self.lexer.add('RETURN', r'sayLess')

        # Data Types
        self.lexer.add('TYPE_INT', r'int')
        self.lexer.add('TYPE_VOID', r'void')
        self.lexer.add('TYPE_BOOLEAN', r'bool')

        # Identifier 
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
    
    def print_tokens(self, text_input):
        lexer = self.get_lexer()
        try:
            for token in lexer.lex(text_input):
                print(f"Token: {token.name}, Value: {token.value}")
        except Exception as e:
            print(f"Lexer Error: {e}")
