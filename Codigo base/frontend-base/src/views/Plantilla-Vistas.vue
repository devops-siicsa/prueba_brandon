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

        <v-app-bar color="#006CA1">
            <v-row>
                <v-col>
                    <v-row>
                        <v-col cols="1">
                            <v-app-bar-nav-icon @click.stop="drawer = !drawer" color="white"
                                style="margin: 0; position: absolute; top: 50%; -ms-transform: translateY(-50%); transform: translateY(-50%);" />
                        </v-col>
                        <v-col>
                            <img src="../assets/Logo.png" height="100" width="120"
                                style="margin: 0; position: absolute; top: 50%; -ms-transform: translateY(-50%); transform: translateY(-50%);" />
                        </v-col>
                    </v-row>
                </v-col>

                <v-col>

                </v-col>

                <v-col>
                    <div
                        style="font-weight: bold; margin: 0; position: absolute; top: 50%; -ms-transform: translateY(-50%); transform: translateY(-50%);">
                        Bienvenido {{ nombreComercial }}
                    </div>
                </v-col>

                <v-col>

                </v-col>

                <v-col>
                    <v-menu v-model="menuAbierto" offset-y location="bottom end" persistent>
                        <template #activator="{ props }">
                            <v-icon color="white" v-bind="props" icon="mdi-account-circle"
                                style="cursor: pointer; margin: 0; position: absolute; top: 50%; transform: translateY(-50%); right: 1%;"
                                size="x-large" />
                        </template>

                        <v-card
                            style="border-radius: 2px; overflow: hidden; min-width: 320px; max-width: 340px; background: #f5f7fa; box-shadow: 0 4px 24px rgba(0,0,0,0.08);"
                            class="pa-4 border-md">
                            <div class="d-flex align-center mb-2">
                                <v-avatar size="64" class="mr-3" style="border: 1px solid #e0e0e0;">
                                    <v-img :src="`${baseURL}images/${comercialId}.jpeg?${Date.now()}`" />
                                </v-avatar>
                                <v-btn color="#006CA1" size="27" icon @click="cambiarImagen()"
                                    class="mb-n14 ml-n8 btn-grow-card" title="Cambiar imagen">
                                    <v-icon size="15">mdi-camera</v-icon>
                                </v-btn>
                                <div>
                                    <div class="font-weight-bold"
                                        style="font-size: 1.15rem; color: #222; max-width: 180px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                                        {{ nombreComercial }}
                                    </div>
                                    <div
                                        style="font-size: 0.95rem; color: #666; max-width: 180px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                                        {{ correoUsuario }}
                                    </div>
                                </div>
                            </div>
                            <v-divider class="mt-3 mb-3"> </v-divider>
                            <div class="d-flex flex-column mt-2">
                                <div class="d-flex align-center  mb-1">
                                    <v-icon class="mr-2" size="small" color="primary">mdi mdi-key-variant</v-icon>
                                    <span class="menu-link mt-2" @click="dialogCambioClave = true">
                                        Cambiar clave
                                    </span>
                                </div>
                                <div class="d-flex align-center">
                                    <v-icon class="mr-2" size="small" color="primary">mdi-logout</v-icon>
                                    <span class="menu-link mt-2" @click="cerrarSesion()">
                                        Cerrar sesión
                                    </span>
                                </div>
                            </div>
                        </v-card>
                    </v-menu>
                </v-col>
            </v-row>
        </v-app-bar>

        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">


            </v-container>
        </v-main>

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
                <v-card-title v-text="mensajeAlert" style="color: black; text-align: center;"></v-card-title>
                <v-btn class="mt-4 mx-auto" @click="cerrarDIV()"
                    style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
            </v-card>
        </v-dialog>
        <!-- Dialog Alertas -->

    </v-app>
</template>

<script>

import axios from 'axios';
import CryptoJS from "crypto-js";

export default {
    data: () => ({
        baseURL: '', // URL base de la API
        comercialId: 0, // ID del usuario comercial
        idCargo: null, // ID del cargo del usuario
        nombreComercial: null, // Nombre del usuario comercial
        correoUsuario: null, // Correo del usuario
        drawer: false, // Estado del menú lateral
        menuAbierto: false, // Estado del menú de usuario

        dialogCambioClave: false,
        claveActual: null,
        nuevaClave: null,
        confirmarClave: null,
        mostrarClaveActual: false,
        mostrarNuevaClave: false,
        mostrarConfirmarClave: false,

        mensajeAlert: null,
        alerta: false,
        ifCargando: false
    }),

    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.comercialId = localStorage.getItem('idUsuario');
        this.idCargo = localStorage.getItem('idCargo');
        this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');;
    },

    methods: {

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
                        this.mensajeAlertLogin = 'Imagen actualizada correctamente, si no puedes vizualizarla, recarga la página.';
                        this.alerta = true;
                        this.ifCargando = false;
                    } catch (error) {
                        console.error('❌ Error al subir imagen:', error);
                    }
                }
            };

            input.click();
        },

        cambiarClave() {
            const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

            if (this.nuevaClave !== this.confirmarClave) {
                this.alerta = true;
                this.mensajeAlertLogin = 'Las claves no coinciden.';
                return;
            } else if (!regex.test(this.nuevaClave)) {
                this.alerta = true;
                this.mensajeAlertLogin = 'La nueva clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.';
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
                            this.mensajeAlertLogin = 'La clave actual ingresada no coincide con el usuario.';
                        } else if (response.data.data[0].respuesta == 'La clave ha sido editada correctamente.') {
                            this.alertLogin = true;
                            this.mensajeAlertLogin = 'La clave ha sido editada correctamente.';
                            this.dialogCambioClave = false;
                            this.claveActual = null;
                            this.nuevaClave = null;
                            this.confirmarClave = null;
                        }
                    })
                    .catch(error => {
                        console.error('Error al cambiar la clave:', error);
                        this.alerta = true;
                        this.mensajeAlertLogin = 'Error al cambiar la clave.';
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

        cerrarSesion() {
            localStorage.removeItem('idUsuario')
            localStorage.removeItem('idCargo')
            localStorage.removeItem('nombreLogin')
            localStorage.removeItem('apellidoLogin')
            localStorage.removeItem('celularLogin')
            localStorage.removeItem('logueado')
            this.$router.push('/')
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
</style>