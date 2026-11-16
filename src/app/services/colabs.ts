import { Service, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface NuevoColaborador {
  floatSueldo: number;
  strApellido: string;
  strNombre: string;
  strPuesto: string;
  strRfc: string;
}

@Service()
export class Colabs {
    // Para Get
    url = "http://192.168.1.159:5000/getColabs"
    // Para Post
    urlPost = "http://192.168.1.159:5000/postColabs";

    private http: HttpClient = inject(HttpClient);
    getcolabs():Observable<any> {
        return this.http.get(this.url)
    }

    postColabs(data: NuevoColaborador): Observable<unknown> {
    return this.http.post(this.urlPost, data);
  }
}
