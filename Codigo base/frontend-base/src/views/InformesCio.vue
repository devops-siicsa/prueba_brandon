<template>
    <v-app>
        <AppHeader :nombre-comercial="nombreComercial" :imagen-comercial="imagenComercial" :correo-usuario="correoUsuario"
            :comercial-id="comercialId" :base-u-r-l="baseURL" :idCargo="idCargo" v-model:drawer="drawer"
            @imagen-actualizada="actualizarImagen" @cerrar-sesion="cerrarSesion"></AppHeader>

        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
                
                <!-- Header Section con Filtros -->
                <v-row class="mb-4 align-center">
                    <v-col cols="12" md="6">
                        <div class="d-flex align-center gap-3">
                            <div class="d-flex align-center justify-center rounded-lg elevation-2"
                                style="width: 56px; height: 56px; background: linear-gradient(135deg, #006CA1 0%, #009B90 100%);">
                                <v-icon color="white" size="32">mdi-chart-box-multiple</v-icon>
                            </div>
                            <div>
                                <h2 class="text-h5 font-weight-bold text-blue-grey-darken-4 mb-0" style="line-height: 1.2;">
                                    Business Intelligence - CIO
                                </h2>
                                <div class="text-caption font-weight-bold text-uppercase" 
                                    style="color: #009B90; letter-spacing: 1px;">
                                    Dashboard de Análisis y Métricas
                                </div>
                            </div>
                        </div>
                    </v-col>

                    <v-col cols="12" md="6">
                        <div class="d-flex gap-2 align-center justify-end flex-wrap">
                            <v-select
                                v-model="periodoSeleccionado"
                                :items="periodos"
                                item-title="label"
                                item-value="value"
                                variant="outlined"
                                density="compact"
                                hide-details
                                class="compact-select"
                                style="max-width: 180px;"
                                prepend-inner-icon="mdi-calendar-clock"
                            ></v-select>
                            <v-text-field 
                                type="date" 
                                v-model="fechaInicio" 
                                label="Desde"
                                variant="outlined" 
                                density="compact" 
                                hide-details
                                clearable
                                class="compact-date-field"
                                style="max-width: 160px;"
                            ></v-text-field>
                            <v-text-field 
                                type="date" 
                                v-model="fechaFin" 
                                label="Hasta" 
                                variant="outlined" 
                                density="compact" 
                                hide-details
                                clearable
                                class="compact-date-field"
                                style="max-width: 160px;"
                            ></v-text-field>
                            <v-btn 
                                color="#006CA1" 
                                variant="flat" 
                                prepend-icon="mdi-refresh"
                                class="text-capitalize"
                                @click="cargarDatos"
                            >
                                Actualizar
                            </v-btn>
                            <v-btn
                                color="#009B90"
                                variant="flat"
                                prepend-icon="mdi-download"
                                class="text-capitalize"
                                @click="exportarPDF"
                            >
                                Exportar
                            </v-btn>
                        </div>
                    </v-col>
                </v-row>

                <!-- KPIs Principales -->
                <v-row class="mb-4">
                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-4 rounded-xl elevation-3 kpi-card" color="white">
                            <div class="d-flex justify-space-between align-center mb-2">
                                <div class="kpi-icon-wrapper" style="background: rgba(13, 71, 161, 0.1);">
                                    <v-icon color="#0D47A1" size="28">mdi-ticket-account</v-icon>
                                </div>
                                <v-chip size="small" color="success" variant="flat">
                                    <v-icon start size="16">mdi-trending-up</v-icon>
                                    +12%
                                </v-chip>
                            </div>
                            <h3 class="text-h4 font-weight-bold text-blue-grey-darken-4 mb-1">{{ kpiTotal }}</h3>
                            <p class="text-caption text-grey-darken-1 mb-0">Total de Solicitudes</p>
                            <v-progress-linear
                                :model-value="kpiTotal > 0 ? 85 : 0"
                                color="#0D47A1"
                                height="4"
                                rounded
                                class="mt-2"
                            ></v-progress-linear>
                        </v-card>
                    </v-col>

                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-4 rounded-xl elevation-3 kpi-card" color="white">
                            <div class="d-flex justify-space-between align-center mb-2">
                                <div class="kpi-icon-wrapper" style="background: rgba(76, 175, 80, 0.1);">
                                    <v-icon color="#4CAF50" size="28">mdi-check-circle</v-icon>
                                </div>
                                <v-chip size="small" color="success" variant="flat">
                                    96.5%
                                </v-chip>
                            </div>
                            <h3 class="text-h4 font-weight-bold text-blue-grey-darken-4 mb-1">{{ kpiResueltos }}</h3>
                            <p class="text-caption text-grey-darken-1 mb-0">Solicitudes Resueltas</p>
                            <v-progress-linear
                                :model-value="porcentajeResueltos"
                                color="#4CAF50"
                                height="4"
                                rounded
                                class="mt-2"
                            ></v-progress-linear>
                        </v-card>
                    </v-col>

                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-4 rounded-xl elevation-3 kpi-card" color="white">
                            <div class="d-flex justify-space-between align-center mb-2">
                                <div class="kpi-icon-wrapper" style="background: rgba(255, 152, 0, 0.1);">
                                    <v-icon color="#FF9800" size="28">mdi-clock-fast</v-icon>
                                </div>
                                <v-chip size="small" color="warning" variant="flat">
                                    <v-icon start size="16">mdi-clock-outline</v-icon>
                                    2.5h
                                </v-chip>
                            </div>
                            <h3 class="text-h4 font-weight-bold text-blue-grey-darken-4 mb-1">{{ kpiEnProceso }}</h3>
                            <p class="text-caption text-grey-darken-1 mb-0">En Proceso</p>
                            <v-progress-linear
                                :model-value="porcentajeEnProceso"
                                color="#FF9800"
                                height="4"
                                rounded
                                class="mt-2"
                            ></v-progress-linear>
                        </v-card>
                    </v-col>

                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-4 rounded-xl elevation-3 kpi-card" color="white">
                            <div class="d-flex justify-space-between align-center mb-2">
                                <div class="kpi-icon-wrapper" style="background: rgba(244, 67, 54, 0.1);">
                                    <v-icon color="#F44336" size="28">mdi-alert-circle</v-icon>
                                </div>
                                <v-chip size="small" color="error" variant="flat">
                                    Alta
                                </v-chip>
                            </div>
                            <h3 class="text-h4 font-weight-bold text-blue-grey-darken-4 mb-1">{{ kpiPrioridadAlta }}</h3>
                            <p class="text-caption text-grey-darken-1 mb-0">Prioridad Alta</p>
                            <v-progress-linear
                                :model-value="kpiTotal > 0 ? (kpiPrioridadAlta / kpiTotal * 100) : 0"
                                color="#F44336"
                                height="4"
                                rounded
                                class="mt-2"
                            ></v-progress-linear>
                        </v-card>
                    </v-col>
                </v-row>

                <!-- Métricas Secundarias -->
                <v-row class="mb-4">
                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-3 rounded-lg elevation-1" color="white">
                            <div class="d-flex align-center gap-3">
                                <v-avatar color="blue-lighten-5" size="48">
                                    <v-icon color="blue">mdi-speedometer</v-icon>
                                </v-avatar>
                                <div>
                                    <p class="text-caption text-grey-darken-1 mb-0">Tiempo Promedio</p>
                                    <h4 class="text-h6 font-weight-bold">3.2h</h4>
                                </div>
                            </div>
                        </v-card>
                    </v-col>

                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-3 rounded-lg elevation-1" color="white">
                            <div class="d-flex align-center gap-3">
                                <v-avatar color="green-lighten-5" size="48">
                                    <v-icon color="green">mdi-chart-line</v-icon>
                                </v-avatar>
                                <div>
                                    <p class="text-caption text-grey-darken-1 mb-0">Tasa Resolución</p>
                                    <h4 class="text-h6 font-weight-bold">89.7%</h4>
                                </div>
                            </div>
                        </v-card>
                    </v-col>

                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-3 rounded-lg elevation-1" color="white">
                            <div class="d-flex align-center gap-3">
                                <v-avatar color="purple-lighten-5" size="48">
                                    <v-icon color="purple">mdi-account-check</v-icon>
                                </v-avatar>
                                <div>
                                    <p class="text-caption text-grey-darken-1 mb-0">SLA Cumplido</p>
                                    <h4 class="text-h6 font-weight-bold">92.5%</h4>
                                </div>
                            </div>
                        </v-card>
                    </v-col>

                    <v-col cols="12" sm="6" md="3">
                        <v-card class="pa-3 rounded-lg elevation-1" color="white">
                            <div class="d-flex align-center gap-3">
                                <v-avatar color="orange-lighten-5" size="48">
                                    <v-icon color="orange">mdi-star</v-icon>
                                </v-avatar>
                                <div>
                                    <p class="text-caption text-grey-darken-1 mb-0">Satisfacción</p>
                                    <h4 class="text-h6 font-weight-bold">4.6/5.0</h4>
                                </div>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>

                <!-- Gráficos Principales -->
                <v-row class="mb-4">
                    <!-- Tendencia Temporal -->
                    <v-col cols="12" md="8">
                        <v-card class="pa-4 rounded-xl elevation-2">
                            <div class="d-flex justify-space-between align-center mb-4">
                                <div>
                                    <h3 class="text-h6 font-weight-bold text-grey-darken-3">Tendencia de Solicitudes</h3>
                                    <p class="text-caption text-grey-darken-1 mb-0">Últimos 30 días</p>
                                </div>
                                <v-btn-toggle v-model="graficoTipo" density="compact" divided>
                                    <v-btn value="dia" size="small">Día</v-btn>
                                    <v-btn value="semana" size="small">Semana</v-btn>
                                    <v-btn value="mes" size="small">Mes</v-btn>
                                </v-btn-toggle>
                            </div>
                            <div style="width: 100%; height: 350px;">
                                <canvas ref="chartTendencia"></canvas>
                            </div>
                        </v-card>
                    </v-col>

                    <!-- Distribución por Estado -->
                    <v-col cols="12" md="4">
                        <v-card class="pa-4 rounded-xl elevation-2" style="height: 100%;">
                            <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">Distribución por Estado</h3>
                            <p class="text-caption text-grey-darken-1 mb-4">Estado actual de solicitudes</p>
                            <div style="width: 100%; max-width: 280px; margin: 20px auto;">
                                <canvas ref="chartEstados"></canvas>
                            </div>
                            <div class="mt-4">
                                <div v-for="(item, index) in estadosData" :key="index" class="d-flex justify-space-between align-center mb-2">
                                    <div class="d-flex align-center gap-2">
                                        <div :style="`width: 12px; height: 12px; border-radius: 50%; background: ${item.color}`"></div>
                                        <span class="text-caption">{{ item.label }} ({{ item.count }})</span>
                                    </div>
                                    <span class="text-caption font-weight-bold">{{ item.value }}%</span>
                                </div>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>

                <!-- Análisis por Canal y Prioridad -->
                <v-row class="mb-4">
                    <!-- Solicitudes por Canal -->
                    <v-col cols="12" md="6">
                        <v-card class="pa-4 rounded-xl elevation-2">
                            <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">Solicitudes por Canal</h3>
                            <p class="text-caption text-grey-darken-1 mb-4">Distribución de canales de comunicación</p>
                            <div style="width: 100%; height: 300px;">
                                <canvas ref="chartCanales"></canvas>
                            </div>
                        </v-card>
                    </v-col>

                    <!-- Análisis por Prioridad -->
                    <v-col cols="12" md="6">
                        <v-card class="pa-4 rounded-xl elevation-2">
                            <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">Análisis por Prioridad</h3>
                            <p class="text-caption text-grey-darken-1 mb-4">Tiempo promedio de resolución</p>
                            <div style="width: 100%; height: 300px;">
                                <canvas ref="chartPrioridad"></canvas>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>

                <!-- Performance de Agentes y Categorías -->
                <v-row class="mb-4">
                    <!-- Top Agentes -->
                    <v-col cols="12" md="6">
                        <v-card class="pa-4 rounded-xl elevation-2">
                            <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">Performance de Agentes</h3>
                            <p class="text-caption text-grey-darken-1 mb-4">Top 5 agentes por resoluciones</p>
                            <div v-for="(agente, index) in topAgentes" :key="index" class="mb-3">
                                <div class="d-flex justify-space-between align-center mb-1">
                                    <div class="d-flex align-center gap-2">
                                        <v-avatar size="32" :color="agente.color">
                                            <span class="text-white text-caption font-weight-bold">{{ agente.iniciales }}</span>
                                        </v-avatar>
                                        <span class="text-body-2 font-weight-medium">{{ agente.nombre }}</span>
                                    </div>
                                    <span class="text-caption font-weight-bold">{{ agente.resueltos }}</span>
                                </div>
                                <v-progress-linear
                                    :model-value="agente.porcentaje"
                                    :color="agente.color"
                                    height="8"
                                    rounded
                                ></v-progress-linear>
                            </div>
                        </v-card>
                    </v-col>

                    <!-- Top Categorías -->
                    <v-col cols="12" md="6">
                        <v-card class="pa-4 rounded-xl elevation-2">
                            <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">Top Categorías</h3>
                            <p class="text-caption text-grey-darken-1 mb-4">Categorías más frecuentes</p>
                            <div style="width: 100%; height: 280px;">
                                <canvas ref="chartCategorias"></canvas>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>

                <!-- Métricas de Tiempo -->
                <v-row class="mb-4">
                    <v-col cols="12">
                        <v-card class="pa-4 rounded-xl elevation-2">
                            <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">Métricas de Tiempo de Respuesta</h3>
                            <p class="text-caption text-grey-darken-1 mb-4">Análisis detallado de tiempos</p>
                            <div style="width: 100%; height: 300px;">
                                <canvas ref="chartTiempos"></canvas>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>

            </v-container>
        </v-main>
    </v-app>
</template>

<script>
import {
    Chart,
    LineController,
    BarController,
    LineElement,
    BarElement,
    PointElement,
    CategoryScale,
    LinearScale,
    Tooltip,
    Legend,
    Filler,
    ArcElement,
    DoughnutController,
} from 'chart.js';

import AppHeader from '../components/AppHeader.vue';
import axios from 'axios';
import jsPDF from 'jspdf';

// Registrar componentes de Chart.js
Chart.register(
    LineController,
    BarController,
    LineElement,
    BarElement,
    PointElement,
    CategoryScale,
    LinearScale,
    Tooltip,
    Legend,
    Filler,
    ArcElement,
    DoughnutController
);

export default {
    name: 'InformesCio',
    components: {
        AppHeader,
    },
    data() {
        return {
            drawer: false,
            nombreComercial: '',
            imagenComercial: '',
            correoUsuario: '',
            comercialId: '',
            idCargo: '',
            baseURL: 'http://localhost:5000/',
            fechaInicio: null,
            fechaFin: null,
            periodoSeleccionado: '30dias',
            periodos: [
                { label: 'Últimos 7 días', value: '7dias' },
                { label: 'Últimos 30 días', value: '30dias' },
                { label: 'Últimos 90 días', value: '90dias' },
                { label: 'Este mes', value: 'mes' },
                { label: 'Personalizado', value: 'custom' }
            ],
            graficoTipo: 'dia',
            // Datos que vienen del backend
            metricas: null,
            loading: false,
            // Referencias de charts
            chartInstances: {
                tendencia: null,
                estados: null,
                canales: null,
                prioridad: null,
                categorias: null,
                tiempos: null
            }
        };
    },
    mounted() {
        this.cargarDatosUsuario();
        this.configurarFechasIniciales();
        this.cargarDatos();
    },
    computed: {
        kpiTotal() {
            return this.metricas ? this.metricas.total : 0;
        },
        kpiResueltos() {
            return this.metricas ? (this.metricas.estados['Resuelto'] || 0) : 0;
        },
        kpiEnProceso() {
            return this.metricas ? (this.metricas.estados['En Proceso'] || 0) : 0;
        },
        kpiPrioridadAlta() {
            return this.metricas ? (this.metricas.prioridades['Alta'] || 0) : 0;
        },
        porcentajeResueltos() {
            if (!this.metricas || this.metricas.total === 0) return 0;
            return ((this.kpiResueltos / this.metricas.total) * 100).toFixed(1);
        },
        porcentajeEnProceso() {
            if (!this.metricas || this.metricas.total === 0) return 0;
            return ((this.kpiEnProceso / this.metricas.total) * 100).toFixed(1);
        },
        estadosData() {
            if (!this.metricas) return [];
            const total = this.metricas.total || 1;
            const estados = this.metricas.estados || {};
            
            const colores = {
                'Nuevo': '#4CAF50',
                'En Proceso': '#FF9800',
                'Resuelto': '#2196F3',
                'Escalar': '#F44336'
            };
            
            return Object.keys(estados).map(estado => ({
                label: estado,
                value: ((estados[estado] / total) * 100).toFixed(1),
                count: estados[estado],
                color: colores[estado] || '#9E9E9E'
            }));
        },
        topAgentes() {
            if (!this.metricas || !this.metricas.agentes) return [];
            
            const agentes = Object.entries(this.metricas.agentes)
                .map(([nombre, count]) => ({
                    nombre,
                    iniciales: this.obtenerIniciales(nombre),
                    resueltos: count,
                    porcentaje: 0
                }))
                .sort((a, b) => b.resueltos - a.resueltos)
                .slice(0, 5);
            
            if (agentes.length === 0) return [];
            
            const maxResueltos = agentes[0].resueltos;
            const colores = ['#0D47A1', '#1976D2', '#2196F3', '#42A5F5', '#64B5F6'];
            
            agentes.forEach((agente, index) => {
                agente.porcentaje = maxResueltos > 0 ? (agente.resueltos / maxResueltos) * 100 : 0;
                agente.color = colores[index] || '#9E9E9E';
            });
            
            return agentes;
        }
    },
    methods: {
        cargarDatosUsuario() {
            this.nombreComercial = localStorage.getItem('nombreComercial') || '';
            this.correoUsuario = localStorage.getItem('correoUsuario') || '';
            this.comercialId = localStorage.getItem('comercialId') || '';
            this.idCargo = localStorage.getItem('idCargo') || '';

            const savedImage = localStorage.getItem('imagenComercial');
            if (savedImage) {
                this.imagenComercial = savedImage;
            } else if (this.comercialId) {
                this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?t=${Date.now()}`;
            } else {
                this.imagenComercial = '';
            }
        },
        actualizarImagen(nuevaImagen) {
            this.imagenComercial = nuevaImagen;
            localStorage.setItem('imagenComercial', nuevaImagen);
        },
        cerrarSesion() {
            localStorage.clear();
            this.$router.push('/');
        },
        configurarFechasIniciales() {
            const hoy = new Date();
            this.fechaFin = hoy.toISOString().split('T')[0];
            
            const hace30Dias = new Date();
            hace30Dias.setDate(hace30Dias.getDate() - 30);
            this.fechaInicio = hace30Dias.toISOString().split('T')[0];
        },
        async cargarDatos() {
            this.loading = true;
            try {
                // Usar el mismo endpoint que Pqr.vue para obtener los datos crudos
                const response = await axios.post(this.baseURL + 'api/cargarpqrs', {
                    'idusu': localStorage.getItem('idUsuario') || this.comercialId || 0,
                });

                if (response.data.status === 'success') {
                    const tickets = response.data.data;
                    this.metricas = this.calcularMetricas(tickets);
                    this.$nextTick(() => {
                        this.actualizarCharts();
                    });
                }
            } catch (error) {
                console.error('Error cargando métricas:', error);
            } finally {
                this.loading = false;
            }
        },

        calcularMetricas(tickets) {
            // Filtrar por fechas si es necesario
            let ticketsFiltrados = tickets;
            if (this.fechaInicio && this.fechaFin) {
                const start = new Date(this.fechaInicio);
                const end = new Date(this.fechaFin);
                end.setHours(23, 59, 59, 999); // Final del día

                ticketsFiltrados = tickets.filter(t => {
                    const fecha = new Date(t.fecha_ingreso);
                    return fecha >= start && fecha <= end;
                });
            }

            const metricas = {
                total: ticketsFiltrados.length,
                estados: {},
                prioridades: {},
                tendencia_dias: {},
                canales: {},
                agentes: {},
                categorias: {}
            };

            ticketsFiltrados.forEach(t => {
                // Estados
                const estado = t.estado || 'Desconocido';
                metricas.estados[estado] = (metricas.estados[estado] || 0) + 1;

                // Prioridades
                const prioridad = t.prioridad || 'Sin Prioridad';
                metricas.prioridades[prioridad] = (metricas.prioridades[prioridad] || 0) + 1;

                // Tendencia (Fecha Ingreso)
                if (t.fecha_ingreso) {
                    const fecha = t.fecha_ingreso.split('T')[0]; // YYYY-MM-DD
                    metricas.tendencia_dias[fecha] = (metricas.tendencia_dias[fecha] || 0) + 1;
                }

                // Canales
                const canal = t.canal || 'Otro';
                metricas.canales[canal] = (metricas.canales[canal] || 0) + 1;

                // Agentes
                const agente = t.com_nom || 'Sin Asignar';
                metricas.agentes[agente] = (metricas.agentes[agente] || 0) + 1;

                // Categorias
                const categoria = t.categoria_pqr || 'Sin Categoría';
                metricas.categorias[categoria] = (metricas.categorias[categoria] || 0) + 1;
            });

            return metricas;
        },
        obtenerIniciales(nombre) {
            if (!nombre) return 'NA';
            const partes = nombre.trim().split(' ');
            if (partes.length >= 2) {
                return (partes[0][0] + partes[1][0]).toUpperCase();
            }
            return nombre.substring(0, 2).toUpperCase();
        },
        exportarPDF() {
            const pdf = new jsPDF('p', 'mm', 'a4');
            pdf.text('Informe Business Intelligence CIO', 10, 10);
            pdf.save('informe-cio.pdf');
        },
        actualizarCharts() {
            // Destruir charts anteriores si existen
            Object.values(this.chartInstances).forEach(chart => {
                if (chart) chart.destroy();
            });
            
            // Crear nuevos charts
            this.crearGraficoTendencia();
            this.crearGraficoEstados();
            this.crearGraficoCanales();
            this.crearGraficoPrioridad();
            this.crearGraficoCategorias();
            this.crearGraficoTiempos();
        },
        crearGraficoTendencia() {
            const canvas = this.$refs.chartTendencia;
            if (!canvas || !this.metricas) return;

            const tendencia = this.metricas.tendencia_dias || {};
            const fechasOrdenadas = Object.keys(tendencia).sort();
            
            const labels = fechasOrdenadas.map(fecha => {
                const f = new Date(fecha);
                return `${f.getDate()}/${f.getMonth() + 1}`;
            });
            
            const dataSolicitudes = fechasOrdenadas.map(fecha => tendencia[fecha]);
            
            // Calcular resueltos acumulados (simulación)
            const dataResueltos = dataSolicitudes.map((val, idx) => 
                Math.floor(val * (0.6 + (idx / fechasOrdenadas.length) * 0.3))
            );

            const ctx = canvas.getContext('2d');
            this.chartInstances.tendencia = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Solicitudes Recibidas',
                            data: dataSolicitudes,
                            borderColor: '#0D47A1',
                            backgroundColor: 'rgba(13, 71, 161, 0.1)',
                            borderWidth: 3,
                            fill: true,
                            tension: 0.4,
                            pointBackgroundColor: '#0D47A1',
                            pointBorderColor: '#fff',
                            pointBorderWidth: 2,
                            pointRadius: 5,
                            pointHoverRadius: 7
                        },
                        {
                            label: 'Solicitudes Resueltas',
                            data: dataResueltos,
                            borderColor: '#4CAF50',
                            backgroundColor: 'rgba(76, 175, 80, 0.1)',
                            borderWidth: 3,
                            fill: true,
                            tension: 0.4,
                            pointBackgroundColor: '#4CAF50',
                            pointBorderColor: '#fff',
                            pointBorderWidth: 2,
                            pointRadius: 5,
                            pointHoverRadius: 7
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top',
                            labels: {
                                usePointStyle: true,
                                padding: 15,
                                font: { size: 12 }
                            }
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            padding: 12,
                            titleColor: '#fff',
                            bodyColor: '#fff',
                            borderColor: '#006CA1',
                            borderWidth: 1
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)',
                                drawBorder: false
                            },
                            ticks: {
                                font: { size: 11 }
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                font: { size: 11 }
                            }
                        }
                    },
                    interaction: {
                        mode: 'nearest',
                        axis: 'x',
                        intersect: false
                    }
                }
            });
        },
        crearGraficoEstados() {
            const canvas = this.$refs.chartEstados;
            if (!canvas || !this.metricas) return;

            const estados = this.metricas.estados || {};
            const colores = {
                'Nuevo': '#4CAF50',
                'En Proceso': '#FF9800',
                'Resuelto': '#2196F3',
                'Escalar': '#F44336'
            };
            
            const labels = Object.keys(estados);
            const data = Object.values(estados);
            const backgroundColor = labels.map(label => colores[label] || '#9E9E9E');

            const ctx = canvas.getContext('2d');
            this.chartInstances.estados = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        data: data,
                        backgroundColor: backgroundColor,
                        borderWidth: 0,
                        hoverOffset: 15
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    cutout: '70%',
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            padding: 12,
                            titleColor: '#fff',
                            bodyColor: '#fff',
                            callbacks: {
                                label: function(context) {
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = ((context.parsed / total) * 100).toFixed(1);
                                    return `${context.label}: ${context.parsed} (${percentage}%)`;
                                }
                            }
                        }
                    }
                }
            });
        },
        crearGraficoCanales() {
            const canvas = this.$refs.chartCanales;
            if (!canvas || !this.metricas) return;

            const canales = this.metricas.canales || {};
            const coloresCanales = {
                'whatsapp': '#25D366',
                'web': '#FFA500',
                'messenger': '#0084FF',
                'instagram': '#E4405F'
            };
            
            const labels = Object.keys(canales).map(c => 
                c.charAt(0).toUpperCase() + c.slice(1)
            );
            const data = Object.values(canales);
            const backgroundColor = Object.keys(canales).map(c => 
                coloresCanales[c.toLowerCase()] || '#9E9E9E'
            );

            const ctx = canvas.getContext('2d');
            this.chartInstances.canales = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Solicitudes',
                        data: data,
                        backgroundColor: backgroundColor,
                        borderRadius: 8,
                        barThickness: 40
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            padding: 12
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        },
        crearGraficoPrioridad() {
            const canvas = this.$refs.chartPrioridad;
            if (!canvas || !this.metricas) return;

            const prioridades = this.metricas.prioridades || {};
            const tiemposSimulados = {
                'Alta': 1.5,
                'Media': 3.2,
                'Baja': 5.8
            };
            
            const coloresPrioridad = {
                'Alta': '#F44336',
                'Media': '#FF9800',
                'Baja': '#4CAF50'
            };
            
            const labels = Object.keys(prioridades);
            const data = labels.map(p => tiemposSimulados[p] || 4.0);
            const backgroundColor = labels.map(p => coloresPrioridad[p] || '#9E9E9E');

            const ctx = canvas.getContext('2d');
            this.chartInstances.prioridad = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Tiempo Promedio (horas)',
                        data: data,
                        backgroundColor: backgroundColor,
                        borderRadius: 8,
                        barThickness: 50
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            padding: 12,
                            callbacks: {
                                label: function(context) {
                                    return `${context.parsed.x}h promedio`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            beginAtZero: true,
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        y: {
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        },
        crearGraficoCategorias() {
            const canvas = this.$refs.chartCategorias;
            if (!canvas || !this.metricas) return;

            const categorias = this.metricas.categorias || {};
            const coloresBase = ['#0D47A1', '#1976D2', '#2196F3', '#64B5F6', '#BBDEFB'];
            
            const sortedCategorias = Object.entries(categorias)
                .sort((a, b) => b[1] - a[1])
                .slice(0, 5);
            
            const labels = sortedCategorias.map(c => c[0]);
            const data = sortedCategorias.map(c => c[1]);
            const backgroundColor = coloresBase.slice(0, labels.length);

            const ctx = canvas.getContext('2d');
            this.chartInstances.categorias = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        data: data,
                        backgroundColor: backgroundColor,
                        borderWidth: 0,
                        hoverOffset: 10
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'right',
                            labels: {
                                usePointStyle: true,
                                padding: 15,
                                font: { size: 11 }
                            }
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            padding: 12
                        }
                    }
                }
            });
        },
        crearGraficoTiempos() {
            const canvas = this.$refs.chartTiempos;
            if (!canvas || !this.metricas) return;

            // Tiempos promedio simulados (en futuras versiones se calcularán desde BD)
            const tiemposData = [0.5, 3.2, 4.1, 1.8];

            const ctx = canvas.getContext('2d');
            this.chartInstances.tiempos = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Primera Respuesta', 'Resolución', 'Tiempo Total', 'Escalamiento'],
                    datasets: [{
                        label: 'Tiempo Promedio (horas)',
                        data: tiemposData,
                        backgroundColor: ['#9C27B0', '#3F51B5', '#009688', '#FF5722'],
                        borderRadius: 8,
                        barThickness: 60
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            padding: 12,
                            callbacks: {
                                label: function(context) {
                                    return `${context.parsed.y}h`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: {
                                color: 'rgba(0, 0, 0, 0.05)'
                            },
                            ticks: {
                                callback: function(value) {
                                    return value + 'h';
                                }
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        }
    },
};
</script>

<style scoped>
.bg-light-gray {
    background: linear-gradient(135deg, #F5F7FA 0%, #E8EBF0 100%);
}

.compact-date-field {
    background-color: white;
}

.compact-select {
    background-color: white;
}

.max-w-1920 {
    max-width: 1920px;
}

.kpi-card {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    border-left: 4px solid transparent;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12) !important;
}

.kpi-icon-wrapper {
    width: 56px;
    height: 56px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
