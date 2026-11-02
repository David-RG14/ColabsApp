import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonIcon,IonButton, LoadingController} from '@ionic/angular';
import { people } from 'ionicons/icons';
import { addIcons } from 'ionicons';
import { Router } from '@angular/router';

@Component({
  selector: 'app-splash-screen',
  templateUrl: './splash-screen.page.html',
  styleUrls: ['./splash-screen.page.scss'],
  imports: [IonContent, CommonModule, FormsModule, IonIcon, IonButton]
})
export class SplashScreenPage implements OnInit {
  private router = inject(Router);
  private loadingCtrl = inject(LoadingController);
  
  constructor() {
    addIcons({
      'people' : people
    });
   }

  ngOnInit() {
    console.log("SplashScreenPage initialized")
  }

  colaboradores(){
    this.router.navigate(['/tabs/tab1']);
  }

}
