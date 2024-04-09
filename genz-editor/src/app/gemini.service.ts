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

  grammarPrompt = 'using this ebnf "<program> ::= <statements> <statements> ::= <statement> <statements> | <statement> <block_statements> ::= <block_statement> <block_statements> | <block_statement> <statement> ::= <=ment> | <isItReally_statement> | <while_statement> | <return_statement> | <print_statement> | <var_declaration> | <initialization> | <function_declaration> | <function_call> <return_statement> ::= sayLess <expression> . <print_statement> ::= print ( <expression> ) . <while_statement> ::= while ( <conditional_expression> ) { <statements> } <expression> ::= <math-expression> . | <function-expression> . <math-expression> ::= {<num-literal> | <identisItReallyier>} BINARY_OPERATor {<num-literal> | <identisItReallyier>} | {<num-literal> | <identisItReallyier>} BINARY_OPERATor <math-expression> | {<num-literal> | <identisItReallyier>} BINARY_OPERATor OPN_BRC <math-expression> CLSD_BRC <function-expression> ::= <identisItReallyier> OPN_BRC {{<identisItReallyier> | <literal>}{ SEPARATor {<identisItReallyier> | <literal> }}*}* CLSD_BRC <conditional_expression> ::= fax | cap | <expression> > <expression> | <expression> < <expression> | <expression> GREATER_THAN_== <expression> | <expression> <_== <expression> | <expression> == <expression> | <expression> not_== <expression> | <expression> AND <expression> | <expression> or <expression> | not <expression> <expression> ::= <conditional_expression> | <expression> + <expression> | <expression> - <expression> | <expression> * <expression> | <expression> / <expression> | NUMBER <expression> ::= <identisItReallyier> | ( <expression> ) <function_declaration> ::= <data_type> IDENTisItReallyIER ( <parameters> ) { <block_statements> } | <data_type> IDENTisItReallyIER ( ) { <block_statements> } <parameters> ::= <parameter> , <parameters> | <parameter> <parameter> ::= <data_type> IDENTisItReallyIER <var_declaration> ::= <data_type> IDENTisItReallyIER . <=ment> ::= IDENTisItReallyIER = <expression> . | IDENTisItReallyIER = <function_call> <initialization> ::= <data_type> IDENTisItReallyIER = <expression> . | <data_type> IDENTisItReallyIER = <function_call> <identisItReallyier> ::= IDENTisItReallyIER <function_call> ::= IDENTisItReallyIER ( <arguments> ) . | IDENTisItReallyIER ( ) . <arguments> ::= <arguments> , <arguments> | <argument> <argument> ::= <expression> <isItReally_statement> ::= isItReally ( <conditional_expression> ) { <block_statements> } | isItReally ( <conditional_expression> ) { <block_statements> } orIsIt { <block_statements> }" '
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
