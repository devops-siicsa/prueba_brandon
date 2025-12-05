<template>
    <v-row class="position-relative" :no-gutters="isMobileApp">
        <!-- Vertical Divider (Desktop only) -->
        <div v-if="modern" class="d-none d-md-block position-absolute bg-gradient-vertical" style="left: 50%; top: 0; bottom: 0; width: 1px; transform: translateX(-50%); z-index: 1;"></div>

        <!-- User Info Section -->
        <v-col cols="12" md="6" :class="modern ? 'pr-md-12' : ''">
            <div class="d-flex align-center gap-3 mb-8">
                <div class="rounded-circle bg-blue-lighten-5 d-flex align-center justify-center text-primary font-weight-bold" style="width: 32px; height: 32px; font-size: 14px;">1</div>
                <h3 class="text-h6 font-weight-bold text-grey-darken-3">Datos del Responsable</h3>
            </div>

            <div class="mb-6 group">
                <label v-if="modern" 
                    class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                    :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                >Usuario Asignado <span class="text-error">*</span></label>
                <v-text-field
                    :model-value="equipo.UsuarioNombre"
                    :label="modern ? undefined : 'Usuario Asignado*'"
                    :placeholder="modern ? 'Escribir nombre...' : undefined"
                    :variant="modern ? 'solo' : 'outlined'"
                    :flat="modern"
                    :readonly="!isEditing"
                    hide-details="auto"
                    :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                    prepend-inner-icon="mdi-account"
                    :rules="[v => !!v || ' ']"
                    @update:model-value="$emit('update', 'UsuarioNombre', $event)"
                ></v-text-field>
            </div>

            <v-row dense class="mb-6">
                <v-col cols="12" md="6">
                    <label v-if="modern" 
                        class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                        :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                    >Cargo <span class="text-error">*</span></label>
                    <v-text-field
                        :model-value="equipo.Cargo"
                        :label="modern ? undefined : 'Cargo*'"
                        :placeholder="modern ? 'Ej. Analista' : undefined"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                        prepend-inner-icon="mdi-briefcase"
                        :rules="[v => !!v || ' ']"
                        @update:model-value="$emit('update', 'Cargo', $event)"
                    ></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <label v-if="modern" 
                        class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                        :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                    >Área <span class="text-error">*</span></label>
                    <v-text-field
                        :model-value="equipo.Area"
                        :label="modern ? undefined : 'Área*'"
                        :placeholder="modern ? 'Ej. IT' : undefined"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                        prepend-inner-icon="mdi-layers"
                        :rules="[v => !!v || ' ']"
                        @update:model-value="$emit('update', 'Area', $event)"
                    ></v-text-field>
                </v-col>
            </v-row>

            <div class="mb-6">
                <label v-if="modern" 
                    class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                    :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                >Correo Electrónico <span class="text-error">*</span></label>
                <v-text-field
                    :model-value="equipo.Correo"
                    :label="modern ? undefined : 'Correo Electrónico*'"
                    :placeholder="modern ? 'usuario@empresa.com' : undefined"
                    :variant="modern ? 'solo' : 'outlined'"
                    :flat="modern"
                    :readonly="!isEditing"
                    hide-details="auto"
                    :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                    prepend-inner-icon="mdi-email"
                    :rules="[v => !!v || ' ', v => /.+@.+\..+/.test(v) || 'Inválido']"
                    @update:model-value="$emit('update', 'Correo', $event)"
                ></v-text-field>
            </div>

            <div class="mb-6">
                <label v-if="modern" 
                    class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                    :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                >Teléfono / Extensión <span class="text-error">*</span></label>
                <v-text-field
                    :model-value="equipo.Telefono"
                    :label="modern ? undefined : 'Teléfono / Extensión*'"
                    :placeholder="modern ? '(+57) 300 ...' : undefined"
                    :variant="modern ? 'solo' : 'outlined'"
                    :flat="modern"
                    :readonly="!isEditing"
                    hide-details="auto"
                    :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                    prepend-inner-icon="mdi-phone"
                    :rules="[v => (!!v && /^\d+$/.test(v) && v.length <= 12) || ' ']"
                    maxlength="12"
                    inputmode="numeric"
                    @update:model-value="$emit('update', 'Telefono', $event.replace(/\D/g, '').slice(0, 12))"
                ></v-text-field>
            </div>
        </v-col>

        <!-- Location Section -->
        <v-col cols="12" md="6" :class="modern ? 'pl-md-12' : ''">
            <div class="d-flex align-center gap-3 mb-8">
                <div class="rounded-circle bg-blue-lighten-5 d-flex align-center justify-center text-primary font-weight-bold" style="width: 32px; height: 32px; font-size: 14px;">2</div>
                <h3 class="text-h6 font-weight-bold text-grey-darken-3">Localización Física</h3>
            </div>

            <!-- Card de Ubicación destacada -->
            <div class="bg-gradient-location rounded-3xl pa-8 border border-blue-lighten-4 shadow-inner-custom">
                <div class="mb-8">
                    <label v-if="modern" 
                        class="d-block font-weight-bold text-blue-darken-3 text-uppercase mb-2 ml-1 opacity-60 tracking-wider"
                        :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                    >Sede Principal <span class="text-error">*</span></label>
                    <v-select
                        :model-value="equipo.SedeId"
                        :label="modern ? undefined : 'Sede Principal*'"
                        :placeholder="modern ? 'Seleccione una sede...' : undefined"
                        :items="sedes"
                        item-title="NombreSede"
                        item-value="Id"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        bg-color="white"
                        :readonly="!isEditing"
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-select' : '', isMobileApp ? 'mobile-input' : '']"
                        prepend-inner-icon="mdi-office-building"
                        menu-icon="mdi-chevron-down"
                        :rules="[v => !!v || ' ']"
                        @update:model-value="updateSede"
                    ></v-select>
                </div>

                <div class="mb-6">
                    <label v-if="modern" 
                        class="d-block font-weight-bold text-blue-darken-3 text-uppercase mb-2 ml-1 opacity-60 tracking-wider"
                        :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                    >Ciudad</label>
                    <v-text-field
                        :model-value="equipo.Ciudad"
                        :label="modern ? undefined : 'Ciudad'"
                        :variant="modern ? 'solo' : 'outlined'"
                        :flat="modern"
                        bg-color="white"
                        readonly
                        hide-details="auto"
                        :class="['rounded-xl', modern ? 'modern-input' : '', isMobileApp ? 'mobile-input' : '']"
                        prepend-inner-icon="mdi-map-marker"
                    ></v-text-field>
                </div>

                <div class="d-flex align-start gap-3 pa-4 bg-blue-lighten-4 rounded-xl">
                    <div class="rounded-circle bg-primary mt-1.5" style="width: 6px; height: 6px; min-width: 6px;"></div>
                    <p class="text-caption text-blue-darken-3 mb-0" style="line-height: 1.6;">
                        La ciudad se completará automáticamente al seleccionar la sede. Si necesita agregar una nueva sede, contacte al administrador.
                    </p>
                </div>
            </div>
        </v-col>
    </v-row>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean,
    modern: Boolean
})

const { isMobileApp } = useMobileDetection()

const emit = defineEmits(['update'])
const sedes = ref([])

async function loadSedes() {
    // Strict filtering: Do not load if no Company ID is provided
    if (!props.equipo.EmpresaId) {
        sedes.value = []
        return
    }

    try {
        const params = { EmpresaId: props.equipo.EmpresaId }
        const res = await axios.get('/api/config/sedes', { 
            withCredentials: true,
            params: params
        })
        sedes.value = res.data
    } catch (e) {
        console.error(e)
    }
}

function updateSede(sedeId) {
    emit('update', 'SedeId', sedeId)
    
    const selectedSede = sedes.value.find(s => s.Id === sedeId)
    if (selectedSede) {
        emit('update', 'Ciudad', selectedSede.Ciudad)
    }
}

watch(() => props.equipo.EmpresaId, (newVal) => {
    if (newVal) {
        loadSedes()
    }
})

onMounted(() => {
    // Initial load if ID is already present
    loadSedes()
})
</script>

<style scoped>
.gap-3 { gap: 12px; }
.rounded-xl { border-radius: 12px !important; }
.rounded-3xl { border-radius: 24px !important; }
.opacity-60 { opacity: 0.6; }
.tracking-wider { letter-spacing: 0.05em; }

.bg-gradient-vertical {
    background: linear-gradient(to bottom, transparent, #e2e8f0, transparent);
}

.bg-gradient-location {
    background: linear-gradient(to bottom right, rgba(239, 246, 255, 0.8), #ffffff); /* from-blue-50/80 to-white */
}

.shadow-inner-custom {
    box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.02);
}

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

/* Mobile Input Optimizations */
:deep(.mobile-input .v-field) {
    min-height: 56px !important;
    border-radius: 16px !important; /* Larger radius for mobile */
}

:deep(.mobile-input input),
:deep(.mobile-select .v-select__selection-text) {
    font-size: 1.1rem !important; /* Larger text */
    padding-top: 12px !important;
    padding-bottom: 12px !important;
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

:deep(.modern-select .v-field__append-inner) {
    color: #9ca3af !important;
}

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
