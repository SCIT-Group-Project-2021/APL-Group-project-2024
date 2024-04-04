import { Component } from '@angular/core';
import { OpenAiService } from '../open-ai.service';

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
  chatHistory: string[] = [];

  constructor(private chatService: OpenAiService) {}

  sendMessage(): void {
    if (this.userInput.trim() === '') {
      return;
    }
    this.chatHistory.push(this.userInput);
    this.chatService.sendMessage(this.userInput).subscribe(response => {
      this.chatHistory.push(response.data.choices[0].text.trim());
    });
    this.userInput = '';
  }

}
