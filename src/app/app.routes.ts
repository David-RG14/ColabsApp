import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./tabs/tabs.routes').then((m) => m.routes),
  },
  {
    path: 'splash-screen',
    loadComponent: () => import('./pages/splash-screen/splash-screen.page').then( m => m.SplashScreenPage)
  },
  {
    path: 'agregar',
    loadComponent: () => import('./pages/agregar/agregar.page').then( m => m.AgregarPage)
  },
  {
    path: 'editar',
    loadComponent: () => import('./pages/editar/editar.page').then( m => m.EditarPage)
  },
  {
    path: 'detalle',
    loadComponent: () => import('./pages/detalle/detalle.page').then( m => m.DetallePage)
  },
];
