import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CrosscallService {

  private runProgram = new Subject<any>();
  
  sendClickEvent() {
    this.runProgram.next("clicked");
  }
  getClickEvent(): Observable<any>{ 
    return this.runProgram.asObservable();
  }

  private loadfile = new Subject<any>();
  
  loadFileEvent(title: string) {
    this.loadfile.next(title);
  }
  getloadFileEvent(): Observable<any>{ 
    return this.loadfile.asObservable();
  }

  private loaduploadfile = new Subject<any>();
  
  loadUploadFileEvent(title: string[]) {
    this.loaduploadfile.next(title);
  }
  getloadUploadFileEvent(): Observable<any>{ 
    return this.loaduploadfile.asObservable();
  }

  editorData !:  string;

  sendEditorData(data: string) {
    this.editorData=data;
  }

  getEditorData(): string{ 
    return this.editorData;
  }

  editorInput !:  string;

  checkEditorData(): string{ 
    return this.editorInput;
  }

  setEditorData(data: string) {
    this.editorInput=data;
  }

  
}
