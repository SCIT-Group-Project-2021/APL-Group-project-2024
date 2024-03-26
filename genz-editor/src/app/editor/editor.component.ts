import { Component, Input } from '@angular/core';
import { CodeModel } from '@ngstack/code-editor';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrl: './editor.component.scss'
})
export class EditorComponent {

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
    console.log('CODE', value);
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

}
