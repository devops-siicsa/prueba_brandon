<template>
  <v-container class="fill-height justify-center bg-grey-lighten-3" fluid>
    <!-- Card centrada en Desktop, Full width en Mobile -->
    <v-card class="elevation-12 rounded-lg" :class="{'w-100 h-100 rounded-0': mobile, 'mx-auto': !mobile}" :max-width="mobile ? '100%' : 450">
      <v-toolbar color="primary" dark flat class="text-center">
        <v-toolbar-title class="font-weight-bold">Sistema de Inventario</v-toolbar-title>
      </v-toolbar>
      
      <v-card-text class="pa-6">
        <div class="text-center mb-6">
            <v-icon size="64" color="primary">mdi-shield-account</v-icon>
            <h2 class="text-h5 mt-2 text-secondary">Iniciar Sesión</h2>
        </div>

        <v-form @submit.prevent="handleLogin" ref="form">
          <!-- Campo Trifuncional -->
          <v-text-field 
            v-model="identifier"
            label="Usuario / Correo / Celular" 
            prepend-inner-icon="mdi-account" 
            variant="outlined"
            color="primary"
            class="mb-2"
            :rules="[v => !!v || 'Requerido']"
            @input="detectInputType"
            :inputmode="inputType"
          ></v-text-field>

          <v-text-field 
            v-model="password"
            label="Contraseña" 
            prepend-inner-icon="mdi-lock" 
            type="password"
            variant="outlined"
            color="primary"
            class="mb-4"
            :rules="[v => !!v || 'Requerido']"
          ></v-text-field>

          <v-alert v-if="error" type="error" variant="tonal" class="mb-4" density="compact">
            {{ error }}
          </v-alert>

          <v-btn 
            block 
            color="primary" 
            size="large" 
            type="submit" 
            :loading="loading"
            class="text-capitalize font-weight-bold"
          >
            Ingresar
          </v-btn>
          
          <div class="text-center mt-4">
            <a href="#" class="text-decoration-none text-body-2 text-primary">¿Olvidaste tu contraseña?</a>
          </div>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { useDisplay } from 'vuetify'

const { mobile } = useDisplay()
const authStore = useAuthStore()
const router = useRouter()

const identifier = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')
const inputType = ref('text')

function detectInputType() {
    // Si empieza con número, sugerir teclado numérico en móvil
    if (/^\d/.test(identifier.value)) {
        inputType.value = 'numeric'
    } else {
        inputType.value = 'text' // o 'email' si contiene @
    }
}

async function handleLogin() {
    loading.value = true
    error.value = ''
    try {
        const result = await authStore.login({
            identifier: identifier.value,
            password: password.value
        })
        
        if (result.requires_2fa) {
            // TODO: Redirigir a pantalla 2FA
            alert('Requiere 2FA (Pendiente de implementar UI)')
        } else {
            router.push('/dashboard')
        }
    } catch (err) {
        error.value = err.response?.data?.message || 'Error al iniciar sesión'
    } finally {
        loading.value = false
    }
}
</script>
