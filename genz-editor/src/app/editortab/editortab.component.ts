import { Component } from '@angular/core';
import { CodeModel } from '@ngstack/code-editor';

@Component({
  selector: 'app-editortab',
  templateUrl: './editortab.component.html',
  styleUrl: './editortab.component.scss'
})
export class EditortabComponent {

  
  theme = 'vs-dark';
  
  model: CodeModel = {
    language: 'html',
    uri: 'main.json',
    value: 'Test'
  }

  options = {
    contextmenu: true,
    minimap: {
      enabled: true
    }
  };

}
