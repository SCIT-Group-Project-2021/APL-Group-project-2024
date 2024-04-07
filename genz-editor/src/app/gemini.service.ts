import { Injectable } from '@angular/core';
import { GoogleGenerativeAI } from '@google/generative-ai';
import { BehaviorSubject, Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GeminiService {
  private genAI : GoogleGenerativeAI;
  private messageHistory : BehaviorSubject<any> = new BehaviorSubject(null);
  private loadFile = new Subject<any>();

  grammarPrompt = "Using this programming language grammar # Program <file> ::= <program-dec> <program-dec> ::= programName <identifier> OPN_C_BRC <statements> <return-statement> CLSD_C_BRC ## Literals <literal> ::= DQUOTE <string> DQUOTE | <bool> | <num-literal> <num-literal> ::= <float> | <int> <type> ::= String | int | char | float <bool> ::= TRUE | FALSE    <string> ::= <string>+ | <char>+ | <int>+ <char> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z <float> ::= <int>* INT_SEPARATOR <int>+ <int> ::= <num>+ <num> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ## Statement <statements> ::= <statement>+ <statement> ::= <selection-statement> | <return-statement> | <iteratation-statement> | <declaration-statement> | <expression> <selection-statement> ::= <if-selection> | <switch-selection> <iteratation-statement> ::= <for-loop> | <while-loop> <declaration-statement> ::= <type-declaration> TERMINATOR | <function-declaration> <return-statement> ::= RETURN TERMINATOR | <identifier> RETURN TERMINATOR | <literal> RETURN TERMINATOR ## Loop <for-loop> ::= FOR_OP OPN_BRC <statements> CLSD_BRC OPN_C_BRC <statements> CLSD_C_BRC <while-loop> ::= WHILE_OP OPN_BRC <statements> CLSD_BRC OPN_C_BRC <statements> CLSD_C_BRC ## Expression <expression> ::= <math-expression> TERMINATOR | <function-expression> TERMINATOR <math-expression> ::= {<num-literal> | <identifier>} BINARY_OPERATOR {<num-literal> | <identifier>} | {<num-literal> | <identifier>} BINARY_OPERATOR <math-expression> | {<num-literal> | <identifier>} BINARY_OPERATOR OPN_BRC <math-expression> CLSD_BRC <function-expression> ::= <identifier> OPN_BRC {{<identifier> | <literal>}{ SEPARATOR {<identifier> | <literal> }}*}* CLSD_BRC ## Declaration <type-declaration> ::= <type> <identifier> TERMINATOR | <type> <identifier> EQUAL <literal> TERMINATOR <function-declaration> ::= <type> <identifier>  OPN_BRC {<type-declaration>{ SEPARATOR <type-declaration>}*}* CLSD_BRC OPN_C_BRC <statements> <return-statement> CLSD_C_BRC <identifier> ::= <string> ## Selection <if-selection> ::= IF OPN_BRC <statements> CLSD_BRC THEN OPN_C_BRC <statement> CLSD_C_BRC | IF OPN_BRC <statements> CLSD_BRC THEN OPN_C_BRC <statements> CLSD_C_BRC ELSE OPN_C_BRC <statements> CLSD_C_BRC <switch-selection> ::= SWITCH OPN_BRC <identifier> CLSD_BRC { option <identifier> OPN_C_BRC <statement> CLSD_C_BRC }+ # Tokens OPN_BRC ::= ( CLSD_BRC ::= ) OPN_C_BRC ::= { CLSD_C_BRC ::= } TERMINATOR ::= . SQUOTE ::= ' DQUOTE ::= ' INT_SEPARATOR ::= . SEPARATOR ::= , EQUAL ::= = MULTIPLY ::= * DIVIDE ::= / ADD ::= + SUB ::= - TRUE ::= fax FALSE ::= cap IF ::= isItReally THEN ::= bet ELSE ::= orIsIt RETURN ::= sayLess TERMINATOR ::= . SWITCH ::=  FOR_OP ::= WHILE_OP ::="

  constructor() { 
    this.genAI = new GoogleGenerativeAI('AIzaSyCZnnYgtgKRWydbuC9BKfmQ8zlfNTfttTQ');
  }

  async generateText(prompt : string) {
    const model = this.genAI.getGenerativeModel({model: 'gemini-pro'});
    this.messageHistory.next({
      from: 'user',
      message: prompt
    });

    prompt = this.grammarPrompt + prompt;
    
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    this.loadFile.next(text);
    

    this.messageHistory.next({
      from: 'bot',
      message: text
    })

  }


  getGeminiCode(): Observable<any>{ 
    return this.loadFile.asObservable();
  }


  public getMessageHistory(): Observable<any> {
    return this.messageHistory.asObservable();
  }
}
