<template>
    <v-row>
        <v-col cols="12" md="6">
            <v-card class="border-thin elevation-0 rounded-lg h-100">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4">
                    Información del Usuario
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12">
                            <v-text-field
                                :model-value="equipo.UsuarioNombre"
                                label="Usuario Asignado"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field
                                :model-value="equipo.Cargo"
                                label="Cargo"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field
                                :model-value="equipo.Area"
                                label="Área"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                                :model-value="equipo.Correo"
                                label="Correo Electrónico"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                prepend-inner-icon="mdi-email"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field
                                :model-value="equipo.Telefono"
                                label="Teléfono"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                prepend-inner-icon="mdi-phone"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>

        <v-col cols="12" md="6">
            <v-card class="border-thin elevation-0 rounded-lg h-100">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4">
                    Ubicación
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12">
                            <v-select
                                :model-value="equipo.SedeId"
                                label="Sede"
                                :items="sedes"
                                item-title="NombreSede"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                            ></v-select>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                                :model-value="equipo.Ciudad"
                                label="Ciudad"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-4"
                                readonly
                                hide-details="auto"
                                hint="Automático según la sede"
                                persistent-hint
                            ></v-text-field>
                        </v-col>
                    </v-row>
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

const emit = defineEmits(['update'])
const sedes = ref([])

async function loadSedes() {
    try {
        // TODO: Filter by company if needed
        const res = await axios.get('/api/config/sedes', { withCredentials: true })
        sedes.value = res.data
    } catch (e) {
        console.error(e)
    }
}

onMounted(() => {
    loadSedes()
})
</script>

<style scoped>
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }
</style>
