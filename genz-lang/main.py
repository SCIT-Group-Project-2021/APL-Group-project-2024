import sys
from lexer import Lexer
from parser_1 import Parser
from codegen import CodeGen

# Default file path if no argument is provided
fname = "input.z"

# Get the file path from the terminal arguments
if len(sys.argv) > 1:
    fname = sys.argv[1]
    
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
print("----- TOKENS ------\n")
Lexer().print_tokens(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parse_tree = parser.parse(tokens)[::-1]

print("\n\n ----- PARSE TREE ------\n")
print(parse_tree)
for statement in parse_tree:
    statement.eval()

codegen.create_ir()
codegen.save_ir("output.ll")