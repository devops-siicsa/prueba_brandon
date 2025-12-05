<template>
    <v-row class="position-relative" :no-gutters="isMobileApp">
        <!-- Section 1: Sistema Operativo -->
        <v-col cols="12" md="6">
            <v-card class="mb-4 rounded-xl border-thin shadow-sm" elevation="0">
                <v-card-text :class="isMobileApp ? 'px-3 py-4' : 'pa-6'">
                    <div class="d-flex align-center gap-3 mb-6">
                        <div class="rounded-circle bg-corporate-blue d-flex align-center justify-center text-white font-weight-bold shadow-md" style="width: 32px; height: 32px; font-size: 14px;">1</div>
                        <h3 class="text-h6 font-weight-bold text-grey-darken-3">Sistema Operativo</h3>
                    </div>

                    <v-row dense>
                        <v-col cols="12">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Sistema Operativo*</label>
                            <v-autocomplete
                                :model-value="equipo.SistemaOperativoId"
                                :label="modern ? undefined : 'Sistema Operativo*'"
                                :items="sistemasOperativos"
                                item-title="Nombre"
                                item-value="Id"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-select' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-microsoft-windows"
                                @update:model-value="$emit('update', 'SistemaOperativoId', $event)"
                                auto-select-first
                                :rules="[v => !!v || ' ']"
                            ></v-autocomplete>
                        </v-col>
                        
                        <!-- Campo para Licencia (Windows/Otros) -->
                        <v-col cols="12" v-if="!isLinuxOrMac" class="mt-4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Licencia / Serial SO*</label>
                            <v-text-field
                                :model-value="equipo.LicenciaSO"
                                :label="modern ? undefined : 'Licencia / Serial SO*'"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-key-variant"
                                @update:model-value="$emit('update', 'LicenciaSO', $event)"
                                :rules="[v => !!v || ' ']"
                            ></v-text-field>
                        </v-col>

                        <!-- Campo para Distribución (Linux/Mac) -->
                        <v-col cols="12" v-if="isLinuxOrMac" class="mt-4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Distribución*</label>
                            <v-text-field
                                :model-value="equipo.Distribucion"
                                :label="modern ? undefined : 'Distribución*'"
                                placeholder="Ej: Ubuntu 22.04, macOS Ventura"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-linux"
                                @update:model-value="$emit('update', 'Distribucion', $event)"
                                :rules="[v => !!v || ' ']"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>

        <!-- Section 2: Ofimática -->
        <v-col cols="12" md="6">
            <v-card class="mb-4 rounded-xl border-thin shadow-sm" elevation="0">
                <v-card-text :class="isMobileApp ? 'px-3 py-4' : 'pa-6'">
                    <div class="d-flex align-center gap-3 mb-6">
                        <div class="rounded-circle bg-corporate-blue d-flex align-center justify-center text-white font-weight-bold shadow-md" style="width: 32px; height: 32px; font-size: 14px;">2</div>
                        <h3 class="text-h6 font-weight-bold text-grey-darken-3">Ofimática</h3>
                    </div>

                    <v-row dense>
                        <v-col cols="12">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Suite Ofimática*</label>
                            <v-autocomplete
                                :model-value="equipo.OfimaticaId"
                                :label="modern ? undefined : 'Suite Ofimática*'"
                                :items="ofimaticas"
                                item-title="Nombre"
                                item-value="Id"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-select' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-file-document-multiple"
                                @update:model-value="$emit('update', 'OfimaticaId', $event)"
                                auto-select-first
                                :rules="[v => !!v || ' ']"
                            ></v-autocomplete>
                        </v-col>
                        
                        <!-- Campo para Licencia (Office Comercial) -->
                        <v-col cols="12" v-if="!isOfficeFree" class="mt-4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Licencia / Cuenta*</label>
                            <v-text-field
                                :model-value="equipo.LicenciaOfimatica"
                                :label="modern ? undefined : 'Licencia / Cuenta*'"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-account-key"
                                @update:model-value="$emit('update', 'LicenciaOfimatica', $event)"
                                :rules="[v => !!v || ' ']"
                            ></v-text-field>
                        </v-col>

                        <!-- Campo para Distribución (Office Libre) -->
                        <v-col cols="12" v-if="isOfficeFree" class="mt-4">
                             <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                             >Distribución*</label>
                             <v-text-field
                                :model-value="equipo.DistribucionOfimatica"
                                :label="modern ? undefined : 'Distribución*'"
                                placeholder="Ej: LibreOffice 7.5"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-package-variant"
                                @update:model-value="$emit('update', 'DistribucionOfimatica', $event)"
                                :rules="[v => !!v || ' ']"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>

        <!-- Section 3: Red y Seguridad -->
        <v-col cols="12">
            <v-card class="mb-4 rounded-xl border-thin shadow-sm" elevation="0">
                <v-card-text :class="isMobileApp ? 'px-3 py-4' : 'pa-6'">
                    <div class="d-flex align-center gap-3 mb-6">
                        <div class="rounded-circle bg-corporate-blue d-flex align-center justify-center text-white font-weight-bold shadow-md" style="width: 32px; height: 32px; font-size: 14px;">3</div>
                        <h3 class="text-h6 font-weight-bold text-grey-darken-3">Red y Seguridad</h3>
                    </div>

                    <v-row dense>
                        <!-- 1. Pertenece a -->
                        <v-col cols="12" md="4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Pertenece a*</label>
                            <v-autocomplete
                                :model-value="equipo.EquipoPertenece"
                                :label="modern ? undefined : 'Pertenece a*'"
                                :items="['Dominio', 'Grupo de Trabajo']"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-select' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-domain"
                                @update:model-value="$emit('update', 'EquipoPertenece', $event)"
                                auto-select-first
                                :rules="[v => !!v || ' ']"
                            ></v-autocomplete>
                        </v-col>

                        <!-- 2. Nombre Grupo / Dominio (Nuevo) -->
                        <v-col cols="12" md="4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Nombre Grupo / Dominio*</label>
                            <v-text-field
                                :model-value="equipo.NombreGrupoDominio"
                                :label="modern ? undefined : 'Nombre Grupo / Dominio*'"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-server-network"
                                @update:model-value="$emit('update', 'NombreGrupoDominio', $event)"
                                :rules="[v => !!v || ' ']"
                            ></v-text-field>
                        </v-col>

                        <!-- 3. Nombre en Red (Hostname) -->
                        <v-col cols="12" md="4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Nombre equipo (hostname)*</label>
                            <v-text-field
                                :model-value="equipo.NombreEnRed"
                                :label="modern ? undefined : 'Nombre equipo (hostname)*'"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-input' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-desktop-tower"
                                @update:model-value="$emit('update', 'NombreEnRed', $event)"
                                :rules="[v => !!v || ' ']"
                            ></v-text-field>
                        </v-col>

                        <!-- 4. Antivirus -->
                        <v-col cols="12" md="4" class="mt-4">
                            <label v-if="modern" 
                                class="d-block font-weight-bold text-grey-darken-3 text-uppercase mb-2 ml-1 tracking-wider"
                                :class="isMobileApp ? 'text-body-2' : 'text-caption'"
                            >Antivirus*</label>
                            <v-autocomplete
                                :model-value="equipo.AntivirusId"
                                :label="modern ? undefined : 'Antivirus*'"
                                :items="antivirus"
                                item-title="Nombre"
                                item-value="Id"
                                :variant="modern ? 'solo' : 'outlined'"
                                :flat="modern"
                                :readonly="!isEditing"
                                hide-details="auto"
                                :class="['rounded-xl', modern ? 'modern-select' : 'mb-3', isMobileApp ? 'mobile-input' : '']"
                                prepend-inner-icon="mdi-shield-check"
                                @update:model-value="$emit('update', 'AntivirusId', $event)"
                                auto-select-first
                                :rules="[v => !!v || ' ']"
                            ></v-autocomplete>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { useCatalogsStore } from '@/stores/catalogs'
import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean,
    modern: Boolean
})

const { isMobileApp } = useMobileDetection()

const emit = defineEmits(['update'])

const catalogsStore = useCatalogsStore()
const { sistemasOperativos, ofimaticas, antivirus } = storeToRefs(catalogsStore)

const selectedOS = computed(() => {
    if (!props.equipo.SistemaOperativoId || !sistemasOperativos.value) return null
    return sistemasOperativos.value.find(os => os.Id === props.equipo.SistemaOperativoId)
})

const isLinuxOrMac = computed(() => {
    if (!selectedOS.value) return false
    const name = selectedOS.value.Nombre.toUpperCase()
    return name.includes('LINUX') || name.includes('MAC') || name.includes('UBUNTU') || name.includes('DEBIAN') || name.includes('CENTOS') || name.includes('RED HAT') || name.includes('APPLE')
})

const selectedOffice = computed(() => {
    if (!props.equipo.OfimaticaId || !ofimaticas.value) return null
    return ofimaticas.value.find(o => o.Id === props.equipo.OfimaticaId)
})

const isOfficeFree = computed(() => {
    if (!selectedOffice.value) return false
    const name = selectedOffice.value.Nombre.toUpperCase()
    return name.includes('LIBRE') || name.includes('OPEN')
})

onMounted(() => {
    catalogsStore.fetchCatalogs(['sistemasOperativos', 'ofimaticas', 'antivirus'])
})
</script>

<style scoped>
.gap-3 { gap: 12px; }
.rounded-xl { border-radius: 12px !important; }
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
    border-color: #d1d5db !important; /* border-gray-300 */
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.05);
}

:deep(.modern-input .v-field--focused),
:deep(.modern-select .v-field--focused) {
    background-color: #ffffff !important;
    border-color: #3b82f6 !important; /* blue-500 */
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15) !important;
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

/* Existing border-thin */
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }

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
