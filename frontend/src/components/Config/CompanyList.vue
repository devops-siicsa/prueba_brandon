<template>
  <v-card :class="['h-100', 'elevation-0', 'bg-grey-lighten-5', isMobileDevice ? 'rounded-0' : 'rounded-xl']">
    <!-- Header Personalizado -->
    <div :class="[isMobileDevice ? 'px-4 py-3' : 'px-6 py-4', 'd-flex justify-space-between align-center bg-white border-b']">
      <div>
          <h2 :class="[isMobileDevice ? 'text-subtitle-1' : 'text-h6', 'font-weight-bold text-grey-darken-3']">Mis Empresas</h2>
          <p class="text-caption text-grey">Gestiona el listado de empresas registradas.</p>
      </div>
      <v-btn icon="mdi-close" variant="text" color="grey" @click="$emit('update:modelValue', false)"></v-btn>
    </div>

    <v-card-text :class="[isMobileDevice ? 'px-3 py-4' : 'px-4 py-6 px-md-8']">
      <!-- Barra de Herramientas -->
      <v-row class="mb-4 align-center" :dense="isMobileDevice">
          <v-col cols="12" md="5">
              <v-text-field
                  v-model="search"
                  prepend-inner-icon="mdi-magnify"
                  label="Buscar empresa"
                  variant="outlined"
                  density="compact"
                  hide-details
                  bg-color="white"
                  class="rounded-lg"
              ></v-text-field>
          </v-col>
          <v-col cols="12" md="3">
              <v-select
                  v-model="statusFilter"
                  :items="[{title: 'Todos', value: 'all'}, {title: 'Activos', value: 'active'}, {title: 'Inactivos', value: 'inactive'}]"
                  label="Estado"
                  variant="outlined"
                  density="compact"
                  hide-details
                  bg-color="white"
                  class="rounded-lg"
              ></v-select>
          </v-col>
          <v-spacer v-if="!isMobileDevice"></v-spacer>
          <v-col cols="12" md="auto">
              <v-btn 
                  color="#1e293b" 
                  block
                  class="text-white text-capitalize rounded-lg" 
                  height="40"
                  prepend-icon="mdi-plus" 
                  elevation="0"
                  @click="openForm(null)"
              >
                  Nueva Empresa
              </v-btn>
          </v-col>
      </v-row>

      <!-- Estado de Carga -->
      <div v-if="loading" class="d-flex justify-center align-center py-12">
          <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
      </div>

      <!-- Estado Vacío (Empty State) -->
      <div v-else-if="filteredCompanies.length === 0" class="d-flex flex-column align-center justify-center py-12 text-center">
          <div class="empty-state-icon mb-6" :style="isMobileDevice ? 'width: 72px; height: 72px;' : ''">
              <v-icon :size="isMobileDevice ? 36 : 48" color="primary">mdi-briefcase-plus-outline</v-icon>
              <div class="plus-badge" :style="isMobileDevice ? 'width: 24px; height: 24px;' : ''">
                  <v-icon :size="isMobileDevice ? 14 : 16" color="white">mdi-plus</v-icon>
              </div>
          </div>
          
          <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">No se encontraron empresas</h3>
          <p class="text-body-2 text-grey mb-8" style="max-width: 400px;">
              Aún no has registrado ninguna empresa.
          </p>

          <v-btn 
              color="primary" 
              variant="tonal" 
              class="text-capitalize rounded-lg px-6" 
              height="44"
              prepend-icon="mdi-plus"
              @click="openForm(null)"
          >
              Agregar empresa
          </v-btn>
      </div>

      <!-- Listado de Empresas (Grid) -->
      <v-row v-else :dense="isMobileDevice">
          <v-col cols="12" sm="6" md="4" lg="3" v-for="company in filteredCompanies" :key="company.Id">
              <v-card 
                  hover 
                  @click="openForm(company)" 
                  class="company-card border-0 elevation-1 h-100 rounded-lg"
              >
                  <div class="card-status-strip" :class="company.Activo ? 'bg-success' : 'bg-grey'"></div>
                  <v-card-text :class="isMobileDevice ? 'pa-3' : 'pa-4'">
                      <div class="d-flex justify-space-between align-start mb-2">
                          <div class="text-subtitle-1 font-weight-bold text-grey-darken-3 text-truncate">{{ company.RazonSocial }}</div>
                      </div>
                      
                      <div class="text-caption text-grey-darken-1 mb-2 font-weight-medium">
                          NIT: {{ company.NIT }}
                      </div>

                      <v-divider class="mb-2 border-opacity-50"></v-divider>

                      <div class="text-caption text-grey mb-1 d-flex align-center">
                          <v-icon size="small" start class="mr-1" color="grey-lighten-1">mdi-map-marker</v-icon>
                          <span class="text-truncate">{{ company.Direccion || 'Sin dirección' }}</span>
                      </div>
                      
                      <div class="text-caption text-grey d-flex align-center">
                          <v-icon size="small" start class="mr-1" color="grey-lighten-1">mdi-phone</v-icon>
                          {{ company.Telefono || 'Sin teléfono' }}
                      </div>
                  </v-card-text>
              </v-card>
          </v-col>
      </v-row>
    </v-card-text>

    <!-- Formulario de Empresa -->
    <CompanyForm 
        v-model="showForm" 
        :company="selectedCompany" 
        :isMobileDevice="isMobileDevice"
        @saved="loadCompanies" 
    />
  </v-card>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios'
import CompanyForm from './CompanyForm.vue'

const props = defineProps({
    modelValue: Boolean,
    isMobileDevice: Boolean
})

const emit = defineEmits(['update:modelValue'])

const companies = ref([])
const loading = ref(false)
const search = ref('')
const statusFilter = ref('all')

const showForm = ref(false)
const selectedCompany = ref(null)

async function loadCompanies() {
    loading.value = true
    try {
        const res = await axios.get('/api/config/companies', { withCredentials: true })
        companies.value = res.data
    } catch (e) {
        console.error(e)
    } finally {
        loading.value = false
    }
}

const filteredCompanies = computed(() => {
    return companies.value.filter(c => {
        // Excluir clientes (EsCliente === true)
        if (c.EsCliente) return false
        
        const matchesSearch = (c.RazonSocial?.toLowerCase().includes(search.value.toLowerCase()) || 
                               c.NIT?.includes(search.value))
        const matchesStatus = statusFilter.value === 'all' 
            ? true 
            : (statusFilter.value === 'active' ? c.Activo : !c.Activo)
        return matchesSearch && matchesStatus
    })
})

function openForm(company) {
    selectedCompany.value = company
    showForm.value = true
}

// Cargar datos al montar
onMounted(() => {
    loadCompanies()
})
</script>

<style scoped>
.empty-state-icon {
    width: 96px;
    height: 96px;
    background-color: #e3f2fd; /* Blue lighten-5 approx */
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
    background-color: #2196F3; /* Primary */
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
