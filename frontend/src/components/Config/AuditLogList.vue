<template>
    <v-card class="h-100 d-flex flex-column bg-grey-lighten-5 rounded-xl">
        <!-- Header Premium -->
        <div :class="[isMobileApp ? 'px-4 py-4' : 'px-8 pt-6 pb-6', 'bg-white elevation-0 border-bottom']">
            <div class="d-flex align-center justify-space-between">
                <div class="d-flex align-center">
                    <div class="header-icon-box mr-4 bg-orange-lighten-5" :style="isMobileApp ? 'width: 40px; height: 40px;' : ''">
                        <v-icon color="orange-darken-2" :size="isMobileApp ? 24 : 28">mdi-file-eye</v-icon>
                    </div>
                    <div>
                        <h2 :class="[isMobileApp ? 'text-subtitle-1' : 'text-h6', 'font-weight-bold text-grey-darken-3 mb-0']">Log de Auditoría</h2>
                        <p class="text-caption text-grey">Historial detallado de cambios en el sistema.</p>
                    </div>
                </div>

                <div>
                    <v-btn 
                        icon="mdi-broom" 
                        variant="text" 
                        color="blue-grey" 
                        class="mr-2" 
                        @click="clearFilters"
                        v-tooltip:bottom="'Limpiar Filtros'"
                    ></v-btn>
                    <v-btn icon="mdi-close" variant="text" color="grey" @click="$emit('update:modelValue', false)"></v-btn>
                </div>
            </div>
        </div>

        <!-- Content -->
        <v-card-text class="pa-0 flex-grow-1 overflow-auto">
            <v-container fluid :class="isMobileApp ? 'pa-4' : 'pa-8'">
                <!-- Filters Section -->
                <div class="mb-6">
                    <v-row dense>
                        <v-col cols="12" sm="6" md="3">
                            <v-autocomplete
                                v-model="filters.table"
                                label="Tabla"
                                :items="filterOptions.tables"
                                prepend-inner-icon="mdi-table"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                clearable
                                @update:model-value="debouncedFetch"
                            ></v-autocomplete>
                        </v-col>
                        <v-col cols="12" sm="6" md="3">
                            <v-select
                                v-model="filters.action"
                                label="Acción"
                                :items="['LOGIN', 'CREAR', 'EDITAR', 'ELIMINAR', 'LOGOUT']"
                                prepend-inner-icon="mdi-gesture-tap"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                clearable
                                @update:model-value="fetchLogs"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" sm="6" md="3">
                            <v-text-field
                                v-model="filters.dateFrom"
                                label="Desde"
                                type="date"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                @update:model-value="fetchLogs"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="3">
                            <v-text-field
                                v-model="filters.dateTo"
                                label="Hasta"
                                type="date"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                @update:model-value="fetchLogs"
                            ></v-text-field>
                        </v-col>
                        <!-- Advanced Filters -->
                        <v-col cols="12" sm="6" md="3">
                            <v-autocomplete
                                v-model="filters.userName"
                                label="Usuario (Nombre)"
                                :items="filterOptions.users"
                                prepend-inner-icon="mdi-account"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                clearable
                                @update:model-value="debouncedFetch"
                            ></v-autocomplete>
                        </v-col>
                        <v-col cols="12" sm="6" md="3">
                            <v-autocomplete
                                v-model="filters.userDoc"
                                label="Usuario (Doc)"
                                :items="filterOptions.userDocs"
                                prepend-inner-icon="mdi-card-account-details"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                clearable
                                @update:model-value="debouncedFetch"
                            ></v-autocomplete>
                        </v-col>
                        <v-col cols="12" sm="6" md="3">
                            <v-autocomplete
                                v-model="filters.companyName"
                                label="Empresa"
                                :items="filterOptions.companies"
                                prepend-inner-icon="mdi-domain"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                clearable
                                @update:model-value="debouncedFetch"
                            ></v-autocomplete>
                        </v-col>
                        <v-col cols="12" sm="6" md="3">
                            <v-autocomplete
                                v-model="filters.companyNit"
                                label="NIT Empresa"
                                :items="filterOptions.companyNits"
                                prepend-inner-icon="mdi-identifier"
                                density="compact"
                                variant="outlined"
                                hide-details
                                bg-color="white"
                                class="rounded-lg"
                                clearable
                                @update:model-value="debouncedFetch"
                            ></v-autocomplete>
                        </v-col>
                    </v-row>
                </div>

                <!-- Table Card (Desktop) -->
                <v-card v-if="!isMobileApp" class="rounded-lg border-thin elevation-0 overflow-hidden">
                    <v-data-table-server
                        v-model:items-per-page="itemsPerPage"
                        v-model:page="currentPage"
                        :headers="headers"
                        :items="logs"
                        :items-length="totalItems"
                        :loading="loading"
                        class="header-bg"
                        hover
                        density="comfortable"
                        @update:options="loadItems"
                    >
                        <template v-slot:item.Accion="{ item }">
                            <v-chip
                                size="small"
                                :color="getActionColor(item.Accion)"
                                class="font-weight-bold"
                                variant="flat"
                            >
                                {{ item.Accion }}
                            </v-chip>
                        </template>

                        <template v-slot:item.Fecha="{ item }">
                            <span class="text-body-2 text-grey-darken-3">{{ formatDate(item.Fecha) }}</span>
                        </template>
                        
                        <template v-slot:item.Usuario="{ item }">
                            <div class="d-flex flex-column">
                                <span class="font-weight-medium text-grey-darken-3">{{ item.Usuario }}</span>
                                <span v-if="item.UsuarioDocumento" class="text-caption text-grey">{{ item.UsuarioDocumento }}</span>
                            </div>
                        </template>

                        <template v-slot:item.Empresa="{ item }">
                            <div class="d-flex flex-column">
                                <span class="font-weight-medium text-grey-darken-3">{{ item.Empresa }}</span>
                                <span v-if="item.EmpresaNIT" class="text-caption text-grey">NIT: {{ item.EmpresaNIT }}</span>
                            </div>
                        </template>

                        <template v-slot:item.Sede="{ item }">
                            <span class="text-body-2 text-grey-darken-3">{{ item.Sede }}</span>
                        </template>

                        <template v-slot:item.Detalle="{ item }">
                            <v-btn
                                size="small"
                                variant="tonal"
                                color="primary"
                                class="text-capitalize"
                                @click="showDetail(item)"
                            >
                                Ver Detalle
                            </v-btn>
                        </template>
                    </v-data-table-server>
                </v-card>

                <!-- Mobile View (Iterator) -->
                <div v-else>
                     <!-- Estado Vacío Móvil -->
                    <div v-if="logs.length === 0 && !loading" class="d-flex flex-column align-center justify-center py-12 text-center">
                        <div class="empty-state-icon mb-6" style="width: 72px; height: 72px; background-color: #fff3e0; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                            <v-icon size="36" color="orange-lighten-2">mdi-file-eye-off</v-icon>
                        </div>
                        <h3 class="text-subtitle-1 font-weight-bold text-grey-darken-3 mb-2">No se encontraron registros</h3>
                        <p class="text-caption text-grey">Intenta ajustar los filtros de búsqueda.</p>
                    </div>

                    <div v-else>
                        <v-row dense>
                            <v-col cols="12" v-for="item in logs" :key="item.Id">
                                <v-card class="border-thin elevation-0 rounded-lg pa-3">
                                    <div class="d-flex justify-space-between align-start mb-2">
                                        <v-chip size="x-small" :color="getActionColor(item.Accion)" variant="flat" class="font-weight-bold">
                                            {{ item.Accion }}
                                        </v-chip>
                                        <span class="text-caption text-grey">{{ formatDate(item.Fecha) }}</span>
                                    </div>
                                    
                                    <div class="mb-2">
                                        <div class="d-flex align-center mb-1">
                                            <v-icon size="14" color="grey" class="mr-1">mdi-account</v-icon>
                                            <span class="text-body-2 font-weight-medium text-grey-darken-3">{{ item.Usuario }}</span>
                                        </div>
                                        <div class="d-flex align-center mb-1">
                                            <v-icon size="14" color="grey" class="mr-1">mdi-domain</v-icon>
                                            <span class="text-caption text-grey-darken-2">{{ item.Empresa }}</span>
                                        </div>
                                        <div class="d-flex align-center">
                                            <v-icon size="14" color="grey" class="mr-1">mdi-table</v-icon>
                                            <span class="text-caption text-grey-darken-2">{{ item.Tabla }}</span>
                                        </div>
                                    </div>

                                    <v-btn
                                        block
                                        size="small"
                                        variant="tonal"
                                        color="blue-grey"
                                        class="text-capitalize mt-2"
                                        @click="showDetail(item)"
                                    >
                                        Ver Detalle
                                    </v-btn>
                                </v-card>
                            </v-col>
                        </v-row>
                        
                        <!-- Paginación Móvil -->
                        <div class="d-flex justify-center mt-4">
                            <v-pagination
                                v-model="currentPage"
                                :length="totalPages"
                                :total-visible="4"
                                density="comfortable"
                                active-color="primary"
                                @update:model-value="fetchLogs"
                            ></v-pagination>
                        </div>
                    </div>
                </div>
            </v-container>
        </v-card-text>

        <!-- Dialogo de Detalle (Estilo Premium) -->
        <v-dialog v-model="detailDialog" :fullscreen="isMobileApp" :max-width="isMobileApp ? '100%' : '600'">
            <v-card class="rounded-xl" :height="isMobileApp ? '100%' : 'auto'">
                <v-card-title :class="[isMobileApp ? 'px-4 py-3' : 'px-6 pt-6 pb-4', 'd-flex align-start justify-space-between bg-white']">
                    <div>
                        <span :class="[isMobileApp ? 'text-subtitle-1' : 'text-h6', 'font-weight-bold text-blue-grey-darken-4']">
                            Detalle del Cambio
                        </span>
                        <p class="text-caption text-grey mt-1">Información completa de la auditoría.</p>
                    </div>
                    <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="detailDialog = false"></v-btn>
                </v-card-title>
                
                <v-divider :class="[isMobileApp ? 'mx-4' : 'mx-6', 'opacity-10 mb-4']"></v-divider>

                <v-card-text :class="[isMobileApp ? 'px-4' : 'px-6', 'py-0 mb-6']">
                    <div v-if="selectedItem">
                        <div class="d-flex mb-6 bg-grey-lighten-5 pa-4 rounded-lg border-thin flex-wrap">
                            <div class="w-50 mb-2 mb-sm-0">
                                <div class="text-caption font-weight-bold text-grey mb-1">USUARIO</div>
                                <div class="font-weight-bold text-body-2">{{ selectedItem.Usuario }}</div>
                            </div>
                            <div class="w-50 mb-2 mb-sm-0">
                                <div class="text-caption font-weight-bold text-grey mb-1">FECHA</div>
                                <div class="font-weight-bold text-body-2">{{ formatDate(selectedItem.Fecha) }}</div>
                            </div>
                        </div>
                        <div class="d-flex mb-6">
                            <div class="w-50">
                                <div class="text-caption font-weight-bold text-grey mb-1">TABLA AFECTADA</div>
                                <div class="font-weight-bold text-body-1">{{ selectedItem.Tabla }}</div>
                            </div>
                            <div class="w-50">
                                <div class="text-caption font-weight-bold text-grey mb-1">ACCIÓN</div>
                                <v-chip size="small" :color="getActionColor(selectedItem.Accion)" variant="flat" class="font-weight-bold">
                                    {{ selectedItem.Accion }}
                                </v-chip>
                            </div>
                        </div>
                        
                        <v-divider class="mb-4 border-dashed"></v-divider>
                        
                        <div class="text-subtitle-2 font-weight-bold text-blue-grey-darken-3 mb-3">Cambios Registrados</div>
                        <v-code class="d-block pa-4 bg-blue-grey-lighten-5 text-blue-grey-darken-4 rounded-lg overflow-auto border-thin" style="max-height: 300px; font-size: 0.85rem;">
                            {{ formatDetail(selectedItem.Detalle) }}
                        </v-code>
                    </div>
                </v-card-text>
                <v-card-actions :class="[isMobileApp ? 'px-4 pb-4' : 'px-6 pb-6', 'pt-0']">
                    <v-spacer></v-spacer>
                    <v-btn 
                        color="#1e293b" 
                        variant="flat" 
                        class="text-white text-capitalize rounded-lg px-6"
                        height="44"
                        @click="detailDialog = false"
                        :block="isMobileApp"
                    >
                        Cerrar
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-card>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useAuthStore } from '@/stores/auth'
import axios from 'axios'
import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    modelValue: Boolean
})

const { isMobileApp } = useMobileDetection()

const emit = defineEmits(['update:modelValue'])

const authStore = useAuthStore()
const loading = ref(false)
const logs = ref([])
const totalItems = ref(0)
const totalPages = ref(0)
const currentPage = ref(1)
const itemsPerPage = ref(10)

const filters = ref({
    table: null,
    action: null,
    dateFrom: null,
    dateTo: null,
    userName: null,
    userDoc: null,
    companyName: null,
    companyNit: null
})

const filterOptions = ref({
    tables: [],
    users: [],
    userDocs: [],
    companies: [],
    companyNits: []
})

const headers = [
    { title: 'Fecha', key: 'Fecha', align: 'start', width: '180px' },
    { title: 'Usuario', key: 'Usuario', align: 'start' },
    { title: 'Empresa', key: 'Empresa', align: 'start' },
    { title: 'Sede', key: 'Sede', align: 'start' },
    { title: 'Acción', key: 'Accion', align: 'center', width: '100px' },
    { title: 'Tabla', key: 'Tabla', align: 'start' },
    { title: 'Detalle', key: 'Detalle', align: 'center', sortable: false, width: '120px' },
]

const detailDialog = ref(false)
const selectedItem = ref(null)

// Debounce simple
let timeout = null
const debouncedFetch = () => {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
        currentPage.value = 1
        // No llamamos fetchLogs directamente, sino que forzamos la actualización de la tabla
        // Pero como v-data-table-server reacciona a cambios, fetchLogs se llamará si cambiamos params
        fetchLogs()
    }, 500)
}

function loadItems({ page, itemsPerPage: ipp }) {
    currentPage.value = page
    itemsPerPage.value = ipp
    fetchLogs()
}

async function fetchFilterOptions() {
    try {
        const response = await axios.get('/api/audit/filters', {
            withCredentials: true
        })
        filterOptions.value = {
            tables: response.data.tables,
            users: response.data.users,
            userDocs: response.data.user_docs,
            companies: response.data.companies,
            companyNits: response.data.company_nits
        }
    } catch (error) {
        console.error('Error fetching filter options:', error)
    }
}

function clearFilters() {
    filters.value = {
        table: null,
        action: null,
        dateFrom: null,
        dateTo: null,
        userName: null,
        userDoc: null,
        companyName: null,
        companyNit: null
    }
    fetchLogs()
}

async function fetchLogs() {
    loading.value = true
    try {
        const params = {
            page: currentPage.value,
            per_page: itemsPerPage.value,
            table: filters.value.table,
            action: filters.value.action,
            dateFrom: filters.value.dateFrom,
            dateTo: filters.value.dateTo,
            userName: filters.value.userName,
            userDoc: filters.value.userDoc,
            companyName: filters.value.companyName,
            companyNit: filters.value.companyNit
        }
        
        // Limpiar nulos/vacíos
        Object.keys(params).forEach(key => {
            if (params[key] === null || params[key] === '') delete params[key]
        })

        const url = '/api/audit/logs'
        
        const response = await axios.get(url, {
            params,
            withCredentials: true
        })

        logs.value = response.data.logs
        totalItems.value = response.data.total
        totalPages.value = response.data.pages
        currentPage.value = response.data.current_page
    } catch (error) {
        console.error('Error fetching audit logs:', error)
    } finally {
        loading.value = false
    }
}

function getActionColor(action) {
    switch (action) {
        case 'CREAR': return 'success'
        case 'EDITAR': return 'info'
        case 'ELIMINAR': return 'error'
        default: return 'grey'
    }
}

function formatDate(dateString) {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleString('es-CO')
}

function showDetail(item) {
    selectedItem.value = item
    detailDialog.value = true
}

function formatDetail(detail) {
    try {
        const parsed = JSON.parse(detail)
        return JSON.stringify(parsed, null, 2)
    } catch (e) {
        return detail
    }
}

// Watch para recargar al abrir el diálogo
watch(() => props.modelValue, (val) => {
    if (val) {
        console.log('AuditLogDialog opened. Fetching logs...')
        fetchLogs()
        fetchFilterOptions()
    }
})

onMounted(() => {
    // Si ya está visible al montar (raro en dialog, pero posible)
    if (props.modelValue) {
        fetchLogs()
        fetchFilterOptions()
    }
})
</script>

<style scoped>
.header-bg {
    background-color: white;
}
.header-icon-box {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.border-bottom { border-bottom: 1px solid rgba(0,0,0,0.05); }
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }
.border-dashed { border-style: dashed !important; border-color: rgba(0,0,0,0.1) !important; }

.v-data-table :deep(th) {
    font-weight: bold !important;
    color: #424242 !important;
    text-transform: uppercase;
    font-size: 0.75rem;
}
</style>
