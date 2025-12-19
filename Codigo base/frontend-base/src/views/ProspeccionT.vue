<template>
    <v-app>
        <AppHeader :imagenComercial="imagenComercial" />
        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
                <!-- RESTO DEL CONTENIDO DE LA VISTA -->
                <v-list v-if="false">

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

                <v-list-item @click="irContactos()" link v-if="false">

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
                        <v-list-item v-bind="props" prepend-icon="mdi mdi-bullhorn" title="Campañas"
                            active></v-list-item>
                    </template>

                    <v-list-item @click="irGaleriaCampanas()" link>

                        <v-list-item-content class="list-item-compact">

                            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/vercampanas' }"
                                style="color: white; font-size: 0.93rem;">
                                <v-icon class="mr-2" size="small" icon="mdi mdi-image-multiple" color="white"
                                    prepend-icon></v-icon>
                                Galería
                            </v-list-item-title>
                        </v-list-item-content>

                    </v-list-item>

                    <v-list-item @click="irInformesCampañas()" link>

                        <v-list-item-content>

                            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/informes-campanas' }"
                                style="color: white; font-size: 0.93rem;">
                                <v-icon class="mr-2" size="small" icon="mdi-chart-bar" color="white"
                                    prepend-icon></v-icon>
                                Métricas
                            </v-list-item-title>
                        </v-list-item-content>

                    </v-list-item>

                    <v-list-item @click="irProspeccionTelefonica()" link>

                        <v-list-item-content>

                            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/prospeccion-telefonica' }"
                                style="color: white; white-space: pre-wrap; font-size: 0.93rem;">
                                <v-icon class="mr-2" size="small" icon="mdi-phone-log" color="white"
                                    prepend-icon></v-icon>
                                Prospección Telefónica
                            </v-list-item-title>
                        </v-list-item-content>

                    </v-list-item>

                    <v-list-item @click="" link>

                        <v-list-item-content>

                            <v-list-item-title style="color: white; white-space: pre-wrap; font-size: 0.93rem;">
                                <v-icon class="mr-2" size="small" icon="mdi-email-newsletter" color="white"
                                    prepend-icon></v-icon>
                                Email Marketing
                            </v-list-item-title>
                        </v-list-item-content>

                    </v-list-item>

                    <v-list-item @click="irCampañas()" link>

                        <v-list-item-content>

                            <v-list-item-title style="color: white; white-space: pre-wrap; font-size: 0.93rem;"
                                :class="{ 'menu-item-activo': menuActivo === '/campana' }">
                                <v-icon class="mr-2" size="small" icon="mdi-whatsapp" color="white"
                                    prepend-icon></v-icon>
                                WhatsApp Business
                            </v-list-item-title>
                        </v-list-item-content>

                    </v-list-item>

                </v-list-group>

                <v-list-group value="Clientes" v-if="idCargo == '2'">
                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" prepend-icon="mdi-account-group" title="Clientes"
                            active></v-list-item>
                    </template>

                    <v-list-item @click="irEmpresas()" link v-if="idCargo == '2'">

                        <v-list-item-content>

                            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/contactos' }"
                                style="color: white;; font-size: 0.93rem; ">
                                <v-icon class="mr-2" size="small" icon="mdi-office-building" color="white"
                                    prepend-icon></v-icon>
                                Empresas
                            </v-list-item-title>
                        </v-list-item-content>

                    </v-list-item>

                </v-list-group>

                <v-list-group value="Chat" v-if="idCargo == '2'">
                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" prepend-icon="mdi-chat-processing" title="Chat"
                            active></v-list-item>
                    </template>

                    <v-list-item @click="irContactos()" link v-if="idCargo == '2'">

                        <v-list-item-content>

                            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/contactos' }"
                                style="color: white; font-size: 0.93rem;">
                                <v-icon class="mr-2" size="small" icon="mdi-contacts" color="white"
                                    prepend-icon></v-icon>
                                Contactos
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

                <v-row style="width: 100%;">
                    <v-col>
                        <v-card class="elevation-5 rounded-lg">
                            <v-card-title>
                                <span class="headline">Prospección Telefónica</span>
                                <v-btn variant="flat" color="teal-darken-3" style="float: right;"
                                    @click="irSeguimientoLlamadas()">
                                    📆 Seguimiento Llamadas
                                </v-btn>
                            </v-card-title>
                            <v-card-text>
                                <p>Registro, control y seguimiento de campañas.</p>
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>

                <v-row style="width: 100%;">
                    <v-col>
                        <v-card class="elevation-5 rounded-lg">
                            <v-card-text>
                                <v-row>
                                    <v-col>
                                        <v-row>
                                            <v-col cols="2">
                                                <p style="white-space: pre-wrap;">Campaña Activa:</p>
                                            </v-col>

                                            <v-col>
                                                <v-autocomplete v-model="campañaSeleccionada" :items="campañas"
                                                    item-title="nombre" item-value="id" label="Seleccione una campaña"
                                                    outlined clearable style="max-width: 300px;" variant="outlined"
                                                    @update:modelValue="cargarGuionCampaña(); llamadoHistorialGestion(); cargandoHistorial = true; historialGestion = [];"
                                                    return-object autocomplete="off" density="compact"></v-autocomplete>
                                            </v-col>

                                            <v-col>
                                                <v-btn variant="flat" color="#006CA1" v-if="!campañaSeleccionada"
                                                    @click="dialogCrearCampaña = true; labelFormularioCampaña = 'Crear nueva campaña'">
                                                    🔔 Crear Campaña
                                                </v-btn>
                                                <v-btn variant="flat" color="blue-darken-3" v-if="campañaSeleccionada"
                                                    @click="irEditarCampanas(campañaSeleccionada.id)">
                                                    ✍️ Editar Campaña
                                                </v-btn>
                                            </v-col>
                                        </v-row>

                                        <v-row class="mt-n4">
                                            <v-col>
                                                <v-btn variant="flat" color="blue-grey-darken-2"
                                                    @click="cargarGuionCampaña()">
                                                    📄 Ver Guión
                                                </v-btn>
                                            </v-col>
                                        </v-row>
                                    </v-col>

                                    <v-col>
                                        <v-row>
                                            <v-col>
                                                <v-card class="pa-2 rounded-lg elevation-5" color="blue-darken-3"
                                                    @click="abrirListaLlamadas(0); filtroInicialSeleccionado = 0">
                                                    <v-card-subtitle>
                                                        <span>Llamadas registradas hoy</span>
                                                    </v-card-subtitle>
                                                    <v-card-text>
                                                        <v-row>
                                                            <v-col style="font-size: 16px;">
                                                                {{ llamadasHoy }}
                                                            </v-col>

                                                            <v-col style="font-size: 16px;">
                                                                <span style="float: right;">📞</span>
                                                            </v-col>
                                                        </v-row>
                                                    </v-card-text>
                                                </v-card>
                                            </v-col>

                                            <v-col>
                                                <v-card class="pa-2 rounded-lg elevation-5" color="green-darken-3"
                                                    @click="abrirListaLlamadas(1); filtroInicialSeleccionado = 1">
                                                    <v-card-subtitle>
                                                        <span>Llamadas Efectivas Con Lead</span>
                                                    </v-card-subtitle>
                                                    <v-card-text>
                                                        <v-row>
                                                            <v-col style="font-size: 16px;">
                                                                {{ llamadasEfectivasLead }}
                                                            </v-col>

                                                            <v-col style="font-size: 16px;">
                                                                <span style="float: right;">✅</span>
                                                            </v-col>
                                                        </v-row>
                                                    </v-card-text>
                                                </v-card>
                                            </v-col>

                                            <v-col>
                                                <v-card class="pa-2 rounded-lg elevation-5" color="teal-darken-3"
                                                    @click="abrirListaLlamadas(2); filtroInicialSeleccionado = 2">
                                                    <v-card-subtitle>
                                                        <span>Llamadas Efectivas Sin Lead</span>
                                                    </v-card-subtitle>
                                                    <v-card-text>
                                                        <v-row>
                                                            <v-col style="font-size: 16px;">
                                                                {{ llamadasEfectivasSinLead }}
                                                            </v-col>

                                                            <v-col style="font-size: 16px;">
                                                                <span style="float: right;">✅</span>
                                                            </v-col>
                                                        </v-row>
                                                    </v-card-text>
                                                </v-card>
                                            </v-col>

                                            <v-col>
                                                <v-card class="pa-2 rounded-lg elevation-5" color="orange-darken-2"
                                                    @click="abrirListaLlamadas(3); filtroInicialSeleccionado = 3">
                                                    <v-card-subtitle>
                                                        <span>Llamadas No Efectivas</span>
                                                    </v-card-subtitle>
                                                    <v-card-text>
                                                        <v-row>
                                                            <v-col style="font-size: 16px;">
                                                                {{ llamadasNoEfectivas }}
                                                            </v-col>

                                                            <v-col style="font-size: 16px;">
                                                                <span style="float: right;">⚠️</span>
                                                            </v-col>
                                                        </v-row>
                                                    </v-card-text>
                                                </v-card>
                                            </v-col>
                                        </v-row>
                                    </v-col>
                                </v-row>

                                <v-row>
                                    <v-col>
                                        <span style="font-weight: bold;">Meta de Llamadas</span>
                                        <span style="float: right;">{{ totalLlamadas }}/{{ metaLlamadas }} ({{
                                            progresoCampañas
                                            }}%)</span>
                                        <v-progress-linear color="primary" v-model="progresoCampañas"
                                            :buffer-value="bufferCampañas" :height="8" rounded></v-progress-linear>
                                    </v-col>
                                </v-row>
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col cols="3">
                        <v-card-title class="text-subtitle-1 d-flex align-center justify-space-between"
                            style="background-color: #006CA1; color:white; border-radius:8px; height: 50px;">
                            <div class="d-flex align-center">
                                <v-icon icon="mdi mdi-phone-log" color="white" prepend-icon></v-icon>
                                <span class="ml-2">Cola de llamadas</span>
                            </div>
                        </v-card-title>
                        <v-card class="pa-2 elevation-5 rounded-lg">

                            <!--<v-divider :thickness="2"></v-divider> -->
                            <v-card-text>
                                <v-autocomplete v-model="contactoFiltro" :items="contactos" item-title="nombre"
                                    :readonly="contactoFiltro" item-value="id"
                                    label="🔎 Buscar Nombre, Empresa, Teléfono" outlined clearable variant="outlined"
                                    style="min-width: 120px; max-width: 100%;" autocomplete="off" density="compact"
                                    return-object @update:model-value="filtrarContactos()"></v-autocomplete>

                                <v-row>
                                    <v-col>
                                        <v-autocomplete v-model="sectorFiltro" :items="sectores" item-title="nombre"
                                            item-value="id" label="Sector:" outlined clearable density="compact"
                                            variant="outlined" hide-details autocomplete="off" return-object
                                            :readonly="contactoFiltro" style="min-width: 120px; max-width: 100%;"
                                            @update:model-value="filtrarContactos()"></v-autocomplete>
                                    </v-col>

                                    <v-col>
                                        <v-autocomplete v-model="ciudadFiltro" :items="ciudadesFiltro"
                                            :readonly="contactoFiltro" item-title="nombre" item-value="id"
                                            label="Ciudad:" outlined clearable density="compact" variant="outlined"
                                            hide-details autocomplete="off" return-object
                                            style="min-width: 120px; max-width: 100%;"
                                            @update:model-value="filtrarContactos()"></v-autocomplete>
                                    </v-col>

                                    <v-col>
                                        <v-autocomplete v-model="cargoFiltro" :items="cargosFiltro" item-title="nombre"
                                            item-value="id" label="Cargo:" outlined clearable density="compact"
                                            variant="outlined" hide-details autocomplete="off" return-object
                                            :readonly="contactoFiltro" style="min-width: 120px; max-width: 100%;"
                                            @update:model-value="filtrarContactos()"></v-autocomplete>
                                    </v-col>
                                </v-row>

                                <v-divider :thickness="2" class="mt-6 mb-4" style="width: 100%;"></v-divider>

                                <v-row style="max-height: 400px; overflow-y: auto;">

                                    <v-col>
                                        <v-card v-for="empresa in listaContactos" :key="empresa.id"
                                            class="pa-0 mb-2 rounded-lg elevation-5" outlined
                                            :style="getCardStyle(empresa)" @click="cargarEmpresa(empresa)">
                                            <v-card-title style="font-size: 14px; font-weight: bold;">
                                                {{ empresa.nombre }}
                                                <v-icon @click="cargarContactoSeleccionado(empresa)" size="20"
                                                    color="blue" style="float: right;">mdi-eye</v-icon>
                                            </v-card-title>
                                            <v-card-subtitle style="font-size: 12px;">
                                                {{ empresa.empresa }} - {{ empresa.ciudad }}
                                            </v-card-subtitle>
                                            <v-card-text style="font-size: 12px;">
                                                <v-row>
                                                    <v-col>
                                                        {{ empresa.celular }}
                                                    </v-col>

                                                    <v-col>
                                                        <v-chip color="blue" small style="float: right;">
                                                            {{ empresa.cargo }}
                                                        </v-chip>
                                                    </v-col>
                                                </v-row>

                                                <v-row>
                                                    <v-col>
                                                        📞 Empresa: {{ empresa.telefono }}
                                                    </v-col>
                                                </v-row>
                                            </v-card-text>
                                        </v-card>
                                    </v-col>
                                </v-row>
                            </v-card-text>

                            <v-divider :thickness="2" class="mt-6 mb-6" style="width: 100%;"></v-divider>

                            <v-card-actions class="mt-n4">
                                <v-row dense class="g-1">
                                    <v-col cols="4" class="pa-1">
                                        <v-btn variant="flat" color="grey-lighten-2"
                                            style="font-size: 12px; width: 100%; white-space: normal; word-break: break-word;"
                                            @click="anteriorEmpresa()">
                                            Anterior
                                        </v-btn>
                                    </v-col>
                                    <v-col cols="4" class="pa-1">
                                        <v-btn variant="flat" color="primary"
                                            style="font-size: 12px; width: 100%; white-space: normal; word-break: break-word;"
                                            @click="siguienteEmpresa()">
                                            Siguiente
                                        </v-btn>
                                    </v-col>
                                    <v-col cols="4" class="pa-1">
                                        <v-btn variant="flat" color="success"
                                            style="font-size: 12px; width: 100%; white-space: normal; word-break: break-word;"
                                            @click="abrirFormularioProspecto()">
                                            + Nuevo<br>Prospecto
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </v-card-actions>
                        </v-card>
                    </v-col>

                    <v-col>
                        <v-row>
                            <v-col>
                                <v-card class="elevation-5 rounded-lg">
                                    <v-card-title>
                                        <span class="headline">Gestionar llamada a</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <p style="font-weight: bold; font-size: 16px;">{{ contactoSeleccionadoNombre }}
                                        </p>
                                        <p>{{ contactoSeleccionadoCelular }}</p>
                                    </v-card-text>
                                </v-card>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col>
                                <v-card class="elevation-5 rounded-lg">
                                    <v-card-title>
                                        <span class="headline">Resultado de la llamada</span>
                                    </v-card-title>
                                    <v-card-subtitle v-if="historialGestion.length > 0 && historialGestion[0].interes === 0">
                                        <v-alert type="error" variant="outlined"
                                            class="mt-2">
                                            Este contacto está siendo atendido por el comercial asignado.
                                        </v-alert>
                                    </v-card-subtitle>
                                    <v-card-text>
                                        <v-row>
                                            <v-col>
                                                <v-btn :color="colorEfectivo" style="font-size: 12px; width: 100%;"
                                                    @click="formllamadaEfectiva()" :disabled="historialGestion.length > 0 && historialGestion[0].interes === 0">
                                                    ✅ Efectiva
                                                </v-btn>
                                            </v-col>

                                            <v-col>
                                                <v-btn :color="colorNoEfectivo" style="font-size: 12px; width: 100%;"
                                                    @click="formLlamadaNoEfectiva()" :disabled="historialGestion.length > 0 && historialGestion[0].interes === 0">
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
                                                <v-autocomplete v-model="comercialAsignado" :items="comerciales"
                                                    item-title="nombre" item-value="id" label="Seleccione un Comercial"
                                                    clearable class="mt-2" density="compact" variant="outlined"
                                                    autocomplete="off" return-object
                                                    style="min-width: 120px; max-width: 100%;"></v-autocomplete>
                                            </v-col>

                                            <v-col>
                                                <p>Producto</p>
                                                <v-autocomplete v-model="productoSeleccionado" :items="productos"
                                                    item-title="nombre" item-value="id" label="Seleccione un Producto"
                                                    clearable class="mt-2" density="compact" variant="outlined"
                                                    return-object autocomplete="off"
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
                                                            item-title="nombre" item-value="id"
                                                            label="Seleccione un Subproducto" clearable class="mt-2"
                                                            density="compact" variant="outlined" autocomplete="off"
                                                            return-object
                                                            style="min-width: 120px; width: 100%;"></v-autocomplete>
                                                    </v-col>
                                                    <v-col cols="4" xs="4" sm="4" md="4" lg="4" xl="4"
                                                        class="d-flex align-center justify-end">
                                                        <v-btn variant="flat" :color="colorBotonSubProducto"
                                                            class="mt-n4"
                                                            style="font-size: 12px; white-space: normal; word-break: break-word;"
                                                            @click="nuevoSubproducto()">
                                                            {{ labelSubproducto }}
                                                        </v-btn>
                                                    </v-col>
                                                </v-row>

                                                <v-row v-if="ifnombreSubproducto">
                                                    <v-col>
                                                        <v-text-field v-model="nombreSubproducto"
                                                            label="Nombre del Subproducto" outlined clearable
                                                            class="mt-n6" density="compact" variant="outlined"
                                                            style="min-width: 120px; max-width: 100%;"></v-text-field>
                                                    </v-col>
                                                </v-row>
                                            </v-col>

                                            <v-col>
                                                <p>Observaciones</p>
                                                <v-textarea v-model="observacionesLlamada" label="Escriba aquí..."
                                                    outlined clearable class="mt-2" density="compact" variant="outlined"
                                                    style="min-width: 120px; max-width: 100%;"></v-textarea>
                                            </v-col>
                                        </v-row>

                                        <v-row v-if="ifLeadNo">
                                            <v-col>
                                                <p>Motivo</p>
                                                <v-autocomplete v-model="motivoNoLead" :items="motivos"
                                                    item-title="nombre" item-value="id" label="Seleccione un Motivo"
                                                    clearable class="mt-2" density="compact" variant="outlined"
                                                    autocomplete="off" return-object
                                                    style="min-width: 120px; max-width: 100%;"></v-autocomplete>
                                            </v-col>
                                        </v-row>

                                        <v-row v-if="ifNoEfectivo">
                                            <v-col>
                                                <p>Motivo</p>
                                                <v-autocomplete v-model="motivoNoEfectivo" :items="motivos"
                                                    item-title="nombre" item-value="id" label="Seleccione un Motivo"
                                                    clearable class="mt-2" density="compact" variant="outlined"
                                                    autocomplete="off" return-object
                                                    style="min-width: 120px; max-width: 100%;"></v-autocomplete>
                                            </v-col>
                                        </v-row>

                                        <v-row
                                            v-if="ifNoEfectivo && (motivoNoEfectivo ? motivoNoEfectivo.id == 10 : false)"
                                            class="mt-n6">
                                            <v-col>
                                                <p>Reagendar</p>
                                                <v-text-field type="datetime-local" v-model="fechaReagenda"
                                                    label="Seleccione una fecha" outlined clearable class="mt-2"
                                                    density="compact" variant="outlined" :min="minDateTime()"
                                                    style="min-width: 120px; max-width: 100%;"></v-text-field>
                                            </v-col>
                                        </v-row>

                                        <v-row v-if="ifNoEfectivo" class="mt-n6">
                                            <v-col>
                                                <p>Observaciones</p>
                                                <v-textarea v-model="observacionesNoEfectivo"
                                                    label="Detalles de la gestión..." outlined clearable class="mt-2"
                                                    density="compact" variant="outlined"
                                                    style="min-width: 120px; max-width: 100%;"></v-textarea>
                                            </v-col>
                                        </v-row>
                                    </v-card-text>

                                    <v-card-actions class="mt-n2">
                                        <v-spacer></v-spacer>
                                        <v-btn variant="flat" color="blue-darken-3"
                                            style="font-size: 12px; white-space: normal; word-break: break-word;"
                                            @click="guardarGestionLlamada()" :disabled="historialGestion.length > 0 && historialGestion[0].interes === 0">
                                            Guardar Gestión
                                        </v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-col>
                        </v-row>
                    </v-col>

                    <v-col cols="3">
                        <v-card class="elevation-5 rounded-lg">
                            <v-card-title class="text-subtitle-1 d-flex align-center justify-space-between"
                                style="background-color: #006CA1; color:white; border-radius:8px; height: 50px;">
                                <div class="d-flex align-center">
                                    <v-icon icon="mdi mdi-phone-clock" color="white" prepend-icon></v-icon>
                                    <span class="ml-2">Historial de Llamadas</span>
                                </div>
                            </v-card-title>
                            <v-card-title>
                                <span class="headline"></span>
                            </v-card-title>
                            <v-card-text>

                                <v-row>
                                    <v-col>
                                        <v-btn variant="text" color="primary" style="font-size: 12px; float: right;"
                                            :disabled="!empresaSeleccionada" @click="historialGlobal()">
                                            Ver Historial Global
                                        </v-btn>
                                    </v-col>
                                </v-row>

                                <v-row>
                                    <v-col>
                                        <p style="font-weight: bold; font-size: 16px;">{{ contactoSeleccionadoNombre }}
                                        </p>
                                        <p style="color: grey;">{{ contactoSeleccionadoEmpresa }} - {{
                                            contactoSeleccionadoCargo
                                            }}</p>
                                    </v-col>

                                    <v-col style="text-align: right;">
                                        <p>{{ contactoSeleccionadoCelular }}</p>
                                        <p style="color: grey;">{{ contactoSeleccionadoEmail }}</p>
                                    </v-col>
                                </v-row>

                                <v-row style="max-height: 625px; overflow-y: auto;">
                                    <v-col>
                                        <p style="font-weight: bold; font-size: 16px;">Historial: </p>

                                        <v-progress-circular :size="50" v-if="cargandoHistorial" indeterminate
                                            color="primary" class="ma-4"></v-progress-circular>

                                        <v-card v-for="gestion in historialGestion" :key="gestion.id"
                                            class="mt-2 pa-2 mb-2 rounded-lg elevation-5" outlined>
                                            <v-card-title style="font-size: 14px; font-weight: bold;">
                                                {{ formatDate(gestion.fecha) }}
                                            </v-card-title>
                                            <v-card-subtitle style="font-size: 12px;">
                                                {{ gestion.interes == 0 ? 'Llamada Efectiva Con Lead' : gestion.interes
                                                    == 1 ?
                                                    'Llamada Efectiva Sin Lead' : 'Llamada No Efectiva' }}
                                            </v-card-subtitle>
                                            <span v-if="gestion.Editado == 'Si'" class="ml-4"
                                                style="font-size: 10px; color: red; font-weight: bold;">🖋️
                                                Editado</span>
                                            <!-- Boton sin texto pero con icono para ver el historial de ediciones -->
                                            <v-btn v-if="gestion.Editado == 'Si'" icon variant="text" color="primary"
                                                class="ml-2" title="Ver historial de ediciones"
                                                @click="abrirHistorialEdiciones(gestion)">
                                                <v-icon style="font-size: 16px;">mdi-history</v-icon>
                                            </v-btn>
                                            <v-card-text style="font-size: 12px;"
                                                :class="{ 'mt-n4': gestion.Editado == 'Si' }">
                                                <p style="margin-top: 0;">"{{ gestion.respuesta }}"</p>
                                                <v-btn variant="text" color="primary"
                                                    style="font-size: 12px; float: right;"
                                                    @click="llamadaEditar = gestion.id">
                                                    ✍️ Editar
                                                </v-btn>
                                                <v-textarea v-if="gestion.id === llamadaEditar" v-model="texto_editado"
                                                    label="Editar observación" outlined clearable class="mt-4"
                                                    density="compact" variant="outlined"
                                                    style="min-width: 120px; max-width: 100%;">
                                                </v-textarea>
                                                <v-row v-if="gestion.id === llamadaEditar" class="align-center mt-n1"
                                                    style="margin-top: 8px;">
                                                    <v-col cols="6" class="pa-0 pr-1" style="min-width:0;">
                                                        <v-btn block variant="tonal" color="primary"
                                                            style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                                            @click="guardarEdicionHistorial(gestion)">
                                                            💾 Guardar
                                                        </v-btn>
                                                    </v-col>
                                                    <v-col cols="6" class="pa-0 pl-1" style="min-width:0;">
                                                        <v-btn block variant="tonal" color="error"
                                                            style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                                            @click="llamadaEditar = null">
                                                            ❌ Cancelar
                                                        </v-btn>
                                                    </v-col>
                                                </v-row>
                                            </v-card-text>
                                        </v-card>
                                    </v-col>
                                </v-row>
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>

            </v-container>
        </v-main>

        <!-- Dialog Crear Campaña -->
        <v-dialog v-model="dialogCrearCampaña" max-width="640" transition="dialog-bottom-transition" persistent>
            <v-card rounded="xl" elevation="3" class="dialog-card">
                <!-- Header -->
                <v-card-title class="py-3 px-4 d-flex align-center" style="background:#006CA1;color:#fff;">
                    <v-icon class="mr-2">mdi-calendar-multiple</v-icon>
                    <span class="text-h6">{{ labelFormularioCampaña }}</span>
                    <v-spacer />
                    <v-btn icon variant="text" color="white" @click="cerrarFormularioCampaña()">
                        <v-icon>mdi-close</v-icon>
                    </v-btn>
                </v-card-title>

                <!-- Body -->
                <v-card-text class="px-4 pt-4 pb-0">
                    <v-form ref="formNuevaCampaña" v-model="formOk">
                        <v-text-field v-model.trim="selectedNombreCampaña" label="Nombre de la campaña"
                            prepend-inner-icon="mdi-bell" variant="outlined" density="comfortable" clearable
                            class="mb-3" />
                        <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                            Este campo es obligatorio
                        </div>

                        <v-textarea v-model.trim="selectedDetalleCampaña" label="Detalle de la campaña"
                            prepend-inner-icon="mdi-account-details-outline" variant="outlined" density="comfortable"
                            auto-grow rows="2" hint="Digitá la descripción que tendrá la campaña" persistent-hint
                            class="mb-3" />
                        <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                            Este campo es obligatorio
                        </div>

                        <v-textarea v-model.trim="selectedGuionCampaña" label="Guion de la campaña"
                            prepend-inner-icon="mdi-text-box-multiple-outline" variant="outlined" density="comfortable"
                            auto-grow rows="5" hint="Guión que se necesitará para realizar la campaña."
                            persistent-hint />
                        <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                            Este campo es obligatorio
                        </div>
                    </v-form>
                </v-card-text>

                <v-divider class="my-4" />

                <!-- Footer -->
                <v-card-actions class="px-4 pb-4 pt-0">
                    <v-spacer />
                    <v-btn variant="outlined" color="primary" class="btn-details text-none btn-grow-card mr-2"
                        @click="cerrarFormularioCampaña()">Cancelar</v-btn>
                    <v-btn v-if="labelFormularioCampaña === 'Crear nueva campaña'" variant="outlined" color="primary"
                        class="btn-details text-none btn-grow-card" @click="guardarFormularioCampaña()">
                        Guardar
                        <v-icon end class="ml-1">mdi-content-save-check</v-icon>
                    </v-btn>
                    <v-btn v-if="labelFormularioCampaña === 'Editar campaña'" variant="outlined" color="primary"
                        class="btn-details text-none btn-grow-card" @click="editarFormularioCampaña()">
                        Editar
                        <v-icon end class="ml-1">mdi-content-save-check</v-icon>
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <!-- Dialog Crear Campaña -->

        <!-- Dialog Guion Campaña -->
        <v-dialog v-model="dialogGuionCampaña" max-width="640" transition="dialog-bottom-transition" persistent>
            <v-card rounded="xl" elevation="3" class="dialog-card">
                <!-- Header -->
                <v-card-title class="py-3 px-4 d-flex align-center" style="background:#006CA1;color:#fff;">
                    <v-icon class="mr-2">mdi-calendar-multiple</v-icon>
                    <span class="text-h6">Speech & Guion de la Campaña</span>
                    <v-spacer />
                    <v-btn size="small" color="#3f94e8" rounded elevation="2"
                        :color="!roGuionCampaña ? 'yellow-darken-3' : 'indigo-darken-3'"
                        @click="roGuionCampaña = !roGuionCampaña">
                        ✍️ Editar Guion
                    </v-btn>
                    <v-btn icon variant="text" color="white"
                        @click="dialogGuionCampaña = false; roGuionCampaña = true; guionCampañaSeleccionada = campañaSeleccionada.guion;">
                        <v-icon>mdi-close</v-icon>
                    </v-btn>
                </v-card-title>

                <v-card-subtitle class="px-4 pt-4 pb-0 mb-0">
                    <p class="mb-2">Producto / Campaña</p>
                    <span style="font-weight: bold; font-size: 16px;">Campaña: {{ campañaSeleccionada.nombre }}</span>
                </v-card-subtitle>

                <!-- Body -->
                <v-card-text class="px-4 pt-4 pb-0 mt-n2 mb-6">
                    <v-textarea :readonly="roGuionCampaña" v-model.trim="guionCampañaSeleccionada"
                        label="Guion de la campaña" prepend-inner-icon="mdi-text-box-multiple-outline"
                        variant="outlined" density="comfortable" auto-grow rows="5"
                        hint="Guión que se necesitará para realizar la campaña." persistent-hint
                        :color="!roGuionCampaña ? 'yellow-darken-2' : undefined"
                        :append-inner-icon="!roGuionCampaña ? 'mdi-pencil' : undefined" />
                    <v-row>
                        <v-col>
                            <div v-if="!roGuionCampaña" class="mt-2"
                                style="color: #ff9800; font-weight: bold; display: flex; align-items: center;">
                                <v-icon color="orange-darken-4" class="mr-1">mdi-pencil</v-icon>
                                Modo edición activado
                            </div>
                        </v-col>

                        <v-col>
                            <v-btn v-if="!roGuionCampaña" variant="flat" color="#006CA1" class="mt-4"
                                @click="guardarGuionCampaña(campañaSeleccionada)" style="float: right;">
                                💾 Guardar Cambios
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-dialog>
        <!-- Dialog Guion Campaña -->

        <!-- Dialog Información Prospecto / Contacto -->
        <v-dialog v-model="dialogInfoProsCon" persistent max-width="1000">
            <v-card-title class="text-h6"
                style="background-color: #006CA1; color: white; display: flex; align-items: center;">

                <div class="d-flex align-center">
                    <v-icon class="mr-2">mdi-file-phone</v-icon>
                    Ficha del Prospecto
                </div>

                <v-spacer></v-spacer>
                <v-btn icon="mdi-close" size="small" color="white" @click="cerrarFichaProspecto()" class="btn-grow" />
            </v-card-title>

            <v-card>
                <v-card-text>
                    <v-row>
                        <v-col>
                            <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">Información de
                                la Empresa </h3>
                            <v-text-field class="mx-5" v-model="fichaNit" label="NIT" variant="outlined" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-numeric</v-icon>
                                </template>
                            </v-text-field>
                            <v-text-field class="mx-5" v-model="fichaRazonSocial" label="Razón Social"
                                variant="outlined" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-domain</v-icon>
                                </template>
                            </v-text-field>
                            <v-row>
                                <v-col>
                                    <v-select class="ml-5" v-model="fichaTipoId" :items="tipoIdentificacion"
                                        return-object item-title="nombre" item-value="id" label="Tipo Identificación"
                                        readonly variant="outlined" autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-card-account-details</v-icon>
                                        </template>
                                    </v-select>
                                </v-col>
                                <v-col>
                                    <v-select disabled class="mr-5" v-model="fichaTipoEmp" :items="tipoEmpresa"
                                        return-object item-title="nombre" item-value="id" label="Tipo Empresa"
                                        variant="outlined" autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-domain</v-icon>
                                        </template>
                                    </v-select>
                                </v-col>
                            </v-row>
                            <v-select class="mx-5" v-model="fichaSector" :items="sectorEmpresa" return-object
                                item-title="nombre" item-value="id" label="Sector" variant="outlined" autocomplete="off"
                                readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1"
                                        style="opacity: 100%;">mdi-office-building</v-icon>
                                </template>
                            </v-select>
                            <v-text-field class="mx-5" v-model="fichaDireccion" label="Dirección" type="text"
                                variant="outlined" autocomplete="off" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-map-marker</v-icon>
                                </template>
                            </v-text-field>
                            <v-row>
                                <v-col>
                                    <v-autocomplete class="ml-5" v-model="fichaDepartamento" :items="departamentos"
                                        return-object item-title="nombre" item-value="id" label="Departamento"
                                        variant="outlined" autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-home-city</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                                <v-col>
                                    <v-autocomplete class="mr-5" v-model="fichaCiudad" :items="ciudades" return-object
                                        item-title="nombre" item-value="id" label="Ciudad" variant="outlined"
                                        autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-city-variant</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                            </v-row>
                            <v-text-field class="mx-5" v-model="fichaWeb" label="Pagina Web" type="text"
                                variant="outlined" autocomplete="off" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-web</v-icon>
                                </template>
                            </v-text-field>
                            <v-text-field class="mx-5" v-model="fichaCorreoEmpresa" label="Mail Empresa" type="email"
                                variant="outlined" autocomplete="off" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                                </template>
                            </v-text-field>
                            <v-row>
                                <v-col>
                                    <v-text-field class="ml-5" @input="filterTel1" :rules="[maxlength2].flat()"
                                        v-model="fichaTel1" label="Telefono 1" type="number" variant="outlined"
                                        autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-cellphone</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>
                                <v-col>
                                    <v-text-field class="mr-5" v-model="fichaTel2" label="Telefono 2" type="number"
                                        variant="outlined" autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-phone</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>

                            </v-row>
                        </v-col>
                        <v-col style="border-left: 1px solid #ccc; padding-left: 20px;">
                            <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">Información del
                                Contacto</h3>
                            <v-text-field class="mx-5" v-model="fichaNombre" label="Nombre" type="text"
                                variant="outlined" autocomplete="off" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                                </template>
                            </v-text-field>
                            <v-text-field class="mx-5" v-model="fichaApellido" label="Apellido" type="text"
                                variant="outlined" autocomplete="off" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                                </template>
                            </v-text-field>
                            <v-row>
                                <v-col>
                                    <v-autocomplete class="mx-5" v-model="fichaCategoria" :items="categorias"
                                        return-object item-title="nombre" item-value="id" label="Categoria Cargo"
                                        variant="outlined" autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-format-list-bulleted-type</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                                <v-col>
                                    <v-autocomplete class="mx-5 ml-0" v-model="fichaCargo" :items="cargos" return-object
                                        item-title="nombre" item-value="id" label="Cargo" type="text" variant="outlined"
                                        autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-account-tie</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                            </v-row>
                            <v-text-field class="mx-5" v-model="fichaCorreoContacto" label="Correo" type="email"
                                variant="outlined" autocomplete="off" readonly>
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                                </template>
                            </v-text-field>

                            <v-row>
                                <v-col cols="4" class="m-0">
                                    <v-text-field class="mx-5 mr-0" v-model="fichaExtension" label="Extensión"
                                        type="number" variant="outlined" autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-phone-in-talk</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>
                                <v-col cols="8">
                                    <v-text-field @input="filterNumber" :rules="[maxlength2].flat()"
                                        class="mx-5 ml-0 pl-0" v-model="fichaCelular" label="Celular" type="number"
                                        variant="outlined" autocomplete="off" readonly>
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-cellphone</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-dialog>
        <!-- Dialog Información Prospecto / Contacto -->

        <!-- FORMULARIO PROSPECTO CONTACTO-->

        <v-dialog v-model="formularioProspecto" width="1100" persistent>
            <v-card-title class="text-h6"
                style="background-color: #006CA1; color: white; display: flex; align-items: center;">

                <div class="d-flex align-center">
                    <v-icon class="mr-2">mdi mdi-account-group </v-icon>
                    Nuevo Prospecto
                </div>

                <v-spacer></v-spacer>
                <v-btn icon="mdi-close" size="small" color="white" @click="cerrarFormularioProspecto()"
                    class="btn-grow" />
            </v-card-title>

            <v-card>
                <v-card-text>
                    <v-row>
                        <v-col>
                            <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">Información de
                                la
                                Empresa
                            </h3>
                            <!--<v-autocomplete class="mx-5" v-model="empresa" :items="empresas" return-object item-title="nombre"
                      item-value="id" label="Empresa" variant="outlined" clearable />-->
                            <v-alert v-if="alertaNit" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                                this.mensajeAlertaNit
                            }}</v-alert>
                            <!--<v-text-field class="mx-5" v-model="nit" label="Número de Identificación" type="number"
                      variant="outlined" clearable />-->

                            <v-row>
                                <v-col cols="11">
                                    <input class="campo-input mx-5 mb-5" list="empresas" id="empresa" v-model="nit"
                                        placeholder="NIT" autocomplete="off" type="number" />
                                </v-col>
                                <v-col style="margin-left: -30px;">
                                    <v-icon class="mt-2" @click="nit = null">
                                        mdi-close-circle
                                    </v-icon>
                                </v-col>
                            </v-row>

                            <datalist id="empresas">
                                <option v-for="(empresa, index) in listaEmpresas" :key="empresa.id"
                                    :value="`${empresa.p_nit}`">
                                </option>
                            </datalist>

                            <v-alert v-if="alertaRazonSocial" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                                this.mensajeAlertaRazonSocial
                            }}</v-alert>
                            <!--<v-text-field class="mx-5" v-model="razonSocial" label="Razón Social" type="text" variant="outlined"
                      clearable />-->
                            <v-row>
                                <v-col cols="11">
                                    <input class="campo-input mx-5 mb-5" list="empresas2" id="empresa"
                                        v-model="razonSocial" placeholder="Razón Social" autocomplete="off" />
                                </v-col>
                                <v-col style="margin-left: -30px;">
                                    <v-icon class="mt-2" @click="razonSocial = null">
                                        mdi-close-circle
                                    </v-icon>
                                </v-col>
                            </v-row>

                            <datalist id="empresas2">
                                <option v-for="(empresa, index) in listaEmpresas2" :key="empresa.id"
                                    :value="`${empresa.p_razon_social}`">
                                </option>
                            </datalist>
                            <v-row>
                                <v-col>
                                    <v-select class="ml-5" v-model="tipoId" :items="tipoIdentificacion" return-object
                                        item-title="nombre" item-value="id" label="Tipo Identificación"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-card-account-details</v-icon>
                                        </template>
                                    </v-select>
                                </v-col>
                                <v-col>
                                    <v-select disabled class="mr-5" v-model="tipoEmp" :items="tipoEmpresa" return-object
                                        item-title="nombre" item-value="id" label="Tipo Empresa" variant="outlined"
                                        clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-domain</v-icon>
                                        </template>
                                    </v-select>
                                </v-col>
                            </v-row>
                            <v-select class="mx-5" v-model="sector" :items="sectorEmpresa" return-object
                                item-title="nombre" item-value="id" label="Sector" variant="outlined" clearable
                                autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1"
                                        style="opacity: 100%;">mdi-office-building</v-icon>
                                </template>
                            </v-select>
                            <v-text-field class="mx-5" v-model="direccion" label="Dirección" type="text"
                                variant="outlined" clearable autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-map-marker</v-icon>
                                </template>
                            </v-text-field>
                            <v-row>
                                <v-col>
                                    <v-autocomplete class="ml-5" v-model="departamento" :items="departamentos"
                                        return-object item-title="nombre" item-value="id" label="Departamento"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-home-city</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                                <v-col>
                                    <v-autocomplete class="mr-5" v-model="ciudad" :items="ciudades" return-object
                                        item-title="nombre" item-value="id" label="Ciudad" variant="outlined" clearable
                                        autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-city-variant</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                            </v-row>
                            <v-text-field class="mx-5" v-model="web" label="Pagina Web" type="text" variant="outlined"
                                clearable autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-web</v-icon>
                                </template>
                            </v-text-field>
                            <v-text-field class="mx-5" v-model="correoEmpresa" label="Mail Empresa" type="email"
                                variant="outlined" clearable autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                                </template>
                            </v-text-field>
                            <v-row>
                                <v-col>
                                    <v-text-field class="ml-5" @input="filterTel1" :rules="[maxlength2].flat()"
                                        v-model="tel1" label="Telefono 1" type="number" variant="outlined" clearable
                                        autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-cellphone</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>
                                <v-col>
                                    <v-text-field class="mr-5" v-model="tel2" label="Telefono 2" type="number"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-phone</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>

                            </v-row>
                            <v-select class="mx-5" clearable label="Servicio" v-model="selectedServicioProspecto"
                                :items="selectServiciosActividad" return-object item-title="nombre" item-value="id"
                                variant="outlined" autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-briefcase</v-icon>
                                </template></v-select>

                        </v-col>
                        <v-col style="border-left: 1px solid #ccc; padding-left: 20px;">
                            <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">Información del
                                Contacto</h3>
                            <v-text-field class="mx-5" v-model="nombre" label="Nombre" type="text" variant="outlined"
                                clearable autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                                </template>
                            </v-text-field>
                            <v-text-field class="mx-5" v-model="apellido" label="Apellido" type="text"
                                variant="outlined" clearable autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                                </template>
                            </v-text-field>
                            <v-row>
                                <v-col>
                                    <v-autocomplete class="mx-5" v-model="categoria" :items="categorias" return-object
                                        item-title="nombre" item-value="id" label="Categoria Cargo" variant="outlined"
                                        clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-format-list-bulleted-type</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                                <v-col>
                                    <v-autocomplete class="mx-5 ml-0" v-model="cargo" :items="cargos" return-object
                                        item-title="nombre" item-value="id" label="Cargo" type="text" variant="outlined"
                                        clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-account-tie</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>
                            </v-row>
                            <v-text-field class="mx-5" v-model="correoContacto" label="Correo" type="email"
                                variant="outlined" clearable autocomplete="off">
                                <template v-slot:prepend-inner>
                                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                                </template>
                            </v-text-field>

                            <v-row>
                                <v-col cols="4" class="m-0">
                                    <v-text-field class="mx-5 mr-0" v-model="extension" label="Extensión" type="number"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-phone-in-talk</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>
                                <v-col cols="8">
                                    <v-text-field @input="filterNumber()" :rules="[maxlength2].flat()"
                                        class="mx-5 ml-0 pl-0" v-model="celular" label="Celular" type="number"
                                        variant="outlined" autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon size="small" color="#006CA1"
                                                style="opacity: 100%;">mdi-cellphone</v-icon>
                                        </template>
                                    </v-text-field>
                                </v-col>
                                <v-col>
                                    <v-alert v-if="alertaCelular" class="mx-5 mb-5" type="error"
                                        icon="mdi-account-alert">{{
                                            this.mensajeAlertaCelular
                                        }}</v-alert>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn variant="outlined" color="primary" class=" text-none btn-grow-card"
                        @click="cerrarFormularioProspecto()">Cancelar</v-btn>

                    <v-btn color="primary" variant="flat" size="large" rounded="lg" class="text-none px-5 btn-grow-card"
                        prepend-icon="mdi mdi-content-save-check-outline" :disabled="dsGuardar"
                        @click="guardarDatos()">Guardar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <!-- FORMULARIO PROSPECTO CONTACTO-->

        <!-- Dialog detalles de llamadas -->
        <v-dialog v-model="dialogListaLlamadas" max-width="95%" height="100vh" persistent>
            <v-card-title class="text-h7"
                style="background-color: #006CA1; color: white; display: flex; align-items: center;">
                <div class="d-flex align-center">
                    <v-icon class="mr-2" size="small">mdi mdi-view-list-outline</v-icon>
                    <span>Listar Llamadas Realizadas</span>
                </div>
                <v-spacer></v-spacer>
                <v-select v-model="filtroLlamadasSeleccionado" :items="filtrosLlamadas" label="Filtrar por"
                    variant="solo" density="compact" style="max-width: 250px; vertical-align: middle; margin-top: 2px;"
                    class="mr-4" return-object hide-details item-title="nombre" item-value="id" clearable
                    @update:model-value="abrirListaLlamadas(filtroLlamadasSeleccionado ? filtroLlamadasSeleccionado.id : filtroInicialSeleccionado)">
                    <template v-slot:prepend-inner>
                        <v-icon size="16">mdi-filter-variant</v-icon>
                    </template>
                </v-select>
                <v-text-field v-model="searchLlamadas" @update:model-value="onSearchInput"
                    placeholder="Buscar por Prospecto, Cliente, Campaña, Interes, Motivo"
                    prepend-inner-icon="mdi-magnify" density="compact" variant="solo" clearable
                    class="header-search mr-6" hide-details style="max-width: 380px;" />
                <v-btn icon="mdi-close" size="small" color="white"
                    @click="dialogListaLlamadas = false; filtroInicialSeleccionado = null;" class="btn-grow" />
            </v-card-title>
            <v-card class="pt-0">

                <!-- Tabla Prospectos / Seguimientos -->
                <v-data-table :headers="headersLlamadas" :items="arrayLlamadas"
                    :sort-by="[{ key: 'fecha', order: 'desc' }]" :search="searchLlamadas"
                    :filter-keys="['nombre', 'nombre_campania', 'interes_texto', 'motivo']"
                    class="elevation-1 rounded-lg data-table fancy-headers fancy-rows" density="compact" virtual-scroll
                    hover fixed-header height="78vh" :items-per-page="20" :items-per-page-options="[10, 20, 50]"
                    items-per-page-text="Registros por página" page-text="({0}-{1}) de ({2})"
                    no-data-text="No hay registros" @click:row="(_, row) => abrirNuevaActividad(row.item)"
                    :item-class="() => 'btn-grow-card-items fancy-row'">

                    <!--HEADERs-->
                    <!-- Header con ícono por columna -->
                    <template #header.nombre_campania="{ column }">
                        <div class="th-content">
                            <v-icon size="16">mdi-bell-circle</v-icon>
                            <span>{{ column.title }}</span>
                        </div>
                    </template>

                    <template #header.nombre="{ column }">
                        <div class="th-content">
                            <v-icon size="16">mdi-rename</v-icon>
                            <span>{{ column.title }}</span>
                        </div>
                    </template>

                    <template #header.fecha="{ column }">
                        <div class="th-content">
                            <v-icon size="16">mdi-calendar-month</v-icon>
                            <span>{{ column.title }}</span>
                        </div>
                    </template>

                    <template #header.respuesta="{ column }">
                        <div class="th-content">
                            <v-icon size="16">mdi-text-account</v-icon>
                            <span>{{ column.title }}</span>
                        </div>
                    </template>

                    <template #header.interes="{ column }">
                        <div class="th-content">
                            <v-icon size="16">mdi-account-alert</v-icon>
                            <span>{{ column.title }}</span>
                        </div>
                    </template>

                    <template #header.motivo="{ column }">
                        <div class="th-content">
                            <v-icon size="16">mdi-account-voice</v-icon>
                            <span>{{ column.title }}</span>
                        </div>
                    </template>

                    <template #header.fecha_reprogramacion="{ column }">
                        <div class="th-content">
                            <v-icon size="16">mdi-calendar-clock</v-icon>
                            <span>{{ column.title }}</span>
                        </div>
                    </template>

                    <!---------->
                    <!--FILAS-->

                    <!-- Fechas en dd/mm/aaaa -->
                    <template #item.fecha="{ item, column }">
                        {{ formatDate(item.fecha) }}
                    </template>
                    <template #item.fecha_reprogramacion="{ item, column }">
                        {{ item.fecha_reprogramacion != 'No se reprograma' ? formatDate(item.fecha_reprogramacion) : '—'
                        }}
                    </template>

                    <template #item.fecha_registro="{ item, column }">
                        {{ formatDate(item.fecha_registro) == '01/01/1970 00:00' ? '—' : formatDate(item.fecha_registro)
                        }}
                    </template>

                    <template #item.fecha_primer_contacto="{ item, column }">
                        {{ formatDate(item.fecha_primer_contacto) == '01/01/1970 00:00' ? '—' :
                            formatDate(item.fecha_primer_contacto)
                        }}
                    </template>

                    <template #item.fecha_registro_prospecto="{ item, column }">
                        {{ formatDate(item.fecha_registro_prospecto) == '01/01/1970 00:00' ? '—' :
                            formatDate(item.fecha_registro_prospecto)
                        }}
                    </template>

                    <!-- Interes con nombres propios -->
                    <template #item.interes="{ item, column }">
                        <span v-if="item.interes === 0">Llamada Efectiva con Lead</span>
                        <span v-else-if="item.interes === 1">Llamada Efectiva sin Lead</span>
                        <span v-else-if="item.interes === 2">Llamada No Efectiva</span>
                        <span v-else>—</span>
                    </template>

                    <template #item.estado_proceso="{ item, column }">
                        <span v-if="item.estado_proceso === 0">Nuevo</span>
                        <span v-else-if="item.estado_proceso === 1">Prospecto</span>
                        <span v-else-if="item.estado_proceso === 2">En Proceso</span>
                        <span v-else-if="item.estado_proceso === 3">Cotizado</span>
                        <span v-else-if="item.estado_proceso === 4">Cerrado Exitoso</span>
                        <span v-else-if="item.estado_proceso === 5">Cerrado Declinado</span>
                        <span v-else>—</span>
                    </template>

                </v-data-table>
            </v-card>
        </v-dialog>
        <!-- Dialog detalles de llamadas -->

        <!-- Dialog historial de ediciones -->
        <v-dialog v-model="dialogHistorialEdiciones" max-width="200vh" height="100vh" persistent>
            <v-card class="pa-4" style="height: 100%;">
                <v-card variant="outlined" elevation="5" class="pa-4 rounded-xl d-flex flex-column"
                    style="height: 100%;">
                    <!-- Encabezado -->
                    <div style="position: sticky; top: 0; z-index: 2; margin-bottom: 2vh;" class="rounded-xs">
                        <v-alert color="#027cb8" class="mb-4 pa-4 rounded-xs ">
                            <v-row align="center" justify="space-between" class="ma-0 pa-0">
                                <v-col cols="12" md="4" class="d-flex align-center">
                                    <v-icon size="26" color="white">mdi-history</v-icon>
                                    <h2 class="ml-2 mb-0">Historial de Ediciones de Observaciones</h2>
                                </v-col>
                                <v-col cols="12" md="8" class="d-flex justify-end align-center" style="gap: 20px;">
                                    <v-text-field v-model="buscadorHistorialGeneral" placeholder="Buscar en historial…"
                                        density="compact" variant="solo" bg-color="rgba(255,255,255, 0.9)"
                                        base-color="rgba(255,255,255, 0.9)" color="white"
                                        prepend-inner-icon="mdi-magnify" clearable rounded="lg" hide-details
                                        style="max-width: 320px;" />
                                    <v-text-field v-model="busquedaFechaHistorialInicio" type="date" density="compact"
                                        variant="solo"
                                        :bg-color="busquedaFechaHistorialFin && !busquedaFechaHistorialInicio ? '#fffbe6' : 'rgba(255,255,255, 0.9)'"
                                        prepend-inner-icon="mdi-calendar" clearable rounded="lg" hide-details
                                        style="max-width: 200px;" label="Desde"
                                        :max="busquedaFechaHistorialFin || undefined"
                                        :error="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialInicio > busquedaFechaHistorialFin"
                                        :hint="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialInicio > busquedaFechaHistorialFin ? 'La fecha desde no puede ser mayor que la fecha hasta' : (busquedaFechaHistorialFin && !busquedaFechaHistorialInicio ? 'Selecciona fecha desde' : '')"
                                        persistent-hint />
                                    <v-text-field v-model="busquedaFechaHistorialFin" type="date" density="compact"
                                        variant="solo"
                                        :bg-color="busquedaFechaHistorialInicio && !busquedaFechaHistorialFin ? '#fffbe6' : 'rgba(255,255,255, 0.9)'"
                                        prepend-inner-icon="mdi-calendar" clearable rounded="lg" hide-details
                                        style="max-width: 200px;" label="Hasta"
                                        :min="busquedaFechaHistorialInicio || undefined"
                                        :error="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialFin < busquedaFechaHistorialInicio"
                                        :hint="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialFin < busquedaFechaHistorialInicio ? 'La fecha hasta no puede ser menor que la fecha desde' : (busquedaFechaHistorialInicio && !busquedaFechaHistorialFin ? 'Selecciona fecha hasta' : '')"
                                        persistent-hint />
                                    <v-tooltip text="Cerrar Historial" location="top">
                                        <template #activator="{ props }">
                                            <v-btn icon size="small" class="btn-grow" v-bind="props"
                                                @click="dialogHistorialEdiciones = false; buscadorHistorialGeneral = null; busquedaFechaHistorialInicio = null; busquedaFechaHistorialFin = null;">
                                                <v-icon color="black">mdi-window-close</v-icon>
                                            </v-btn>
                                        </template>
                                    </v-tooltip>
                                </v-col>
                            </v-row>
                        </v-alert>
                    </div>
                    <!-- Cuerpo scroll -->
                    <div style="overflow-y: auto; flex: 1; max-height: 60vh;" class="mt-2 mb-2 ml-2 custom-scroll">
                        <v-row v-for="(item, index) in filteredHistorialEdiciones" :key="index" class="mb-2 align-start"
                            no-gutters>
                            <!-- Avatar usuario -->
                            <v-col cols="auto" class="pr-2 d-flex justify-center">
                                <v-avatar size="36" color="#1976d2">
                                    <v-icon color="white" size="22">mdi-account-edit</v-icon>
                                </v-avatar>
                            </v-col>
                            <!-- Tarjeta de edición -->
                            <v-col>
                                <v-card class="pa-3" variant="outlined" style="border-radius: 10px; font-size: 2vh;">
                                    <div class="d-flex justify-space-between align-center mb-1">
                                        <div class="d-flex align-center">
                                            <v-icon size="18" color="#1976d2" class="mr-1">mdi-account</v-icon>
                                            <span style="font-weight: 600; color: #1976d2;">{{ item.nombre_usu }}</span>
                                        </div>
                                        <div class="d-flex align-center">
                                            <v-icon size="16" color="#027cb8" class="mr-1">mdi-calendar-clock</v-icon>
                                            <span style="font-size: 1.5vh;">Edición: {{ formatDate(item.fecha_edicion)
                                                }}</span>
                                        </div>
                                    </div>
                                    <div class="d-flex align-center mb-2">
                                        <v-icon size="16" color="#757575" class="mr-1">mdi-calendar-edit</v-icon>
                                        <span class="text-caption">Original: {{
                                            formatDate(item.fecha_original_historial)
                                            }}</span>
                                    </div>
                                    <v-divider class="my-2" />
                                    <div class="mb-2">
                                        <v-icon size="18" color="#43a047" class="mr-1">mdi-pencil</v-icon>
                                        <span style="font-weight: 500; color: #43a047;">Observación editada:</span>
                                        <span class="ml-2">{{ item.texto_editado }}</span>
                                    </div>
                                    <div class="mb-2">
                                        <v-icon size="18" color="#fbc02d" class="mr-1">mdi-history</v-icon>
                                        <span style="font-weight: 500; color: #fbc02d;">Observación original:</span>
                                        <span class="ml-2">{{ item.texto_original }}</span>
                                    </div>
                                </v-card>
                            </v-col>
                        </v-row>
                    </div>
                </v-card>
            </v-card>
        </v-dialog>
        <!-- Dialog historial de ediciones -->

        <!-- Dialog historial de ediciones -->
        <v-dialog v-model="dialogHistorialGlobal" max-width="200vh" height="100vh" persistent>
            <v-card variant="outlined" elevation="5" class="pa-4 rounded-xl d-flex flex-column"
                style="height: 100%; background-color: white;">
                <!-- Encabezado -->
                <div style="position: sticky; top: 0; z-index: 2; margin-bottom: 2vh;" class="rounded-xs">
                    <v-alert color="#027cb8" class="mb-4 pa-4 rounded-xs ">
                        <v-row align="center" justify="space-between" class="ma-0 pa-0">
                            <v-col cols="12" md="4" class="d-flex align-center">
                                <v-icon size="26" color="white">mdi-history</v-icon>
                                <h2 class="ml-2 mb-0">Historial Global</h2>
                            </v-col>
                            <v-col cols="12" md="8" class="d-flex justify-end align-center" style="gap: 20px;">
                                <v-btn icon color="#d2e6fa" class="btn-grow-card" size="large"
                                    style="margin-right: 8px;" title="Agrupar Campañas" v-if="historialActivo == 1"
                                    @click="tipoAgrupacion = 1; cargarHistorialGlobalLlamadas(tipoAgrupacion);">
                                    <v-icon color="#1976d2" size="28">mdi-bullhorn</v-icon>
                                </v-btn>
                                <v-btn icon color="#d2f8e5" class="btn-grow-card" size="large"
                                    style="margin-right: 8px;" title="Agrupar Prospectos" v-if="historialActivo == 1"
                                    @click="tipoAgrupacion = 2; cargarHistorialGlobalLlamadas(tipoAgrupacion);">
                                    <v-icon color="#43a047" size="28">mdi-office-building</v-icon>
                                </v-btn>
                                <v-btn icon color="#f8d2d2" class="btn-grow-card" size="large"
                                    style="margin-right: 8px;" title="Sin Agrupar" v-if="historialActivo == 1"
                                    @click="tipoAgrupacion = 3; cargarHistorialGlobalLlamadas(tipoAgrupacion);">
                                    <v-icon color="#e53935" size="28">mdi-format-list-bulleted</v-icon>
                                </v-btn>
                                <v-btn icon color="#d2e6fa" class="btn-grow-card" size="large"
                                    style="margin-right: 8px;" title="Agrupar Campañas" v-if="historialActivo == 2"
                                    @click="tipoAgrupacion = 1; llamadoHistorialLead(tipoAgrupacion);">
                                    <v-icon color="#1976d2" size="28">mdi-bullhorn</v-icon>
                                </v-btn>
                                <v-btn icon color="#d2f8e5" class="btn-grow-card" size="large"
                                    style="margin-right: 8px;" title="Agrupar Prospectos" v-if="historialActivo == 2"
                                    @click="tipoAgrupacion = 2; llamadoHistorialLead(tipoAgrupacion);">
                                    <v-icon color="#43a047" size="28">mdi-office-building</v-icon>
                                </v-btn>
                                <v-btn icon color="#f8d2d2" class="btn-grow-card" size="large"
                                    style="margin-right: 8px;" title="Sin Agrupar" v-if="historialActivo == 2"
                                    @click="tipoAgrupacion = 3; llamadoHistorialLead(tipoAgrupacion);">
                                    <v-icon color="#e53935" size="28">mdi-format-list-bulleted</v-icon>
                                </v-btn>
                                <v-btn variant="flat" color="teal-darken-2" class="btn-grow-card"
                                    @click="tipoAgrupacion = 1; historialActivo = 1; cargandoHistorial2 = true; historialGestion = []; llamadoHistorialGestion(); cargarHistorialGlobalLlamadas(tipoAgrupacion);">
                                    <v-icon left size="16">mdi-phone</v-icon>
                                    Llamadas
                                </v-btn>
                                <v-btn variant="flat" color="orange-darken-3" class="btn-grow-card"
                                    @click="tipoAgrupacion = 1; historialActivo = 2; cargandoHistorial2 = true; historialLead = []; llamadoHistorialLead(tipoAgrupacion);">
                                    <v-icon left size="16">mdi-account-plus</v-icon>
                                    Proceso Lead
                                </v-btn>
                                <v-tooltip text="Cerrar Historial" location="top">
                                    <template #activator="{ props }">
                                        <v-btn icon size="small" class="btn-grow" v-bind="props"
                                            @click="dialogHistorialGlobal = false; tipoAgrupacion = 1;">
                                            <v-icon color="black">mdi-window-close</v-icon>
                                        </v-btn>
                                    </template>
                                </v-tooltip>
                            </v-col>
                        </v-row>
                    </v-alert>
                </div>
                <!-- Cuerpo scroll -->
                <div style="overflow-y: auto; flex: 1; max-height: 100vh;" class="mt-n4 mb-2 ml-2 custom-scroll">
                    <v-progress-circular :size="50" v-if="cargandoHistorial2" indeterminate color="primary"
                        class="ma-4"></v-progress-circular>

                    <v-card color="#f0f4f8" v-for="campaña in historialGlobalLlamadas.data" :key="campaña.id"
                        v-if="!cargandoHistorial2 && historialActivo == 1 && tipoAgrupacion == 1" class="mb-4">
                        <v-card-title class="text-h6" style="color: #0A1C3A; font-weight: bold;">
                            <v-icon left size="20" color="#0A1C3A" class="mr-2">mdi-bell-circle</v-icon>
                            Campaña: {{ campaña.nombre_campania }}
                        </v-card-title>

                        <v-card-text style="color: #0A1C3A; font-size: 14px;">
                            Total Llamadas: <strong>{{ campaña.detalles.length }}</strong> |
                            Llamadas Efectivas con Lead: <strong>{{ campaña.llamadas_con_lead }}</strong> |
                            Llamadas Efectivas sin Lead: <strong>{{ campaña.llamadas_sin_lead }}</strong> |
                            Llamadas No Efectivas: <strong>{{ campaña.llamadas_no_efectivas }}</strong>
                        </v-card-text>

                        <v-card-actions class="mt-n4 mb-2">
                            <v-expansion-panels bg-color="#d3e2ed" class="btn-grow-card-items">
                                <v-expansion-panel>
                                    <v-expansion-panel-title>
                                        Ver Detalles de Llamadas
                                    </v-expansion-panel-title>
                                    <v-expansion-panel-text>
                                        <div class="timeline-container" v-if="historialActivo == 1"
                                            style="height: 500px; overflow-y: auto;">
                                            <div v-for="(gestion, idx) in campaña.detalles" :key="gestion.id"
                                                class="timeline-item">
                                                <!-- Línea vertical y punto -->
                                                <div class="timeline-marker" :class="timelineColor(gestion.interes)">
                                                    <v-icon :color="timelineIconColor(gestion.interes)" size="22">
                                                        {{ timelineIcon(gestion.interes) }}
                                                    </v-icon>
                                                </div>
                                                <div class="timeline-content">
                                                    <p class="mt-2"><strong># de Campaña: </strong>{{ gestion.idcampenv
                                                    }}</p>
                                                    <div class="d-flex align-center justify-space-between">
                                                        <span class="timeline-date">{{ formatDate(gestion.fecha)
                                                        }}</span>
                                                        <span class="timeline-type">
                                                            <v-icon size="18"
                                                                :color="timelineIconColor(gestion.interes)">
                                                                {{ timelineIcon(gestion.interes) }}
                                                            </v-icon>
                                                            {{ interesToText(gestion.interes) }}
                                                        </span>
                                                        <span v-if="gestion.Editado == 'Si'" class="ml-2"
                                                            style="font-size: 10px; color: red; font-weight: bold;">
                                                            🖋️ Editado
                                                        </span>
                                                        <v-btn v-if="gestion.Editado == 'Si'" icon variant="text"
                                                            color="primary" class="ml-2"
                                                            title="Ver historial de ediciones"
                                                            @click="abrirHistorialEdiciones(gestion)">
                                                            <v-icon style="font-size: 16px;">mdi-history</v-icon>
                                                        </v-btn>
                                                    </div>
                                                    <div class="timeline-text mt-2">
                                                        <p style="margin-top: 0;">
                                                            <strong>Prospecto:</strong> {{ gestion.razon_social }}
                                                        </p>
                                                        <p style="margin-top: 0;">"<strong>Gestión:</strong> {{
                                                            gestion.respuesta }}"</p>
                                                        <v-btn class="mb-2 mr-2 mt-n4" variant="text" color="primary"
                                                            style="font-size: 12px; float: right;"
                                                            @click="llamadaEditar = gestion.id">
                                                            ✍️ Editar
                                                        </v-btn>
                                                        <v-textarea v-if="gestion.id === llamadaEditar"
                                                            v-model="texto_editado" label="Editar observación" outlined
                                                            clearable class="mt-4" density="compact" variant="outlined"
                                                            style="min-width: 120px; max-width: 90%;">
                                                        </v-textarea>
                                                        <v-row v-if="gestion.id === llamadaEditar"
                                                            class="align-center mt-n1" style="margin-top: 8px;">
                                                            <v-col cols="6" class="pa-0 pr-1" style="min-width:0;">
                                                                <v-btn block variant="tonal" color="primary"
                                                                    class="ml-4 mb-6"
                                                                    style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                                                    @click="guardarEdicionHistorial(gestion)">
                                                                    💾 Guardar
                                                                </v-btn>
                                                            </v-col>
                                                            <v-col cols="6" class="pa-0 pl-1" style="min-width:0;">
                                                                <v-btn block variant="tonal" color="error" class="mb-6"
                                                                    style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                                                    @click="llamadaEditar = null">
                                                                    ❌ Cancelar
                                                                </v-btn>
                                                            </v-col>
                                                        </v-row>
                                                    </div>
                                                </div>
                                                <!-- Línea vertical entre items -->
                                                <div v-if="idx < historialGestion.length - 1"
                                                    class="timeline-connector">
                                                </div>
                                            </div>
                                        </div>
                                    </v-expansion-panel-text>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </v-card-actions>
                    </v-card>

                    <v-card color="#f0f4f8" v-for="campaña in historialGlobalLlamadas.data" :key="campaña.id"
                        v-if="!cargandoHistorial2 && historialActivo == 1 && tipoAgrupacion == 2" class="mb-4">
                        <v-card-title class="text-h6" style="color: #0A1C3A; font-weight: bold;">
                            <v-icon left size="20" color="#0A1C3A" class="mr-2">mdi-bell-circle</v-icon>
                            Prospecto: {{ campaña.razon_social }}
                        </v-card-title>

                        <v-card-text style="color: #0A1C3A; font-size: 14px;">
                            Total Llamadas: <strong>{{ campaña.detalles.length }}</strong> |
                            Llamadas Efectivas con Lead: <strong>{{ campaña.llamadas_con_lead }}</strong> |
                            Llamadas Efectivas sin Lead: <strong>{{ campaña.llamadas_sin_lead }}</strong> |
                            Llamadas No Efectivas: <strong>{{ campaña.llamadas_no_efectivas }}</strong>
                        </v-card-text>

                        <v-card-actions class="mt-n4 mb-2">
                            <v-expansion-panels bg-color="#d3e2ed" class="btn-grow-card-items">
                                <v-expansion-panel>
                                    <v-expansion-panel-title>
                                        Ver Detalles de Llamadas
                                    </v-expansion-panel-title>
                                    <v-expansion-panel-text>
                                        <div class="timeline-container" v-if="historialActivo == 1"
                                            style="height: 500px; overflow-y: auto;">
                                            <div v-for="(gestion, idx) in campaña.detalles" :key="gestion.id"
                                                class="timeline-item">
                                                <!-- Línea vertical y punto -->
                                                <div class="timeline-marker" :class="timelineColor(gestion.interes)">
                                                    <v-icon :color="timelineIconColor(gestion.interes)" size="22">
                                                        {{ timelineIcon(gestion.interes) }}
                                                    </v-icon>
                                                </div>
                                                <div class="timeline-content">
                                                    <p class="mt-2"><strong>Nombre Campaña: </strong>{{
                                                        gestion.nombre_campania
                                                        }}</p>
                                                    <div class="d-flex align-center justify-space-between">
                                                        <span class="timeline-date">{{ formatDate(gestion.fecha)
                                                        }}</span>
                                                        <span class="timeline-type">
                                                            <v-icon size="18"
                                                                :color="timelineIconColor(gestion.interes)">
                                                                {{ timelineIcon(gestion.interes) }}
                                                            </v-icon>
                                                            {{ interesToText(gestion.interes) }}
                                                        </span>
                                                        <span v-if="gestion.Editado == 'Si'" class="ml-2"
                                                            style="font-size: 10px; color: red; font-weight: bold;">
                                                            🖋️ Editado
                                                        </span>
                                                        <v-btn v-if="gestion.Editado == 'Si'" icon variant="text"
                                                            color="primary" class="ml-2"
                                                            title="Ver historial de ediciones"
                                                            @click="abrirHistorialEdiciones(gestion)">
                                                            <v-icon style="font-size: 16px;">mdi-history</v-icon>
                                                        </v-btn>
                                                    </div>
                                                    <div class="timeline-text mt-2">
                                                        <p style="margin-top: 0;">
                                                            <strong>Prospecto:</strong> {{ gestion.razon_social }}
                                                        </p>
                                                        <p style="margin-top: 0;">"<strong>Gestión:</strong> {{
                                                            gestion.respuesta }}"</p>
                                                        <v-btn class="mb-2 mr-2 mt-n4" variant="text" color="primary"
                                                            style="font-size: 12px; float: right;"
                                                            @click="llamadaEditar = gestion.id">
                                                            ✍️ Editar
                                                        </v-btn>
                                                        <v-textarea v-if="gestion.id === llamadaEditar"
                                                            v-model="texto_editado" label="Editar observación" outlined
                                                            clearable class="mt-4" density="compact" variant="outlined"
                                                            style="min-width: 120px; max-width: 90%;">
                                                        </v-textarea>
                                                        <v-row v-if="gestion.id === llamadaEditar"
                                                            class="align-center mt-n1" style="margin-top: 8px;">
                                                            <v-col cols="6" class="pa-0 pr-1" style="min-width:0;">
                                                                <v-btn block variant="tonal" color="primary"
                                                                    class="ml-4 mb-6"
                                                                    style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                                                    @click="guardarEdicionHistorial(gestion)">
                                                                    💾 Guardar
                                                                </v-btn>
                                                            </v-col>
                                                            <v-col cols="6" class="pa-0 pl-1" style="min-width:0;">
                                                                <v-btn block variant="tonal" color="error" class="mb-6"
                                                                    style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                                                    @click="llamadaEditar = null">
                                                                    ❌ Cancelar
                                                                </v-btn>
                                                            </v-col>
                                                        </v-row>
                                                    </div>
                                                </div>
                                                <!-- Línea vertical entre items -->
                                                <div v-if="idx < historialGestion.length - 1"
                                                    class="timeline-connector">
                                                </div>
                                            </div>
                                        </div>
                                    </v-expansion-panel-text>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </v-card-actions>
                    </v-card>

                    <div class="timeline-container mb-2 pa-2"
                        v-if="!cargandoHistorial2 && historialActivo == 1 && tipoAgrupacion == 3"
                        style="overflow-y: auto; border: 2px solid #666; border-radius: 5px;"
                        v-for="gestion in historialGlobalLlamadas" :key="gestion.id">
                        <!-- Línea vertical y punto -->
                        <div class="timeline-marker" :class="timelineColor(gestion.interes)">
                            <v-icon :color="timelineIconColor(gestion.interes)" size="22">
                                {{ timelineIcon(gestion.interes) }}
                            </v-icon>
                        </div>
                        <div class="timeline-content">
                            <p class="mt-2"><strong>Nombre Campaña: </strong>{{
                                gestion.nombre_campania }}</p>
                            <p class="mt-2"><strong># de Campaña: </strong>{{ gestion.idcampenv
                            }}</p>
                            <div class="d-flex align-center justify-space-between">
                                <span class="timeline-date">{{ formatDate(gestion.fecha)
                                }}</span>
                                <span class="timeline-type">
                                    <v-icon size="18" :color="timelineIconColor(gestion.interes)">
                                        {{ timelineIcon(gestion.interes) }}
                                    </v-icon>
                                    {{ interesToText(gestion.interes) }}
                                </span>
                                <span v-if="gestion.Editado == 'Si'" class="ml-2"
                                    style="font-size: 10px; color: red; font-weight: bold;">
                                    🖋️ Editado
                                </span>
                                <v-btn v-if="gestion.Editado == 'Si'" icon variant="text" color="primary" class="ml-2"
                                    title="Ver historial de ediciones" @click="abrirHistorialEdiciones(gestion)">
                                    <v-icon style="font-size: 16px;">mdi-history</v-icon>
                                </v-btn>
                            </div>
                            <div class="timeline-text mt-2">
                                <p style="margin-top: 0;">
                                    <strong>Prospecto:</strong> {{ gestion.razon_social }}
                                </p>
                                <p style="margin-top: 0;">"<strong>Gestión:</strong> {{
                                    gestion.respuesta }}"</p>
                                <v-btn class="mb-2 mr-2 mt-n4" variant="text" color="primary"
                                    style="font-size: 12px; float: right;" @click="llamadaEditar = gestion.id">
                                    ✍️ Editar
                                </v-btn>
                                <v-textarea v-if="gestion.id === llamadaEditar" v-model="texto_editado"
                                    label="Editar observación" outlined clearable class="mt-4" density="compact"
                                    variant="outlined" style="min-width: 120px; max-width: 90%;">
                                </v-textarea>
                                <v-row v-if="gestion.id === llamadaEditar" class="align-center mt-n1"
                                    style="margin-top: 8px;">
                                    <v-col cols="6" class="pa-0 pr-1" style="min-width:0;">
                                        <v-btn block variant="tonal" color="primary" class="ml-4 mb-6"
                                            style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                            @click="guardarEdicionHistorial(gestion)">
                                            💾 Guardar
                                        </v-btn>
                                    </v-col>
                                    <v-col cols="6" class="pa-0 pl-1" style="min-width:0;">
                                        <v-btn block variant="tonal" color="error" class="mb-6"
                                            style="font-size: 12px; white-space: normal; word-break: break-word; min-width: 0;"
                                            @click="llamadaEditar = null">
                                            ❌ Cancelar
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </div>
                        </div>
                    </div>

                    <v-card color="#F0F8FF" v-for="campaña in historialLead.data" :key="campaña.id"
                        v-if="!cargandoHistorial2 && historialActivo == 2 && tipoAgrupacion == 1" class="mb-4">
                        <v-card-title class="text-h6" style="color: #0A1C3A; font-weight: bold;">
                            <v-icon left size="20" color="#0A1C3A" class="mr-2">mdi-bell-circle</v-icon>
                            Campaña: {{ campaña.nombre_campania }}
                        </v-card-title>

                        <v-card-text style="color: #0A1C3A; font-size: 14px;">
                            Total Llamadas: <strong>{{ campaña.detalles ? campaña.detalles.length : 0 }}</strong> |
                            Llamadas Efectivas con Lead: <strong>{{ campaña.llamadas_con_lead }}</strong> |
                            Llamadas Efectivas sin Lead: <strong>{{ campaña.llamadas_sin_lead }}</strong> |
                            Llamadas No Efectivas: <strong>{{ campaña.llamadas_no_efectivas }}</strong>
                        </v-card-text>

                        <v-card-actions class="mt-n4 mb-2">
                            <v-expansion-panels bg-color="#DBE9FA" class="btn-grow-card-items">
                                <v-expansion-panel>
                                    <v-expansion-panel-title>
                                        Ver Detalles del Proceso Lead
                                    </v-expansion-panel-title>
                                    <v-expansion-panel-text>
                                        <div class="timeline-container" v-if="historialActivo == 2"
                                            style="height: 500px; overflow-y: auto;">
                                            <div v-for="(gestion, idx) in campaña.detalles" :key="gestion.id"
                                                class="timeline-item"
                                                style="background: #f8fbff; border: 1.5px solid #e0e7ef; border-radius: 16px; box-shadow: 0 2px 8px 0 #006ca11a; margin-bottom: 24px;">
                                                <!-- Línea vertical y punto -->
                                                <div class="timeline-marker"
                                                    :class="timelineColorLead2(gestion.idactividad)">
                                                    <v-icon :color="timelineColorLead(gestion.idactividad)" size="22">
                                                        {{ timelineIconLead(gestion.idactividad) }}
                                                    </v-icon>
                                                </div>
                                                <div class="timeline-content">
                                                    <div class="d-flex align-center justify-space-between mb-1">
                                                        <span class="timeline-date"
                                                            style="font-size: 1rem; font-weight: bold; color: #1565c0;">
                                                            <v-icon size="18" color="#1565c0"
                                                                class="mr-1">mdi-calendar-month</v-icon>
                                                            {{ gestion.fecha_act }}
                                                        </span>
                                                        <span class="ml-2"
                                                            style="font-size: 1rem; color: #1565c0; font-weight: bold;">
                                                            🏢 {{ gestion.razon_social }}
                                                        </span>
                                                        <span class="timeline-type" style="font-size: 0.95rem;">
                                                            <v-chip size="small"
                                                                :color="timelineColorLead(gestion.idactividad)"
                                                                text-color="white" class="mr-2">
                                                                <v-icon size="16" class="mr-1">{{
                                                                    timelineIconLead(gestion.idactividad)
                                                                }}</v-icon>
                                                                {{ actividadToText(gestion.idactividad) }}
                                                            </v-chip>
                                                        </span>
                                                    </div>
                                                    <v-divider class="my-2" />
                                                    <div class="d-flex flex-row flex-wrap align-center mb-2"
                                                        style="gap: 18px;">
                                                        <div style="flex: 1; min-width: 180px;">
                                                            <span
                                                                style="font-size: 0.98rem; color: #222; font-weight: 500;">
                                                                <v-icon size="16" color="#1976d2"
                                                                    class="mr-1">mdi-comment-text</v-icon>
                                                                {{ gestion.idactividad == 0 ? 'Nuevo Proceso' :
                                                                    gestion.observact }}
                                                            </span>
                                                        </div>
                                                        <!-- Estado badge mejorado -->
                                                        <v-chip size="small"
                                                            :color="timeLineColorEstado(gestion.estado)" class="ml-1"
                                                            style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1">
                                                                {{ estadoToText(gestion.estado) === 'Nuevo' ?
                                                                    'mdi-check-circle'
                                                                    :
                                                                    (estadoToText(gestion.estado) === 'En Proceso' ?
                                                                        'mdi-clock-outline' :
                                                                        'mdi-help-circle') }}
                                                            </v-icon>
                                                            {{ estadoToText(gestion.estado) }}
                                                        </v-chip>
                                                        <v-chip size="small" color="#00897b" text-color="white"
                                                            class="ml-1" style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1">mdi-briefcase</v-icon>
                                                            {{ servicioToText(gestion.idservicio) }}
                                                        </v-chip>
                                                    </div>
                                                    <div class="d-flex flex-row flex-wrap align-center mb-2"
                                                        style="gap: 18px;">
                                                        <v-chip size="small" color="red" class="ml-1"
                                                            style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1"
                                                                color="black">mdi-account</v-icon>
                                                            {{ gestion.nombre_comercial }}
                                                        </v-chip>
                                                        <v-chip size="small" color="#8e24aa" text-color="white"
                                                            class="ml-1" style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1">mdi-package-variant</v-icon>
                                                            {{ gestion.nombre_producto }}
                                                        </v-chip>
                                                    </div>
                                                </div>
                                                <!-- Línea vertical entre items -->
                                                <div v-if="idx < historialLead.length - 1" class="timeline-connector">
                                                </div>
                                            </div>
                                        </div>
                                    </v-expansion-panel-text>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </v-card-actions>
                    </v-card>

                    <v-card color="#F0F8FF" v-for="campaña in historialLead.data" :key="campaña.id"
                        v-if="!cargandoHistorial2 && historialActivo == 2 && tipoAgrupacion == 2" class="mb-4">
                        <v-card-title class="text-h6" style="color: #0A1C3A; font-weight: bold;">
                            <v-icon left size="20" color="#0A1C3A" class="mr-2">mdi-bell-circle</v-icon>
                            Prospecto: {{ campaña.razon_social }}
                        </v-card-title>

                        <v-card-text style="color: #0A1C3A; font-size: 14px;">
                            Total Llamadas: <strong>{{ campaña.detalles ? campaña.detalles.length : 0 }}</strong> |
                            Llamadas Efectivas con Lead: <strong>{{ campaña.llamadas_con_lead }}</strong> |
                            Llamadas Efectivas sin Lead: <strong>{{ campaña.llamadas_sin_lead }}</strong> |
                            Llamadas No Efectivas: <strong>{{ campaña.llamadas_no_efectivas }}</strong>
                        </v-card-text>

                        <v-card-actions class="mt-n4 mb-2">
                            <v-expansion-panels bg-color="#DBE9FA" class="btn-grow-card-items">
                                <v-expansion-panel :disabled="!campaña.detalles || campaña.detalles.length === 0">
                                    <v-expansion-panel-title>
                                        Ver Detalles del Proceso Lead <span class="ml-2" style="font-size: 0.8rem; color: red;" v-if="!campaña.detalles">  (Sin Llamadas Con Lead)</span>
                                    </v-expansion-panel-title>
                                    <v-expansion-panel-text>
                                        <div class="timeline-container" v-if="historialActivo == 2"
                                            style="height: 500px; overflow-y: auto;">
                                            <div v-for="(gestion, idx) in campaña.detalles" :key="gestion.id"
                                                class="timeline-item"
                                                style="background: #f8fbff; border: 1.5px solid #e0e7ef; border-radius: 16px; box-shadow: 0 2px 8px 0 #006ca11a; margin-bottom: 24px;">
                                                <!-- Línea vertical y punto -->
                                                <div class="timeline-marker"
                                                    :class="timelineColorLead2(gestion.idactividad)">
                                                    <v-icon :color="timelineColorLead(gestion.idactividad)" size="22">
                                                        {{ timelineIconLead(gestion.idactividad) }}
                                                    </v-icon>
                                                </div>
                                                <div class="timeline-content">
                                                    <div class="d-flex align-center justify-space-between mb-1">
                                                        <span class="timeline-date"
                                                            style="font-size: 1rem; font-weight: bold; color: #1565c0;">
                                                            <v-icon size="18" color="#1565c0"
                                                                class="mr-1">mdi-calendar-month</v-icon>
                                                            {{ gestion.fecha_act }}
                                                        </span>
                                                        <span class="ml-2"
                                                            style="font-size: 1rem; color: #1565c0; font-weight: bold;">
                                                            🏢 {{ gestion.razon_social }}
                                                        </span>
                                                        <span class="timeline-type" style="font-size: 0.95rem;">
                                                            <v-chip size="small"
                                                                :color="timelineColorLead(gestion.idactividad)"
                                                                text-color="white" class="mr-2">
                                                                <v-icon size="16" class="mr-1">{{
                                                                    timelineIconLead(gestion.idactividad)
                                                                }}</v-icon>
                                                                {{ actividadToText(gestion.idactividad) }}
                                                            </v-chip>
                                                        </span>
                                                    </div>
                                                    <v-divider class="my-2" />
                                                    <div class="d-flex flex-row flex-wrap align-center mb-2"
                                                        style="gap: 18px;">
                                                        <div style="flex: 1; min-width: 180px;">
                                                            <span
                                                                style="font-size: 0.98rem; color: #222; font-weight: 500;">
                                                                <v-icon size="16" color="#1976d2"
                                                                    class="mr-1">mdi-comment-text</v-icon>
                                                                {{ gestion.idactividad == 0 ? 'Nuevo Proceso' :
                                                                    gestion.observact }}
                                                            </span>
                                                        </div>
                                                        <!-- Estado badge mejorado -->
                                                        <v-chip size="small"
                                                            :color="timeLineColorEstado(gestion.estado)" class="ml-1"
                                                            style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1">
                                                                {{ estadoToText(gestion.estado) === 'Nuevo' ?
                                                                    'mdi-check-circle'
                                                                    :
                                                                    (estadoToText(gestion.estado) === 'En Proceso' ?
                                                                        'mdi-clock-outline' :
                                                                        'mdi-help-circle') }}
                                                            </v-icon>
                                                            {{ estadoToText(gestion.estado) }}
                                                        </v-chip>
                                                        <v-chip size="small" color="#00897b" text-color="white"
                                                            class="ml-1" style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1">mdi-briefcase</v-icon>
                                                            {{ servicioToText(gestion.idservicio) }}
                                                        </v-chip>
                                                    </div>
                                                    <div class="d-flex flex-row flex-wrap align-center mb-2"
                                                        style="gap: 18px;">
                                                        <v-chip size="small" color="red" class="ml-1"
                                                            style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1"
                                                                color="black">mdi-account</v-icon>
                                                            {{ gestion.nombre_comercial }}
                                                        </v-chip>
                                                        <v-chip size="small" color="#8e24aa" text-color="white"
                                                            class="ml-1" style="font-size: 0.92rem;">
                                                            <v-icon size="14" class="mr-1">mdi-package-variant</v-icon>
                                                            {{ gestion.nombre_producto }}
                                                        </v-chip>
                                                    </div>
                                                </div>
                                                <!-- Línea vertical entre items -->
                                                <div v-if="idx < historialLead.length - 1" class="timeline-connector">
                                                </div>
                                            </div>
                                        </div>
                                    </v-expansion-panel-text>
                                </v-expansion-panel>
                            </v-expansion-panels>
                        </v-card-actions>
                    </v-card>

                    <div class="timeline-container" v-if="!cargandoHistorial2 && historialActivo == 2 && tipoAgrupacion == 3"
                        style="overflow-y: auto;">
                        <div v-for="(gestion, idx) in historialLead" :key="gestion.id" class="timeline-item"
                            style="background: #f8fbff; border: 1.5px solid #e0e7ef; border-radius: 16px; box-shadow: 0 2px 8px 0 #006ca11a; margin-bottom: 24px;">
                            <!-- Línea vertical y punto -->
                            <div class="timeline-marker" :class="timelineColorLead2(gestion.idactividad)">
                                <v-icon :color="timelineColorLead(gestion.idactividad)" size="22">
                                    {{ timelineIconLead(gestion.idactividad) }}
                                </v-icon>
                            </div>
                            <div class="timeline-content">
                                <div class="d-flex align-center justify-space-between mb-1">
                                    <span class="timeline-date"
                                        style="font-size: 1rem; font-weight: bold; color: #1565c0;">
                                        <v-icon size="18" color="#1565c0" class="mr-1">mdi-calendar-month</v-icon>
                                        {{ gestion.fecha_act }}
                                    </span>
                                    <span class="ml-2" style="font-size: 1rem; color: #1565c0; font-weight: bold;">
                                        🏢 {{ gestion.razon_social }}
                                    </span>
                                    <span class="timeline-type" style="font-size: 0.95rem;">
                                        <v-chip size="small" :color="timelineColorLead(gestion.idactividad)"
                                            text-color="white" class="mr-2">
                                            <v-icon size="16" class="mr-1">{{
                                                timelineIconLead(gestion.idactividad)
                                            }}</v-icon>
                                            {{ actividadToText(gestion.idactividad) }}
                                        </v-chip>
                                    </span>
                                </div>
                                <v-divider class="my-2" />
                                <div class="d-flex flex-row flex-wrap align-center mb-2" style="gap: 18px;">
                                    <div style="flex: 1; min-width: 180px;">
                                        <span style="font-size: 0.98rem; color: #222; font-weight: 500;">
                                            <v-icon size="16" color="#1976d2" class="mr-1">mdi-comment-text</v-icon>
                                            {{ gestion.idactividad == 0 ? 'Nuevo Proceso' :
                                                gestion.observact }}
                                        </span>
                                    </div>
                                    <!-- Estado badge mejorado -->
                                    <v-chip size="small" :color="timeLineColorEstado(gestion.estado)" class="ml-1"
                                        style="font-size: 0.92rem;">
                                        <v-icon size="14" class="mr-1">
                                            {{ estadoToText(gestion.estado) === 'Nuevo' ?
                                                'mdi-check-circle'
                                                :
                                                (estadoToText(gestion.estado) === 'En Proceso' ?
                                                    'mdi-clock-outline' :
                                                    'mdi-help-circle') }}
                                        </v-icon>
                                        {{ estadoToText(gestion.estado) }}
                                    </v-chip>
                                    <v-chip size="small" color="#00897b" text-color="white" class="ml-1"
                                        style="font-size: 0.92rem;">
                                        <v-icon size="14" class="mr-1">mdi-briefcase</v-icon>
                                        {{ servicioToText(gestion.idservicio) }}
                                    </v-chip>
                                </div>
                                <div class="d-flex flex-row flex-wrap align-center mb-2" style="gap: 18px;">
                                    <v-chip size="small" color="red" class="ml-1" style="font-size: 0.92rem;">
                                        <v-icon size="14" class="mr-1" color="black">mdi-account</v-icon>
                                        {{ gestion.nombre_comercial }}
                                    </v-chip>
                                    <v-chip size="small" color="#8e24aa" text-color="white" class="ml-1"
                                        style="font-size: 0.92rem;">
                                        <v-icon size="14" class="mr-1">mdi-package-variant</v-icon>
                                        {{ gestion.nombre_producto }}
                                    </v-chip>
                                </div>
                            </div>
                            <!-- Línea vertical entre items -->
                            <div v-if="idx < historialLead.length - 1" class="timeline-connector">
                            </div>
                        </div>
                    </div>

                </div>
            </v-card>
        </v-dialog>
        <!-- Dialog historial de ediciones -->

        <!-- Dialog Cambio Clave -->
        <v-dialog v-model="dialogCambioClave" persistent max-width="400px">
            <v-card class="pa-4 rounded-xl">
                <v-card-title class="text-h6" style="color: #0A1C3A;">
                    Cambiar Clave
                </v-card-title>
                <v-card-text>
                    <v-text-field v-model="claveActual" label="Clave Actual"
                        :type="mostrarClaveActual ? 'text' : 'password'" variant="outlined" required clearable>
                        <template v-slot:append-inner>
                            <v-icon :icon="mostrarClaveActual ? 'mdi-eye' : 'mdi-eye-closed'"
                                @click="mostrarClaveActual = !mostrarClaveActual" />
                        </template>
                    </v-text-field>
                    <v-text-field v-model="nuevaClave" label="Nueva Clave"
                        :type="mostrarNuevaClave ? 'text' : 'password'" variant="outlined" required clearable>
                        <template v-slot:append-inner>
                            <v-icon :icon="mostrarNuevaClave ? 'mdi-eye' : 'mdi-eye-closed'"
                                @click="mostrarNuevaClave = !mostrarNuevaClave" />
                        </template>
                    </v-text-field>
                    <div class="text-caption mt-n4 mb-4" style="color: red;"
                        v-if="nuevaClave && !isValidPassword(nuevaClave)">
                        La
                        nueva
                        clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.
                    </div>
                    <v-text-field v-model="confirmarClave" label="Confirmar Nueva Clave"
                        :type="mostrarConfirmarClave ? 'text' : 'password'" variant="outlined" required clearable>
                        <template v-slot:append-inner>
                            <v-icon :icon="mostrarConfirmarClave ? 'mdi-eye' : 'mdi-eye-closed'"
                                @click="mostrarConfirmarClave = !mostrarConfirmarClave" />
                        </template>
                    </v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn variant="flat" color="#006CA1" @click="cambiarClave()">Guardar</v-btn>
                    <v-btn variant="flat" color="grey"
                        @click="dialogCambioClave = false; claveActual = null; nuevaClave = null; confirmarClave = null;">Cancelar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <!-- Dialog Cambio Clave -->

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

    </v-app>
</template>

<script>
import AppHeader from '../components/AppHeader.vue';
import axios from 'axios';
import CryptoJS from "crypto-js";

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
        imagenComercial: '', // URL de la imagen del comercial

        labelFormularioCampaña: 'Crear nueva campaña',

        dialogCambioClave: false,
        claveActual: null,
        nuevaClave: null,
        confirmarClave: null,
        mostrarClaveActual: false,
        mostrarNuevaClave: false,
        mostrarConfirmarClave: false,

        mensajeAlert: null,
        alerta: false,
        ifCargando: false,

        campañas: [],
        campañaSeleccionada: null,

        llamadasHoy: null,
        llamadasEfectivasLead: null,
        llamadasEfectivasSinLead: null,
        llamadasNoEfectivas: null,

        progresoCampañas: null,
        bufferCampañas: null,
        totalLlamadas: null,
        metaLlamadas: 20,

        contactoFiltro: null,
        contactos: [],

        sectorFiltro: null,
        sectores: [],
        ciudadFiltro: null,
        ciudadesFiltro: [],
        cargoFiltro: null,
        cargosFiltro: [],
        listaContactos: [],
        listaContactosTmp: [],
        empresaSeleccionada: null,

        contactoSeleccionadoNombre: null,
        contactoSeleccionadoCelular: null,
        contactoSeleccionadoEmail: null,
        contactoSeleccionadoEmpresa: null,
        contactoSeleccionadoCargo: null,

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

        observacionesLlamada: null,
        observacionesNoEfectivo: null,

        obsHistorial: [],
        llamadaEditar: null,
        texto_editado: null,

        dialogCrearCampaña: false,
        selectedNombreCampaña: null,
        selectedDetalleCampaña: null,
        selectedGuionCampaña: null,
        formOk: false,
        validandoActividad: false,
        formNuevaCampaña: null,

        dialogGuionCampaña: false,
        guionCampañaSeleccionada: null,
        roGuionCampaña: true,

        dialogInfoProsCon: false,
        fichaNit: null,
        fichaRazonSocial: null,
        fichaTipoId: null,
        fichaTipoEmp: null,
        fichaSector: null,
        fichaDireccion: null,
        fichaDepartamento: null,
        fichaCiudad: null,
        fichaWeb: null,
        fichaCorreoEmpresa: null,
        fichaTel1: null,
        fichaTel2: null,
        fichaNombre: null,
        fichaApellido: null,
        fichaCategoria: null,
        fichaCargo: null,
        fichaCorreoContacto: null,
        fichaExtension: null,
        fichaCelular: null,

        formularioProspecto: false,
        nombre: null,
        apellido: null,
        categoria: null,
        categorias: [],
        cargo: null,
        cargos: [],
        correoContacto: null,
        celular: '57',
        extension: '57',
        selectedServicioProspecto: null,
        empresa: null,
        alerta: false,
        mensajeAlerta: '',
        dsGuardar: false,
        nit: null,
        razonSocial: null,
        tipoId: null,
        tipoIdentificacion: [],
        tipoEmp: null,
        tipoEmpresa: [],
        sector: null,
        sectorEmpresa: [],
        direccion: null,
        departamento: null,
        departamentos: [],
        ciudad: null,
        ciudades: [],
        web: null,
        correoEmpresa: null,
        tel1: '57',
        tel2: null,
        mensajeAlertaRazonSocial: '',
        alertaNit: false,
        mensajeAlertaNit: '',
        alertaRazonSocial: false,
        listaEmpresas: [],
        listaEmpresas2: [],
        maxlength2: [v => !v || String(v).length < 13 || "Error. Máximo 10 dígitos"],
        mensajeAlertaCelular: null,
        alertaCelular: false,
        selectServiciosActividad: [],
        selectEstadosActividad: [],

        historialGestion: [],
        cargandoHistorial: false,
        cargandoHistorial2: false,
        informeLlamadas: [],

        dialogListaLlamadas: false,
        arrayLlamadas: [],
        headersLlamadas: [
            { title: 'Nombre de la campaña', key: 'nombre_campania', sortable: true },
            { title: 'Nombre / Razón Social', key: 'nombre', sortable: true },
            { title: 'Gestión realizada', key: 'respuesta', sortable: true },
            { title: 'Interés de la Llamada', key: 'interes_texto', sortable: true },
            { title: 'Motivo', key: 'motivo', sortable: true },
            { title: 'Nombre Comercial', key: 'nombre_comercial', sortable: true },
            { title: 'Producto', key: 'nombre_producto', sortable: true },
            { title: 'Estado Proceso', key: 'estado_proceso', sortable: true },
            { title: 'Fecha Registro Prospecto', key: 'fecha_registro_prospecto', sortable: true },
            { title: 'Fecha Primer Contacto', key: 'fecha_primer_contacto', sortable: true },
            { title: 'Fecha Último Contacto', key: 'fecha', sortable: true },
            { title: 'Fecha de Asignación', key: 'fecha_registro', sortable: true },
            { title: 'Fecha de reprogramación', key: 'fecha_reprogramacion', sortable: false },
        ],
        searchLlamadas: '',
        _searchTimer: null,
        filtroLlamadasSeleccionado: null,
        filtrosLlamadas: [
            { nombre: 'Todas', id: 4 },
            { nombre: 'Llamadas Registradas Hoy', id: 0 },
            { nombre: 'Llamadas Efectivas con Lead', id: 1 },
            { nombre: 'Llamadas Efectivas sin Lead', id: 2 },
            { nombre: 'Llamadas No Efectivas', id: 3 },
        ],
        filtroInicialSeleccionado: null,

        dialogHistorialEdiciones: false,
        historialEdiciones: [],
        buscadorHistorialGeneral: null,
        busquedaFechaHistorialInicio: null,
        busquedaFechaHistorialFin: null,
        menuActivo: "",

        dialogHistorialGlobal: false,
        historialActivo: 1, // 1 = llamadas, 2 = proceso lead
        tipoAgrupacion: 1, // 1 = por campaña, 2 = por empresa, 3 = sin agrupar
        historialLead: [],
        historialGlobalLlamadas: [],

        estados_comerciales: [
            {
                id: 1,
                nombre: 'Llamada Realizada',
                color: '#1565C0',
                icon: 'mdi-phone',
                items: []
            },
            {
                id: 2,
                nombre: 'Correo Enviado',
                color: '#2095c9',
                icon: 'mdi-gmail',
                items: []
            },
            {
                id: 3,
                nombre: 'Visita Presencial',
                color: 'orange-darken-2',
                icon: 'mdi-calendar-cursor-outline',
                items: []
            },
            {
                id: 4,
                nombre: 'Visita Virtual',
                color: 'teal-darken-1',
                icon: 'mdi-monitor-account',
                items: []
            },
            {
                id: 5,
                nombre: 'Activación de Demo',
                color: '#8E24AA',
                icon: 'mdi-laptop',
                items: []
            },
            {
                id: 6,
                nombre: 'Cotización',
                color: 'brown-darken-3',
                icon: 'mdi-point-of-sale',
                items: []
            }
        ],
    }),

    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.comercialId = localStorage.getItem('idUsuario');
        this.idCargo = localStorage.getItem('idCargo');
        this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');
        this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?${Date.now()}`;

        this.llamadoMotivos();
        this.llamadoEmpresas();
        this.llamadoCampañas();
        this.llamadoComerciales();
        this.llamadoProductos();
        this.llamadoSubproductos(0);
        this.campañasEnviadas();
        this.cargarServiciosActividad();
        this.cargarEstadosActividad();
    },

    watch: {
        tipoId(newVal) {
            if (!newVal) return;

            if (newVal.nombre === 'NIT') {
                this.tipoEmp = this.tipoEmpresa.find(item => item.nombre === 'Jurídica');
            } else {
                this.tipoEmp = this.tipoEmpresa.find(item => item.nombre === 'Natural');
            }
        },

        razonSocial(newRazonSocial) {
            this.validarRazonSocial(newRazonSocial);
        },

        nit(newNit) {
            this.validarNit(newNit);
        },

        departamento(newValue) {
            this.llamadoCiudades(newValue ? newValue.id : 0);
        },

        fichaDepartamento(newValue) {
            this.llamadoCiudades(newValue ? newValue.id : 0);
        },

        fichaCategoria(newValue) {
            if (newValue) {
                this.llamadoCargos(newValue.id);
            }
        },

        categoria(newValue) {
            if (newValue) {
                this.llamadoCargos(newValue.id);
            }
        },
    },

    computed: {
        filteredHistorialEdiciones() {
            // Filtros de texto y fechas para historial de ediciones
            let result = this.historialEdiciones;

            // Filtro por texto (usuario, observaciones editadas u originales)
            if (this.buscadorHistorialGeneral && this.buscadorHistorialGeneral.trim() !== '') {
                const search = this.buscadorHistorialGeneral.trim().toLowerCase();
                result = result.filter(item => {
                    const nombreUsu = (item.nombre_usu || '').toLowerCase();
                    const textoEditado = (item.texto_editado || '').toLowerCase();
                    const textoOriginal = (item.texto_original || '').toLowerCase();
                    return nombreUsu.includes(search) || textoEditado.includes(search) || textoOriginal.includes(search);
                });
            }

            // Filtro solo por fecha de edición
            if (this.busquedaFechaHistorialInicio || this.busquedaFechaHistorialFin) {
                // Ajustar fechas para comparar solo por día y que el rango sea inclusivo
                const start = this.busquedaFechaHistorialInicio
                    ? new Date(this.busquedaFechaHistorialInicio + 'T00:00:00')
                    : null;
                const end = this.busquedaFechaHistorialFin
                    ? new Date(this.busquedaFechaHistorialFin + 'T23:59:59.999')
                    : null;
                result = result.filter(item => {
                    const fechaEdicion = item.fecha_edicion ? new Date(item.fecha_edicion) : null;
                    if (!fechaEdicion) return false;
                    if (start && end) {
                        return fechaEdicion >= start && fechaEdicion <= end;
                    } else if (start) {
                        return fechaEdicion >= start;
                    } else if (end) {
                        return fechaEdicion <= end;
                    }
                    return true;
                });
            }
            return result;
        }
    },

    methods: {

        timelineColor(interes) {
            if (interes === 0) return 'timeline-green';
            if (interes === 1) return 'timeline-blue';
            if (interes === 2) return 'timeline-red';
            return 'timeline-neutral';
        },
        timelineIcon(interes) {
            if (interes === 0) return 'mdi-check-circle';
            if (interes === 1) return 'mdi-phone';
            if (interes === 2) return 'mdi-close-circle';
            return 'mdi-help-circle';
        },
        timelineIconColor(interes) {
            if (interes === 0) return 'green';
            if (interes === 1) return 'blue';
            if (interes === 2) return 'red';
            return 'grey';
        },

        timelineIconLead(idactividad) {
            const estado = this.estados_comerciales.find(e => e.id === idactividad);
            return estado ? estado.icon : 'mdi-help-circle';
        },
        timelineColorLead(idactividad) {
            const estado = this.estados_comerciales.find(e => e.id === idactividad);
            return estado ? estado.color : 'grey';
        },
        timelineColorLead2(idactividad) {
            const estado = this.estados_comerciales.find(e => e.id === idactividad);
            return estado ? 'timeline-' + estado.color.replace('#', '') : 'timeline-neutral';
        },
        timeLineColorEstado(estado) {
            if (estado === 1) return 'blue';
            if (estado === 2) return 'purple';
            if (estado === 3) return 'orange';
            if (estado === 4) return 'green';
            if (estado === 5) return 'red';
            return 'grey';
        },

        toneClass(item) {
            // item.interes: 0 = verde pastel, 1 = azul pastel, 2 = rojo pastel
            if (item.interes == 0) return 'tone--green-pastel'
            if (item.interes == 1) return 'tone--blue-pastel'
            if (item.interes == 2) return 'tone--red-pastel'
            return ''
        },

        onSearchInput(val) {
            clearTimeout(this._searchTimer)
            this._searchTimer = setTimeout(() => {
                this.searchLlamadas = val
            }, 200)
        },

        formatDate(dateString) {
            const date = new Date(dateString);
            const day = String(date.getUTCDate()).padStart(2, '0');
            const month = String(date.getUTCMonth() + 1).padStart(2, '0');
            const year = date.getUTCFullYear();
            const hours = String(date.getUTCHours()).padStart(2, '0');
            const minutes = String(date.getUTCMinutes()).padStart(2, '0');
            return `${day}/${month}/${year} ${hours}:${minutes}`;
        },

        minDateTime() {
            /*// Obtenemos la fecha y hora actual
            const today = new Date();
            // Formateamos la fecha en "YYYY-MM-DDTHH:mm"
            const formattedDateTime = today.toISOString().slice(0, 16);*/
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

        anteriorEmpresa() {
            if (!this.listaContactos || this.listaContactos.length === 0) return;
            let idx = this.listaContactos.findIndex(e => e.id === (this.empresaSeleccionada && this.empresaSeleccionada.id));
            if (idx === -1) idx = 0;
            let nuevoIdx = idx === 0 ? this.listaContactos.length - 1 : idx - 1;
            this.empresaSeleccionada = this.listaContactos[nuevoIdx];
            this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
            this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
            this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
            this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
            this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
            this.$forceUpdate(); // Forzar actualización para getCardStyle

            this.$nextTick(() => {
                // Scroll automático
                const cardsContainer = document.querySelectorAll('div[style*="max-height: 400px"]')[0];
                const cards = cardsContainer ? cardsContainer.querySelectorAll('.v-card') : [];
                let cardIdx = nuevoIdx;
                if (cards && cards[cardIdx]) {
                    const card = cards[cardIdx];
                    // Si es la última, scroll al final
                    if (nuevoIdx === this.listaContactos.length - 1) {
                        cardsContainer.scrollTop = cardsContainer.scrollHeight;
                    } else if (nuevoIdx === 0) {
                        // Si es la primera, scroll al inicio
                        cardsContainer.scrollTop = 0;
                    } else {
                        // Scroll para que la tarjeta esté visible
                        const cardTop = card.offsetTop;
                        const cardBottom = cardTop + card.offsetHeight;
                        const containerTop = cardsContainer.scrollTop;
                        const containerBottom = containerTop + cardsContainer.clientHeight;
                        if (cardTop < containerTop) {
                            cardsContainer.scrollTop = cardTop;
                        } else if (cardBottom > containerBottom) {
                            cardsContainer.scrollTop = cardBottom - cardsContainer.clientHeight;
                        }
                    }
                }
            });

            setTimeout(() => {
                this.historialGestion = [];
                this.cargandoHistorial = true;
                this.llamadoHistorialGestion();
            }, 500);
        },

        siguienteEmpresa() {
            if (!this.listaContactos || this.listaContactos.length === 0) return;
            let idx = this.listaContactos.findIndex(e => e.id === (this.empresaSeleccionada && this.empresaSeleccionada.id));
            if (idx === -1) idx = 0;
            let nuevoIdx = idx === this.listaContactos.length - 1 ? 0 : idx + 1;
            this.empresaSeleccionada = this.listaContactos[nuevoIdx];
            this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
            this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
            this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
            this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
            this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
            this.$forceUpdate(); // Forzar actualización para getCardStyle

            this.$nextTick(() => {
                // Scroll automático
                const cardsContainer = document.querySelectorAll('div[style*="max-height: 400px"]')[0];
                const cards = cardsContainer ? cardsContainer.querySelectorAll('.v-card') : [];
                let cardIdx = nuevoIdx;
                if (cards && cards[cardIdx]) {
                    const card = cards[cardIdx];
                    // Si es la primera, scroll al inicio
                    if (nuevoIdx === 0) {
                        cardsContainer.scrollTop = 0;
                    } else if (nuevoIdx === this.listaContactos.length - 1) {
                        // Si es la última, scroll al final
                        cardsContainer.scrollTop = cardsContainer.scrollHeight;
                    } else {
                        // Scroll para que la tarjeta esté visible
                        const cardTop = card.offsetTop;
                        const cardBottom = cardTop + card.offsetHeight;
                        const containerTop = cardsContainer.scrollTop;
                        const containerBottom = containerTop + cardsContainer.clientHeight;
                        if (cardBottom > containerBottom) {
                            cardsContainer.scrollTop = cardBottom - cardsContainer.clientHeight;
                        } else if (cardTop < containerTop) {
                            cardsContainer.scrollTop = cardTop;
                        }
                    }
                }
            });

            setTimeout(() => {
                this.historialGestion = [];
                this.cargandoHistorial = true;
                this.llamadoHistorialGestion();
            }, 500);
        },

        cargarEmpresa(empresa) {
            this.empresaSeleccionada = empresa;
            this.contactoSeleccionadoNombre = empresa.nombre != 'No disponible' ? empresa.nombre : empresa.empresa;
            this.contactoSeleccionadoCelular = empresa.celular ? empresa.celular : empresa.telefono;
            this.contactoSeleccionadoEmail = empresa.email;
            this.contactoSeleccionadoEmpresa = empresa.empresa;
            this.contactoSeleccionadoCargo = empresa.cargo;
            this.$forceUpdate(); // Forzar actualización para getCardStyle

            setTimeout(() => {
                this.historialGestion = [];
                this.cargandoHistorial = true;
                this.llamadoHistorialGestion();
            }, 500);
        },

        abrirListaLlamadas(filtro) {
            this.dialogListaLlamadas = true;

            this.filtroLlamadasSeleccionado = this.filtrosLlamadas.find(item => item.id === filtro) || null;

            axios.post(this.baseURL + 'api/llamadasRealizadas', {
                'id_usuario': this.comercialId,
                'filtro': filtro
            })
                .then(response => {
                    this.arrayLlamadas = response.data.data.map(item => ({
                        ...item,
                        interes_texto: this.interesToText(item.interes)
                    }));
                })
                .catch(error => {
                    console.log(error);
                    this.mensajeAlert = 'Error al cargar las llamadas realizadas';
                    this.alerta = true;
                    this.ifCargando = false;
                });
        },

        interesToText(interes) {
            if (interes === 0) return 'Llamada Efectiva con Lead';
            if (interes === 1) return 'Llamada Efectiva sin Lead';
            if (interes === 2) return 'Llamada No Efectiva';
            return '';
        },

        actividadToText(estado) {
            estado = parseInt(estado);
            const estadoObj = this.estados_comerciales.find(e => e.id === estado);
            return estadoObj ? estadoObj.nombre : 'Nuevo Proceso';
        },

        servicioToText(idservicio) {
            idservicio = parseInt(idservicio);
            const servicioObj = this.selectServiciosActividad.find(e => e.id === idservicio);
            return servicioObj ? servicioObj.nombre : '';
        },

        estadoToText(estado) {
            estado = parseInt(estado);
            const estadoObj = this.selectEstadosActividad.find(e => e.id === estado);
            return estadoObj ? estadoObj.nombre : '';
        },

        guardarGestionLlamada() {
            if (this.empresaSeleccionada.activo == 0) {
                this.mensajeAlert = 'La empresa seleccionada no se encuentra autorizada. Por favor, selecciona otra empresa.';
                this.alerta = true;
                return;
            }

            if (!this.campañaSeleccionada) {
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
                        'id_campania': this.campañaSeleccionada.id,
                        'id_contacto': this.empresaSeleccionada ? this.empresaSeleccionada.idContacto : 0,
                        'id_usuario': this.comercialId,
                        'efectividad': this.estadoGestionLlamada,
                        'crear_lead': this.ifLeadSi ? 1 : 0,
                        'motivo_no_lead': this.motivoNoLead ? this.motivoNoLead.id : 0,
                        'motivo_no_efectivo': this.motivoNoEfectivo ? this.motivoNoEfectivo.id : 0,
                        'observaciones_no_efectivo': this.observacionesNoEfectivo ? this.observacionesNoEfectivo : '',
                        'id_empresa': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
                        'fecha_reagenda': this.fechaReagenda ? this.fechaReagenda : '',
                        'estado': 3,
                        'id_campenv': 0
                    })
                        .then(response => {
                            this.mensajeAlert = 'Gestión guardada con éxito';
                            this.alerta = true;
                            this.ifCargando = false;
                            this.limpiarCamposGestion();
                            this.historialGestion = [];
                            this.cargandoHistorial = true;
                            this.campañasEnviadas();
                            this.llamadoHistorialGestion();
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
                        'id_campania': this.campañaSeleccionada.id,
                        'id_contacto': this.empresaSeleccionada ? this.empresaSeleccionada.idContacto : 0,
                        'id_usuario': this.comercialId,
                        'efectividad': this.estadoGestionLlamada,
                        'crear_lead': this.ifLeadSi ? 1 : 0,
                        'motivo_no_lead': this.motivoNoLead ? this.motivoNoLead.id : 0,
                        'motivo_no_efectivo': this.motivoNoEfectivo ? this.motivoNoEfectivo.id : 0,
                        'observaciones_no_efectivo': this.observacionesNoEfectivo ? this.observacionesNoEfectivo : '',
                        'id_empresa': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
                        'fecha_reagenda': this.fechaReagenda ? this.fechaReagenda : '',
                        'estado': 0,
                        'id_campenv': 0
                    })
                        .then(response => {
                            this.mensajeAlert = 'Gestión guardada con éxito';
                            this.alerta = true;
                            this.ifCargando = false;
                            this.limpiarCamposGestion();
                            this.historialGestion = [];
                            this.cargandoHistorial = true;
                            this.campañasEnviadas();
                            this.llamadoHistorialGestion();
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
                    'id_campania': this.campañaSeleccionada.id,
                    'id_contacto': this.empresaSeleccionada ? this.empresaSeleccionada.idContacto : 0,
                    'id_usuario': this.comercialId,
                    'efectividad': this.estadoGestionLlamada,
                    'crear_lead': this.ifLeadSi ? 1 : 0,
                    'motivo_no_lead': this.motivoNoLead ? this.motivoNoLead.id : 0,
                    'motivo_no_efectivo': this.motivoNoEfectivo ? this.motivoNoEfectivo.id : 0,
                    'observaciones_no_efectivo': this.observacionesNoEfectivo ? this.observacionesNoEfectivo : '',
                    'id_empresa': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
                    'fecha_reagenda': this.fechaReagenda ? this.fechaReagenda : '',
                    'estado': 0,
                    'id_campenv': 0
                })
                    .then(response => {
                        this.mensajeAlert = 'Gestión guardada con éxito';
                        this.alerta = true;
                        this.ifCargando = false;
                        this.limpiarCamposGestion();
                        this.historialGestion = [];
                        this.cargandoHistorial = true;
                        this.campañasEnviadas();
                        this.llamadoHistorialGestion();
                    })
                    .catch(error => {
                        console.log(error);
                        this.mensajeAlert = 'Error al guardar la gestión';
                        this.alerta = true;
                        this.ifCargando = false;
                    });
            }
        },

        abrirHistorialEdiciones(gestion) {
            axios.post(this.baseURL + 'api/historialEdiciones', {
                'id_historial': gestion.id
            })
                .then(response => {
                    this.historialEdiciones = response.data.data;
                    this.dialogHistorialEdiciones = true;
                })
                .catch(error => {
                    console.log(error);
                    this.mensajeAlert = 'Error al cargar el historial de ediciones';
                    this.alerta = true;
                    this.ifCargando = false;
                });
        },

        guardarEdicionHistorial(gestion) {
            this.ifCargando = true;

            axios.post(this.baseURL + 'api/editarGestionTelefonica', {
                'id_historial': gestion.id,
                'fecha_original': this.formatDate(gestion.fecha),
                'texto_original': gestion.respuesta,
                'texto_editado': this.texto_editado,
                'id_usu': this.comercialId,
                'id_tipo_log': 1
            })
                .then(response => {
                    this.mensajeAlert = 'Edición guardada con éxito';
                    this.alerta = true;
                    this.ifCargando = false;
                    this.historialGestion = [];
                    this.cargandoHistorial = true;
                    this.llamadoHistorialGestion();
                    this.llamadaEditar = null;
                    this.texto_editado = null;

                    axios.post(this.baseURL + 'api/historialGlobalLlamadas', {
                        'id_usuario': this.comercialId,
                    })
                        .then(response => {
                            const parsed = JSON.parse(response.data.data[0].json_resultado);

                            this.historialGlobalLlamadas = parsed;
                            this.cargandoHistorial2 = false;
                        })
                        .catch(error => {
                            console.log(error);
                        });
                })
                .catch(error => {
                    console.log(error);
                    this.mensajeAlert = 'Error al guardar la edición';
                    this.alerta = true;
                    this.ifCargando = false;
                });
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

        async guardarDatos() {

            var contacto = false;
            // if (!this.nombre || !this.apellido || !this.cargo || !this.correoContacto || !this.celular || !this.extension) {
            // Valida los campos del contacto que son obligatorios
            if (!this.razonSocial) {
                this.mensajeAlert = 'Por favor, digite la razón social de la empresa';
                this.alerta = true;
                return;
            }
            else if (!this.departamento) {
                this.mensajeAlert = 'Por favor, seleccione el departamento de la empresa';
                this.alerta = true;
                return;
            }
            else if (!this.ciudad) {
                this.mensajeAlert = 'Por favor, seleccione la ciudad de la empresa';
                this.alerta = true;
                return;
            } else if (!this.tel1 && !this.tel2) {
                this.mensajeAlert = 'Por favor, digite al menos un teléfono de la empresa';
                this.alerta = true;
                return;
            }

            if (this.web && !this.esUrlValida(this.web)) {
                this.mensajeAlert = 'Por favor, ingrese una URL válida.';
                this.alerta = true;
                return;
            }

            if (this.correoEmpresa && !this.esCorreoValido(this.correoEmpresa)) {
                this.mensajeAlert = 'Por favor, ingrese un correo válido.';
                this.alerta = true;
                return;
            }

            if (!this.selectedServicioProspecto) {
                this.mensajeAlert = 'Por favor, Selecciona un servicio para el contacto';
                this.alerta = true;
                return;
            }
            const nitDuplicado = await this.validarNit(this.nit);
            const razonDuplicada = await this.validarRazonSocial(this.razonSocial);

            if (nitDuplicado || razonDuplicada || this.dsGuardar) {
                this.mensajeAlert = this.mensajeAlertaNit || this.mensajeAlertaRazonSocial || 'Ya existe un prospecto con este NIT o razón social';
                this.alerta = true;
                this.ifCargando = false;
                return;
            }

            if (this.nombre && !this.apellido) {
                this.mensajeAlert = 'Por favor, digite el apellido del contacto';
                this.alerta = true;
                return;
            }
            else if (!this.nombre && this.apellido) {
                this.mensajeAlert = 'Por favor, digite el nombre del contacto';
                this.alerta = true;
                return;
            }
            else if (this.correoContacto && !this.esCorreoValido(this.correoContacto)) {
                this.mensajeAlert = 'Por favor, ingrese un correo válido.';
                this.alerta = true;
                return;
            } else if (!this.celular) {
                this.mensajeAlert = 'Por favor, digite el celular del contacto';
                this.alerta = true;
                return;
            }

            console.log('tipoId:', this.tipoId ? this.tipoId.id : 0);
            console.log("url:" + this.baseURL);

            this.mensajeAlert = 'Guardando prospecto...';
            this.alerta = true;
            this.ifCargando = true;


            console.log('Servicio: ', this.selectedServicioProspecto ? this.selectedServicioProspecto.id : 0);

            await axios.post(this.baseURL + 'api/newprospecto', {
                'nit': this.nit,
                'razon_social': this.razonSocial,
                'tipo_identif': this.tipoId ? this.tipoId.id : 0,
                'tipo_emp': this.tipoEmp ? this.tipoEmp.id : 0,
                'sector': this.sector ? this.sector.id : 0,
                'direccion': this.direccion ? this.direccion : '',
                'dpto': this.departamento ? this.departamento.id : 0,
                'ciudad': this.ciudad ? this.ciudad.id : 0,
                'web': this.web ? this.web : '',
                'correo': this.correoEmpresa ? this.correoEmpresa : '',
                'telefono1': this.tel1 ? this.tel1 : '',
                'telefono2': this.tel2 ? this.tel2 : '',
                'comercial': 0,
                'servicio': this.selectedServicioProspecto ? this.selectedServicioProspecto.id : 0,
                'mercadeo': this.comercialId,
            })
                .then(response => {
                    this.idEmpresa = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });


            console.log('ID Empresa:', this.idEmpresa);

            if (this.nombre && this.apellido) {
                await axios.post(this.baseURL + 'api/newprospectocontacto', {
                    'nombre': this.nombre ? this.nombre : '',
                    'apellido': this.apellido ? this.apellido : '',
                    'cargo': this.cargo ? this.cargo.id : 0,
                    'correo': this.correoContacto ? this.correoContacto : '',
                    'celular': this.celular ? this.celular : '',
                    'extension': this.extension ? this.extension : '',
                    'idemp': this.idEmpresa[0].id,
                })
                    .then(response => {
                        this.cerrarFormularioProspecto();
                        contacto = true;
                        setTimeout(() => {
                            this.mensajeAlert = 'Prospecto creado exitosamente';
                            this.alerta = true;
                            this.ifCargando = false;
                            this.llamadoEmpresas();
                        }, 600);
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
            if (!contacto) {
                this.cerrarFormularioProspecto();

                setTimeout(() => {
                    this.mensajeAlert = 'Prospecto creado exitosamente';
                    this.alerta = true;
                    this.ifCargando = false;
                    this.llamadoEmpresas();
                }, 600);
            }
        },

        guardarFormularioCampaña() {
            this.validandoActividad = true;

            if (!this.selectedNombreCampaña?.trim()) {
                this.mensajeAlert = 'Por favor, Digite el nombre de la Campaña.';
                this.alerta = true;
                this.validandoActividad = false;
                return;
            }

            if (!this.selectedDetalleCampaña?.trim()) {
                this.mensajeAlert = 'Por favor, Digite el detalle de la Campaña.';
                this.alerta = true;
                this.validandoActividad = false;
                return;
            }

            if (!this.selectedGuionCampaña?.trim()) {
                this.mensajeAlert = 'Por favor, Digite el guion de la Campaña.';
                this.alerta = true;
                this.validandoActividad = false;
                return;
            }

            axios.post(this.baseURL + '/api/CrearCampania', {
                'nombre': this.selectedNombreCampaña,
                'detalle': this.selectedDetalleCampaña,
                'guion': this.selectedGuionCampaña,
                'idusu': localStorage.getItem('idUsuario'),
                'idCampania': 0, // 0 Para crear
                'tipo': 0, // 0 Para crear
                'url_media': '',
                'canal': 2, // 2 para Telemercadeo
                'activo': 1, // 1 por defecto
            })
                .then(response => {
                    this.mensajeAlert = 'Campaña Creada Exitosamente.';
                    this.alerta = true;
                    this.cerrarFormularioCampaña();
                    this.llamadoCampañas();
                    this.campañaSeleccionada = null;
                    console.log("Respuesta correcta", response.data);
                })
                .catch(error => {
                    console.error('Error al cargar historial de campaña:', error)
                })

        },

        editarFormularioCampaña() {

            this.validandoActividad = true;

            if (!this.selectedNombreCampaña?.trim()) {
                this.mensajeAlert = 'Por favor, Digite el nombre de la Campaña.';
                this.alerta = true;
                this.validandoActividad = false;
                return;
            }

            if (!this.selectedDetalleCampaña?.trim()) {
                this.mensajeAlert = 'Por favor, Digite el detalle de la Campaña.';
                this.alerta = true;
                this.validandoActividad = false;
                return;
            }

            if (!this.selectedGuionCampaña?.trim()) {
                this.mensajeAlert = 'Por favor, Digite el guion de la Campaña.';
                this.alerta = true;
                this.validandoActividad = false;
                return;
            }

            axios.post(this.baseURL + '/api/CrearCampania', {
                'nombre': this.selectedNombreCampaña,
                'detalle': this.selectedDetalleCampaña,
                'guion': this.selectedGuionCampaña,
                'idusu': localStorage.getItem('idUsuario'),
                'idCampania': this.campañaSeleccionada.id,
                'tipo': 1, // 1 Para Editar
                'canal': 2, // 1 Por defecto
                'activo': 1, // 1 por defecto
            })
                .then(response => {
                    this.mensajeAlert = 'Campaña Editada Exitosamente.';
                    this.alerta = true;
                    this.cerrarFormularioCampaña();
                    this.llamadoCampañas();
                    this.campañaSeleccionada = null;
                    console.log("Respuesta correcta", response.data);
                })
                .catch(error => {
                    console.error('Error al cargar historial de campaña:', error)
                })
        },

        guardarGuionCampaña(campaña) {

            if (!this.guionCampañaSeleccionada?.trim()) {
                this.mensajeAlert = 'Por favor, Digite el guion de la Campaña.';
                this.alerta = true;
                return;
            }

            this.dialogGuionCampaña = false;

            axios.post(this.baseURL + '/api/CrearCampania', {
                'nombre': campaña.nombre,
                'detalle': campaña.detalle,
                'guion': this.guionCampañaSeleccionada,
                'idusu': localStorage.getItem('idUsuario'),
                'idCampania': campaña.id,
                'tipo': 1, // 1 Para Editar
                'canal': 2, // 1 Por defecto
                'activo': 1, // 1 por defecto
            })
                .then(response => {

                    this.mensajeAlert = 'Guión de la Campaña Editado Exitosamente.';
                    this.alerta = true;
                    this.roGuionCampaña = true;
                    this.llamadoCampañas();
                    this.campañaSeleccionada = null;
                    console.log("Respuesta correcta", response.data);
                })
                .catch(error => {
                    console.error('Error al cargar historial de campaña:', error)
                })
        },

        irEditarCampanas(idCampana) {
            this.labelFormularioCampaña = 'Editar campaña';
            this.dialogCrearCampaña = true;

            axios.post(this.baseURL + 'api/infoCampania', {
                idCampania: idCampana
            })
                .then(response => {
                    console.log('DATOS DE:', response.data.data);
                    this.selectedNombreCampaña = response.data.data[0].nombre;
                    this.selectedDetalleCampaña = response.data.data[0].detalle;
                    this.selectedGuionCampaña = response.data.data[0].guion;
                    //this.selectedArchivoCampania = response.data.data;
                    //this.listaCampañas = response.data.data;

                }).catch(error => {
                    console.error('Error al cargar las campañas:', error);
                });
        },

        cargarGuionCampaña() {
            if (this.campañaSeleccionada) {
                this.dialogGuionCampaña = true;
                console.log(this.campañaSeleccionada);
                this.guionCampañaSeleccionada = this.campañaSeleccionada.guion;
            }
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


        async datosIniciales() {
            this.listaContactos = [];
            for (const empresa of this.listaEmpresas) {
                // Esperar cada llamado y guardar los datos temporalmente
                await this.llamadoCiudadesAsync(empresa.p_dpto);
                if (empresa.pc_categoria) {
                    await this.llamadoCargosAsync(empresa.pc_categoria);
                }
                await this.llamadoSectoresAsync();

                let ciudad = this.ciudades.find(c => c.id == empresa.p_ciudad) || { nombre: '' };
                let cargo = this.cargos.find(c => c.id == empresa.pc_cargo) || { nombre: '' };
                let sector = this.sectorEmpresa.find(s => s.id == empresa.p_sector) || { nombre: '' };

                this.listaContactos.push({
                    id: empresa.id,
                    nombre: empresa.pc_nombre ? empresa.pc_nombre + ' ' + empresa.pc_apellido : 'No disponible',
                    empresa: empresa.p_razon_social,
                    ciudad: ciudad.nombre,
                    celular: empresa.pc_celular,
                    cargo: cargo.nombre ? cargo.nombre : 'No disponible',
                    telefono: empresa.p_telefono1,
                    sector: sector.nombre,
                    email: empresa.pc_correo ? empresa.pc_correo : 'No disponible',
                    idContacto: empresa.pc_id ? empresa.pc_id : 0,
                    activo: empresa.p_activo
                });
            }
            // Seleccionar la empresa de la posición 0
            this.empresaSeleccionada = this.listaContactos[0];
            this.listaContactosTmp = this.listaContactos;
            this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
            this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
            this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
            this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
            this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
            this.llenarFiltros();
            this.historialGestion = [];
            this.cargandoHistorial = true;
            this.llamadoHistorialGestion();
        },

        // Métodos auxiliares async para esperar los axios
        llamadoCiudadesAsync(id) {
            return axios.post(this.baseURL + 'api/cargarci', { 'iddpto': id })
                .then(response => { this.ciudades = response.data.data; })
                .catch(error => { console.log(error); });
        },
        llamadoCargosAsync(id) {
            return axios.post(this.baseURL + 'api/cargarca', { 'idcat': id })
                .then(response => { this.cargo = null; this.cargos = response.data.data; })
                .catch(error => { console.log(error); });
        },
        llamadoSectoresAsync() {
            return axios.get(this.baseURL + 'api/cargarse')
                .then(response => { this.sectorEmpresa = response.data.data; })
                .catch(error => { console.log(error); });
        },

        llenarFiltros() {
            // Contactos: se deja igual
            this.contactos = [...new Set(this.listaContactos.map(c => ({ id: c.id, nombre: c.nombre + ' - ' + c.empresa + ' - ' + (c.celular ? c.celular : c.telefono) })))];

            // Sectores únicos por nombre
            const sectoresMap = new Map();
            this.listaContactos.forEach(c => {
                if (c.sector && !sectoresMap.has(c.sector)) {
                    sectoresMap.set(c.sector, { id: c.sector, nombre: c.sector });
                }
            });
            this.sectores = Array.from(sectoresMap.values());

            // Ciudades únicas por nombre
            const ciudadesMap = new Map();
            this.listaContactos.forEach(c => {
                if (c.ciudad && !ciudadesMap.has(c.ciudad)) {
                    ciudadesMap.set(c.ciudad, { id: c.ciudad, nombre: c.ciudad });
                }
            });
            this.ciudadesFiltro = Array.from(ciudadesMap.values());

            // Cargos únicos por nombre, omitiendo 'No disponible'
            const cargosMap = new Map();
            this.listaContactos.forEach(c => {
                if (c.cargo && !cargosMap.has(c.cargo)) {
                    cargosMap.set(c.cargo, { id: c.cargo, nombre: c.cargo });
                }
            });
            this.cargosFiltro = Array.from(cargosMap.values());
        },

        cargarContactoSeleccionado(empresa) {

            this.llamadoTipoIdentificacion();
            this.llamadoSectores();
            this.llamadoTipoEmpresa();
            this.llamadoDepartamentos();
            this.llamadoCategorias();

            setTimeout(() => {
                axios
                    .post(this.baseURL + "api/cargaproscon", {
                        idprosp: empresa.id,
                    })
                    .then((response) => {
                        console.log("Prospecto cargado:", response.data);
                        this.dialogInfoProsCon = true;

                        this.fichaNit = response.data.data[0].p_nit;
                        this.fichaRazonSocial = response.data.data[0].p_razon_social;
                        this.fichaTipoId = this.tipoIdentificacion.find(
                            (item) => item.id == response.data.data[0].p_tipo_identif
                        );
                        this.fichaSector = this.sectorEmpresa.find(
                            (item) => item.id == response.data.data[0].p_sector
                        );
                        this.fichaDireccion = response.data.data[0].p_direccion;
                        this.fichaDepartamento = this.departamentos.find(
                            (item) => item.id == response.data.data[0].p_dpto
                        );
                        setTimeout(() => {
                            this.fichaCiudad = this.ciudades.find(
                                (item) => item.id == response.data.data[0].p_ciudad
                            );
                        }, 1000);
                        this.fichaWeb = response.data.data[0].p_web;
                        this.fichaCorreoEmpresa = response.data.data[0].p_correo;
                        this.fichaTel1 = response.data.data[0].p_telefono1;
                        this.fichaTel2 = response.data.data[0].p_telefono2;

                        this.fichaNombre = response.data.data[0].pc_nombre;
                        this.fichaApellido = response.data.data[0].pc_apellido;
                        this.fichaCategoria = this.categorias.find(
                            (item) => item.id == response.data.data[0].pc_categoria
                        );
                        setTimeout(() => {
                            this.fichaCargo = this.cargos.find(
                                (item) => item.id == response.data.data[0].pc_cargo
                            );
                        }, 1000);
                        this.fichaCorreoContacto = response.data.data[0].pc_correo;
                        this.fichaCelular = response.data.data[0].pc_celular;
                        this.fichaExtension = response.data.data[0].pc_extension;
                    })
                    .catch((error) => {
                        console.error("Error al cargar prospecto:", error);
                    });
            }, 500);
        },

        filtrarContactos() {

            if (this.contactoFiltro) {
                this.listaContactos = this.listaContactos.filter(c => c.id == this.contactoFiltro.id);
                this.empresaSeleccionada = this.listaContactos[0];
                this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
                this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
                this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
                this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
                this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
                this.historialGestion = [];
                this.cargandoHistorial = true;
                this.llamadoHistorialGestion();
            } else if (this.sectorFiltro || this.ciudadFiltro || this.cargoFiltro) {
                this.listaContactos = this.listaContactosTmp;

                if (this.sectorFiltro) {
                    this.listaContactos = this.listaContactos.filter(c => c.sector == this.sectorFiltro.nombre);
                    this.empresaSeleccionada = this.listaContactos[0];
                    this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
                    this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
                    this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
                    this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
                    this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
                    this.historialGestion = [];
                    this.cargandoHistorial = true;
                    this.llamadoHistorialGestion();
                }
                if (this.ciudadFiltro) {
                    this.listaContactos = this.listaContactos.filter(c => c.ciudad == this.ciudadFiltro.nombre);
                    this.empresaSeleccionada = this.listaContactos[0];
                    this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
                    this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
                    this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
                    this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
                    this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
                    this.historialGestion = [];
                    this.cargandoHistorial = true;
                    this.llamadoHistorialGestion();
                }
                if (this.cargoFiltro) {
                    this.listaContactos = this.listaContactos.filter(c => c.cargo == this.cargoFiltro.nombre);
                    this.empresaSeleccionada = this.listaContactos[0];
                    this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
                    this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
                    this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
                    this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
                    this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
                    this.historialGestion = [];
                    this.cargandoHistorial = true;
                    this.llamadoHistorialGestion();
                }
            } else {
                this.listaContactos = this.listaContactosTmp;
                this.empresaSeleccionada = this.listaContactos[0];
                this.contactoSeleccionadoNombre = this.empresaSeleccionada.nombre != 'No disponible' ? this.empresaSeleccionada.nombre : this.empresaSeleccionada.empresa;
                this.contactoSeleccionadoCelular = this.empresaSeleccionada.celular ? this.empresaSeleccionada.celular : this.empresaSeleccionada.telefono;
                this.contactoSeleccionadoEmail = this.empresaSeleccionada.email;
                this.contactoSeleccionadoEmpresa = this.empresaSeleccionada.empresa;
                this.contactoSeleccionadoCargo = this.empresaSeleccionada.cargo;
                this.historialGestion = [];
                this.cargandoHistorial = true;
                this.llamadoHistorialGestion();
            }
        },

        abrirFormularioProspecto() {
            this.llamadoTipoIdentificacion();
            this.llamadoSectores();
            this.llamadoTipoEmpresa();
            this.llamadoDepartamentos();
            this.llamadoCategorias();
            this.cargarServiciosActividad();
            this.formularioProspecto = true;
        },

        historialGlobal() {
            this.dialogHistorialGlobal = true;
            this.historialActivo = 1;
            this.cargandoHistorial2 = true;

            this.cargarHistorialGlobalLlamadas(this.tipoAgrupacion);
        },

        cargarHistorialGlobalLlamadas(tipoAgrupar) {
            axios.post(this.baseURL + 'api/historialGlobalLlamadas', {
                'id_usuario': this.comercialId,
                'agrupar': tipoAgrupar
            })
                .then(response => {
                    if (tipoAgrupar != 3) {
                        const parsed = JSON.parse(response.data.data[0].json_resultado);

                        this.historialGlobalLlamadas = parsed;
                        this.cargandoHistorial2 = false;
                    } else {
                        this.historialGlobalLlamadas = response.data.data;
                        this.cargandoHistorial2 = false;
                    }
                })
                .catch(error => {
                    console.log(error);
                });
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

        llamadoCampañas() {

            axios.post(this.baseURL + 'api/cargarcamptel', {
                'idusu': localStorage.getItem('idUsuario'),
                'tipo': 2
            })
                .then(response => {
                    this.campañas = response.data.data;
                    this.campañaSeleccionada = this.campañas.length > 0 ? this.campañas[0] : null;
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
                    this.prospectos = response.data.data;
                    this.listaEmpresas = response.data.data;
                    this.listaEmpresas2 = response.data.data;

                    this.datosIniciales();
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoTipoIdentificacion() {

            axios.get(this.baseURL + 'api/cargarti')
                .then(response => {
                    this.tipoIdentificacion = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoSectores() {

            axios.get(this.baseURL + 'api/cargarse')
                .then(response => {
                    this.sectorEmpresa = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoTipoEmpresa() {

            axios.get(this.baseURL + 'api/cargarte')
                .then(response => {
                    this.tipoEmpresa = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoDepartamentos() {

            axios.get(this.baseURL + 'api/cargarde')
                .then(response => {
                    this.departamentos = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoCategorias() {

            axios.get(this.baseURL + 'api/cargarcc')
                .then(response => {
                    this.categorias = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoCiudades(id) {

            axios.post(this.baseURL + 'api/cargarci', {
                'iddpto': id,
            })
                .then(response => {
                    this.ciudades = response.data.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoCargos(id) {

            axios.post(this.baseURL + 'api/cargarca', {
                'idcat': id,
            })
                .then(response => {
                    this.cargo = null;
                    this.cargos = response.data.data;
                })
                .catch(error => {
                    console.log(error);
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

        llamadoHistorialGestion() {

            axios.post(this.baseURL + 'api/cargarhistorialgestion', {
                'id_campaña': this.campañaSeleccionada ? this.campañaSeleccionada.id : 0,
                'id_contacto': this.empresaSeleccionada ? this.empresaSeleccionada.idContacto : 0,
                'id_empresa': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
            })
                .then(response => {
                    this.historialGestion = response.data.data;
                    this.cargandoHistorial = false;
                    this.cargandoHistorial2 = false;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        llamadoHistorialLead(tipoAgrupar) {

            axios.post(this.baseURL + 'api/cargarhistoriallead', {
                'id_usuario': this.comercialId,
                'agrupar': tipoAgrupar
            })
                .then(response => {
                    if (tipoAgrupar != 3) {
                        const parsed = JSON.parse(response.data.data[0].json_resultado);
                        this.historialLead = parsed;
                        this.cargandoHistorial2 = false;
                    } else {
                        this.historialLead = response.data.data;
                        this.cargandoHistorial2 = false;
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },

        cargarServiciosActividad() {
            axios.get(this.baseURL + 'api/cargarsv')
                .then(response => {
                    // Filtra para ocultar el servicio con nombre 'Presentación Corporativa'
                    const serviciosFiltrados = response.data.data.filter(s => s.nombre?.toLowerCase() !== 'presentacion comercial');
                    this.selectServiciosActividad = serviciosFiltrados;
                })
                .catch(error => {
                    console.log(response.data[0].error);
                });
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

        campañasEnviadas() {
            axios.post(this.baseURL + 'api/reporteCampaniasEnviadas', {
                'idusu': localStorage.getItem('idUsuario'),
            })
                .then(response => {
                    this.informeLlamadas = response.data.data;

                    this.llamadasHoy = this.informeLlamadas[0].llamadas_hoy;
                    this.llamadasEfectivasLead = this.informeLlamadas[0].llamadas_con_lead;
                    this.llamadasEfectivasSinLead = this.informeLlamadas[0].llamadas_sin_lead;
                    this.llamadasNoEfectivas = this.informeLlamadas[0].llamadas_no_efectivas;
                    this.totalLlamadas = this.informeLlamadas[0].total_llamadas;

                    this.progresoCampañas = Math.round((this.totalLlamadas / this.metaLlamadas) * 100);
                    this.bufferCampañas = this.progresoCampañas + 15;
                })
                .catch(error => {
                    console.log(error);
                });
        },

        esCorreoValido(correo) {
            const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return regex.test(correo);
        },

        esUrlValida(url) {
            const regex = /^(https?:\/\/)?([\w.-]+)+(:\d+)?(\/[\w./#-]*)*\/?$/;
            return regex.test(url);
        },

        validarNit(nit) {
            axios.post(this.baseURL + 'api/validarnitraz', { nit, raz: '' })
                .then(({ data }) => {
                    const row = data?.data?.[0];
                    if (!row) {
                        this.alertaNit = false;
                        this.mensajeAlertaNit = '';
                        this.dsGuardar = false;
                        return;
                    }
                    if (row.comercial && row.comercial.toLowerCase() === (this.nombreComercial || '').toLowerCase()) {
                        this.mensajeAlertaNit = 'Este NIT ya está registrado en tu cartera.';
                    } else {
                        this.mensajeAlertaNit = `Este NIT ya se encuentra asignado al comercial: ${row.comercial}`;
                    }
                    this.alertaNit = true;
                    this.dsGuardar = true;
                })
                .catch(err => {
                    console.log(err);
                });
        },

        // Valida Razón Social y muestra mensaje según el comercial asignado
        validarRazonSocial(newRazonSocial) {
            axios.post(this.baseURL + 'api/validarnitraz', { nit: '', raz: newRazonSocial })
                .then(({ data }) => {
                    const row = data?.data?.[0];
                    if (!row) {
                        this.alertaRazonSocial = false;
                        this.mensajeAlertaRazonSocial = '';
                        this.dsGuardar = false;
                        return;
                    }
                    if (row.comercial && row.comercial.toLowerCase() === (this.nombreComercial || '').toLowerCase()) {
                        this.mensajeAlertaRazonSocial = 'Esta razón social ya está registrada en tu cartera.';
                    } else {
                        this.mensajeAlertaRazonSocial = `Esta razón social ya se encuentra asignada al comercial: ${row.comercial}`;
                    }
                    this.alertaRazonSocial = true;
                    this.dsGuardar = true;
                })
                .catch(err => {
                    console.log(err);
                });
        },

        cerrarFormularioCampaña() {
            this.dialogCrearCampaña = false;
            this.selectedNombreCampaña = null;
            this.selectedDetalleCampaña = null;
            this.selectedGuionCampaña = null;
            this.validandoActividad = false;
        },

        cerrarFichaProspecto() {
            this.dialogInfoProsCon = false;
            this.fichaNit = null;
            this.fichaRazonSocial = null;
            this.fichaTipoId = null;
            this.fichaTipoEmp = null;
            this.fichaSector = null;
            this.fichaDireccion = null;
            this.fichaDepartamento = null;
            this.fichaCiudad = null;
            this.fichaWeb = null;
            this.fichaCorreoEmpresa = null;
            this.fichaTel1 = null;
            this.fichaTel2 = null;
            this.fichaNombre = null;
            this.fichaApellido = null;
            this.fichaCategoria = null;
            this.fichaCargo = null;
            this.fichaCorreoContacto = null;
            this.fichaExtension = null;
            this.fichaCelular = null;
        },

        cerrarFormularioProspecto() {
            this.formularioProspecto = false;
            this.empresa = null;
            this.nit = null;
            this.tipoId = null;
            this.tipoEmp = null;
            this.sector = null;
            this.departamento = null;
            this.ciudad = null;
            this.web = null;
            this.correoEmpresa = null;
            this.tel1 = null;
            this.tel2 = null;
            this.razonSocial = null;
            this.direccion = null;
            this.dsGuardar = false;
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

        cambiarImagen() {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/jpeg';

            input.onchange = async (event) => {
                const file = event.target.files[0];
                if (file) {
                    const formData = new FormData();
                    const nombre = `${this.comercialId}.jpeg`;
                    formData.append('imagen', file);
                    formData.append('nombre_archivo', nombre);

                    try {
                        await axios.post(this.baseURL + 'api/subir-imagen', formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            }
                        });

                        // Forzar recarga para evitar caché
                        this.imagenComercial = `/images/${this.comercialId}.jpeg?${Date.now()}`;
                        this.mensajeAlert = 'Imagen actualizada correctamente, si no puedes vizualizarla, recarga la página.';
                        this.alerta = true;
                        this.ifCargando = false;
                    } catch (error) {
                        console.error('❌ Error al subir imagen:', error);
                    }
                }
            };

            input.click();
        },

        filterTel1() {
            if (this.tel1 < 57) {
                this.tel1 = 57;
            }
            if (this.tel1 && this.tel1.length > 12) {
                // Si tiene más de 10 dígitos, truncar el valor
                this.tel1 = this.tel1.slice(0, 12);
            }
        },

        filterNumber() {
            if (this.celular < 573) {
                this.celular = 573;
            }

            if (this.celular && this.celular.length > 12) {
                // Si tiene más de 10 dígitos, truncar el valor
                this.celular = this.celular.slice(0, 12);
            }
        },

        cambiarClave() {
            const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

            if (this.nuevaClave !== this.confirmarClave) {
                this.alerta = true;
                this.mensajeAlert = 'Las claves no coinciden.';
                return;
            } else if (!regex.test(this.nuevaClave)) {
                this.alerta = true;
                this.mensajeAlert = 'La nueva clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.';
                return;
            } else {
                axios.post(this.baseURL + 'api/cambiarclave', {
                    idusu: localStorage.getItem('idUsuario'),
                    claveActual: CryptoJS.MD5(this.claveActual).toString(),
                    nuevaClave: CryptoJS.MD5(this.nuevaClave).toString(),
                })
                    .then(response => {
                        if (response.data.data[0].respuesta == 'La clave actual ingresada no coincide con el usuario.') {
                            this.alertLogin = true;
                            this.mensajeAlert = 'La clave actual ingresada no coincide con el usuario.';
                        } else if (response.data.data[0].respuesta == 'La clave ha sido editada correctamente.') {
                            this.alertLogin = true;
                            this.mensajeAlert = 'La clave ha sido editada correctamente.';
                            this.dialogCambioClave = false;
                            this.claveActual = null;
                            this.nuevaClave = null;
                            this.confirmarClave = null;
                        }
                    })
                    .catch(error => {
                        console.error('Error al cambiar la clave:', error);
                        this.alerta = true;
                        this.mensajeAlert = 'Error al cambiar la clave.';
                    });
            }
        },

        isValidPassword(password) {
            const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;
            return regex.test(password);
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

        getCardStyle(empresa) {
            if (empresa.activo == 1) {
                return {
                    backgroundColor: this.empresaSeleccionada ? (this.empresaSeleccionada.id === empresa.id ? '#E3E7FC' : 'white') : 'white',
                };
            } else {
                return {
                    backgroundColor: this.empresaSeleccionada ? (this.empresaSeleccionada.id === empresa.id ? '#E6B3B9' : '#f8d7da') : '#f8d7da', // Color de fondo rojo claro para inactivos
                    opacity: this.empresaSeleccionada ? (this.empresaSeleccionada.id === empresa.id ? 1 : 0.7) : 0.7, // Opacidad reducida para inactivos
                }
            }
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

        irEmpresas() {
            this.$router.push('/empresas');
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
            this.$router.push('/contactos');
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

.campo-input {
    width: 91%;
    padding: 8px 12px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    outline: none;
    transition: border 0.3s;
}

.campo-input:focus {
    border-color: #007BFF;
    /* azul al enfocar */
    box-shadow: 0 0 3px rgba(0, 123, 255, 0.5);
}

.header-search .v-field {
    background: rgba(255, 255, 255, .12);
}

.header-search .v-field__input,
.header-search .v-icon {
    color: #fff !important;
}

.header-search .v-field__input::placeholder {
    color: rgba(255, 255, 255, .75);
}

.header-search .v-field__outline,
.header-search .v-field__overlay {
    opacity: .18;
}

.data-table :deep(th) {
    font-weight: 700;
}

.data-table :deep(td),
.data-table :deep(th) {
    white-space: nowrap;
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

.fancy-headers :deep(.v-table__wrapper > table > thead > tr > th) {
    background-color: #0078b4 !important;
    color: #fff !important;
    font-weight: 700;
    /* bold */
    font-size: 0.85rem;
    /* un poco más grande */
    text-align: center;
    letter-spacing: .2px;
    border-bottom: 2px solid rgba(255, 255, 255, .15);
}

/* 2) Mantener iconos del header en blanco */
.fancy-headers :deep(.v-table__wrapper thead .v-icon) {
    color: #fff !important;
    opacity: .95;
}

/* Zebra + hover + cursor */
.fancy-rows :deep(tbody tr.fancy-row) {
    transition: transform .15s ease, background-color .15s ease, box-shadow .15s ease;
    cursor: pointer;
}

.fancy-rows :deep(tbody tr.fancy-row:nth-child(even)) {
    background-color: rgba(0, 0, 0, 0.005);
}

.fancy-rows :deep(tbody tr.fancy-row:hover) {
    background-color: rgba(0, 108, 161, .06);
    /* azul muy suave */
    transform: translateY(-1px);
    box-shadow: 0 1px 0 rgba(0, 0, 0, .04) inset;
}

/* Bordes sutiles entre filas y más respiración */
.fancy-rows :deep(tbody td) {
    padding: 10px 12px;
    border-bottom: 1px solid rgba(0, 0, 0, .06);
}

/* Alinear números a la derecha (ej. costo) si quieres */
.fancy-rows :deep(tbody td.text-right) {
    text-align: right;
}

.fancy-rows :deep(tbody tr.tone--urgent > td) {
    background-color: rgba(211, 47, 47, 0.08) !important;
    /* #d32f2f @ 8% */
    color: #5c0101 !important;
    /* texto casi negro con tinte rojo */
}

.fancy-rows :deep(tbody tr.tone--urgent:hover > td) {
    background-color: rgba(211, 47, 47, 0.08) !important;
}

/* Próximo (3–5 días): amarillo suave */
.fancy-rows :deep(tbody tr.tone--soon > td) {
    background-color: rgba(251, 193, 45, 0.15) !important;
    /* #fbc02d @ 10% */
    color: #544e01 !important;
}

.fancy-rows :deep(tbody tr.tone--soon:hover > td) {
    background-color: rgba(251, 192, 45, 0.16) !important;
}

/* Seguro (>=7 días): azul como tu ejemplo */
.fancy-rows :deep(tbody tr.tone--safe > td) {
    background-color: rgba(69, 80, 236, 0.075) !important;
    /* #4550ec @ 6% */
    color: #131269 !important;
}

.fancy-rows :deep(tbody tr.tone--safe:hover > td) {
    background-color: rgba(69, 80, 236, 0.12) !important;
}

/* VENCIDO (gris suave) — solo si usarGrisVencido = true */
.fancy-rows :deep(.v-table__wrapper > table > tbody > tr.tone--past > td) {
    background-color: rgba(0, 0, 0, .04) !important;
    /* gris 4% */
    color: #2f2f2f !important;
    /* casi negro */
}

/* Neutro (sin color) */
.fancy-rows :deep(.v-table__wrapper > table > tbody > tr.tone--neutral > td) {
    background-color: transparent !important;
    color: inherit !important;
}

/* Colores pastel para interés en llamadas */
.fancy-rows :deep(tbody tr.tone--green-pastel > td) {
    background-color: #d2f8e5 !important;
    color: #1a3d2f !important;
}

.fancy-rows :deep(tbody tr.tone--green-pastel:hover > td) {
    background-color: #b6f2d6 !important;
}

.fancy-rows :deep(tbody tr.tone--blue-pastel > td) {
    background-color: #d2e6fa !important;
    color: #1a2a3d !important;
}

.fancy-rows :deep(tbody tr.tone--blue-pastel:hover > td) {
    background-color: #b6d6f2 !important;
}

.fancy-rows :deep(tbody tr.tone--red-pastel > td) {
    background-color: #f8d2d2 !important;
    color: #3d1a1a !important;
}

.fancy-rows :deep(tbody tr.tone--red-pastel:hover > td) {
    background-color: #f2b6b6 !important;
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

.timeline-container {
    position: relative;
    margin-left: 20px;
    margin-right: 10px;
}

.timeline-item {
    display: flex;
    align-items: flex-start;
    position: relative;
    margin-bottom: 32px;
    background: #fff;
    border: 1.5px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 2px 8px 0 #006ca11a;
    transition: box-shadow 0.2s, border 0.2s;

}

.timeline-marker {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #e0e0e0;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 16px;
    flex-shrink: 0;
    border: 2px solid #bdbdbd;
    margin-top: 10px;
    margin-left: 10px;

}

.timeline-green {
    border-color: #43a047;
    background: #d2f8e5;
}

.timeline-blue {
    border-color: #1976d2;
    background: #d2e6fa;
}

.timeline-red {
    border-color: #e53935;
    background: #f8d2d2;
}

.timeline-neutral {
    border-color: #bdbdbd;
    background: #f5f5f5;
}

.timeline-1565C0 {
    border-color: #1565c0;
    background: #d2e6fa;
}

.timeline-2095c9 {
    border-color: #2095c9;
    background: #d2e6fa;
}

.timeline-orange-darken-2 {
    border-color: #f57c00;
    background: #fff3e0;
}

.timeline-teal-darken-1 {
    border-color: #00897b;
    background: #e0f2f1;
}

.timeline-8E24AA {
    border-color: #8e24aa;
    background: #f3e5f5;
}

.timeline-brown-darken-3 {
    border-color: #5d4037;
    background: #efebe9;
}

.timeline-content {
    flex: 1;
    min-width: 0;
}

.timeline-date {
    font-size: 13px;
    font-weight: bold;
    color: #006CA1;
}

.timeline-type {
    font-size: 12px;
    font-weight: 500;
    margin-left: 8px;
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 10px 10px;
}

.timeline-text {
    font-size: 12px;
    margin-top: 4px;
}

.timeline-connector {
    position: absolute;
    left: 25px;
    top: 45px;
    width: 2px;
    height: calc(100% - 60px + 10px);
    background: #bdbdbd;
    z-index: 0;
}

@media (max-width: 600px) {
    .timeline-container {
        margin-left: 8px;
    }

    .timeline-marker {
        width: 24px;
        height: 24px;
        margin-right: 8px;
    }

    .timeline-content {
        font-size: 11px;
    }
}
</style>