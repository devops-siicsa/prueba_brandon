<template>
    <v-row>
        <v-col cols="12" md="8">
            <v-card class="border-thin elevation-0 rounded-lg mb-4">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4">
                    Datos del Equipo
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12" md="6">
                            <v-text-field
                                :model-value="equipo.CodigoEquipo"
                                label="Código de Inventario"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'CodigoEquipo', $event)"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-select
                                :model-value="equipo.EstadoEquipoId"
                                label="Estado del Equipo"
                                :items="estados"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'EstadoEquipoId', $event)"
                            ></v-select>
                        </v-col>
                        
                        <v-col cols="12" md="6">
                            <v-select
                                :model-value="equipo.TipoEquipoId"
                                label="Tipo de Equipo"
                                :items="tipos"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'TipoEquipoId', $event)"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-select
                                :model-value="equipo.FabricanteId"
                                label="Fabricante"
                                :items="fabricantes"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'FabricanteId', $event)"
                            ></v-select>
                        </v-col>

                        <v-col cols="12" md="6">
                            <v-text-field
                                :model-value="equipo.Modelo"
                                label="Modelo"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'Modelo', $event)"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field
                                :model-value="equipo.Serial"
                                label="Serial"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                append-inner-icon="mdi-camera"
                                @update:model-value="$emit('update', 'Serial', $event)"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>

            <v-card class="border-thin elevation-0 rounded-lg">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4">
                    Propiedad y Adquisición
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12" md="4">
                            <v-switch
                                :model-value="equipo.EsPropio"
                                label="Equipo Propio"
                                color="primary"
                                :readonly="!isEditing"
                                hide-details
                                inset
                                @update:model-value="$emit('update', 'EsPropio', $event)"
                            ></v-switch>
                        </v-col>
                        
                        <template v-if="!equipo.EsPropio">
                            <v-col cols="12" md="4">
                                <v-text-field
                                    :model-value="equipo.ProveedorAlquiler"
                                    label="Proveedor Alquiler"
                                    variant="outlined"
                                    density="comfortable"
                                    bg-color="grey-lighten-5"
                                    :readonly="!isEditing"
                                    hide-details="auto"
                                    @update:model-value="$emit('update', 'ProveedorAlquiler', $event)"
                                ></v-text-field>
                            </v-col>
                            <v-col cols="12" md="4">
                                <v-text-field
                                    :model-value="equipo.CodigoAlquiler"
                                    label="Código Alquiler"
                                    variant="outlined"
                                    density="comfortable"
                                    bg-color="grey-lighten-5"
                                    :readonly="!isEditing"
                                    hide-details="auto"
                                    @update:model-value="$emit('update', 'CodigoAlquiler', $event)"
                                ></v-text-field>
                            </v-col>
                        </template>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>

        <v-col cols="12" md="4">
             <v-card class="border-thin elevation-0 rounded-lg h-100 d-flex flex-column justify-center align-center bg-grey-lighten-5 border-dashed">
                <v-icon size="64" color="grey-lighten-2" class="mb-4">mdi-image-outline</v-icon>
                <div class="text-body-2 text-grey">Foto del Equipo</div>
                <v-btn v-if="isEditing" variant="text" color="primary" size="small" class="mt-2">Subir Foto</v-btn>
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

const emit = defineEmits(['update'])

const estados = ref([])
const tipos = ref([])
const fabricantes = ref([])

async function loadCatalogs() {
    try {
        const [resEstados, resTipos, resFabs] = await Promise.all([
            axios.get('/api/config/catalogs/estados_equipo', { withCredentials: true }),
            axios.get('/api/config/catalogs/tipos_equipo', { withCredentials: true }),
            axios.get('/api/config/catalogs/fabricantes', { withCredentials: true })
        ])
        estados.value = resEstados.data
        tipos.value = resTipos.data
        fabricantes.value = resFabs.data
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
.border-dashed { border-style: dashed !important; }
</style>
