from lexer import Lexer
from parser_1 import Parser
from codegen import CodeGen

fname = "input.z"
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

print(parse_tree)
for statement in parse_tree:
    statement.eval()

codegen.create_ir()
codegen.save_ir("output.ll")