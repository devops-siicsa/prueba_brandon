<template>
  <v-app>
    <v-main>
      <!-- Aquí se renderizarán las vistas según la ruta -->
      <router-view />
    </v-main>

    <v-snackbar
        v-model="showSyncSnackbar"
        :color="syncing ? 'info' : 'success'"
        location="top"
        timeout="-1"
    >
        <div class="d-flex align-center">
            <v-progress-circular
                v-if="syncing"
                indeterminate
                color="white"
                size="20"
                width="2"
                class="mr-3"
            ></v-progress-circular>
            <v-icon v-else icon="mdi-check-circle" class="mr-3"></v-icon>
            
            <span v-if="syncing">Sincronizando registros offline...</span>
            <span v-else>¡{{ syncCount }} registros sincronizados exitosamente!</span>
        </div>
    </v-snackbar>
  </v-app>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { syncService } from '@/services/syncService'

const syncing = ref(false)
const syncCount = ref(0)
const showSyncSnackbar = ref(false)

async function handleOnline() {
    try {
        const queue = await syncService.getQueue()
        if (queue.length > 0) {
            syncing.value = true
            showSyncSnackbar.value = true
            syncCount.value = await syncService.processQueue()
            
            // Show success message briefly
            setTimeout(() => {
                showSyncSnackbar.value = false
                syncing.value = false
            }, 3000)
        }
    } catch (e) {
        console.error('Error processing offline queue', e)
        syncing.value = false
    }
}

onMounted(() => {
    window.addEventListener('online', handleOnline)
    // Check on load too, in case we just came back online
    if (navigator.onLine) {
        handleOnline()
    }
})

onUnmounted(() => {
    window.removeEventListener('online', handleOnline)
})
</script>