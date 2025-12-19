<template>
    <!-- Navigation Drawer: Menú lateral con opciones según rol -->
    <v-navigation-drawer 
        v-model="drawerLocal" 
        temporary 
        :width="$vuetify.display.smAndDown ? 180 : 240" 
        app
        class="modern-drawer">
        
        <!-- Sección de perfil para PQR (Cargo ID = 5) -->
        <div v-if="idCargo === '5'" class="profile-section">
            <div class="profile-bg"></div>
            <div class="profile-content">
                <v-avatar 
                    size="90" 
                    class="profile-avatar elevation-8">
                    <v-img v-if="imagenComercial" :src="imagenComercial" cover></v-img>
                    <v-icon v-else color="white" size="52">mdi-account-circle</v-icon>
                </v-avatar>
                <div class="text-white text-caption mb-2" style="opacity: 0.95;">Bienvenido</div>
                <div class="text-white font-weight-bold text-h6 mt-3 mb-1">{{ nombreComercial }}</div>
                <v-chip 
                    size="small" 
                    color="rgba(255,255,255,0.2)" 
                    text-color="white"
                    class="mt-1 font-weight-medium">
                    <v-icon start size="16">mdi-shield-account</v-icon>
                    ID: {{ idCargo }}
                </v-chip>
            </div>
        </div>

        <v-list nav class="menu-list py-3">
            <!-- Separador decorativo -->
            <div v-if="idCargo === '5'" class="menu-divider"></div>

            <!-- Configuración (Cargo ID = 1 - Administrador) -->
            <div 
                v-if="idCargo === '1'"
                class="menu-item-custom rounded-xl mx-2 mb-2"
                :class="{ 'active-menu': $route.path === '/configuracion' }"
                @click="navegarA('/configuracion')">
                <v-icon class="menu-icon">mdi-cog-outline</v-icon>
                <span class="menu-item-text">Configuración</span>
            </div>

            <!-- Comercial (Cargo ID = 3) -->
            <div 
                v-if="idCargo === '3'"
                class="menu-item-custom rounded-xl mx-2 mb-2"
                :class="{ 'active-menu': $route.path === '/comercial' }"
                @click="navegarA('/comercial')">
                <v-icon class="menu-icon">mdi-briefcase-outline</v-icon>
                <span class="menu-item-text">Comercial</span>
            </div>

            <!-- Pendientes (Cargo ID = 3) -->
            <div 
                v-if="idCargo === '3'"
                class="menu-item-custom rounded-xl mx-2 mb-2"
                :class="{ 'active-menu': $route.path === '/pendiente-general' }"
                @click="navegarA('/pendiente-general')">
                <v-icon class="menu-icon">mdi-clipboard-check-outline</v-icon>
                <span class="menu-item-text">Pendientes</span>
            </div>

            <!-- Campañas (Cargo ID = 2) -->
            <!-- Campañas -->
            <div 
                v-if="idCargo === '2'"
                class="menu-group-container" 
                @mouseenter="campanasExpandido = true" 
                @mouseleave="campanasExpandido = false"
            >
                <div 
                    class="menu-item-custom"
                    :class="{ 
                        'active-menu': $route.path === '/VerCampanas' || 
                                       $route.path === '/informes-campanas' || 
                                       $route.path === '/prospeccion-telefonica' || 
                                       $route.path === '/seguimiento-llamadas' || 
                                       $route.path === '/campana'
                    }"
                >
                    <v-icon class="menu-icon">mdi-bullhorn-outline</v-icon>
                    <span class="menu-item-text">Campañas</span>
                    <v-icon class="expand-icon" :class="{ expanded: campanasExpandido }">mdi-chevron-down</v-icon>
                </div>
                
                <transition name="expand">
                    <div v-show="campanasExpandido" class="submenu-container">
                        <div 
                            class="submenu-item-custom" 
                            :class="{ 'active-submenu': $route.path === '/VerCampanas' }"
                            @click="navegarA('/VerCampanas')"
                        >
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-view-gallery-outline</v-icon>
                            <span class="submenu-text">Galería</span>
                        </div>
                        
                        <div 
                            class="submenu-item-custom" 
                            :class="{ 'active-submenu': $route.path === '/informes-campanas' }"
                            @click="navegarA('/informes-campanas')"
                        >
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-chart-line</v-icon>
                            <span class="submenu-text">Métricas</span>
                        </div>
                        
                        <div 
                            class="submenu-item-custom" 
                            :class="{ 'active-submenu': $route.path === '/prospeccion-telefonica' }"
                            @click="navegarA('/prospeccion-telefonica')"
                        >
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-phone-outline</v-icon>
                            <span class="submenu-text">Prospección Telefónica</span>
                        </div>
                        
                        <div 
                            class="submenu-item-custom" 
                            :class="{ 'active-submenu': $route.path === '/seguimiento-llamadas' }"
                            @click="navegarA('/seguimiento-llamadas')"
                        >
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-phone-clock</v-icon>
                            <span class="submenu-text">Seguimiento Llamadas</span>
                        </div>
                        
                        <div class="submenu-item-custom disabled">
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-email-outline</v-icon>
                            <span class="submenu-text">Email Marketing</span>
                        </div>
                        
                        <div 
                            class="submenu-item-custom" 
                            :class="{ 'active-submenu': $route.path === '/campana' }"
                            @click="navegarA('/campana')"
                        >
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-whatsapp</v-icon>
                            <span class="submenu-text">WhatsApp Business</span>
                        </div>
                    </div>
                </transition>
            </div>

            <!-- Clientes -->
            <div 
                v-if="idCargo === '2'"
                class="menu-group-container" 
                @mouseenter="clientesExpandido = true" 
                @mouseleave="clientesExpandido = false"
            >
                <div 
                    class="menu-item-custom"
                    :class="{ 'active-menu': $route.path === '/empresas' }"
                >
                    <v-icon class="menu-icon">mdi-account-group-outline</v-icon>
                    <span class="menu-item-text">Clientes</span>
                    <v-icon class="expand-icon" :class="{ expanded: clientesExpandido }">mdi-chevron-down</v-icon>
                </div>
                
                <transition name="expand">
                    <div v-show="clientesExpandido" class="submenu-container">
                        <div 
                            class="submenu-item-custom" 
                            :class="{ 'active-submenu': $route.path === '/empresas' }"
                            @click="navegarA('/empresas')"
                        >
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-domain</v-icon>
                            <span class="submenu-text">Empresas</span>
                        </div>
                    </div>
                </transition>
            </div>

            <!-- Chat -->
            <div 
                v-if="idCargo === '2'"
                class="menu-group-container" 
                @mouseenter="chatExpandido = true" 
                @mouseleave="chatExpandido = false"
            >
                <div 
                    class="menu-item-custom"
                    :class="{ 'active-menu': $route.path === '/contactos' }"
                >
                    <v-icon class="menu-icon">mdi-message-text-outline</v-icon>
                    <span class="menu-item-text">Chat</span>
                    <v-icon class="expand-icon" :class="{ expanded: chatExpandido }">mdi-chevron-down</v-icon>
                </div>
                
                <transition name="expand">
                    <div v-show="chatExpandido" class="submenu-container">
                        <div 
                            class="submenu-item-custom" 
                            :class="{ 'active-submenu': $route.path === '/contactos' }"
                            @click="navegarA('/contactos')"
                        >
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-card-account-details-outline</v-icon>
                            <span class="submenu-text">Contactos</span>
                        </div>
                    </div>
                </transition>
            </div>

            <!-- Gerencial (Cargo ID = 4 - En construcción) -->
            <div 
                v-if="idCargo === '4'"
                class="menu-item-custom rounded-xl mx-2 mb-2 disabled"
                style="opacity: 0.6; cursor: not-allowed;">
                <v-icon class="menu-icon" style="opacity: 0.5;">mdi-chart-timeline-variant</v-icon>
                <span class="menu-item-text" style="opacity: 0.8;">
                    Gerencial
                </span>
                <v-chip size="x-small" color="warning" class="ml-2">Próximamente</v-chip>
            </div>

            <!-- PQR (Cargo ID = 5) -->
            <div 
                v-if="idCargo === '5'" 
                class="menu-group-container"
                @mouseenter="pqrExpandido = true"
                @mouseleave="pqrExpandido = false">
                <div 
                    class="menu-item-custom rounded-xl mx-2 mb-1"
                    :class="{ 'active-menu': $route.path === '/pqr' || $route.path === '/informes-cio' }"
                    @click="pqrExpandido = !pqrExpandido">
                    <v-icon class="menu-icon">mdi-face-agent</v-icon>
                    <span class="menu-item-text">Centro de Atención</span>
                    <v-icon class="expand-icon" :class="{ expanded: pqrExpandido }">mdi-chevron-down</v-icon>
                </div>

                <transition name="expand">
                    <div v-show="pqrExpandido" class="submenu-container">
                        <div class="submenu-item-custom" :class="{ 'active-submenu': $route.path === '/pqr' }" @click="navegarA('/pqr')">
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-ticket-account</v-icon>
                            <span class="submenu-text">Solicitudes PQR</span>
                        </div>

                        <div class="submenu-item-custom" :class="{ 'active-submenu': $route.path === '/informes-cio' }" @click="navegarA('/informes-cio')">
                            <span class="submenu-bullet"></span>
                            <v-icon class="submenu-icon">mdi-chart-box-multiple-outline</v-icon>
                            <span class="submenu-text">Informes</span>
                        </div>
                    </div>
                </transition>
            </div>

            <!-- Pedidos (Cargo ID = 3) -->
            <div 
                v-if="idCargo === '3'"
                class="menu-item-custom rounded-xl mx-2 mb-2"
                :class="{ 'active-menu': $route.path === '/pedidos' }"
                @click="navegarA('/pedidos')">
                <v-icon class="menu-icon">mdi-package-variant</v-icon>
                <span class="menu-item-text">Pedidos</span>
            </div>

            <!-- Fallback: Si no hay permisos específicos, mostrar mensaje -->
            <v-list-item v-if="!idCargo || (idCargo !== '1' && idCargo !== '2' && idCargo !== '3' && idCargo !== '4' && idCargo !== '5')" class="mt-4">
                <v-list-item-title style="color: white; text-align: center; font-size: 0.9rem; opacity: 0.8;">
                    Sin opciones de menú disponibles
                </v-list-item-title>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>

    <!-- App Bar: Barra superior -->
    <v-app-bar color="white" elevation="1" height="64" class="border-b">
        <v-container class="d-flex align-center px-6" fluid>
            <!-- Hamburger Menu -->
            <v-app-bar-nav-icon variant="text" @click.stop="toggleDrawer"></v-app-bar-nav-icon>

            <!-- Logo Section -->
            <div class="d-flex align-center mr-4 ml-2">
                <img src="../assets/LogosinFondo.png" alt="Logo" style="height: 50px; width: auto;" />
            </div>

            <!-- Back Button -->
            <v-btn icon variant="text" color="#475569" class="mr-4" @click="$router.go(-1)">
                <v-icon>mdi-arrow-left</v-icon>
            </v-btn>

            <v-spacer></v-spacer>

            <!-- Title -->
            <h1 class="text-subtitle-1 font-weight-bold text-grey-darken-2 hidden-xs-only">
                Bienvenido {{ nombreComercial }}
            </h1>

            <v-spacer></v-spacer>

            <!-- Notifications -->
            <v-menu v-model="menuNotificaciones" offset-y location="bottom end" :close-on-content-click="false">
                <template v-slot:activator="{ props }">
                    <v-btn icon variant="text" color="grey-darken-1" v-bind="props" class="mr-2">
                        <v-badge :content="notificacionesNoLeidas" :value="notificacionesNoLeidas > 0" color="red" dot offset-x="2" offset-y="2">
                            <v-icon>mdi-bell-outline</v-icon>
                        </v-badge>
                    </v-btn>
                </template>

                <v-card width="350" class="rounded-lg mt-2">
                    <v-card-title class="text-subtitle-1 font-weight-bold px-4 py-3 border-b d-flex align-center justify-space-between">
                        Notificaciones
                        <v-btn size="x-small" variant="text" color="primary" @click="marcarTodasLeidas" v-if="notificacionesNoLeidas > 0">
                            Marcar leídas
                        </v-btn>
                    </v-card-title>
                    
                    <v-list lines="two" max-height="400" class="overflow-y-auto py-0">
                        <template v-if="notificaciones.length > 0">
                            <v-list-item v-for="(notificacion, index) in notificaciones" :key="index" :value="index" 
                                :class="{'bg-blue-lighten-5': !notificacion.leida}"
                                @click="verNotificacion(notificacion)">
                                <template v-slot:prepend>
                                    <v-avatar color="blue-lighten-4" size="32">
                                        <v-icon size="18" color="blue-darken-2">{{ getIconoNotificacion(notificacion.tipo) }}</v-icon>
                                    </v-avatar>
                                </template>
                                
                                <v-list-item-title class="text-body-2 font-weight-bold mb-1">
                                    {{ notificacion.titulo }}
                                </v-list-item-title>
                                <v-list-item-subtitle class="text-caption text-grey-darken-1">
                                    {{ notificacion.mensaje }}
                                </v-list-item-subtitle>
                                <template v-slot:append>
                                    <div class="d-flex flex-column align-end">
                                        <span class="text-caption text-grey">{{ notificacion.hora }}</span>
                                        <v-icon v-if="!notificacion.leida" color="blue" size="8" class="mt-1">mdi-circle</v-icon>
                                    </div>
                                </template>
                            </v-list-item>
                        </template>
                        <div v-else class="d-flex flex-column align-center justify-center py-8 text-grey">
                            <v-icon size="48" class="mb-2 opacity-50">mdi-bell-off-outline</v-icon>
                            <span class="text-caption">No tienes notificaciones nuevas</span>
                        </div>
                    </v-list>
                    
                    <v-divider></v-divider>
                    <v-btn block variant="text" color="primary" class="text-caption py-2">
                        Ver todas
                    </v-btn>
                </v-card>
            </v-menu>

            <!-- User Profile -->
            <v-menu v-model="menuAbierto" offset-y location="bottom end" persistent>
                <template #activator="{ props }">
                    <v-btn icon v-bind="props" class="ml-2">
                        <v-avatar color="#1E293B" size="40" :src="imagenComercial">
                            <v-icon color="white" size="24">mdi-account</v-icon>
                        </v-avatar>
                    </v-btn>
                </template>

                <v-card width="300" class="rounded-lg mt-2">
                    <v-list>
                        <v-list-item :prepend-avatar="imagenComercial" :title="nombreComercial"
                            :subtitle="correoUsuario" @click="dialogImagenPerfil = true">
                        </v-list-item>
                    </v-list>
                    <v-divider></v-divider>
                    <v-list density="compact">
                        <v-list-item prepend-icon="mdi-key-variant" title="Cambiar clave"
                            @click="dialogCambioClave = true"></v-list-item>
                        <v-list-item prepend-icon="mdi-logout" title="Cerrar sesión"
                            @click="$emit('cerrar-sesion')"></v-list-item>
                    </v-list>
                </v-card>
            </v-menu>
        </v-container>
    </v-app-bar>

    <!-- Diálogo para ver/actualizar foto de perfil -->
    <v-dialog v-model="dialogImagenPerfil" max-width="600px" scrim="black" opacity="0.9">
        <div class="d-flex flex-column align-center justify-center" style="height: 100%;">
            <!-- Imagen grande sin tarjeta -->
            <v-avatar size="350" class="elevation-20 mb-8" style="border: 4px solid white;">
                <v-img :src="imagenComercial" cover></v-img>
            </v-avatar>
            
            <!-- Controles flotantes estilo píldora -->
            <v-sheet class="rounded-pill px-6 py-3 d-flex align-center justify-space-between elevation-10" color="white" width="auto" min-width="280">
                <v-btn icon variant="text" color="primary" @click="seleccionarNuevaImagen" class="mr-2">
                    <v-icon size="32">mdi-camera-flip</v-icon>
                    <v-tooltip activator="parent" location="top">Cambiar Foto</v-tooltip>
                </v-btn>
                
                <v-divider vertical class="mx-3"></v-divider>
                
                <v-btn icon variant="text" color="error" @click="eliminarImagen" class="mx-2">
                    <v-icon size="32">mdi-delete-outline</v-icon>
                    <v-tooltip activator="parent" location="top">Eliminar Foto</v-tooltip>
                </v-btn>

                <v-divider vertical class="mx-3"></v-divider>

                <v-btn icon variant="text" color="grey-darken-2" @click="dialogImagenPerfil = false" class="ml-2">
                    <v-icon size="32">mdi-close-circle-outline</v-icon>
                    <v-tooltip activator="parent" location="top">Cerrar</v-tooltip>
                </v-btn>
            </v-sheet>
        </div>
    </v-dialog>

    <!-- Diálogo Cambiar Clave -->
    <v-dialog v-model="dialogCambioClave" persistent max-width="400px">
        <v-card class="pa-4 rounded-xl">
            <v-card-title class="text-h6 text-primary">
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
                    La nueva clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.
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
                <v-btn variant="flat" color="#223551" @click="cambiarClave()">Guardar</v-btn>
                <v-btn variant="flat" color="grey"
                    @click="dialogCambioClave = false; claveActual = null; nuevaClave = null; confirmarClave = null;">Cancelar</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <!-- Alerta de Permisos Denegados -->
    <v-snackbar 
        v-model="dialogPermisos" 
        location="top right"
        :timeout="5000"
        color="rgba(255, 205, 210, 0.85)"
        rounded="lg"
        elevation="4"
        multi-line
        class="mt-4">
        <div class="d-flex align-center justify-space-between">
            <div class="d-flex align-center">
                <v-icon class="mr-3" color="#c62828">mdi-lock-alert</v-icon>
                <span class="font-weight-medium" style="color: #b71c1c;">No tienes permisos para acceder a esta página</span>
            </div>
            <v-btn 
                icon="mdi-close" 
                size="small" 
                variant="text" 
                color="#c62828"
                @click="dialogPermisos = false"
                class="ml-4">
            </v-btn>
        </div>
    </v-snackbar>

    <!-- Alerta Tipo Snackbar -->
    <v-snackbar 
        v-model="alerta" 
        location="top right"
        :timeout="4000"
        :color="tipoAlerta === 'success' ? 'rgba(200, 230, 201, 0.85)' : 
                 tipoAlerta === 'error' ? 'rgba(255, 205, 210, 0.85)' : 
                 tipoAlerta === 'warning' ? 'rgba(255, 249, 196, 0.85)' : 
                 'rgba(187, 222, 251, 0.85)'"
        rounded="lg"
        elevation="4"
        multi-line
        class="mt-4">
        <div class="d-flex align-center justify-space-between">
            <div class="d-flex align-center">
                <v-icon 
                    class="mr-3"
                    :color="tipoAlerta === 'success' ? '#2e7d32' : 
                            tipoAlerta === 'error' ? '#c62828' : 
                            tipoAlerta === 'warning' ? '#f57f17' : 
                            '#1565c0'">
                    {{ tipoAlerta === 'success' ? 'mdi-check-circle' : 
                       tipoAlerta === 'error' ? 'mdi-alert-circle' : 
                       tipoAlerta === 'warning' ? 'mdi-alert' : 'mdi-information' }}
                </v-icon>
                <span 
                    class="font-weight-medium"
                    :style="{ color: tipoAlerta === 'success' ? '#1b5e20' : 
                                     tipoAlerta === 'error' ? '#b71c1c' : 
                                     tipoAlerta === 'warning' ? '#f57f17' : 
                                     '#0d47a1' }">{{ mensajeAlerta }}</span>
            </div>
            <v-btn 
                icon="mdi-close" 
                size="small" 
                variant="text" 
                :color="tipoAlerta === 'success' ? '#2e7d32' : 
                        tipoAlerta === 'error' ? '#c62828' : 
                        tipoAlerta === 'warning' ? '#f57f17' : 
                        '#1565c0'"
                @click="alerta = false"
                class="ml-4">
            </v-btn>
        </div>
    </v-snackbar>
</template>

<script>
import axios from 'axios';
import CryptoJS from "crypto-js";
import Pusher from 'pusher-js';

export default {
    name: 'AppHeader',
    props: {
        nombreComercial: { type: String, default: '' },
        imagenComercial: { type: String, default: '' },
        correoUsuario: { type: String, default: '' },
        comercialId: { type: String, default: '0' },
        baseURL: { type: String, required: true },
        drawer: { type: Boolean, default: true },
        idCargo: { type: String, default: null }  // Nuevo: rol del usuario
    },
    data() {
        return {
            drawerLocal: this.drawer || false,  // Inicializar con el valor del prop
            menuAbierto: false,
            menuNotificaciones: false,
            notificaciones: [], // Inicialmente vacía, se carga dinámicamente
            pusher: null,
            channel: null,
            
            dialogImagenPerfil: false,
            dialogCambioClave: false,
            
            // Control de expansión de menús
            pqrExpandido: false,
            campanasExpandido: false,
            clientesExpandido: false,
            chatExpandido: false,
            
            // Diálogo de error de permisos
            dialogPermisos: false,
            
            // Clave
            claveActual: null,
            nuevaClave: null,
            confirmarClave: null,
            mostrarClaveActual: false,
            mostrarNuevaClave: false,
            mostrarConfirmarClave: false,

            // Alerta
            alerta: false,
            mensajeAlerta: '',
            tipoAlerta: 'success', // success, error, warning, info
            ifCargando: false
        }
    },
    mounted() {
        // Log para debug: verificar que idCargo llega correctamente
        console.log('AppHeader mounted - idCargo:', this.idCargo, 'tipo:', typeof this.idCargo);
        this.cargarNotificaciones();
        // Escuchar el evento de acceso denegado del router
        window.addEventListener('access-denied', this.mostrarErrorPermisos);
    },
    beforeUnmount() {
        // Limpiar el listener al destruir el componente
        window.removeEventListener('access-denied', this.mostrarErrorPermisos);
        if (this.pusher) {
            this.pusher.disconnect();
        }
    },
    watch: {
        // Sincronizar drawer prop con estado local
        drawer(newVal) {
            this.drawerLocal = newVal;
        },
        drawerLocal(newVal) {
            this.$emit('update:drawer', newVal);
        }
    },
    emits: ['update:drawer', 'cerrar-sesion', 'imagen-actualizada'],
    computed: {
        notificacionesNoLeidas() {
            return this.notificaciones.filter(n => !n.leida).length;
        }
    },
    methods: {
        async marcarTodasLeidas() {
            this.notificaciones.forEach(n => n.leida = true);
            try {
                await axios.post(this.baseURL + 'api/actualizar_notificacion', {
                    id_usuario: this.comercialId,
                    marcar_todas: true
                });
            } catch (error) {
                console.error("Error marcando todas como leídas:", error);
            }
        },
        async verNotificacion(notificacion) {
            notificacion.leida = true;
            this.menuNotificaciones = false;
            
            if (notificacion.origen === 'bd') {
                try {
                    await axios.post(this.baseURL + 'api/actualizar_notificacion', {
                        id_notificacion: notificacion.id,
                        leida: true
                    });
                } catch (error) {
                    console.error("Error actualizando notificación:", error);
                }
            }

            if (notificacion.link) {
                this.$router.push(notificacion.link);
            } else {
                // Fallback para notificaciones legacy
                if (notificacion.titulo.includes('Tickets')) this.$router.push('/pqr');
                if (notificacion.titulo.includes('Pedidos')) this.$router.push('/pedidos');
            }
        },
        getIconoNotificacion(tipo) {
            switch(tipo) {
                case 'asignacion': return 'mdi-account-plus';
                case 'actualizacion': return 'mdi-update';
                case 'info': return 'mdi-information';
                case 'alerta': return 'mdi-alert';
                case 'exito': return 'mdi-check-circle';
                default: return 'mdi-bell';
            }
        },
        
        formatearFecha(fechaStr) {
            if (!fechaStr) return '';
            const fecha = new Date(fechaStr);
            const ahora = new Date();
            const diffMs = ahora - fecha;
            const diffMins = Math.floor(diffMs / 60000);
            const diffHrs = Math.floor(diffMs / 3600000);
            
            if (diffMins < 1) return 'Ahora';
            if (diffMins < 60) return `Hace ${diffMins} min`;
            if (diffHrs < 24) return `Hace ${diffHrs} h`;
            return fecha.toLocaleDateString();
        },

        async cargarNotificaciones() {
            let nuevasNotificaciones = [];

            // 1. Cargar notificaciones BD
            try {
                const response = await axios.post(this.baseURL + 'api/cargarNotificaciones', {
                    idusu: this.comercialId
                });
                if (response.data && response.data.data) {
                    const notifBD = response.data.data.map(n => ({
                        id: n.id,
                        titulo: n.titulo,
                        mensaje: n.mensaje,
                        hora: this.formatearFecha(n.fecha_creacion),
                        leida: n.leida,
                        tipo: n.tipo || 'info',
                        link: n.link,
                        origen: 'bd'
                    }));
                    nuevasNotificaciones = [...nuevasNotificaciones, ...notifBD];
                }
            } catch (e) {
                console.error("Error cargando notificaciones BD:", e);
            }

            // 2. Lógica Legacy (PQR)
            if (this.idCargo === '5') {
                try {
                    const response = await axios.post(this.baseURL + 'api/cargarpqrs', {
                        'idusu': this.comercialId,
                    });
                    if (response.data && response.data.data) {
                        const tickets = response.data.data;
                        const misTickets = tickets.filter(t => t.asignado == this.comercialId);
                        const nuevos = misTickets.filter(t => t.estado === 'Nuevo').length;
                        const enProceso = misTickets.filter(t => t.estado === 'En Proceso').length;
                        
                        if (nuevos > 0) {
                            nuevasNotificaciones.push({
                                id: 'pqr-new-' + Date.now(),
                                titulo: 'Tickets Nuevos',
                                mensaje: `Tienes ${nuevos} tickets nuevos asignados.`,
                                hora: 'Pendiente',
                                leida: false,
                                tipo: 'asignacion',
                                origen: 'local'
                            });
                        }
                        if (enProceso > 0) {
                            nuevasNotificaciones.push({
                                id: 'pqr-proc-' + Date.now(),
                                titulo: 'Tickets en Proceso',
                                mensaje: `Tienes ${enProceso} tickets en proceso.`,
                                hora: 'Pendiente',
                                leida: false,
                                tipo: 'actualizacion',
                                origen: 'local'
                            });
                        }
                    }
                } catch (e) { console.error(e); }
            }

            // 3. Lógica Legacy (Pedidos)
            if (this.idCargo === '3') {
                try {
                    const response = await axios.post(this.baseURL + 'api/cargarPedidos');
                    if (response.data && response.data.data) {
                        const pedidos = response.data.data;
                        const nuevos = pedidos.filter(p => p.est_nombre === 'Nuevo').length;
                        if (nuevos > 0) {
                            nuevasNotificaciones.push({
                                id: 'ped-new-' + Date.now(),
                                titulo: 'Pedidos Nuevos',
                                mensaje: `Hay ${nuevos} pedidos nuevos.`,
                                hora: 'Hoy',
                                leida: false,
                                tipo: 'info',
                                origen: 'local'
                            });
                        }
                    }
                } catch (e) { console.error(e); }
            }

            // 4. Pusher
            if (this.idCargo === '2') {
                this.initPusher();
            }

            this.notificaciones = nuevasNotificaciones;
        },

        initPusher() {
            const app_key = import.meta.env.VITE_PUSHER_KEY || 'f0b7888bd36a4d955af0'; 
            const cluster = import.meta.env.VITE_PUSHER_CLUSTER || 'us2';

            if (!this.pusher) {
                this.pusher = new Pusher(app_key, {
                    cluster: cluster,
                    encrypted: true
                });
                
                this.channel = this.pusher.subscribe('webhooks');
                this.channel.bind('App\\Events\\Comercial', (data) => {
                    this.notificaciones.unshift({
                        id: Date.now(),
                        titulo: 'Campaña Finalizada',
                        mensaje: data.message || 'Proceso de campaña terminado.',
                        hora: 'Ahora',
                        leida: false,
                        tipo: 'info'
                    });
                    this.alerta = true;
                    this.mensajeAlerta = 'Nueva notificación de campaña recibida';
                    this.tipoAlerta = 'info';
                });
            }
        },

        mostrarErrorPermisos() {
            this.dialogPermisos = true
        },
        // Toggle del drawer de navegación
        toggleDrawer() {
            this.drawerLocal = !this.drawerLocal;
        },

        // Navegar a una ruta y cerrar el drawer
        navegarA(ruta) {
            this.$router.push(ruta);
            this.drawerLocal = false;
        },
        seleccionarNuevaImagen() {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/jpeg, image/png';

            input.onchange = async (event) => {
                const file = event.target.files[0];
                if (file) {
                    const formData = new FormData();
                    const nombre = `${this.comercialId}.jpeg`;
                    formData.append('imagen', file);
                    formData.append('nombre_archivo', nombre);

                    try {
                        this.ifCargando = true;
                        const response = await axios.post(this.baseURL + 'api/subir-imagen', formData, {
                            headers: { 'Content-Type': 'multipart/form-data' }
                        });

                        let newUrl;
                        if (response.data.url) {
                             const separator = response.data.url.includes('?') ? '&' : '?';
                             newUrl = response.data.url + separator + 't=' + Date.now();
                             localStorage.setItem('imagenComercial', newUrl);
                        } else {
                             newUrl = `${this.baseURL}images/${this.comercialId}.jpeg?t=${Date.now()}`;
                             localStorage.setItem('imagenComercial', newUrl);
                        }
                       
                        this.$emit('imagen-actualizada', newUrl);
                        this.mensajeAlerta = 'Imagen actualizada correctamente.';
                        this.tipoAlerta = 'success';
                        this.alerta = true;
                        this.dialogImagenPerfil = false;
                    } catch (error) {
                        console.error('❌ Error al subir imagen:', error);
                        this.mensajeAlerta = 'Error al subir la imagen.';
                        this.tipoAlerta = 'error';
                        this.alerta = true;
                    } finally {
                        this.ifCargando = false;
                    }
                }
            };

            input.click();
        },

        eliminarImagen() {
            const localUrl = `/images/${this.comercialId}.jpeg?t=${Date.now()}`;
            localStorage.removeItem('imagenComercial');
            this.$emit('imagen-actualizada', localUrl);
            
            this.mensajeAlerta = 'Imagen eliminada (restaurada a predeterminada).';
            this.tipoAlerta = 'info';
            this.alerta = true;
            this.dialogImagenPerfil = false;
        },

        isValidPassword(password) {
            const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;
            return regex.test(password);
        },

        cambiarClave() {
            const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

            if (this.nuevaClave !== this.confirmarClave) {
                this.mensajeAlerta = 'Las claves no coinciden.';
                this.tipoAlerta = 'warning';
                this.alerta = true;
                return;
            } else if (!regex.test(this.nuevaClave)) {
                this.mensajeAlerta = 'La nueva clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.';
                this.tipoAlerta = 'warning';
                this.alerta = true;
                return;
            } else {
                axios.post(this.baseURL + 'api/cambiarclave', {
                    idusu: this.comercialId,
                    claveActual: CryptoJS.MD5(this.claveActual).toString(),
                    nuevaClave: CryptoJS.MD5(this.nuevaClave).toString(),
                })
                    .then(response => {
                        if (response.data.data[0].respuesta == 'La clave actual ingresada no coincide con el usuario.') {
                            this.mensajeAlerta = 'La clave actual ingresada no coincide con el usuario.';
                            this.tipoAlerta = 'error';
                            this.alerta = true;
                        } else if (response.data.data[0].respuesta == 'La clave ha sido editada correctamente.') {
                            this.mensajeAlerta = 'La clave ha sido editada correctamente.';
                            this.tipoAlerta = 'success';
                            this.alerta = true;
                            this.dialogCambioClave = false;
                            this.claveActual = null;
                            this.nuevaClave = null;
                            this.confirmarClave = null;
                        }
                    })
                    .catch(error => {
                        console.error('Error al cambiar la clave:', error);
                        this.mensajeAlerta = 'Error al cambiar la clave.';
                        this.tipoAlerta = 'error';
                        this.alerta = true;
                    });
            }
        }
    }
}
</script>

<style scoped>
/* Modern Drawer Styles */
.modern-drawer {
    background: linear-gradient(180deg, #006CA1 0%, #004B73 100%) !important;
    box-shadow: 4px 0 24px rgba(0, 0, 0, 0.15) !important;
}

/* Profile Section */
.profile-section {
    position: relative;
    padding: 2rem 1.5rem;
    margin-bottom: 1rem;
    overflow: hidden;
}

.profile-bg {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 140px;
    background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 100%);
    border-radius: 0 0 30% 30%;
}

.profile-content {
    position: relative;
    z-index: 1;
    text-align: center;
}

.profile-avatar {
    border: 4px solid rgba(255, 255, 255, 0.95) !important;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-avatar:hover {
    transform: scale(1.05);
}

/* Menu Divider */
.menu-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    margin: 0.5rem 1rem 1rem 1rem;
}

/* Menu List */
.menu-list {
    padding-top: 0.5rem !important;
}

/* Menu Items */
.menu-item {
    margin: 0.25rem 0.5rem !important;
    padding: 0.75rem 0.5rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border: 1px solid transparent !important;
}

.menu-item:hover {
    background: rgba(255, 255, 255, 0.15) !important;
    border-color: rgba(255, 255, 255, 0.25) !important;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.menu-item:active {
    transform: translateX(4px) scale(0.98);
}

/* Menu Item Active - Indicador minimalista */
.menu-item.active-menu,
.menu-item-custom.active-menu {
    background: rgba(255, 255, 255, 0.12) !important;
    border-left: 3px solid #ffffff !important;
    padding-left: calc(0.5rem - 3px) !important;
}

.menu-item.active-menu .menu-icon,
.menu-item-custom.active-menu .menu-icon {
    color: #ffffff !important;
}

.menu-item-text {
    color: white !important;
    font-weight: 500 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.3px;
}

.menu-icon {
    color: rgba(255, 255, 255, 0.95) !important;
    font-size: 22px !important;
    margin-right: 0.5rem !important;
    transition: transform 0.3s ease;
}

/* Anular espaciado de Vuetify en prepend */
.menu-item :deep(.v-list-item__prepend) {
    margin-inline-end: 0.5rem !important;
    margin-inline-start: 0 !important;
    padding-inline-end: 0 !important;
    width: 22px !important;
    min-width: 22px !important;
}

.menu-item :deep(.v-list-item__content) {
    padding-inline-start: 0 !important;
    padding-inline-end: 0 !important;
}

.menu-item:hover .menu-icon {
    transform: scale(1.1) rotate(5deg);
}

/* Submenu Items */
.submenu-item {
    padding: 0.6rem 1rem 0.6rem 3.5rem !important;
    margin: 0.15rem 0.5rem 0.15rem 1rem !important;
    border-radius: 10px !important;
    transition: all 0.25s ease !important;
    position: relative;
}

.submenu-item::before {
    content: '';
    position: absolute;
    left: 2.2rem;
    top: 50%;
    transform: translateY(-50%);
    width: 6px;
    height: 6px;
    background: rgba(255, 255, 255, 0.4);
    border-radius: 50%;
    transition: all 0.25s ease;
}

.submenu-item:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    padding-left: 3.75rem !important;
}

.submenu-item:hover::before {
    width: 8px;
    height: 8px;
    background: rgba(255, 255, 255, 0.8);
    box-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
}

.submenu-text {
    color: rgba(255, 255, 255, 0.95) !important;
    font-size: 0.88rem !important;
    font-weight: 400 !important;
}

.submenu-icon {
    color: rgba(255, 255, 255, 0.8) !important;
    font-size: 18px !important;
    margin-right: 0 !important;
}

/* Anular espaciado de Vuetify en prepend de submenú */
.submenu-item :deep(.v-list-item__prepend) {
    margin-inline-end: 0.5rem !important;
    margin-inline-start: 0 !important;
    padding-inline-end: 0 !important;
    width: 15px !important;
    min-width: 15px !important;
}

.submenu-item :deep(.v-list-item__content) {
    padding-inline-start: 0 !important;
    padding-inline-end: 0 !important;
}

/* Menu Group Transitions */
.menu-group {
    margin-bottom: 0.5rem;
}

/* Menu Group Container - incluye hover para todo el grupo */
.menu-group-container {
    margin-bottom: 0.5rem;
}

/* Custom Menu Item (sin v-list-group) */
.menu-item-custom {
    display: flex;
    align-items: center;
    padding: 0.75rem 0.5rem;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border: 1px solid transparent;
    position: relative;
}

.menu-item-custom:hover {
    background: rgba(255, 255, 255, 0.15) !important;
    border-color: rgba(255, 255, 255, 0.25) !important;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.menu-item-custom:active {
    transform: translateX(4px) scale(0.98);
}

.menu-item-custom .menu-icon {
    margin-right: 0.5rem;
    flex-shrink: 0;
}

.menu-item-custom .menu-item-text {
    flex: 1;
    color: white !important;
    font-weight: 500 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.3px;
}

.menu-item-custom .expand-icon {
    color: rgba(255, 255, 255, 0.8) !important;
    font-size: 20px !important;
    transition: transform 0.3s ease;
    margin-left: auto;
}

.menu-item-custom .expand-icon.expanded {
    transform: rotate(180deg);
}

/* Submenu Container */
.submenu-container {
    overflow: hidden;
}

.submenu-item-custom {
    display: flex;
    align-items: center;
    padding: 0.6rem 1rem 0.6rem 2.5rem;
    margin: 0.15rem 0.5rem 0.15rem 1rem;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.25s ease;
    position: relative;
}

.submenu-item-custom:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    padding-left: 2.75rem;
}

.submenu-item-custom .submenu-bullet {
    position: absolute;
    left: 1.5rem;
    width: 6px;
    height: 6px;
    background: rgba(255, 255, 255, 0.4);
    border-radius: 50%;
    transition: all 0.25s ease;
}

.submenu-item-custom:hover .submenu-bullet {
    width: 8px;
    height: 8px;
    background: rgba(255, 255, 255, 0.8);
    box-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
}

.submenu-item-custom .submenu-icon {
    margin-right: 0.5rem;
    flex-shrink: 0;
}

.submenu-item-custom .submenu-text {
    color: rgba(255, 255, 255, 0.95) !important;
    font-size: 0.88rem !important;
    font-weight: 400 !important;
}

/* Submenu Item Active - Indicador minimalista */
.submenu-item-custom.active-submenu {
    background: rgba(255, 255, 255, 0.15) !important;
    border-left: 2px solid rgba(255, 255, 255, 0.9) !important;
    padding-left: calc(2.5rem - 2px) !important;
}

.submenu-item-custom.active-submenu .submenu-bullet {
    background: #ffffff !important;
    width: 8px;
    height: 8px;
    box-shadow: 0 0 8px rgba(255, 255, 255, 0.6);
}

.submenu-item-custom.active-submenu .submenu-icon {
    color: #ffffff !important;
}

.submenu-item-custom.active-submenu .submenu-text {
    color: #ffffff !important;
    font-weight: 500 !important;
}

/* Submenu Item Disabled */
.submenu-item-custom.disabled {
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
}

/* Expand Transition */
.expand-enter-active,
.expand-leave-active {
    transition: all 0.3s ease;
}

.expand-enter-from,
.expand-leave-to {
    opacity: 0;
    max-height: 0;
}

.expand-enter-to,
.expand-leave-from {
    opacity: 1;
    max-height: 500px;
}

/* Scrollbar Styling */
.modern-drawer ::-webkit-scrollbar {
    width: 6px;
}

.modern-drawer ::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
}

.modern-drawer ::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
}

.modern-drawer ::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.5);
}

/* Animations */
@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.menu-item, .submenu-item {
    animation: slideInLeft 0.3s ease-out backwards;
}

.menu-item:nth-child(1) { animation-delay: 0.05s; }
.menu-item:nth-child(2) { animation-delay: 0.1s; }
.menu-item:nth-child(3) { animation-delay: 0.15s; }
.menu-item:nth-child(4) { animation-delay: 0.2s; }
.menu-item:nth-child(5) { animation-delay: 0.25s; }
</style>
