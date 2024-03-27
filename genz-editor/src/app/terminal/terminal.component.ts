import { Component, ViewChild } from '@angular/core';
import { Subscription } from 'rxjs'; 
import { TerminalService } from 'primeng/terminal'; 

@Component({
  selector: 'app-terminal',
  templateUrl: './terminal.component.html',
  styleUrl: './terminal.component.scss', 
  providers: [TerminalService] 
})
export class TerminalComponent {
  subscription!: Subscription; 
  response: string = "";
  parserOutput: string = "This is the Parsers output";
  
  
  constructor(private terminalService: TerminalService) { 
    this.terminalService.commandHandler.subscribe(command => { 
      this.checkCommand(command)//function that calls functions, see case
    }); 
  }


  checkCommand(command: string) {
    //execute actual useful functions here and place the output into response
    console.log(command)
      switch (command) {
        case "run":
          
          //function to parse code

          //command to print parser output, swap text for variable with text
          this.response = this.parserOutput
          break;

        case "break":
          this.response = 'Stopping code'
          break;
      
        default:
          this.response = "'"+ command + "' is not recognized as an internal command."
          break;
      }
    this.terminalService.sendResponse(this.response); 
  }

  //have topbar button run the code/function that pulls the text from the editor  and parses it then places the output into this.response then executes "this.terminalService.sendResponse(this.response); "
}
