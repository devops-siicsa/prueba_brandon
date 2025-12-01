<template>
  <v-app>
    <AppDrawer 
      v-model="drawer" 
      :mobile="isMobileApp" 
    />

    <AppBar 
      :mobile="isMobileApp"
      @toggle-drawer="drawer = !drawer" 
    />
    
    <v-main class="bg-grey-lighten-4">
      <v-container fluid class="pa-6">
        
        <router-view 
          :is-mobile-device="isMobileApp"
          :is-functional-mobile="isMobileApp"
        ></router-view>

      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, watch } from 'vue'
import AppDrawer from '@/components/layout/AppDrawer.vue'
import AppBar from '@/components/layout/AppBar.vue'
import { useMobileDetection } from '@/composables/useMobileDetection'

// Usamos la nueva lógica centralizada
const { isMobileApp } = useMobileDetection()

// El drawer inicia cerrado si es móvil/tablet, abierto si es escritorio
const drawer = ref(!isMobileApp.value)

// Si cambia el tipo de dispositivo (ej: rotación o cambio de user agent simulado), ajustamos el drawer
watch(isMobileApp, (val) => {
    drawer.value = !val
})
</script>