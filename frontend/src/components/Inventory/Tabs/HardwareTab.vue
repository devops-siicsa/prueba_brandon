<template>
    <v-row>
        <!-- PROCESADOR -->
        <v-col cols="12">
            <v-card class="border-thin elevation-0 rounded-lg mb-4">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4 d-flex align-center">
                    <v-icon start color="blue-grey" size="small">mdi-cpu-64-bit</v-icon>
                    Procesador
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12" md="4">
                            <v-select
                                label="Marca"
                                :items="marcasProcesador"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select
                                label="Tipo / Familia"
                                :items="tiposProcesador"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select
                                label="Generación"
                                :items="generacionesProcesador"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                            ></v-select>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>

        <!-- RAM -->
        <v-col cols="12" md="6">
            <v-card class="border-thin elevation-0 rounded-lg mb-4 h-100">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4 d-flex align-center justify-space-between">
                    <div class="d-flex align-center">
                        <v-icon start color="teal" size="small">mdi-memory</v-icon>
                        Memoria RAM
                    </div>
                    <v-btn v-if="isEditing" size="x-small" variant="text" color="primary" prepend-icon="mdi-plus">Slot</v-btn>
                </v-card-title>
                <v-card-text class="pa-4">
                    <!-- Lista de Slots RAM -->
                    <div v-for="(slot, index) in ramSlots" :key="index" class="mb-3 pa-3 bg-grey-lighten-5 rounded border-thin">
                        <div class="d-flex justify-space-between mb-2">
                            <span class="text-caption font-weight-bold text-grey">Slot {{ index + 1 }}</span>
                            <v-icon v-if="isEditing" size="small" color="error" class="cursor-pointer">mdi-delete</v-icon>
                        </div>
                        <v-row dense>
                            <v-col cols="4">
                                <v-select density="compact" label="Tipo" variant="outlined" hide-details bg-color="white"></v-select>
                            </v-col>
                            <v-col cols="4">
                                <v-select density="compact" label="Capacidad" variant="outlined" hide-details bg-color="white"></v-select>
                            </v-col>
                            <v-col cols="4">
                                <v-select density="compact" label="Bus" variant="outlined" hide-details bg-color="white"></v-select>
                            </v-col>
                        </v-row>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>

        <!-- ALMACENAMIENTO -->
        <v-col cols="12" md="6">
            <v-card class="border-thin elevation-0 rounded-lg mb-4 h-100">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4 d-flex align-center justify-space-between">
                    <div class="d-flex align-center">
                        <v-icon start color="indigo" size="small">mdi-harddisk</v-icon>
                        Almacenamiento
                    </div>
                    <v-btn v-if="isEditing" size="x-small" variant="text" color="primary" prepend-icon="mdi-plus">Disco</v-btn>
                </v-card-title>
                <v-card-text class="pa-4">
                    <!-- Lista de Discos -->
                    <div v-for="(disk, index) in storageSlots" :key="index" class="mb-3 pa-3 bg-grey-lighten-5 rounded border-thin">
                        <div class="d-flex justify-space-between mb-2">
                            <span class="text-caption font-weight-bold text-grey">Disco {{ index + 1 }}</span>
                            <v-icon v-if="isEditing" size="small" color="error" class="cursor-pointer">mdi-delete</v-icon>
                        </div>
                        <v-row dense>
                            <v-col cols="6">
                                <v-select density="compact" label="Tipo" variant="outlined" hide-details bg-color="white"></v-select>
                            </v-col>
                            <v-col cols="6">
                                <v-select density="compact" label="Capacidad" variant="outlined" hide-details bg-color="white"></v-select>
                            </v-col>
                        </v-row>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean
})

const marcasProcesador = ref([])
const tiposProcesador = ref([])
const generacionesProcesador = ref([])

const ramSlots = ref([{}]) // Mock initial slot
const storageSlots = ref([{}]) // Mock initial slot

async function loadCatalogs() {
    try {
        const [resM, resT, resG] = await Promise.all([
            axios.get('/api/config/catalogs/marcas_procesador', { withCredentials: true }),
            axios.get('/api/config/catalogs/tipos_procesador', { withCredentials: true }),
            axios.get('/api/config/catalogs/generaciones_procesador', { withCredentials: true })
        ])
        marcasProcesador.value = resM.data
        tiposProcesador.value = resT.data
        generacionesProcesador.value = resG.data
    } catch (e) {
        console.error(e)
    }
}

onMounted(() => {
    loadCatalogs()
})
</script>

<style scoped>
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }
</style>
