import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { EditorComponent } from './editor/editor.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { TerminalComponent } from './terminal/terminal.component';
import { RootComponent } from './root/root.component';
import { ChatpanelComponent } from './chatpanel/chatpanel.component';


import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTabsModule } from '@angular/material/tabs';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatCommonModule } from '@angular/material/core';
import { MatDividerModule } from '@angular/material/divider';
import { MatTreeModule } from '@angular/material/tree';
import { MatBottomSheetModule } from '@angular/material/bottom-sheet';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { FormsModule } from '@angular/forms';

import { CodeEditorModule } from '@ngstack/code-editor';
import { TerminalModule } from 'primeng/terminal'; 

import { saveAs } from 'file-saver';
import { config } from 'dotenv';

import { OpenAI } from 'openai';


@NgModule({
  declarations: [
    AppComponent,
    EditorComponent, 
    SidebarComponent,
    TerminalComponent,
    RootComponent,
    ChatpanelComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatIconModule,
    MatTabsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatCommonModule,
    MatDividerModule,
    MatTreeModule,
    MatBottomSheetModule,
    MatButtonModule,
    CodeEditorModule.forRoot(),
    MatCardModule,
    TerminalModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    provideClientHydration(),
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { 
  
}
