<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useMobileDetection } from '@/composables/useMobileDetection'
import axios from 'axios'
import { draftService } from '@/services/draftService'

const props = defineProps({
    companyId: {
        type: [Number, String],
        required: true
    }
})

const router = useRouter()
const { isMobileApp } = useMobileDetection()

const search = ref('')
const loading = ref(false)
const equipos = ref([])
const drafts = ref([])
const showDraftsDialog = ref(false)
const showResumePrompt = ref(false)

const filteredEquipos = computed(() => {
    if (!Array.isArray(equipos.value)) return []
    let result = equipos.value
    
    if (search.value) {
        const term = search.value.toLowerCase()
        result = result.filter(e => 
            (e.Modelo && e.Modelo.toString().toLowerCase().includes(term)) ||
            (e.CodigoEquipo && e.CodigoEquipo.toString().toLowerCase().includes(term)) ||
            (e.Serial && e.Serial.toString().toLowerCase().includes(term)) ||
            (e.UsuarioNombre && e.UsuarioNombre.toString().toLowerCase().includes(term))
        )
    }
    return result
})

async function loadEquipos() {
    loading.value = true
    try {
        const response = await axios.get('/api/inventory/equipos', { 
            params: { companyId: props.companyId },
            withCredentials: true 
        })
        equipos.value = Array.isArray(response.data) ? response.data : []
    } catch (error) {
        console.error('Error loading equipments:', error)
        equipos.value = []
    } finally {
        loading.value = false
    }
}

async function loadDrafts() {
    try {
        const cid = parseInt(props.companyId)
        if (!isNaN(cid)) {
            const allDrafts = await draftService.getDraftsByCompany(cid)
            drafts.value = Array.isArray(allDrafts) ? allDrafts : []
        }
    } catch (e) {
        console.error('Error loading drafts', e)
        drafts.value = []
    }
}

function openDrafts() {
    showDraftsDialog.value = true
}

function openDraft(draft) {
    showDraftsDialog.value = false
    router.push({ 
        name: 'EquipmentCreate', 
        query: { 
            companyId: props.companyId,
            draftKey: draft.key 
        } 
    })
}

async function deleteDraft(draft) {
    try {
        await draftService.deleteDraft(draft.key)
        await loadDrafts()
        if (drafts.value.length === 0) {
            showDraftsDialog.value = false
        }
    } catch (e) {
        console.error('Error deleting draft', e)
    }
}

function handleNewEquipmentClick() {
    if (drafts.value.length > 0) {
        showResumePrompt.value = true
    } else {
        navigateToCreate()
    }
}

function navigateToCreate() {
    showResumePrompt.value = false
    router.push({ name: 'EquipmentCreate', query: { companyId: props.companyId } })
}

function goToDetail(equipo) {
    router.push({ name: 'EquipmentDetail', params: { id: equipo.Id } })
}

function getDraftDate(key) {
    try {
        const parts = key.split('_')
        if (parts.length >= 3) {
            const timestamp = parseInt(parts[2])
            if (!isNaN(timestamp)) {
                const date = new Date(timestamp)
                return `${date.toLocaleDateString()} ${date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
            }
        }
        return 'Sin fecha'
    } catch (e) {
        return 'Sin fecha'
    }
}

onMounted(() => {
    loadEquipos()
    loadDrafts()
})
</script>

<template>
  <div class="h-100">
    <!-- Toolbar -->
    <v-row class="mb-6 align-center" :class="{ 'gap-4': isMobileApp }">
        <!-- Search Field (Always First) -->
        <v-col cols="12" md="6" :class="{ 'pa-0': isMobileApp }">
            <v-text-field
                v-model="search"
                prepend-inner-icon="mdi-magnify"
                label="Buscar equipo"
                placeholder="Código, Serial, Usuario..."
                variant="solo-filled"
                flat
                density="comfortable"
                hide-details
                bg-color="white"
                class="search-field rounded-xl elevation-1"
                clearable
            ></v-text-field>
        </v-col>

        <!-- Actions -->
        <v-col cols="12" md="6" class="d-flex" :class="isMobileApp ? 'justify-space-between gap-2 pa-0 text-truncate px-1' : 'justify-end gap-3'">
            <!-- Drafts Button -->
            <v-btn 
                color="white" 
                variant="flat" 
                class="text-capitalize rounded-lg border-thin" 
                height="44"
                :class="{ 'flex-grow-1 px-2': isMobileApp, 'mr-2': !isMobileApp }"
                @click="openDrafts"
                :min-width="isMobileApp ? '44' : 'auto'"
            >
                <v-icon :start="!isMobileApp">mdi-file-document-edit-outline</v-icon>
                <span v-if="!isMobileApp">Borradores</span>
                <v-badge
                    v-if="drafts.length > 0"
                    :content="drafts.length"
                    color="error"
                    inline
                    class="ml-2"
                ></v-badge>
            </v-btn>

            <!-- Create Button -->
            <v-btn 
                color="primary" 
                class="text-white text-capitalize rounded-lg" 
                height="44"
                elevation="2"
                @click="handleNewEquipmentClick"
                :class="{ 'flex-grow-1 ml-auto': isMobileApp }"
                :min-width="isMobileApp ? '120' : 'auto'"
            >
                <v-icon start>mdi-plus</v-icon>
                <span class="d-none d-sm-inline">Nuevo Equipo</span>
                <span class="d-inline d-sm-none">Nuevo</span>
            </v-btn>
        </v-col>
    </v-row>

    <!-- Loading -->
    <div v-if="loading" class="d-flex justify-center align-center py-12">
        <v-progress-circular indeterminate color="corporate-blue" size="64" width="6"></v-progress-circular>
    </div>

    <!-- Empty State -->
    <div v-else-if="filteredEquipos.length === 0" class="d-flex flex-column align-center justify-center py-16 text-center animate-fade-in">
        <div class="bg-grey-lighten-4 rounded-circle pa-6 mb-4">
            <v-icon size="48" color="grey-lighten-1">mdi-laptop-off</v-icon>
        </div>
        <h3 class="text-h6 text-grey-darken-3 font-weight-bold mb-1">No se encontraron equipos</h3>
        <p class="text-body-2 text-grey">No hay equipos registrados para esta empresa o búsqueda.</p>
    </div>

    <!-- Gallery -->
    <v-row v-else class="match-height">
        <v-col cols="12" sm="6" md="4" lg="3" v-for="equipo in filteredEquipos" :key="equipo.Id">
            <v-card 
                hover 
                @click="goToDetail(equipo)"
                class="equipment-card border-0 elevation-0 h-100 rounded-xl d-flex flex-column group"
                :class="{ 'mobile-card': isMobileApp }"
            >
                <!-- Status Badge -->
                <div class="position-absolute top-0 right-0 mt-4 mr-4 z-10">
                     <v-chip 
                        size="x-small" 
                        color="emerald" 
                        class="bg-green-lighten-5 text-green-darken-2 font-weight-bold border-0" 
                        variant="flat"
                    >
                        Activo
                    </v-chip>
                </div>

                <v-card-text class="pa-5 d-flex flex-column h-100 position-relative">
                    <!-- Icon & Title -->
                    <div class="d-flex align-start gap-4 mb-4">
                        <div 
                            class="rounded-xl bg-indigo-lighten-5 text-indigo-darken-1 d-flex align-center justify-center flex-shrink-0"
                            style="width: 56px; height: 56px;"
                        >
                            <v-icon size="32">mdi-laptop</v-icon>
                        </div>
                        <div class="pt-1 pr-12">
                            <h3 class="text-subtitle-1 font-weight-bold text-grey-darken-3 line-height-tight mb-1 clamp-2">
                                {{ equipo.Modelo || 'Sin Modelo' }}
                            </h3>
                            <div class="text-caption text-grey font-weight-medium d-flex align-center gap-1">
                                <v-icon size="12">mdi-barcode</v-icon>
                                {{ equipo.Serial || 'S/N' }}
                            </div>
                        </div>
                    </div>

                    <!-- Details -->
                    <div class="mb-auto">
                        <div class="d-flex align-center gap-2 mb-2 bg-grey-lighten-5 pa-2 rounded-lg">
                            <v-icon size="16" color="grey-darken-1">mdi-identifier</v-icon>
                            <span class="text-caption font-weight-medium text-grey-darken-2">{{ equipo.CodigoEquipo }}</span>
                        </div>
                        <div class="d-flex align-center gap-2 px-2">
                            <v-icon size="16" color="grey-lighten-1">mdi-account</v-icon>
                            <span class="text-caption text-grey-darken-1">{{ equipo.UsuarioNombre || 'Sin Asignar' }}</span>
                        </div>
                    </div>

                    <v-divider class="my-4 border-dashed"></v-divider>

                    <!-- Action -->
                    <div class="d-flex align-center justify-space-between text-corporate-blue group-hover:text-primary transition-colors">
                        <span class="text-caption font-weight-bold text-uppercase tracking-wide">Ver Detalles</span>
                        <v-btn icon variant="text" density="compact" size="small" class="ml-2">
                            <v-icon class="transform group-hover:translate-x-1 transition-transform">mdi-arrow-right</v-icon>
                        </v-btn>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>

    <!-- Drafts Dialog -->
    <v-dialog 
        v-model="showDraftsDialog" 
        :max-width="isMobileApp ? '100%' : '500'"
        :fullscreen="isMobileApp"
        :transition="isMobileApp ? 'dialog-bottom-transition' : 'scale-transition'"
    >
        <v-card :class="['d-flex flex-column', isMobileApp ? 'rounded-0' : 'rounded-xl']">
            <v-card-title class="pa-4 d-flex align-center justify-space-between border-b bg-white position-sticky top-0 z-10">
                <span class="text-h6 font-weight-bold">Borradores Guardados</span>
                <v-btn icon="mdi-close" variant="text" density="comfortable" @click="showDraftsDialog = false"></v-btn>
            </v-card-title>
            <v-card-text class="pa-0 flex-grow-1 overflow-y-auto">
                <v-list lines="two" class="pa-2">
                    <v-list-item
                        v-for="draft in drafts"
                        :key="draft.key"
                        :value="draft.key"
                        @click="openDraft(draft)"
                        class="rounded-lg mb-1"
                        color="primary"
                    >
                        <template v-slot:prepend>
                            <v-avatar color="blue-lighten-5" class="text-blue-darken-1">
                                <v-icon icon="mdi-file-document-edit-outline"></v-icon>
                            </v-avatar>
                        </template>
                        
                        <v-list-item-title class="font-weight-bold message-text">
                            {{ draft.Modelo || 'Nuevo Equipo Sin Modelo' }}
                        </v-list-item-title>
                        
                        <v-list-item-subtitle class="d-flex align-center gap-2 mt-1 flex-wrap">
                            <span v-if="draft.CodigoEquipo" class="text-caption bg-grey-lighten-4 px-2 py-0.5 rounded text-no-wrap">
                                {{ draft.CodigoEquipo }}
                            </span>
                            <span class="text-caption text-grey text-wrap">
                                {{ getDraftDate(draft.key) }}
                            </span>
                        </v-list-item-subtitle>
                        
                        <template v-slot:append>
                            <v-btn
                                icon="mdi-delete-outline"
                                variant="text"
                                color="error"
                                density="comfortable"
                                @click.stop="deleteDraft(draft)"
                            ></v-btn>
                        </template>
                    </v-list-item>
                </v-list>
            </v-card-text>
        </v-card>
    </v-dialog>

    <!-- Resume Prompt Dialog -->
    <v-dialog v-model="showResumePrompt" max-width="400">
        <v-card class="rounded-xl pa-2">
            <v-card-text class="text-center pt-6 pb-2">
                <v-avatar color="amber-lighten-5" size="64" class="mb-4">
                    <v-icon size="32" color="amber-darken-3">mdi-clipboard-text-clock-outline</v-icon>
                </v-avatar>
                <h3 class="text-h6 font-weight-bold text-grey-darken-3 mb-2">Borradores Encontrados</h3>
                <p class="text-body-2 text-grey-darken-1 mb-4">
                    Tienes {{ drafts.length }} borrador(es) pendiente(s). <br>
                    ¿Deseas continuarlos o empezar uno nuevo?
                </p>
                <div class="d-flex flex-column gap-3 mt-4">
                    <v-btn
                        block
                        color="amber-lighten-5"
                        variant="flat"
                        class="text-amber-darken-4 text-capitalize font-weight-bold rounded-lg"
                        height="48"
                        @click="showResumePrompt = false; showDraftsDialog = true"
                    >
                        <v-icon start>mdi-file-eye-outline</v-icon>
                        Ver Borradores
                    </v-btn>
                    <v-btn
                        block
                        color="primary"
                        variant="flat"
                        class="text-capitalize font-weight-bold rounded-lg"
                        height="48"
                        @click="navigateToCreate"
                    >
                        <v-icon start>mdi-plus</v-icon>
                        Crear Nuevo
                    </v-btn>
                </div>
            </v-card-text>
        </v-card>
    </v-dialog>
  </div>
</template>
