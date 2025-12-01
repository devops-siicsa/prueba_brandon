<template>
    <v-row class="position-relative">
        <v-col cols="12" md="8">
            <div class="d-flex align-center gap-3 mb-8">
                <div class="rounded-circle bg-blue-lighten-5 d-flex align-center justify-center text-primary font-weight-bold" style="width: 32px; height: 32px; font-size: 14px;">1</div>
                <h3 class="text-h6 font-weight-bold text-grey-darken-3">Datos del Equipo</h3>
            </div>

            <v-row dense class="mb-6">
                <v-col cols="12" md="6">
                    <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Código de Inventario</label>
                    <v-text-field
                    :model-value="equipo.CodigoEquipo"
                    :label="modern ? undefined : 'Código de Inventario'"
                    :variant="modern ? 'solo' : 'outlined'"
                    :flat="modern"
                    :readonly="!isEditing"
                    hide-details="auto"
                    :class="['rounded-xl', modern ? 'modern-input' : '']"
                    :error-messages="codeError"
                    
                    :append-inner-icon="isMobileApp ? 'mdi-qrcode-scan' : undefined"
                    @click:append-inner="openCamera('CodigoEquipo')"
                    
                    @update:model-value="handleCodeUpdate"
                ></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Estado del Equipo</label>
                    <v-select
                        :model-value="equipo.EstadoEquipoId"
                        :label="modern ? undefined : 'Estado del Equipo'"
                        :items="estados"
                        item-title="Nombre"
                        item-value="Id"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-select' : '']"
                        @update:model-value="$emit('update', 'EstadoEquipoId', $event)"
                    ></v-select>
                </v-col>
                
                <v-col cols="12" md="6" class="mt-4">
                    <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Tipo de Equipo</label>
                    <v-select
                        :model-value="equipo.TipoEquipoId"
                        :label="modern ? undefined : 'Tipo de Equipo'"
                        :items="tipos"
                        item-title="Nombre"
                        item-value="Id"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-select' : '']"
                        @update:model-value="$emit('update', 'TipoEquipoId', $event)"
                    ></v-select>
                </v-col>
                <v-col cols="12" md="6" class="mt-4">
                    <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Fabricante</label>
                    <v-select
                        :model-value="equipo.FabricanteId"
                        :label="modern ? undefined : 'Fabricante'"
                        :items="fabricantes"
                        item-title="Nombre"
                        item-value="Id"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-select' : '']"
                        @update:model-value="$emit('update', 'FabricanteId', $event)"
                    ></v-select>
                </v-col>

                <v-col cols="12" md="6" class="mt-4">
                    <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Modelo</label>
                    <v-text-field
                        :model-value="equipo.Modelo"
                        :label="modern ? undefined : 'Modelo'"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-input' : '']"
                        @update:model-value="$emit('update', 'Modelo', $event)"
                    ></v-text-field>
                </v-col>
                <v-col cols="12" md="6" class="mt-4">
                    <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Serial</label>
                    <v-text-field
                        :model-value="equipo.Serial"
                        :label="modern ? undefined : 'Serial'"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-input' : '']"
                        append-inner-icon="mdi-camera"
                        @update:model-value="$emit('update', 'Serial', $event)"
                    ></v-text-field>
                </v-col>
            </v-row>

            <div class="d-flex align-center gap-3 mb-8 mt-8">
                <div class="rounded-circle bg-blue-lighten-5 d-flex align-center justify-center text-primary font-weight-bold" style="width: 32px; height: 32px; font-size: 14px;">2</div>
                <h3 class="text-h6 font-weight-bold text-grey-darken-3">Propiedad y Adquisición</h3>
            </div>

            <v-row dense>
                <v-col cols="12" md="4">
                    <v-switch
                        :model-value="equipo.EsPropio"
                        label="Equipo Propio"
                        color="primary"
                        :readonly="!isEditing"
                        hide-details
                        inset
                        @update:model-value="$emit('update', 'EsPropio', $event)"
                    ></v-switch>
                </v-col>
                
                <template v-if="!equipo.EsPropio">
                    <v-col cols="12" md="4">
                        <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Proveedor Alquiler</label>
                        <v-text-field
                            :model-value="equipo.ProveedorAlquiler"
                            :label="modern ? undefined : 'Proveedor Alquiler'"
                            :variant="modern ? 'solo' : 'outlined'"
                            :flat="modern"
                            :readonly="!isEditing"
                            hide-details="auto"
                            :class="['rounded-xl', modern ? 'modern-input' : '']"
                            @update:model-value="$emit('update', 'ProveedorAlquiler', $event)"
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" md="4">
                        <label v-if="modern" class="d-block text-caption font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider">Código Alquiler</label>
                        <v-text-field
                            :model-value="equipo.CodigoAlquiler"
                            :label="modern ? undefined : 'Código Alquiler'"
                            :variant="modern ? 'solo' : 'outlined'"
                            :flat="modern"
                            :readonly="!isEditing"
                            hide-details="auto"
                            :class="['rounded-xl', modern ? 'modern-input' : '']"
                            @update:model-value="$emit('update', 'CodigoAlquiler', $event)"
                        ></v-text-field>
                    </v-col>
                </template>
            </v-row>
        </v-col>

        <v-col cols="12" md="4">
             <div class="border-dashed rounded-xl h-100 d-flex flex-column justify-center align-center bg-grey-lighten-5 pa-6">
                <v-icon size="64" color="grey-lighten-2" class="mb-4">mdi-image-outline</v-icon>
                <div class="text-body-2 text-grey">Foto del Equipo</div>
                <v-btn v-if="isEditing" variant="text" color="primary" size="small" class="mt-2">Subir Foto</v-btn>
             </div>
        </v-col>
    </v-row>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean,
    modern: Boolean
})

const emit = defineEmits(['update'])
const { isMobileApp, platform } = useMobileDetection()

const estados = ref([])
const tipos = ref([])
const fabricantes = ref([])
const codeError = ref('')
let debounceTimer = null

function openCamera() {
    // Placeholder for camera logic
    alert('Abrir cámara para escanear código (Funcionalidad en desarrollo)')
    console.log('Opening camera...')
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
                const exists = res.data.some(e => e.Id !== props.equipo.Id)
                if (exists) {
                    codeError.value = 'El código ya existe en la base de datos.'
                }
            }
        } catch (e) {
            console.error('Error validating code:', e)
        }
    }, 500)
}

async function loadCatalogs() {
    try {
        const [resEstados, resTipos, resFabs] = await Promise.all([
            axios.get('/api/config/catalogs/estados_equipo', { withCredentials: true }),
            axios.get('/api/config/catalogs/tipos_equipo', { withCredentials: true }),
            axios.get('/api/config/catalogs/fabricantes', { withCredentials: true })
        ])
        estados.value = resEstados.data
        tipos.value = resTipos.data
        fabricantes.value = resFabs.data
    } catch (e) {
        console.error(e)
    }
}

onMounted(() => {
    loadCatalogs()
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
    background-color: #f9fafb !important; /* bg-gray-50 */
    transition: all 0.2s ease-in-out;
    border: 1px solid transparent;
    box-shadow: none;
    color: #111827 !important; /* text-gray-900 (Sharp Black) */
}

:deep(.modern-input input),
:deep(.modern-select .v-select__selection-text) {
    color: #111827 !important; /* Ensure text is sharp black */
    font-weight: 500; /* Slightly bolder text */
}

:deep(.modern-input .v-field:hover),
:deep(.modern-select .v-field:hover) {
    background-color: #ffffff !important;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}

:deep(.modern-input .v-field--focused),
:deep(.modern-select .v-field--focused) {
    background-color: #ffffff !important;
    border-color: #bfdbfe !important; /* blue-200 */
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important; /* ring-4 ring-blue-500/10 */
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
</style>
