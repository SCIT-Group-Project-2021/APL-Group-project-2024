import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CrosscallService } from '../crosscall.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.scss'
})

export class SidebarComponent {

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
