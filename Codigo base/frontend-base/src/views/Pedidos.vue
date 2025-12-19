<template>
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

            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/comercial' }" style="color: white;">
              <v-icon icon="mdi mdi-home-account" color="white" prepend-icon></v-icon>
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

            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/pendiente-general' }" style="color: white;">
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

            <v-list-item-title  :class="{ 'menu-item-activo': menuActivo === '/pedidos' }" style="color: white;">
              <v-icon class="mr-2" size="small"  icon="mdi mdi-package-variant" color="white" prepend-icon></v-icon>
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

        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
                <v-row style="height: 100%;">
                    <v-col style="height: 100%;">
                        <v-card class="elevation-5 rounded-lg fill-height"
                            style="background-color: #F0F4F8; overflow-y: auto;">
                            <v-card-title class="text-h6" style="color: #0A1C3A;">
                                <h2 style="color: #0A1C3A; font-weight: bold;">Historial de Pedidos</h2>
                            </v-card-title>

                            <v-row class="mx-1">
                                <v-col>
                                    <v-text-field type="date" v-model="fechaInicio" label="Fecha Inicio" clearable
                                        style="width: 50%;" density="compact" />
                                    <v-spacer></v-spacer>

                                </v-col>

                                <v-col>
                                    <v-text-field type="date" v-model="fechaFin" label="Fecha Fin" style="width: 50%;"
                                        clearable density="compact" />
                                </v-col>

                                <v-col>
                                    <v-btn color="blue-darken-4" @click="nuevoPedido()" style="float: right">
                                        <v-icon class="mr-2">mdi-plus</v-icon>
                                        Nuevo Pedido
                                    </v-btn>
                                </v-col>
                            </v-row>

                            <v-divider :thickness="3" color="#0A1C3A" class="border-opacity-50"></v-divider>

                            <v-card-text>
                                <v-row>
                                    <v-col>
                                        <v-card color="#0A1C3A" class="pa-4"
                                            style="height: 100%; width: 100%; overflow-y: auto;">
                                            <v-row>
                                                <v-col cols="4">
                                                    <v-icon icon="mdi-calendar-check-outline" size="50" color="white"
                                                        class="mx-auto d-block"></v-icon>
                                                </v-col>

                                                <v-col>
                                                    <h4 style="color: white;">Total de pedidos</h4>
                                                    <h2 style="color: white;">{{ totalPedidos }}</h2>
                                                </v-col>
                                            </v-row>
                                        </v-card>
                                    </v-col>

                                    <v-col>
                                        <v-card color="green" class="pa-4"
                                            style="height: 100%; width: 100%; overflow-y: auto;">
                                            <v-row>
                                                <v-col cols="4">
                                                    <v-icon icon="mdi-new-box" size="50" color="white"
                                                        class="mx-auto d-block"></v-icon>
                                                </v-col>

                                                <v-col>
                                                    <h4 style="color: white;">Nuevos</h4>
                                                    <h2 style="color: white;">{{ totalNuevos }}</h2>
                                                </v-col>
                                            </v-row>
                                        </v-card>
                                    </v-col>

                                    <v-col>
                                        <v-card color="blue-darken-4" class="pa-4"
                                            style="height: 100%; width: 100%; overflow-y: auto;">
                                            <v-row>
                                                <v-col cols="4">
                                                    <v-icon icon="mdi-progress-clock" size="50" color="white"
                                                        class="mx-auto d-block"></v-icon>
                                                </v-col>

                                                <v-col>
                                                    <h4 style="color: white;">En Proceso</h4>
                                                    <h2 style="color: white;">{{ totalEnProceso }}</h2>
                                                </v-col>
                                            </v-row>
                                        </v-card>
                                    </v-col>

                                    <v-col>
                                        <v-card color="yellow" class="pa-4"
                                            style="height: 100%; width: 100%; overflow-y: auto;">
                                            <v-row>
                                                <v-col cols="4">
                                                    <v-icon icon="mdi-check-circle" size="50" color="black"
                                                        class="mx-auto d-block"></v-icon>
                                                </v-col>

                                                <v-col>
                                                    <h4 style="color: black;">Entregados</h4>
                                                    <h2 style="color: black;">{{ totalEntregados }}</h2>
                                                </v-col>
                                            </v-row>
                                        </v-card>
                                    </v-col>

                                    <v-col>
                                        <v-card color="red-lighten-1" class="pa-4"
                                            style="height: 100%; width: 100%; overflow-y: auto;">
                                            <v-row>
                                                <v-col cols="4">
                                                    <v-icon icon="mdi-close-octagon" size="50" color="white"
                                                        class="mx-auto d-block"></v-icon>
                                                </v-col>

                                                <v-col>
                                                    <h4 style="color: white;">Cancelados</h4>
                                                    <h2 style="color: white;">{{ totalCancelados }}</h2>
                                                </v-col>
                                            </v-row>
                                        </v-card>
                                    </v-col>
                                </v-row>

                                <v-row>
                                    <v-col cols="6" class="d-flex align-center justify-center">
                                        <div style="width: 100%; height: 100%;">
                                            <canvas ref="myChart"></canvas>
                                        </div>
                                    </v-col>

                                    <v-col cols="6" class="d-flex align-center justify-center">
                                        <div style="width: 50%; height: 100%;">
                                            <h2>Pedidos por estado</h2>
                                            <canvas ref="myChart2"></canvas>
                                        </div>
                                    </v-col>
                                </v-row>

                                <v-row>
                                    <v-col>
                                        <v-data-table :headers="headersProductos" :items="listaPedidos"
                                            class="elevation-1 rounded-lg data-table"
                                            items-per-page-text="Pedidos por página" items-per-page="5"
                                            :items-per-page-options="[5, 10, 15]" style="height: 100%; width: 100%;"
                                            page-text="Pedidos del ({0}) al ({1}) de ({2})">

                                            <template v-slot:item.estadoNombre="{ item }">
                                                <v-chip
                                                    :color="item.estadoNombre == 'Nuevo' ? 'green' : item.estadoNombre == 'En proceso' ? '#006CA1' : item.estadoNombre == 'Entregado' ? 'yellow' : 'red'"
                                                    variant="elevated">
                                                    {{ item.estadoNombre }}
                                                </v-chip>
                                            </template>


                                            <!-- formatear la fecha con hora en formato 12 horas y formato dd/mm/yy-->
                                            <template v-slot:item.fechaPedido="{ item }">
                                                {{ formatDate(item.fechaPedido) }}
                                            </template>
                                        </v-data-table>
                                    </v-col>
                                </v-row>
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>

            <!----- Dialogo para nuevo pedido ----->
            <v-dialog v-model="dialogNuevoPedido" persistent max-width="600px">
                <v-card class="pa-4 rounded-xl">
                    <v-card-title class="text-h6" style="color: #0A1C3A;">
                        Nuevo Pedido
                    </v-card-title>
                    <v-card-text>
                        <v-autocomplete v-model="empresaSeleccionada" :items="empresas" item-title="p_razon_social"
                            :error="errorEmpresa" item-value="id" label="Empresa *" density="compact" variant="outlined"
                            clearable @update:model-value="cargarContacto()" return-object />
                        <v-select label="Contacto Prospecto *" variant="outlined" density="compact" :items="contactos"
                            :error="errorContacto"
                            :item-title="item => `${item.nombre}` ? `${item.nombre}` : 'No disponible'" item-value="id"
                            v-model="contactoSeleccionado" return-object readonly />
                        <v-select clearable label="Servicio para Pedido *" v-model="servicioSeleccionado"
                            :items="servicios" return-object item-title="nombre" item-value="id" variant="outlined"
                            density="compact" :error="errorServicio" autocomplete="off"></v-select>
                        <v-text-field label="Cantidad *" v-model="cantidadPedido" type="number" variant="outlined"
                            :error="errorCantidad" density="compact" clearable />
                        <v-textarea label="Detalle del Pedido" variant="outlined" density="compact"
                            v-model="detallePedido" rows="3" clearable></v-textarea>
                    </v-card-text>
                    <v-card-actions class="mt-n8">
                        <v-spacer></v-spacer>
                        <v-btn variant="flat" color="#006CA1" @click="guardarPedido()">Guardar</v-btn>
                        <v-btn variant="flat" color="grey"
                            @click="dialogNuevoPedido = false; limpiarDialogNuevoPedido()">Cancelar</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <!----- Dialogo para nuevo pedido ----->


            <!----- Dialogo para cambio de clave ----->

            <!----- Dialogo para las alertas ----->
            <v-dialog v-model="alerta" persistent style="z-index: 10000;">
                <v-card :style="getAlertStyle()">
                    <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
                        class="mx-auto"></v-progress-circular>
                    <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-tittle>
                    <v-btn class="mt-4 mx-auto" @click="cerrarDIV()" :readonly="ifCargando"
                        style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
                </v-card>
            </v-dialog>
            <!----- Dialogo para las alertas ----->
        </v-main>
    </v-app>
</template>

<script>
import CryptoJS from "crypto-js";

import {
    Chart,
    LineController,
    LineElement,
    PointElement,
    CategoryScale,
    LinearScale,
    Tooltip,
    Legend,
    Filler,
    ArcElement,
    DoughnutController,
    PieController,
    BarController,
    BarElement,
} from 'chart.js';

import axios from 'axios';
import { format } from "crypto-js";
import AppHeader from '../components/AppHeader.vue';

Chart.register(
    LineController,
    LineElement,
    PointElement,
    CategoryScale,
    LinearScale,
    Tooltip,
    Legend,
    Filler,
    ArcElement,
    DoughnutController,
    PieController,
    BarController,
    BarElement
);

export default {
    components: {
        AppHeader
    },
    data: () => ({

        drawer: false,
        menuAbierto: false,
        nombreComercial: localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin') || 'Comercial',
        comercialId: localStorage.getItem('idUsuario') || '0',
        idCargo: null,
        correoUsuario: localStorage.getItem('correoUsuario') || 'No disponible',
        imagenComercial: null,

        alerta: false,
        mensajeAlertLogin: null,
        ifCargando: false,
        baseURL: null,

        fechaInicio: null,
        fechaFin: null,

        headersProductos: [],

        totalPedidos: 0,
        totalNuevos: 0,
        totalEnProceso: 0,
        totalEntregados: 0,
        totalCancelados: 0,

        dialogNuevoPedido: false,
        empresaSeleccionada: null,
        errorEmpresa: false,
        errorContacto: false,
        errorServicio: false,
        errorCantidad: false,
        empresas: [],
        contactoSeleccionado: null,
        contactos: [],
        servicioSeleccionado: null,
        servicios: [],
        cantidadPedido: null,
        detallePedido: null,

        listaPedidos: [],
        dataChart: [],
        dataChart2: [],
        chartInstance: null,
        chartInstance2: null,

        menuActivo: null,

    }),

    created() {
        window.addEventListener("message", (e) => this.recibirMensaje(e));
    },
    destroyed() {
        window.removeEventListener("message", (e) => this.recibirMensaje(e));
    },

    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.idCargo = localStorage.getItem('idCargo');
        this.cargarPedidos();
        this.setMenuActivoPorRuta();

        // Cargar imagen del comercial
        const savedImage = localStorage.getItem('imagenComercial');
        if (savedImage) {
            this.imagenComercial = savedImage;
        } else {
            this.imagenComercial = `/images/${this.comercialId}.jpeg?t=${Date.now()}`;
        }
    },

    watch: {

        empresaSeleccionada(newValue) {
            if (newValue) {
                this.errorEmpresa = false;
            }
        },

        contactoSeleccionado(newValue) {
            if (newValue) {
                this.errorContacto = false;
            }
        },

        servicioSeleccionado(newValue) {
            if (newValue) {
                this.errorServicio = false;
            }
        },

        cantidadPedido(newValue) {
            if (newValue) {
                this.errorCantidad = false;
            }
        },

    },

    computed: {

    },

    methods: {

        nuevoPedido() {
            this.dialogNuevoPedido = true;
            this.obtenerEmpresas();
            this.cargarServiciosActividad();
        },

        obtenerEmpresas() {
            axios.post(this.baseURL + 'api/cargarpp', {
                'idusu': 0,
            })
                .then(response => {
                    this.empresas = response.data.data;
                })
                .catch(error => {
                    console.error('Error al cargar empresas:', error)
                })
        },

        cargarServiciosActividad() {
            axios.get(this.baseURL + 'api/cargarsv')
                .then(response => {
                    this.servicios = response.data.data;
                })
                .catch(error => {
                    console.log(response.data[0].error);
                });
        },

        cargarContacto() {
            if (this.empresaSeleccionada) {
                this.contactoSeleccionado = null;
                this.contactos = [];
                this.contactos.push({
                    id: this.empresaSeleccionada.pc_id,
                    nombre: this.empresaSeleccionada.pc_nombre ? this.empresaSeleccionada.pc_nombre + ' ' + (this.empresaSeleccionada.pc_apellido ? this.empresaSeleccionada.pc_apellido : 'No disponible') : 'No disponible'
                });
                setTimeout(() => {
                    this.contactoSeleccionado = this.contactos[0];
                }, 500);
            } else {
                this.contactos = [];
                this.contactoSeleccionado = null;
            }
        },

        guardarPedido() {
            if (!this.empresaSeleccionada && !this.contactoSeleccionado && !this.servicioSeleccionado && !this.cantidadPedido) {
                this.errorEmpresa = true;
                this.errorContacto = true;
                this.errorServicio = true;
                this.errorCantidad = true;

                this.alerta = true;
                this.mensajeAlertLogin = 'Por favor, complete todos los campos obligatorios (*).';
                return;
            } else {
                if (!this.empresaSeleccionada) {
                    this.errorEmpresa = true;
                    this.alerta = true;
                    this.mensajeAlertLogin = 'Por favor, seleccione una empresa.';
                    return;
                } else {
                    this.errorEmpresa = false;
                }

                if (!this.contactoSeleccionado) {
                    this.errorContacto = true;
                    this.alerta = true;
                    this.mensajeAlertLogin = 'Por favor, seleccione un contacto.';
                    return;
                } else {
                    this.errorContacto = false;
                }

                if (!this.servicioSeleccionado) {
                    this.errorServicio = true;
                    this.alerta = true;
                    this.mensajeAlertLogin = 'Por favor, seleccione un servicio.';
                    return;
                } else {
                    this.errorServicio = false;
                }

                if (!this.cantidadPedido || this.cantidadPedido <= 0) {
                    this.errorCantidad = true;
                    this.alerta = true;
                    this.mensajeAlertLogin = 'Por favor, ingrese una cantidad válida.';
                    return;
                } else {
                    this.errorCantidad = false;
                }
            }

            this.ifCargando = true;
            this.alerta = true;
            this.mensajeAlertLogin = 'Guardando pedido...';

            axios.post(this.baseURL + 'api/guardarPedido', {
                'empresaId': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
                'contactoId': this.contactoSeleccionado.id ? this.contactoSeleccionado.id : 0,
                'servicioId': this.servicioSeleccionado ? this.servicioSeleccionado.id : 0,
                'cantidad': this.cantidadPedido ? this.cantidadPedido : 1,
                'detalle': this.detallePedido ? this.detallePedido : '',
                'comercialId': this.comercialId
            })
                .then(response => {
                    this.alerta = true;
                    this.mensajeAlertLogin = 'Pedido guardado correctamente.';
                    this.dialogNuevoPedido = false;
                    this.limpiarDialogNuevoPedido();
                    this.ifCargando = false;
                    this.cargarPedidos();
                })
                .catch(error => {
                    console.error('Error al guardar el pedido:', error);
                    this.alerta = true;
                    this.mensajeAlertLogin = 'Error al guardar el pedido.';
                });
        },

        cargarPedidos() {
            axios.post(this.baseURL + 'api/cargarPedidos')
                .then(response => {
                    this.listaPedidos = response.data.data;
                    this.listaPedidos = this.listaPedidos.map(pedido => ({
                        id: pedido.pe_id,
                        fechaPedido: pedido.pe_fecha,
                        nitProspecto: pedido.prosp_nit,
                        nomProspecto: pedido.prosp_nom,
                        telProspecto: pedido.props_tel,
                        nomContacto: pedido.cont_nom,
                        celContacto: pedido.cont_cel,
                        nomProducto: pedido.prod_nom,
                        ctaProducto: pedido.prco_cta,
                        estadoNombre: pedido.est_nombre,
                        comNombre: pedido.com_nom,
                    }));

                    this.totalPedidos = this.listaPedidos.length;
                    this.totalNuevos = this.listaPedidos.filter(p => p.estadoNombre == 'Nuevo').length;
                    this.totalEnProceso = this.listaPedidos.filter(p => p.estadoNombre == 'En proceso').length;
                    this.totalEntregados = this.listaPedidos.filter(p => p.estadoNombre == 'Entregado').length;
                    this.totalCancelados = this.listaPedidos.filter(p => p.estadoNombre == 'Cancelado').length;

                    // Actualizar los headers de la tabla
                    this.headersProductos = [
                        { title: 'ID', key: 'id' },
                        { title: 'Fecha Pedido', key: 'fechaPedido' },
                        { title: 'NIT del Prospecto', key: 'nitProspecto' },
                        { title: 'Nombre del Prospecto', key: 'nomProspecto' },
                        { title: 'Telefono del Prospecto', key: 'telProspecto' },
                        { title: 'Nombre del Contacto', key: 'nomContacto' },
                        { title: 'Celular del Contacto', key: 'celContacto' },
                        { title: 'Nombre del Producto', key: 'nomProducto' },
                        { title: 'CTA del Producto', key: 'ctaProducto' },
                        { title: 'Estado', key: 'estadoNombre' },
                        { title: 'Comercial', key: 'comNombre' },
                    ];

                    this.iniciarChart();
                })
                .catch(error => {
                    console.error('Error al cargar pedidos:', error);
                });
        },

        formatDate(dateString) {
            if (!dateString) {
                return '';
            }

            try {
                // Si ya viene como objeto Date o como string GMT
                if (dateString instanceof Date || dateString.includes('GMT')) {
                    const date = new Date(dateString);

                    return date.toLocaleString('es-CO', {
                        year: '2-digit',
                        month: '2-digit',
                        day: '2-digit',
                        hour: '2-digit',
                        minute: '2-digit',
                        hour12: true
                    }).replace(',', '');
                }

                // Si viniera como 'YYYY-MM-DD HH:mm:ss.SSS'
                const [datePart, timePart] = dateString.split(' ');
                const [year, month, day] = datePart.split('-').map(Number);
                const [hour, minute, secondWithMs] = timePart.split(':');
                const second = parseInt(secondWithMs.split('.')[0]);

                const date = new Date(year, month - 1, day, parseInt(hour), parseInt(minute), second);

                return date.toLocaleString('es-CO', {
                    year: '2-digit',
                    month: '2-digit',
                    day: '2-digit',
                    hour: '2-digit',
                    minute: '2-digit',
                    hour12: true
                }).replace(',', '');
            } catch (error) {
                console.error('Error al formatear fecha:', dateString, error);
                return dateString;
            }
        },

        limpiarDialogNuevoPedido() {
            this.empresaSeleccionada = null;
            this.contactoSeleccionado = null;
            this.servicioSeleccionado = null;
            this.cantidadPedido = null;
            this.detallePedido = null;
            this.errorEmpresa = false;
            this.errorContacto = false;
            this.errorServicio = false;
            this.errorCantidad = false;
        },

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

        iniciarChart() {
            this.$nextTick(() => {
                const canvas = this.$refs.myChart;
                if (canvas) {
                    const ctx = canvas.getContext('2d');

                    if (this.chartInstance) {
                        this.chartInstance.destroy();
                    }

                    const servicio1 = this.listaPedidos.filter(p => p.nomProducto === 'Siicsa Bot').length ? this.listaPedidos.filter(p => p.nomProducto === 'Siicsa Bot').length : 0;
                    const servicio2 = this.listaPedidos.filter(p => p.nomProducto === 'Siicsa Cloud').length ? this.listaPedidos.filter(p => p.nomProducto === 'Siicsa Cloud').length : 0;
                    const servicio3 = this.listaPedidos.filter(p => p.nomProducto === 'Siicsa IT Support').length ? this.listaPedidos.filter(p => p.nomProducto === 'Siicsa IT Support').length : 0;
                    const servicio4 = this.listaPedidos.filter(p => p.nomProducto === 'Siicsa Training').length ? this.listaPedidos.filter(p => p.nomProducto === 'Siicsa Training').length : 0;
                    const servicio5 = this.listaPedidos.filter(p => p.nomProducto === 'SIESA MOV').length ? this.listaPedidos.filter(p => p.nomProducto === 'SIESA MOV').length : 0;
                    const servicio6 = this.listaPedidos.filter(p => p.nomProducto === 'SIESA Soporte').length ? this.listaPedidos.filter(p => p.nomProducto === 'SIESA Soporte').length : 0;
                    const servicio7 = this.listaPedidos.filter(p => p.nomProducto === 'Presentación Corporativa').length ? this.listaPedidos.filter(p => p.nomProducto === 'Presentación Corporativa').length : 0;
                    const servicio8 = this.listaPedidos.filter(p => p.nomProducto === 'Presentacion Comercial').length ? this.listaPedidos.filter(p => p.nomProducto === 'Presentacion Comercial').length : 0;

                    this.dataChart = [servicio1, servicio2, servicio3, servicio4, servicio5, servicio6, servicio7, servicio8];

                    this.chartInstance = new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: ['SIICSA Bot', 'SIICSA Cloud', 'SIICSA IT Support', 'SIICSA Training', 'SIESA MOV', 'SIESA Soporte', 'Presentación Corporativa', 'Presentación Comercial'],
                            datasets: [{
                                label: 'Pedidos por Servicio',
                                data: this.dataChart,
                                backgroundColor: [
                                    '#FBC02D', // Amarillo
                                    '#2196F3', // Azul
                                    '#D32F2F', // Rojo
                                    '#388E3C', // Verde
                                    '#8E24AA', // Morado
                                    '#F57C00', // Naranja
                                    '#BDBDBD', // Gris rata
                                    '#757575', // negro claro
                                ],
                                borderRadius: 10,
                                borderSkipped: false, // Para redondeo completo en todas las esquinas
                            }]
                        },
                        options: {
                            responsive: true,
                            plugins: {
                                legend: {
                                    display: true,
                                },
                                tooltip: {
                                    enabled: true,
                                }
                            },
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    min: 0,
                                    ticks: {
                                        stepSize: 1
                                    }
                                }
                            }
                        }
                    });
                } else {
                    console.error('Canvas no disponible en $refs.myChart');
                }
            });


            this.$nextTick(() => {
                const canvas = this.$refs.myChart2;
                if (canvas) {
                    const ctx = canvas.getContext('2d');

                    if (this.chartInstance2) {
                        this.chartInstance2.destroy();
                    }

                    this.dataChart2 = [this.totalNuevos, this.totalEnProceso, this.totalEntregados, this.totalCancelados];

                    this.chartInstance2 = new Chart(ctx, {
                        type: 'doughnut',
                        data: {
                            labels: ['Nuevos', 'En Proceso', 'Entregados', 'Cancelados'],
                            datasets: [{
                                label: 'PQRs',
                                data: this.dataChart2,
                                backgroundColor: [
                                    '#4CAF50',
                                    '#006CA1',
                                    '#FFC107',
                                    '#F44336',

                                ],
                                borderColor: '#fff',
                                borderWidth: 2
                            }]
                        },
                        options: {
                            responsive: true,
                            plugins: {
                                legend: {
                                    position: 'bottom'
                                },
                                tooltip: {
                                    callbacks: {
                                        label: function (context) {
                                            return `${context.label}: ${context.raw}`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                } else {
                    console.error('Canvas circularChart no disponible');
                }
            });
        },

        cerrarDIV() {
            this.alerta = false;
        },

        getAlertStyle() {
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
        },

        irHome() {
            this.$router.push('/comercial');
        },

        actualizarImagen(url) {
            this.imagenComercial = url;
        },

        setMenuActivoPorRuta() {
            const path = (this.$route.path || '').toLowerCase();
            if (path.includes('/vercampanas')) this.menuActivo = '/vercampanas';
            else if (path.includes('/campana')) this.menuActivo = '/campana';
            else if (path.includes('/contactos')) this.menuActivo = '/contactos';
            else if (path.includes('/prospeccion-telefonica')) this.menuActivo = '/prospeccion-telefonica';
            else if (path.includes('/seguimiento-llamadas')) this.menuActivo = '/seguimiento-llamadas';
            else if (path.includes('/informes-campanas')) this.menuActivo = '/informes-campanas';
            else if (path.includes('/comercial')) this.menuActivo = '/comercial';
            else if (path.includes('/pendiente-general')) this.menuActivo = '/pendiente-general';
            else if (path.includes('/pedidos')) this.menuActivo = '/pedidos'

            // ...agrega más si tienes otras rutas...
            else this.menuActivo = '';
        },


    }
}

</script>

<style scoped>
.rounded-lg {
    border-radius: 12px;

}

.texto-limitado {
    max-width: 350px;
    /* Puedes ajustar este valor */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

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
}

.menu-item-activo {
  background: #fff !important;
  color: #006CA1 !important;
  border-radius: 12px !important;
  box-shadow: 0 2px 12px 0 #006ca11a;
  transition: background 0.2s, color 0.2s;
  padding-top: 5px;
  padding-bottom: 5px;
}
.menu-item-activo .v-list-item-title,
.menu-item-activo .v-icon {
  color: #006CA1 !important;
}

</style>