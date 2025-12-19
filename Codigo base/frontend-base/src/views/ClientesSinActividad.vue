<template>
  <!-- Cambios Angelo -->
  <v-app>
    <v-navigation-drawer v-model="drawer" color="#006CA1" dark fixed app>
      <v-list>

        <v-list-item @click="irConfiguracion()" link v-if="idCargo == '1'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-cog" color="white" prepend-icon></v-icon>
              Configuración
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irComercial()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-account-tie" color="white" prepend-icon></v-icon>
              Comercial
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irContactos()" link v-if="idCargo == '2'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-contacts" color="white" prepend-icon></v-icon>
              Contactos Mercadeo
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irPendientesGeneral()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-format-list-checks" color="white" prepend-icon></v-icon>
              Pendientes
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-group value="Campañas" v-if="idCargo == '2'">
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" prepend-icon="mdi-bell-cog" title="Campañas" active></v-list-item>
          </template>

          <v-list-item @click="irCampañas()" link>

            <v-list-item-content>

              <v-list-item-title style="color: white;">
                <v-icon icon="mdi-bell" color="white" prepend-icon></v-icon>
                Ver Campañas
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irInformesCampañas()" link>

            <v-list-item-content>

              <v-list-item-title style="color: white;">
                <v-icon icon="mdi-chart-bell-curve-cumulative" color="white" prepend-icon></v-icon>
                Informes
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irGaleriaCampanas()" link>

            <v-list-item-content class="list-item-compact">

              <v-list-item-title style="color: white;">
                <v-icon icon="mdi mdi-view-gallery-outline" color="white" prepend-icon></v-icon>
                Ver Galería de Campañas
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

        </v-list-group>

        <v-list-item @click="irPQR()" link v-if="idCargo == '5'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-information-variant-circle" color="white" prepend-icon></v-icon>
              PQR
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irPedidos()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-package" color="white" prepend-icon></v-icon>
              Pedidos
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="abrirDialogProspectos()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-office-building-cog" color="white" prepend-icon></v-icon>
              Prospecto
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <AppHeader :nombre-comercial="nombreComercial" :imagen-comercial="imagenComercial" :correo-usuario="correoUsuario"
      :comercial-id="comercialId" :base-u-r-l="baseURL" v-model:drawer="drawer" @imagen-actualizada="actualizarImagen"
      @cerrar-sesion="cerrarSesion" />

    <!-- Cambios Angelo -->
    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
      <v-row class="mx-auto my-auto">
        <v-col cols="12">
          <h1 class="font-weight-bold">Seguimiento de Clientes Sin Actividad
            <v-tooltip text="Regresar al Panel Principal" location="top">
            <template #activator="{ props }">
              <v-icon @click="irComercial()" v-bind="props" size="30" class="mt-1 ml-2 btn-grow"
                color="#006CA1">
                  mdi-arrow-left-circle-outline
              </v-icon>
            </template>
          </v-tooltip>
          </h1>
        </v-col>

      </v-row>

      <v-row class="mx-auto my-auto" >
        <v-col v-for="(column, index) in estados" :key="index" cols="12" sm="6" md="4" lg="2"
          class="d-flex flex-column gap-4">
          <v-card elevation="3" class="">
            <v-card-title :class="column.color" class="text-white text-subtitle-1 font-weight-bold">
              <v-icon size="16">
                {{
                  column.id === 1 ? 'mdi-phone' :
                    column.id === 2 ? 'mdi-gmail' :
                      column.id === 3 ? 'mdi-calendar-cursor-outline' :
                        column.id === 4 ? 'mdi-monitor-account' :
                          column.id === 5 ? 'mdi-laptop' :
                            column.id === 6 ? 'mdi-point-of-sale' : 'mdi-calendar'
                }}
              </v-icon>
              {{ column.nombre }}
            </v-card-title>

            <v-card-text class="pa-2">
              <template v-for="(item, i) in column.items" :key="i">
                <v-tooltip location="right">
                  <template #activator="{ props }">
                    <v-card
                      @click="irPendientes(item)"
                      class="mb-3 px-4 py-3"
                      variant="elevated"
                      style="border-radius: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); cursor: pointer; transition: box-shadow 0.2s;"
                      v-bind="props"
                    >
                      <div class="d-flex align-center justify-space-between">
                        <div>
                          <div class="font-weight-bold" style="font-size: 1.08rem;">
                            {{ item.name }}
                          </div>
                          <div class="text-caption text-grey-darken-1 mb-1">
                            {{ item.description }}
                          </div>
                          <div v-if="item.date" class="text-caption mt-1 d-flex align-center">
                            <div class="text-caption text-grey-darken-1 mb-1">
                            {{ item.id }}
                            </div>
                            <v-icon size="18" class="mr-1" color="#1976D2">
                              {{
                                column.id === 1 ? 'mdi-phone' :
                                column.id === 2 ? 'mdi-gmail' :
                                column.id === 3 ? 'mdi-calendar-cursor-outline' :
                                column.id === 4 ? 'mdi-monitor-account' :
                                column.id === 5 ? 'mdi-laptop' :
                                column.id === 6 ? 'mdi-point-of-sale' : 'mdi-calendar'
                              }}
                            </v-icon>
                            <span>{{ item.date }}</span>
                          </div>
                        </div>
                      </div>
                    </v-card>
                  </template>
                  <span>
                    <strong>Contacto:</strong> {{ item.contacto || 'N/A' }}<br>
                    <strong>Teléfono:</strong> {{ item.telefono || 'N/A' }}<br>
                    <strong>Celular:</strong> {{ item.celular || 'N/A' }}<br>
                    <strong>Observación:</strong> {{ item.obsev || 'Sin observación' }}
                  </span>
                </v-tooltip>
              </template>

              <!-- Mostrar mensaje si no hay ítems -->
              <div v-if="column.items.length === 0" class="text-center text-grey">
                No hay registros
              </div>
            </v-card-text>
          </v-card>

        </v-col>
      </v-row>

      <v-dialog v-model="dialogNuevaActividad" max-width="600px" height="100vh" persistent>
        <v-card>

          <v-card-title class="text-h6">Registrar Actividad</v-card-title>

          <v-card-text>

            <!-- Cambios Angelo -->
            <v-row class="mt-n4">
              <v-col>
                <v-autocomplete label="Cliente" prepend-inner-icon="mdi-domain" v-model="selectedClienteActividad"
                  :items="selectClientesActividad" return-object item-title="nombre" item-value="id" variant="outlined"
                  :readonly="roClienteActividad"></v-autocomplete>
              </v-col>
            </v-row>
            <!-- Cambios Angelo -->

            <v-row class="mt-n4">
              <v-col>
                Actividad:
              </v-col>
            </v-row>

            <v-row class="mt-n2">
              <v-col>
                <v-checkbox label="Llamada realizada" prepend-icon="mdi-phone" v-model="cbLlamadaRealizada" color="red"
                  density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Visita presencial" prepend-icon="mdi-handshake-outline"
                  v-model="cbVisitaPresencial" color="red" density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Activación de Demo" prepend-icon="mdi-account-reactivate"
                  v-model="cbActivacionDemo" color="red" density="compact"></v-checkbox>
              </v-col>

              <v-col>
                <v-checkbox label="Correo enviado" prepend-icon="mdi-email" v-model="cbCorreoEnviado" color="red"
                  density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Visita virtual" prepend-icon="mdi-monitor-account"
                  v-model="cbVisitaVirtual" color="red" density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Cotización" prepend-icon="mdi-network-pos" v-model="cbCotizacion"
                  color="red" density="compact"></v-checkbox>
              </v-col>
            </v-row>

            <v-row class="mt-n6" v-if="ifServicioActividad">
              <v-col>
                <v-select clearable label="Servicio a cotizar" prepend-inner-icon="mdi-list-box-outline"
                  v-model="selectedServicioActividad" :items="selectServiciosActividad" return-object
                  item-title="nombre" item-value="id" variant="outlined"></v-select>
              </v-col>
            </v-row>

            <v-row class="mt-n6" v-if="ifValorProyecto">
              <v-col>
                <v-text-field label="Valor del Proyecto" clearable prepend-inner-icon="mdi-currency-usd"
                  variant="outlined" v-model="selectedValorProyecto" type="number"></v-text-field>
              </v-col>
            </v-row>

            <v-row class="mt-n6" v-if="ifDocumentos">
              <v-col>
                <v-file-input label="Adjuntar RUT" density="compact" variant="outlined" clearable
                  v-model="archivoRUT"></v-file-input>
                <v-file-input multiple label="Adjuntar documento" density="compact" variant="outlined" clearable
                  v-model="archivosActividad"></v-file-input>
              </v-col>
            </v-row>

            <v-row class="mt-n6" v-if="ifObservaciones">
              <v-col>
                <v-btn color="green" text @click="dialogHistorico = true" density="compact"
                  style="float: right;">Histórico</v-btn>
              </v-col>
            </v-row>

            <v-row class="mt-n2" v-if="ifObservaciones">
              <v-col>
                <v-textarea prepend-inner-icon="mdi-eye" label="Observaciones" rows="4" variant="outlined"
                  density="compact" v-model="selectedObservacionesActividad" clearable></v-textarea>
              </v-col>
            </v-row>

            <v-row class="mt-n2">
              <v-col>
                <v-select label="Estado actual del cliente" prepend-inner-icon="mdi-list-status"
                  v-model="selectedEstadoActividad" :items="selectEstadosActividad" return-object item-title="nombre"
                  item-value="id" variant="outlined" :readonly="roEstadoActividad"></v-select>
              </v-col>
            </v-row>

            <v-row class="mt-n2" v-if="ifComentariosAdicionales">
              <v-col>
                <v-textarea prepend-inner-icon="mdi-text-box-outline" label="Comentarios adicionales" rows="4"
                  variant="outlined" density="compact" v-model="selectedComentariosActividad" clearable></v-textarea>
              </v-col>
            </v-row>

            <v-row class="mt-n2">
              <v-col>
                <v-text-field type="date" clearable label="Próximo seguimiento" prepend-inner-icon="mdi-calendar"
                  v-model="proximoSeguimientoActividad" variant="outlined"></v-text-field>
              </v-col>
            </v-row>

            <v-row class="mt-n4" v-if="ifProximoSeguimientoActividad">
              <v-col>
                Seguimiento a realizar:
              </v-col>
            </v-row>

            <v-row class="mt-n2" v-if="ifProximoSeguimientoActividad">
              <v-col>
                <v-checkbox label="Llamar" prepend-icon="mdi-phone" v-model="cbLlamar" color="green"
                  density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Visita presencial" prepend-icon="mdi-handshake-outline"
                  v-model="cbVisitarPresencial" color="green" density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Activar Demo" prepend-icon="mdi-account-reactivate"
                  v-model="cbActivarDemo" color="green" density="compact"></v-checkbox>
              </v-col>

              <v-col>
                <v-checkbox label="Enviar Correo" prepend-icon="mdi-email" v-model="cbEnviarCorreo" color="green"
                  density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Visita virtual" prepend-icon="mdi-monitor-account"
                  v-model="cbVisitarVirtual" color="green" density="compact"></v-checkbox>
                <v-checkbox class="mt-n4" label="Cotizar" prepend-icon="mdi-network-pos" v-model="cbCotizar"
                  color="green" density="compact"></v-checkbox>
              </v-col>
            </v-row>

          </v-card-text>

          <v-row class="mt-n4">
            <v-col>
              <v-btn color="blue" class="ml-2" style="float: right;" @click="registrarActividad()">Registrar
                Actividad</v-btn>
              <v-btn color="blue" style="float: right;"
                @click="dialogNuevaActividad = false; limpiarCamposDialogActividad()">Cerrar</v-btn>
            </v-col>
          </v-row>

        </v-card>
      </v-dialog>

      <v-dialog v-model="alerta" persistent>
        <v-card :style="getAlertStyle()">
          <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
            class="mx-auto"></v-progress-circular>
          <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-tittle>
          <v-btn class="mt-4 mx-auto" @click="cerrarDIV()" :readonly="ifCargando"
            style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
        </v-card>
      </v-dialog>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';
import CryptoJS from "crypto-js";
import AppHeader from '../components/AppHeader.vue';

export default {
  components: {
    AppHeader,
  },
  data() {
    return {

      estados: [
        {
          id: 1,
          nombre: 'Llamada Realizada',
          color: 'bg-indigo-darken-3',
          items: []
        },
        {
          id: 2,
          nombre: 'Correo Enviado',
          color: 'bg-light-blue-darken-3',
          items: []
        },
        {
          id: 3,
          nombre: 'Visita Presencial',
          color: 'bg-orange-darken-3',
          items: []
        },
        {
          id: 4,
          nombre: 'Visita Virtual',
          color: 'bg-teal-darken-4',
          items: []
        },
        {
          id: 5,
          nombre: 'Activación de Demo',
          color: 'bg-purple-darken-1',
          items: []
        },
        {
          id: 6,
          nombre: 'Cotización',
          color: 'bg-brown-darken-3',
          items: []
        }
      ],

      baseURL: '',
      idUsuario: null,
      idCargo: null,
      dialogNuevaActividad: false,
      selectedClienteActividad: null,
      selectClientesActividad: [],
      roClienteActividad: false,
      cbLlamadaRealizada: false,
      cbVisitaPresencial: false,
      cbActivacionDemo: false,
      cbCorreoEnviado: false,
      cbVisitaVirtual: false,
      cbCotizacion: false,
      ifServicioActividad: false,
      selectedServicioActividad: null,
      selectServiciosActividad: [],
      ifValorProyecto: false,
      selectedValorProyecto: null,
      archivoRUT: null,
      archivosActividad: [],
      ifDocumentos: false,
      ifObservaciones: false,
      selectedObservacionesActividad: '',
      selectedEstadoActividad: null,
      selectEstadosActividad: [],
      roEstadoActividad: false,
      ifComentariosAdicionales: false,
      selectedComentariosActividad: '',
      proximoSeguimientoActividad: '',
      ifProximoSeguimientoActividad: false,
      cbLlamar: false,
      cbVisitarPresencial: false,
      cbActivarDemo: false,
      cbEnviarCorreo: false,
      cbVisitarVirtual: false,
      cbCotizar: false,
      dialogHistorico: false,
      itemSeleccionado: null,

      // Cambios Angelo
      idproccom: null,
      nombreComercial: null,
      imagenComercial: null,
      correoUsuario: null,
      comercialId: null,
      drawer: false,

      alerta: false,
      mensajeAlertLogin: '',
    };
  },

  mounted() {
    this.baseURL = import.meta.env.VITE_API_BASE_URL;
    this.cargarDatos();
    this.cargarClientesActividad();
    this.cargarServiciosActividad();
    this.cargarEstadosActividad();
    this.idCargo = localStorage.getItem('idCargo');

    // Cambios Angelo
    this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');
    this.idproccom = localStorage.getItem('idproccom');
    this.correoUsuario = localStorage.getItem('correo');
    this.comercialId = localStorage.getItem('idUsuario');

    const imagenGuardada = localStorage.getItem('imagenComercial');
    if (imagenGuardada) {
      this.imagenComercial = imagenGuardada;
    } else {
      this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg`;
    }

    setTimeout(() => {
      //this.cargarActividades();
      console.log('ID de Oportunidad:', this.idproccom);
    }, 1000);

  },

  watch: {

    cbCotizacion(newValue) {
      if (newValue) {
        this.ifServicioActividad = true;
        this.ifValorProyecto = true;
        this.ifDocumentos = true;
        this.ifObservaciones = false;
        this.ifComentariosAdicionales = true;
        this.roEstadoActividad = true;
        this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 3);

        this.idActividad = 6;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbVisitaVirtual = false;
        this.cbActivacionDemo = false;
      } else {
        this.ifServicioActividad = false;
        this.ifValorProyecto = false;
        this.ifDocumentos = false;
        this.ifObservaciones = true;
        this.ifComentariosAdicionales = false;
        this.roEstadoActividad = false;
        this.selectedEstadoActividad = null;
        this.idActividad = null;
      }
    },

    selectedEstadoActividad(newValue) {
      if (newValue) {
        if (newValue.id === 3) {
          this.ifServicioActividad = true;
          this.ifValorProyecto = true;
          this.ifDocumentos = true;
          this.ifObservaciones = false;
          this.ifComentariosAdicionales = true;
          this.roEstadoActividad = true;
          this.cbCotizacion = true;
        } else {
          this.ifServicioActividad = false;
          this.ifValorProyecto = false;
          this.ifDocumentos = false;
          this.ifObservaciones = true;
          this.ifComentariosAdicionales = false;
          this.roEstadoActividad = false;
          this.cbCotizacion = false;
        }
      }
    },

    proximoSeguimientoActividad(newValue) {
      if (newValue) {
        this.ifProximoSeguimientoActividad = true;
      } else {
        this.ifProximoSeguimientoActividad = false;
        this.cbLlamar = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      }
    },

    cbLlamadaRealizada(newValue) {
      if (newValue) {
        this.idActividad = 1;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbActivacionDemo = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbCorreoEnviado(newValue) {
      if (newValue) {
        this.idActividad = 2;
        this.cbLlamadaRealizada = false;
        this.cbVisitaPresencial = false;
        this.cbActivacionDemo = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbVisitaPresencial(newValue) {
      if (newValue) {
        this.idActividad = 3;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbActivacionDemo = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbVisitaVirtual(newValue) {
      if (newValue) {
        this.idActividad = 4;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbActivacionDemo = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbActivacionDemo(newValue) {
      if (newValue) {
        this.idActividad = 5;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbLlamar(newValue) {
      if (newValue) {
        this.idSeguimiento = 1;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbEnviarCorreo(newValue) {
      if (newValue) {
        this.idSeguimiento = 2;
        this.cbLlamar = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbVisitarPresencial(newValue) {
      if (newValue) {
        this.idSeguimiento = 3;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbActivarDemo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbVisitarVirtual(newValue) {
      if (newValue) {
        this.idSeguimiento = 4;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbActivarDemo(newValue) {
      if (newValue) {
        this.idSeguimiento = 5;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbCotizar(newValue) {
      if (newValue) {
        this.idSeguimiento = 6;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbVisitarVirtual = false;
        this.cbActivarDemo = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    fechaInicio(newValue) {
      // Si ya había fechaFin y es anterior a la nueva inicio,
      // la limpiamos para forzar al usuario a elegir de nuevo.
      if (this.fechaInicio == null) {
        this.fechaFin = null;
      }
      else if (this.fechaFin && this.fechaFin < newValue) {
        this.fechaFin = this.fechaInicio;
      }
    }

  },

  methods: {

    irComercial() {
      this.$router.push('/comercial');
    },

    irPendientesGeneral() {
      this.$router.push('/pendiente-general');
    },

    irConfiguracion() {
      this.$router.push('/configuracion');
    },

    irPQR() {
      this.$router.push('/pqr');
    },

    irPedidos() {
      this.$router.push('/pedidos');
    },

    irCampañas() {
      this.$router.push('/campana');
    },

    irInformesCampañas() {
      this.$router.push('/informes-campanas');
    },

    irGaleriaCampanas() {
      this.$router.push('/VerCampanas');
    },

    irContactos() {
      this.$router.push('/contactos');
    },

    abrirFormularioActividad(item) {

      this.dialogNuevaActividad = true;
      this.selectedClienteActividad.id = item.idproc;
      console.log('ID del item seleccionado:', item.idproc);

    },

    limpiarCamposDialogActividad() {
      this.selectedClienteActividad = null;
      this.cbLlamadaRealizada = false;
      this.cbVisitaPresencial = false;
      this.cbActivacionDemo = false;
      this.cbCorreoEnviado = false;
      this.cbVisitaVirtual = false;
      this.cbCotizacion = false;

      this.selectedObservacionesActividad = null;

      this.selectedEstadoActividad = null;

      this.proximoSeguimientoActividad = null;

      this.cbLlamar = false;
      this.cbVisitarPresencial = false;
      this.cbActivarDemo = false;
      this.cbEnviarCorreo = false;
      this.cbVisitarVirtual = false;
      this.cbCotizar = false;

      this.selectedServicioActividad = null;
      this.selectedValorProyecto = null;

      this.archivoRUT = null;
      this.archivosActividad = [];

      this.selectedComentariosActividad = null;
    },

    cargarEstadosActividad() {
      axios.get(this.baseURL + 'api/cargares')
        .then(response => {
          this.selectEstadosActividad = response.data.data;
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
    },

    cargarServiciosActividad() {
      axios.get(this.baseURL + 'api/cargarsv')
        .then(response => {
          this.selectServiciosActividad = response.data.data;
          this.selectServiciosOportunidad = response.data.data;
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
    },

    cargarClientesActividad() {
      axios.post(this.baseURL + 'api/cargarpp', {
        'idusu': localStorage.getItem('idUsuario')
      })
        .then(response => {
          this.selectClientesActividad = response.data.data;
          this.selectClientesOportunidad = response.data.data;
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
    },

    registrarActividad() {

      let cbCotizacion = this.cbCotizacion;

      const isValid1 = this.selectClientesActividad && this.idActividad !== null && this.selectedObservacionesActividad && this.selectedEstadoActividad && this.proximoSeguimientoActividad && this.idSeguimiento !== null;

      const isValid2 = this.selectClientesActividad && this.idActividad !== null && this.selectedEstadoActividad && this.proximoSeguimientoActividad && this.idSeguimiento !== null && this.selectServiciosActividad && this.selectedValorProyecto && this.archivoRUT !== null && this.selectedComentariosActividad;

      if (cbCotizacion) {

        if (!isValid2) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos. 1';
          this.alerta = true;
          return;
        }
      } else {
        if (!isValid1) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos. 2';
          this.alerta = true;
          return;
        }

      }

      // Cambios Angelo
      let formData = new FormData();
      formData.append('procom', this.idOportunidad);
      formData.append('cli', this.selectedClienteActividad.id);
      formData.append('act', this.idActividad);
      formData.append('obs', this.selectedObservacionesActividad);
      formData.append('estado', this.selectedEstadoActividad.id);
      formData.append('fpseg', this.proximoSeguimientoActividad);
      formData.append('idseg', this.idSeguimiento);
      formData.append('idmedio', 1);
      formData.append('file', this.archivoRUT);

      axios.post(this.baseURL + 'api/newproccomact', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => {
        this.dialogNuevaActividad = false;
        this.limpiarCamposDialogActividad();
        this.cargarClientesActividad();
        this.cargarEstadosActividad();

        console.log('Actividad registrada:', response.data.data);

        setTimeout(() => {
          this.mensajeAlertLogin = 'La actividad se ha registrado correctamente.';
          this.alerta = true;
        }, 600);
      })
        .catch(error => {
          console.error('Error al registrar la actividad:', error);
        });

    },

    cargarDatos() {
      const id = localStorage.getItem('idUsuario');

      axios.post(this.baseURL + 'api/cargarlispend', {
        idusu: id,
      })
        .then(response => {
          const datos = response.data?.data;
          console.log('Datos cargados:', datos);

          if (!Array.isArray(datos)) {
            console.error('⚠️ La respuesta del servidor no contiene un arreglo válido:', response.data);
            return;
          }


          // Limpiar todos los items de cada estado
          this.estados.forEach(estado => {
            estado.items = [];
          });

          // Llenar items según el campo nomseg
          datos.forEach(item => {
            const etapa = item.nomseg || 'Sin etapa';

            const estadoEncontrado = this.estados.find(e => e.nombre === etapa);

            const nuevoItem = {
              name: item.razon_social,
              description: item.nomserv,
              date: item.fecproxseg,
              idproc: item.idproc,
              obsev: item.obsev,
              idprosp: item.idprosp,
              telefono: item.telprosp,
              contacto: item.nomcontacto,
              celular: item.nomcelu,
            };

            if (estadoEncontrado) {
              estadoEncontrado.items.push(nuevoItem);
            } else {
              // Si no coincide con ningún estado, lo pone en "Sin etapa"
              const sinEtapa = this.estados.find(e => e.nombre === 'Sin etapa');
              if (sinEtapa) {
                sinEtapa.items.push(nuevoItem);
              }
            }
          });
        })
        .catch(error => {
          console.error('Error al cargar datos:', error);
        });
    },

    // Cambios Angelo
    cargarActividades() {
      const data = {
        idproccom: this.idproccom,
      };

      axios.post(this.baseURL + 'api/cargarprosppend', data)
        .then(response => {
          console.log('Actividades cargadas:', response.data.data);

          const datos = response.data?.data;

          this.estados.forEach(estado => {
            estado.items = [];
          });

          datos.forEach(item => {
            const etapa = item.nomseg || 'Sin etapa';

            const estadoEncontrado = this.estados.find(e => e.nombre === etapa);

            const nuevoItem = {
              name: item.razon_social,
              description: item.nomserv,
              date: item.fecproxseg,
              idproc: item.idproc,
              obsev: item.obsev
            };

            if (estadoEncontrado) {
              estadoEncontrado.items.push(nuevoItem);
            } else {
              // Si no coincide con ningún estado, lo pone en "Sin etapa"
              const sinEtapa = this.estados.find(e => e.nombre === 'Sin etapa');
              if (sinEtapa) {
                sinEtapa.items.push(nuevoItem);
              }
            }
          });
        })
        .catch(error => {
          console.error('Error al cargar actividades:', error);
        });
    },

    getAlertStyle() {
      if (this.isMobileView == true) {
        return {
          borderRadius: '20px',
          position: 'fixed',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          backgroundColor: 'rgb(227, 231, 252)',
          padding: '20px',
          border: '1px solid black',
          borderRadius: '10px',
          boxShadow: '0 6px 15px rgba(0, 0, 0, 0.5)',
          transition: 'box-shadow 0.3s ease-in-out',
          width: '75%'
        };
      } else {
        return {
          borderRadius: '20px',
          position: 'fixed',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          backgroundColor: 'rgb(227, 231, 252)',
          padding: '20px',
          border: '1px solid black',
          borderRadius: '10px',
          boxShadow: '0 6px 15px rgba(0, 0, 0, 0.5)',
          transition: 'box-shadow 0.3s ease-in-out',
          width: '20%'
        };
      }
    },

    cerrarDIV() {
      this.alerta = false;
    },

    cerrarSesion() {
      localStorage.removeItem('idUsuario')
      localStorage.removeItem('idCargo')
      localStorage.removeItem('nombreLogin')
      localStorage.removeItem('apellidoLogin')
      localStorage.removeItem('celularLogin')
      localStorage.removeItem('logueado')
      this.$router.push('/')
    },

    formatDDMMYYYY(val) {
    const d = this.parseDate(val);
    if (!d) return 'Fecha no válida';
    const dd = String(d.getDate()).padStart(2, '0');
    const mm = String(d.getMonth() + 1).padStart(2, '0');
    const yyyy = d.getFullYear();
    return `${dd}/${mm}/${yyyy}`;
  },

  // ---- PARSEO robusto (YYYY-MM-DD HH:MMAM/PM o ISO)
  parseDate(val) {
    if (!val) return null;
    const s = String(val).trim();

    // Caso ISO simple: "2025-08-06 12:00AM" -> "2025-08-06T12:00AM"
    let d = new Date(s.replace(' ', 'T'));
    if (!isNaN(+d)) { d.setHours(0,0,0,0); return d; }

    // Caso AM/PM explícito "YYYY-MM-DD HH:MMAM/PM"
    const m = s.match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{1,2}):(\d{2})(AM|PM)$/i);
    if (m) {
      let [,Y,Mo,D,h,mi,ampm] = m;
      let hh = (parseInt(h,10) % 12) + (ampm.toUpperCase()==='PM' ? 12 : 0);
      d = new Date(`${Y}-${Mo}-${D}T${String(hh).padStart(2,'0')}:${mi}:00`);
      if (!isNaN(+d)) { d.setHours(0,0,0,0); return d; }
    }
    return null;
  },


  }
};
</script>

<style scoped>
.menu-link {
  color: #1976D2;
  cursor: pointer;
  text-decoration: underline;
  font-size: 1rem;
  margin-bottom: 8px;
  font-weight: 500;
  transition: color 0.2s;
  width: fit-content;
}
.menu-link:hover {
  color: #0A1C3A;
  text-decoration: underline;
}</style>
