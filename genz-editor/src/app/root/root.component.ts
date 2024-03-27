import { Component, ViewChild } from '@angular/core';
import { animate, state, style, transition, trigger } from '@angular/animations';
import { EditorComponent } from '../editor/editor.component';

@Component({
  selector: 'app-root',
  templateUrl: './root.component.html',
  styleUrl: './root.component.scss',animations: [
    trigger('rotatedState', [
      state('default', style({ transform: 'rotate(0)' })),
      state('rotated', style({ transform: 'rotate(-180deg)' })),
      transition('rotated => default', animate('150ms ease-out')),
      transition('default => rotated', animate('150ms ease-in'))
    ])
  ]
})
export class RootComponent {

  

  state: string = 'default';

  rotate() {
    this.state = (this.state === 'default' ? 'rotated' : 'default');
  }

  constructor() { }
  
  public editor!: EditorComponent;

  addTab() {
    this.editor.addTab(true);
  }

}
