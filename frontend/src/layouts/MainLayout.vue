<template>
  <v-app>
    <AppDrawer 
      v-model="drawer" 
      :mobile="isVisualMobile" 
      @toggle-debug="toggleDebug"
    />

    <AppBar 
      :mobile="isVisualMobile"
      @toggle-drawer="drawer = !drawer" 
    />
    
    <v-main class="bg-grey-lighten-4">
      <v-container fluid class="pa-6">
        
        <router-view 
          :is-mobile-device="isVisualMobile"
          :is-functional-mobile="isFunctionalMobile"
        ></router-view>

      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import AppDrawer from '@/components/layout/AppDrawer.vue'
import AppBar from '@/components/layout/AppBar.vue'
import { useDisplay } from 'vuetify'

const { platform, mobile } = useDisplay()
const forceMobile = ref(null) 

// -------------------------------------------------------------
// VARIABLE 1: LÓGICA DE HARDWARE (Adaptive)
// Define: "¿Soy un teléfono real con cámara?"
// Esto controla si muestras CAMARA o EXCEL
// -------------------------------------------------------------
const isFunctionalMobile = computed(() => {
    if (forceMobile.value !== null) return forceMobile.value
    // Detecta solo el SO (Android/iOS)
    return platform.android || platform.ios
})

// -------------------------------------------------------------
// VARIABLE 2: LÓGICA VISUAL (Responsive Layout)
// Define: "¿Debo mostrar el menú hamburguesa?"
// CORRECCIÓN AQUÍ: Esto debe depender del ANCHO (mobile.value), 
// no del sistema operativo.
// -------------------------------------------------------------
const isVisualMobile = computed(() => {
    // Si la pantalla es < 1280px (o breakpoint configurado), es visualmente móvil.
    // Esto asegura que en PC con ventana pequeña, el menú se oculte.
    return mobile.value
})

const drawer = ref(!isVisualMobile.value)

// Watcher: Si la pantalla se achica (visual), el menú reacciona
watch(isVisualMobile, (val) => {
    drawer.value = !val
})

function toggleDebug() {
    if (forceMobile.value === null) {
        forceMobile.value = !isFunctionalMobile.value
    } else {
        forceMobile.value = !forceMobile.value
    }
}
</script>