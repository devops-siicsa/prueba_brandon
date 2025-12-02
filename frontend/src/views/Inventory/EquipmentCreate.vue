<template>
    <div class="d-flex h-screen bg-main overflow-hidden font-sans">
        <!-- 1. SIDEBAR DE NAVEGACIÓN MEJORADO -->
        <aside class="sidebar-custom d-flex flex-column align-center py-6 bg-white">
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
                    @click="saveEquipo"
                >
                    <v-icon size="24">mdi-content-save</v-icon>
                </v-btn>
            </div>
        </aside>

        <!-- 2. ÁREA PRINCIPAL DE CONTENIDO -->
        <main class="flex-grow-1 ml-24 pa-8 pa-lg-16 w-100 overflow-y-auto scroll-smooth" id="create-container">
            <div style="max-width: 1280px; margin: 0 auto;">
                
                <!-- Header -->
                <header class="mb-12 d-flex flex-column flex-md-row align-md-end justify-space-between gap-4 animate-fade-in-down">
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
                        <p class="text-h6 text-grey-darken-1 font-weight-regular" style="max-width: 600px; line-height: 1.6;">
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
                    <div class="position-relative bg-gradient-header border-b px-10 py-8">
                        <div class="accent-bar bg-corporate-blue"></div>
                        <div class="d-flex align-center gap-5">
                            <div class="icon-box rounded-xl bg-white shadow-sm d-flex align-center justify-center text-corporate-blue border">
                                <v-icon :icon="currentStep.icon" size="28"></v-icon>
                            </div>
                            <div>
                                <h2 class="text-h5 font-weight-bold text-grey-darken-3">{{ currentStep.label }}</h2>
                                <p class="text-body-2 text-grey-darken-1">Información requerida para esta sección.</p>
                            </div>
                        </div>
                    </div>

                    <div class="pa-10 pa-lg-12 position-relative">
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
                                <SoftwareTab :equipo="equipo" :is-editing="true" @update="updateEquipoField" />
                            </v-window-item>
                            <v-window-item value="apps">
                                <div class="text-center py-12 text-grey">Módulo de Aplicativos en construcción</div>
                            </v-window-item>
                            <v-window-item value="files">
                                <div class="text-center py-12 text-grey">Módulo de Adjuntos en construcción</div>
                            </v-window-item>
                            <v-window-item value="history">
                                <div class="text-center py-12 text-grey">El historial se generará automáticamente.</div>
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
    </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import GeneralInfoTab from '@/components/Inventory/Tabs/GeneralInfoTab.vue'
import UserInfoTab from '@/components/Inventory/Tabs/UserInfoTab.vue'
import HardwareTab from '@/components/Inventory/Tabs/HardwareTab.vue'
import SoftwareTab from '@/components/Inventory/Tabs/SoftwareTab.vue'
import { syncService } from '@/services/syncService'
import { draftService } from '@/services/draftService'
import { useCatalogsStore } from '@/stores/catalogs'
import { storeToRefs } from 'pinia'

const router = useRouter()
const route = useRoute()
const catalogsStore = useCatalogsStore()
const { offlineReady, loading: catalogsLoading } = storeToRefs(catalogsStore)

const saving = ref(false)
const activeSection = ref('user')
const showDraftSnackbar = ref(false)
const showQueueSnackbar = ref(false)

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

// Initialize with default values
const equipo = reactive({
    EsPropio: true,
    Procesadores: [],
    MemoriasRAM: [],
    Almacenamiento: []
})

// Auto-save draft
let draftTimeout = null
watch(equipo, (newVal) => {
    if (draftTimeout) clearTimeout(draftTimeout)
    draftTimeout = setTimeout(async () => {
        try {
            // Convert reactive object to plain object for storage
            const dataToSave = JSON.parse(JSON.stringify(newVal))
            await draftService.saveDraft('new_equipment_draft', dataToSave)
            // console.log('Draft saved')
        } catch (e) {
            console.error('Error saving draft', e)
        }
    }, 1000)
}, { deep: true })

onMounted(async () => {
    // Pre-fetch ALL catalogs for offline support
    catalogsStore.fetchCatalogs([
        // General
        'estadosEquipo', 'tiposEquipo', 'fabricantes',
        // Hardware
        'marcasProcesador', 'tiposProcesador', 'generacionesProcesador',
        'tiposRam', 'capacidadesRam', 'busesRam',
        'tiposAlmacenamiento', 'capacidadesAlmacenamiento', 'protocolosAlmacenamiento', 'factoresFormaAlmacenamiento',
        // Software
        'sistemasOperativos', 'ofimaticas', 'antivirus'
    ])

    const storedCompanyId = localStorage.getItem('selectedCompanyId')
    if (route.query.companyId) {
        equipo.EmpresaId = parseInt(route.query.companyId)
    } else if (storedCompanyId) {
        equipo.EmpresaId = parseInt(storedCompanyId)
    }

    // Check for draft
    try {
        const draft = await draftService.getDraft('new_equipment_draft')
        if (draft) {
            // Restore draft
            Object.assign(equipo, draft)
            showDraftSnackbar.value = true
        }
    } catch (e) {
        console.error('Error restoring draft', e)
    }
})

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
            // Check essential general info fields
            const basicInfo = !!(equipo.CodigoEquipo && equipo.EstadoEquipoId && equipo.TipoEquipoId && equipo.FabricanteId && equipo.Modelo && equipo.Serial);
            // If rented, check rental fields
            if (!equipo.EsPropio) {
                return basicInfo && !!(equipo.ProveedorAlquiler && equipo.CodigoAlquiler);
            }
            return basicInfo;
        case 'hardware':
            // Example: At least one processor and RAM
            // return equipo.Procesadores?.length > 0 && equipo.MemoriasRAM?.length > 0;
            return false; // Placeholder for now until Hardware logic is fully implemented
        case 'software':
             // Example: At least one OS selected (if applicable)
             return false; // Placeholder
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
        await draftService.deleteDraft('new_equipment_draft')
        
        router.push({ name: 'EquipmentDetail', params: { id: res.data.Id } })
    } catch (e) {
        // Handle offline or network error
        if (e.message === 'OFFLINE' || e.code === 'ERR_NETWORK' || !e.response) {
            try {
                // Save to offline queue
                const dataToSave = JSON.parse(JSON.stringify(equipo))
                await syncService.addToQueue(dataToSave)
                
                // Clear draft
                await draftService.deleteDraft('new_equipment_draft')
                
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
    color: #00A08F; /* Green Action */
    border: 2px solid #d1fae5; /* green-100 */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Subtle shadow for white icons */
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
</style>
