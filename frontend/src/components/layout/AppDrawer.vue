<template>
  <v-navigation-drawer v-model="drawer" :rail="rail" permanent @click="rail = false" color="primary" theme="dark">
    <v-list-item
      prepend-avatar="https://randomuser.me/api/portraits/men/85.jpg"
      :title="authStore.userName || 'Usuario'"
      nav
    >
      <template v-slot:append>
        <v-btn variant="text" icon="mdi-chevron-left" @click.stop="rail = !rail"></v-btn>
      </template>
    </v-list-item>

    <v-divider></v-divider>

    <v-list density="compact" nav>
      <!-- Pantalla Principal -->
      <v-list-item prepend-icon="mdi-home" title="Inicio" value="dashboard" to="/dashboard"></v-list-item>
      
      <v-divider class="my-2"></v-divider>

      <!-- Grupo Panel de Control -->
      <v-list-group value="panel_control">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            prepend-icon="mdi-cog-box"
            title="Panel de Control"
          ></v-list-item>
        </template>

        <v-list-item
          prepend-icon="mdi-cogs"
          title="Config. Sistema"
          value="sys_config"
          to="/config/system"
          v-permission="'menu:view_sys_config'"
        ></v-list-item>

        <v-list-item
          prepend-icon="mdi-account-cog"
          title="Config. Cliente"
          value="client_config"
          to="/config/client"
        ></v-list-item>
      </v-list-group>

    </v-list>
    
    <template v-slot:append>
        <div class="pa-2">
            <v-btn block color="error" prepend-icon="mdi-logout" v-if="!rail" @click="logout">
                Cerrar Sesión
            </v-btn>
            <v-btn icon="mdi-logout" color="error" variant="text" v-else @click="logout"></v-btn>
        </div>
    </template>
  </v-navigation-drawer>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const drawer = ref(true)
const rail = ref(false)
const authStore = useAuthStore()
const router = useRouter()

function logout() {
    authStore.logout()
    router.push('/login')
}
</script>
