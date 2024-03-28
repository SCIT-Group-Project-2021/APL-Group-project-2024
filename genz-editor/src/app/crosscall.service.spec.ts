import { TestBed } from '@angular/core/testing';

import { CrosscallService } from './crosscall.service';

describe('CrosscallService', () => {
  let service: CrosscallService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CrosscallService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
