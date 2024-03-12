# APL-Group-project-2024

## Literals

    <literal> ::= '"' <string> '"' | <float> | <int>
    <type> ::= String | int | char | float
    
    <string> ::= {<string>}+ | {<char>}+ | {<int>}+ 
    <char> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
    <float> ::= <int>*.<int>+
    <int> ::= {<num>}+
    <num> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0

## Statement

    <statement> ::= <selection-statement> | <return-statement>
    
    <selection-statement> ::= isItReally ( <expression> ) bet '{' <statement> '}' | isItReally ( <expression> ) bet '{' <statement> '}' orIsIt  '{' <statement> '}'
    
    <return-statement> ::= sayLess | sayLess <identifier> | sayLess <literal>

## Expression

    <expression> ::= <expression> | <expression> {<expression>}? | ( <expression> ) | <statement>
    
## Declaration
    
    <type-declaration> ::= <type> <identifier> | <type> <identifier> '=' <literal>
    
    <function-declaration> ::= <type> <identifier> '{' <expression> <return-statement> '}'

# Tokens

OPN_BRC ::= (

CLSD_BRC ::= )

OPN_C_BRC ::= {

CLSD_C_BRC ::= }

TERMINATOR ::= .

SQUOTE ::= '

SQUOTE ::= "

