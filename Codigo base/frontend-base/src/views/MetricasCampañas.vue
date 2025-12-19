<template>
    <v-app>
        <AppHeader :imagenComercial="imagenComercial" />
        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
                <!--SECCIÓN TITULO DE LA PAGINA-->
                <v-card elevation="3" class="pa-5 mb-6"
                    style="border-radius:18px; background: linear-gradient(90deg, #f5f7fa 100%, #e3f6ff 100%); box-shadow: 0 4px 24px rgba(0,0,0,0.07);">
                    <v-row class="align-center justify-space-between">
                        <v-col>
                            <div>
                                <h2 class="mb-1"
                                    style="font-weight:750; font-size:1.3rem; color:#0A1C3A; letter-spacing:-1px;">
                                    Métricas de campañas</h2>
                                <div style="font-size:0.9rem; color:#4B5563; font-weight:500;">
                                    Panel analítico de SIICSA-BOT — Interacciones por canal y rendimiento por campaña.
                                </div>
                            </div>
                        </v-col>
                        <v-col cols="auto" class="d-flex align-center" style="gap:12px;">
                            <v-btn color="#1565c0" dark rounded size="large" elevation="2">
                                <v-icon left size="20">mdi-file-excel</v-icon>
                                Exportar Excel
                            </v-btn>
                            <v-btn color="#3f94e8" dark rounded size="large" elevation="2">
                                <v-icon left size="20" color="white">mdi-file-pdf-box</v-icon>
                                <span color="white">Exportar PDF</span>
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card>
                <!--SECCIÓN TITULO DE LA PAGINA-->

                <!--SECCIÓN FILTROS-->

                <v-card elevation="3" class="pa-4 mb-4 "
                    style="border-radius:18px; background: linear-gradient(90deg, #f5f7fa 100%, #e3f6ff 100%); box-shadow: 0 4px 24px rgba(0,0,0,0.07);">
                    <v-row class="" style="gap:0px; align-items: flex-end;">
                        <v-col cols="12" md="2">
                            <h2 class="mb-1"
                                style="font-weight:750; font-size:1.3rem; color:#0A1C3A; letter-spacing:-1px;">
                                Filtrar las Campañas</h2>
                            <div style="font-weight:400; color:#0A1C3A; font-size:0.9rem; margin-bottom:2px;">Fecha de
                                inicio
                                <v-icon color="#006CA1">mdi mdi-calendar-account</v-icon>
                            </div>
                            <v-text-field v-model="filtroFechaInicio" placeholder="dd/mm/aaaa" variant="outlined"
                                type="date" density="compact" hide-details>
                                <template #append-inner>
                                    <v-icon icon="mdi-calendar" size="20" color="#006CA1" />
                                </template>
                            </v-text-field>
                        </v-col>
                        <v-col cols="12" md="2">
                            <div style="font-weight:400; color:#0A1C3A; font-size:0.9rem; margin-bottom:2px;">Fecha de
                                fin
                                <v-icon color="#006CA1">mdi mdi-calendar-account</v-icon>
                            </div>
                            <v-text-field v-model="filtroFechaFin" placeholder="dd/mm/aaaa" variant="outlined"
                                type="date" density="compact" hide-details>
                                <template #append-inner>
                                    <v-icon icon="mdi-calendar" size="20" color="#006CA1" />
                                </template>
                            </v-text-field>
                        </v-col>
                        <v-col cols="12" md="2">
                            <div style="font-weight:500; color:#0A1C3A; font-size:0.9rem; margin-bottom:2px;">Sector
                                <v-icon color="#006CA1">mdi-office-building</v-icon>
                            </div>
                            <v-autocomplete v-model="filtroSector" :items="ListaSectores" variant="outlined"
                                density="compact" hide-details clearable />
                        </v-col>
                        <v-col cols="12" md="2">
                            <div style="font-weight:500; color:#0A1C3A; font-size:0.9rem; margin-bottom:2px;">Ciudad
                                <v-icon color="#006CA1">mdi-city-variant</v-icon>
                            </div>
                            <v-autocomplete v-model="filtroCiudad" :items="ListaCiudades" variant="outlined"
                                density="compact" hide-details clearable />
                        </v-col>
                        <v-col cols="12" md="2">
                            <div style="font-weight:500; color:#0A1C3A; font-size:0.9rem; margin-bottom:2px;">Canal
                                <v-icon color="#006CA1">mdi-format-list-bulleted-type</v-icon>
                            </div>
                            <v-autocomplete v-model="filtroCanal" :items="ListaCanales" variant="outlined"
                                density="compact" hide-details clearable />
                        </v-col>
                        <v-col cols="12" md="2">
                            <div style="font-weight:500; color:#0A1C3A; font-size:0.9rem; margin-bottom:2px;">Nombre de
                                campaña
                                <v-icon color="#006CA1">mdi mdi-calendar-account</v-icon>
                            </div>
                            <v-autocomplete v-model="filtroNombreCampania" placeholder="Nombre de las Campañas"
                                variant="outlined" density="compact" clearable hide-details />
                        </v-col>
                        <v-col cols="12" md="2" class="d-flex flex-column justify-center align-center">
                            <v-btn color="#006CA1" style="float: right;" class="btn-grow-card d-flex justify-center">
                                <v-icon icon="mdi mdi-reload" class="mr-2"></v-icon>
                                Restablecer filtros
                            </v-btn>
                        </v-col>
                        <v-col cols="12" md="4" class="d-flex align-center">
                            <span class="mb-1" style="color:#64748B; font-size:1.05rem; font-weight:500;">
                                {{ CampaniasFiltradas.length }} campañas coinciden con los filtros.
                            </span>
                        </v-col>
                    </v-row>
                </v-card>
                <!--SECCIÓN FILTROS-->

                <!--SECCIÓN AVISOS-->
                <v-row no-gutters class="mb-2 d-flex justify-space-between " style="align-items: center;">
                    <v-col cols="12" md="2"
                        style="flex: 1 1 20%; max-width: 20%; padding-left: 14px; padding-right: 14px; ">
                        <v-card elevation="3" class="pa-3 justify-center align-center btn-grow-card"
                            style="border-radius:16px; background:#1565c0; color:white; width: 100%; min-width: 210px;">
                            <div class="d-flex justify-center" style="font-size:0.8rem; font-weight:700;">CAMPAÑAS
                                TOTALES</div>
                            <div class="d-flex justify-center" style="font-size:1.1rem; font-weight:800;">
                                {{ListaCampanias.length }}</div>
                            <div class="d-flex justify-center" style="font-size:0.8rem; opacity:0.85;">Periodo
                                seleccionado
                            </div>
                        </v-card>
                    </v-col>
                    <v-col cols="12" md="2"
                        style="flex: 1 1 20%; max-width: 20%; padding-left: 14px; padding-right: 14px;">
                        <v-card elevation="2" class="pa-3 btn-grow-card"
                            style="border-radius:16px; background:#3f94e8; color:white; width: 100%; min-width: 210px;">
                            <div class="d-flex justify-center" style="font-size:0.8rem; font-weight:700;">CAMPAÑAS
                                ENTREGADAS
                            </div>
                            <div class="d-flex justify-center" style="font-size:1.1rem; font-weight:800; ">{{
                                CampaniasFiltradas.filter(c => c.entregada).length}}</div>
                            <div class="d-flex justify-center" style="font-size:0.8rem; opacity:0.85;">Registradas como
                                enviadas
                            </div>
                            <v-icon color="white"
                                style="position:absolute; top:12px; right:16px;">mdi-email-send</v-icon>
                        </v-card>
                    </v-col>
                    <v-col cols="12" md="2"
                        style="flex: 1 1 20%; max-width: 20%; padding-left: 14px; padding-right: 14px;">
                        <v-card elevation="2" class="pa-3 btn-grow-card"
                            style="border-radius:16px; background:#19bf56; color:white; width: 100%; min-width: 210px;">
                            <div class="d-flex justify-center" style="font-size:0.8rem; font-weight:700;">INTERÉS
                                POSITIVO
                            </div>
                            <div class="d-flex justify-center" style="font-size:1.1rem; font-weight:800;">{{
                                CampaniasFiltradas.reduce((acc, c) => acc + (c.positivas || 0), 0)}}</div>
                            <div class="d-flex justify-center" style="font-size:0.8rem; opacity:0.85;">Total respuestas
                            </div>
                            <div class="d-flex justify-center" style="position:absolute; top:12px; right:16px;">
                            </div>
                        </v-card>
                    </v-col>
                    <v-col cols="12" md="2"
                        style="flex: 1 1 20%; max-width: 20%; padding-left: 14px; padding-right: 8px;">
                        <v-card elevation="2" class="pa-3 btn-grow-card"
                            style="border-radius:16px; background:#de8d04; color:white; width: 100%; min-width: 210px;">
                            <div class="d-flex justify-center" style="font-size:0.8rem; font-weight:700;">INTERÉS
                                NEGATIVO</div>
                            <div class="d-flex justify-center" style="font-size:1.1rem; font-weight:800;">{{
                                CampaniasFiltradas.reduce((acc, c) => acc + (c.negativas || 0), 0)}}</div>
                            <div class="d-flex justify-center" style="font-size:0.8rem; opacity:0.85;">Total respuestas
                            </div>
                        </v-card>
                    </v-col>
                    <v-col cols="12" md="2"
                        style="flex: 1 1 20%; max-width: 20%; padding-left: 8px; padding-right: 8px;">
                        <v-card elevation="2" class="pa-3 btn-grow-card"
                            style="border-radius:16px; background:#454a52; color:white; width: 100%; min-width: 210px;">
                            <div class="d-flex justify-center" style="font-size:0.8rem; font-weight:700;">SIN RESPUESTA
                            </div>
                            <div class="d-flex justify-center" style="font-size:1.1rem; font-weight:800; ">{{
                                CampaniasFiltradas.reduce((acc, c) => acc + (c.sinRespuesta || 0), 0)}}</div>
                            <div class="d-flex justify-center" style="font-size:0.8rem; opacity:0.85;">Total</div>
                        </v-card>
                    </v-col>
                </v-row>
                <!--SECCIÓN AVISOS-->

            </v-container>
        </v-main>
    </v-app>
</template>

<script>
import AppHeader from '../components/AppHeader.vue';
import axios from 'axios';
import CryptoJS from "crypto-js";

import {
  Chart,
  BarController, BarElement,
  CategoryScale, LinearScale,
  DoughnutController, ArcElement,
  Tooltip, Legend,
} from 'chart.js';

Chart.register(DoughnutController, ArcElement, Tooltip, Legend);
Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend);


export default {
    components: {
        AppHeader
    },
    data: () => ({
        baseURL: '', // URL base de la API
        comercialId: 0, // ID del usuario comercial
        idCargo: null, // ID del cargo del usuario
        nombreComercial: null, // Nombre del usuario comercial
        correoUsuario: null, // Correo del usuario
        imagenComercial: '', // Imagen del usuario

        mensajeAlert: null,
        alerta: false,
        ifCargando: false,
        listaUsuarios: [],

        CHANNEL_COLORS: {
            Telefónico: "#006CA1",
            WhatsApp: "#22C55E",
            Email: "#F59E0B",
        },
        ICONO_CANAL: {
            Telefónico: "☎️",
            WhatsApp: "💬",
            Email: "✉️"
        },

        ListaCampanias: [
            { id: "CMP-001", nombre: "Prospección Telefónica – Julio", fecha: "2025-07-15", canal: "Telefónico", sector: "Automotriz", ciudad: "Cali", positivas: 45, negativas: 12, sinRespuesta: 18, entregada: true },
            { id: "CMP-002", nombre: "WhatsApp – Retail Agosto", fecha: "2025-08-02", canal: "WhatsApp", sector: "Retail", ciudad: "Bogotá", positivas: 62, negativas: 15, sinRespuesta: 20, entregada: true },
            { id: "CMP-003", nombre: "Emailing – Sector Salud", fecha: "2025-08-05", canal: "Email", sector: "Salud", ciudad: "Medellín", positivas: 28, negativas: 10, sinRespuesta: 42, entregada: true },
            { id: "CMP-004", nombre: "Telemarketing – B2B Cali", fecha: "2025-07-28", canal: "Telefónico", sector: "Servicios", ciudad: "Cali", positivas: 37, negativas: 9, sinRespuesta: 14, entregada: true },
            { id: "CMP-005", nombre: "WA – Seguimiento Leads", fecha: "2025-08-10", canal: "WhatsApp", sector: "Tecnología", ciudad: "Bogotá", positivas: 31, negativas: 22, sinRespuesta: 28, entregada: true },
            { id: "CMP-006", nombre: "Email – Promoción PYME", fecha: "2025-08-12", canal: "Email", sector: "PyME", ciudad: "Barranquilla", positivas: 19, negativas: 25, sinRespuesta: 51, entregada: true },
            { id: "CMP-007", nombre: "Telefónico – Reenganche", fecha: "2025-07-20", canal: "Telefónico", sector: "Industrial", ciudad: "Medellín", positivas: 29, negativas: 6, sinRespuesta: 9, entregada: true },
            { id: "CMP-008", nombre: "WhatsApp – Postventa", fecha: "2025-08-15", canal: "WhatsApp", sector: "Automotriz", ciudad: "Cali", positivas: 54, negativas: 11, sinRespuesta: 17, entregada: true },
        ],

        ListaProspecciones: [
            { fecha: "2025-08-01", "Prospección Telefónica – Julio": 20, "WhatsApp – Retail Agosto": 34, "Emailing – Sector Salud": 12 },
            { fecha: "2025-08-03", "Prospección Telefónica – Julio": 28, "WhatsApp – Retail Agosto": 38, "Emailing – Sector Salud": 15 },
            { fecha: "2025-08-06", "Prospección Telefónica – Julio": 24, "WhatsApp – Retail Agosto": 33, "Emailing – Sector Salud": 19 },
            { fecha: "2025-08-09", "Prospección Telefónica – Julio": 18, "WhatsApp – Retail Agosto": 42, "Emailing – Sector Salud": 14 },
            { fecha: "2025-08-12", "Prospección Telefónica – Julio": 16, "WhatsApp – Retail Agosto": 29, "Emailing – Sector Salud": 21 },
            { fecha: "2025-08-15", "Prospección Telefónica – Julio": 14, "WhatsApp – Retail Agosto": 36, "Emailing – Sector Salud": 17 },
        ],

        filtroFechaInicio: '',
        filtroFechaFin: '',
        filtroSector: '',
        filtroCiudad: '',
        filtroCanal: '',
        filtroNombreCampania: '',
    }),

    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.comercialId = localStorage.getItem('idUsuario');
        this.idCargo = localStorage.getItem('idCargo');
        this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');
        this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?${Date.now()}`;
        this.obtenerUsuarios();
    },

    computed: {
        CampaniasFiltradas() {
            return this.ListaCampanias.filter(c => {
                if (this.filtroFechaInicio && c.fecha < this.filtroFechaInicio) return false;
                if (this.filtroFechaFin && c.fecha > this.filtroFechaFin) return false;
                if (this.filtroSector && this.filtroSector !== 'Todos los sectores' && c.sector !== this.filtroSector) return false;
                if (this.filtroCiudad && this.filtroCiudad !== 'Todas las ciudades' && c.ciudad !== this.filtroCiudad) return false;
                if (this.filtroCanal && this.filtroCanal !== 'Todos' && c.canal !== this.filtroCanal) return false;
                if (this.filtroNombreCampania && this.filtroNombreCampania !== 'Todas las campañas' && c.nombre !== this.filtroNombreCampania) return false;
                return true;
            });
        },

        ListaSectores() {
            const sectores = this.CampaniasFiltradas.map(c => c.sector);
            return Array.from(new Set(sectores));
        },
        ListaCiudades() {
            const ciudades = this.CampaniasFiltradas.map(c => c.ciudad);
            return Array.from(new Set(ciudades));
        },
        ListaCanales() {
            const canales = this.CampaniasFiltradas.map(c => c.canal);
            return Array.from(new Set(canales));
        },
        ListaNombresCampania() {
            const nombres = this.CampaniasFiltradas.map(c => c.nombre);
            return Array.from(new Set(nombres));
        },

        canalDonutData() {
            const canales = ['Telefónico', 'WhatsApp', 'Email'];
            const counts = canales.map(canal =>
                this.ListaCampanias.filter(c => c.canal === canal).length
            );
            return {
                labels: canales,
                datasets: [{
                    data: counts,
                    backgroundColor: ['#1565c0', '#22C55E', '#F59E0B'],
                    borderWidth: 2
                }]
            };
        },
        canalDonutLegend() {
            return [
                { label: 'Telefónico', color: '#1565c0', icon: '☎️' },
                { label: 'WhatsApp', color: '#22C55E', icon: '💬' },
                { label: 'Email', color: '#F59E0B', icon: '✉️' }
            ];
        },


    },

    methods: {

        obtenerUsuarios() {
            axios.post(this.baseURL + "api/cargausus", {
                idusu: 0,
                tipo: 1, // 1 para cargar todos los Comerciales
            })
                .then((response) => {
                    this.listaUsuarios = response.data.data;
                    console.log("Lista de Usuarios:", this.listaUsuarios);
                })
                .catch((error) => {
                    console.error("Error al cargar usuarios:", error);
                });
        },
    }
}

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
}

.metric-card-col {
    align-items: stretch;
    padding-left: 0px;
    padding-right: 0px;
}

.metric-card {
    border-radius: 18px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.09);
    min-height: 120px;
    position: relative;
    transition: box-shadow 0.2s, transform 0.2s;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;
}

.metric-card:hover {
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.16);
    transform: translateY(-2px) scale(1.03);
}

.metric-header {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 2px;
}

.metric-title {
    letter-spacing: -1px;
    font-size: 0.95rem;
    font-weight: 700;
}

.metric-value {
    font-size: 2.1rem;
    font-weight: 800;
    margin: 8px 0 2px 0;
    letter-spacing: -2px;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.metric-desc {
    font-size: 0.92rem;
    opacity: 0.85;
    font-weight: 500;
}

.metric-total {
    background: linear-gradient(90deg, #1565c0 80%, #1976d2 100%);
}

.metric-entregadas {
    background: linear-gradient(90deg, #1976d2 80%, #2196f3 100%);
}

.metric-positivo {
    background: linear-gradient(90deg, #22c55e 80%, #16a34a 100%);
}

.metric-negativo {
    background: linear-gradient(90deg, #f59e0b 80%, #fbbf24 100%);
}

.metric-sinrespuesta {
    background: linear-gradient(90deg, #374151 80%, #64748B 100%);
}

.btn-grow-card {
    transition: transform 0.2s;
}

.btn-grow-card:hover {
    transform: scale(1.05);
    z-index: 1.5;
}

.btn-grow-card-items {
    transition: transform 0.2s;
}

.btn-grow-card-items:hover {
    transform: scale(1.01);
    z-index: 1.1;
}

.btn-grow-card-items-active {
    transition: transform 0.2s;
}

.btn-grow-card-items-active:hover {
    background-color: #9e2121 !important;
    /* rojo más oscuro, ajusta el alpha si quieres más intensidad */
}

.donut-legend {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.donut-legend-item {
    display: flex;
    align-items: center;
    font-size: 1rem;
}
</style>