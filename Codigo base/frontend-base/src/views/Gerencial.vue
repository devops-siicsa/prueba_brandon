<template>
    <v-app>
        <AppHeader :imagenComercial="imagenComercial" />

        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
              
            </v-container>
        </v-main>

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
        listaUsuarios: [],
    }),

    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.comercialId = localStorage.getItem('idUsuario');
        this.idCargo = localStorage.getItem('idCargo');
        this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');;
        this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?${Date.now()}`;
        this.obtenerUsuarios();
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
</style>