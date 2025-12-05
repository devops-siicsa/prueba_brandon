<template>
    <div class="d-flex h-screen bg-main overflow-hidden font-sans">
        <!-- 1. SIDEBAR DE NAVEGACIÓN MEJORADO (DESKTOP) -->
        <aside v-if="!isMobileApp" class="sidebar-custom d-flex flex-column align-center py-6 bg-white">
            <v-btn icon="mdi-arrow-left" variant="text" color="grey-lighten-1" class="mb-6 hover-scale flex-shrink-0" @click="goBack"></v-btn>

            <div class="flex-grow-1 d-flex flex-column gap-5 w-100 align-center overflow-y-auto hidden-scrollbar" style="min-height: 0;">
                <div 
                    v-for="step in steps" 
                    :key="step.id" 
                    class="position-relative group cursor-pointer w-100 d-flex justify-center flex-shrink-0"
                    @click="scrollTo(step.id)"
                >
                    <!-- Línea conectora -->
                    <div v-if="step.index < steps.length" class="connector-line"></div>

                    <div 
                        class="step-icon d-flex align-center justify-center rounded-xl transition-all"
                        :class="{
                            'active': activeSection === step.id,
                            'completed': isStepComplete(step.id) && activeSection !== step.id
                        }"
                    >
                        <v-icon 
                            v-if="isStepComplete(step.id) && activeSection !== step.id" 
                            icon="mdi-check-circle-outline" 
                            size="20" 
                        ></v-icon>
                        <v-icon 
                            v-else 
                            :icon="step.icon" 
                            size="20"
                        ></v-icon>
                        
                        <!-- Punto indicador activo -->
                        <span v-if="activeSection === step.id" class="active-dot"></span>
                    </div>

                    <!-- Tooltip Mejorado -->
                    <v-tooltip activator="parent" location="end" offset="10" content-class="custom-tooltip">
                        {{ step.label }}
                    </v-tooltip>
                </div>
            </div>

            <div class="pt-6 flex-shrink-0">
                <v-btn 
                    icon="mdi-content-save" 
                    class="save-btn text-white" 
                    size="x-large"
                    elevation="0"
                    :loading="saving"
                    :disabled="!isFormComplete"
                    @click="saveEquipo"
                >
                    <v-icon size="24">mdi-content-save</v-icon>
                </v-btn>
            </div>
        </aside>

        <!-- 2. ÁREA PRINCIPAL DE CONTENIDO -->
        <main 
            class="flex-grow-1 w-100 overflow-y-auto scroll-smooth" 
            :class="isMobileApp ? 'pa-4 pb-16' : 'ml-24 pa-8 pa-lg-16'"
            id="create-container"
        >
            <div style="max-width: 1280px; margin: 0 auto;">
                
                <!-- Header -->
                <header class="d-flex flex-column flex-md-row align-md-end justify-space-between gap-4 animate-fade-in-down" :class="isMobileApp ? 'mb-4' : 'mb-12'">
                    <div>
                        <div class="d-flex align-center gap-3 mb-3">
                            <span class="text-caption font-weight-bold tracking-widest text-uppercase text-primary bg-blue-lighten-5 px-3 py-1 rounded-lg border border-blue-lighten-4">
                                Paso {{ currentStepIndex }} de {{ steps.length }}
                            </span>
                            <span class="dot-separator bg-grey-lighten-1"></span>
                            <span class="text-caption font-weight-medium text-grey-lighten-1 text-uppercase tracking-wider">Registro de Activos</span>
                            
                            <!-- Offline Indicator Badge -->
                            <v-fade-transition>
                                <div v-if="offlineReady" class="d-flex align-center gap-2 ml-2 bg-green-lighten-5 text-green-darken-1 px-3 py-1 rounded-pill border border-green-lighten-4">
                                    <v-icon icon="mdi-cloud-check" size="14"></v-icon>
                                    <span class="text-caption font-weight-bold tracking-wide text-uppercase" style="font-size: 10px;">Offline Activo</span>
                                </div>
                                <div v-else-if="catalogsLoading" class="d-flex align-center gap-2 ml-2 bg-blue-lighten-5 text-blue-darken-1 px-3 py-1 rounded-pill border border-blue-lighten-4">
                                    <v-icon icon="mdi-cloud-sync" size="14" style="animation: spin 2s linear infinite;"></v-icon>
                                    <span class="text-caption font-weight-bold tracking-wide text-uppercase" style="font-size: 10px;">Sincronizando...</span>
                                </div>
                            </v-fade-transition>
                        </div>
                        <h1 class="text-h4 font-weight-bold text-corporate-blue mb-2 tracking-tight">
                            Nuevo Equipo
                        </h1>
                        <p v-if="!isMobileApp" class="text-h6 text-grey-darken-1 font-weight-regular" style="max-width: 600px; line-height: 1.6;">
                            Complete la información inicial para registrar un nuevo activo tecnológico en el sistema centralizado.
                        </p>
                    </div>

                    <!-- Indicador de progreso circular -->
                    <div class="d-none d-lg-flex align-center gap-4 pr-4">
                        <div class="text-right">
                            <p class="text-caption text-grey-lighten-1 font-weight-medium text-uppercase mb-0">Progreso</p>
                            <p class="text-h6 font-weight-bold text-corporate-blue mb-0">{{ progressPercentage }}%</p>
                        </div>
                        <v-progress-circular :model-value="progressPercentage" color="#00A08F" size="48" width="4" class="rotate-45"></v-progress-circular>
                    </div>
                </header>

                <!-- Tarjeta Principal del Formulario -->
                <div class="bg-white rounded-3xl shadow-custom border border-white overflow-hidden animate-fade-in-up">
                    
                    <!-- Header Visual Dinámico -->
                    <div class="position-relative bg-gradient-header border-b" :class="isMobileApp ? 'px-4 py-4' : 'px-10 py-8'">
                        <div class="accent-bar bg-corporate-blue"></div>
                        <div class="d-flex align-center" :class="isMobileApp ? 'gap-3' : 'gap-5'">
                            <div class="icon-box rounded-xl bg-white shadow-sm d-flex align-center justify-center text-corporate-blue border" :class="{ 'mobile-icon-box': isMobileApp }">
                                <v-icon :icon="currentStep.icon" :size="isMobileApp ? 20 : 28"></v-icon>
                            </div>
                            <div>
                                <h2 class="text-h5 font-weight-bold text-grey-darken-3" :class="{ 'text-subtitle-1': isMobileApp }">{{ currentStep.label }}</h2>
                                <p v-if="!isMobileApp" class="text-body-2 text-grey-darken-1">Información requerida para esta sección.</p>
                            </div>
                        </div>
                    </div>

                    <div class="position-relative" :class="isMobileApp ? 'px-2 py-4' : 'pa-10 pa-lg-12'">
                        <!-- Render Active Section -->
                         <v-window v-model="activeSection" class="overflow-visible">
                            <v-window-item value="user">
                                <UserInfoTab :equipo="equipo" :is-editing="true" :modern="true" @update="updateEquipoField" />
                            </v-window-item>
                            <v-window-item value="general">
                                <GeneralInfoTab :equipo="equipo" :is-editing="true" :modern="true" @update="updateEquipoField" />
                            </v-window-item>
                            <v-window-item value="hardware">
                                <HardwareTab :equipo="equipo" :is-editing="true" />
                            </v-window-item>
                            <v-window-item value="software">
                                <SoftwareTab :equipo="equipo" :is-editing="true" :modern="true" @update="updateEquipoField" />
                            </v-window-item>
                            <v-window-item value="apps">
                                <AppsTab :equipo="equipo" :is-editing="true" :modern="true" @update="updateEquipoField" />
                            </v-window-item>
                            <v-window-item value="files">
                                <AttachmentsTab :equipo="equipo" :is-editing="true" :modern="true" @update="updateEquipoField" />
                            </v-window-item>
                            <v-window-item value="history">
                                <HistoryTab :equipo="equipo" :is-editing="true" @update="updateEquipoField" />
                            </v-window-item>
                         </v-window>
                    </div>
                </div>

                <!-- Navigation Buttons (Bottom) -->
                <div class="d-flex justify-end mt-8 gap-4">
                     <v-btn 
                        v-if="currentStepIndex > 1"
                        variant="text" 
                        size="large" 
                        color="grey-darken-1"
                        @click="prevStep"
                    >
                        Anterior
                    </v-btn>
                    <v-btn 
                        v-if="currentStepIndex < steps.length"
                        color="primary" 
                        size="large" 
                        class="px-8 rounded-lg text-capitalize"
                        elevation="2"
                        @click="nextStep"
                    >
                        Siguiente Paso
                        <v-icon end>mdi-arrow-right</v-icon>
                    </v-btn>
                </div>

            </div>
        </main>

        <!-- MOBILE BOTTOM NAV -->
        <div v-if="isMobileApp" class="mobile-bottom-nav d-flex align-center px-4 bg-white border-t">
            <div class="d-flex align-center gap-4 overflow-x-auto hidden-scrollbar flex-grow-1 py-2" style="white-space: nowrap;">
                <div 
                    v-for="step in steps" 
                    :key="step.id" 
                    class="d-flex flex-column align-center justify-center pa-2 rounded-lg transition-all"
                    :class="{ 
                        'bg-blue-lighten-5 text-corporate-blue': activeSection === step.id, 
                        'text-grey': activeSection !== step.id,
                        'completed-mobile': isStepComplete(step.id) && activeSection !== step.id
                    }"
                    @click="scrollTo(step.id)"
                    style="min-width: 60px;"
                >
                    <v-icon :icon="step.icon" :size="activeSection === step.id ? 24 : 20"></v-icon>
                    <span class="text-caption font-weight-medium mt-1" style="font-size: 10px;">{{ step.label }}</span>
                </div>
            </div>
            
            <!-- FAB Save Button -->
            <v-btn
                icon="mdi-content-save"
                color="corporate-blue"
                class="ml-2 mb-12"
                elevation="4"
                position="fixed"
                location="bottom right"
                style="bottom: 80px; right: 16px; z-index: 100;"
                size="large"
                :loading="saving"
                :disabled="!isFormComplete"
                @click="saveEquipo"
            ></v-btn>
        </div>

        <v-snackbar
            v-model="showDraftSnackbar"
            color="info"
            timeout="4000"
            location="bottom right"
        >
            Borrador restaurado automáticamente.
            <template v-slot:actions>
                <v-btn color="white" variant="text" @click="showDraftSnackbar = false">
                    Cerrar
                </v-btn>
            </template>
        </v-snackbar>

        <v-snackbar
            v-model="showQueueSnackbar"
            color="warning"
            timeout="4000"
            location="bottom right"
        >
            Guardado en cola offline. Se subirá cuando haya internet.
            <template v-slot:actions>
                <v-btn color="white" variant="text" @click="showQueueSnackbar = false">
                    Cerrar
                </v-btn>
            </template>
        </v-snackbar>

        <!-- Exit Confirmation Dialog (Ultra Compact) -->
        <v-dialog v-model="showExitDialog" max-width="320" persistent>
            <v-card class="rounded-xl elevation-5 pa-3">
                <v-card-title class="text-subtitle-2 font-weight-bold text-center pt-2 pb-1 text-grey-darken-3">
                    ¿Guardar borrador?
                </v-card-title>
                
                <v-card-text class="text-center text-caption text-grey-darken-1 px-2 pb-3">
                    Tienes cambios sin guardar.
                </v-card-text>

                <v-card-actions class="d-flex flex-column gap-2 px-2 pb-1">
                    <v-btn
                        block
                        color="blue-lighten-4"
                        variant="flat"
                        class="text-capitalize rounded-lg text-blue-darken-4 font-weight-bold"
                        @click="handleExit('save')"
                        height="40"
                        elevation="0"
                    >
                        Guardar y Salir
                    </v-btn>
                    
                    <v-btn
                        block
                        color="red-lighten-4"
                        variant="flat"
                        class="text-capitalize rounded-lg text-red-darken-4 font-weight-bold"
                        @click="handleExit('discard')"
                        height="40"
                        elevation="0"
                    >
                        Descartar
                    </v-btn>
                    
                    <v-btn
                        block
                        color="grey-darken-1"
                        variant="text"
                        size="x-small"
                        class="text-capitalize rounded-lg mt-1"
                        @click="handleExit('cancel')"
                    >
                        Cancelar
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed, watch, onBeforeUnmount } from 'vue'
import { useRouter, useRoute, onBeforeRouteLeave } from 'vue-router'
import { useDisplay } from 'vuetify'
import axios from 'axios'
import GeneralInfoTab from '@/components/Inventory/Tabs/GeneralInfoTab.vue'
import UserInfoTab from '@/components/Inventory/Tabs/UserInfoTab.vue'
import HardwareTab from '@/components/Inventory/Tabs/HardwareTab.vue'
import SoftwareTab from '@/components/Inventory/Tabs/SoftwareTab.vue'
import AppsTab from '@/components/Inventory/Tabs/AppsTab.vue'
import AttachmentsTab from '@/components/Inventory/Tabs/AttachmentsTab.vue'
import HistoryTab from '@/components/Inventory/Tabs/HistoryTab.vue'
import { syncService } from '@/services/syncService'
import { draftService } from '@/services/draftService'
import { useMobileDetection } from '@/composables/useMobileDetection'
import { useCatalogsStore } from '@/stores/catalogs'
import { storeToRefs } from 'pinia'

const router = useRouter()
const route = useRoute()
const catalogsStore = useCatalogsStore()
const { 
    offlineReady, loading: catalogsLoading, tiposEquipo, busesRam,
    protocolosAlmacenamiento, factoresFormaAlmacenamiento,
    sistemasOperativos, ofimaticas
} = storeToRefs(catalogsStore)
const { isMobileApp } = useMobileDetection()

const saving = ref(false)
const activeSection = ref('user')
const showDraftSnackbar = ref(false)
const showQueueSnackbar = ref(false)

// Exit Dialog State
const showExitDialog = ref(false)
const pendingNavigation = ref(null)
const hasChanges = ref(false)

const steps = [
    { id: 'user', label: 'Usuario', icon: 'mdi-account', index: 1 },
    { id: 'general', label: 'Equipo', icon: 'mdi-laptop', index: 2 },
    { id: 'hardware', label: 'Hardware', icon: 'mdi-cpu-64-bit', index: 3 },
    { id: 'software', label: 'Software', icon: 'mdi-microsoft-windows', index: 4 },
    { id: 'apps', label: 'Apps', icon: 'mdi-apps', index: 5 },
    { id: 'files', label: 'Adjuntos', icon: 'mdi-paperclip', index: 6 },
    { id: 'history', label: 'Historial', icon: 'mdi-history', index: 7 },
]

const currentStep = computed(() => steps.find(s => s.id === activeSection.value) || steps[0])
const currentStepIndex = computed(() => currentStep.value.index)

// Calculate progress based on completed steps
const completedStepsCount = computed(() => steps.filter(step => isStepComplete(step.id)).length)
const progressPercentage = computed(() => Math.round((completedStepsCount.value / steps.length) * 100))

const isFormComplete = computed(() => {
    return steps.every(step => isStepComplete(step.id))
})

// Initialize with default values
const equipo = reactive({
    EsPropio: true,
    Procesadores: [],
    MemoriasRAM: [],
    Almacenamiento: []
})

// Track changes
watch(equipo, () => {
    hasChanges.value = true
}, { deep: true })

// Window unload warning
const handleBeforeUnload = (e) => {
    if (hasChanges.value) {
        e.preventDefault()
        e.returnValue = ''
    }
}

// Draft State
const currentDraftKey = ref(route.query.draftKey || null)

onMounted(async () => {
    window.addEventListener('beforeunload', handleBeforeUnload)

    // Pre-fetch ALL catalogs for offline support
    catalogsStore.fetchCatalogs([
        // General
        'estadosEquipo', 'tiposEquipo', 'fabricantes',
        // Hardware
        'marcasProcesador', 'tiposProcesador', 'generacionesProcesador',
        'tiposRam', 'capacidadesRam', 'busesRam',
        'tiposAlmacenamiento', 'capacidadesAlmacenamiento', 'protocolosAlmacenamiento', 'factoresFormaAlmacenamiento',
        // Software
        'sistemasOperativos', 'ofimaticas', 'antivirus',
        // Apps
        'aplicativos'
    ])

    const storedCompanyId = localStorage.getItem('selectedCompanyId')
    if (route.query.companyId) {
        equipo.EmpresaId = parseInt(route.query.companyId)
    } else if (storedCompanyId) {
        equipo.EmpresaId = parseInt(storedCompanyId)
    }

    // Check for draft
    try {
        if (currentDraftKey.value) {
            const draft = await draftService.getDraft(currentDraftKey.value)
            if (draft) {
                Object.assign(equipo, draft)
                showDraftSnackbar.value = true
                setTimeout(() => { hasChanges.value = false }, 100)
            }
        }
    } catch (e) {
        console.error('Error restoring draft', e)
    }
})

onBeforeUnmount(() => {
    window.removeEventListener('beforeunload', handleBeforeUnload)
})

// Navigation Guard
onBeforeRouteLeave((to, from, next) => {
    if (hasChanges.value && !saving.value) {
        // Show dialog
        showExitDialog.value = true
        pendingNavigation.value = next
    } else {
        next()
    }
})

async function handleExit(action) {
    if (action === 'save') {
        try {
            const dataToSave = JSON.parse(JSON.stringify(equipo))
            
            // Generate key if not exists
            if (!currentDraftKey.value) {
                currentDraftKey.value = `draft_${equipo.EmpresaId}_${Date.now()}`
            }
            
            await draftService.saveDraft(currentDraftKey.value, dataToSave)
            hasChanges.value = false // Prevent guard from firing again
            showExitDialog.value = false
            if (pendingNavigation.value) pendingNavigation.value()
        } catch (e) {
            console.error('Error saving draft', e)
            alert('Error al guardar el borrador')
        }
    } else if (action === 'discard') {
        try {
            if (currentDraftKey.value) {
                await draftService.deleteDraft(currentDraftKey.value)
            }
        } catch (e) {
            console.error('Error deleting draft', e)
        }
        hasChanges.value = false
        showExitDialog.value = false
        if (pendingNavigation.value) pendingNavigation.value()
    } else {
        // Cancel
        showExitDialog.value = false
        pendingNavigation.value = null // Cancel navigation
    }
}

function updateEquipoField(field, value) {
    equipo[field] = value
}

function scrollTo(sectionId) {
    activeSection.value = sectionId
}

function nextStep() {
    if (currentStepIndex.value < steps.length) {
        activeSection.value = steps[currentStepIndex.value].id
    }
}

function prevStep() {
    if (currentStepIndex.value > 1) {
        activeSection.value = steps[currentStepIndex.value - 2].id
    }
}

// Validation Logic
function isStepComplete(stepId) {
    switch (stepId) {
        case 'user':
            return !!(equipo.UsuarioNombre && equipo.Cargo && equipo.Area && equipo.Correo && equipo.Telefono && equipo.SedeId);
        case 'general':
            // Check if it's a CLON
            const isClon = () => {
                if (!equipo.TipoEquipoId || !tiposEquipo.value) return false
                const tipo = tiposEquipo.value.find(t => t.Id === equipo.TipoEquipoId)
                return tipo && tipo.Nombre.toLowerCase().includes('clon')
            }

            // Check essential general info fields
            let basicInfo = !!(equipo.CodigoEquipo && equipo.EstadoEquipoId && equipo.TipoEquipoId);
            
            // Only require specific fields if NOT a clone
            if (!isClon()) {
                basicInfo = basicInfo && !!(equipo.FabricanteId && equipo.Modelo && equipo.Serial);
            }

            // If rented, check rental fields
            if (!equipo.EsPropio) {
                return basicInfo && !!(equipo.ProveedorAlquiler && equipo.CodigoAlquiler);
            }
            return basicInfo;
        case 'hardware':
            const isBusNA = (slot) => {
                if (!slot.VelocidadId || !busesRam.value) return false
                const bus = busesRam.value.find(b => b.Id === slot.VelocidadId)
                return bus && (bus.Nombre.toUpperCase() === 'N/A' || bus.Nombre.toUpperCase() === 'NA')
            }

            const hasRam = equipo.MemoriasRAM?.length > 0 && 
                           equipo.MemoriasRAM[0].TipoId && 
                           equipo.MemoriasRAM[0].VelocidadId &&
                           (isBusNA(equipo.MemoriasRAM[0]) || equipo.MemoriasRAM[0].CapacidadId);

            const hasStorage = (() => {
                if (!equipo.Almacenamiento || equipo.Almacenamiento.length === 0) return false
                const disk = equipo.Almacenamiento[0]
                if (!disk.TipoId || !disk.CapacidadId) return false
                
                // Protocol check
                const filteredProtocols = protocolosAlmacenamiento.value ? protocolosAlmacenamiento.value.filter(p => p.TipoId === disk.TipoId) : []
                if (filteredProtocols.length > 0 && !disk.ProtocoloId) return false
                
                // Form Factor check
                const filteredFactors = factoresFormaAlmacenamiento.value ? factoresFormaAlmacenamiento.value.filter(f => f.TipoId === disk.TipoId) : []
                if (filteredFactors.length > 0 && !disk.FactorFormaId) return false
                
                return true
            })();

            return !!(hasRam && hasStorage);
        case 'software':
            // 1. OS Validation
            if (!equipo.SistemaOperativoId) return false;
            
            const isLinuxOrMac = (() => {
                if (!sistemasOperativos.value) return false;
                const os = sistemasOperativos.value.find(o => o.Id === equipo.SistemaOperativoId);
                if (!os) return false;
                const name = os.Nombre.toUpperCase();
                return name.includes('LINUX') || name.includes('MAC') || name.includes('UBUNTU') || name.includes('DEBIAN') || name.includes('CENTOS') || name.includes('RED HAT') || name.includes('APPLE');
            })();

            if (isLinuxOrMac) {
                if (!equipo.Distribucion) return false;
            } else {
                if (!equipo.LicenciaSO) return false; // Windows/Others require license
            }

            // 2. Office Validation
            if (!equipo.OfimaticaId) return false;

            const isOfficeFree = (() => {
                 if (!ofimaticas.value) return false;
                 const office = ofimaticas.value.find(o => o.Id === equipo.OfimaticaId);
                 if (!office) return false;
                 const name = office.Nombre.toUpperCase();
                 return name.includes('LIBRE') || name.includes('OPEN');
            })();

            if (isOfficeFree) {
                if (!equipo.DistribucionOfimatica) return false;
            } else {
                if (!equipo.LicenciaOfimatica) return false;
            }

            // 3. Network & Security Validation
            return !!(equipo.EquipoPertenece && 
                      equipo.NombreGrupoDominio && 
                      equipo.NombreEnRed && 
                      equipo.AntivirusId);
        case 'apps':
            return equipo.Aplicativos && equipo.Aplicativos.length >= 5;
        case 'files':
        case 'history':
            return true; // Optional steps
        default:
            return false;
    }
}

async function saveEquipo() {
    saving.value = true
    try {
        // Check if offline
        if (!navigator.onLine) {
            throw new Error('OFFLINE')
        }

        const res = await axios.post('/api/inventory/equipos', equipo, { withCredentials: true })
        
        // Clear draft on success
        if (currentDraftKey.value) {
            await draftService.deleteDraft(currentDraftKey.value)
        }
        hasChanges.value = false // Reset changes
        
        router.push({ name: 'EquipmentDetail', params: { id: res.data.Id } })
    } catch (e) {
        // Handle offline or network error
        if (e.message === 'OFFLINE' || e.code === 'ERR_NETWORK' || !e.response) {
            try {
                // Save to offline queue
                const dataToSave = JSON.parse(JSON.stringify(equipo))
                await syncService.addToQueue(dataToSave)
                
                // Clear draft
                if (currentDraftKey.value) {
                    await draftService.deleteDraft(currentDraftKey.value)
                }
                hasChanges.value = false // Reset changes
                
                // Show feedback and reset form (or redirect)
                showQueueSnackbar.value = true
                
                // Reset form for next entry (optional, or redirect to list)
                // For now, we'll redirect to inventory home to show it's "done"
                setTimeout(() => {
                    router.push({ name: 'InventoryHome' })
                }, 2000)
                
            } catch (queueError) {
                console.error("Error adding to queue", queueError)
                alert("Error al guardar en modo offline")
            }
        } else {
            console.error("Error creating equipment", e)
            alert(e.response?.data?.message || "Error al crear el equipo")
        }
    } finally {
        saving.value = false
    }
}

function goBack() {
    router.back()
}
</script>

<style scoped>
/* Layout & Typography */
.h-screen { height: 100vh; }
.font-sans { font-family: 'Inter', sans-serif !important; }
.ml-24 { margin-left: 96px; }
.gap-3 { gap: 12px; }
.gap-4 { gap: 16px; }
.gap-5 { gap: 20px; }
.rounded-3xl { border-radius: 2rem !important; }
.rounded-xl { border-radius: 0.75rem !important; }
.tracking-widest { letter-spacing: 0.1em; }
.tracking-tight { letter-spacing: -0.025em; }

/* Colors */
.bg-main { background-color: #F8F9FA !important; }
.text-corporate-blue { color: #223551 !important; }
.bg-corporate-blue { background-color: #223551 !important; }

/* Sidebar */
.sidebar-custom {
    width: 96px;
    height: 100%;
    position: fixed;
    z-index: 20;
    box-shadow: 4px 0 30px rgba(0,0,0,0.15); /* Increased opacity for better definition */
}

.step-icon {
    width: 48px;
    height: 48px;
    color: #cbd5e1; /* gray-300 */
    background: white;
    cursor: pointer;
    position: relative;
    transition: all 0.3s ease;
    border: 2px solid transparent;
}

.step-icon:hover {
    background-color: #f8fafc; /* Relleno del icono */
    color: #64748b; /* Color del texto */
}

.step-icon.active {
    background-color: #223551; /* Relleno del icono */
    color: white; /* Color del texto */
    box-shadow: 0 10px 30px -10px rgba(30, 58, 138, 0.6); /* Stronger, more centered shadow */
    transform: scale(1.1);
    border-color: #223551; /* Color del borde */
}

.step-icon.completed {
    background-color: white;
    color: #4ade80; /* green-400 - Vivid green for icon */
    border: 2px solid #4ade80; /* green-400 */
    box-shadow: 0 0 15px rgba(74, 222, 128, 0.5); /* Strong green glow */
}

/* Mobile Completed State */
.completed-mobile {
    color: #4ade80 !important;
    text-shadow: 0 0 10px rgba(74, 222, 128, 0.4);
}
.completed-mobile .v-icon {
    color: #4ade80 !important;
    filter: drop-shadow(0 0 2px rgba(74, 222, 128, 0.5));
}

.active-dot {
    position: absolute;
    top: -4px;
    right: -4px;
    width: 12px;
    height: 12px;
    background-color: #4ade80; /* green-400 */
    border: 2px solid white;
    border-radius: 50%;
}

.connector-line {
    position: absolute;
    top: 40px;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 20px;
    background-color: #f1f5f9;
    z-index: -1;
}

.save-btn {
    width: 56px;
    height: 56px;
    border-radius: 16px;
    background-color: #00A08F !important;
    box-shadow: 0 20px 25px -5px rgba(0, 160, 143, 0.3);
    transition: all 0.3s;
}
.save-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 25px 30px -5px rgba(0, 160, 143, 0.4);
}

/* Scrollbar Hiding */
.hidden-scrollbar::-webkit-scrollbar {
    display: none;
}
.hidden-scrollbar {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
}

/* Main Card */
.shadow-custom {
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1); /* shadow-2xl shadow-gray-200/60 approximation */
}

.bg-gradient-header {
    background: linear-gradient(to right, #f8fafc, #ffffff);
}

.accent-bar {
    position: absolute;
    top: 0;
    left: 0;
    width: 6px;
    height: 100%;
}

.icon-box {
    width: 56px;
    height: 56px;
}

.mobile-icon-box {
    width: 40px !important;
    height: 40px !important;
}

.dot-separator {
    width: 4px;
    height: 4px;
    border-radius: 50%;
}

.rotate-45 {
    transform: rotate(-45deg);
}

/* Animations */
@keyframes fadeInDown {
    from { opacity: 0; transform: translate3d(0, -20px, 0); }
    to { opacity: 1; transform: translate3d(0, 0, 0); }
}
.animate-fade-in-down { animation: fadeInDown 0.5s ease-out; }

@keyframes fadeInUp {
    from { opacity: 0; transform: translate3d(0, 20px, 0); }
    to { opacity: 1; transform: translate3d(0, 0, 0); }
}
.animate-fade-in-up { animation: fadeInUp 0.7s ease-out; }

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.mobile-bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 70px;
    z-index: 50;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.05);
}
</style>
