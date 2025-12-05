<template>
    <v-row class="position-relative" :no-gutters="isMobileApp">
        <v-col cols="12" md="12">
            <!-- Section 1: Datos del Equipo -->
            <v-card class="mb-6 rounded-xl border-thin shadow-sm" elevation="0">
                <v-card-text :class="mobile ? 'px-3 py-4' : 'pa-6'">
                    <div class="d-flex align-center gap-3 mb-6">
                        <div class="rounded-circle bg-corporate-blue d-flex align-center justify-center text-white font-weight-bold shadow-md" :style="{ width: mobile ? '28px' : '32px', height: mobile ? '28px' : '32px', fontSize: mobile ? '12px' : '14px' }">1</div>
                        <h3 class="text-h6 font-weight-bold text-grey-darken-3">Datos del Equipo</h3>
                    </div>

                    <v-row dense>
                        <v-col cols="12" md="6">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Código de Inventario <span class="text-error">*</span></label>
                            <v-text-field
                                :model-value="equipo.CodigoEquipo"
                                :label="modern ? undefined : 'Código de Inventario*'"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-barcode"
                                :append-inner-icon="isMobileApp ? 'mdi-qrcode-scan' : undefined"
                                :rules="[v => !!v || ' ']"
                                @click:append-inner="openCamera('CodigoEquipo')"
                                @update:model-value="handleCodeUpdate"
                            ></v-text-field>
                            <v-expand-transition>
                                <div v-if="codeError" class="mt-2">
                                    <v-alert
                                        type="warning"
                                        variant="tonal"
                                        density="compact"
                                        class="rounded-lg border-thin"
                                        icon="mdi-alert-circle-outline"
                                    >
                                        <span class="text-caption font-weight-bold">{{ codeError }}</span>
                                    </v-alert>
                                </div>
                            </v-expand-transition>
                        </v-col>
                        <v-col cols="12" md="6">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Estado del Equipo <span class="text-error">*</span></label>
                            <v-select
                                :model-value="equipo.EstadoEquipoId"
                                :label="modern ? undefined : 'Estado del Equipo*'"
                                :items="estados"
                                item-title="Nombre"
                                item-value="Id"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-select' : '', isMobileApp ? 'mobile-input' : '']"
                                :rules="[v => !!v || ' ']"
                                @update:model-value="$emit('update', 'EstadoEquipoId', $event)"
                            >
                                <template v-slot:prepend-inner>
                                    <v-icon :color="statusIconColor">mdi-heart-pulse</v-icon>
                                </template>
                            </v-select>
                        </v-col>
                        
                        <v-col cols="12" md="6" class="mt-4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Tipo de Equipo <span class="text-error">*</span></label>
                            <v-select
                                :model-value="equipo.TipoEquipoId"
                                :label="modern ? undefined : 'Tipo de Equipo*'"
                                :items="tipos"
                                item-title="Nombre"
                                item-value="Id"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-select' : '', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-devices"
                                :rules="[v => !!v || ' ']"
                                @update:model-value="$emit('update', 'TipoEquipoId', $event)"
                            ></v-select>
                        </v-col>
                        <v-col cols="12" md="6" class="mt-4" v-if="!isClon">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Fabricante <span class="text-error">*</span></label>
                            <v-select
                                :model-value="equipo.FabricanteId"
                                :label="modern ? undefined : 'Fabricante*'"
                                :items="fabricantes"
                                item-title="Nombre"
                                item-value="Id"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-select' : '', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-domain"
                                :rules="[v => !!v || ' ']"
                                @update:model-value="$emit('update', 'FabricanteId', $event)"
                            ></v-select>
                        </v-col>

                        <v-col cols="12" md="6" class="mt-4" v-if="!isClon">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Modelo <span class="text-error">*</span></label>
                            <v-text-field
                                :model-value="equipo.Modelo"
                                :label="modern ? undefined : 'Modelo*'"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-tag-text-outline"
                                :rules="[v => !!v || ' ']"
                                @update:model-value="$emit('update', 'Modelo', $event)"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6" class="mt-4" v-if="!isClon">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Serial <span class="text-error">*</span></label>
                            <v-text-field
                                :model-value="equipo.Serial"
                                :label="modern ? undefined : 'Serial*'"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-fingerprint"
                                :append-inner-icon="photoPreview ? 'mdi-paperclip' : 'mdi-camera'"
                                :append-inner-icon-color="photoPreview ? 'primary' : undefined"
                                :rules="[v => !!v || ' ']"
                                @click:append-inner="handlePhotoClick"
                                @update:model-value="$emit('update', 'Serial', $event)"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>

            <!-- Section 2: Propiedad y Adquisición -->
            <v-card class="rounded-xl border-thin shadow-sm" elevation="0">
                <v-card-text :class="mobile ? 'px-3 py-4' : 'pa-6'">
                    <div class="d-flex align-center gap-3 mb-6">
                        <div class="rounded-circle bg-corporate-blue d-flex align-center justify-center text-white font-weight-bold shadow-md" :style="{ width: mobile ? '28px' : '32px', height: mobile ? '28px' : '32px', fontSize: mobile ? '12px' : '14px' }">2</div>
                        <h3 class="text-h6 font-weight-bold text-grey-darken-3">Propiedad y Adquisición</h3>
                    </div>

                    <v-row dense align="center">
                        <v-col cols="12" md="4">
                            <div class="d-flex align-center pa-4 bg-grey-lighten-5 rounded-xl border-thin">
                                <v-switch
                                    :model-value="equipo.EsPropio"
                                    color="primary"
                                    :readonly="!isEditing"
                                    hide-details
                                    inset
                                    class="ml-2"
                                    @update:model-value="$emit('update', 'EsPropio', $event)"
                                >
                                    <template v-slot:label>
                                        <span class="font-weight-bold text-grey-darken-3 ml-2">
                                            {{ equipo.EsPropio ? 'Equipo Propio' : 'Equipo Alquilado' }}
                                        </span>
                                    </template>
                                </v-switch>
                            </div>
                        </v-col>
                        
                        <template v-if="!equipo.EsPropio">
                            <v-col cols="12" md="4">
                                <label v-if="modern" 
                                    class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                    :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                                >Proveedor Alquiler <span class="text-error">*</span></label>
                                <v-text-field
                                    :model-value="equipo.ProveedorAlquiler"
                                    :label="modern ? undefined : 'Proveedor Alquiler*'"
                                    :variant="modern ? 'solo' : 'outlined'"
                                    :flat="modern"
                                    :readonly="!isEditing"
                                    hide-details="auto"
                                    :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                                    prepend-inner-icon="mdi-store"
                                    :rules="[v => !!v || ' ']"
                                    @update:model-value="$emit('update', 'ProveedorAlquiler', $event)"
                                ></v-text-field>
                            </v-col>
                            <v-col cols="12" md="4">
                                <label v-if="modern" 
                                    class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                    :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                                >Código Alquiler <span class="text-error">*</span></label>
                                <v-text-field
                                    :model-value="equipo.CodigoAlquiler"
                                    :label="modern ? undefined : 'Código Alquiler*'"
                                    :variant="modern ? 'solo' : 'outlined'"
                                    :flat="modern"
                                    :readonly="!isEditing"
                                    hide-details="auto"
                                    :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                                    prepend-inner-icon="mdi-file-document-outline"
                                    :rules="[v => !!v || ' ']"
                                    @update:model-value="$emit('update', 'CodigoAlquiler', $event)"
                                ></v-text-field>
                            </v-col>
                        </template>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>
        
        <QRScanner v-model="showScanner" @scan="handleScan" />

        <!-- Photo Options Sheet -->
        <v-bottom-sheet v-model="showPhotoOptions">
            <v-card class="rounded-t-xl">
                <v-card-title class="text-center font-weight-bold text-grey-darken-3 pt-4">
                    Foto del Equipo
                </v-card-title>
                <v-list class="pt-0">
                    <v-list-item @click="triggerFileInput(true)" prepend-icon="mdi-camera" title="Tomar Foto"></v-list-item>
                    <v-list-item @click="triggerFileInput(false)" prepend-icon="mdi-image" title="Seleccionar de Galería"></v-list-item>
                    <v-list-item v-if="photoPreview" @click="showPreviewDialog = true" prepend-icon="mdi-eye" title="Ver Foto Actual"></v-list-item>
                </v-list>
            </v-card>
        </v-bottom-sheet>

        <!-- Hidden File Input -->
        <input 
            type="file" 
            ref="fileInput" 
            accept="image/*" 
            style="display: none" 
            @change="handleFileChange"
        />

        <!-- Photo Preview Dialog (Lightbox Style) -->
        <v-dialog v-model="showPreviewDialog" width="auto" max-width="90vw" max-height="90vh" scrim="black">
            <div class="position-relative d-flex justify-center align-center">
                <!-- Close Button -->
                <v-btn 
                    icon="mdi-close" 
                    variant="flat" 
                    color="rgba(0,0,0,0.6)" 
                    class="text-white position-absolute top-0 right-0 mt-n2 mr-n2"
                    style="z-index: 10;"
                    size="small"
                    @click="showPreviewDialog = false"
                ></v-btn>

                <!-- Image -->
                <img 
                    :src="photoPreview" 
                    style="max-width: 100%; max-height: 80vh; border-radius: 16px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);" 
                />

                <!-- Delete Action -->
                <v-btn
                    color="error"
                    variant="flat"
                    prepend-icon="mdi-delete-outline"
                    class="position-absolute text-capitalize"
                    style="bottom: 20px; z-index: 10; background-color: rgba(239, 68, 68, 0.9);"
                    rounded="pill"
                    @click="removePhoto"
                >
                    Eliminar
                </v-btn>
            </div>
        </v-dialog>
    </v-row>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useDisplay } from 'vuetify'
import axios from 'axios'
import { storeToRefs } from 'pinia'
import { useMobileDetection } from '@/composables/useMobileDetection'
import { useCatalogsStore } from '@/stores/catalogs'
import QRScanner from '@/components/Common/QRScanner.vue'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean,
    modern: Boolean
})

const emit = defineEmits(['update'])
const { mobile } = useDisplay()
const { isMobileApp, platform } = useMobileDetection()
const catalogsStore = useCatalogsStore()
const { estadosEquipo: estados, tiposEquipo: tipos, fabricantes } = storeToRefs(catalogsStore)

const codeError = ref('')
const showScanner = ref(false)
const showPhotoOptions = ref(false)
const fileInput = ref(null)
const photoPreview = ref(null)
const showPreviewDialog = ref(false)
let debounceTimer = null

function openCamera() {
    showScanner.value = true
}

function handleScan(code) {
    handleCodeUpdate(code)
}

function handlePhotoClick() {
    if (photoPreview.value) {
        showPreviewDialog.value = true
    } else {
        showPhotoOptions.value = true
    }
}

function removePhoto() {
    photoPreview.value = null
    if (fileInput.value) {
        fileInput.value.value = ''
    }
    emit('update', 'Foto', null)
    showPreviewDialog.value = false
}

function triggerFileInput(capture = false) {
    if (fileInput.value) {
        if (capture) {
            fileInput.value.setAttribute('capture', 'environment')
        } else {
            fileInput.value.removeAttribute('capture')
        }
        fileInput.value.click()
    }
    showPhotoOptions.value = false
}

function handleFileChange(event) {
    const file = event.target.files[0]
    if (file) {
        // Create preview
        const reader = new FileReader()
        reader.onload = (e) => {
            photoPreview.value = e.target.result
            // Here you would typically emit the file to the parent or upload it
            // emit('update', 'Foto', file) 
            // For now we just keep the preview local or maybe emit it if the parent expects it
            emit('update', 'Foto', file)
        }
        reader.readAsDataURL(file)
    }
}

function handleCodeUpdate(value) {
    emit('update', 'CodigoEquipo', value)
    
    // Clear previous error and timer
    codeError.value = ''
    if (debounceTimer) clearTimeout(debounceTimer)
    
    if (!value) return

    // Debounce API call
    debounceTimer = setTimeout(async () => {
        try {
            const res = await axios.get(`/api/inventory/equipos?CodigoEquipo=${value}`, { withCredentials: true })
            if (res.data && res.data.length > 0) {
                // Check if it's not the current equipment (in case of edit)
                const duplicate = res.data.find(e => e.Id !== props.equipo.Id)
                if (duplicate) {
                    const empresa = duplicate.EmpresaNombre || 'otra empresa'
                    codeError.value = `Este código ya está asignado a la empresa "${empresa}"`
                }
            }
        } catch (e) {
            console.error('Error validating code:', e)
        }
    }, 500)
}

const statusIconColor = computed(() => {
    if (!props.equipo.EstadoEquipoId || !estados.value) return 'grey'
    
    const estado = estados.value.find(e => e.Id === props.equipo.EstadoEquipoId)
    if (!estado) return 'grey'
    
    const nombre = estado.Nombre.toLowerCase()
    if (nombre.includes('activo')) return 'success'
    if (nombre.includes('inactivo')) return 'warning'
    if (nombre.includes('baja') || nombre.includes('dañado') || nombre.includes('robado')) return 'error'
    
    return 'grey'
})

const isClon = computed(() => {
    if (!props.equipo.TipoEquipoId || !tipos.value) return false
    const tipo = tipos.value.find(t => t.Id === props.equipo.TipoEquipoId)
    return tipo && tipo.Nombre.toLowerCase().includes('clon')
})

onMounted(() => {
    catalogsStore.fetchCatalogs(['estadosEquipo', 'tiposEquipo', 'fabricantes'])
    
    // If there is an existing photo URL in props.equipo.Foto, set it to preview
    if (props.equipo.Foto) {
        // Assuming Foto is a URL or base64
        photoPreview.value = props.equipo.Foto
    }
})
</script>

<style scoped>
.gap-3 { gap: 12px; }
.rounded-xl { border-radius: 12px !important; }
.border-dashed { border-style: dashed !important; }
.tracking-wider { letter-spacing: 0.05em; }

/* Modern Input Styles - Pixel Perfect Match */
:deep(.modern-input .v-field),
:deep(.modern-select .v-field) {
    border-radius: 12px !important;
    background-color: #f3f4f6 !important; /* bg-gray-100 */
    transition: all 0.2s ease-in-out;
    border: 1px solid #e5e7eb !important; /* border-gray-200 */
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    color: #111827 !important; /* text-gray-900 */
}

:deep(.modern-input input),
:deep(.modern-select .v-select__selection-text) {
    color: #111827 !important;
    font-weight: 500;
}

:deep(.modern-input .v-field:hover),
:deep(.modern-select .v-field:hover) {
    background-color: #ffffff !important;
    border-color: #d1d5db !important; /* border-gray-300 */
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.05);
}

:deep(.modern-input .v-field--focused),
:deep(.modern-select .v-field--focused) {
    background-color: #ffffff !important;
    border-color: #3b82f6 !important; /* blue-500 */
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15) !important;
}

/* Mobile Input Optimizations */
:deep(.mobile-input .v-field) {
    min-height: 56px !important;
    border-radius: 16px !important;
}

:deep(.mobile-input input),
:deep(.mobile-select .v-select__selection-text) {
    font-size: 1.1rem !important;
    padding-top: 12px !important;
    padding-bottom: 12px !important;
}

/* Icon Styling */
:deep(.modern-input .v-field__prepend-inner > .v-icon),
:deep(.modern-select .v-field__prepend-inner > .v-icon) {
    color: #9ca3af !important; /* text-gray-400 */
    opacity: 1;
    transition: color 0.2s;
}

:deep(.modern-input .v-field--focused .v-field__prepend-inner > .v-icon),
:deep(.modern-select .v-field--focused .v-field__prepend-inner > .v-icon) {
    color: #2563eb !important; /* text-blue-600 */
}

/* Utilities */
.bg-corporate-blue { background-color: #223551 !important; }
.shadow-sm { box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important; }
.shadow-md { box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important; }

/* Error State Styling - Red Shadow instead of Text */
:deep(.v-field--error) {
    box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.25) !important; /* red-500 with opacity */
    border-color: #ef4444 !important;
}
:deep(.v-field--error .v-field__outline) {
    color: #ef4444 !important;
}
:deep(.v-input--error .v-input__details) {
    display: none !important;
}
</style>
