
<file> ::= <program-dec>
<program-dec> ::= programName <identifier> OPN_C_BRC <statements> <return-statement> CLSD_C_BRC
    programName program1 {
        <statements>
            <statement>
                <type-declaration>.
                    <type> <identifier> EQUAL <literal> TERMINATOR
                        int num1 = 14.

            <statement>
                <type-declaration>.
                    <type> <identifier> TERMINATOR
                        int x.

            <statement>
                <expression>
                    <function-expression> TERMINATOR
                        <identifier> OPN_BRC {{<identifier> | <literal>}{ , {<identifier> | <literal> }}*}* CLSD_BRC .
                                multiply (13,14).

            <statement>
                <function-declaration>
                    <type> <identifier>  OPN_BRC {<type-declaration>{ , <type-declaration>}*}* CLSD_BRC OPN_C_BRC <statements> <return-statement> CLSD_C_BRC
                        int multiply (int num1 = 0, int num2) {

                            <statements>
                                <statement>
                                    <binding-statement>
                                        <assignment> ::= <identifier> EQUAL { <literal> | <identifier> | <expression> }
                                            x = <math_expression> TERMINATOR
                                                {<num-literal> | <identifier>} BINARY_OPERATOR {<num-literal> | <identifier>} | {<num-literal> | <identifier>} BINARY_OPERATOR <math_expression> | {<num-literal> | <identifier>} BINARY_OPERATOR OPN_BRC <math_expression> CLSD_BRC .
                                                    num1 + (2 * 34).
                            <return-statement>
                                x sayLess.
                        }
        
        
        <return-statement>
            sayLess.
    }

programName program1 {

int num1 = 14.

int x.

multiply (13,14).

int multiply (int num 1, int num2) {

    x = num1 + (2 * 34).

    x sayLess.
}

sayLess.
}
