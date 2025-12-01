<template>
  <v-container fluid class="bg-grey-lighten-5 fill-height align-start">
    <div class="w-100">
        <!-- Header -->
        <div class="mb-6">
            <div class="d-flex align-center mb-2">
                <v-btn icon="mdi-arrow-left" variant="text" size="small" class="mr-2" @click="goBack"></v-btn>
                <div class="text-caption text-grey">
                    <v-icon size="small" class="mr-1">mdi-home</v-icon> / Inventario / Equipos / Detalle
                </div>
            </div>
            
            <div class="d-flex flex-column flex-md-row justify-space-between align-md-center">
                <div>
                    <div class="d-flex align-center">
                        <h1 class="text-h5 text-md-h4 font-weight-bold text-primary mb-1 mr-3">
                            {{ equipo.CodigoEquipo || 'Cargando...' }}
                        </h1>
                        <v-chip v-if="equipo.Estado" size="small" color="emerald" class="bg-green-lighten-5 text-green-darken-1 font-weight-bold">
                            {{ equipo.Estado }}
                        </v-chip>
                    </div>
                    <p class="text-body-2 text-grey-darken-1">
                        {{ equipo.Modelo }} - {{ equipo.Serial }}
                    </p>
                </div>
                
                <div class="mt-4 mt-md-0 d-flex gap-2">
                    <v-btn 
                        :color="isEditing ? 'error' : 'primary'" 
                        variant="flat" 
                        class="text-capitalize rounded-lg"
                        prepend-icon="mdi-pencil"
                        @click="toggleEdit"
                    >
                        {{ isEditing ? 'Cancelar Edición' : 'Editar Equipo' }}
                    </v-btn>
                    <v-btn 
                        v-if="isEditing"
                        color="success" 
                        variant="flat" 
                        class="text-capitalize rounded-lg"
                        prepend-icon="mdi-content-save"
                        @click="saveChanges"
                        :loading="saving"
                    >
                        Guardar Cambios
                    </v-btn>
                </div>
            </div>
        </div>

        <!-- Tabs -->
        <v-card class="rounded-xl border-0 elevation-1 overflow-hidden">
            <v-tabs 
                v-model="activeTab" 
                color="primary" 
                bg-color="white" 
                :show-arrows="isMobileDevice"
                :grow="!isMobileDevice"
                :density="isMobileDevice ? 'compact' : 'default'"
            >
                <v-tab value="user" class="text-capitalize"><v-icon start>mdi-account</v-icon> {{ isMobileDevice ? '' : 'Usuario' }}</v-tab>
                <v-tab value="general" class="text-capitalize"><v-icon start>mdi-laptop</v-icon> {{ isMobileDevice ? '' : 'Equipo' }}</v-tab>
                <v-tab value="hardware" class="text-capitalize"><v-icon start>mdi-cpu-64-bit</v-icon> {{ isMobileDevice ? '' : 'Hardware' }}</v-tab>
                <v-tab value="software" class="text-capitalize"><v-icon start>mdi-microsoft-windows</v-icon> {{ isMobileDevice ? '' : 'Software' }}</v-tab>
                <v-tab value="apps" class="text-capitalize"><v-icon start>mdi-apps</v-icon> {{ isMobileDevice ? '' : 'Aplicativos' }}</v-tab>
                <v-tab value="files" class="text-capitalize"><v-icon start>mdi-paperclip</v-icon> {{ isMobileDevice ? '' : 'Adjuntos' }}</v-tab>
                <v-tab value="history" class="text-capitalize"><v-icon start>mdi-history</v-icon> {{ isMobileDevice ? '' : 'Historial' }}</v-tab>
            </v-tabs>

            <v-divider></v-divider>

            <v-card-text :class="isMobileDevice ? 'pa-3' : 'pa-6'" style="min-height: 500px;">
                <v-window v-model="activeTab">
                    <v-window-item value="user">
                        <UserInfoTab :equipo="equipo" :is-editing="isEditing" :is-mobile="isMobileDevice" @update="updateEquipoField" />
                    </v-window-item>
                    
                    <v-window-item value="general">
                        <GeneralInfoTab :equipo="equipo" :is-editing="isEditing" :is-mobile="isMobileDevice" @update="updateEquipoField" />
                    </v-window-item>

                    <v-window-item value="hardware">
                        <HardwareTab :equipo="equipo" :is-editing="isEditing" :is-mobile="isMobileDevice" />
                    </v-window-item>

                    <v-window-item value="software">
                        <SoftwareTab :equipo="equipo" :is-editing="isEditing" :is-mobile="isMobileDevice" @update="updateEquipoField" />
                    </v-window-item>
                    
                    <v-window-item value="apps">
                        <div class="text-center py-12 text-grey">Módulo de Aplicativos en construcción</div>
                    </v-window-item>

                    <v-window-item value="files">
                        <div class="text-center py-12 text-grey">Módulo de Adjuntos en construcción</div>
                    </v-window-item>

                    <v-window-item value="history">
                        <div class="text-center py-12 text-grey">Módulo de Historial en construcción</div>
                    </v-window-item>
                </v-window>
            </v-card-text>
        </v-card>
    </div>
  </v-container>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useDisplay } from 'vuetify'
import axios from 'axios'
import UserInfoTab from '@/components/Inventory/Tabs/UserInfoTab.vue'
import GeneralInfoTab from '@/components/Inventory/Tabs/GeneralInfoTab.vue'
import HardwareTab from '@/components/Inventory/Tabs/HardwareTab.vue'
import SoftwareTab from '@/components/Inventory/Tabs/SoftwareTab.vue'

const { mobile } = useDisplay()
const isMobileDevice = computed(() => mobile.value)

const route = useRoute()
const router = useRouter()
const activeTab = ref('user')
const isEditing = ref(false)
const saving = ref(false)
const equipo = ref({})

const equipoId = computed(() => route.params.id)

async function loadEquipo() {
    if (!equipoId.value) return
    try {
        const res = await axios.get(`/api/inventory/equipos/${equipoId.value}`, { withCredentials: true })
        equipo.value = res.data
    } catch (e) {
        console.error("Error loading equipo", e)
    }
}

function toggleEdit() {
    if (isEditing.value) {
        // Cancelar: Recargar datos originales
        loadEquipo()
    }
    isEditing.value = !isEditing.value
}

function updateEquipoField(field, value) {
    equipo.value[field] = value
}

async function saveChanges() {
    saving.value = true
    try {
        await axios.put(`/api/inventory/equipos/${equipoId.value}`, equipo.value, { withCredentials: true })
        isEditing.value = false
        // TODO: Show success notification
    } catch (e) {
        console.error("Error saving", e)
        alert("Error al guardar cambios")
    } finally {
        saving.value = false
    }
}

function goBack() {
    router.back()
}

onMounted(() => {
    loadEquipo()
})
</script>

<style scoped>
.gap-2 { gap: 8px; }
</style>
