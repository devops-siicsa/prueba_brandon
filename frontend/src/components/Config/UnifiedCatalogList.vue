<template>
  <v-card :class="['h-100', 'elevation-0', 'bg-grey-lighten-5', isMobileDevice ? 'rounded-0' : 'rounded-xl']">
    <!-- Header Personalizado -->
    <div class="px-6 py-4 d-flex justify-space-between align-center bg-white border-b">
      <div class="d-flex align-center">
          <div class="header-icon-box mr-4">
              <v-icon color="primary" size="24">{{ icon }}</v-icon>
          </div>
          <div>
              <h2 class="text-h6 font-weight-bold text-grey-darken-3 mb-1">{{ title }}</h2>
              <p class="text-caption text-grey">{{ description }}</p>
          </div>
      </div>
      <v-btn icon="mdi-close" variant="text" color="grey" @click="$emit('update:modelValue', false)"></v-btn>
    </div>

    <v-card-text class="px-4 py-6 px-md-8">
      <!-- Barra de Herramientas -->
      <v-row class="mb-4 align-center">
          <v-col cols="12" md="4">
              <v-text-field
                  v-model="search"
                  prepend-inner-icon="mdi-magnify"
                  :label="`Buscar en ${title}...`"
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

          <v-spacer></v-spacer>
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
                  Nuevo
              </v-btn>
          </v-col>
      </v-row>

      <!-- Tabla de Items -->
      <v-card class="rounded-lg border-0 elevation-1" :loading="loading">
          <v-data-table
              :headers="headers"
              :items="filteredItems"
              :search="search"
              :loading="loading"
              hover
              density="comfortable"
              class="rounded-lg"
              @click:row="(_, { item }) => openForm(item)"
          >
              <!-- Slot: ID -->
              <template v-slot:item.Id="{ item }">
                  <span class="text-grey-darken-1 font-weight-medium">{{ String(item.Id).padStart(3, '0') }}</span>
              </template>

              <!-- Slot: Nombre -->
              <template v-slot:item.Nombre="{ item }">
                  <span class="font-weight-bold text-grey-darken-3">{{ item.Nombre }}</span>
              </template>

              <!-- Slot: Estado -->
              <template v-slot:item.Activo="{ item }">
                  <v-chip 
                      :color="item.Activo ? 'emerald' : 'grey'" 
                      :class="item.Activo ? 'bg-green-lighten-5 text-green-darken-1' : 'bg-grey-lighten-4 text-grey-darken-1'"
                      size="small" 
                      class="font-weight-bold"
                      variant="flat"
                  >
                      <template v-slot:prepend>
                          <v-icon size="8" class="mr-1" :color="item.Activo ? 'success' : 'grey'">mdi-circle</v-icon>
                      </template>
                      {{ item.Activo ? 'Activo' : 'Inactivo' }}
                  </v-chip>
              </template>

              <!-- Estado Vacío -->
              <template v-slot:no-data>
                  <div class="d-flex flex-column align-center justify-center py-8">
                      <v-icon size="48" color="grey-lighten-2" class="mb-2">{{ icon }}</v-icon>
                      <div class="text-body-1 text-grey">No hay registros</div>
                  </div>
              </template>
          </v-data-table>
      </v-card>
    </v-card-text>

    <!-- Formulario de Catálogo Unificado -->
    <UnifiedCatalogForm 
        v-model="formDialog" 
        :item="editedItem" 
        :catalog-name="catalogName"
        :isMobileDevice="isMobileDevice"
        @save="loadItems" 
    />
  </v-card>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios'
import UnifiedCatalogForm from './UnifiedCatalogForm.vue'

const props = defineProps({
    modelValue: Boolean,
    catalogName: {
        type: String,
        required: true
    },
    title: {
        type: String,
        default: 'Catálogo'
    },
    icon: {
        type: String,
        default: 'mdi-database'
    },
    description: {
        type: String,
        default: ''
    },
    isMobileDevice: Boolean
})

const emit = defineEmits(['update:modelValue'])

const items = ref([])
const loading = ref(false)
const search = ref('')
const formDialog = ref(false)
const statusFilter = ref('all')

const headers = [
    { title: 'ID', key: 'Id', align: 'start', width: '80px' },
    { title: 'NOMBRE', key: 'Nombre', align: 'start' },
    { title: 'ESTADO', key: 'Activo', align: 'center', width: '120px' },
]

const defaultItem = {
    Id: null,
    Nombre: '',
    Activo: true
}

const editedItem = ref({ ...defaultItem })

const filteredItems = computed(() => {
    return items.value.filter(item => {
        if (statusFilter.value === 'all') return true
        if (statusFilter.value === 'active') return item.Activo
        if (statusFilter.value === 'inactive') return !item.Activo
        return true
    })
})

async function loadItems() {
    loading.value = true
    try {
        const res = await axios.get(`/api/config/catalogs/${props.catalogName}`, { withCredentials: true })
        items.value = res.data
    } catch (e) {
        console.error(`Error cargando ${props.catalogName}:`, e)
    } finally {
        loading.value = false
    }
}

function openForm(item) {
    editedItem.value = item ? { ...item } : { ...defaultItem }
    formDialog.value = true
}

// Recargar si cambia el catálogo mientras el componente está montado
watch(() => props.catalogName, () => {
    loadItems()
})

onMounted(() => {
    loadItems()
})
</script>

<style scoped>
.header-icon-box {
    width: 42px;
    height: 42px;
    background-color: #e3f2fd;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
