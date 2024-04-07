import { Component, OnInit, ViewChild } from '@angular/core';
import { Subscription } from 'rxjs'; 
import { TerminalService } from 'primeng/terminal'; 
import { CompilerServiceService } from '../compiler-service.service';
import { CrosscallService } from '../crosscall.service';

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
  clickEventsubscription!:Subscription 
  fileBlob !: Blob
  file = new File (["Text"],"gen.z");
  
  
  constructor(public terminalService: TerminalService, private compiler: CompilerServiceService, private crosscallservice:CrosscallService) { 
    this.terminalService.commandHandler.subscribe(command => { 
      this.checkCommand(command)//function that calls functions, see case
    }); 
    this.clickEventsubscription = this.crosscallservice.getClickEvent().subscribe((data)=>{
      this.runProgram();
    })
  }


  checkCommand(command: string) {
    //execute actual useful functions here and place the output into response
    console.log(command)
      switch (command) {
        case "run":
            this.runProgram()
          break;

        case "break":
          this.response = 'Stopping code'
          this.terminalService.sendResponse(this.response); 
          break;
      
        default:
          this.response = "'"+ command + "' is not recognized as an internal command."
          this.terminalService.sendResponse(this.response); 
          break;
      }
    
  }

  runProgram() {
    console.log("Running program")
    /*this.compiler.getDatawithoutsub().subscribe(async (res) => {
      this.response = JSON.stringify(res);
      await this.terminalService.sendResponse(this.response); 
    })*/

    console.log("Editor data", this.crosscallservice.getEditorData())
    this.file = new File ([this.crosscallservice.getEditorData()],"gen.z");
    this.compiler.compileFIle(this.file).subscribe(async (res) => {
      await this.stringifyJSON(res);
      console.log(res)
      //await this.terminalService.sendResponse(this.response); 
    })
  }

  stringifyJSON(res : Object){
    this.response = JSON.stringify(res);
  }

  


  //have topbar button run the code/function that pulls the text from the editor  and parses it then places the output into this.response then executes "this.terminalService.sendResponse(this.response); "
}
