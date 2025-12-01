<template>
    <v-row>
        <v-col cols="12" md="6">
            <v-card class="border-thin elevation-0 rounded-lg mb-4">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4">
                    Sistema Operativo
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12">
                            <v-select
                                :model-value="equipo.SistemaOperativoId"
                                label="Sistema Operativo"
                                :items="sistemasOperativos"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'SistemaOperativoId', $event)"
                            ></v-select>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                                :model-value="equipo.LicenciaSO"
                                label="Licencia / Serial SO"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'LicenciaSO', $event)"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>

        <v-col cols="12" md="6">
            <v-card class="border-thin elevation-0 rounded-lg mb-4">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4">
                    Ofimática
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12">
                            <v-select
                                :model-value="equipo.OfimaticaId"
                                label="Suite Ofimática"
                                :items="ofimaticas"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'OfimaticaId', $event)"
                            ></v-select>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                                :model-value="equipo.LicenciaOfimatica"
                                label="Licencia / Cuenta"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'LicenciaOfimatica', $event)"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>

        <v-col cols="12">
            <v-card class="border-thin elevation-0 rounded-lg mb-4">
                <v-card-title class="text-subtitle-1 font-weight-bold text-grey-darken-3 px-4 pt-4">
                    Red y Seguridad
                </v-card-title>
                <v-card-text class="pa-4">
                    <v-row dense>
                        <v-col cols="12" md="4">
                            <v-text-field
                                :model-value="equipo.NombreEnRed"
                                label="Nombre en Red (Hostname)"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'NombreEnRed', $event)"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select
                                :model-value="equipo.EquipoPertenece"
                                label="Pertenece a"
                                :items="['Dominio', 'Grupo de Trabajo']"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'EquipoPertenece', $event)"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select
                                :model-value="equipo.AntivirusId"
                                label="Antivirus"
                                :items="antivirus"
                                item-title="Nombre"
                                item-value="Id"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-5"
                                :readonly="!isEditing"
                                hide-details="auto"
                                class="mb-3"
                                @update:model-value="$emit('update', 'AntivirusId', $event)"
                            ></v-select>
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

const sistemasOperativos = ref([])
const ofimaticas = ref([])
const antivirus = ref([])

async function loadCatalogs() {
    try {
        const [resSO, resOfi, resAV] = await Promise.all([
            axios.get('/api/config/catalogs/sistemas_operativos', { withCredentials: true }),
            axios.get('/api/config/catalogs/ofimaticas', { withCredentials: true }),
            axios.get('/api/config/catalogs/antivirus', { withCredentials: true })
        ])
        sistemasOperativos.value = resSO.data
        ofimaticas.value = resOfi.data
        antivirus.value = resAV.data
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
