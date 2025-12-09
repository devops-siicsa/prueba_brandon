<template>
    <div class="h-100 d-flex flex-column bg-grey-lighten-5">
        <!-- Toolbar -->
        <!-- Toolbar -->
        <div 
            class="flex-shrink-0 pa-4 d-flex align-center justify-space-between transition-all"
            :class="isEditing ? 'bg-white border-b elevation-1' : 'bg-transparent'"
        >
            <h3 class="text-h6 font-weight-bold text-grey-darken-3">
                Historial de Cambios
            </h3>
            <v-btn
                v-if="isEditing"
                color="#223551"
                :prepend-icon="!isMobileApp ? 'mdi-comment-plus-outline' : undefined"
                class="text-capitalize rounded-lg"
                :class="isMobileApp ? 'px-0' : 'px-4'"
                elevation="0"
                :height="isMobileApp ? '44' : '44'"
                :min-width="isMobileApp ? '44' : undefined"
                @click="handleAddComment"
            >
                <v-icon v-if="isMobileApp">mdi-comment-plus-outline</v-icon>
                <span v-else>Agregar Observación</span>
            </v-btn>
        </div>

        <!-- Timeline Content -->
        <div class="flex-grow-1 overflow-y-auto custom-scrollbar" :class="isMobileApp ? 'pa-2' : 'pa-4'">
            
            <!-- Loading State -->
            <div v-if="loading" class="d-flex justify-center py-8">
                <v-progress-circular indeterminate color="primary"></v-progress-circular>
            </div>

            <!-- Empty State -->
            <div v-else-if="logs.length === 0" class="d-flex flex-column align-center justify-center h-75 text-grey">
                <v-icon size="64" color="grey-lighten-2" class="mb-4">mdi-history</v-icon>
                <div class="text-h6 text-grey-darken-1 font-weight-bold">Sin historial</div>
                <div class="text-body-2 text-grey">
                    {{ equipo.Id ? 'No hay cambios registrados aún.' : 'Guarde el equipo para comenzar el historial.' }}
                </div>
            </div>

            <!-- Timeline -->
            <div v-else class="timeline-container mx-auto" style="max-width: 800px;">
                <div v-for="(log, index) in logs" :key="log.Id" class="mb-4">
                    <!-- Date Header (if different from previous) -->
                    <div v-if="shouldShowDateHeader(index)" class="d-flex align-center justify-center mb-4">
                        <div class="bg-grey-lighten-3 text-grey-darken-2 px-3 py-1 rounded-pill text-caption font-weight-bold">
                            {{ formatDateHeader(log.Fecha) }}
                        </div>
                    </div>

                    <v-card 
                        class="rounded-xl overflow-hidden transition-all"
                        :class="isEditing ? 'border-thin elevation-1' : 'border-0 bg-transparent'"
                        :variant="isEditing ? 'elevated' : 'flat'"
                    >
                        <!-- Card Header -->
                        <div 
                            class="px-4 py-3 d-flex align-center justify-space-between border-b-thin"
                            :class="isEditing ? 'bg-white' : 'bg-transparent'"
                        >
                            <div class="d-flex align-center gap-3">
                                <v-avatar color="grey-lighten-4" size="32">
                                    <span class="text-caption font-weight-bold text-corporate-blue">
                                        {{ getInitials(log.Usuario) }}
                                    </span>
                                </v-avatar>
                                <div>
                                    <div class="text-subtitle-2 font-weight-bold text-grey-darken-3">
                                        {{ log.Usuario }}
                                    </div>
                                    <div class="text-caption text-grey">
                                        {{ formatTime(log.Fecha) }}
                                    </div>
                                </div>
                            </div>
                            <v-chip
                                size="small"
                                :color="getActionColor(log.Accion)"
                                variant="flat"
                                class="font-weight-bold"
                            >
                                {{ log.Accion }}
                            </v-chip>
                        </div>

                        <!-- Card Body -->
                        <div class="pa-4" :class="isEditing ? 'bg-white' : 'bg-white rounded-xl'">
                            <div v-if="log.Accion === 'COMENTARIO'" class="text-body-2 text-grey-darken-3 bg-blue-grey-lighten-5 pa-3 rounded-lg border-thin">
                                <v-icon size="16" color="blue-grey" class="mr-2 mb-1">mdi-comment-quote-outline</v-icon>
                                <div v-html="log.Detalle" class="d-inline-block align-top ml-1 rich-text-content"></div>
                            </div>

                            <!-- Creation -->
                            <div v-else-if="log.Accion === 'CREAR'" class="text-body-2 text-grey-darken-1">
                                <v-icon size="16" color="success" class="mr-2">mdi-plus-circle-outline</v-icon>
                                {{ getCreationMessage(log.Tabla) }}
                            </div>

                            <!-- Deletion -->
                            <div v-else-if="log.Accion === 'ELIMINAR'" class="text-body-2 text-grey-darken-1">
                                <div class="font-weight-bold text-red mb-1">{{ getDeletionMessage(log.Tabla) }}</div>
                                <div v-if="isJson(log.Detalle)" class="ml-2">
                                    <div v-for="(value, field) in parseDeleted(log.Detalle)" :key="field" class="d-flex gap-2 mb-1">
                                        <span class="text-caption font-weight-bold text-grey-darken-2">{{ formatFieldName(field, log.Tabla) }}:</span>
                                        <span class="text-caption text-grey-darken-1">{{ formatValue(field, value, log.Tabla) }}</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Edits -->
                            <div v-else>
                                <div v-if="isJson(log.Detalle)">
                                    <div v-for="(change, field) in parseChanges(log.Detalle)" :key="field" class="mb-2 last-mb-0">
                                        <div v-if="field !== 'EquipoId'" class="d-flex flex-column">
                                            <div class="text-caption font-weight-bold text-grey-darken-2 mb-1">
                                                Cambio en {{ formatFieldName(field, log.Tabla) }}
                                            </div>
                                            <div class="d-flex align-center gap-2 text-body-2">
                                                <div class="bg-red-lighten-5 text-red-darken-2 px-2 py-1 rounded text-decoration-line-through">
                                                    {{ formatValue(field, change.antes, log.Tabla) }}
                                                </div>
                                                <v-icon size="16" color="grey">mdi-arrow-right</v-icon>
                                                <div class="bg-green-lighten-5 text-green-darken-2 px-2 py-1 rounded font-weight-medium">
                                                    {{ formatValue(field, change.despues, log.Tabla) }}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div v-else class="text-body-2 text-grey-darken-2">
                                    {{ log.Detalle }}
                                </div>
                            </div>
                        </div>
                    </v-card>
                </div>
            </div>
        </div>

        <!-- Add Comment Dialog -->
        <v-dialog 
            v-model="showCommentDialog" 
            :fullscreen="isDialogMaximized || isMobileApp"
            :max-width="isDialogMaximized ? undefined : 800"
            transition="dialog-bottom-transition"
        >
            <v-card class="rounded-xl d-flex flex-column">
                <v-card-title class="px-6 pt-6 pb-4 d-flex align-center justify-space-between text-h6 font-weight-bold text-corporate-blue">
                    <span>Agregar Observación</span>
                    <div class="d-flex align-center gap-2">
                        <v-btn 
                            v-if="!isMobileApp"
                            icon 
                            variant="text" 
                            color="grey-darken-1" 
                            @click="isDialogMaximized = !isDialogMaximized"
                        >
                            <v-icon>{{ isDialogMaximized ? 'mdi-window-restore' : 'mdi-window-maximize' }}</v-icon>
                            <v-tooltip activator="parent" location="bottom">
                                {{ isDialogMaximized ? 'Restaurar tamaño' : 'Maximizar' }}
                            </v-tooltip>
                        </v-btn>
                        <v-btn icon variant="text" color="grey-darken-1" @click="showCommentDialog = false">
                            <v-icon>mdi-close</v-icon>
                        </v-btn>
                    </div>
                </v-card-title>
                
                <v-card-text class="px-6 flex-grow-1 d-flex flex-column" :class="{ 'pa-0': isDialogMaximized }">
                    <div class="flex-grow-1 d-flex flex-column" style="min-height: 300px;">
                        <QuillEditor 
                            v-model:content="newComment" 
                            contentType="html"
                            theme="snow" 
                            toolbar="full"
                            placeholder="Escribe tu observación detallada aquí..."
                            class="flex-grow-1"
                            style="height: 100%;"
                        />
                    </div>
                </v-card-text>

                <v-card-actions class="px-6 pb-6 pt-4 justify-end border-t">
                    <v-btn color="grey-darken-1" variant="text" @click="showCommentDialog = false">Cancelar</v-btn>
                    <v-btn 
                        color="corporate-blue" 
                        variant="flat" 
                        class="px-6 rounded-lg" 
                        @click="submitComment"
                        :loading="submitting"
                        :disabled="!newComment || newComment === '<p><br></p>'"
                    >
                        Guardar
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-snackbar
            v-model="showErrorSnackbar"
            color="warning"
            timeout="3000"
            location="top"
        >
            {{ errorMessage }}
            <template v-slot:actions>
                <v-btn color="white" variant="text" @click="showErrorSnackbar = false">
                    Cerrar
                </v-btn>
            </template>
        </v-snackbar>
    </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import { useMobileDetection } from '@/composables/useMobileDetection'
import { useCatalogsStore } from '@/stores/catalogs'
import { storeToRefs } from 'pinia'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean
})

const { isMobileApp } = useMobileDetection()

const logs = ref([])
const loading = ref(false)
const showCommentDialog = ref(false)
const newComment = ref('') // This will now hold HTML
const submitting = ref(false)
const isDialogMaximized = ref(false)

// Quill Toolbar Options
const toolbarOptions = [
  ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
  ['blockquote', 'code-block'],

  [{ 'header': 1 }, { 'header': 2 }],               // custom button values
  [{ 'list': 'ordered'}, { 'list': 'bullet' }],
  [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
  [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
  [{ 'direction': 'rtl' }],                         // text direction

  [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
  [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

  [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
  [{ 'font': [] }],
  [{ 'align': [] }],

  ['clean']                                         // remove formatting button
]

const showErrorSnackbar = ref(false)
const errorMessage = ref('')

const emit = defineEmits(['update'])

function handleAddComment() {
    showCommentDialog.value = true
}

async function fetchLogs() {
    if (!props.equipo?.Id) {
        // If no ID, show pending comments if any
        if (props.equipo.PendingComments) {
            logs.value = props.equipo.PendingComments.map((comment, index) => ({
                Id: `temp-${index}`,
                Usuario: 'Tú (Borrador)',
                Fecha: new Date().toISOString(),
                Accion: 'COMENTARIO',
                Detalle: comment
            }))
        }
        return
    }

    loading.value = true
    try {
        const res = await axios.get('/api/audit/logs', {
            params: {
                table: 'Equipos',
                recordId: props.equipo.Id,
                per_page: 100
            },
            withCredentials: true
        })
        logs.value = res.data.logs
    } catch (e) {
        console.error("Error fetching history", e)
    } finally {
        loading.value = false
    }
}

async function submitComment() {
    if (!newComment.value.trim()) return

    submitting.value = true
    try {
        if (props.equipo?.Id) {
            // Online/Saved mode
            await axios.post('/api/audit/comments', {
                table: 'Equipos',
                recordId: props.equipo.Id,
                comment: newComment.value
            }, { withCredentials: true })
            await fetchLogs()
        } else {
            // Offline/Pre-save mode
            const currentComments = props.equipo.PendingComments || []
            const updatedComments = [...currentComments, newComment.value]
            
            // Emit update to parent
            // We assume the parent handles 'PendingComments' field
            // Since updateEquipoField does equipo[field] = value, this works.
            emit('update', 'PendingComments', updatedComments)
            
            // Manually update local logs for immediate feedback
            logs.value.unshift({
                Id: `temp-${Date.now()}`,
                Usuario: 'Tú (Borrador)',
                Fecha: new Date().toISOString(),
                Accion: 'COMENTARIO',
                Detalle: newComment.value
            })
        }
        
        newComment.value = ''
        showCommentDialog.value = false
    } catch (e) {
        console.error("Error submitting comment", e)
        errorMessage.value = "Error al guardar comentario"
        showErrorSnackbar.value = true
    } finally {
        submitting.value = false
    }
}

// Helpers
function shouldShowDateHeader(index) {
    if (index === 0) return true
    const current = new Date(logs.value[index].Fecha).toDateString()
    const prev = new Date(logs.value[index - 1].Fecha).toDateString()
    return current !== prev
}

function formatDateHeader(dateStr) {
    return new Date(dateStr).toLocaleDateString('es-ES', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
}

function formatTime(dateStr) {
    return new Date(dateStr).toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' })
}

function getInitials(name) {
    return name ? name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase() : '??'
}

function getActionColor(action) {
    switch (action) {
        case 'CREAR': return 'success'
        case 'EDITAR': return 'warning'
        case 'ELIMINAR': return 'error'
        case 'COMENTARIO': return 'info'
        default: return 'grey'
    }
}

function isJson(str) {
    try {
        JSON.parse(str)
        return true
    } catch (e) {
        return false
    }
}

function parseChanges(jsonStr) {
    try {
        return JSON.parse(jsonStr)
    } catch (e) {
        return {}
    }
}

function parseDeleted(jsonStr) {
    try {
        const obj = JSON.parse(jsonStr)
        // Exclude internal fields
        const ignored = ['Id', 'EquipoId', 'UsuarioId', 'TenantId']
        const result = {}
        for (const key in obj) {
            if (!ignored.includes(key) && obj[key] !== null) {
                result[key] = obj[key]
            }
        }
        return result
    } catch (e) {
        return {}
    }
}

function formatFieldName(field, table) {
    // Map technical names to user friendly names
    const map = {
        'UsuarioId': 'Usuario Asignado',
        'EstadoEquipoId': 'Estado',
        'SedeId': 'Sede',
        'EmpresaId': 'Empresa',
        'TipoEquipoId': 'Tipo de Equipo',
        'FabricanteId': 'Fabricante',
        'Modelo': 'Modelo',
        'Serial': 'Número de Serie',
        'CodigoEquipo': 'Código Interno',
        'SistemaOperativoId': 'Sistema Operativo',
        'LicenciaSO': 'Licencia S.O.',
        'OfimaticaId': 'Ofimática',
        'AntivirusId': 'Antivirus',
        'NombreEnRed': 'Nombre en Red',
        'DireccionIP': 'Dirección IP',
        'MacAddress': 'Dirección MAC',
        'AnioAdquisicion': 'Año Adquisición',
        'CapacidadId': 'Capacidad',
        'BusId': 'Velocidad/Bus',
        'GeneracionId': 'Generación',
        'ProtocoloId': 'Protocolo',
        'FactorFormaId': 'Factor de Forma'
    }

    // Contextual overrides
    if (field === 'CapacidadId') {
        if (table === 'EquipoRAM') return 'Capacidad (RAM)'
        if (table === 'EquipoAlmacenamiento') return 'Capacidad (Disco)'
    }
    if (field === 'SlotNumero') {
        if (table === 'EquipoRAM') return 'Slot RAM'
        if (table === 'EquipoAlmacenamiento') return 'Slot Disco'
    }

    return map[field] || field
}

// Catalogs Store
const catalogsStore = useCatalogsStore()
const { 
    tiposEquipo, estadosEquipo, fabricantes, sistemasOperativos, ofimaticas, antivirus,
    capacidadesRam, busesRam, generacionesProcesador,
    capacidadesAlmacenamiento, protocolosAlmacenamiento, factoresFormaAlmacenamiento
} = storeToRefs(catalogsStore)

function formatValue(field, value, table) {
    if (value === null || value === undefined || value === '') return 'Vacío'
    
    let catalog = null
    // Assign catalog based on field name and table context
    if (field === 'TipoEquipoId') catalog = tiposEquipo.value
    else if (field === 'EstadoEquipoId') catalog = estadosEquipo.value
    else if (field === 'FabricanteId') catalog = fabricantes.value
    else if (field === 'SistemaOperativoId') catalog = sistemasOperativos.value
    else if (field === 'OfimaticaId') catalog = ofimaticas.value
    else if (field === 'AntivirusId') catalog = antivirus.value
    // Hardware Mappings
    else if (field === 'CapacidadId') {
        if (table === 'EquipoRAM') catalog = capacidadesRam.value
        else if (table === 'EquipoAlmacenamiento') catalog = capacidadesAlmacenamiento.value
    }
    else if (field === 'BusId') catalog = busesRam.value
    else if (field === 'GeneracionId') catalog = generacionesProcesador.value
    else if (field === 'ProtocoloId') catalog = protocolosAlmacenamiento.value
    else if (field === 'FactorFormaId') catalog = factoresFormaAlmacenamiento.value
    
    // Look up
    if (catalog && Array.isArray(catalog)) {
        const item = catalog.find(i => i.Id == value) // Loose equality for string/int mismatch
        if (item) {
            // Special formatting for RAM Bus (Type + Speed)
            if (field === 'BusId' && item.TipoNombre) {
                return `${item.TipoNombre} - ${item.Nombre}`
            }
            // Special formatting for Storage Protocol (Type + Protocol)
            if (field === 'ProtocoloId' && item.TipoNombre) {
                return `${item.TipoNombre} - ${item.Nombre}`
            }
            // Special formatting for Processor (Brand + Type + Generation)
            if (field === 'GeneracionId') {
                const parts = []
                if (item.MarcaNombre) parts.push(item.MarcaNombre)
                if (item.TipoNombre) parts.push(item.TipoNombre)
                parts.push(item.Nombre)
                return parts.join(' ')
            }
            // Fallback for others
            return item.Nombre || item.Capacidad || item.Velocidad || item.Descripcion || item.Generacion
        }
    }
    
    return value
}

function getCreationMessage(table) {
    if (table.includes('RAM')) return 'Memoria RAM agregada.'
    if (table.includes('Procesador')) return 'Procesador agregado.'
    if (table.includes('Almacenamiento')) return 'Disco de almacenamiento agregado.'
    if (table.includes('Aplicaciones')) return 'Aplicación asignada.'
    if (table.includes('Adjuntos')) return 'Archivo adjunto subido.'
    return 'Elemento creado exitosamente.'
}

function getDeletionMessage(table) {
    if (table.includes('RAM')) return 'Memoria RAM eliminada.'
    if (table.includes('Procesador')) return 'Procesador eliminado.'
    if (table.includes('Almacenamiento')) return 'Disco de almacenamiento eliminado.'
    if (table.includes('Aplicaciones')) return 'Aplicación desasignada.'
    if (table.includes('Adjuntos')) return 'Archivo adjunto eliminado.'
    return 'Elemento eliminado exitosamente.'
}

onMounted(() => {
    catalogsStore.fetchCatalogs([
        'tiposEquipo', 'estadosEquipo', 'fabricantes', 'sistemasOperativos', 'ofimaticas', 'antivirus',
        'capacidadesRam', 'busesRam', 'generacionesProcesador',
        'capacidadesAlmacenamiento', 'protocolosAlmacenamiento', 'factoresFormaAlmacenamiento'
    ])
    fetchLogs()
})

watch(() => props.equipo?.Id, (newId) => {
    if (newId) fetchLogs()
})
</script>

<style scoped>
.gap-2 { gap: 8px; }
.gap-3 { gap: 12px; }
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }
.border-b-thin { border-bottom: 1px solid rgba(0,0,0,0.08) !important; }
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background-color: rgba(0,0,0,0.1); border-radius: 20px; }
.last-mb-0:last-child { margin-bottom: 0 !important; }
</style>
