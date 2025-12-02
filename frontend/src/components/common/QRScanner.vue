<template>
  <v-dialog v-model="dialog" fullscreen transition="dialog-bottom-transition" persistent>
    <v-card class="bg-black">
      <v-toolbar color="black" density="compact">
        <v-btn icon @click="close">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-toolbar-title>Escanear Código</v-toolbar-title>
      </v-toolbar>

      <v-card-text class="pa-0 d-flex flex-column align-center justify-center h-100 position-relative">
        <div id="reader" style="width: 100%; max-width: 600px;"></div>
        
        <div class="text-center mt-4 text-grey">
            <p>Apunta la cámara al código QR o de barras.</p>
        </div>

        <v-overlay v-model="loading" class="align-center justify-center">
            <v-progress-circular indeterminate color="primary"></v-progress-circular>
        </v-overlay>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, watch, onBeforeUnmount, nextTick } from 'vue'
import { Html5Qrcode, Html5QrcodeSupportedFormats } from "html5-qrcode"

const props = defineProps({
  modelValue: Boolean
})

const emit = defineEmits(['update:modelValue', 'scan'])

const dialog = ref(false)
const loading = ref(false)
let html5QrCode = null

watch(() => props.modelValue, (val) => {
  dialog.value = val
  if (val) {
    startScanner()
  } else {
    stopScanner()
  }
})

watch(dialog, (val) => {
  emit('update:modelValue', val)
})

async function startScanner() {
    loading.value = true
    await nextTick()
    
    // Give DOM time to render #reader
    setTimeout(async () => {
        try {
            if (!html5QrCode) {
                html5QrCode = new Html5Qrcode("reader")
            }

            const config = { 
                fps: 10, 
                qrbox: { width: 250, height: 250 },
                aspectRatio: 1.0
            }
            
            await html5QrCode.start(
                { facingMode: "environment" }, 
                config, 
                onScanSuccess, 
                onScanFailure
            )
            loading.value = false
        } catch (err) {
            console.error("Error starting scanner", err)
            loading.value = false
            alert("No se pudo iniciar la cámara. Asegúrate de dar permisos.")
            close()
        }
    }, 300)
}

function onScanSuccess(decodedText, decodedResult) {
    // Handle the scanned code as you like, for example:
    console.log(`Code matched = ${decodedText}`, decodedResult)
    emit('scan', decodedText)
    close()
}

function onScanFailure(error) {
    // handle scan failure, usually better to ignore and keep scanning.
    // console.warn(`Code scan error = ${error}`);
}

async function stopScanner() {
    if (html5QrCode && html5QrCode.isScanning) {
        try {
            await html5QrCode.stop()
            html5QrCode.clear()
        } catch (err) {
            console.error("Failed to stop scanner", err)
        }
    }
}

function close() {
    stopScanner()
    dialog.value = false
}

onBeforeUnmount(() => {
    stopScanner()
})
</script>

<style scoped>
#reader {
    border-radius: 12px;
    overflow: hidden;
    background: #000;
}
</style>
