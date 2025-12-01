<template>
  <v-card :class="['h-100', 'elevation-0', 'bg-grey-lighten-5', isMobileApp ? 'rounded-0' : 'rounded-xl']">
    <!-- Header Personalizado -->
    <div :class="[isMobileApp ? 'px-4 py-3' : 'px-6 py-4', 'd-flex justify-space-between align-center bg-white border-b']">
      <div>
          <h2 :class="[isMobileApp ? 'text-subtitle-1' : 'text-h6', 'font-weight-bold text-grey-darken-3']">{{ title }}</h2>
          <p class="text-caption text-grey">Gestiona el acceso y los permisos de los usuarios.</p>
      </div>
      <v-btn icon="mdi-close" variant="text" color="grey" @click="$emit('update:modelValue', false)"></v-btn>
    </div>

    <v-card-text :class="[isMobileApp ? 'px-3 py-4' : 'px-4 py-6 px-md-8']">
      <!-- Barra de Herramientas -->
      <v-row class="mb-4 align-center" :dense="isMobileApp">
          <v-col cols="12" md="5">
              <v-text-field
                  v-model="search"
                  prepend-inner-icon="mdi-magnify"
                  :label="`Buscar en ${title}`"
                  variant="outlined"
                  density="compact"
                  hide-details
                  bg-color="white"
                  class="rounded-lg"
              ></v-text-field>
          </v-col>
          <v-spacer v-if="!isMobileApp"></v-spacer>
          <v-col cols="12" md="auto">
              <v-btn 
                  color="#1e293b" 
                  block
                  class="text-white text-capitalize rounded-lg" 
                  height="40"
                  prepend-icon="mdi-account-plus" 
                  elevation="0"
                  @click="openCreate"
              >
                  Nuevo Usuario
              </v-btn>
          </v-col>
      </v-row>

      <!-- Estado de Carga -->
      <div v-if="loading" class="d-flex justify-center align-center py-12">
          <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
      </div>

      <!-- Estado Vacío (Empty State) -->
      <div v-else-if="filteredUsers.length === 0" class="d-flex flex-column align-center justify-center py-12 text-center">
          <div class="empty-state-icon mb-6" :style="isMobileApp ? 'width: 72px; height: 72px;' : ''">
              <v-icon :size="isMobileApp ? 36 : 48" color="primary">mdi-account-off</v-icon>
              <div class="plus-badge" :style="isMobileApp ? 'width: 24px; height: 24px;' : ''">
                  <v-icon :size="isMobileApp ? 14 : 16" color="white">mdi-plus</v-icon>
              </div>
          </div>
          
          <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">No se encontraron registros</h3>
          <p class="text-body-2 text-grey mb-8" style="max-width: 400px;">
              No hay usuarios registrados que coincidan con tu búsqueda.
          </p>

          <v-btn 
              color="primary" 
              variant="tonal" 
              class="text-capitalize rounded-lg px-6" 
              height="44"
              prepend-icon="mdi-account-plus"
              @click="openCreate"
          >
              Crear nuevo
          </v-btn>
      </div>

      <!-- Listado de Usuarios (Grid) -->
      <v-row v-else :dense="isMobileApp">
          <v-col cols="12" sm="6" md="4" lg="3" v-for="user in filteredUsers" :key="user.Id">
              <v-card 
                  hover 
                  @click="openEdit(user)" 
                  class="user-card border-0 elevation-1 h-100 rounded-lg"
              >
                  <div class="card-status-strip" :class="user.Activo ? 'bg-success' : 'bg-grey'"></div>
                  <v-card-text :class="isMobileApp ? 'pa-3' : 'pa-4'">
                      <div class="d-flex align-center mb-2">
                          <v-avatar color="blue-lighten-5" size="40" class="mr-3">
                              <span class="text-primary font-weight-bold">{{ getInitials(user) }}</span>
                          </v-avatar>
                          <div class="text-truncate" style="flex: 1; min-width: 0;">
                              <div class="text-subtitle-2 font-weight-bold text-grey-darken-3 text-truncate">
                                  {{ user.Nombre }} {{ user.Apellido }}
                              </div>
                              <div class="text-caption text-grey text-truncate">{{ user.Correo }}</div>
                          </div>
                      </div>
                      
                      <v-divider class="mb-2 border-opacity-50"></v-divider>

                      <div class="text-caption text-grey-darken-1 mb-1 font-weight-medium d-flex align-center">
                          <v-icon size="small" start class="mr-1">mdi-shield-account</v-icon>
                          <span class="text-truncate">{{ user.Rol || 'Sin Rol' }}</span>
                      </div>

                      <div class="text-caption text-grey mb-1 d-flex align-center" v-if="user.CargoId">
                          <v-icon size="small" start class="mr-1" color="grey-lighten-1">mdi-badge-account-horizontal</v-icon>
                          <span class="text-truncate">{{ getCatalogName('cargos', user.CargoId) }}</span>
                      </div>
                      
                      <div class="text-caption text-grey d-flex align-center" v-if="user.SedeId">
                          <v-icon size="small" start class="mr-1" color="grey-lighten-1">mdi-map-marker</v-icon>
                          <span class="text-truncate">{{ getSedeName(user.SedeId) }}</span>
                      </div>
                  </v-card-text>
              </v-card>
          </v-col>
      </v-row>

    </v-card-text>

    <!-- Formulario Modal -->
    <UserForm 
        v-model="showForm"
        :user="selectedUser"
        :allowed-roles="filterRoles"
        :client-mode="clientMode"
        @save="handleSave" 
    />
  </v-card>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'
import UserForm from './UserForm.vue'
import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    modelValue: Boolean,
    filterRoles: {
        type: Array,
        default: () => []
    },
    title: {
        type: String,
        default: 'Mis Usuarios'
    },
    embedded: {
        type: Boolean,
        default: false
    },
    clientMode: {
        type: Boolean,
        default: false
    }
})

const emit = defineEmits(['update:modelValue'])
const { isMobileApp } = useMobileDetection()

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

const users = ref([])
const sedes = ref([])
const cargos = ref([])
const search = ref('')
const showForm = ref(false)
const selectedUser = ref(null)
const loading = ref(false)

const filteredUsers = computed(() => {
    let result = users.value

    // Filtrar por roles si se especifican
    if (props.filterRoles.length > 0) {
        result = result.filter(u => props.filterRoles.includes(u.Rol))
    }

    if (!search.value) return result
    
    const term = search.value.toLowerCase()
    return result.filter(u => 
        u.Nombre.toLowerCase().includes(term) ||
        u.Apellido.toLowerCase().includes(term) ||
        u.Correo.toLowerCase().includes(term)
    )
})

function getInitials(user) {
    return `${user.Nombre.charAt(0)}${user.Apellido.charAt(0)}`.toUpperCase()
}

function getCatalogName(catalog, id) {
    if (catalog === 'cargos') {
        const item = cargos.value.find(c => c.Id === id)
        return item ? item.Nombre : 'Desconocido'
    }
    return ''
}

function getSedeName(id) {
    const item = sedes.value.find(s => s.Id === id)
    return item ? item.NombreSede : 'Desconocida'
}

async function loadData() {
    loading.value = true
    try {
        const [usersRes, sedesRes, cargosRes] = await Promise.all([
            axios.get('/api/config/users', { withCredentials: true }),
            axios.get('/api/config/sedes', { withCredentials: true }),
            axios.get('/api/config/catalogs/cargos', { withCredentials: true })
        ])
        users.value = usersRes.data
        sedes.value = sedesRes.data
        cargos.value = cargosRes.data
    } catch (error) {
        console.error("Error cargando datos:", error)
    } finally {
        loading.value = false
    }
}

function openCreate() {
    selectedUser.value = null
    showForm.value = true
}

function openEdit(user) {
    selectedUser.value = { ...user }
    showForm.value = true
}

async function handleSave() {
    await loadData()
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

.user-card {
    transition: all 0.2s ease;
    position: relative;
    overflow: hidden;
    cursor: pointer;
}

.user-card:hover {
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
