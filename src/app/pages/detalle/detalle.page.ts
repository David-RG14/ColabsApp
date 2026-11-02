import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonBackButton, IonButtons, IonAvatar, IonText, IonIcon, IonButton, AlertController } from '@ionic/angular';
import { addIcons } from 'ionicons';
import { mail,call,briefcase,location,calendar,trash,pencil } from 'ionicons/icons';
import { Router } from '@angular/router';

@Component({
  selector: 'app-detalle',
  templateUrl: './detalle.page.html',
  styleUrls: ['./detalle.page.scss'],
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonBackButton, IonButtons, IonAvatar, IonText, IonIcon, IonButton]
})
export class DetallePage implements OnInit {
private alertController = inject(AlertController);
private router = inject(Router);

  constructor() { 
    addIcons({ mail,call,briefcase,location,calendar,trash,pencil});
  }
  async mostrarAlertaEliminar() {
    const alert = await this.alertController.create({
      cssClass: 'custom-alert-delete',
      header: '¿Eliminar colaborador?',
      message: 'Esta acción no se puede deshacer.',
      buttons: [
        {
          text: 'Cancelar',
          role: 'cancel',
          cssClass: 'btn-cancelar',
          handler: () => {
            console.log('Eliminación cancelada');
          }
        },
        {
          text: 'Eliminar',
          cssClass: 'btn-eliminar-rojo',
          handler: () => {
            console.log('Colaborador eliminado');
          }
        }
      ]
    });

    await alert.present();
  }

  editarColab(){
    this.router.navigate(['/editar']);
  }

  ngOnInit() {
  }

}
