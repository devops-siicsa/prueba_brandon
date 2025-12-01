<template>
  <v-card :class="['h-100', 'elevation-0', 'bg-grey-lighten-5', isMobileDevice ? 'rounded-0' : 'rounded-xl']">
    <!-- Header Personalizado -->
    <div :class="[isMobileDevice ? 'px-4 py-3' : 'px-6 py-4', 'd-flex justify-space-between align-center bg-white border-b']">
      <div class="d-flex align-center">
          <div class="header-icon-box mr-4" :style="isMobileDevice ? 'width: 36px; height: 36px;' : ''">
              <v-icon color="primary" :size="isMobileDevice ? 20 : 24">mdi-badge-account</v-icon>
          </div>
          <div>
              <h2 :class="[isMobileDevice ? 'text-subtitle-1' : 'text-h6', 'font-weight-bold text-grey-darken-3 mb-1']">Gestión de Cargos</h2>
              <p class="text-caption text-grey">Gestiona los cargos y roles laborales.</p>
          </div>
      </div>
      <v-btn icon="mdi-close" variant="text" color="grey" @click="$emit('update:modelValue', false)"></v-btn>
    </div>

    <v-card-text :class="[isMobileDevice ? 'px-3 py-4' : 'px-4 py-6 px-md-8']">
      <!-- Barra de Herramientas -->
      <v-row class="mb-4 align-center" :dense="isMobileDevice">
          <v-col cols="12" md="4">
              <v-text-field
                  v-model="search"
                  prepend-inner-icon="mdi-magnify"
                  label="Buscar cargo..."
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
                  Nuevo Cargo
              </v-btn>
          </v-col>
      </v-row>

      <!-- VISTA DE ESCRITORIO: Tabla de Cargos -->
      <v-card v-if="!isMobileDevice" class="rounded-lg border-0 elevation-1" :loading="loading">
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
                      <v-icon size="48" color="grey-lighten-2" class="mb-2">mdi-badge-account</v-icon>
                      <div class="text-body-1 text-grey">No hay cargos registrados</div>
                  </div>
              </template>
          </v-data-table>
      </v-card>

      <!-- VISTA MÓVIL: Lista de Tarjetas -->
      <div v-else>
        <!-- Estado Vacío Móvil -->
        <div v-if="filteredItems.length === 0" class="d-flex flex-column align-center justify-center py-12 text-center">
            <div class="empty-state-icon mb-6" style="width: 72px; height: 72px;">
                <v-icon size="36" color="primary">mdi-badge-account</v-icon>
                <div class="plus-badge" style="width: 24px; height: 24px;">
                    <v-icon size="14" color="white">mdi-plus</v-icon>
                </div>
            </div>
            <h3 class="text-subtitle-1 font-weight-bold text-grey-darken-3 mb-2">No se encontraron cargos</h3>
            <v-btn color="primary" variant="tonal" class="text-capitalize rounded-lg" prepend-icon="mdi-plus" @click="openForm(null)">
                Crear nuevo
            </v-btn>
        </div>

        <!-- Grid de Tarjetas -->
        <v-row v-else dense>
            <v-col cols="12" v-for="item in filteredItems" :key="item.Id">
                <v-card hover @click="openForm(item)" class="border-0 elevation-1 rounded-lg">
                    <div class="d-flex align-center pa-3">
                        <!-- Icono / Estado -->
                        <div class="mr-3">
                            <v-avatar :color="item.Activo ? 'green-lighten-5' : 'grey-lighten-4'" size="40" class="rounded-lg">
                                <v-icon :color="item.Activo ? 'success' : 'grey'" size="20">mdi-badge-account</v-icon>
                            </v-avatar>
                        </div>
                        
                        <!-- Info -->
                        <div class="flex-grow-1" style="min-width: 0;">
                            <div class="text-subtitle-2 font-weight-bold text-grey-darken-3 text-truncate">
                                {{ item.Nombre }}
                            </div>
                            <div class="text-caption text-grey">
                                ID: {{ String(item.Id).padStart(3, '0') }}
                            </div>
                        </div>

                        <!-- Chip Estado -->
                        <div class="ml-2">
                             <v-chip size="x-small" :color="item.Activo ? 'success' : 'grey'" variant="flat" class="font-weight-bold">
                                {{ item.Activo ? 'Activo' : 'Inactivo' }}
                            </v-chip>
                        </div>
                    </div>
                </v-card>
            </v-col>
        </v-row>
      </div>
    </v-card-text>

    <!-- Formulario de Cargo -->
    <CargoForm 
        v-model="formDialog" 
        :cargo="editedItem" 
        :isMobileDevice="isMobileDevice"
        @save="loadItems" 
    />
  </v-card>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import CargoForm from './CargoForm.vue'

const props = defineProps({
    modelValue: Boolean,
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
    { title: 'NOMBRE DEL CARGO', key: 'Nombre', align: 'start' },
    { title: 'ESTADO', key: 'Activo', align: 'center', width: '120px' },
]

const defaultItem = {
    Id: null,
    Nombre: '',
    Activo: true
}

const filteredItems = computed(() => {
    return items.value.filter(item => {
        if (statusFilter.value === 'all') return true
        if (statusFilter.value === 'active') return item.Activo
        if (statusFilter.value === 'inactive') return !item.Activo
        return true
    })
})

const editedItem = ref({ ...defaultItem })

async function loadItems() {
    loading.value = true
    try {
        const res = await axios.get('/api/config/catalogs/cargos', { withCredentials: true })
        items.value = res.data
    } catch (e) {
        console.error("Error cargando cargos:", e)
    } finally {
        loading.value = false
    }
}

function openForm(item) {
    editedItem.value = item ? { ...item } : { ...defaultItem }
    formDialog.value = true
}

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
