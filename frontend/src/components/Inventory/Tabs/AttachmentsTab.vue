<template>
    <div class="h-100 d-flex flex-column">
        <!-- Toolbar -->
        <div class="flex-shrink-0 pb-4" v-if="isEditing || files.length > 0">
            <div class="d-flex align-center gap-3">
                <h3 class="text-h6 font-weight-bold text-grey-darken-3 mr-auto">
                    Galería de Adjuntos
                </h3>
                
                <template v-if="isEditing">
                    <!-- Hidden Inputs -->
                    <input
                        ref="fileInput"
                        type="file"
                        multiple
                        class="d-none"
                        @change="handleFileSelect"
                    >
                    <input
                        ref="cameraInput"
                        type="file"
                        accept="image/*"
                        capture="environment"
                        class="d-none"
                        @change="handleCameraCapture"
                    >

                    <!-- Action Buttons -->
                    <v-btn
                        v-if="isMobileApp"
                        color="white"
                        :prepend-icon="!isMobileApp ? 'mdi-camera' : undefined"
                        class="rounded-xl border-thin"
                        elevation="0"
                        height="44"
                        min-width="44"
                        :class="isMobileApp ? 'px-0' : 'text-capitalize'"
                        @click="triggerCamera"
                    >
                        <v-icon v-if="isMobileApp">mdi-camera</v-icon>
                        <span v-else>Tomar Foto</span>
                    </v-btn>

                    <v-btn
                        color="corporate-blue"
                        :prepend-icon="!isMobileApp ? 'mdi-paperclip' : undefined"
                        class="rounded-xl font-weight-bold ml-auto text-white"
                        elevation="0"
                        height="44"
                        :min-width="isMobileApp ? '44' : undefined"
                        :class="isMobileApp ? 'px-0' : 'text-capitalize px-6'"
                        @click="triggerFileInput"
                    >
                        <v-icon v-if="isMobileApp">mdi-paperclip</v-icon>
                        <span v-else>Agregar Archivos</span>
                    </v-btn>
                </template>
            </div>
        </div>

        <!-- Main Content -->
        <div 
            class="flex-grow-1 overflow-y-auto custom-scrollbar position-relative"
            :class="isMobileApp ? 'pr-0' : 'pr-2'"
            @dragover.prevent="isEditing ? isDragging = true : null"
            @dragleave.prevent="isDragging = false"
            @drop.prevent="handleDrop"
        >
            <!-- Drag Overlay -->
            <v-fade-transition>
                <div 
                    v-if="isDragging && isEditing"
                    class="position-absolute fill-height w-100 d-flex align-center justify-center bg-blue-lighten-5"
                    style="z-index: 10; opacity: 0.9; border: 3px dashed #3b82f6; border-radius: 24px;"
                >
                    <div class="text-center">
                        <v-icon size="64" color="primary" class="mb-4">mdi-cloud-upload</v-icon>
                        <h3 class="text-h5 font-weight-bold text-primary">Suelta los archivos aquí</h3>
                    </div>
                </div>
            </v-fade-transition>
            
            <!-- Empty State (Desktop) - Editing -->
            <div v-if="files.length === 0 && !isMobileApp && isEditing" class="d-flex flex-column align-center justify-center h-75 text-grey border-dashed rounded-xl ma-2 transition-all" :class="{'bg-grey-lighten-5': isDragging}">
                <div class="bg-white elevation-1 rounded-circle pa-6 mb-4">
                    <v-icon size="48" color="primary">mdi-cloud-upload-outline</v-icon>
                </div>
                <div class="text-h6 text-grey-darken-1 font-weight-bold">Arrastra y suelta archivos aquí</div>
                <div class="text-body-2 text-grey mb-6">o selecciona documentos y fotos</div>
                <v-btn
                    color="primary"
                    variant="flat"
                    class="text-capitalize rounded-lg px-6"
                    :height="isMobileApp ? '56' : '44'"
                    @click="triggerFileInput"
                >
                    Seleccionar Archivos
                </v-btn>
            </div>

            <!-- Empty State (Desktop/Mobile) - View Only -->
            <div v-else-if="files.length === 0 && !isEditing" class="d-flex flex-column align-center justify-center h-75 text-grey ma-2">
                 <v-empty-state
                    icon="mdi-file-document-outline"
                    title="No hay adjuntos"
                    text="Este equipo no tiene archivos adjuntos cargados."
                    class="text-grey-darken-1"
                 ></v-empty-state>
            </div>

            <!-- Mobile Empty State (Simpler) - Editing -->
            <div v-else-if="files.length === 0 && isMobileApp && isEditing" class="d-flex flex-column align-center justify-center h-50 text-grey ma-4">
                <v-icon size="64" color="grey-lighten-2">mdi-image-multiple-outline</v-icon>
                <div class="text-subtitle-1 text-grey-darken-1 font-weight-bold mt-4">Sin Adjuntos</div>
                <div class="d-flex gap-3 mt-4">
                    <v-btn color="white" border class="rounded-lg text-capitalize" @click="triggerCamera">
                        <v-icon start>mdi-camera</v-icon> Cámara
                    </v-btn>
                    <v-btn color="primary" class="rounded-lg text-capitalize" @click="triggerFileInput">
                        <v-icon start>mdi-paperclip</v-icon> Archivos
                    </v-btn>
                </div>
            </div>

            <!-- Gallery Grid -->
            <v-row v-else dense>
                <v-col
                    v-for="(file, index) in files"
                    :key="index"
                    cols="6"
                    sm="4"
                    md="3"
                    lg="2"
                >
                    <v-hover v-slot="{ isHovering, props: hoverProps }">
                        <v-card
                            v-bind="hoverProps"
                            class="rounded-xl transition-all h-100 position-relative border-thin"
                            :class="isHovering ? 'elevation-4 transform-up' : 'elevation-0'"
                            color="white"
                            @click="downloadFile(file)"
                            style="cursor: pointer;"
                        >
                            <!-- Delete Button (Overlay) -->
                            <v-scale-transition>
                                <v-btn
                                    v-if="isHovering && isEditing"
                                    icon="mdi-close"
                                    size="x-small"
                                    color="error"
                                    variant="flat"
                                    class="delete-btn"
                                    @click.prevent="removeFile(index)"
                                ></v-btn>
                            </v-scale-transition>

                            <!-- Content -->
                            <div class="aspect-ratio-square d-flex flex-column">
                                <!-- Image Preview -->
                                <v-img
                                    v-if="isImage(file)"
                                    :src="file.preview"
                                    cover
                                    class="flex-grow-1 bg-grey-lighten-4 rounded-t-xl"
                                    height="120"
                                >
                                    <template v-slot:placeholder>
                                        <div class="d-flex align-center justify-center fill-height">
                                            <v-progress-circular indeterminate color="grey-lighten-3"></v-progress-circular>
                                        </div>
                                    </template>
                                </v-img>

                                <!-- File Icon -->
                                <div v-else class="flex-grow-1 d-flex align-center justify-center bg-grey-lighten-5 rounded-t-xl" style="height: 120px;">
                                    <v-icon size="48" :color="getFileIconColor(file)">{{ getFileIcon(file) }}</v-icon>
                                </div>

                                <!-- Footer Info -->
                                <div class="bg-white rounded-b-xl border-t-thin" :class="isMobileApp ? 'pa-2' : 'pa-3'">
                                    <div class="text-caption font-weight-bold text-truncate text-grey-darken-3" :title="file.name">
                                        {{ file.name }}
                                    </div>
                                    <div class="d-flex align-center justify-space-between mt-1">
                                        <span class="text-caption text-grey text-uppercase" style="font-size: 10px;">
                                            {{ getFileExtension(file.name) }}
                                        </span>
                                        <span class="text-caption text-grey" style="font-size: 10px;">
                                            {{ formatFileSize(file.size) }}
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </v-card>
                    </v-hover>
                </v-col>

                <!-- Add New Card -->
                <v-col cols="6" sm="4" md="3" lg="2" v-if="isEditing">
                    <v-card
                        class="rounded-xl border-dashed d-flex flex-column align-center justify-center h-100 cursor-pointer bg-grey-lighten-5 transition-all"
                        elevation="0"
                        style="min-height: 160px; border: 2px dashed #e0e0e0;"
                        @click="triggerFileInput"
                        v-ripple
                    >
                        <v-icon size="40" color="grey-darken-1" class="mb-2">mdi-plus</v-icon>
                        <span class="text-caption font-weight-bold text-grey-darken-1">Agregar más</span>
                    </v-card>
                </v-col>
            </v-row>
        </div>
    </div>
</template>

<script setup>
import { ref, onUnmounted, watch } from 'vue'
import { useMobileDetection } from '@/composables/useMobileDetection'
import axios from 'axios'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean,
    modern: Boolean
})

const emit = defineEmits(['update'])
const { isMobileApp } = useMobileDetection()

const fileInput = ref(null)
const cameraInput = ref(null)
const files = ref([])
const isDragging = ref(false)

// Initialize files from props
watch(() => props.equipo, (newVal) => {
    if (newVal && newVal.Adjuntos) {
        files.value = newVal.Adjuntos.map(adj => ({
            ...adj,
            preview: adj.type && adj.type.startsWith('image/') ? adj.url : null  // Use Azure URL directly
        }))
    }
}, { immediate: true, deep: true })

// Download file with correct name (handles cross-origin Azure URLs)
const downloadFile = async (file) => {
    try {
        const response = await fetch(file.url || file.path)
        const blob = await response.blob()
        const url = window.URL.createObjectURL(blob)
        const link = document.createElement('a')
        link.href = url
        link.download = file.name
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
        window.URL.revokeObjectURL(url)
    } catch (error) {
        console.error('Error downloading file:', error)
        // Fallback: open in new tab
        window.open(file.url || file.path, '_blank')
    }
}

function triggerFileInput() {
    fileInput.value.click()
}

function triggerCamera() {
    cameraInput.value.click()
}

function handleFileSelect(event) {
    const selectedFiles = Array.from(event.target.files)
    processFiles(selectedFiles)
    // Reset input to allow selecting same file again
    event.target.value = ''
}

function handleCameraCapture(event) {
    const selectedFiles = Array.from(event.target.files)
    processFiles(selectedFiles)
    event.target.value = ''
}

function handleDrop(event) {
    isDragging.value = false
    const droppedFiles = Array.from(event.dataTransfer.files)
    processFiles(droppedFiles)
}

async function processFiles(newFiles) {
    if (!props.isEditing) {
        alert("Debes estar en modo edición para agregar archivos.")
        return
    }

    for (const file of newFiles) {
        // Create form data
        const formData = new FormData()
        formData.append('file', file)

        try {
            const res = await axios.post(`/api/inventory/equipos/${props.equipo.Id}/attachments`, formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
                withCredentials: true
            })
            
            // Add returned file to list
            const uploadedFile = res.data.file
            if (uploadedFile.type && uploadedFile.type.startsWith('image/')) {
                uploadedFile.preview = uploadedFile.url  // Use Azure URL directly
            }
            files.value.push(uploadedFile)
            emit('update') // Refresh parent data
        } catch (error) {
            console.error("Error uploading file:", error)
            alert("Error al subir archivo: " + (error.response?.data?.message || error.message))
        }
    }
}

async function removeFile(index) {
    if (!props.isEditing) return

    const file = files.value[index]
    if (!confirm(`¿Estás seguro de eliminar el archivo ${file.name}?`)) return

    try {
        await axios.delete(`/api/inventory/equipos/${props.equipo.Id}/attachments/${file.Id}`, { withCredentials: true })
        files.value.splice(index, 1)
        emit('update')
    } catch (error) {
         console.error("Error deleting file:", error)
         alert("Error al eliminar archivo")
    }
}

function isImage(file) {
    return file.type && file.type.startsWith('image/')
}

function getFileExtension(filename) {
    return filename.slice((filename.lastIndexOf(".") - 1 >>> 0) + 2).toUpperCase();
}

function getFileIcon(file) {
    const ext = getFileExtension(file.name).toLowerCase()
    switch (ext) {
        case 'pdf': return 'mdi-file-pdf-box'
        case 'doc': 
        case 'docx': return 'mdi-file-word-box'
        case 'xls': 
        case 'xlsx': return 'mdi-file-excel-box'
        case 'txt': return 'mdi-file-document-outline'
        case 'zip': 
        case 'rar': return 'mdi-folder-zip-outline'
        case 'mp4':
        case 'mov':
        case 'avi':
        case 'mkv': return 'mdi-file-video-outline'
        case 'ppt':
        case 'pptx': return 'mdi-file-powerpoint-box'
        case 'mp3':
        case 'wav': return 'mdi-file-music-outline'
        default: return 'mdi-file-outline'
    }
}

function getFileIconColor(file) {
    const ext = getFileExtension(file.name).toLowerCase()
    switch (ext) {
        case 'pdf': return 'red'
        case 'doc': 
        case 'docx': return 'blue'
        case 'xls': 
        case 'xlsx': return 'green'
        case 'zip': 
        case 'rar': return 'orange'
        case 'mp4':
        case 'mov':
        case 'avi':
        case 'mkv': return 'purple'
        case 'ppt':
        case 'pptx': return 'orange-darken-1'
        case 'mp3':
        case 'wav': return 'teal'
        default: return 'grey'
    }
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 B'
    const k = 1024
    const sizes = ['B', 'KB', 'MB', 'GB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i]
}

// Cleanup object URLs to avoid memory leaks
onUnmounted(() => {
    files.value.forEach(file => {
        if (file.preview) {
            URL.revokeObjectURL(file.preview)
        }
    })
})
</script>

<style scoped>
.gap-3 { gap: 12px; }
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }
.border-dashed { border: 2px dashed rgba(0,0,0,0.1) !important; }
.transition-all { transition: all 0.2s ease; }
.transform-up { transform: translateY(-4px); }

.delete-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    z-index: 10;
}

.aspect-ratio-square {
    aspect-ratio: 1;
}

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
    width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
    background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
    background-color: rgba(0,0,0,0.1);
    border-radius: 20px;
}
.custom-scrollbar:hover::-webkit-scrollbar-thumb {
    background-color: rgba(0,0,0,0.2);
}
</style>
