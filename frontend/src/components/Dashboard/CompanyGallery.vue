<template>
  <div class="h-100">
    <!-- Toolbar -->
    <v-row class="mb-6 align-center">
        <v-col cols="12" md="6">
            <v-text-field
                v-model="search"
                prepend-inner-icon="mdi-magnify"
                label="Buscar por NIT, Razón Social..."
                placeholder="Escribe para filtrar..."
                variant="outlined"
                density="comfortable"
                hide-details
                bg-color="white"
                class="rounded-lg elevation-1"
            ></v-text-field>
        </v-col>
        <v-col cols="12" md="6" class="d-flex justify-end">
             <v-chip-group v-model="filterType" selected-class="text-primary" mandatory>
                <v-chip filter value="all" variant="outlined" class="bg-white">Todos</v-chip>
                <v-chip filter value="clients" variant="outlined" class="bg-white">Clientes</v-chip>
                <v-chip filter value="own" variant="outlined" class="bg-white">Mis Empresas</v-chip>
            </v-chip-group>
        </v-col>
    </v-row>

    <!-- Loading -->
    <div v-if="loading" class="d-flex justify-center align-center py-12">
        <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
    </div>

    <!-- Empty State -->
    <div v-else-if="filteredCompanies.length === 0" class="d-flex flex-column align-center justify-center py-12 text-center">
        <v-icon size="64" color="grey-lighten-2" class="mb-4">mdi-domain-off</v-icon>
        <h3 class="text-h6 text-grey-darken-2">No se encontraron empresas</h3>
        <p class="text-body-2 text-grey">Intenta con otros términos de búsqueda.</p>
    </div>

    <!-- Gallery -->
    <v-row v-else>
        <v-col cols="12" sm="6" md="4" lg="3" v-for="company in filteredCompanies" :key="company.Id">
            <v-card 
                hover 
                @click="goToInventory(company)"
                class="company-card border-0 elevation-2 h-100 rounded-lg"
            >
                <div class="card-top-accent" :class="company.EsCliente ? 'bg-teal' : 'bg-blue-grey'"></div>
                
                <v-card-text class="pa-4 d-flex flex-column h-100">
                    <div class="d-flex justify-space-between align-start mb-3">
                        <v-avatar 
                            :color="company.EsCliente ? 'teal-lighten-5' : 'blue-grey-lighten-5'" 
                            size="48" 
                            class="rounded-lg"
                        >
                            <v-icon :color="company.EsCliente ? 'teal-darken-1' : 'blue-grey-darken-1'" size="28">
                                {{ company.EsCliente ? 'mdi-account-tie' : 'mdi-domain' }}
                            </v-icon>
                        </v-avatar>
                        <v-chip size="x-small" :color="company.EsCliente ? 'teal' : 'blue-grey'" variant="flat" class="font-weight-bold">
                            {{ company.EsCliente ? 'CLIENTE' : 'PROPIA' }}
                        </v-chip>
                    </div>

                    <div class="mb-auto">
                        <h3 class="text-subtitle-1 font-weight-bold text-grey-darken-3 line-height-tight mb-1">
                            {{ company.RazonSocial }}
                        </h3>
                        <div class="text-caption text-grey-darken-1 font-weight-medium mb-3">
                            NIT: {{ company.NIT }}
                        </div>
                    </div>

                    <v-divider class="my-3 border-opacity-50"></v-divider>

                    <div class="d-flex align-center justify-space-between">
                        <span class="text-caption text-grey">Ir a Inventario</span>
                        <v-icon size="small" color="primary">mdi-arrow-right</v-icon>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const props = defineProps({
    isMobileDevice: Boolean
})

const router = useRouter()
const companies = ref([])
const loading = ref(false)
const search = ref('')
const filterType = ref('all')

async function loadCompanies() {
    loading.value = true
    try {
        const res = await axios.get('/api/config/companies', { withCredentials: true })
        companies.value = res.data
    } catch (e) {
        console.error(e)
    } finally {
        loading.value = false
    }
}

const filteredCompanies = computed(() => {
    return companies.value.filter(c => {
        // Filter by Type
        if (filterType.value === 'clients' && !c.EsCliente) return false
        if (filterType.value === 'own' && c.EsCliente) return false
        
        // Filter by Search
        const term = search.value.toLowerCase()
        const matches = (
            c.RazonSocial?.toLowerCase().includes(term) || 
            c.NIT?.includes(term)
        )
        
        return matches && c.Activo
    })
})

function goToInventory(company) {
    localStorage.setItem('selectedCompanyId', company.Id)
    router.push({ 
        name: 'InventoryList', 
        query: { 
            companyId: company.Id,
            companyName: company.RazonSocial 
        } 
    })
}

onMounted(() => {
    loadCompanies()
})
</script>

<style scoped>
.company-card {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.company-card:hover {
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
</style>
