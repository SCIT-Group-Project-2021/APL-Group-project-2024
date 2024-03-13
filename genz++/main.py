
from lexer import Lexer
from parser import Parser

text_input = """
programName program1 {

        int num1 = 14.

        int x.

        multiply (13).

        int multiply (int num) {

            x = num1 + (2 * 34).

            x sayLess.
        }

        isItReally (x > 5) {
            x = 25.
        } orIsIt {
            x = 0.
        } 
        
        print(x).

        sayLess.
    } 
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)
    

pg = Parser()
pg.parse()
parser = pg.get_parser()
print(parser.parse(tokens).eval())
parser.parse(tokens).eval()