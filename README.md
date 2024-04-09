# APL-Group-project-2024

# EBNF

    <program> ::= <statements>

    <statements> ::= <statement> <statements> | <statement>

    <block_statements> ::= <block_statement> <block_statements> | <block_statement>
    
    <statement> ::= <assignment> | <if_statement> | <while_statement> | <return_statement> | <print_statement> | <var_declaration> | <initialization> | <function_declaration> | <function_call>

    <return_statement> ::= RETURN <expression> TERMINATOR

    <print_statement> ::= PRINT OPEN_PAREN <expression> CLOSE_PAREN TERMINATOR

    <while_statement> ::= WHILE OPEN_PAREN <conditional_expression> CLOSE_PAREN OPEN_CURL_BRACE <statements> CLOSE_CURL_BRACE

    <expression> ::= <math-expression> TERMINATOR | <function-expression> TERMINATOR

    <math-expression> ::= {<num-literal> | <identifier>} BINARY_OPERATOR {<num-literal> | <identifier>} | {<num-literal> | <identifier>} BINARY_OPERATOR <math-expression> | {<num-literal> | <identifier>} BINARY_OPERATOR OPN_BRC <math-expression> CLSD_BRC

    <function-expression> ::= <identifier> OPN_BRC {{<identifier> | <literal>}{ SEPARATOR {<identifier> | <literal> }}*}* CLSD_BRC

    <conditional_expression> ::= TRUE | FALSE | <expression> GREATER_THAN <expression> | <expression> LESS_THAN <expression> | <expression> GREATER_THAN_EQUALS <expression> | <expression> LESS_THAN_EQUALS <expression> | <expression> EQUALS <expression> | <expression> NOT_EQUALS <expression> | <expression> AND <expression> | <expression> OR <expression> | NOT <expression>

    <expression> ::= <conditional_expression> | <expression> SUM <expression> | <expression> SUB <expression> | <expression> MUL <expression> | <expression> DIV <expression> | NUMBER

    <expression> ::= <identifier> | OPEN_PAREN <expression> CLOSE_PAREN

    <function_declaration> ::= <data_type> IDENTIFIER OPEN_PAREN <parameters> CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE | <data_type> IDENTIFIER OPEN_PAREN CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE

    <parameters> ::= <parameter> COMMA <parameters> | <parameter>

    <parameter> ::= <data_type> IDENTIFIER

    <var_declaration> ::= <data_type> IDENTIFIER TERMINATOR

    <assignment> ::= IDENTIFIER ASSIGN <expression> TERMINATOR | IDENTIFIER ASSIGN <function_call>
    
    <initialization> ::= <data_type> IDENTIFIER ASSIGN <expression> TERMINATOR | <data_type> IDENTIFIER ASSIGN <function_call>

    <identifier> ::= IDENTIFIER

    <function_call> ::= IDENTIFIER OPEN_PAREN <arguments> CLOSE_PAREN TERMINATOR | IDENTIFIER OPEN_PAREN CLOSE_PAREN TERMINATOR

    <arguments> ::= <arguments> COMMA <arguments> | <argument>

    <argument> ::= <expression>
    
    <if_statement> ::= IF OPEN_PAREN <conditional_expression> CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE | IF OPEN_PAREN <conditional_expression> CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE ELSE OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE
  
# Tokens

    PRINT ::= print

    OPEN_PAREN ::= (
    
    CLOSE_PAREN ::= )
    
    OPEN_CURL_BRACE ::= {
    
    CLOSE_CURL_BRACE ::= }

    NUMBER ::= d+
    
    TERMINATOR ::= .

    COMMA ::= ,

    ASSIGN  ::= =   
    
    EQUAL ::= =

    EQUALS ::= ==

    NOT_EQUALS ::= !=

    GREATER_THAN_EQUALS ::= >=

    LESS_THAN_EQUALS ::= <=

    GREATER_THAN ::= >

    LESS_THAN ::= <
    
    MUL ::= *

    DIV ::= /
    
    SUM ::= +
    
    SUB ::= -
    
    TRUE ::= fax
    
    FALSE ::= cap
    
    IF ::= isItReally
    
    THEN ::= bet
    
    ELSE ::= orIsIt

    WHILE ::= while

    OR ::= or

    NOT ::= not
    
    RETURN ::= sayLess
    
    TERMINATOR ::= . 

    TYPE_INT ::= int

    TYPE_VOID ::= void

    TYPE_BOOLEAN ::= bool

    IDENTIFIER ::= [a-zA-Z_][a-zA-Z0-9_]