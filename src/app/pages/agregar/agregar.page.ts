import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonAvatar, IonButton, IonButtons, IonContent, IonHeader, IonIcon, IonInput, 
  IonSelect, IonSelectOption, IonTitle, IonToolbar, IonBackButton } from '@ionic/angular';
import { addIcons } from 'ionicons';
import { cameraOutline } from 'ionicons/icons';

import { HttpErrorResponse } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';
import { Colabs, type NuevoColaborador } from '../../services/colabs';


import {
  form,
  FormField,
  required,
  pattern,
  min,
  submit
} from '@angular/forms/signals';

interface ColaboradorForm {
  strNombre: string;
  strApellido: string;
  strPuesto: string;
  strRfc: string;
  floatSueldo: number | null;
}
function crearModeloInicial(): ColaboradorForm {
  return {
    strNombre: '',
    strApellido: '',
    strPuesto: '',
    strRfc: '',
    floatSueldo: null
  };
}

@Component({
  selector: 'app-agregar',
  templateUrl: './agregar.page.html',
  styleUrls: ['./agregar.page.scss'],
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, 
    FormsModule, IonIcon, IonInput, IonSelect, IonSelectOption, 
    IonButton, IonAvatar, IonButtons, IonBackButton, FormField]
})
export class AgregarPage implements OnInit {
  private readonly colabs = inject(Colabs);

  readonly mensajeError = signal('');
  readonly mensajeExito = signal('');

  // Cambia estas opciones por tus puestos.
  readonly puestos = [
    'Administrativo',
    'Desarrollador',
    'Soporte técnico'
  ];

  // Datos del formulario.
  readonly modelo = signal<ColaboradorForm>(crearModeloInicial());

  // Formulario y validaciones.
  readonly formulario = form(this.modelo, (campo) => {
    required(campo.strNombre);
    pattern(campo.strNombre, /\S/);

    required(campo.strApellido);
    pattern(campo.strApellido, /\S/);

    required(campo.strPuesto);

    required(campo.strRfc);

    // Formato general del RFC: 12 o 13 caracteres.
    pattern(
      campo.strRfc,
      /^[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}$/i
    );

    required(campo.floatSueldo);
    min(campo.floatSueldo, 0);
  });

  constructor() { 
    addIcons({ cameraOutline });
  }

  async guardar(event: Event): Promise<void> {
    event.preventDefault();

    if (this.formulario().submitting()) {
      return;
    }

    this.mensajeError.set('');
    this.mensajeExito.set('');

    try {
      const guardado = await submit(this.formulario, async (campos) => {
        const datos = campos().value();
        const sueldo = datos.floatSueldo;

        if (sueldo === null || !Number.isFinite(sueldo)) {
          return {
            kind: 'sueldoInvalido',
            message: 'Ingresa un sueldo válido.',
            fieldTree: campos.floatSueldo
          };
        }

        const payload: NuevoColaborador = {
          strNombre: datos.strNombre.trim(),
          strApellido: datos.strApellido.trim(),
          strPuesto: datos.strPuesto,
          strRfc: datos.strRfc.trim().toUpperCase(),
          floatSueldo: sueldo
        };

        // Espera a que termine la petición del servicio.
        await firstValueFrom(
          this.colabs.postColabs(payload)
        );

        return undefined;
      });

      if (guardado) {
        this.formulario().reset(crearModeloInicial());
        this.mensajeExito.set('Colaborador guardado correctamente.');
      }
    } catch (error: unknown) {
      const mensaje = error instanceof HttpErrorResponse
        ? error.error?.mensaje
        : undefined;

      this.mensajeError.set(
        typeof mensaje === 'string'
          ? mensaje
          : 'No se pudo guardar el colaborador.'
      );
    }
  }

  ngOnInit() {
  }

}
