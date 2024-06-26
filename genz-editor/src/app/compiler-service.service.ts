import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { from, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompilerServiceService {
 
  //readonly ROOT_URL = 'https://jsonplaceholder.typicode.com/todos/1'

  //readonly ROOT_URL = 'https://genz-editor-flask-app.azurewebsites.net/compile'

  readonly ROOT_URL = 'http://127.0.0.1:5000/compile'

  // readonly ROOT_URL = '  https://httpbin.org/post'


  posts: any;

  optionsLoad!: {
    userId: string,
    id: string,
    title: string,
    completed: boolean
  }

  constructor(private http: HttpClient) {}

  async getDataAsync() {
    return await this.http.get(this.ROOT_URL)
  }

  async getData() {
    
  }

  getDatawithoutsub() {
    return this.http.get(this.ROOT_URL)
  }

  compileFIle(file: File) {
    const formData: FormData = new FormData();
    formData.append('file', file);

    const headers = new HttpHeaders();
    headers.append('Content-Type', 'multipart/form-data');

    return this.http.post(this.ROOT_URL, formData, { headers: headers });
  }


}
