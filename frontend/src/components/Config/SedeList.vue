<template>
  <v-dialog v-model="dialog" max-width="1100" height="auto" scrollable transition="dialog-bottom-transition">
    <v-card class="rounded-xl elevation-24">
      <!-- Header Personalizado -->
      <div class="px-8 pt-8 pb-4 d-flex justify-space-between align-start">
        <div>
            <h2 class="text-h5 font-weight-bold text-grey-darken-3 mb-1">Mis Sedes</h2>
            <p class="text-body-2 text-grey">Gestiona las sedes y oficinas operativas de tus empresas.</p>
        </div>
        <v-btn icon="mdi-close" variant="text" color="grey" @click="dialog = false"></v-btn>
      </div>

      <v-divider class="mx-8"></v-divider>

      <v-card-text class="px-8 py-6 bg-grey-lighten-5">
        <!-- Barra de Herramientas -->
        <v-row class="mb-6 align-center">
            <v-col cols="12" md="5">
                <v-text-field
                    v-model="search"
                    prepend-inner-icon="mdi-magnify"
                    label="Buscar por nombre o dirección"
                    variant="outlined"
                    density="compact"
                    hide-details
                    bg-color="white"
                    color="primary"
                    class="rounded-lg"
                ></v-text-field>
            </v-col>
            <v-spacer></v-spacer>
            <v-col cols="12" md="auto">
                <v-btn 
                    color="#1e293b" 
                    class="text-white text-capitalize rounded-lg" 
                    height="40"
                    prepend-icon="mdi-plus" 
                    elevation="0"
                    @click="openCreate"
                >
                    Nueva Sede
                </v-btn>
            </v-col>
        </v-row>

        <!-- Estado de Carga -->
        <div v-if="loading" class="d-flex justify-center align-center py-12">
            <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
        </div>

        <!-- Estado Vacío (Empty State) -->
        <div v-else-if="filteredSedes.length === 0" class="d-flex flex-column align-center justify-center py-12 text-center">
            <div class="empty-state-icon mb-6">
                <v-icon size="48" color="primary">mdi-map-marker-off</v-icon>
                <div class="plus-badge">
                    <v-icon size="16" color="white">mdi-plus</v-icon>
                </div>
            </div>
            
            <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">No se encontraron sedes</h3>
            <p class="text-body-2 text-grey mb-8" style="max-width: 400px;">
                No hay sedes registradas que coincidan con tu búsqueda. Agrega una nueva sede para comenzar.
            </p>

            <v-btn 
                color="primary" 
                variant="tonal" 
                class="text-capitalize rounded-lg px-6" 
                height="44"
                prepend-icon="mdi-plus"
                @click="openCreate"
            >
                Agregar mi primera sede
            </v-btn>
        </div>

        <!-- Listado de Sedes (Grid) -->
        <v-row v-else>
            <v-col cols="12" sm="6" md="4" lg="3" v-for="sede in filteredSedes" :key="sede.Id">
                <v-card 
                    hover 
                    @click="openEdit(sede)" 
                    class="company-card border-0 elevation-1 h-100 rounded-lg"
                >
                    <div class="card-status-strip" :class="sede.Activo ? 'bg-success' : 'bg-grey'"></div>
                    <v-card-text class="pa-5">
                        <div class="d-flex justify-space-between align-start mb-3">
                            <div class="text-subtitle-1 font-weight-bold text-grey-darken-3 text-truncate">{{ sede.NombreSede }}</div>
                        </div>
                        
                        <div class="text-caption text-grey-darken-1 mb-2 font-weight-medium d-flex align-center">
                            <v-icon size="small" start class="mr-1">mdi-domain</v-icon>
                            <span class="text-truncate">{{ getCompanyName(sede.EmpresaId) }}</span>
                        </div>

                        <v-divider class="mb-3"></v-divider>

                        <div class="text-caption text-grey mb-1 d-flex align-center">
                            <v-icon size="small" start class="mr-1" color="grey-lighten-1">mdi-map-marker</v-icon>
                            <span class="text-truncate">{{ sede.Direccion || 'Sin dirección' }}</span>
                        </div>
                        
                        <div class="text-caption text-grey d-flex align-center">
                            <v-icon size="small" start class="mr-1" color="grey-lighten-1">mdi-phone</v-icon>
                            {{ sede.Telefono || 'Sin teléfono' }}
                        </div>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

      </v-card-text>
    </v-card>

    <!-- Formulario Modal -->
    <SedeForm 
        v-model="showForm"
        :sede="selectedSede" 
        :companies="companies"
        @save="handleSave" 
    />
  </v-dialog>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'
import SedeForm from './SedeForm.vue'

const props = defineProps({
    modelValue: Boolean
})

const emit = defineEmits(['update:modelValue'])

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

const sedes = ref([])
const companies = ref([])
const search = ref('')
const showForm = ref(false)
const selectedSede = ref(null)
const loading = ref(false)

const filteredSedes = computed(() => {
    if (!search.value) {
        // Filtrar sedes de empresas internas (No clientes)
        return sedes.value.filter(s => {
            const comp = companies.value.find(c => c.Id === s.EmpresaId)
            return comp && !comp.EsCliente
        })
    }
    
    const term = search.value.toLowerCase()
    return sedes.value.filter(s => {
        const comp = companies.value.find(c => c.Id === s.EmpresaId)
        // Debe ser empresa interna Y coincidir con búsqueda
        if (comp && comp.EsCliente) return false
        
        return s.NombreSede.toLowerCase().includes(term) ||
               (s.Direccion && s.Direccion.toLowerCase().includes(term))
    })
})

function getCompanyName(id) {
    const comp = companies.value.find(c => c.Id === id)
    return comp ? comp.RazonSocial : 'Desconocida'
}

async function loadData() {
    loading.value = true
    try {
        const [sedesRes, companiesRes] = await Promise.all([
            axios.get('http://localhost:5000/api/config/sedes', { withCredentials: true }),
            axios.get('http://localhost:5000/api/config/companies', { withCredentials: true })
        ])
        sedes.value = sedesRes.data
        companies.value = companiesRes.data
    } catch (error) {
        console.error("Error cargando datos:", error)
    } finally {
        loading.value = false
    }
}

function openCreate() {
    selectedSede.value = null
    showForm.value = true
}

function openEdit(sede) {
    selectedSede.value = { ...sede } // Copia para editar
    showForm.value = true
}

async function handleSave() {
    await loadData() // Recargar lista
    showForm.value = false
}

watch(dialog, (val) => {
    if (val) loadData()
}, { immediate: true })

onMounted(() => {
    loadData()
})
</script>

<style scoped>
.empty-state-icon {
    width: 96px;
    height: 96px;
    background-color: #e3f2fd;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.plus-badge {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 28px;
    height: 28px;
    background-color: #2196F3;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid white;
}

.company-card {
    transition: all 0.2s ease;
    position: relative;
    overflow: hidden;
    cursor: pointer;
}

.company-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
}

.card-status-strip {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
}
</style>
