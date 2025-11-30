<template>
  <v-dialog v-model="dialog" max-width="900" scrollable transition="dialog-bottom-transition">
    <v-card class="bg-grey-lighten-5 rounded-xl" height="600">
      <!-- Header -->
      <div class="px-8 pt-6 pb-6 bg-white elevation-0 border-bottom">
        <div class="d-flex align-center justify-space-between">
            <div class="d-flex align-center">
                <div class="header-icon-box mr-4 bg-teal-lighten-5">
                    <v-icon color="teal-darken-1" size="28">mdi-memory</v-icon>
                </div>
                <div>
                    <h2 class="text-h6 font-weight-bold text-grey-darken-3 mb-0">Memoria RAM</h2>
                    <p class="text-caption text-grey">Gestiona tipos, capacidades y velocidades de memoria.</p>
                </div>
            </div>
            <v-btn icon="mdi-close" variant="text" color="grey" @click="dialog = false"></v-btn>
        </div>

        <!-- Toolbar -->
        <div class="mt-6 d-flex align-center flex-wrap gap-4">
            <div style="width: 280px;">
                <v-text-field
                    v-model="search"
                    prepend-inner-icon="mdi-magnify"
                    placeholder="Buscar memoria..."
                    variant="outlined"
                    density="compact"
                    hide-details
                    bg-color="white"
                    class="rounded-lg search-input"
                ></v-text-field>
            </div>
            
            <div style="width: 200px;">
                <v-select
                    v-model="filterTipo"
                    :items="tipos"
                    item-title="Nombre"
                    item-value="Id"
                    placeholder="Todos los Tipos"
                    variant="outlined"
                    density="compact"
                    hide-details
                    bg-color="white"
                    class="rounded-lg"
                    clearable
                ></v-select>
            </div>

            <v-spacer></v-spacer>

            <v-btn 
                color="blue-grey-lighten-4" 
                variant="flat"
                class="text-blue-grey-darken-4 text-capitalize rounded-lg px-4 mr-2" 
                height="40"
                prepend-icon="mdi-database-plus" 
                elevation="0"
                @click="openCapacityDialog"
            >
            Capacidad
            </v-btn>

            <v-btn 
                color="#1e293b" 
                class="text-white text-capitalize rounded-lg px-6" 
                height="40"
                prepend-icon="mdi-plus" 
                elevation="0"
                @click="openCreateDialog"
            >
            RAM
            </v-btn>
        </div>
      </div>

      <v-container fluid class="pa-8">
        <v-card class="rounded-lg border-thin elevation-0 overflow-hidden">
            <v-data-table
                :headers="headers"
                :items="tableItems"
                :search="search"
                :loading="loading"
                hover
                class="header-bg cursor-pointer"
                @click:row="editItem"
            >
                <!-- TIPO -->
                <template v-slot:item.Tipo="{ item }">
                    <v-chip
                        size="small"
                        color="teal"
                        variant="flat"
                        class="font-weight-bold bg-teal-lighten-5 text-teal-darken-2"
                    >
                        {{ item.Tipo }}
                    </v-chip>
                </template>

                <!-- VELOCIDAD -->
                <template v-slot:item.Velocidad="{ item }">
                    <span class="text-body-2 text-grey-darken-1">{{ item.Velocidad }}</span>
                </template>

                <!-- ESTADO -->
                <template v-slot:item.Estado="{ item }">
                    <v-chip 
                        :color="item.Activo ? 'emerald' : 'grey'" 
                        :class="item.Activo ? 'bg-green-lighten-5 text-green-darken-1' : 'bg-grey-lighten-4 text-grey-darken-1'"
                        class="font-weight-bold"
                        size="small" 
                        variant="flat"
                    >
                        <template v-slot:prepend>
                            <v-icon size="8" class="mr-1" :color="item.Activo ? 'success' : 'grey'">mdi-circle</v-icon>
                        </template>
                        {{ item.Activo ? 'Activo' : 'Inactivo' }}
                    </v-chip>
                </template>
            </v-data-table>
        </v-card>
      </v-container>
    </v-card>

    <!-- Dialogo Crear RAM (Tipo + Velocidad) -->
    <v-dialog v-model="formDialog" max-width="450" persistent>
        <v-card class="rounded-xl pa-4">
            <v-card-title class="px-4 pt-2 pb-2 d-flex align-start justify-space-between">
                <div>
                    <span class="text-h6 font-weight-bold text-blue-grey-darken-4">
                        Nueva Velocidad RAM
                    </span>
                    <p class="text-caption text-grey mt-1">Registra Tipo y Velocidad de bus.</p>
                </div>
                <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="formDialog = false"></v-btn>
            </v-card-title>
            
            <v-divider class="mx-4 opacity-10 mb-4"></v-divider>

            <v-card-text class="px-4 py-0">
                <v-form @submit.prevent="save">
                    <v-row no-gutters>
                        <!-- TIPO -->
                        <v-col cols="12" class="mb-4">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">TIPO</label>
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Selecciona o escribe (ej. DDR4)</span>
                            </div>
                            <v-combobox
                                :model-value="formData.Tipo"
                                @update:model-value="v => formData.Tipo = v?.toUpperCase() ?? ''"
                                :items="tipos"
                                item-title="Nombre"
                                item-value="Nombre"
                                placeholder="Ej. DDR4"
                                variant="outlined"
                                density="comfortable"
                                color="primary"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                :return-object="false"
                                bg-color="grey-lighten-5"
                            ></v-combobox>
                        </v-col>

                        <!-- VELOCIDAD -->
                        <v-col cols="12" class="mb-2">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">VELOCIDAD</label>
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Vinculada al Tipo (ej. 3200MHZ)</span>
                            </div>
                            <v-combobox
                                :model-value="formData.Velocidad"
                                @update:model-value="v => formData.Velocidad = v?.toUpperCase() ?? ''"
                                :items="filteredVelocidades"
                                item-title="Nombre"
                                item-value="Nombre"
                                placeholder="Ej. 3200MHZ"
                                variant="outlined"
                                density="comfortable"
                                color="primary"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                :return-object="false"
                                bg-color="grey-lighten-5"
                                :disabled="!formData.Tipo"
                            ></v-combobox>
                        </v-col>
                    </v-row>
                </v-form>
            </v-card-text>

            <v-card-actions class="px-4 pb-2 pt-4">
                <v-spacer></v-spacer>
                <v-btn 
                    variant="text" 
                    color="blue-grey-darken-1" 
                    class="text-capitalize font-weight-medium px-4" 
                    @click="formDialog = false"
                >
                    Cancelar
                </v-btn>
                <v-btn 
                    color="#1e293b" 
                    variant="flat" 
                    class="text-white text-capitalize rounded-lg px-6 ml-2"
                    height="44"
                    @click="save" 
                    :loading="saving"
                >
                    <v-icon start class="mr-2">mdi-content-save-outline</v-icon>
                    Guardar
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <!-- Dialogo Editar -->
    <v-dialog v-model="editDialog" max-width="450" persistent>
        <v-card class="rounded-xl pa-4">
            <v-card-title class="px-4 pt-2 pb-2 d-flex align-start justify-space-between">
                <div>
                    <span class="text-h6 font-weight-bold text-blue-grey-darken-4">
                        Editar Velocidad
                    </span>
                    <p class="text-caption text-grey mt-1">Modifica la velocidad o cambia su estado.</p>
                </div>
                <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="editDialog = false"></v-btn>
            </v-card-title>
            
            <v-divider class="mx-4 opacity-10 mb-4"></v-divider>

            <v-card-text class="px-4 py-0">
                <v-form @submit.prevent="updateItem">
                    <v-row no-gutters>
                        <!-- TIPO (Readonly) -->
                        <v-col cols="12" class="mb-4">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">TIPO</label>
                            </div>
                            <v-text-field
                                v-model="editData.Tipo"
                                variant="outlined"
                                density="comfortable"
                                bg-color="grey-lighten-4"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                readonly
                            ></v-text-field>
                        </v-col>

                        <!-- VELOCIDAD -->
                        <v-col cols="12" class="mb-4">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">VELOCIDAD</label>
                            </div>
                            <v-text-field
                                v-model="editData.Velocidad"
                                placeholder="Ej. 3200MHZ"
                                variant="outlined"
                                density="comfortable"
                                color="primary"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                bg-color="grey-lighten-5"
                                @update:model-value="v => editData.Velocidad = v?.toUpperCase() ?? ''"
                            ></v-text-field>
                        </v-col>

                        <!-- ESTADO -->
                        <v-col cols="12" class="mb-2">
                            <v-switch
                                v-model="editData.Activo"
                                color="success"
                                label="Activo"
                                hide-details
                                inset
                            ></v-switch>
                        </v-col>
                    </v-row>
                </v-form>
            </v-card-text>

            <v-card-actions class="px-4 pb-2 pt-4">
                <v-spacer></v-spacer>
                <v-btn 
                    variant="text" 
                    color="blue-grey-darken-1" 
                    class="text-capitalize font-weight-medium px-4" 
                    @click="editDialog = false"
                >
                    Cancelar
                </v-btn>
                <v-btn 
                    color="#1e293b" 
                    variant="flat" 
                    class="text-white text-capitalize rounded-lg px-6 ml-2"
                    height="44"
                    @click="updateItem" 
                    :loading="saving"
                >
                    <v-icon start class="mr-2">mdi-content-save-outline</v-icon>
                    Actualizar
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <!-- Dialogo Crear Capacidad -->
    <v-dialog v-model="capacityDialog" max-width="400" persistent>
        <v-card class="rounded-xl pa-4">
            <v-card-title class="px-4 pt-2 pb-2 d-flex align-start justify-space-between">
                <div>
                    <span class="text-h6 font-weight-bold text-blue-grey-darken-4">
                        Nueva Capacidad
                    </span>
                    <p class="text-caption text-grey mt-1">Añade una capacidad global.</p>
                </div>
                <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="capacityDialog = false"></v-btn>
            </v-card-title>
            
            <v-divider class="mx-4 opacity-10 mb-4"></v-divider>

            <v-card-text class="px-4 py-0">
                <v-form @submit.prevent="saveCapacity">
                    <v-row no-gutters>
                        <v-col cols="12" class="mb-2">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">CAPACIDAD</label>
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Selecciona o escribe (ej. 64GB)</span>
                            </div>
                            <v-combobox
                                v-model="newCapacity"
                                :items="capacidades"
                                item-title="Nombre"
                                item-value="Nombre"
                                placeholder="Ej. 64GB"
                                variant="outlined"
                                density="comfortable"
                                color="primary"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                bg-color="grey-lighten-5"
                                :return-object="false"
                                @update:model-value="v => newCapacity = v?.toUpperCase() ?? ''"
                            ></v-combobox>
                        </v-col>
                    </v-row>
                </v-form>
            </v-card-text>

            <v-card-actions class="px-4 pb-2 pt-4">
                <v-spacer></v-spacer>
                <v-btn 
                    variant="text" 
                    color="blue-grey-darken-1" 
                    class="text-capitalize font-weight-medium px-4" 
                    @click="capacityDialog = false"
                >
                    Cancelar
                </v-btn>
                <v-btn 
                    color="#1e293b" 
                    variant="flat" 
                    class="text-white text-capitalize rounded-lg px-6 ml-2"
                    height="44"
                    @click="saveCapacity" 
                    :loading="savingCapacity"
                >
                    <v-icon start class="mr-2">mdi-content-save-outline</v-icon>
                    Guardar
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
  </v-dialog>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios'

const props = defineProps({
    modelValue: Boolean
})

const emit = defineEmits(['update:modelValue'])

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

// Data
const tipos = ref([])
const capacidades = ref([])
const velocidades = ref([]) // Raw data
const loading = ref(false)

// Filters
const search = ref('')
const filterTipo = ref(null)

// Table
const headers = [
    { title: 'TIPO', key: 'Tipo', align: 'start', width: '120px' },
    { title: 'VELOCIDAD', key: 'Velocidad', align: 'start' },
    { title: 'ESTADO', key: 'Estado', align: 'end', width: '120px' },
]

const tableItems = computed(() => {
    let items = velocidades.value.map(v => {
        const tipo = tipos.value.find(t => t.Id === v.TipoRAMId)
        return {
            Id: v.Id,
            Velocidad: v.Nombre,
            Tipo: tipo ? tipo.Nombre : '?',
            TipoId: v.TipoRAMId,
            Activo: v.Activo
        }
    })

    if (filterTipo.value) {
        items = items.filter(i => i.TipoId === filterTipo.value)
    }

    return items
})

// Form RAM (Tipo + Velocidad)
const formDialog = ref(false)
const saving = ref(false)
const formData = ref({ Tipo: '', Velocidad: '' })

// Edit Form
const editDialog = ref(false)
const editData = ref({ Id: null, Tipo: '', Velocidad: '', Activo: true })

// Form Capacidad
const capacityDialog = ref(false)
const savingCapacity = ref(false)
const newCapacity = ref('')

const filteredVelocidades = computed(() => {
    const tipoObj = tipos.value.find(t => t.Nombre === formData.value.Tipo)
    if (!tipoObj) return []
    return velocidades.value.filter(v => v.TipoRAMId === tipoObj.Id)
})

// API
const API_URL = '/api/config'

async function loadAll() {
    loading.value = true
    try {
        const [resTipos, resCaps, resVels] = await Promise.all([
            axios.get(`${API_URL}/tipos_ram`, { withCredentials: true }),
            axios.get(`${API_URL}/capacidades_ram`, { withCredentials: true }),
            axios.get(`${API_URL}/velocidades_ram`, { withCredentials: true })
        ])
        tipos.value = resTipos.data
        capacidades.value = resCaps.data
        velocidades.value = resVels.data
    } catch (e) {
        console.error("Error loading RAM data", e)
    } finally {
        loading.value = false
    }
}

function openCreateDialog() {
    formData.value = { Tipo: '', Velocidad: '' }
    formDialog.value = true
}

function editItem(event, { item }) {
    editData.value = { 
        Id: item.Id, 
        Tipo: item.Tipo, 
        Velocidad: item.Velocidad, 
        Activo: item.Activo 
    }
    editDialog.value = true
}

async function updateItem() {
    if (!editData.value.Velocidad) return
    saving.value = true
    try {
        await axios.put(`${API_URL}/velocidades_ram/${editData.value.Id}`, {
            Nombre: editData.value.Velocidad,
            Activo: editData.value.Activo
        }, { withCredentials: true })
        
        await loadAll()
        editDialog.value = false
    } catch (e) {
        alert("Error al actualizar: " + (e.response?.data?.message || e.message))
    } finally {
        saving.value = false
    }
}

function openCapacityDialog() {
    newCapacity.value = ''
    capacityDialog.value = true
}

async function saveCapacity() {
    if (!newCapacity.value) return
    savingCapacity.value = true
    try {
        // Verificar si ya existe
        const existing = capacidades.value.find(c => c.Nombre === newCapacity.value)
        if (existing) {
            alert("Esa capacidad ya existe")
            savingCapacity.value = false
            return
        }
        
        await axios.post(`${API_URL}/capacidades_ram`, { Nombre: newCapacity.value }, { withCredentials: true })
        await loadAll()
        capacityDialog.value = false
    } catch (e) {
        alert("Error al guardar capacidad: " + (e.response?.data?.message || e.message))
    } finally {
        savingCapacity.value = false
    }
}

async function save() {
    if (!formData.value.Tipo || !formData.value.Velocidad) {
        alert("Por favor complete Tipo y Velocidad")
        return
    }
    saving.value = true

    try {
        // 1. Find or Create TIPO
        let tipoId = null
        const existingTipo = tipos.value.find(t => t.Nombre === formData.value.Tipo)
        if (existingTipo) {
            tipoId = existingTipo.Id
        } else {
            const res = await axios.post(`${API_URL}/tipos_ram`, { Nombre: formData.value.Tipo }, { withCredentials: true })
            await loadAll()
            const newTipo = tipos.value.find(t => t.Nombre === formData.value.Tipo)
            if (newTipo) tipoId = newTipo.Id
        }

        // 2. Find or Create VELOCIDAD (Depende de Tipo)
        const existingVel = velocidades.value.find(v => v.Nombre === formData.value.Velocidad && v.TipoRAMId === tipoId)
        if (!existingVel) {
            await axios.post(`${API_URL}/velocidades_ram`, { Nombre: formData.value.Velocidad, TipoRAMId: tipoId }, { withCredentials: true })
        } else {
            alert("Esta velocidad ya existe para este tipo de RAM")
        }

        await loadAll()
        formDialog.value = false
    } catch (e) {
        alert("Error al guardar: " + (e.response?.data?.message || e.message))
    } finally {
        saving.value = false
    }
}

onMounted(() => {
    if (dialog.value) loadAll()
})

watch(dialog, (val) => {
    if (val) loadAll()
})
</script>

<style scoped>
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
.gap-4 { gap: 16px; }
.search-input :deep(.v-field__outline__start),
.search-input :deep(.v-field__outline__end) { border-color: rgba(0,0,0,0.08) !important; }
</style>
