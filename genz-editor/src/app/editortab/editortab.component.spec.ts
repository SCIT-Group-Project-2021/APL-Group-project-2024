import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditortabComponent } from './editortab.component';

describe('EditortabComponent', () => {
  let component: EditortabComponent;
  let fixture: ComponentFixture<EditortabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EditortabComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditortabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
