<template>
    <div class="h-100 d-flex flex-column">
        <!-- Toolbar (Sticky Top) -->
        <div class="flex-shrink-0 pb-4">
            <div class="d-flex align-center gap-3">
                <!-- Search -->
                <!-- Search -->
                <v-text-field
                    v-model="searchQuery"
                    placeholder="Buscar aplicativos..."
                    :variant="isEditing ? 'solo' : 'outlined'"
                    :flat="isEditing"
                    hide-details
                    density="comfortable"
                    :class="['flex-grow-1 rounded-xl', isEditing ? 'modern-input' : 'bg-transparent', isMobileApp ? 'mobile-input' : '']"
                    prepend-inner-icon="mdi-magnify"
                    clearable
                ></v-text-field>

                <!-- View Toggle -->
                <v-menu
                    v-if="selectedApps.length > 0 && !isMobileApp"
                    location="bottom end"
                    :close-on-content-click="false"
                >
                    <template v-slot:activator="{ props }">
                        <v-chip
                            v-bind="props"
                            color="primary"
                            variant="flat"
                            class="font-weight-bold mr-2 cursor-pointer"
                            prepend-icon="mdi-basket"
                            link
                        >
                            {{ selectedApps.length }} Seleccionadas
                        </v-chip>
                    </template>

                    <v-card min-width="300" max-width="400" class="rounded-xl">
                        <v-card-title class="text-subtitle-1 font-weight-bold pa-4 border-b">
                            Apps Seleccionadas
                        </v-card-title>
                        <v-list class="py-0" style="max-height: 300px; overflow-y: auto;">
                            <v-list-item
                                v-for="app in selectedApps"
                                :key="app.Id"
                                :title="app.Nombre"
                                :subtitle="app.Version"
                            >
                                <template v-slot:prepend>
                                    <v-avatar :color="getAppColor(app.Nombre)" size="32" rounded="lg" class="mr-2">
                                        <span class="text-white text-caption">{{ app.Nombre.charAt(0) }}</span>
                                    </v-avatar>
                                </template>
                                <template v-slot:append>
                                    <v-btn
                                        icon="mdi-close"
                                        size="small"
                                        variant="text"
                                        color="grey"
                                        @click="toggleSelection(app)"
                                    ></v-btn>
                                </template>
                            </v-list-item>
                        </v-list>
                    </v-card>
                </v-menu>

                <div class="d-flex bg-white rounded-xl pa-1 border-thin shadow-sm">
                    <v-btn
                        :variant="viewMode === 'grid' ? 'flat' : 'text'"
                        :color="viewMode === 'grid' ? 'primary' : 'grey-darken-1'"
                        class="rounded-lg"
                        size="small"
                        icon="mdi-view-grid"
                        @click="viewMode = 'grid'"
                    ></v-btn>
                    <v-btn
                        :variant="viewMode === 'list' ? 'flat' : 'text'"
                        :color="viewMode === 'list' ? 'primary' : 'grey-darken-1'"
                        class="rounded-lg"
                        size="small"
                        icon="mdi-view-list"
                        @click="viewMode = 'list'"
                    ></v-btn>
                </div>

                <!-- Create Button -->
                <v-btn
                    v-if="isEditing"
                    color="corporate-blue"
                    :prepend-icon="!isMobileApp ? 'mdi-plus' : undefined"
                    :class="['rounded-xl text-white', isMobileApp ? 'px-0' : 'px-6 font-weight-bold text-capitalize']"
                    elevation="0"
                    height="44"
                    :min-width="isMobileApp ? '44' : undefined"
                    @click="showCreateDialog = true"
                >
                    <v-icon v-if="isMobileApp">mdi-plus</v-icon>
                    <span v-else>Crear App</span>
                </v-btn>
            </div>
        </div>

        <!-- Main Content (Split View) -->
        <v-row class="flex-grow-1 overflow-hidden ma-0" style="min-height: 0;">
            
            <!-- Gallery (Scrollable) -->
            <v-col cols="12" class="h-100 overflow-y-auto px-0 pt-0 custom-scrollbar">
                
                <!-- Loading -->
                <div v-if="loading" class="d-flex justify-center align-center h-50">
                    <v-progress-circular indeterminate color="primary"></v-progress-circular>
                </div>

                <!-- Empty State -->
                <!-- Empty State -->
                <div v-else-if="filteredApps.length === 0" class="d-flex flex-column align-center justify-center h-50 text-grey">
                    <v-icon size="64" color="grey-lighten-2">mdi-store-search</v-icon>
                    <div class="text-h6 text-grey-lighten-1 mt-4">
                        {{ isEditing ? 'No se encontraron aplicativos' : 'Sin aplicativos asignados' }}
                    </div>
                    <div v-if="!isEditing" class="text-body-2 text-grey-lighten-1 mt-2 text-center" style="max-width: 300px;">
                        Para asignar aplicativos a este equipo, haz clic en el botón <span class="font-weight-bold">"Editar Equipo"</span>.
                    </div>
                    <v-btn
                        v-if="isEditing"
                        variant="text"
                        color="primary"
                        class="mt-2 text-capitalize"
                        @click="showCreateDialog = true"
                    >
                        Crear "{{ searchQuery }}"
                    </v-btn>
                </div>

                <!-- Grid View -->
                <v-row v-else-if="viewMode === 'grid'" dense>
                    <v-col
                        v-for="app in paginatedApps"
                        :key="app.Id"
                        :cols="isMobileApp ? 6 : 12"
                        sm="6"
                        class="v-col-md-custom-5"
                    >
                        <v-hover v-slot="{ isHovering, props }">
                            <v-card
                                v-bind="props"
                                class="rounded-xl transition-all h-100 position-relative"
                                :class="[
                                    isSelected(app) && isEditing ? 'border-primary ring-2' : 'border-thin',
                                    isHovering && isEditing ? 'elevation-3 transform-up' : 'elevation-0',
                                    isEditing ? 'cursor-pointer' : '',
                                    !isEditing ? 'bg-grey-lighten-5 border-0' : 'bg-white'
                                ]"
                                @click="toggleSelection(app)"
                                :ripple="isEditing"
                            >
                                <!-- Selected Badge -->
                                <v-scale-transition>
                                    <div v-if="isSelected(app) && isEditing" class="selected-badge">
                                        <v-icon color="white" size="12">mdi-check</v-icon>
                                    </div>
                                </v-scale-transition>

                                <v-card-text class="d-flex flex-column align-center text-center h-100" :class="isMobileApp ? 'pa-2' : 'pa-3'">
                                    <v-avatar
                                        :color="getAppColor(app.Nombre)"
                                        :size="isMobileApp ? 40 : 48"
                                        class="mb-2 shadow-sm"
                                        rounded="xl"
                                    >
                                        <span class="font-weight-bold text-white" :class="isMobileApp ? 'text-subtitle-2' : 'text-h6'">
                                            {{ app.Nombre.charAt(0).toUpperCase() }}
                                        </span>
                                    </v-avatar>
                                    
                                    <div class="font-weight-bold text-grey-darken-3 text-truncate w-100 mb-0" :class="isMobileApp ? 'text-caption' : 'text-body-2'" :title="app.Nombre">
                                        {{ app.Nombre }}
                                    </div>
                                    <div class="text-caption text-grey text-truncate w-100" style="font-size: 0.7rem !important;">
                                        {{ app.Version || 'v1.0' }}
                                    </div>
                                </v-card-text>
                            </v-card>
                        </v-hover>
                    </v-col>
                </v-row>

                <!-- List View -->
                <v-list v-else bg-color="transparent" class="pa-0">
                    <v-list-item
                        v-for="app in paginatedApps"
                        :key="app.Id"
                        :value="app"
                        class="mb-2 rounded-xl border-thin transition-all"
                        :class="[
                            isSelected(app) && isEditing ? 'border-primary bg-blue-lighten-5' : 'bg-white',
                            !isEditing ? 'bg-grey-lighten-5 border-0' : ''
                        ]"
                        @click="toggleSelection(app)"
                        :ripple="isEditing"
                    >
                        <template v-slot:prepend>
                            <v-avatar
                                :color="getAppColor(app.Nombre)"
                                class="mr-3"
                                rounded="lg"
                                size="40"
                            >
                                <span class="text-subtitle-1 font-weight-bold text-white">
                                    {{ app.Nombre.charAt(0).toUpperCase() }}
                                </span>
                            </v-avatar>
                        </template>
                        <v-list-item-title class="font-weight-bold text-grey-darken-3">{{ app.Nombre }}</v-list-item-title>
                        <v-list-item-subtitle>{{ app.Version || 'v1.0' }}</v-list-item-subtitle>
                        
                        <template v-slot:append>
                            <v-icon v-if="isSelected(app) && isEditing" color="primary">mdi-check-circle</v-icon>
                        </template>
                    </v-list-item>
                </v-list>
            </v-col>
        </v-row>

        <!-- Pagination Footer -->
        <div class="flex-shrink-0 pt-2 border-t bg-white">
            <div class="d-flex align-center justify-end px-4 py-2 gap-4 text-caption text-grey-darken-1">
                <div class="d-flex align-center gap-2">
                    <span>Items por página:</span>
                    <v-select
                        v-model="itemsPerPage"
                        :items="[10, 20, 50, 100]"
                        variant="outlined"
                        density="compact"
                        hide-details
                        class="rounded-lg"
                        style="width: 80px"
                    ></v-select>
                </div>
                
                <div>
                    {{ paginationText }}
                </div>

                <div class="d-flex align-center">
                    <v-btn
                        icon="mdi-chevron-left"
                        variant="text"
                        density="comfortable"
                        :disabled="page === 1"
                        @click="page--"
                    ></v-btn>
                    <v-btn
                        icon="mdi-chevron-right"
                        variant="text"
                        density="comfortable"
                        :disabled="page >= pageCount"
                        @click="page++"
                    ></v-btn>
                </div>
            </div>
        </div>

        <!-- Mobile Selection Sheet -->
        <v-bottom-sheet v-model="showMobileSelection" inset>
            <v-card class="rounded-t-xl">
                <v-card-title class="d-flex justify-space-between align-center">
                    <span>Apps Seleccionadas ({{ selectedApps.length }})</span>
                    <v-btn icon="mdi-close" variant="text" @click="showMobileSelection = false"></v-btn>
                </v-card-title>
                <v-card-text style="max-height: 50vh; overflow-y: auto;">
                    <v-list>
                        <v-list-item
                            v-for="app in selectedApps"
                            :key="app.Id"
                            :title="app.Nombre"
                            :subtitle="app.Version"
                        >
                            <template v-slot:prepend>
                                <v-avatar :color="getAppColor(app.Nombre)" size="32" rounded="lg">
                                    <span class="text-white">{{ app.Nombre.charAt(0) }}</span>
                                </v-avatar>
                            </template>
                            <template v-slot:append>
                                <v-btn icon="mdi-delete-outline" color="error" variant="text" @click="toggleSelection(app)"></v-btn>
                            </template>
                        </v-list-item>
                    </v-list>
                </v-card-text>
            </v-card>
        </v-bottom-sheet>

        <!-- Mobile FAB -->
        <v-fab-transition>
            <v-btn
                v-if="selectedApps.length > 0 && $vuetify.display.smAndDown"
                color="primary"
                icon="mdi-basket"
                position="fixed"
                location="bottom right"
                class="mb-4 mr-4"
                @click="showMobileSelection = true"
                style="z-index: 100;"
            >
                <v-badge :content="selectedApps.length" color="error">
                    <v-icon>mdi-basket</v-icon>
                </v-badge>
            </v-btn>
        </v-fab-transition>

        <!-- Create Dialog -->
        <v-dialog v-model="showCreateDialog" max-width="400">
            <v-card class="rounded-xl">
                <v-card-title class="text-h6 font-weight-bold pa-4 bg-grey-lighten-5">
                    Crear Nuevo Aplicativo
                </v-card-title>
                <v-card-text class="pa-4 pt-6">
                    <v-text-field
                        v-model="newApp.Nombre"
                        label="Nombre del Aplicativo"
                        variant="outlined"
                        class="mb-3"
                        autofocus
                        rounded="lg"
                        :density="isMobileApp ? undefined : 'comfortable'"
                    ></v-text-field>
                    <v-text-field
                        v-model="newApp.Version"
                        label="Versión (Opcional)"
                        variant="outlined"
                        rounded="lg"
                        :density="isMobileApp ? undefined : 'comfortable'"
                    ></v-text-field>
                </v-card-text>
                <v-card-actions class="pa-4 pt-0 justify-end">
                    <v-btn variant="text" color="grey" @click="showCreateDialog = false">Cancelar</v-btn>
                    <v-btn
                        color="primary"
                        variant="flat"
                        class="rounded-lg px-6"
                        :disabled="!newApp.Nombre"
                        @click="createApp"
                    >
                        Crear
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useCatalogsStore } from '@/stores/catalogs'
import { storeToRefs } from 'pinia'
import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean,
    modern: Boolean
})

const emit = defineEmits(['update'])
const { isMobileApp } = useMobileDetection()
const catalogsStore = useCatalogsStore()
const { aplicativos, loading } = storeToRefs(catalogsStore)

const searchQuery = ref('')
const viewMode = ref('grid')
const showCreateDialog = ref(false)
const showMobileSelection = ref(false)
const newApp = ref({ Nombre: '', Version: '' })

// Pagination
const page = ref(1)
const itemsPerPage = ref(10)

// Colors for dynamic icons
const appColors = [
    '#EF4444', '#F59E0B', '#10B981', '#3B82F6', '#6366F1', 
    '#8B5CF6', '#EC4899', '#F43F5E', '#0EA5E9', '#84CC16'
]

function getAppColor(name) {
    if (!name) return '#9CA3AF'
    let hash = 0
    for (let i = 0; i < name.length; i++) {
        hash = name.charCodeAt(i) + ((hash << 5) - hash)
    }
    const index = Math.abs(hash % appColors.length)
    return appColors[index]
}

// Use ref for selected IDs to ensure proper reactivity
const selectedIds = ref([])
const isTogglingManually = ref(false) // Flag to prevent watch interference

// Sync selectedIds with props when equipo changes (but not during manual toggles)
watch(() => props.equipo.Aplicativos, (newApps) => {
    // Skip if we're in the middle of a manual toggle
    if (isTogglingManually.value) return
    
    if (newApps) {
        selectedIds.value = newApps
            .filter(a => a && a.AplicacionId)
            .map(a => a.AplicacionId)
    } else {
        selectedIds.value = []
    }
}, { immediate: true })

const filteredApps = computed(() => {
    // In View Mode, only show selected (assigned) apps. In Edit Mode, show all for selection.
    const source = props.isEditing ? aplicativos.value : selectedApps.value
    
    if (!searchQuery.value) return source
    const query = searchQuery.value.toLowerCase()
    return source.filter(app => 
        app.Nombre.toLowerCase().includes(query)
    )
})

const paginatedApps = computed(() => {
    const start = (page.value - 1) * itemsPerPage.value
    const end = start + itemsPerPage.value
    return filteredApps.value.slice(start, end)
})

const pageCount = computed(() => {
    return Math.ceil(filteredApps.value.length / itemsPerPage.value)
})

const paginationText = computed(() => {
    const total = filteredApps.value.length
    if (total === 0) return '0-0 de 0'
    const start = (page.value - 1) * itemsPerPage.value + 1
    const end = Math.min(start + itemsPerPage.value - 1, total)
    return `${start}-${end} de ${total}`
})

// Reset page when search changes
watch(searchQuery, () => {
    page.value = 1
})

const selectedApps = computed(() => {
    return aplicativos.value.filter(app => selectedIds.value.includes(app.Id))
})

function isSelected(app) {
    return selectedIds.value.includes(app.Id)
}

function toggleSelection(app) {
    if (!props.isEditing) return
    
    isTogglingManually.value = true // Set flag to prevent watch
    
    const index = selectedIds.value.indexOf(app.Id)
    if (index === -1) {
        selectedIds.value.push(app.Id)
    } else {
        selectedIds.value.splice(index, 1)
    }
    
    // Emit the update
    emit('update', 'Aplicativos', selectedIds.value)
    
    // Reset flag after a short delay to allow parent update
    setTimeout(() => {
        isTogglingManually.value = false
    }, 100)
}

async function createApp() {
    if (!newApp.value.Nombre) return
    
    try {
        const created = await catalogsStore.createAplicativo(newApp.value.Nombre, newApp.value.Version)
        toggleSelection(created)
        newApp.value = { Nombre: '', Version: '' }
        showCreateDialog.value = false
    } catch (e) {
        console.error('Failed to create app', e)
    }
}

onMounted(() => {
    catalogsStore.fetchCatalogs(['aplicativos'])
})
</script>

<style scoped>
.gap-3 { gap: 12px; }
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }
.border-primary { border-color: #3b82f6 !important; }
.ring-2 { box-shadow: 0 0 0 2px #3b82f6 !important; }
.cursor-pointer { cursor: pointer; }
.transition-all { transition: all 0.2s ease; }

.transform-up { transform: translateY(-4px); }

.selected-badge {
    position: absolute;
    top: 8px;
    right: 8px;
    background-color: #3b82f6;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
}

.text-corporate-blue { color: #223551 !important; }
.bg-corporate-blue { background-color: #223551 !important; }

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

/* Modern Input */
:deep(.modern-input .v-field) {
    border-radius: 12px !important;
    background-color: #f3f4f6 !important;
    border: 1px solid #e5e7eb !important;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}
:deep(.modern-input .v-field--focused) {
    background-color: #ffffff !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15) !important;
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

@media (min-width: 960px) {
    .v-col-md-custom-5 {
        flex: 0 0 20% !important;
        max-width: 20% !important;
    }
}
</style>
