<template>
  <v-navigation-drawer
    v-model="drawer"
    :rail="rail"
    permanent
    class="sidebar-drawer"
    width="280"
    rail-width="90"
    elevation="0"
  >
    <!-- Header: Logo -->
    <div class="drawer-header d-flex align-center pa-4" :class="rail ? 'justify-center' : 'justify-start'">
      <div class="logo-box" :class="rail ? 'mx-auto' : 'mr-3'">
        <v-icon color="#00A08F" size="28">mdi-office-building</v-icon>
      </div>
      <div v-if="!rail" class="d-flex flex-column fade-transition">
        <span class="text-h6 font-weight-bold text-white tracking-tight" style="line-height: 1;">SIICSA</span>
        <span class="text-caption text-grey-lighten-1">Inventario v2.0</span>
      </div>
    </div>

    <v-divider color="rgba(255,255,255,0.1)"></v-divider>

    <!-- Body: Navigation -->
    <v-list class="py-2" density="compact" nav>
      <template v-for="(item, i) in menuItems" :key="i">
        
        <!-- Item Simple -->
        <v-list-item
          v-if="!item.children"
          :to="item.to"
          :value="item.value"
          color="#00A08F"
          class="mb-1 rounded-lg"
          :class="{'justify-center': rail}"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon" :color="isActive(item.to) ? '#00A08F' : 'grey-lighten-1'"></v-icon>
          </template>
          <v-list-item-title v-if="!rail" class="text-body-2 font-weight-medium text-grey-lighten-1">
            {{ item.title }}
          </v-list-item-title>
          
          <!-- Tooltip en Rail Mode -->
          <v-tooltip v-if="rail" activator="parent" location="end" offset="10">
            {{ item.title }}
          </v-tooltip>
        </v-list-item>

        <!-- Item con Submenú (Dual Logic) -->
        <template v-else>
          <!-- Modo Expandido: Accordion (v-list-group) -->
          <v-list-group v-if="!rail" :value="item.group">
            <template v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
                class="mb-1 rounded-lg"
              >
                <template v-slot:prepend>
                  <v-icon :icon="item.icon" color="grey-lighten-1"></v-icon>
                </template>
                <v-list-item-title class="text-body-2 font-weight-medium text-grey-lighten-1">
                  {{ item.title }}
                </v-list-item-title>
              </v-list-item>
            </template>

            <v-list-item
              v-for="(child, j) in filterChildren(item.children)"
              :key="j"
              :to="child.to"
              :value="child.value"
              color="#00A08F"
              class="mb-1 rounded-lg pl-8"
            >
              <template v-slot:prepend>
                <v-icon :icon="child.icon" size="small" :color="isActive(child.to) ? '#00A08F' : 'grey-darken-1'"></v-icon>
              </template>
              <v-list-item-title class="text-caption font-weight-medium text-grey-lighten-2">
                {{ child.title }}
              </v-list-item-title>
            </v-list-item>
          </v-list-group>

          <!-- Modo Colapsado: Popover (v-menu) -->
          <v-menu v-else location="end" offset="10" open-on-hover open-delay="100" close-delay="100">
            <template v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
                class="mb-1 rounded-lg justify-center"
              >
                <template v-slot:prepend>
                  <v-icon :icon="item.icon" color="grey-lighten-1"></v-icon>
                </template>
              </v-list-item>
            </template>
            
            <v-card min-width="200" color="#223551" class="border-thin border-opacity-25 border-white">
              <v-list density="compact" bg-color="#223551">
                <v-list-subheader class="text-uppercase text-caption font-weight-bold text-grey">{{ item.title }}</v-list-subheader>
                <v-list-item
                  v-for="(child, j) in filterChildren(item.children)"
                  :key="j"
                  :to="child.to"
                  :value="child.value"
                  color="#00A08F"
                  class="mb-1"
                >
                  <template v-slot:prepend>
                    <v-icon :icon="child.icon" size="small"></v-icon>
                  </template>
                  <v-list-item-title class="text-body-2 text-grey-lighten-1">{{ child.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-menu>
        </template>

      </template>
    </v-list>

    <!-- Footer: Profile & Toggle -->
    <template v-slot:append>
      <div class="pa-3">
        <!-- Botón Toggle (Visible siempre, cambia icono) -->
        <div class="d-flex justify-end mb-2" v-if="!rail">
           <v-btn icon="mdi-chevron-left" variant="text" color="grey" density="compact" @click="toggleRail"></v-btn>
        </div>
        <div class="d-flex justify-center mb-2" v-else>
           <v-btn icon="mdi-chevron-right" variant="text" color="grey" density="compact" @click="toggleRail"></v-btn>
        </div>

        <!-- Tarjeta de Perfil -->
        <v-card color="rgba(255,255,255,0.05)" class="rounded-lg elevation-0" :class="rail ? 'pa-1' : 'pa-3'">
            <div class="d-flex align-center" :class="rail ? 'justify-center flex-column' : ''">
                <v-avatar :size="rail ? 32 : 40" class="cursor-pointer border-sm border-opacity-25 border-white">
                    <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
                </v-avatar>
                
                <div v-if="!rail" class="ml-3 overflow-hidden" style="flex: 1;">
                    <div class="text-subtitle-2 font-weight-bold text-white text-truncate">
                        {{ authStore.userName || 'Administrador' }}
                    </div>
                    <div class="text-caption text-grey text-truncate">
                        {{ authStore.userRole || 'Sistema' }}
                    </div>
                </div>

                <v-btn 
                    v-if="!rail"
                    icon="mdi-logout" 
                    variant="text" 
                    color="error" 
                    size="small" 
                    @click="logout"
                    v-tooltip:top="'Cerrar Sesión'"
                ></v-btn>
            </div>
            <!-- Logout en modo Rail -->
             <v-btn 
                v-if="rail"
                block
                variant="text" 
                color="error" 
                size="small" 
                class="mt-2"
                @click="logout"
            >
                <v-icon>mdi-logout</v-icon>
            </v-btn>
        </v-card>
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script setup>
import { ref, computed, watch, onBeforeUnmount } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter, useRoute } from 'vue-router'

const drawer = ref(true)
const rail = ref(false) // Iniciar expandido por defecto
const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()

// Definición del Menú
const menuItems = [
  { 
    title: 'Inicio', 
    icon: 'mdi-home-outline', 
    to: '/dashboard',
    value: 'dashboard'
  },
  {
    title: 'Panel de Control',
    icon: 'mdi-cog-outline',
    group: 'panel_control',
    children: [
      { 
        title: 'Config. Sistema', 
        icon: 'mdi-tune', 
        to: '/config/system', 
        value: 'sys_config',
        permission: 'menu:view_sys_config'
      },
      { 
        title: 'Config. Cliente', 
        icon: 'mdi-account-cog-outline', 
        to: '/config/client', 
        value: 'client_config',
        permission: 'menu:view_client_config' // Asumiendo permiso, si no existe no filtra
      }
    ]
  }
]

function filterChildren(children) {
    return children.filter(child => {
        if (!child.permission) return true
        return authStore.hasPermission(child.permission)
    })
}

function isActive(path) {
    return route.path === path
}

function toggleRail() {
    rail.value = !rail.value
}

// Lógica manual para Click Outside
function handleClickOutside(event) {
    if (rail.value) return // Si ya está colapsado, no hacer nada

    // Verificar si el clic fue dentro del drawer usando la clase
    if (event.target.closest('.sidebar-drawer')) {
        return
    }

    // Si fue fuera, colapsar
    rail.value = true
}

watch(rail, (val) => {
    if (!val) {
        // Expandido: Escuchar clicks (con delay para evitar trigger inmediato)
        setTimeout(() => {
            document.addEventListener('click', handleClickOutside)
        }, 0)
    } else {
        // Colapsado: Dejar de escuchar
        document.removeEventListener('click', handleClickOutside)
    }
}, { immediate: true })

onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside)
})

function logout() {
    authStore.logout()
    router.push('/login')
}
</script>

<style scoped>
.sidebar-drawer {
  background-color: #223551 !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05);
}

.logo-box {
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.2s;
}

.tracking-tight {
  letter-spacing: -0.5px;
}

/* Custom Scrollbar */
:deep(.v-navigation-drawer__content::-webkit-scrollbar) {
  width: 4px;
}
:deep(.v-navigation-drawer__content::-webkit-scrollbar-track) {
  background: transparent;
}
:deep(.v-navigation-drawer__content::-webkit-scrollbar-thumb) {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 2px;
}

/* List Item Styles */
:deep(.v-list-item--active) {
    background: rgba(0, 160, 143, 0.15) !important;
}
:deep(.v-list-item--active .v-list-item-title) {
    color: #00A08F !important;
    font-weight: 700 !important;
}
:deep(.v-list-item--active .v-icon) {
    color: #00A08F !important;
    opacity: 1 !important;
}

/* Hover effects */
:deep(.v-list-item:hover:not(.v-list-item--active)) {
    background: rgba(255, 255, 255, 0.03);
}

/* Fix Icon Centering in Rail Mode */
:deep(.v-navigation-drawer--rail .v-list-item__prepend) {
    margin-inline-end: 0 !important;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}
:deep(.v-navigation-drawer--rail .v-list-item__content) {
    display: none !important;
}
:deep(.v-navigation-drawer--rail .v-list-item) {
    display: flex;
    justify-content: center;
    padding-inline: 0 !important;
    width: 100%;
}

.fade-transition {
    transition: opacity 0.2s ease-in-out;
}
</style>
