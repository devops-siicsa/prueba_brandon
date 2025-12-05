<template>
  <div class="h-100">
    <!-- Toolbar -->
    <v-row class="mb-6 align-center" :class="{ 'flex-column-reverse align-stretch gap-4': isMobileApp }">
        <v-col cols="12" md="6" :class="{ 'pa-0': isMobileApp }">
            <v-text-field
                v-model="search"
                prepend-inner-icon="mdi-magnify"
                label="Buscar empresa"
                placeholder="NIT o Razón Social..."
                variant="solo-filled"
                flat
                density="comfortable"
                hide-details
                bg-color="white"
                class="search-field rounded-xl elevation-1"
                clearable
            ></v-text-field>
        </v-col>
        <v-col cols="12" md="6" class="d-flex" :class="isMobileApp ? 'justify-start pa-0 mb-4 overflow-x-auto' : 'justify-end'">
             <v-chip-group 
                v-model="filterType" 
                selected-class="text-white bg-corporate-blue" 
                mandatory
                class="filter-chips"
            >
                <v-chip filter value="all" variant="elevated" class="font-weight-medium">Todos</v-chip>
                <v-chip filter value="clients" variant="elevated" class="font-weight-medium">Clientes</v-chip>
                <v-chip filter value="own" variant="elevated" class="font-weight-medium">Mis Empresas</v-chip>
            </v-chip-group>
        </v-col>
    </v-row>

    <!-- Loading -->
    <div v-if="loading" class="d-flex justify-center align-center py-12">
        <v-progress-circular indeterminate color="corporate-blue" size="64" width="6"></v-progress-circular>
    </div>

    <!-- Empty State -->
    <div v-else-if="filteredCompanies.length === 0" class="d-flex flex-column align-center justify-center py-16 text-center animate-fade-in">
        <div class="bg-grey-lighten-4 rounded-circle pa-6 mb-4">
            <v-icon size="48" color="grey-lighten-1">mdi-domain-off</v-icon>
        </div>
        <h3 class="text-h6 text-grey-darken-3 font-weight-bold mb-1">No se encontraron empresas</h3>
        <p class="text-body-2 text-grey">Intenta ajustar los filtros o la búsqueda.</p>
    </div>

    <!-- Gallery -->
    <v-row v-else class="match-height">
        <v-col cols="12" sm="6" md="4" lg="3" v-for="company in filteredCompanies" :key="company.Id">
            <v-card 
                hover 
                @click="goToInventory(company)"
                class="company-card border-0 elevation-0 h-100 rounded-xl d-flex flex-column group"
                :class="{ 'mobile-card': isMobileApp }"
            >
                <!-- Status Badge -->
                <div class="position-absolute top-0 right-0 mt-4 mr-4 z-10">
                    <v-chip 
                        size="x-small" 
                        :color="company.EsCliente ? 'teal-lighten-5' : 'blue-grey-lighten-5'" 
                        :class="company.EsCliente ? 'text-teal-darken-2' : 'text-blue-grey-darken-2'"
                        variant="flat" 
                        class="font-weight-bold text-uppercase tracking-wider border-0"
                    >
                        {{ company.EsCliente ? 'Cliente' : 'Propia' }}
                    </v-chip>
                </div>

                <v-card-text class="pa-5 d-flex flex-column h-100 position-relative">
                    <!-- Icon & Title -->
                    <div class="d-flex align-start gap-4 mb-4">
                        <div 
                            class="rounded-xl d-flex align-center justify-center flex-shrink-0 transition-colors"
                            :class="company.EsCliente ? 'bg-teal-lighten-5 text-teal-darken-1' : 'bg-blue-grey-lighten-5 text-blue-grey-darken-1'"
                            style="width: 56px; height: 56px;"
                        >
                            <v-icon size="32">{{ company.EsCliente ? 'mdi-account-tie' : 'mdi-domain' }}</v-icon>
                        </div>
                        <div class="pt-1 pr-12">
                            <h3 class="text-subtitle-1 font-weight-bold text-grey-darken-3 line-height-tight mb-1 clamp-2">
                                {{ company.RazonSocial }}
                            </h3>
                            <div class="text-caption text-grey font-weight-medium d-flex align-center gap-1">
                                <v-icon size="12">mdi-identifier</v-icon>
                                {{ company.NIT }}
                            </div>
                        </div>
                    </div>

                    <v-divider class="mt-auto mb-4 border-dashed"></v-divider>

                    <!-- Action -->
                    <div class="d-flex align-center justify-space-between text-corporate-blue group-hover:text-primary transition-colors">
                        <span class="text-caption font-weight-bold text-uppercase tracking-wide">Gestionar Inventario</span>
                        <v-btn icon variant="text" density="compact" size="small" class="ml-2">
                            <v-icon class="transform group-hover:translate-x-1 transition-transform">mdi-arrow-right</v-icon>
                        </v-btn>
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

import { useMobileDetection } from '@/composables/useMobileDetection'

const { isMobileApp } = useMobileDetection()

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
.gap-4 { gap: 16px; }
.gap-1 { gap: 4px; }

.search-field :deep(.v-field) {
    border-radius: 16px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
}

.company-card {
    background: white;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    border: 1px solid rgba(0,0,0,0.03) !important;
}

.company-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.08) !important;
    border-color: rgba(0,0,0,0.05) !important;
}

.company-card.mobile-card:active {
    transform: scale(0.98);
}

.line-height-tight {
    line-height: 1.3;
}

.clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.border-dashed {
    border-style: dashed !important;
    opacity: 0.15;
}

/* Animations */
.animate-fade-in {
    animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.group:hover .group-hover\:text-primary {
    color: #00A08F !important; /* Corporate Primary */
}

.transform { transition: transform 0.2s; }
.group:hover .translate-x-1 {
    transform: translateX(4px);
}

.z-10 { z-index: 10; }
</style>
