import { Component, inject } from '@angular/core';
import { OpenAiService } from '../open-ai.service';
import { GeminiService } from '../gemini.service';

@Component({
  selector: 'app-chatpanel',
  templateUrl: './chatpanel.component.html',
  styleUrl: './chatpanel.component.scss'
})

/*const openai = new OpenAIApi ( new Configuration({
  apiKey: process.env.API_KEY
}))*/
export class ChatpanelComponent {

  userInput: string = '';
  prompt: string = '';

  geminiService : GeminiService = inject(GeminiService);

  chatHistory : any[] = [];
  constructor() {
    this.geminiService.getMessageHistory().subscribe(res =>{
      if(res){
        this.chatHistory.push(res);
      }
    })
  }

  sendMessage(){
    if(this.prompt){
      this.geminiService.generateText(this.prompt);
    }
  }

}
