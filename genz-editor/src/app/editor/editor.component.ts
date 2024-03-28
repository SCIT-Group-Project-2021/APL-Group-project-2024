import { Component, Input } from '@angular/core';
import { CodeModel } from '@ngstack/code-editor';
import saveAs from 'file-saver';
import { CrosscallService } from '../crosscall.service';
import { File } from 'buffer';
import { Subscription } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrl: './editor.component.scss'
})
export class EditorComponent {

  readonly file_url = 'assets/exampleFiles/'

  clickEventsubscription!:Subscription 
  
  constructor(private crosscallService:CrosscallService,private http: HttpClient) { 
    this.clickEventsubscription = this.crosscallService.getloadFileEvent().subscribe((value)=>{
      console.log(value)
      this.loadFile(true,value);
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
  
  onCodeChanged(value: any) {
    console.log(value);
    this.file[this.selected].model.value = value
  }
  selected = 0;

  addTab(selectAfterAdding: boolean) {
    this.file.push( {
      title: "file#" + (1+this.file.length) +".z",
      model: {
        language: 'html',
        uri: 'main.json',
        value: ''
      }
    });

    if (selectAfterAdding) {
      this.selected = (this.file.length - 1);
    }
  }

  loadFile(selectAfterAdding: boolean,file?: any) {
    this.http.get(this.file_url + file, {responseType: 'text'} )
        .subscribe(data => {
          console.log(data)
          this.file.push( {
            title: "file#" + (1+this.file.length) +".z",
            model: {
              language: 'c',
              uri: 'main.json',
              value: data
            }
          });
        });
    

    if (selectAfterAdding) {
      this.selected = (this.file.length-1);
    }
  }

  removeTab(index: number) {
    this.file.splice(index, 1);
    this.selected = index;
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
