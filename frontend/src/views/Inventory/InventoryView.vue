<template>
  <v-container>
    <h2 class="mb-4">
      {{ isFunctionalMobile ? 'Escaneo Rápido (Móvil)' : 'Gestión de Inventario (Escritorio)' }}
    </h2>

    <v-card class="pa-5" elevation="2">
      
      <div v-if="isFunctionalMobile" class="text-center">
        <v-icon size="64" color="primary" class="mb-3">mdi-barcode-scan</v-icon>
        <p class="text-body-1 mb-4">Apunta la cámara al código de barras del equipo.</p>
        
        <v-btn 
          color="primary" 
          size="x-large" 
          block 
          @click="activarCamara"
        >
          Abrir Cámara
        </v-btn>
      </div>

      <div v-else>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field 
              label="Ingresar Serial Manualmente" 
              prepend-inner-icon="mdi-keyboard"
              variant="outlined"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-file-input 
              label="Carga Masiva (Excel)" 
              prepend-icon="mdi-microsoft-excel"
              variant="outlined"
              @change="cargarExcel"
            ></v-file-input>
          </v-col>
        </v-row>
        
        <div class="d-flex justify-end mt-4">
          <v-btn color="secondary" variant="text" class="mr-2">Cancelar</v-btn>
          <v-btn color="success" @click="guardarManual">Guardar Registro</v-btn>
        </div>
      </div>

    </v-card>
    


  </v-container>
</template>

<script setup>
// Recibimos la señal limpia desde el MainLayout
const props = defineProps({
  isFunctionalMobile: Boolean
})

// --- Métodos simulados ---

const activarCamara = () => {
  console.log("Lógica de cámara nativa activada...")
  // Aquí iría tu código para leer el QR/Barcode
}

const cargarExcel = () => {
  console.log("Abriendo explorador de archivos...")
}

const guardarManual = () => {
  console.log("Enviando formulario JSON a Flask...")
}
</script>
