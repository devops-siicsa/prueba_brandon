<template>
  <v-card :class="['h-100', 'elevation-0', 'bg-grey-lighten-5', isMobileDevice ? 'rounded-0' : 'rounded-xl']">
    <!-- Header Personalizado -->
    <div class="px-6 py-4 d-flex justify-space-between align-center bg-white border-b">
      <div>
          <h2 class="text-h6 font-weight-bold text-grey-darken-3">Mis Sedes</h2>
          <p class="text-caption text-grey">Gestiona las sedes y oficinas operativas.</p>
      </div>
      <v-btn icon="mdi-close" variant="text" color="grey" @click="$emit('update:modelValue', false)"></v-btn>
    </div>

    <v-card-text class="px-4 py-6 px-md-8">
      <!-- Barra de Herramientas -->
      <v-row class="mb-4 align-center">
          <v-col cols="12" md="5">
              <v-text-field
                  v-model="search"
                  prepend-inner-icon="mdi-magnify"
                  label="Buscar sede"
                  variant="outlined"
                  density="compact"
                  hide-details
                  bg-color="white"
                  class="rounded-lg"
              ></v-text-field>
          </v-col>
          <v-spacer></v-spacer>
          <v-col cols="12" md="auto">
              <v-btn 
                  color="#1e293b" 
                  block
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
              No hay sedes registradas que coincidan con tu búsqueda.
          </p>

          <v-btn 
              color="primary" 
              variant="tonal" 
              class="text-capitalize rounded-lg px-6" 
              height="44"
              prepend-icon="mdi-plus"
              @click="openCreate"
          >
              Agregar sede
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
                  <v-card-text class="pa-4">
                      <div class="d-flex justify-space-between align-start mb-2">
                          <div class="text-subtitle-1 font-weight-bold text-grey-darken-3 text-truncate">{{ sede.NombreSede }}</div>
                      </div>
                      
                      <div class="text-caption text-grey-darken-1 mb-2 font-weight-medium d-flex align-center">
                          <v-icon size="small" start class="mr-1">mdi-domain</v-icon>
                          <span class="text-truncate">{{ getCompanyName(sede.EmpresaId) }}</span>
                      </div>

                      <v-divider class="mb-2 border-opacity-50"></v-divider>

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

    <!-- Formulario de Sede -->
    <SedeForm 
        v-model="showForm" 
        :sede="selectedSede" 
        :companies="companies"
        :isMobileDevice="isMobileDevice"
        @save="handleSave" 
    />
  </v-card>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios'
import SedeForm from './SedeForm.vue'

const props = defineProps({
    modelValue: Boolean,
    isMobileDevice: Boolean
})

const emit = defineEmits(['update:modelValue'])

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
            axios.get('/api/config/sedes', { withCredentials: true }),
            axios.get('/api/config/companies', { withCredentials: true })
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

// Cargar datos al montar
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
