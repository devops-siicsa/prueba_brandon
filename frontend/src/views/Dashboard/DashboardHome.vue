<template>
  <v-container fluid class="bg-grey-lighten-5 fill-height align-start">
    <div class="w-100">
        <!-- Header -->
        <div class="mb-6 mb-md-8">
            <div class="text-caption text-grey mb-1">
                <v-icon size="small" class="mr-1">mdi-home</v-icon> / Dashboard
            </div>
            <h1 class="text-h5 text-md-h4 font-weight-bold text-primary mb-1">
                Panel Principal
            </h1>
            <p class="text-body-2 text-md-body-1 text-grey-darken-1">
                Selecciona una empresa para gestionar su inventario.
            </p>
        </div>

        <!-- Gallery -->
        <CompanyGallery :is-mobile-device="isMobileDevice" />
    </div>
  </v-container>
</template>

<script setup>
import CompanyGallery from '@/components/Dashboard/CompanyGallery.vue'
import { useDisplay } from 'vuetify'
import { computed } from 'vue'

const { mobile } = useDisplay()
const isMobileDevice = computed(() => mobile.value)
</script>