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

  grammarPrompt = "Using this programming language grammar # <program> ::= <statements> <statements> ::= <statement> <statements>    | <statement> <blockstatements> ::= <block_statement> <block_statements>       | <block_statement> <statement> ::= <assignment>   | <if_statement>   | <while_statement>  | <return_statement>  | <print_statement>   | <var_declaration> | <initialization>  | <function_declaration>   | <function_call> <function_declaration> ::= <data_type> IDENTIFIER OPEN_PAREN <parameters> CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE  | <data_type> IDENTIFIER OPEN_PAREN CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE <parameters> ::= <parameter> COMMA <parameters>  | <parameter> <parameter> ::= <data_type> IDENTIFIER <function_call> ::= IDENTIFIER OPEN_PAREN <arguments> CLOSE_PAREN TERMINATOR | IDENTIFIER OPEN_PAREN CLOSE_PAREN TERMINATOR <arguments> ::= <arguments> COMMA <arguments> | <argument> <argument> ::= <expression> <data_type> ::= TYPE_INT   | TYPE_VOID  | TYPE_BOOLEAN <assignment> ::= IDENTIFIER ASSIGN <expression> TERMINATOR | IDENTIFIER ASSIGN <function_call> <initialization> ::= <data_type> IDENTIFIER ASSIGN <expression> TERMINATOR | <data_type> IDENTIFIER ASSIGN <function_call> <if_statement> ::= IF OPEN_PAREN <conditional_expression> CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE   | IF OPEN_PAREN <conditional_expression> CLOSE_PAREN OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE ELSE OPEN_CURL_BRACE <block_statements> CLOSE_CURL_BRACE <while_statement> ::= WHILE OPEN_PAREN <conditional_expression> CLOSE_PAREN OPEN_CURL_BRACE <statements> CLOSE_CURL_BRACE <var_declaration> ::= <data_type> IDENTIFIER TERMINATOR <return_statement> ::= RETURN <expression> TERMINATOR <print_statement> ::= PRINT OPEN_PAREN <expression> CLOSE_PAREN TERMINATOR <conditional_expression> ::= TRUE   | FALSE     | <expression> GREATER_THAN <expression> | <expression> LESS_THAN <expression>   | <expression> GREATER_THAN_EQUALS <expression>   | <expression> LESS_THAN_EQUALS <expression>    | <expression> EQUALS <expression>   | <expression> NOT_EQUALS <expression>   | <expression> AND <expression>     | <expression> OR <expression>   | NOT <expression> <expression> ::= <conditional_expression>   | <expression> SUM <expression>   | <expression> SUB <expression>    | <expression> MUL <expression>    | <expression> DIV <expression>   | NUMBER <identifier> ::= IDENTIFIER <expression> ::= <identifier>   | OPEN_PAREN <expression> CLOSE_PAREN PRINT r'print' OPEN_PAREN r'(' CLOSE_PAREN r')' OPEN_CURL_BRACE r'{' CLOSE_CURL_BRACE r'}' SUM r'+' SUB r'-' MUL r'*' DIV r'/' NUMBER r'\d+' TRUE r'fax' FALSE r'cap' EQUALS r'==' NOT_EQUALS r'!=' GREATER_THAN_EQUALS r'>=' LESS_THAN_EQUALSr'<=' GREATER_THANr'>' LESS_THAN r'<' TERMINATOR r'.' COMMA r',' ASSIGN r'=' IF r'isItReally' ELSE r'orIsIt' WHILE r'while' AND r'and' OR r'or' NOT r'not' RETURN r'sayLess' TYPE_INT r'int' TYPE_VOID r'void' TYPE_BOOLEAN r'bool' IDENTIFIER r'[a-zA-Z][a-zA-Z0-9_]*'"

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
