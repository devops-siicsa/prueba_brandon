<template>
  <v-container fluid class="fill-height pa-0">
    <v-row no-gutters class="fill-height">
      <!-- Panel Izquierdo (Información) -->
      <v-col cols="12" md="6" class="d-none d-md-flex flex-column justify-space-between pa-12 left-panel position-relative">
        <!-- Imagen de Fondo -->
        <div class="bg-image"></div>
        <!-- Overlay Gradiente -->
        <div class="bg-overlay"></div>

        <!-- Contenido (z-index 10) -->
        <div class="d-flex flex-column justify-space-between fill-height position-relative" style="z-index: 10;">
          <!-- Logo -->
          <div class="d-flex align-center">
            <div class="logo-box mr-3">
              <v-icon color="white" size="32">mdi-office-building</v-icon>
            </div>
            <span class="text-h4 font-weight-bold text-white tracking-tight">SIICSA</span>
          </div>

          <!-- Texto Central -->
          <div>
            <h1 class="text-h3 font-weight-black text-white mb-4" style="line-height: 1.1;">
              Gestión de Inventario<br>Inteligente.
            </h1>
            <p class="text-h6 text-white text-opacity-80 font-weight-regular" style="max-width: 480px; opacity: 0.9; line-height: 1.6;">
              Control total sobre tus activos tecnológicos, sedes y usuarios en una sola plataforma unificada.
            </p>
          </div>

          <!-- Footer -->
          <div class="text-body-2 text-white text-opacity-60" style="opacity: 0.7;">
            &copy; 2025 SIICSA S.A.S. Todos los derechos reservados.
          </div>
        </div>
      </v-col>

      <!-- Panel Derecho (Formulario) -->
      <v-col cols="12" md="6" class="bg-white d-flex align-center justify-center pa-8 sm:pa-12 lg:pa-24">
        <div class="w-100 animate-slide-in" style="max-width: 448px;">
          
          <!-- Header Formulario -->
          <div class="mb-8">
            <!-- Logo móvil -->
            <div class="d-md-none d-flex justify-center mb-6">
               <div class="pa-3 bg-blue-lighten-5 rounded-lg">
                  <v-icon color="#223551" size="32">mdi-office-building</v-icon>
               </div>
            </div>

            <h2 class="text-h4 font-weight-black text-grey-darken-4 mb-2 tracking-tight text-center text-md-left">
              Bienvenido de nuevo
            </h2>
            <p class="text-body-1 text-grey-darken-1 text-center text-md-left">
              Ingresa tus credenciales para acceder al sistema.
            </p>
          </div>

          <v-form @submit.prevent="handleLogin" ref="form" class="mt-8">
            <!-- Usuario -->
            <div class="mb-5">
              <label class="text-caption font-weight-bold text-grey-darken-3 mb-2 d-block">Correo Electrónico</label>
              <v-text-field 
                v-model="identifier"
                placeholder="nombre@empresa.com" 
                prepend-inner-icon="mdi-email-outline" 
                variant="outlined"
                color="primary"
                class="rounded-xl"
                bg-color="grey-lighten-5"
                :rules="[v => !!v || 'Requerido']"
                hide-details="auto"
                density="comfortable"
                height="56"
              ></v-text-field>
            </div>

            <!-- Contraseña -->
            <div class="mb-6">
              <div class="d-flex justify-space-between align-center mb-2">
                <label class="text-caption font-weight-bold text-grey-darken-3">Contraseña</label>
                <a href="#" class="text-caption text-primary text-decoration-none font-weight-medium hover-underline">¿Olvidaste tu contraseña?</a>
              </div>
              <v-text-field 
                v-model="password"
                placeholder="••••••••" 
                prepend-inner-icon="mdi-lock-outline" 
                :append-inner-icon="showPassword ? 'mdi-eye-off-outline' : 'mdi-eye-outline'"
                @click:append-inner="showPassword = !showPassword"
                :type="showPassword ? 'text' : 'password'"
                variant="outlined"
                color="primary"
                class="rounded-xl"
                bg-color="grey-lighten-5"
                :rules="[v => !!v || 'Requerido']"
                hide-details="auto"
                density="comfortable"
                height="56"
              ></v-text-field>
            </div>

            <v-alert v-if="error" type="error" variant="tonal" class="mb-6 rounded-lg" density="compact">
              {{ error }}
            </v-alert>

            <v-btn 
              block 
              color="#223551" 
              size="x-large" 
              type="submit" 
              :loading="loading"
              class="text-capitalize font-weight-bold rounded-xl text-white shadow-lg hover-elevate"
              elevation="0"
              height="56"
            >
              Ingresar al Sistema
              <v-icon end class="ml-2">mdi-arrow-right</v-icon>
            </v-btn>
          </v-form>
          
          <div class="mt-8">
            <div class="position-relative text-center">
              <div class="position-absolute w-100 border-t" style="top: 50%; border-color: #e5e7eb;"></div>
              <div class="position-relative d-inline-block bg-white px-2 text-caption text-grey">
                SIICSA Inventario v2.0
              </div>
            </div>
          </div>

        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const identifier = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')
const showPassword = ref(false)

async function handleLogin() {
    loading.value = true
    error.value = ''
    try {
        const result = await authStore.login({
            identifier: identifier.value,
            password: password.value
        })
        
        if (result.requires_2fa) {
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

<style scoped>
.left-panel {
  background-color: #111827; /* gray-900 fallback */
  overflow: hidden;
}

.bg-image {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2301&auto=format&fit=crop');
  background-size: cover;
  background-position: center;
  opacity: 0.5;
  transform: scale(1.05);
}

.bg-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to top right, #223551, #00A08F);
  opacity: 0.9;
}

.logo-box {
  padding: 10px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}

.tracking-tight {
  letter-spacing: -0.025em;
}

.hover-underline:hover {
  text-decoration: underline !important;
}

.hover-elevate {
  transition: all 0.2s;
}
.hover-elevate:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
}

.animate-slide-in {
  animation: slideIn 0.5s ease-out forwards;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Custom Input Styles to match Tailwind rounded-xl and padding */
:deep(.v-field--variant-outlined .v-field__outline__start) {
  border-radius: 12px 0 0 12px !important;
}
:deep(.v-field--variant-outlined .v-field__outline__end) {
  border-radius: 0 12px 12px 0 !important;
}
:deep(.v-field__input) {
  padding-top: 14px !important;
  padding-bottom: 14px !important;
}
</style>
