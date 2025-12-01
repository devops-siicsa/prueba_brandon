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
            <h1 class="text-h5 text-md-h4 font-weight-bold text-primary mb-1">
                {{ companyName || 'Inventario' }}
            </h1>
            <p class="text-body-2 text-md-body-1 text-grey-darken-1">
                Gestión de equipos y activos asignados.
            </p>
        </div>

        <!-- Gallery -->
        <EquipmentGallery :is-mobile-device="isMobileDevice" :company-id="companyId" />
    </div>
  </v-container>
</template>

<script setup>
import EquipmentGallery from '@/components/Inventory/EquipmentGallery.vue'
import { useDisplay } from 'vuetify'
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const { mobile } = useDisplay()
const isMobileDevice = computed(() => mobile.value)
const route = useRoute()
const router = useRouter()

const companyId = computed(() => route.query.companyId)
const companyName = computed(() => route.query.companyName)

function goBack() {
    router.push({ name: 'InventoryHome' })
}
</script>
