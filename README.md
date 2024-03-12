# APL-Group-project-2024

## Literals

    <literal> ::= DQUOTE <string> DQUOTE | <float> | <int>
    <type> ::= String | int | char | float
    
    <string> ::= <string>+ | {<char>}+ | {<int>}+ 
    <char> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
    <float> ::= <int>* INT_SEPARATOR <int>+
    <int> ::= <num>+
    <num> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0

## Statement

    <statement> ::= <selection-statement> | <return-statement>
    
    <selection-statement> ::= isItReally OPN_BRC <expression> CLSD_BRC bet OPN_C_BRC <statement> CLSD_C_BRC | isItReally OPN_BRC <expression> CLSD_BRC bet OPN_C_BRC <statement> CLSD_C_BRC orIsIt OPN_C_BRC <statement> CLSD_C_BRC
    
    <return-statement> ::= sayLess | sayLess <identifier> | sayLess <literal>

## Expression

    <expression> ::= <expression> | <expression> {<expression>}? | OPEN_BRC <expression> CLSD_BRC | <statement>
    
## Declaration
    
    <type-declaration> ::= <type> <identifier> | <type> <identifier> EQUAL <literal>
    
    <function-declaration> ::= <type> <identifier> OPN_C_BRC <expression> <return-statement> CLSD_C_BRC

# Tokens

OPN_BRC ::= (

CLSD_BRC ::= )

OPN_C_BRC ::= {

CLSD_C_BRC ::= }

TERMINATOR ::= .

SQUOTE ::= '

SQUOTE ::= "

INT_SEPARATOR ::= .

EQUAL ::= =

MULTIPLY ::= *

ADD ::= +

SUB ::= -

IF ::= isItReally

ELSE - or is it
Then - bet
Return - say less
; - . (Period)
True - fax
False - cap
