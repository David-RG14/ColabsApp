import { TestBed } from '@angular/core/testing';
import { Colabs } from './colabs';

describe('Colabs', () => {
  let service: Colabs;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Colabs);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
