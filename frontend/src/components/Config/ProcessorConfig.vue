<template>
  <v-dialog v-model="dialog" max-width="900" scrollable transition="dialog-bottom-transition">
    <v-card class="bg-grey-lighten-5 rounded-xl" height="600">
      <!-- Header -->
      <div class="px-8 pt-6 pb-6 bg-white elevation-0 border-bottom">
        <div class="d-flex align-center justify-space-between">
            <div class="d-flex align-center">
                <div class="header-icon-box mr-4 bg-blue-grey-lighten-5">
                    <v-icon color="blue-grey-darken-1" size="28">mdi-cpu-64-bit</v-icon>
                </div>
                <div>
                    <h2 class="text-h6 font-weight-bold text-grey-darken-3 mb-0">Procesadores</h2>
                    <p class="text-caption text-grey">Gestiona las especificaciones de CPUs disponibles.</p>
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
                    placeholder="Buscar modelo..."
                    variant="outlined"
                    density="compact"
                    hide-details
                    bg-color="white"
                    class="rounded-lg search-input"
                ></v-text-field>
            </div>
            
            <div style="width: 200px;">
                <v-select
                    v-model="filterMarca"
                    :items="marcas"
                    item-title="Nombre"
                    item-value="Id"
                    placeholder="Todas las Marcas"
                    variant="outlined"
                    density="compact"
                    hide-details
                    bg-color="white"
                    class="rounded-lg"
                    clearable
                ></v-select>
            </div>

            <div style="width: 220px;">
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
                color="#1e293b" 
                class="text-white text-capitalize rounded-lg px-6" 
                height="40"
                prepend-icon="mdi-plus" 
                elevation="0"
                @click="openCreateDialog"
            >
            Agregar
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
                class="header-bg"
            >
                <!-- ID -->
                <template v-slot:item.Id="{ item }">
                    <span class="text-caption font-weight-bold text-grey">{{ String(item.Id).padStart(3, '0') }}</span>
                </template>

                <!-- MARCA -->
                <template v-slot:item.Marca="{ item }">
                    <v-chip
                        size="small"
                        :color="getBrandColor(item.Marca)"
                        variant="flat"
                        class="font-weight-bold"
                        :class="`bg-${getBrandColor(item.Marca)}-lighten-5 text-${getBrandColor(item.Marca)}-darken-2`"
                    >
                        {{ item.Marca }}
                    </v-chip>
                </template>

                <!-- TIPO -->
                <template v-slot:item.Tipo="{ item }">
                    <span class="font-weight-bold text-grey-darken-3">{{ item.Tipo }}</span>
                </template>

                <!-- GENERACIÓN -->
                <template v-slot:item.Generacion="{ item }">
                    <span class="text-body-2 text-grey-darken-1">{{ item.Generacion }}</span>
                </template>

                <!-- ESTADO -->
                <template v-slot:item.Estado="{ item }">
                    <v-chip 
                        color="emerald" 
                        class="bg-green-lighten-5 text-green-darken-1 font-weight-bold"
                        size="small" 
                        variant="flat"
                    >
                        <template v-slot:prepend>
                            <v-icon size="8" class="mr-1" color="success">mdi-circle</v-icon>
                        </template>
                        Activo
                    </v-chip>
                </template>

                <!-- ACTIONS -->
                <template v-slot:item.actions="{ item }">
                    <v-btn icon variant="text" size="small" color="grey" @click="editItem(item)">
                        <v-icon size="18">mdi-pencil</v-icon>
                    </v-btn>
                </template>

                <template v-slot:no-data>
                    <div class="py-8 text-center">
                        <v-icon size="48" color="grey-lighten-2" class="mb-2">mdi-cpu-64-bit</v-icon>
                        <div class="text-grey">No hay datos disponibles</div>
                    </div>
                </template>
            </v-data-table>
        </v-card>
      </v-container>
    </v-card>

    <!-- Dialogo Crear/Editar -->
    <v-dialog v-model="formDialog" max-width="450" persistent>
        <v-card class="rounded-xl pa-4">
            <v-card-title class="px-4 pt-2 pb-2 d-flex align-start justify-space-between">
                <div>
                    <span class="text-h6 font-weight-bold text-blue-grey-darken-4">
                        {{ isEditing ? 'Editar Procesador' : 'Nuevo Procesador' }}
                    </span>
                    <p class="text-caption text-grey mt-1">Registra un nuevo modelo de CPU.</p>
                </div>
                <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="formDialog = false"></v-btn>
            </v-card-title>
            
            <v-divider class="mx-4 opacity-10 mb-4"></v-divider>

            <v-card-text class="px-4 py-0">
                <v-form @submit.prevent="save">
                    <v-row no-gutters>
                        <!-- MARCA -->
                        <v-col cols="12" class="mb-4">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">MARCA</label>
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Selecciona o escribe para crear</span>
                            </div>
                            <v-combobox
                                :model-value="formData.Marca"
                                @update:model-value="v => formData.Marca = v?.toUpperCase() ?? ''"
                                :items="marcas"
                                item-title="Nombre"
                                item-value="Nombre"
                                placeholder="Ej. INTEL"
                                variant="outlined"
                                density="comfortable"
                                color="primary"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                :return-object="false"
                                bg-color="grey-lighten-5"
                            ></v-combobox>
                        </v-col>

                        <!-- TIPO -->
                        <v-col cols="12" class="mb-4">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">TIPO (FAMILIA)</label>
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Vinculado a la Marca</span>
                            </div>
                            <v-combobox
                                :model-value="formData.Tipo"
                                @update:model-value="v => formData.Tipo = v?.toUpperCase() ?? ''"
                                :items="filteredTiposForForm"
                                item-title="Nombre"
                                item-value="Nombre"
                                placeholder="Ej. CORE I9"
                                variant="outlined"
                                density="comfortable"
                                color="primary"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                :return-object="false"
                                bg-color="grey-lighten-5"
                                :disabled="!formData.Marca"
                            ></v-combobox>
                        </v-col>

                        <!-- GENERACIÓN -->
                        <v-col cols="12" class="mb-2">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">GENERACIÓN</label>
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Vinculado al Tipo</span>
                            </div>
                            <v-combobox
                                :model-value="formData.Generacion"
                                @update:model-value="v => formData.Generacion = v?.toUpperCase() ?? ''"
                                :items="filteredGeneracionesForForm"
                                item-title="Nombre"
                                item-value="Nombre"
                                placeholder="Ej. 13TH GEN"
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
const marcas = ref([])
const tipos = ref([])
const generaciones = ref([])
const loading = ref(false)

// Filters
const search = ref('')
const filterMarca = ref(null)
const filterTipo = ref(null)

// Table
const headers = [
    { title: 'ID', key: 'Id', align: 'start', width: '80px' },
    { title: 'MARCA', key: 'Marca', align: 'start', width: '120px' },
    { title: 'TIPO', key: 'Tipo', align: 'start' },
    { title: 'GENERACIÓN', key: 'Generacion', align: 'start' },
    { title: 'ESTADO', key: 'Estado', align: 'end', width: '120px' },
    { title: '', key: 'actions', align: 'end', sortable: false, width: '50px' },
]

const tableItems = computed(() => {
    // Flatten data: Generaciones are the main rows
    let items = generaciones.value.map(gen => {
        const tipo = tipos.value.find(t => t.Id === gen.TipoId)
        const marca = tipo ? marcas.value.find(m => m.Id === tipo.MarcaId) : null
        return {
            Id: gen.Id,
            Generacion: gen.Nombre,
            Tipo: tipo ? tipo.Nombre : 'Sin Tipo',
            TipoId: gen.TipoId,
            Marca: marca ? marca.Nombre : 'Sin Marca',
            MarcaId: marca ? marca.Id : null,
            Raw: gen,
            Level: 'generacion'
        }
    })

    // Filter
    if (filterMarca.value) {
        items = items.filter(i => i.MarcaId === filterMarca.value)
    }
    if (filterTipo.value) {
        items = items.filter(i => i.TipoId === filterTipo.value)
    }

    return items
})

// Form
const formDialog = ref(false)
const saving = ref(false)
const isEditing = ref(false)
// FormData now holds strings for Marca and Tipo to allow "Find or Create"
const formData = ref({ Id: null, Generacion: '', Marca: '', Tipo: '' })

const filteredTiposForForm = computed(() => {
    // If Marca is selected (and exists in list), filter types
    const marcaObj = marcas.value.find(m => m.Nombre === formData.value.Marca)
    if (!marcaObj) return []
    return tipos.value.filter(t => t.MarcaId === marcaObj.Id)
})

const filteredGeneracionesForForm = computed(() => {
    const marcaObj = marcas.value.find(m => m.Nombre === formData.value.Marca)
    if (!marcaObj) return []
    
    const tipoObj = tipos.value.find(t => t.Nombre === formData.value.Tipo && t.MarcaId === marcaObj.Id)
    if (!tipoObj) return []
    
    return generaciones.value.filter(g => g.TipoId === tipoObj.Id)
})

// API
const API_URL = 'http://localhost:5000/api/config/catalogs'

async function loadAll() {
    loading.value = true
    try {
        const [resMarcas, resTipos, resGen] = await Promise.all([
            axios.get(`${API_URL}/marcas_procesador`, { withCredentials: true }),
            axios.get(`${API_URL}/tipos_procesador`, { withCredentials: true }),
            axios.get(`${API_URL}/generaciones_procesador`, { withCredentials: true })
        ])
        marcas.value = resMarcas.data
        tipos.value = resTipos.data
        generaciones.value = resGen.data
    } catch (e) {
        console.error("Error loading data", e)
    } finally {
        loading.value = false
    }
}

function getBrandColor(brandName) {
    const name = (brandName || '').toLowerCase()
    if (name.includes('intel')) return 'blue'
    if (name.includes('amd')) return 'red'
    if (name.includes('apple')) return 'grey'
    return 'blue-grey'
}

function openCreateDialog() {
    isEditing.value = false
    formData.value = { Id: null, Generacion: '', Marca: '', Tipo: '' }
    formDialog.value = true
}

function editItem(item) {
    isEditing.value = true
    formData.value = { 
        Id: item.Id, 
        Generacion: item.Generacion, 
        Tipo: item.Tipo,
        Marca: item.Marca 
    }
    formDialog.value = true
}

async function save() {
    if (!formData.value.Generacion || !formData.value.Marca || !formData.value.Tipo) {
        alert("Por favor complete todos los campos")
        return
    }
    saving.value = true

    try {
        // 1. Find or Create Marca
        let marcaId = null
        const existingMarca = marcas.value.find(m => m.Nombre.toLowerCase() === formData.value.Marca.toLowerCase())
        if (existingMarca) {
            marcaId = existingMarca.Id
        } else {
            const resM = await axios.post(`${API_URL}/marcas_procesador`, { Nombre: formData.value.Marca }, { withCredentials: true })
            // Assuming backend returns the created object or we reload. 
            // Standard generic create might not return ID in all implementations, but let's assume standard REST or reload.
            // If the generic create endpoint returns the created item, we use it. 
            // If not, we might need to reload and find it. 
            // Let's assume we need to reload to be safe or use the response if available.
            // The current generic implementation returns { message: "Item creado exitosamente" } usually.
            // We need to fetch the new ID.
            await loadAll() 
            const newMarca = marcas.value.find(m => m.Nombre === formData.value.Marca)
            if (newMarca) marcaId = newMarca.Id
        }

        if (!marcaId) throw new Error("Error al procesar la Marca")

        // 2. Find or Create Tipo
        let tipoId = null
        const existingTipo = tipos.value.find(t => t.Nombre.toLowerCase() === formData.value.Tipo.toLowerCase() && t.MarcaId === marcaId)
        if (existingTipo) {
            tipoId = existingTipo.Id
        } else {
            await axios.post(`${API_URL}/tipos_procesador`, { Nombre: formData.value.Tipo, MarcaId: marcaId }, { withCredentials: true })
            await loadAll()
            const newTipo = tipos.value.find(t => t.Nombre === formData.value.Tipo && t.MarcaId === marcaId)
            if (newTipo) tipoId = newTipo.Id
        }

        if (!tipoId) throw new Error("Error al procesar el Tipo")

        // 3. Create/Update Generacion
        const payload = { 
            Nombre: formData.value.Generacion,
            TipoId: tipoId
        }

        if (isEditing.value && formData.value.Id) {
            await axios.put(`${API_URL}/generaciones_procesador/${formData.value.Id}`, payload, { withCredentials: true })
        } else {
            await axios.post(`${API_URL}/generaciones_procesador`, payload, { withCredentials: true })
        }

        await loadAll()
        formDialog.value = false
    } catch (e) {
        alert("Error al guardar: " + (e.response?.data?.message || e.message))
    } finally {
        saving.value = false
    }
}

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

.border-bottom {
    border-bottom: 1px solid rgba(0,0,0,0.05);
}

.border-thin {
    border: 1px solid rgba(0,0,0,0.08) !important;
}

.gap-4 {
    gap: 16px;
}

.search-input :deep(.v-field__outline__start),
.search-input :deep(.v-field__outline__end) {
    border-color: rgba(0,0,0,0.08) !important;
}

.header-bg :deep(thead tr th) {
    background-color: #f8fafc !important;
    color: #64748b !important;
    font-weight: 600 !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.05em !important;
}
</style>
