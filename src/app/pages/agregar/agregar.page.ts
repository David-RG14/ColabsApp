import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonAvatar, IonButton, IonButtons, IonContent, IonHeader, IonIcon, IonInput, 
  IonSelect, IonSelectOption, IonTitle, IonToolbar, IonBackButton } from '@ionic/angular';

import { addIcons } from 'ionicons';
import { cameraOutline } from 'ionicons/icons';

@Component({
  selector: 'app-agregar',
  templateUrl: './agregar.page.html',
  styleUrls: ['./agregar.page.scss'],
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, 
    FormsModule, IonIcon, IonInput, IonSelect, IonSelectOption, 
    IonButton, IonAvatar, IonButtons, IonBackButton]
})
export class AgregarPage implements OnInit {

  constructor() { 
    addIcons({ cameraOutline });
  }

  ngOnInit() {
  }

}
