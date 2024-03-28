import { Component, OnInit, ViewChild } from '@angular/core';
import { Subscription } from 'rxjs'; 
import { TerminalService } from 'primeng/terminal'; 
import { CompilerServiceService } from '../compiler-service.service';

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
  compilerOutput: any;
  
  
  constructor(private terminalService: TerminalService, private compiler: CompilerServiceService) { 
    this.terminalService.commandHandler.subscribe(command => { 
      this.checkCommand(command)//function that calls functions, see case
    }); 
  }

  checkCommand(command: string) {
    //execute actual useful functions here and place the output into response
    console.log(command)
      switch (command) {
        case "run":

          this.compiler.getDatawithoutsub().subscribe(async (res) => {
            this.response = JSON.stringify(res);
            await this.terminalService.sendResponse(this.response); 
          })
          
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
