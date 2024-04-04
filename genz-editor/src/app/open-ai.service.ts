import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OpenAiService {

  private openAIUrl = 'https://api.openai.com/v1/completions';
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'Bearer YOUR_OPENAI_API_KEY' // Replace with your OpenAI API key
    })
  };

  constructor(private http: HttpClient) {}

  sendMessage(message: string): Observable<any> {
    const requestBody = {
      model: 'davinci', // Or whichever ChatGPT model you prefer
      prompt: message,
      max_tokens: 150,
      temperature: 0.7,
      n: 1
    };

    return this.http.post(this.openAIUrl, requestBody, this.httpOptions);
  }
}
