<template>
    <v-app>
        <AppHeader :nombreComercial="nombreComercial" :imagenComercial="imagenComercial" :correoUsuario="correoUsuario" :comercialId="comercialId" :baseURL="baseURL" :idCargo="idCargo" v-model:drawer="drawer" @imagenActualizada="actualizarImagen" @cerrarSesion="cerrarSesion" />
        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">

                <!-- 📌 Aquí integramos el visual de Seguimientos -->
                <h2 class="mb-6">Seguimientos</h2>
                <p class="text-subtitle-2 mb-6">Agenda, Kanban y calendario semanal.</p>

                <!-- Tarjetas -->
                <v-row class="mb-6" dense>
                    <v-col cols="12" sm="2">
                        <v-card style="background-color: #EF4444; color: white"
                            class="stat-card orange lighten-2 white--text">
                            <div class="stat-number">{{ conteoSeguimientos.atrasados }}</div>
                            <div class="stat-label">Atrasados ⏰</div>
                        </v-card>
                    </v-col>
                    <v-col cols="12" sm="2">
                        <v-card style="background-color: #F97316; color: white"
                            class="stat-card blue lighten-2 white--text">
                            <div class="stat-number">{{ conteoSeguimientos.paraHoy }}</div>
                            <div class="stat-label">Para hoy 📅</div>
                        </v-card>
                    </v-col>
                    <v-col cols="12" sm="2">
                        <v-card style="background-color: #0EA5E9; color: white"
                            class="stat-card purple lighten-2 white--text">
                            <div class="stat-number">{{ conteoSeguimientos.prox7 }}</div>
                            <div class="stat-label">Próx. 7 días 📅</div>
                        </v-card>
                    </v-col>
                    <v-col cols="12" sm="2">
                        <v-card style="background-color: #9CA3AF; color: white"
                            class="stat-card deep-purple lighten-2 white--text">
                            <div class="stat-number">{{ conteoSeguimientos.reprogramados }}</div>
                            <div class="stat-label">Reprogramados 🔃</div>
                        </v-card>
                    </v-col>
                    <v-col cols="12" sm="2">
                        <v-card style="background-color: #22C55E; color: white"
                            class="stat-card green lighten-2 white--text">
                            <div class="stat-number">{{ completadosHoy }}</div>
                            <div class="stat-label">Completados (hoy) ✅</div>
                        </v-card>
                    </v-col>
                </v-row>

                <!-- Filtros -->
                <v-card class="pa-4 mb-6" style="background-color: #E9F2F7;">
                    <v-row dense>
                        <!-- Fecha inicio -->
                        <v-col cols="12" sm="3">
                            <v-text-field v-model="fechaInicio" type="date" label="Fecha inicio" outlined dense
                                variant="outlined" density="compact" clearable />
                        </v-col>

                        <!-- Fecha fin -->
                        <v-col cols="12" sm="3">
                            <v-text-field v-model="fechaFin" type="date" label="Fecha fin" outlined dense
                                variant="outlined" density="compact" clearable />
                        </v-col>

                        <!-- Campaña -->
                        <v-col cols="12" sm="3">
                            <v-autocomplete v-model="campaña" return-object item-title="nombre" item-value="id"
                                :items="campañas" label="Campaña" outlined dense variant="outlined" density="compact"
                                clearable />
                        </v-col>

                        <!-- Empresa -->
                        <v-col cols="12" sm="3">
                            <v-autocomplete v-model="empresa" return-object item-title="p_razon_social" item-value="id"
                                :items="empresas" label="Empresa" outlined dense variant="outlined" density="compact"
                                clearable />
                        </v-col>
                    </v-row>

                    <v-row dense>
                        <v-col cols="12" class="d-flex justify-end">
                            <v-btn color="grey" variant="outlined" @click="limpiarFiltros()">
                                <v-icon left>mdi-broom</v-icon> Limpiar
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card>

                <!-- Dialog Registrar Gestión -->
                <v-dialog v-model="dialogGestion" max-width="800px" persistent>
                    <v-card class="pa-6 rounded-lg">
                        <v-card-title class="text-h6">
                            <v-row>
                                <v-col>
                                    Registrar gestión
                                    <v-spacer></v-spacer>
                                </v-col>
                                <v-col class="d-flex justify-end">
                                    <v-btn icon @click="cerrarRegistrarGestion()">
                                        <v-icon>mdi-close</v-icon>
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-card-title>

                        <v-card-text>
                            <v-row>
                                <v-col>
                                    <v-btn :color="colorEfectivo" style="font-size: 12px; width: 100%;"
                                        @click="formllamadaEfectiva()">
                                        ✅ Efectiva
                                    </v-btn>
                                </v-col>

                                <v-col>
                                    <v-btn :color="colorNoEfectivo" style="font-size: 12px; width: 100%;"
                                        @click="formLlamadaNoEfectiva()">
                                        ❌ No Efectivo
                                    </v-btn>
                                </v-col>
                            </v-row>

                            <v-row v-if="ifCrearLead">
                                <v-col>
                                    <p>Crear Lead</p>
                                </v-col>
                            </v-row>

                            <v-row class="mt-n4" v-if="ifCrearLead">
                                <v-col>
                                    <v-btn :color="colorLead" style="font-size: 12px; width: 100%;"
                                        @click="colorLead = 'blue'; colorNoLead = 'white'; ifLeadSi = true; ifLeadNo = false">
                                        👍 Si
                                    </v-btn>
                                </v-col>

                                <v-col>
                                    <v-btn :color="colorNoLead" style="font-size: 12px; width: 100%;"
                                        @click="colorNoLead = 'orange-darken-3'; colorLead = 'white'; ifLeadSi = false; ifLeadNo = true">
                                        👎 No
                                    </v-btn>
                                </v-col>
                            </v-row>

                            <v-row v-if="ifLeadSi">
                                <v-col>
                                    <p>Asignar</p>
                                    <v-autocomplete v-model="comercialAsignado" :items="comerciales" item-title="nombre"
                                        item-value="id" label="Seleccione un Comercial" clearable class="mt-2"
                                        density="compact" variant="outlined" autocomplete="off" return-object
                                        style="min-width: 120px; max-width: 100%;"></v-autocomplete>
                                </v-col>

                                <v-col>
                                    <p>Producto</p>
                                    <v-autocomplete v-model="productoSeleccionado" :items="productos"
                                        item-title="nombre" item-value="id" label="Seleccione un Producto" clearable
                                        class="mt-2" density="compact" variant="outlined" return-object
                                        autocomplete="off"
                                        @update:modelValue="llamadoSubproductos(productoSeleccionado.id)"
                                        style="min-width: 120px; max-width: 100%;"></v-autocomplete>
                                </v-col>
                            </v-row>

                            <v-row class="mt-n4" v-if="ifLeadSi">
                                <v-col>
                                    <p>Subproducto</p>
                                    <v-row no-gutters align="center">
                                        <v-col cols="8" xs="8" sm="8" md="8" lg="8" xl="8">
                                            <v-autocomplete v-model="subproductoSeleccionado"
                                                :readonly="!productoSeleccionado" :items="subproductos"
                                                item-title="nombre" item-value="id" label="Seleccione un Subproducto"
                                                clearable class="mt-2" density="compact" variant="outlined"
                                                autocomplete="off" return-object
                                                style="min-width: 120px; width: 100%;"></v-autocomplete>
                                        </v-col>
                                        <v-col cols="4" xs="4" sm="4" md="4" lg="4" xl="4"
                                            class="d-flex align-center justify-end">
                                            <v-btn variant="flat" :color="colorBotonSubProducto" class="mt-n4"
                                                style="font-size: 12px; white-space: normal; word-break: break-word;"
                                                @click="nuevoSubproducto()">
                                                {{ labelSubproducto }}
                                            </v-btn>
                                        </v-col>
                                    </v-row>

                                    <v-row v-if="ifnombreSubproducto">
                                        <v-col>
                                            <v-text-field v-model="nombreSubproducto" label="Nombre del Subproducto"
                                                outlined clearable class="mt-n6" density="compact" variant="outlined"
                                                style="min-width: 120px; max-width: 100%;"></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-col>

                                <v-col>
                                    <p>Observaciones</p>
                                    <v-textarea v-model="observacionesLlamada" label="Escriba aquí..." outlined
                                        clearable class="mt-2" density="compact" variant="outlined"
                                        style="min-width: 120px; max-width: 100%;"></v-textarea>
                                </v-col>
                            </v-row>

                            <v-row v-if="ifLeadNo">
                                <v-col>
                                    <p>Motivo</p>
                                    <v-autocomplete v-model="motivoNoLead" :items="motivos" item-title="nombre"
                                        item-value="id" label="Seleccione un Motivo" clearable class="mt-2"
                                        density="compact" variant="outlined" autocomplete="off" return-object
                                        style="min-width: 120px; max-width: 100%;"></v-autocomplete>
                                </v-col>
                            </v-row>

                            <v-row v-if="ifNoEfectivo">
                                <v-col>
                                    <p>Motivo</p>
                                    <v-autocomplete v-model="motivoNoEfectivo" :items="motivos" item-title="nombre"
                                        item-value="id" label="Seleccione un Motivo" clearable class="mt-2"
                                        density="compact" variant="outlined" autocomplete="off" return-object
                                        style="min-width: 120px; max-width: 100%;"></v-autocomplete>
                                </v-col>
                            </v-row>

                            <v-row v-if="ifNoEfectivo && (motivoNoEfectivo ? motivoNoEfectivo.id == 10 : false)"
                                class="mt-n6">
                                <v-col>
                                    <p>Reagendar</p>
                                    <v-text-field type="datetime-local" v-model="fechaReagenda"
                                        label="Seleccione una fecha" outlined clearable class="mt-2" density="compact"
                                        variant="outlined" :min="minDateTime()"
                                        style="min-width: 120px; max-width: 100%;"></v-text-field>
                                </v-col>
                            </v-row>

                            <v-row v-if="ifNoEfectivo" class="mt-n6">
                                <v-col>
                                    <p>Observaciones</p>
                                    <v-textarea v-model="observacionesNoEfectivo" label="Detalles de la gestión..."
                                        outlined clearable class="mt-2" density="compact" variant="outlined"
                                        style="min-width: 120px; max-width: 100%;"></v-textarea>
                                </v-col>
                            </v-row>
                        </v-card-text>

                        <v-card-actions class="mt-n2">
                            <v-spacer></v-spacer>
                            <v-btn variant="flat" color="blue-darken-3"
                                style="font-size: 12px; white-space: normal; word-break: break-word;"
                                @click="guardarGestionLlamada()">
                                Guardar Gestión
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>

                <!-- Tabs -->
                <v-tabs v-model="tab" background-color="transparent" grow>
                    <v-tab value="agenda">Agenda</v-tab>
                    <v-tab value="tablero">Tablero</v-tab>
                    <v-tab value="calendario">Calendario</v-tab>
                </v-tabs>

                <v-window v-model="tab" class="mt-4">
                    <v-window-item value="agenda">
                        <v-card v-for="(seguimiento, index) in seguimientoFiltrado" :key="index"
                            class="mb-4 pa-4 d-flex justify-space-between align-center">
                            <div>
                                <!-- Nombre del contacto y empresa -->
                                <strong>{{ seguimiento.nombre_contacto || 'Sin contacto' }}</strong>
                                <span style="margin-left: 8px" class="company">{{
                                    seguimiento.razon_social || 'Sin empresa'
                                }}</span>

                                <!-- Datos extra -->
                                <div class="text-caption">
                                    {{ seguimiento.cargo_contacto || 'Sin cargo' }} ·
                                    {{ seguimiento.ciudad || 'Sin ciudad' }} ·
                                    {{ seguimiento.sector || 'Sin sector' }}
                                </div>

                                <!-- Estado campaña -->
                                <v-chip small color="orange" class="ma-1">
                                    {{ seguimiento.estado_campaña }}
                                </v-chip>

                                <!-- Interés campaña -->
                                <v-chip small color="purple" class="ma-1">
                                    {{ seguimiento.interes_campaña }}
                                </v-chip>

                                <!-- Fecha reprogramación (opcional formateada) -->
                                <div class="text-caption mt-2">
                                    Reprogramado para: {{ new
                                        Date(seguimiento.fecha_reprogramacion).toLocaleString("es-CO", {
                                            timeZone: "UTC"
                                        }) }}
                                </div>

                                <!-- Respuesta -->
                                <div class="text-body-2 mt-1">
                                    {{ seguimiento.respuesta }}
                                </div>
                            </div>

                            <!-- Botón -->
                            <v-btn color="primary" @click="dialogGestion = true; seguimientoSeleccionado = seguimiento"
                                variant="outlined">
                                Registrar gestión
                            </v-btn>
                        </v-card>
                    </v-window-item>

                    <v-window-item value="tablero">
                        <v-container fluid>
                            <v-row>
                                <v-col v-for="col in columnas" :key="col.titulo" cols="12" sm="6" md="2">
                                    <!-- Título de columna -->
                                    <v-card outlined>
                                        <v-card-title class="d-flex justify-space-between">
                                            {{ col.titulo }}
                                            <v-chip color="primary" size="small" v-if="col.items.length > 0">
                                                {{ col.items.length }}
                                            </v-chip>
                                        </v-card-title>

                                        <!-- Listado de gestiones -->
                                        <v-card-text>
                                            <v-card v-for="(item, index) in col.items" :key="index" class="mb-2"
                                                outlined @click="abrirForm(item)">
                                                <v-card-text>
                                                    <div class="text-h6">{{ item.hora }}</div>
                                                    <div class="font-weight-bold">{{ item.nombre }}</div>
                                                    <div>{{ item.cargo }} • {{ item.ciudad }} • {{ item.sector }}</div>
                                                    <v-chip v-if="item.estado" :color="item.estadoColor" size="small"
                                                        class="mt-1">
                                                        {{ item.estado }}
                                                    </v-chip>
                                                </v-card-text>
                                            </v-card>
                                        </v-card-text>
                                    </v-card>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-window-item>

                    <v-window-item value="calendario">
                        <v-container fluid>
                            <!-- Calendario semanal -->
                            <v-sheet height="850">
                                <v-calendar ref="calendario" v-model="fechaActual" type="week" :events="eventos"
                                    color="primary" @update:interval="onUpdateInterval">
                                    <template #event="{ event }">
                                        <v-card @click="abrirForm(event.original)" flat tile class="pa-1"
                                            style="min-width:120px;">
                                            <div class="d-flex justify-space-between">
                                                <div>
                                                    <div class="text-subtitle-2 font-weight-medium">{{ event.title }}
                                                    </div>
                                                    <div class="text-caption">
                                                        {{ formatHora(event.start) }} • {{ event.details?.empresa || '—'
                                                        }}
                                                    </div>
                                                    <div class="text-caption"
                                                        v-if="event.details?.ciudad || event.details?.sector">
                                                        {{ event.details?.ciudad || '—' }} · {{ event.details?.sector ||
                                                            '—' }}
                                                    </div>
                                                </div>

                                                <v-chip small class="ml-2" :color="event.color">
                                                    {{ event.details?.estado || '—' }}
                                                </v-chip>
                                            </div>
                                        </v-card>
                                    </template>

                                    <template v-slot:day-label="{ date }">
                                        <div class="text-center grey--text text-caption">— Soltar aquí —</div>
                                    </template>
                                </v-calendar>
                            </v-sheet>
                        </v-container>
                    </v-window-item>
                </v-window>

                <!-- Dialog Alertas -->
                <v-dialog v-model="alerta" persistent style="z-index: 10000;">
                    <v-card :style="getAlertStyle()">
                        <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
                            class="mx-auto"></v-progress-circular>
                        <v-card-title v-text="mensajeAlert"
                            style="color: black; text-align: center; white-space: pre-wrap;"></v-card-title>
                        <v-btn class="mt-4 mx-auto" @click="alerta = false; ifCargando = false;"
                            style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
                    </v-card>
                </v-dialog>
                <!-- Dialog Alertas -->

            </v-container>
        </v-main>

        <!-- Aquí se mantienen los diálogos (cambio clave, alertas, etc.) -->
        <!-- ... -->
    </v-app>
</template>

<script>
import AppHeader from '../components/AppHeader.vue';
import axios from "axios";
import CryptoJS from "crypto-js";

export default {
    name: "SeguimientosPage",
    components: {
        AppHeader
    },
    data: () => ({
        baseURL: "",
        comercialId: 0,
        idCargo: null,
        nombreComercial: null,
        correoUsuario: null,
        imagenComercial: "",
        drawer: false,  // Control del drawer de navegación de AppHeader
        tab: "agenda",
        fechaInicio: null,
        fechaFin: null,
        campaña: null,
        empresa: null,
        productos: ["Producto A", "Producto B", "Producto C"],
        subproductos: ["Subproducto X", "Subproducto Y", "Subproducto Z"],
        usuarios: ["Usuario 1", "Usuario 2", "Usuario 3"],
        dialogGestion: false,
        resultadoLlamada: null,
        producto: null,
        crearLead: null,
        subproducto: null,
        asignar: null,
        observaciones: null,
        mostrarInput: null,
    empresas: [],
    campañas: [],
    seguimientoCampanas: [],
    columnas: [],
    completadosHoy: 0,
        estadoGestionLlamada: null,
        colorEfectivo: 'white',
        colorNoEfectivo: 'white',
        colorLead: 'white',
        colorNoLead: 'white',
        ifCrearLead: false,
        ifNoEfectivo: false,
        ifLeadSi: false,
        ifLeadNo: false,
        comercialAsignado: null,
        comerciales: [],
        productoSeleccionado: null,
        productos: [],
        subproductoSeleccionado: null,
        subproductos: [],
        creandoSubproducto: false,
        labelSubproducto: 'Crear +',
        colorBotonSubProducto: 'yellow-darken-3',
        ifnombreSubproducto: false,
        nombreSubproducto: null,
        motivoNoLead: null,
        motivoNoEfectivo: null,
        fechaReagenda: null,
        motivos: [],
        seguimientoSeleccionado: null,
        mensajeAlert: null,
        alerta: false,
        ifCargando: false,

        observacionesNoEfectivo: null,

        fechaActual: new Date().toISOString().substr(0, 10),
        rango: { start: null, end: null },
        eventos: [],
        menuActivo: "",
    }),
    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.comercialId = localStorage.getItem("idUsuario");
        this.idCargo = localStorage.getItem("idCargo");
        this.nombreComercial =
            localStorage.getItem("nombreLogin") +
            " " +
            localStorage.getItem("apellidoLogin");
        this.correoUsuario = localStorage.getItem("correoUsuario");
        this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?${Date.now()}`;
        this.llamadoCampañas();
        this.llamadoEmpresas();
        this.llamadoSeguimientos();
        this.llamadoProductos();
        this.llamadoSubproductos(0);
        this.llamadoComerciales();
        this.llamadoMotivos();
        this.setMenuActivoPorRuta();
    },

    computed: {

        seguimientoFiltrado() {
            console.log('Recalculando seguimientoFiltrado', this.fechaInicio, this.fechaFin, this.campaña, this.empresa);
            const eq = (a, b) => (String(a || '').trim().toLowerCase() === String(b || '').trim().toLowerCase());

            return this.seguimientoCampanas.filter(seg => {
                // Protecciones
                if (!seg) return false;

                // Fecha del registro
                if (!seg.fecha_reprogramacion) return false;
                const fechaSeg = new Date(seg.fecha_reprogramacion);
                if (isNaN(fechaSeg.getTime())) return false;

                // Normalizo fechaSeg a inicio del día para comparaciones de fecha-only
                const fechaSegInicioDia = new Date(fechaSeg);
                fechaSegInicioDia.setHours(0, 0, 0, 0);

                // Fecha inicio filtro (si existe)
                if (this.fechaInicio) {
                    const inicio = new Date(this.fechaInicio);
                    inicio.setHours(0, 0, 0, 0);
                    if (fechaSegInicioDia < inicio) return false;
                }

                // Fecha fin filtro (si existe) -> incluyente
                if (this.fechaFin) {
                    const fin = new Date(this.fechaFin);
                    fin.setHours(23, 59, 59, 999);
                    if (fechaSeg > fin) return false;
                }

                // Campaña (si seleccionada)
                if (this.campaña) {
                    // campaña puede ser objeto (return-object) o string
                    const campNombreFiltro = (typeof this.campaña === 'object') ? (this.campaña.nombre || '') : this.campaña;
                    if (campNombreFiltro && seg.nombre) {
                        if (!eq(seg.nombre, campNombreFiltro)) return false;
                    }
                }

                // Empresa (si seleccionada)
                if (this.empresa) {
                    const empNombreFiltro = (typeof this.empresa === 'object') ? (this.empresa.p_razon_social || this.empresa.nombre || '') : this.empresa;
                    if (empNombreFiltro && seg.razon_social) {
                        if (!eq(seg.razon_social, empNombreFiltro)) return false;
                    }
                }

                return true;
            });
        },
        conteoSeguimientos() {
            // Cuenta atrasados, para hoy y próximos 7 días
            let atrasados = 0, paraHoy = 0, prox7 = 0;
            const hoy = new Date();
            hoy.setHours(0, 0, 0, 0);
            const fin7 = new Date(hoy);
            fin7.setDate(hoy.getDate() + 7);

            // Usar seguimientoCampanasOriginal para el contador de reprogramados
            const reprogramados = Array.isArray(this.seguimientoCampanasOriginal) ? this.seguimientoCampanasOriginal.length : 0;

            for (const seg of this.seguimientoCampanas) {
                if (!seg || !seg.fecha_reprogramacion) continue;
                const fechaSeg = new Date(seg.fecha_reprogramacion);
                if (isNaN(fechaSeg.getTime())) continue;
                const fechaSegDia = new Date(fechaSeg);
                fechaSegDia.setHours(0, 0, 0, 0);

                if (fechaSegDia < hoy) {
                    atrasados++;
                } else if (fechaSegDia.getTime() === hoy.getTime()) {
                    paraHoy++;
                } else if (fechaSegDia > hoy && fechaSegDia <= fin7) {
                    prox7++;
                }
            }
            return { atrasados, paraHoy, prox7, reprogramados };
        },

        eventos() {
            return this.seguimientoFiltrado
                .filter(seg => seg && seg.fecha_reprogramacion)
                .map(seg => {
                    const fecha = new Date(seg.fecha_reprogramacion);
                    if (isNaN(fecha.getTime())) return null;
                    return {
                        title: seg.nombre_contacto?.trim() || 'Sin contacto',
                        start: fecha,
                        end: new Date(fecha.getTime() + 60 * 60 * 1000),
                        color: this.getColorEstado(seg.estado_campaña_id),
                        details: {
                            empresa: seg.razon_social,
                            ciudad: seg.ciudad,
                            sector: seg.sector,
                            estado: seg.estado_campaña
                        },
                        original: seg // <-- Agrega esta línea
                    };
                })
                .filter(Boolean);
        },

        columnas() {
            // Columnas: Hoy, Pendientes, Completados (Hoy)
            const hoy = new Date();
            hoy.setHours(0, 0, 0, 0);
            const fin7 = new Date(hoy);
            fin7.setDate(hoy.getDate() + 7);

            const hoyItems = [];
            const pendientesItems = [];
            const completadosHoyItems = [];

            this.seguimientoFiltrado.forEach(seg => {
                if (!seg || !seg.fecha_reprogramacion) return;
                const fechaSeg = new Date(seg.fecha_reprogramacion);
                if (isNaN(fechaSeg.getTime())) return;
                const fechaSegDia = new Date(fechaSeg);
                fechaSegDia.setHours(0, 0, 0, 0);

                const item = {
                    hora: fechaSeg.toLocaleString("es-CO", { timeZone: "UTC" }),
                    nombre: seg.nombre_contacto || "Sin contacto",
                    cargo: seg.cargo_contacto || "Sin cargo",
                    ciudad: seg.ciudad || "Sin ciudad",
                    sector: seg.sector || "Sin sector",
                    estado: seg.estado_campaña,
                    estadoColor: this.getColorEstado(seg.estado_campaña_id)
                };

                // Hoy
                if (fechaSegDia.getTime() === hoy.getTime()) {
                    hoyItems.push(item);
                }
                // Pendientes próximos 7 días
                if (fechaSegDia > hoy && fechaSegDia <= fin7) {
                    pendientesItems.push(item);
                }
            });

            // Completados (Hoy): usar el mismo filtro que el contador sobre seguimientoCampanasOriginal
                // Depuración: mostrar en consola el contenido de seguimientoCampanasOriginal
                console.log('[DEBUG columnas] seguimientoCampanasOriginal:', this.seguimientoCampanasOriginal);
            if (Array.isArray(this.seguimientoCampanasOriginal)) {
                this.seguimientoCampanasOriginal.forEach(item => {
                    if (item.estado_campaña_id === 3 && item.fecha_reprogramacion) {
                        const fechaItem = new Date(item.fecha_reprogramacion);
                        completadosHoyItems.push({
                            hora: fechaItem.toLocaleString("es-CO", { timeZone: "UTC" }),
                            nombre: item.nombre_contacto || "Sin contacto",
                            cargo: item.cargo_contacto || "Sin cargo",
                            ciudad: item.ciudad || "Sin ciudad",
                            sector: item.sector || "Sin sector",
                            estado: item.estado_campaña,
                            estadoColor: this.getColorEstado(item.estado_campaña_id)
                        });
                    }
                });
            }
                // Depuración: mostrar en consola los items de la columna Completados (Hoy)
                console.log('[DEBUG columnas] Completados (Hoy) items:', completadosHoyItems);

            return [
                { titulo: "Hoy", items: hoyItems },
                { titulo: "Pendientes", items: pendientesItems },
                { titulo: "Completados", items: completadosHoyItems }
            ];
        }
    },

    methods: {
        // Actualizar imagen del usuario cuando cambia desde AppHeader
        actualizarImagen(nuevaUrl) {
            this.imagenComercial = nuevaUrl;
        },

        abrirForm(item) {
            this.dialogGestion = true;
            this.seguimientoSeleccionado = item;
            console.log('Columna seleccionada:', item);
            // Podríamos preseleccionar algo basado en la columna si es necesario
        },

        limpiarCamposGestion() {
            this.estadoGestionLlamada = null;
            this.colorEfectivo = 'white';
            this.colorNoEfectivo = 'white';
            this.ifCrearLead = false;
            this.ifNoEfectivo = false;
            this.ifLeadSi = false;
            this.ifLeadNo = false;
            this.colorLead = 'white';
            this.colorNoLead = 'white';

            this.comercialAsignado = null;
            this.productoSeleccionado = null;
            this.subproductoSeleccionado = null;
            this.motivoNoLead = null;
            this.motivoNoEfectivo = null;
            this.fechaReagenda = null;
            this.observacionesLlamada = null;
            this.observacionesNoEfectivo = null;

            this.llamadoSubproductos(0);
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

        minDateTime() {
            /// Obtenemos la fecha y hora actual
            const today = new Date();
            // Formateamos la fecha en "YYYY-MM-DDTHH:mm"
            const formattedDateTime = today.toISOString().slice(0, 16);
            //fecha actual mas 1 dia
            const fecha = new Date();
            fecha.setDate(fecha.getDate() + 1);
            const year = fecha.getFullYear();
            const month = String(fecha.getMonth() + 1).padStart(2, '0');
            const day = String(fecha.getDate()).padStart(2, '0');
            const hours = String(fecha.getHours()).padStart(2, '0');
            const minutes = String(fecha.getMinutes()).padStart(2, '0'); // Formatea la fecha en el formato deseado
            const fechaFormateada = `${year}-${month}-${day}T${hours}:${minutes}`;
            return fechaFormateada;
        },

        nuevoSubproducto() {
            this.creandoSubproducto = !this.creandoSubproducto;

            if (this.creandoSubproducto) {
                this.ifnombreSubproducto = true;
                this.ifNuevoSubproducto = true;
                this.labelSubproducto = 'Guardar';
                this.colorBotonSubProducto = 'green';
            } else {
                this.ifnombreSubproducto = false;
                this.nombreSubproducto = null;
                this.ifNuevoSubproducto = false;
                this.labelSubproducto = 'Crear +';
                this.colorBotonSubProducto = 'yellow-darken-3';
            }
        },

        llamadoComerciales() {
            axios
                .post(this.baseURL + "api/cargausus", {
                    idusu: 0,
                    tipo: 1, // 1 para cargar los usuarios del rol comercial
                })
                .then((response) => {
                    this.comerciales = response.data.data.map((c) => ({
                        id: c.u_id,
                        nombre: `${c.u_nom} ${c.u_ape}`,
                    }));
                })
                .catch((error) => {
                    console.error("Error al cargar comerciales:", error);
                });
        },

        llamadoMotivos() {
            axios.get(this.baseURL + 'api/cargarmotivos')
                .then(response => {
                    this.motivos = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        formllamadaEfectiva() {
            this.estadoGestionLlamada = 1;
            this.colorEfectivo = 'green';
            this.colorNoEfectivo = 'white';
            this.ifCrearLead = true;
            this.ifNoEfectivo = false;
            this.ifLeadSi = false;
            this.ifLeadNo = false;
            this.colorLead = 'white';
            this.colorNoLead = 'white';

            this.llamadoMotivos();

            setTimeout(() => {
                this.motivos = this.motivos.filter(motivo => motivo.tipo == 1);
            }, 500);
        },

        formLlamadaNoEfectiva() {
            this.estadoGestionLlamada = 2;
            this.colorNoEfectivo = 'red';
            this.colorEfectivo = 'white';
            this.ifCrearLead = false;
            this.ifNoEfectivo = true;
            this.ifLeadSi = false;
            this.ifLeadNo = false;
            this.colorLead = 'white';
            this.colorNoLead = 'white';

            this.llamadoMotivos();

            setTimeout(() => {
                this.motivos = this.motivos.filter(motivo => motivo.tipo == 2);
            }, 500);
        },

        llamadoProductos() {
            axios
                .post(this.baseURL + "api/cargaProducto", {
                    id: 0,
                })
                .then((response) => {
                    this.productos = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        llamadoSubproductos(id) {
            axios
                .post(this.baseURL + "api/cargarSubProductos", {
                    id: id ? id : 0,
                })
                .then((response) => {
                    this.subproductos = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        guardarGestionLlamada() {
            if (!this.seguimientoSeleccionado) {
                this.mensajeAlert = 'Por favor, selecciona una campaña';
                this.alerta = true;
                return;
            }

            if (!this.estadoGestionLlamada) {
                this.mensajeAlert = 'Por favor, selecciona una gestión para la llamada';
                this.alerta = true;
                return;
            }

            if (this.estadoGestionLlamada == 1) { // Efectiva
                if (this.ifLeadSi) { // Con Lead
                    if (!this.comercialAsignado) {
                        this.mensajeAlert = 'Por favor, asigna un comercial';
                        this.alerta = true;
                        return;
                    }
                    if (!this.productoSeleccionado) {
                        this.mensajeAlert = 'Por favor, selecciona un producto';
                        this.alerta = true;
                        return;
                    }
                    if (!this.observacionesLlamada) {
                        this.mensajeAlert = 'Por favor, ingresa las observaciones para la llamada efectiva';
                        this.alerta = true;
                        return;
                    }

                    axios.post(this.baseURL + 'api/guardarGestionTelefonica', {
                        'id_comercial': this.comercialAsignado ? this.comercialAsignado.id : 0,
                        'id_producto': this.productoSeleccionado ? this.productoSeleccionado.id : 0,
                        'id_subproducto': this.subproductoSeleccionado ? this.subproductoSeleccionado.id : 0,
                        'observaciones': this.observacionesLlamada ? this.observacionesLlamada : '',
                        'id_campania': this.seguimientoSeleccionado.id_campaña,
                        'id_contacto': (this.seguimientoSeleccionado && this.seguimientoSeleccionado.id_contacto) ? this.seguimientoSeleccionado.id_contacto : 0,
                        'id_usuario': this.comercialId,
                        'efectividad': this.estadoGestionLlamada,
                        'crear_lead': this.ifLeadSi ? 1 : 0,
                        'motivo_no_lead': this.motivoNoLead ? this.motivoNoLead.id : 0,
                        'motivo_no_efectivo': this.motivoNoEfectivo ? this.motivoNoEfectivo.id : 0,
                        'observaciones_no_efectivo': this.observacionesNoEfectivo ? this.observacionesNoEfectivo : '',
                        'id_empresa': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_empresa : 0,
                        'fecha_reagenda': this.fechaReagenda ? this.fechaReagenda : '',
                        'estado': 3,
                        'id_campenv': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_campaña_detalle : 0
                    })
                        .then(response => {
                            this.mensajeAlert = 'Gestión guardada con éxito';
                            this.alerta = true;
                            this.ifCargando = false;
                            this.limpiarCamposGestion();
                            this.dialogGestion = false;
                            this.llamadoSeguimientos();
                        })
                        .catch(error => {
                            console.log(error);
                            this.mensajeAlert = 'Error al guardar la gestión';
                            this.alerta = true;
                            this.ifCargando = false;
                        });
                } else if (this.ifLeadNo) { // Sin Lead
                    if (!this.motivoNoLead) {
                        this.mensajeAlert = 'Por favor, selecciona un motivo para no crear el lead';
                        this.alerta = true;
                        return;
                    }

                    axios.post(this.baseURL + 'api/guardarGestionTelefonica', {
                        'id_comercial': this.comercialAsignado ? this.comercialAsignado.id : 0,
                        'id_producto': this.productoSeleccionado ? this.productoSeleccionado.id : 0,
                        'id_subproducto': this.subproductoSeleccionado ? this.subproductoSeleccionado.id : 0,
                        'observaciones': this.observacionesLlamada ? this.observacionesLlamada : '',
                        'id_campania': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_campaña : 0,
                        'id_contacto': (this.seguimientoSeleccionado && this.seguimientoSeleccionado.id_contacto) ? this.seguimientoSeleccionado.id_contacto : 0,
                        'id_usuario': this.comercialId,
                        'efectividad': this.estadoGestionLlamada,
                        'crear_lead': this.ifLeadSi ? 1 : 0,
                        'motivo_no_lead': this.motivoNoLead ? this.motivoNoLead.id : 0,
                        'motivo_no_efectivo': this.motivoNoEfectivo ? this.motivoNoEfectivo.id : 0,
                        'observaciones_no_efectivo': this.observacionesNoEfectivo ? this.observacionesNoEfectivo : '',
                        'id_empresa': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_empresa : 0,
                        'fecha_reagenda': this.fechaReagenda ? this.fechaReagenda : '',
                        'estado': this.motivoNoLead ? this.motivoNoLead.id == 10 ? 0 : 3 : 0,
                        'id_campenv': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_campaña_detalle : 0
                    })
                        .then(response => {
                            this.mensajeAlert = 'Gestión guardada con éxito';
                            this.alerta = true;
                            this.ifCargando = false;
                            this.limpiarCamposGestion();
                            this.dialogGestion = false;
                            this.llamadoSeguimientos();
                        })
                        .catch(error => {
                            console.log(error);
                            this.mensajeAlert = 'Error al guardar la gestión';
                            this.alerta = true;
                            this.ifCargando = false;
                        });
                } else {
                    this.mensajeAlert = 'Por favor, selecciona si se crea lead o no';
                    this.alerta = true;
                    return;
                }
            } else if (this.estadoGestionLlamada == 2) { // No Efectiva
                if (!this.motivoNoEfectivo) {
                    this.mensajeAlert = 'Por favor, selecciona un motivo para la llamada no efectiva';
                    this.alerta = true;
                    return;
                }

                if (this.motivoNoEfectivo == 10 && !this.fechaReagenda) {
                    this.mensajeAlert = 'Por favor, selecciona la fecha para la reagenda';
                    this.alerta = true;
                    return;
                }

                if (!this.observacionesNoEfectivo) {
                    this.mensajeAlert = 'Por favor, ingresa las observaciones para la llamada no efectiva';
                    this.alerta = true;
                    return;
                }

                axios.post(this.baseURL + 'api/guardarGestionTelefonica', {
                    'id_comercial': this.comercialAsignado ? this.comercialAsignado.id : 0,
                    'id_producto': this.productoSeleccionado ? this.productoSeleccionado.id : 0,
                    'id_subproducto': this.subproductoSeleccionado ? this.subproductoSeleccionado.id : 0,
                    'observaciones': this.observacionesLlamada ? this.observacionesLlamada : '',
                    'id_campania': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_campaña : 0,
                    'id_contacto': (this.seguimientoSeleccionado && this.seguimientoSeleccionado.id_contacto) ? this.seguimientoSeleccionado.id_contacto : 0,
                    'id_usuario': this.comercialId,
                    'efectividad': this.estadoGestionLlamada,
                    'crear_lead': this.ifLeadSi ? 1 : 0,
                    'motivo_no_lead': this.motivoNoLead ? this.motivoNoLead.id : 0,
                    'motivo_no_efectivo': this.motivoNoEfectivo ? this.motivoNoEfectivo.id : 0,
                    'observaciones_no_efectivo': this.observacionesNoEfectivo ? this.observacionesNoEfectivo : '',
                    'id_empresa': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_empresa : 0,
                    'fecha_reagenda': this.fechaReagenda ? this.fechaReagenda : '',
                    'estado': this.motivoNoEfectivo ? this.motivoNoEfectivo.id == 10 ? 0 : 3 : 0,
                    'id_campenv': this.seguimientoSeleccionado ? this.seguimientoSeleccionado.id_campaña_detalle : 0
                })
                    .then(response => {
                        this.mensajeAlert = 'Gestión guardada con éxito';
                        this.alerta = true;
                        this.ifCargando = false;
                        this.limpiarCamposGestion();
                        this.dialogGestion = false;
                        this.llamadoSeguimientos();
                    })
                    .catch(error => {
                        console.log(error);
                        this.mensajeAlert = 'Error al guardar la gestión';
                        this.alerta = true;
                        this.ifCargando = false;
                    });
            }
        },

        formatHora(fecha) {
            const d = fecha instanceof Date ? fecha : new Date(fecha);
            if (!d || isNaN(d.getTime())) return '';
            return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        },

        clickEvento(event) {
            console.log("Evento clickeado:", event);
            console.log("Título:", event.title);
            console.log("Detalles:", event.details);

            alert(`
                Título: ${event.name || "Sin nombre"}
                Empresa: ${event.details?.razon_social || "Sin empresa"}
                Ciudad: ${event.details?.ciudad || "Sin ciudad"}
                Sector: ${event.details?.sector || "Sin sector"}
                Estado: ${event.details?.estado || "Sin estado"}
            `);
        },

        onUpdateInterval() {
            console.log("Intervalo del calendario cambió");
        },

        getColorEstado(id) {
            switch (id) {
                case 1: return "orange";
                case 2: return "blue";
                case 3: return "purple";
                case 4: return "green";
                case 5: return "red";
                default: return "grey";
            }
        },

        limpiarFiltros() {
            this.fechaInicio = null;
            this.fechaFin = null;
            this.campaña = null;
            this.empresa = null;
        },

        llamadoSeguimientos() {

            axios.post(this.baseURL + 'api/cargarSeguimientosCampanasT', {
                'id_usuario': localStorage.getItem('idUsuario'),
            })
                .then(response => {
                    const items = Array.isArray(response.data.data) ? response.data.data : [];
                    this.seguimientoCampanas = items.filter(item => item.estado_campaña_id !== 3);
                        // Guardar el array original para Completados (Hoy)
                        this.seguimientoCampanasOriginal = items;
                    // Contar los completados (hoy) con estado_campaña_id === 3 y fecha_reprogramacion igual a hoy
                    const hoy = new Date();
                    hoy.setHours(0, 0, 0, 0);
                    this.completadosHoy = items.filter(item => {
                        if (item.estado_campaña_id === 3 && item.fecha_reprogramacion) {
                            const fechaItem = new Date(item.fecha_reprogramacion);
                            fechaItem.setHours(0, 0, 0, 0);
                            return fechaItem.getTime() === hoy.getTime();
                        }
                        return false;
                    }).length;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoEmpresas() {

            axios.post(this.baseURL + 'api/cargarpp', {
                'idusu': localStorage.getItem('idUsuario'),
            })
                .then(response => {
                    this.empresas = response.data.data;

                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoCampañas() {

            axios.post(this.baseURL + 'api/cargarcamptel', {
                'idusu': localStorage.getItem('idUsuario'),
                'tipo': 2
            })
                .then(response => {
                    this.campañas = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        onUpdateInterval({ start, end }) {
            this.rango = { start, end };
        },
        formatoFecha(fecha) {
            if (!fecha) return "";
            return new Date(fecha).toLocaleDateString("es-CO", {
                day: "numeric",
                month: "short",
                year: "numeric",
            });
        },

        guardarSubproducto() {

            alert(`Nuevo subproducto guardado: ${this.nuevoSubproducto}`);

        },

        cerrarRegistrarGestion() {
            this.dialogGestion = false;
            this.resultadoLlamada = null;
            this.producto = null;
            this.crearLead = null;
            this.subproducto = null;
            this.asignar = null;
            this.observaciones = null;

        },

        irComercial() {
            this.$router.push("/comercial");
        },
        irPendientesGeneral() {
            this.$router.push("/pendiente-general");
        },
        irConfiguracion() {
            this.$router.push("/configuracion");
        },
        irPQR() {
            this.$router.push("/pqr");
        },
        irPedidos() {
            this.$router.push("/pedidos");
        },
        irCampañas() {
            this.$router.push("/campana");
        },
        irGaleriaCampanas() {
            this.$router.push('/VerCampanas');
        },

        irInformesCampañas() {
            this.$router.push('/informes-campanas');
        },

        irProspeccionTelefonica() {
            this.$router.push('/prospeccion-telefonica');
        },

        irSeguimientoLlamadas() {
            this.$router.push('/seguimiento-llamadas');
        },
        irContactos() {
            this.$router.push("/contactos");
        },
        cerrarSesion() {
            localStorage.clear();
            this.$router.push("/");
        },
        cambiarImagen() {
            const input = document.createElement("input");
            input.type = "file";
            input.accept = "image/jpeg";
            input.onchange = async (event) => {
                const file = event.target.files[0];
                if (file) {
                    const formData = new FormData();
                    formData.append("imagen", file);
                    formData.append("nombre_archivo", `${this.comercialId}.jpeg`);
                    try {
                        await axios.post(this.baseURL + "api/subir-imagen", formData, {
                            headers: { "Content-Type": "multipart/form-data" },
                        });
                    } catch (error) {
                        console.error("❌ Error al subir imagen:", error);
                    }
                }
            };
            input.click();
        },
        setMenuActivoPorRuta() {
        const path = (this.$route.path || '').toLowerCase();
        if (path.includes('/vercampanas')) this.menuActivo = '/vercampanas';
        else if (path.includes('/campana')) this.menuActivo = '/campana';
        else if (path.includes('/contactos')) this.menuActivo = '/contactos';
        else if (path.includes('/prospeccion-telefonica')) this.menuActivo = '/prospeccion-telefonica';
        else if (path.includes('/seguimiento-llamadas')) this.menuActivo = '/seguimiento-llamadas';
        else if (path.includes('/informes-campanas')) this.menuActivo = '/informes-campanas';
        // ...agrega más si tienes otras rutas...
        else this.menuActivo = '';
        },
    },
};
</script>

<style scoped>
.stat-card {
    text-align: center;
    padding: 20px;
    border-radius: 12px;
}

.stat-number {
    font-size: 24px;
    font-weight: bold;
}

.stat-label {
    font-size: 14px;
}

.company {
    color: #1976d2;
    font-weight: 500;
}

.menu-link {
    color: #1976d2;
    cursor: pointer;
    text-decoration: underline;
    font-size: 1rem;
    margin-bottom: 8px;
    font-weight: 500;
    transition: color 0.2s;
    width: fit-content;
}

.menu-link:hover {
    color: #0a1c3a;
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
