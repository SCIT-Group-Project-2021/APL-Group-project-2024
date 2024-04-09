import { Component, Input } from '@angular/core';
import { CodeModel } from '@ngstack/code-editor';
import saveAs from 'file-saver';
import { CrosscallService } from '../crosscall.service';
import { File } from 'buffer';
import { Subscription } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { GeminiService } from '../gemini.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrl: './editor.component.scss'
})
export class EditorComponent {

  readonly file_url = 'assets/exampleFiles/'

  clickEventsubscription!:Subscription
  geminiSub!:Subscription
  
  constructor(private crosscallService:CrosscallService, private geminiService: GeminiService, private http: HttpClient) { 
    this.clickEventsubscription = this.crosscallService.getloadFileEvent().subscribe((value)=>{
      console.log(value)
      this.loadFile(true,value);
    })
    this.clickEventsubscription = this.crosscallService.getloadUploadFileEvent().subscribe((value)=>{
      console.log(value)
      this.loadUploadFile(true,value[0],value[1]);
    })

    this.geminiSub = this.geminiService.getGeminiCode().subscribe(async value =>{
      console.log(value)
      await this.loadGeminiFile(true,value);
    })
  }

  runProgram() {
    this.crosscallService.sendClickEvent();
  }

  examplefile = [
    {
      title: "datatypes_example.z",
      model: {
        language: 'c',
        uri: 'main.json',
        value: 'int b.\r\nint a = 2.\r\nb = 4.\r\nprint(b * 2).\r\n'
      }
    },
    {
      title: "if_example.z",
      model: {
        language: 'c',
        uri: 'main.json',
        value: 'int age = 21.\r\nbool isMale = fax.\r\nisItReally ((age >= 18) and isMale) {\r\n    print(fax).\r\n} orIsIt {\r\n    print(cap).\r\n}'
      }
    },
    {
      title: "print_example2.z",
      model: {
        language: 'c',
        uri: 'main.json',
        value: 'print(1 == 1).\r\nprint(1 != 1).\r\nprint(2 > 3).\r\nprint(5 < 10).\r\nprint(21 >= 18).\r\nprint(21 <= 18).'
      }
    },
    {
      title: "function_return.z",
      model: {
        language: 'c',
        uri: 'main.json',
        value: 'int Sum(int a, int b) {\r\n    sayLess a + b.\r\n}\r\nint res = Sum(2,4).\r\nprint(res).'
      }
    }
  ]

  file = [
    {
      title: "First.html",
      model: {
        language: 'html',
        uri: 'main.json',
        value: 'Html Test File'
      }
    }
  ]

  theme = 'vs-dark';

  model = this.file[0].model

  options = {
    contextmenu: true,
    minimap: {
      enabled: true
    }
  };

  selected = this.file.length-1;
  
  onCodeChanged(value: any) {
    try {
      this.file[this.selected].model.value = value
      this.crosscallService.sendEditorData(this.file[this.selected].model.value)
      console.log("We have updated Data");
    } catch (error) {
      console.log("No data to swap to");
    }
    
  }


  loadGeminiFile(selectAfterAdding: boolean, response : string) {
    this.file.push( {
      title: "gemini response #" + (1+this.file.length) +".z",
      model: {
        language: 'c',
        uri: 'main.json',
        value: response.slice(3,-3)
      }
    });
    if (selectAfterAdding) {
      if (this.file.length == 0) {
        this.selected = (this.file.length);
      } else {
        this.selected = (this.file.length-1);
      }
      
    }
  }

  addTab(selectAfterAdding: boolean) {
    this.file.push( {
      title: "file#" + (1+this.file.length) +".z",
      model: {
        language: 'html',
        uri: 'main.json',
        value: ''
      }
    });
    console.log("Created new Tab");

    if (selectAfterAdding) {
      this.selected = (this.file.length - 1);
    }
    if (this.file.length-1 == 0) {
      this.selected = (this.file.length);
      console.log("Empty to new Tab");
    }
  }

  loadFile(selectAfterAdding: boolean,file?: any) {

    const selectedFile = this.examplefile.find((item) => item.title === file);
    const value = selectedFile?.model.value ?? '';
    {
          this.file.push( {
            title: file,
            model: {
              language: 'c',
              uri: 'main.json',
              value: value
            }
          });
          if (selectAfterAdding) {
            if (this.file.length == 0) {
              this.selected = (this.file.length);
            } else {
              this.selected = (this.file.length-1);
            }
            
          }
        }    
  }

  loadUploadFile(selectAfterAdding: boolean, filetitle: string,filedata: string) {
    this.file.push( {
      title: filetitle,
      model: {
        language: 'c',
        uri: 'main.json',
        value: filedata
      }
    });
    if (selectAfterAdding) {
      if (this.file.length == 0) {
        this.selected = (this.file.length);
      } else {
        this.selected = (this.file.length-1);
      } 
    }    
  }

  removeTab(index: number) {
    this.file.splice(index, 1);
    try {
      this.selected = this.file.length-1;
      if (this.file.length == 0) {
        this.model = {
          language: 'html',
          uri: 'main.json',
          value: ''
        }
    }
    } catch (error) {
      
    }
    
  }

  swapEditor(x:number){
    try {
      if (x < this.file.length) {
        var newData = this.file[x].model;
        console.log('swapping')
        console.log(newData)
        this.model = JSON.parse(JSON.stringify(newData));
      } else {
        var newData = {
          language: 'html',
          uri: 'main.json',
          value: ''
        }
        console.log('resetting')
        this.model = JSON.parse(JSON.stringify(newData));
      }
      
    } catch (error) {
      
    }
    
 }

  printIndex(x:number) {
    console.log('Current index = ', x, "final index = ", this.file.length)
  }

  saveFile() {
    const blob = 
        new Blob(
          [this.file[this.selected].model.value], 
                 {type: "text/plain;charset=utf-8"});
    saveAs(blob, this.file[this.selected].title +'.txt');

  }



}
