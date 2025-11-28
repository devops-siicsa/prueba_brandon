<template>
  <v-dialog v-model="dialog" max-width="700" height="auto" scrollable transition="dialog-bottom-transition">
    <v-card class="rounded-xl elevation-24">
      <!-- Header Personalizado -->
      <div class="px-8 pt-8 pb-4 d-flex justify-space-between align-start">
        <div class="d-flex align-center">
            <div class="header-icon-box mr-4">
                <v-icon color="primary" size="32">{{ icon }}</v-icon>
            </div>
            <div>
                <h2 class="text-h5 font-weight-bold text-grey-darken-3 mb-1">{{ title }}</h2>
                <p class="text-body-2 text-grey">{{ description }}</p>
            </div>
        </div>
        <v-btn icon="mdi-close" variant="text" color="grey" @click="dialog = false"></v-btn>
      </div>

      <v-divider class="mx-8"></v-divider>

      <v-card-text class="px-8 py-6 bg-grey-lighten-5">
        <!-- Barra de Herramientas -->
        <v-row class="mb-6 align-center">
            <v-col cols="12" md="4">
                <v-text-field
                    v-model="search"
                    prepend-inner-icon="mdi-magnify"
                    :label="`Buscar en ${title}...`"
                    variant="outlined"
                    density="compact"
                    hide-details
                    bg-color="white"
                    color="primary"
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
                    color="primary"
                    class="rounded-lg"
                ></v-select>
            </v-col>

            <v-spacer></v-spacer>
            <v-col cols="12" md="auto">
                <v-btn 
                    color="#1e293b" 
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
    </v-card>

    <!-- Dialogo Formulario (Crear/Editar) -->
    <v-dialog v-model="formDialog" max-width="500" persistent>
        <v-card class="rounded-xl">
            <v-card-title class="px-6 pt-6 pb-2 d-flex align-center justify-space-between">
                <span class="text-h6 font-weight-bold text-grey-darken-3">
                    {{ editedItem.Id ? 'Editar Registro' : 'Nuevo Registro' }}
                </span>
                <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="closeForm"></v-btn>
            </v-card-title>
            
            <v-divider class="mx-6"></v-divider>

            <v-card-text class="px-6 py-4">
                <v-form ref="form" @submit.prevent="save">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">NOMBRE</label>
                    <v-text-field
                        v-model="editedItem.Nombre"
                        placeholder="Ingrese el nombre"
                        variant="outlined"
                        density="compact"
                        bg-color="grey-lighten-5"
                        class="rounded-lg mb-4"
                        :rules="[v => !!v || 'El nombre es requerido']"
                        hide-details="auto"
                        autofocus
                    ></v-text-field>

                    <div v-if="editedItem.Id">
                        <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">ESTADO</label>
                        <v-switch
                            v-model="editedItem.Activo"
                            color="primary"
                            :label="editedItem.Activo ? 'Activo' : 'Inactivo'"
                            hide-details
                            inset
                        ></v-switch>
                    </div>
                </v-form>
            </v-card-text>

            <v-card-actions class="px-6 pb-6 pt-2">
                <v-spacer></v-spacer>
                <v-btn variant="text" color="grey-darken-1" class="text-capitalize" @click="closeForm">Cancelar</v-btn>
                <v-btn 
                    color="#1e293b" 
                    variant="flat" 
                    class="text-white text-capitalize rounded-lg px-6"
                    @click="save"
                    :loading="saving"
                >
                    Guardar
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
  </v-dialog>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
    modelValue: Boolean,
    catalogName: { type: String, required: true },
    title: { type: String, required: true },
    icon: { type: String, default: 'mdi-database' },
    description: { type: String, default: 'Gestión de catálogo del sistema.' }
})

const emit = defineEmits(['update:modelValue'])

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

const items = ref([])
const loading = ref(false)
const search = ref('')
const formDialog = ref(false)
const saving = ref(false)
const form = ref(null)
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
        const res = await axios.get(`http://localhost:5000/api/config/catalogs/${props.catalogName}`, { withCredentials: true })
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

function closeForm() {
    formDialog.value = false
    editedItem.value = { ...defaultItem }
}

async function save() {
    const { valid } = await form.value.validate()
    if (!valid) return

    saving.value = true
    try {
        const url = `http://localhost:5000/api/config/catalogs/${props.catalogName}`
        
        if (editedItem.value.Id) {
            await axios.put(`${url}/${editedItem.value.Id}`, editedItem.value, { withCredentials: true })
        } else {
            await axios.post(url, { Nombre: editedItem.value.Nombre }, { withCredentials: true })
        }
        
        await loadItems()
        closeForm()
    } catch (e) {
        console.error(e)
        alert("Error al guardar: " + (e.response?.data?.message || e.message))
    } finally {
        saving.value = false
    }
}

watch(dialog, (val) => {
    if (val) loadItems()
}, { immediate: true })

// Recargar si cambia el catálogo mientras el diálogo está abierto
watch(() => props.catalogName, () => {
    if (dialog.value) loadItems()
})

onMounted(() => {
    if (dialog.value) loadItems()
})
</script>

<style scoped>
.header-icon-box {
    width: 56px;
    height: 56px;
    background-color: #e3f2fd;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
