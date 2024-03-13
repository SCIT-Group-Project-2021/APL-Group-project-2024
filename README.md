# APL-Group-project-2024

# Program

    <file> ::= <program-dec>
    
    <program-dec> ::= programName <identifier> OPN_C_BRC <statements> <return-statement> CLSD_C_BRC

## Literals

    <literal> ::= DQUOTE <string> DQUOTE | <bool> | <num-literal>

    <num-literal> ::= <float> | <int>
    
    <type> ::= String | int | char | float

    <bool> ::= TRUE | FALSE    
    
    <string> ::= <string>+ | <char>+ | <int>+ 
    
    <char> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
    
    <float> ::= <int>* INT_SEPARATOR <int>+
    
    <int> ::= <num>+
    
    <num> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0
    
## Statement

    <statements> ::= <statement>+

    <statement> ::= <selection-statement> | <return-statement> | <iteratation-statement> | <declaration-statement> | <binding-statement>
    
    <selection-statement> ::= <if-selection> | <switch-selection>
    
    <iteratation-statement> ::= <for-loop> | <while-loop>

    <declaration-statement> ::= <type-declaration> TERMINATOR | <function-declaration>
    
    <return-statement> ::= RETURN | <identifier> RETURN | <literal> RETURN

## Loop

    <for-loop> ::= FOR_OP OPN_BRC <statements> CLSD_BRC OPN_C_BRC <statements> CLSD_C_BRC

    <while-loop> ::= WHILE_OP OPN_BRC <statements> CLSD_BRC OPN_C_BRC <statements> CLSD_C_BRC

## Expression
    
    <expression> ::= <math_expression>

    <math_expression> ::= {<num-literal> | <identifier>} BINARY_OPERATOR {<num-literal> | <identifier>} | {<num-literal> | <identifier>} BINARY_OPERATOR <math_operation> | {<num-literal> | <identifier>} BINARY_OPERATOR OPN_BRC <math_operation> CLSD_BRC

    
## Declaration
    
    <type-declaration> ::= <type> <identifier> | <type> <identifier> EQUAL <literal>
    
    <function-declaration> ::= <type> <identifier>  OPN_BRC {<type-declaration>{ , <type-declaration>*}}* CLSD_BRC OPN_C_BRC <statements> <return-statement> CLSD_C_BRC

    <identifier> ::= <string>

## Binding

    <assignment> ::= <identifier> EQUAL { <literal> | <identifier> | <operation }

## Selection
    
    <if-selection> ::= IF OPN_BRC <statements> CLSD_BRC THEN OPN_C_BRC <statement> CLSD_C_BRC | IF OPN_BRC <statements> CLSD_BRC bet OPN_C_BRC <statements> CLSD_C_BRC ELSE OPN_C_BRC <statements> CLSD_C_BRC

    <switch-selection> ::= SWITCH OPN_BRC <identifier> CLSD_BRC { option <identifier> OPN_C_BRC <statement> CLSD_C_BRC }+

## Operation

    

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

    SWITCH ::=

    FOR_OP ::=

    WHILE_OP ::=
