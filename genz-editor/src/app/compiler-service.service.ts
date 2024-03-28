import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { from, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompilerServiceService {

  readonly ROOT_URL = 'https://jsonplaceholder.typicode.com/todos/1'

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


}
