import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CrosscallService } from '../crosscall.service';
import { FileUploadEvent } from 'primeng/fileupload';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.scss'
})

export class SidebarComponent {

  uploadedFiles: any[] = [];

  onUpload(event: any) {
    for(let file of event.files) {
      this.uploadedFiles.push(file);
      let reader = new FileReader();
      reader.readAsText(file);
      reader.onload = () => {
        console.log('File name:', file.name);
        console.log('File content:', reader.result);
        this.crosscallService.loadUploadFileEvent([file.name, reader.result]);
      };
    }
  }

  constructor(private crosscallService:CrosscallService, private router: Router) { }
  
  loadSelection() {
    this.crosscallService.loadFileEvent('if_example.z');
  }

  loadFunction() {
    this.crosscallService.loadFileEvent('function_return.z');
  }

  loadPrint() {
    this.crosscallService.loadFileEvent('print_example2.z');
  }

  loadDatatype() {
    this.crosscallService.loadFileEvent('datatypes_example.z');
  }
  
}
