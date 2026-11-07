import { Component, OnInit, inject } from '@angular/core';
import { IonHeader, IonToolbar, IonTitle, IonContent, IonSearchbar, IonFab, IonFabButton, IonIcon, IonButton, IonList, IonItem, IonAvatar, IonLabel, LoadingController } from '@ionic/angular';
import { Router } from '@angular/router';
import { addIcons } from 'ionicons';
import { add, peopleSharp } from 'ionicons/icons';
import { Colabs } from '../services/colabs';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
  imports: [IonList, IonItem, IonAvatar, IonLabel, IonButton, IonFab, IonFabButton, IonIcon, IonHeader, IonToolbar, IonTitle, IonContent,IonSearchbar],
})
export class Tab1Page implements OnInit{
    private colabs = inject(Colabs);
    listaColabs:any[]=[]
    
    colabexiste = true
    private loadingCtrl = inject(LoadingController);

  constructor(private router: Router) {
    addIcons({ add, peopleSharp });
  }

  ngOnInit() {
    this.colabs.getcolabs().subscribe((data)=>{
      console.log(data.Respuesta[0].strNombre)
      this.listaColabs=data.Respuesta
    })  

    console.log("tab1 initialized")
    if(this.colabexiste){
      this.showLoading();
    }
  }

  async showLoading() {
    const loading = await this.loadingCtrl.create({
      message: 'Cargando Colaboradores ...',
      duration: 1000,
    });

    loading.present();
  }

  agregarColab(){
    this.router.navigate(['/agregar'])
  }

  detalleColab(){
    this.router.navigate(['/detalle'])
  }
}
