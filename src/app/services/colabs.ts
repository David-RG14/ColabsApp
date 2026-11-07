import { Service, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Service()
export class Colabs {
    url = "http://192.168.1.154:5000/getColabs"
    private http: HttpClient = inject(HttpClient);
    getcolabs():Observable<any> {
        return this.http.get(this.url)
    }
}
