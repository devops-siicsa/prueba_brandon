<template>
  <v-dialog v-model="dialog" :fullscreen="isMobileApp" :max-width="isMobileApp ? '100%' : '1000px'" scrollable transition="dialog-bottom-transition">
    <v-card class="bg-grey-lighten-5 rounded-xl" :height="isMobileApp ? '100%' : '700'">
      <!-- Header -->
      <div :class="[isMobileApp ? 'px-4 py-3' : 'px-8 pt-6 pb-6', 'bg-white elevation-0 border-bottom']">
        <div class="d-flex align-center justify-space-between">
            <div class="d-flex align-center">
                <div class="header-icon-box mr-4 bg-teal-lighten-5" :style="isMobileApp ? 'width: 40px; height: 40px;' : ''">
                    <v-icon color="teal-darken-1" :size="isMobileApp ? 24 : 28">mdi-harddisk</v-icon>
                </div>
                <div>
                    <h2 :class="[isMobileApp ? 'text-subtitle-1' : 'text-h6', 'font-weight-bold text-grey-darken-3 mb-0']">Almacenamiento</h2>
                    <p class="text-caption text-grey">Gestiona tipos, protocolos y factores de forma.</p>
                </div>
            </div>
            <v-btn icon="mdi-close" variant="text" color="grey" @click="dialog = false"></v-btn>
        </div>

        <!-- Toolbar -->
        <div class="mt-6 d-flex align-center flex-wrap gap-4">
            <div :style="isMobileApp ? 'width: 100%;' : 'width: 280px;'">
                <v-text-field
                    v-model="search"
                    prepend-inner-icon="mdi-magnify"
                    placeholder="Buscar almacenamiento..."
                    variant="outlined"
                    density="compact"
                    hide-details
                    bg-color="white"
                    class="rounded-lg search-input"
                ></v-text-field>
            </div>
            
            <v-spacer v-if="!isMobileApp"></v-spacer>

            <div :class="isMobileApp ? 'd-flex w-100 gap-2' : 'd-flex'">
                <v-btn 
                    color="blue-grey-lighten-4" 
                    variant="flat"
                    :class="[isMobileApp ? 'flex-grow-1' : 'mr-2', 'text-blue-grey-darken-4 text-capitalize rounded-lg px-4']" 
                    height="40"
                    prepend-icon="mdi-database-plus" 
                    elevation="0"
                    @click="openCapacityDialog"
                >
                Capacidad
                </v-btn>

                <v-btn 
                    color="#1e293b" 
                    :class="[isMobileApp ? 'flex-grow-1' : '', 'text-white text-capitalize rounded-lg px-6']" 
                    height="40"
                    prepend-icon="mdi-plus" 
                    elevation="0"
                    @click="openCreateDialog"
                >
                Tipo
                </v-btn>
            </div>
        </div>
      </div>

      <v-container fluid :class="isMobileApp ? 'pa-4' : 'pa-8'">
        <!-- VISTA DE ESCRITORIO: Tabla -->
        <v-card v-if="!isMobileApp" class="rounded-lg border-thin elevation-0 overflow-hidden">
            <v-data-table
                :headers="headers"
                :items="tableItems"
                :loading="loading"
                hover
                class="header-bg cursor-pointer"
                @click:row="editItem"
            >
                <!-- TIPO -->
                <template v-slot:item.Tipo="{ item }">
                    <v-chip
                        size="small"
                        color="indigo"
                        variant="flat"
                        class="font-weight-bold bg-indigo-lighten-5 text-indigo-darken-2"
                    >
                        {{ item.Tipo }}
                    </v-chip>
                </template>

                <!-- PROTOCOLOS -->
                <template v-slot:item.Protocolos="{ item }">
                    <div class="d-flex flex-wrap gap-1">
                        <v-chip 
                            v-for="p in item.Protocolos" 
                            :key="p.Id"
                            size="x-small"
                            class="mr-1 mb-1"
                            :color="p.Activo ? 'blue' : 'grey'"
                            variant="tonal"
                        >
                            {{ p.Nombre }}
                        </v-chip>
                        <span v-if="item.Protocolos.length === 0" class="text-caption text-grey">-</span>
                    </div>
                </template>

                <!-- FACTORES DE FORMA -->
                <template v-slot:item.Factores="{ item }">
                    <div class="d-flex flex-wrap gap-1">
                        <v-chip 
                            v-for="f in item.Factores" 
                            :key="f.Id"
                            size="x-small"
                            class="mr-1 mb-1"
                            :color="f.Activo ? 'purple' : 'grey'"
                            variant="tonal"
                        >
                            {{ f.Nombre }}
                        </v-chip>
                        <span v-if="item.Factores.length === 0" class="text-caption text-grey">-</span>
                    </div>
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

        <!-- VISTA MÓVIL: Lista de Tarjetas -->
        <div v-else>
             <!-- Estado Vacío Móvil -->
            <div v-if="tableItems.length === 0" class="d-flex flex-column align-center justify-center py-12 text-center">
                <div class="empty-state-icon mb-6" style="width: 72px; height: 72px; background-color: #e8eaf6; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                    <v-icon size="36" color="indigo-lighten-2">mdi-harddisk</v-icon>
                </div>
                <h3 class="text-subtitle-1 font-weight-bold text-grey-darken-3 mb-2">No se encontraron tipos</h3>
                <v-btn color="indigo-darken-3" variant="tonal" class="text-capitalize rounded-lg" prepend-icon="mdi-plus" @click="openCreateDialog">
                    Agregar nuevo
                </v-btn>
            </div>

            <v-row v-else dense>
                <v-col cols="12" v-for="item in tableItems" :key="item.Id">
                    <v-card hover @click="editItem(null, { item })" class="border-thin elevation-0 rounded-lg">
                        <div class="d-flex align-center pa-3">
                            <!-- Icono -->
                            <div class="mr-3">
                                <v-avatar color="indigo-lighten-5" size="40" class="rounded-lg">
                                    <v-icon color="indigo-darken-1" size="20">mdi-harddisk</v-icon>
                                </v-avatar>
                            </div>
                            
                            <!-- Info -->
                            <div class="flex-grow-1" style="min-width: 0;">
                                <div class="d-flex align-center mb-1">
                                    <span class="text-subtitle-2 font-weight-bold text-grey-darken-3 text-truncate mr-2">
                                        {{ item.Tipo }}
                                    </span>
                                    <v-chip size="x-small" :color="item.Activo ? 'success' : 'grey'" variant="flat" class="font-weight-bold">
                                        {{ item.Activo ? 'Activo' : 'Inactivo' }}
                                    </v-chip>
                                </div>
                                
                                <div class="d-flex flex-wrap gap-1 mt-1">
                                    <span v-if="item.Protocolos.length > 0" class="text-caption text-grey mr-1">
                                        {{ item.Protocolos.length }} Protocolos
                                    </span>
                                    <span v-if="item.Factores.length > 0" class="text-caption text-grey">
                                        {{ item.Factores.length }} Factores
                                    </span>
                                    <span v-if="item.Protocolos.length === 0 && item.Factores.length === 0" class="text-caption text-grey font-italic">
                                        Sin configuración
                                    </span>
                                </div>
                            </div>

                            <!-- Chevron -->
                            <div class="ml-2">
                                <v-icon color="grey-lighten-1">mdi-chevron-right</v-icon>
                            </div>
                        </div>
                    </v-card>
                </v-col>
            </v-row>
        </div>
      </v-container>
    </v-card>

    <!-- Dialogo Crear Tipo -->
    <v-dialog v-model="formDialog" max-width="500" persistent>
        <v-card class="rounded-xl pa-4">
            <v-card-title class="px-4 pt-2 pb-2 d-flex align-start justify-space-between">
                <div>
                    <span class="text-h6 font-weight-bold text-blue-grey-darken-4">
                        Nuevo Tipo de Almacenamiento
                    </span>
                    <p class="text-caption text-grey mt-1">Define un tipo base (ej. SSD, M.2).</p>
                </div>
                <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="formDialog = false"></v-btn>
            </v-card-title>
            
            <v-divider class="mx-4 opacity-10 mb-4"></v-divider>

            <v-card-text class="px-4 py-0">
                <v-form @submit.prevent="saveType">
                    <v-row no-gutters>
                        <v-col cols="12" class="mb-4">
                            <div class="d-flex justify-space-between align-center mb-1">
                                <label class="text-caption font-weight-bold text-grey-darken-1">NOMBRE DEL TIPO</label>
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Ej. NVMe, SAS</span>
                            </div>
                            <v-text-field
                                v-model="newTypeName"
                                placeholder="Ej. NVMe"
                                variant="outlined"
                                density="comfortable"
                                color="primary"
                                class="rounded-lg text-uppercase"
                                hide-details="auto"
                                bg-color="grey-lighten-5"
                                @update:model-value="v => newTypeName = v?.toUpperCase() ?? ''"
                            ></v-text-field>
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
                    @click="saveType" 
                    :loading="saving"
                >
                    <v-icon start class="mr-2">mdi-content-save-outline</v-icon>
                    Guardar
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <!-- Dialogo Editar Tipo y Detalles -->
    <v-dialog v-model="editDialog" max-width="600" persistent>
        <v-card class="rounded-xl pa-4">
            <v-card-title class="px-4 pt-2 pb-2 d-flex align-start justify-space-between">
                <div>
                    <span class="text-h6 font-weight-bold text-blue-grey-darken-4">
                        Configurar {{ editData.Tipo }}
                    </span>
                    <p class="text-caption text-grey mt-1">Gestiona protocolos y factores de forma asociados.</p>
                </div>
                <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="editDialog = false"></v-btn>
            </v-card-title>
            
            <v-divider class="mx-4 opacity-10 mb-4"></v-divider>

            <v-card-text class="px-4 py-0" style="max-height: 600px; overflow-y: auto;">
                
                <!-- PROTOCOLOS -->
                <div class="mb-6">
                    <div class="d-flex align-center justify-space-between mb-2">
                        <label class="text-subtitle-2 font-weight-bold text-blue-grey-darken-3">Protocolos</label>
                        <v-btn size="small" variant="text" color="primary" prepend-icon="mdi-plus" @click="addProtocol">Agregar</v-btn>
                    </div>
                    <v-sheet border class="rounded-lg pa-0 overflow-hidden">
                        <v-list density="compact" class="py-0">
                            <v-list-item v-for="p in editData.Protocolos" :key="p.Id" :title="p.Nombre">
                                <template v-slot:append>
                                    <v-switch
                                        v-model="p.Activo"
                                        color="success"
                                        density="compact"
                                        hide-details
                                        inset
                                        @update:model-value="updateProtocolStatus(p)"
                                    ></v-switch>
                                </template>
                            </v-list-item>
                            <v-list-item v-if="editData.Protocolos.length === 0">
                                <span class="text-caption text-grey font-italic">No hay protocolos definidos</span>
                            </v-list-item>
                        </v-list>
                    </v-sheet>
                </div>

                <!-- FACTORES DE FORMA -->
                <div>
                    <div class="d-flex align-center justify-space-between mb-2">
                        <label class="text-subtitle-2 font-weight-bold text-blue-grey-darken-3">Factores de Forma</label>
                        <v-btn size="small" variant="text" color="primary" prepend-icon="mdi-plus" @click="addFactor">Agregar</v-btn>
                    </div>
                    <v-sheet border class="rounded-lg pa-0 overflow-hidden">
                        <v-list density="compact" class="py-0">
                            <v-list-item v-for="f in editData.Factores" :key="f.Id" :title="f.Nombre">
                                <template v-slot:append>
                                    <v-switch
                                        v-model="f.Activo"
                                        color="success"
                                        density="compact"
                                        hide-details
                                        inset
                                        @update:model-value="updateFactorStatus(f)"
                                    ></v-switch>
                                </template>
                            </v-list-item>
                            <v-list-item v-if="editData.Factores.length === 0">
                                <span class="text-caption text-grey font-italic">No hay factores definidos</span>
                            </v-list-item>
                        </v-list>
                    </v-sheet>
                </div>

            </v-card-text>

            <v-card-actions class="px-4 pb-2 pt-4">
                <v-spacer></v-spacer>
                <v-btn 
                    color="#1e293b" 
                    variant="flat" 
                    class="text-white text-capitalize rounded-lg px-6"
                    height="44"
                    @click="editDialog = false" 
                >
                    Listo
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <!-- Dialogo Agregar Item (Protocolo/Factor) -->
    <v-dialog v-model="addItemDialog" max-width="400" persistent>
        <v-card class="rounded-xl pa-4">
            <v-card-title class="px-4 pt-2 pb-2">
                <span class="text-h6 font-weight-bold text-blue-grey-darken-4">
                    Nuevo {{ addItemType === 'protocol' ? 'Protocolo' : 'Factor de Forma' }}
                </span>
            </v-card-title>
            <v-card-text class="px-4 py-0">
                <v-text-field
                    v-model="newItemName"
                    :placeholder="addItemType === 'protocol' ? 'Ej. SATA' : 'Ej. 2.5'"
                    variant="outlined"
                    density="comfortable"
                    color="primary"
                    class="rounded-lg text-uppercase"
                    hide-details="auto"
                    bg-color="grey-lighten-5"
                    @update:model-value="v => newItemName = v?.toUpperCase() ?? ''"
                    autofocus
                ></v-text-field>
            </v-card-text>
            <v-card-actions class="px-4 pb-2 pt-4">
                <v-spacer></v-spacer>
                <v-btn variant="text" color="grey" @click="addItemDialog = false">Cancelar</v-btn>
                <v-btn color="primary" variant="flat" @click="saveNewItem" :loading="savingItem">Guardar</v-btn>
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
                                <span class="text-caption text-grey-lighten-1" style="font-size: 10px;">Selecciona o escribe (ej. 512GB)</span>
                            </div>
                            <v-combobox
                                v-model="newCapacity"
                                :items="capacidades"
                                item-title="Nombre"
                                item-value="Nombre"
                                placeholder="Ej. 512GB"
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
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    modelValue: Boolean
})

const { isMobileApp } = useMobileDetection()

const emit = defineEmits(['update:modelValue'])

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

// Data
const tipos = ref([])
const capacidades = ref([])
const protocolos = ref([])
const factores = ref([])
const loading = ref(false)
const search = ref('')

// Table
const headers = [
    { title: 'TIPO', key: 'Tipo', align: 'start', width: '150px' },
    { title: 'PROTOCOLOS', key: 'Protocolos', align: 'start' },
    { title: 'FACTORES DE FORMA', key: 'Factores', align: 'start' },
    { title: 'ESTADO', key: 'Estado', align: 'end', width: '120px' },
]

const tableItems = computed(() => {
    let items = tipos.value.map(t => {
        return {
            Id: t.Id,
            Tipo: t.Nombre,
            Activo: t.Activo,
            Protocolos: protocolos.value.filter(p => p.TipoId === t.Id),
            Factores: factores.value.filter(f => f.TipoId === t.Id)
        }
    })

    if (search.value) {
        const q = search.value.toUpperCase()
        items = items.filter(i => 
            i.Tipo.includes(q) || 
            i.Protocolos.some(p => p.Nombre.includes(q)) ||
            i.Factores.some(f => f.Nombre.includes(q))
        )
    }

    return items
})

// Dialogs
const formDialog = ref(false)
const saving = ref(false)
const newTypeName = ref('')

const editDialog = ref(false)
const editData = ref({ Id: null, Tipo: '', Protocolos: [], Factores: [] })

const capacityDialog = ref(false)
const savingCapacity = ref(false)
const newCapacity = ref('')

const addItemDialog = ref(false)
const addItemType = ref('protocol') // 'protocol' or 'factor'
const newItemName = ref('')
const savingItem = ref(false)

// API
const API_URL = '/api/config'

async function loadAll() {
    loading.value = true
    try {
        const [resTipos, resCaps, resProtos, resFacts] = await Promise.all([
            axios.get(`${API_URL}/tipos_almacenamiento`, { withCredentials: true }),
            axios.get(`${API_URL}/capacidades_almacenamiento`, { withCredentials: true }),
            axios.get(`${API_URL}/protocolos_almacenamiento`, { withCredentials: true }),
            axios.get(`${API_URL}/factores_forma_almacenamiento`, { withCredentials: true })
        ])
        tipos.value = resTipos.data
        capacidades.value = resCaps.data
        protocolos.value = resProtos.data
        factores.value = resFacts.data
    } catch (e) {
        console.error("Error loading Storage data", e)
    } finally {
        loading.value = false
    }
}

function openCreateDialog() {
    newTypeName.value = ''
    formDialog.value = true
}

async function saveType() {
    if (!newTypeName.value) return
    saving.value = true
    try {
        await axios.post(`${API_URL}/tipos_almacenamiento`, { Nombre: newTypeName.value }, { withCredentials: true })
        await loadAll()
        formDialog.value = false
    } catch (e) {
        alert("Error: " + e.message)
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
        await axios.post(`${API_URL}/capacidades_almacenamiento`, { Nombre: newCapacity.value }, { withCredentials: true })
        await loadAll()
        capacityDialog.value = false
    } catch (e) {
        alert("Error: " + e.message)
    } finally {
        savingCapacity.value = false
    }
}

function editItem(event, { item }) {
    editData.value = {
        Id: item.Id,
        Tipo: item.Tipo,
        Protocolos: item.Protocolos, // Reference to reactive objects
        Factores: item.Factores
    }
    editDialog.value = true
}

function addProtocol() {
    addItemType.value = 'protocol'
    newItemName.value = ''
    addItemDialog.value = true
}

function addFactor() {
    addItemType.value = 'factor'
    newItemName.value = ''
    addItemDialog.value = true
}

async function saveNewItem() {
    if (!newItemName.value) return
    savingItem.value = true
    try {
        const endpoint = addItemType.value === 'protocol' ? 'protocolos_almacenamiento' : 'factores_forma_almacenamiento'
        await axios.post(`${API_URL}/${endpoint}`, {
            Nombre: newItemName.value,
            TipoId: editData.value.Id
        }, { withCredentials: true })
        
        await loadAll()
        // Update editData references
        const updatedItem = tableItems.value.find(i => i.Id === editData.value.Id)
        if (updatedItem) {
            editData.value.Protocolos = updatedItem.Protocolos
            editData.value.Factores = updatedItem.Factores
        }
        addItemDialog.value = false
    } catch (e) {
        alert("Error: " + e.message)
    } finally {
        savingItem.value = false
    }
}

async function updateProtocolStatus(item) {
    try {
        await axios.put(`${API_URL}/protocolos_almacenamiento/${item.Id}`, { Activo: item.Activo }, { withCredentials: true })
    } catch (e) {
        console.error(e)
        item.Activo = !item.Activo // Revert
    }
}

async function updateFactorStatus(item) {
    try {
        await axios.put(`${API_URL}/factores_forma_almacenamiento/${item.Id}`, { Activo: item.Activo }, { withCredentials: true })
    } catch (e) {
        console.error(e)
        item.Activo = !item.Activo // Revert
    }
}

onMounted(() => {
    loadAll()
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
.gap-4 { gap: 16px; }
.search-input :deep(.v-field__outline__start),
.search-input :deep(.v-field__outline__end) { border-color: rgba(0,0,0,0.08) !important; }
</style>
