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

    this.geminiSub = this.geminiService.getGeminiCode().subscribe(async value =>{
      console.log(value)
      await this.loadGeminiFile(true,value);
    })
  }



  runProgram() {
    this.crosscallService.sendClickEvent();
  }

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
    this.http.get(this.file_url + file, {responseType: 'text'} )
        .subscribe(data => {
          this.file.push( {
            title: "file#" + (1+this.file.length) +".z",
            model: {
              language: 'c',
              uri: 'main.json',
              value: data
            }
          });
          if (selectAfterAdding) {
            if (this.file.length == 0) {
              this.selected = (this.file.length);
            } else {
              this.selected = (this.file.length-1);
            }
            
          }
        });
    
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
