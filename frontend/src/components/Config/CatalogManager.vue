<template>
  <v-card flat>
    <v-card-title class="d-flex align-center">
      {{ title }}
      <v-spacer></v-spacer>
      <v-btn 
        color="primary" 
        prepend-icon="mdi-plus" 
        size="small"
        @click="dialog = true"
        v-permission="'catalogs:create'"
      >
        Nuevo
      </v-btn>
    </v-card-title>
    
    <v-card-text>
      <v-data-table
        :headers="headers"
        :items="items"
        :loading="loading"
        density="compact"
      >
        <template v-slot:item.Activo="{ item }">
            <v-chip :color="item.Activo ? 'success' : 'error'" size="x-small">
                {{ item.Activo ? 'Activo' : 'Inactivo' }}
            </v-chip>
        </template>
      </v-data-table>
    </v-card-text>

    <!-- Dialogo Crear -->
    <v-dialog v-model="dialog" max-width="400">
        <v-card>
            <v-card-title>Nuevo Item</v-card-title>
            <v-card-text>
                <v-text-field v-model="newItemName" label="Nombre" variant="outlined" autofocus></v-text-field>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="grey" variant="text" @click="dialog = false">Cancelar</v-btn>
                <v-btn color="primary" @click="saveItem" :loading="saving">Guardar</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
    catalogName: { type: String, required: true },
    title: { type: String, default: 'Catálogo' }
})

const items = ref([])
const loading = ref(false)
const dialog = ref(false)
const newItemName = ref('')
const saving = ref(false)

const headers = [
    { title: 'ID', key: 'Id', width: '80px' },
    { title: 'Nombre', key: 'Nombre' }, // Asumimos Nombre por defecto, ajustar si es Capacidad
    { title: 'Estado', key: 'Activo', width: '100px' }
]

async function loadItems() {
    loading.value = true
    try {
        const res = await axios.get(`/api/config/catalogs/${props.catalogName}`, { withCredentials: true })
        items.value = res.data
    } catch (e) {
        console.error("Error cargando catalogo", e)
    } finally {
        loading.value = false
    }
}

async function saveItem() {
    if(!newItemName.value) return
    saving.value = true
    try {
        // Ajuste simple: enviamos 'Nombre'. Si el backend espera 'Capacidad', el servicio debe manejarlo o el componente ser mas listo.
        // Por ahora asumo que la mayoría usa Nombre.
        await axios.post(`/api/config/catalogs/${props.catalogName}`, {
            Nombre: newItemName.value
        }, { withCredentials: true })
        
        dialog.value = false
        newItemName.value = ''
        loadItems()
    } catch (e) {
        alert("Error al guardar: " + (e.response?.data?.message || e.message))
    } finally {
        saving.value = false
    }
}

watch(() => props.catalogName, loadItems)
onMounted(loadItems)
</script>
