# APL-Group-project-2024

# Program

    <file> ::= <program-dec>
    
    <program-dec> ::= <identifier> OPN_BRC <expression> CLSD_BRC

## Literals

    <literal> ::= DQUOTE <string> DQUOTE | <bool> | <float> | <int>
    
    <type> ::= String | int | char | float

    <bool> ::= TRUE | FALSE    
    
    <string> ::= <string>+ | {<char>}+ | {<int>}+ 
    
    <char> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
    
    <float> ::= <int>* INT_SEPARATOR <int>+
    
    <int> ::= <num>+
    
    <num> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0
    
## Statement

    <statements> ::= <statement>+

    <statement> ::= <selection-statement> | <return-statement> | <iteratation-statement>
    
    <selection-statement> ::= IF OPN_BRC <expression> CLSD_BRC THEN OPN_C_BRC <statement> CLSD_C_BRC | IF OPN_BRC <expression> CLSD_BRC bet OPN_C_BRC <statements> CLSD_C_BRC ELSE OPN_C_BRC <statements> CLSD_C_BRC

    <iteratation-statement> ::= <for-loop> | <while-loop>

    <declaration-statement> ::= <type-declaration> | <function-declaration>
    
    <return-statement> ::= RETURN | RETURN <identifier> | RETURN <literal>

## Loop

    <for-loop> ::= for OPN_BRC <expression> CLSD_BRC OPN_C_BRC <statements> CLSD_C_BRC

    <while-loop> ::= while OPN_BRC <expression> CLSD_BRC OPN_C_BRC <statements> CLSD_C_BRC

## Expression

    <expression> ::= <expression> | OPEN_BRC <expression> CLSD_BRC | <statements>
    
## Declaration
    
    <type-declaration> ::= <type> <identifier> | <type> <identifier> EQUAL <literal>
    
    <function-declaration> ::= <type> <identifier> OPN_C_BRC <expression> <return-statement> CLSD_C_BRC

    <identifier> ::= <string>

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
    
    TRUE ::= fax
    
    FALSE ::= cap
    
    IF ::= isItReally
    
    THEN ::= bet
    
    ELSE ::= orIsIt
    
    RETURN ::= sayLess
    
    TERMINATOR ::= . 
    
