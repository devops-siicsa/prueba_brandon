<template>
  <v-container fluid class="bg-grey-lighten-5 fill-height align-start">
    <div class="w-100">
        <!-- Header -->
        <div class="mb-6 mb-md-8">
            <div class="d-flex align-center mb-1">
                <v-btn icon="mdi-arrow-left" variant="text" size="small" class="mr-2" @click="goBack"></v-btn>
                <div class="text-caption text-grey">
                    <v-icon size="small" class="mr-1">mdi-home</v-icon> / Inventario / Equipos
                </div>
            </div>
            <h1 class="text-h5 text-md-h4 font-weight-bold text-primary mb-1 d-flex align-center">
                {{ companyName || 'Inventario' }}
                <v-tooltip v-if="offlineReady" location="bottom">
                    <template v-slot:activator="{ props }">
                        <v-icon 
                            v-bind="props" 
                            icon="mdi-cloud-off-outline" 
                            color="grey-lighten-1" 
                            size="small" 
                            class="ml-2"
                        ></v-icon>
                    </template>
                    <span>Modo Offline Listo</span>
                </v-tooltip>
                <v-tooltip v-else-if="loading" location="bottom">
                    <template v-slot:activator="{ props }">
                        <v-icon 
                            v-bind="props" 
                            icon="mdi-cloud-sync" 
                            color="primary" 
                            size="small" 
                            class="ml-2"
                            style="animation: spin 2s linear infinite;"
                        ></v-icon>
                    </template>
                    <span>Descargando datos...</span>
                </v-tooltip>
            </h1>
            <p class="text-body-2 text-md-body-1 text-grey-darken-1">
                Gestión de equipos y activos asignados.
            </p>
        </div>

        <!-- Gallery -->
        <EquipmentGallery :company-id="companyId" />
    </div>
  </v-container>
</template>

<script setup>
import EquipmentGallery from '@/components/Inventory/EquipmentGallery.vue'
import { computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCatalogsStore } from '@/stores/catalogs'
import { storeToRefs } from 'pinia'

const route = useRoute()
const router = useRouter()
const catalogsStore = useCatalogsStore()
const { offlineReady, loading } = storeToRefs(catalogsStore)

const companyId = computed(() => route.query.companyId)
const companyName = computed(() => route.query.companyName)

function goBack() {
    router.push({ name: 'InventoryHome' })
}

onMounted(() => {
    // Start downloading catalogs for offline use immediately
    catalogsStore.fetchCatalogs(['estadosEquipo', 'tiposEquipo', 'fabricantes'])
})
</script>

<style>
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
</style>
