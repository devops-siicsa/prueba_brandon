<template>
    <div class="h-100 d-flex flex-column bg-grey-lighten-5">
        <!-- Toolbar -->
        <div class="flex-shrink-0 pa-4 bg-white border-b d-flex align-center justify-space-between">
            <h3 class="text-h6 font-weight-bold text-grey-darken-3">
                Historial de Cambios
            </h3>
            <v-btn
                color="#223551"
                prepend-icon="mdi-comment-plus-outline"
                class="text-capitalize rounded-lg px-4"
                elevation="0"
                @click="handleAddComment"
            >
                Agregar Observación
            </v-btn>
        </div>

        <!-- Timeline Content -->
        <div class="flex-grow-1 overflow-y-auto custom-scrollbar pa-4">
            
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

                    <v-card class="rounded-xl border-thin elevation-0 overflow-hidden">
                        <!-- Card Header -->
                        <div class="px-4 py-3 d-flex align-center justify-space-between bg-white border-b-thin">
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
                        <div class="pa-4 bg-white">
                            <div v-if="log.Accion === 'COMENTARIO'" class="text-body-2 text-grey-darken-3 bg-blue-grey-lighten-5 pa-3 rounded-lg border-thin">
                                <v-icon size="16" color="blue-grey" class="mr-2 mb-1">mdi-comment-quote-outline</v-icon>
                                <div v-html="log.Detalle" class="d-inline-block align-top ml-1 rich-text-content"></div>
                            </div>

                            <!-- Creation -->
                            <div v-else-if="log.Accion === 'CREAR'" class="text-body-2 text-grey-darken-1">
                                <v-icon size="16" color="success" class="mr-2">mdi-plus-circle-outline</v-icon>
                                Equipo creado exitosamente.
                            </div>

                            <!-- Edits -->
                            <div v-else>
                                <div v-if="isJson(log.Detalle)">
                                    <div v-for="(change, field) in parseChanges(log.Detalle)" :key="field" class="mb-2 last-mb-0">
                                        <div class="text-caption font-weight-bold text-grey-darken-2 mb-1">
                                            Cambio en {{ formatFieldName(field) }}
                                        </div>
                                        <div class="d-flex align-center gap-2 text-body-2">
                                            <div class="bg-red-lighten-5 text-red-darken-2 px-2 py-1 rounded text-decoration-line-through">
                                                {{ change.antes || 'Vacío' }}
                                            </div>
                                            <v-icon size="16" color="grey">mdi-arrow-right</v-icon>
                                            <div class="bg-green-lighten-5 text-green-darken-2 px-2 py-1 rounded font-weight-medium">
                                                {{ change.despues || 'Vacío' }}
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
            :fullscreen="isDialogMaximized"
            :max-width="isDialogMaximized ? undefined : 800"
            transition="dialog-bottom-transition"
        >
            <v-card class="rounded-xl d-flex flex-column">
                <v-card-title class="px-6 pt-6 pb-4 d-flex align-center justify-space-between text-h6 font-weight-bold text-corporate-blue">
                    <span>Agregar Observación</span>
                    <div class="d-flex align-center gap-2">
                        <v-btn 
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

const props = defineProps({
    equipo: Object,
    isEditing: Boolean
})

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

function formatFieldName(field) {
    // Map technical names to user friendly names
    const map = {
        'UsuarioId': 'Usuario Asignado',
        'EstadoEquipoId': 'Estado',
        'SedeId': 'Sede',
        'EmpresaId': 'Empresa',
        // Add more mappings as needed
    }
    return map[field] || field
}

onMounted(() => {
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
