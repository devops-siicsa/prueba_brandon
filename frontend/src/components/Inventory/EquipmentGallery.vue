<template>
  <div class="h-100">
    <!-- Toolbar -->
    <v-row class="mb-6 align-center">
        <v-col cols="12" md="6">
            <v-text-field
                v-model="search"
                prepend-inner-icon="mdi-magnify"
                label="Buscar equipo..."
                placeholder="Código, Serial, Usuario..."
                variant="outlined"
                density="comfortable"
                hide-details
                bg-color="white"
                class="rounded-lg elevation-1"
            ></v-text-field>
        </v-col>
        <v-col cols="12" md="6" class="d-flex justify-end gap-2">
            <v-btn 
                color="white" 
                variant="flat" 
                class="text-capitalize rounded-lg border" 
                height="44"
                prepend-icon="mdi-filter-variant"
            >
                Filtros
            </v-btn>
            <v-btn 
                color="#1e293b" 
                class="text-white text-capitalize rounded-lg" 
                height="44"
                prepend-icon="mdi-plus" 
                elevation="2"
                @click="goToCreate"
            >
                Nuevo Equipo
            </v-btn>
        </v-col>
    </v-row>

    <!-- Loading -->
    <div v-if="loading" class="d-flex justify-center align-center py-12">
        <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
    </div>

    <!-- Empty State -->
    <div v-else-if="filteredEquipos.length === 0" class="d-flex flex-column align-center justify-center py-12 text-center">
        <v-icon size="64" color="grey-lighten-2" class="mb-4">mdi-laptop-off</v-icon>
        <h3 class="text-h6 text-grey-darken-2">No se encontraron equipos</h3>
        <p class="text-body-2 text-grey">No hay equipos registrados para esta empresa o búsqueda.</p>
    </div>

    <!-- Gallery -->
    <v-row v-else>
        <v-col cols="12" sm="6" md="4" lg="3" v-for="equipo in filteredEquipos" :key="equipo.Id">
            <v-card 
                hover 
                @click="goToDetail(equipo)"
                class="equipment-card border-0 elevation-2 h-100 rounded-lg"
            >
                <div class="card-top-accent bg-indigo"></div>
                
                <v-card-text class="pa-4 d-flex flex-column h-100">
                    <div class="d-flex justify-space-between align-start mb-3">
                        <v-avatar 
                            color="indigo-lighten-5" 
                            size="48" 
                            class="rounded-lg"
                        >
                            <v-icon color="indigo-darken-1" size="28">mdi-laptop</v-icon>
                        </v-avatar>
                        <v-chip size="x-small" color="grey-lighten-3" class="font-weight-bold text-grey-darken-2">
                            {{ equipo.CodigoEquipo }}
                        </v-chip>
                    </div>

                    <div class="mb-auto">
                        <h3 class="text-subtitle-1 font-weight-bold text-grey-darken-3 line-height-tight mb-1 text-truncate">
                            {{ equipo.Modelo || 'Sin Modelo' }}
                        </h3>
                        <div class="text-caption text-grey-darken-1 font-weight-medium mb-1 d-flex align-center">
                            <v-icon size="small" start class="mr-1">mdi-barcode</v-icon>
                            {{ equipo.Serial || 'S/N' }}
                        </div>
                         <div class="text-caption text-grey d-flex align-center">
                            <v-icon size="small" start class="mr-1">mdi-account</v-icon>
                            {{ equipo.UsuarioNombre || 'Sin Asignar' }}
                        </div>
                    </div>

                    <v-divider class="my-3 border-opacity-50"></v-divider>

                    <div class="d-flex align-center justify-space-between">
                        <v-chip size="x-small" color="emerald" class="bg-green-lighten-5 text-green-darken-1 font-weight-bold" variant="flat">
                            Activo
                        </v-chip>
                        <v-btn size="small" variant="text" color="primary" icon="mdi-chevron-right"></v-btn>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'

const props = defineProps({
    isMobileDevice: Boolean,
    companyId: [String, Number]
})

const router = useRouter()
const route = useRoute()
const equipos = ref([])
const loading = ref(false)
const search = ref('')

async function loadEquipos() {
    if (!props.companyId) return
    
    loading.value = true
    try {
        const res = await axios.get(`/api/inventory/equipos?EmpresaId=${props.companyId}`, { withCredentials: true })
        equipos.value = res.data
        // TODO: Enrich with User Name if not provided by backend directly (Backend currently returns IDs)
        // For now we display what we have. Ideally backend should return joined data or we fetch users.
    } catch (e) {
        console.error(e)
    } finally {
        loading.value = false
    }
}

const filteredEquipos = computed(() => {
    if (!search.value) return equipos.value
    const term = search.value.toLowerCase()
    return equipos.value.filter(e => 
        e.CodigoEquipo?.toLowerCase().includes(term) ||
        e.Modelo?.toLowerCase().includes(term) ||
        e.Serial?.toLowerCase().includes(term)
    )
})

function goToDetail(equipo) {
    // Navigate to detail view (to be implemented)
    console.log("Go to detail", equipo.Id)
    // router.push({ name: 'EquipmentDetail', params: { id: equipo.Id } })
}

function goToCreate() {
    console.log("Go to create")
}

watch(() => props.companyId, () => {
    loadEquipos()
})

onMounted(() => {
    loadEquipos()
})
</script>

<style scoped>
.equipment-card {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.equipment-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 20px -8px rgba(0, 0, 0, 0.15) !important;
}

.card-top-accent {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
}

.line-height-tight {
    line-height: 1.2;
}

.gap-2 {
    gap: 8px;
}
</style>
