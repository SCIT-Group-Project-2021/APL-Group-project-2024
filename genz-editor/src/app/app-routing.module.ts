import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SidebarComponent } from './sidebar/sidebar.component';
import { TerminalComponent } from './terminal/terminal.component';
import { EditorComponent } from './editor/editor.component';
import { RootComponent } from './root/root.component';

const routes: Routes = [
  {
    path: '',
    component: RootComponent,
    title: 'root'
  },
  {
    path: 'editor',
    component: EditorComponent,
    title: 'Editor'
  },
  {
    path: 'terminal',
    component: TerminalComponent,
    title: 'Terminal'
  },
  {
    path: 'sidebar',
    component: SidebarComponent,
    title: 'Sidebar'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
