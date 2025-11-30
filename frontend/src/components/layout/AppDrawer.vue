<template>
  <v-navigation-drawer
    v-model="drawer"
    :rail="!mobile"
    :permanent="!mobile"
    :temporary="mobile"
    class="modern-drawer"
    :width="mobile ? 85 : 260"
    rail-width="80"
    elevation="0"
    app
    touchless
  >
    <!-- Desktop Logo Section -->
    <div v-if="!mobile" class="drawer-header d-flex align-center justify-center py-6">
      <div class="logo-box">
        <v-icon color="#00A08F" size="32">mdi-office-building</v-icon>
      </div>
    </div>

    <!-- Mobile Header: User Profile (Avatar Only) -->
    <div v-else class="mobile-header d-flex justify-center pt-8 pb-6 mb-2">
        <v-avatar size="48" class="border-2 border-white elevation-3">
            <v-img src="https://randomuser.me/api/portraits/men/85.jpg" cover></v-img>
        </v-avatar>
    </div>

    <!-- Navigation Items -->
    <div class="d-flex flex-column w-100 py-2 gap-2" :class="mobile ? 'align-center' : 'align-center'">
      <template v-for="(item, i) in menuItems" :key="i">
        
        <!-- Single Item -->
        <v-tooltip 
          v-if="!item.children"
          :text="item.title" 
          location="end" 
          offset="10"
          :disabled="false"
        >
          <template v-slot:activator="{ props }">
            <div 
              v-bind="props"
              class="nav-item-wrapper"
              :class="{ 'active': isActive(item.to), 'mobile-item': mobile }"
              @click="navigate(item.to)"
            >
              <div class="icon-container" :class="{ 'active-icon': isActive(item.to) }">
                  <v-icon :icon="item.icon" :size="mobile ? 24 : 24" :color="isActive(item.to) ? '#00A08F' : (mobile ? 'grey-lighten-1' : 'grey-lighten-1')"></v-icon>
              </div>
              <!-- Text Hidden on Mobile Rail -->
            </div>
          </template>
        </v-tooltip>

        <!-- Group Item -->
        <div v-else class="w-100 d-flex flex-column align-center">
            <!-- Menu Popover (Both Desktop and Mobile Rail) -->
            <v-menu location="end" offset="10" open-on-hover open-delay="0" close-delay="100">
                <template v-slot:activator="{ props }">
                    <div 
                        v-bind="props"
                        class="nav-item-wrapper"
                        :class="{ 'active': isGroupActive(item), 'mobile-item': mobile }"
                    >
                        <div class="icon-container" :class="{ 'active-icon': isGroupActive(item) }">
                            <v-icon :icon="item.icon" size="24" :color="isGroupActive(item) ? '#00A08F' : 'grey-lighten-1'"></v-icon>
                        </div>
                    </div>
                </template>
                <v-card min-width="220" color="#1e293b" class="py-2 border-thin border-opacity-25 border-white elevation-4 rounded-lg">
                    <div class="px-4 py-2 text-caption font-weight-bold text-grey text-uppercase">{{ item.title }}</div>
                    <v-list density="compact" bg-color="transparent">
                        <v-list-item
                            v-for="(child, j) in filterChildren(item.children)"
                            :key="j"
                            :to="child.to"
                            color="#00A08F"
                            class="rounded-lg mx-2 mb-1"
                        >
                            <template v-slot:prepend>
                                <v-icon :icon="child.icon" size="small" class="mr-2"></v-icon>
                            </template>
                            <v-list-item-title class="text-body-2">{{ child.title }}</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-menu>
        </div>

      </template>
    </div>

    <!-- Footer -->
    <template v-slot:append>
      <div class="d-flex flex-column align-center pb-8 gap-4">
        
        <!-- Logout Icon Only -->
        <v-tooltip text="Cerrar Sesión" location="end" offset="10">
            <template v-slot:activator="{ props }">
                <div v-bind="props" class="nav-item-wrapper logout-btn" @click="logout">
                    <v-icon icon="mdi-logout" size="24" color="error"></v-icon>
                </div>
            </template>
        </v-tooltip>

      </div>
    </template>
  </v-navigation-drawer>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter, useRoute } from 'vue-router'
import { useMenu } from '@/composables/useMenu'

const props = defineProps({
    modelValue: Boolean,
    mobile: Boolean
})

const emit = defineEmits(['update:modelValue'])

const drawer = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()
const { menuItems, filterChildren } = useMenu()

function isActive(path) {
    return route.path === path
}

function isGroupActive(item) {
    if (!item.children) return false
    return item.children.some(child => route.path === child.to)
}

function navigate(path) {
    router.push(path)
}

function logout() {
    authStore.logout()
    router.push('/login')
}
</script>

<style scoped>
.modern-drawer:not(.v-navigation-drawer--temporary) {
  background-color: #0f172a !important; /* Slate 900 - Darker, modern */
  border-right: 1px solid rgba(255, 255, 255, 0.05);
  z-index: 1005 !important; /* Ensure it stays above standard content but below high-priority modals if needed */
  height: 100vh !important;
  position: fixed !important;
  top: 0 !important;
  bottom: 0 !important;
}

.modern-drawer.v-navigation-drawer--temporary {
  background-color: #0f172a !important;
  z-index: 2000 !important; /* Higher z-index for mobile overlay */
  position: fixed !important;
  top: 0 !important;
  bottom: 0 !important;
  height: auto !important; /* Allow browser to determine height based on top/bottom */
}

/* Logo Box */
.logo-box {
  width: 56px;
  height: 56px;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

.gap-2 { gap: 12px; }
.gap-4 { gap: 16px; }

/* Nav Item Wrapper */
.nav-item-wrapper {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    position: relative;
    color: #94a3b8;
}

/* Mobile Item Styling */
.nav-item-wrapper.mobile-item {
    width: 100%;
    height: 64px; /* Taller for touch */
    justify-content: flex-start;
    padding: 0 16px;
    background-color: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.03);
    margin-bottom: 8px;
    border-radius: 16px;
}

.nav-item-wrapper.mobile-item:active {
    transform: scale(0.98);
}

.nav-item-wrapper.mobile-item.active {
    background: linear-gradient(90deg, rgba(0, 160, 143, 0.15) 0%, rgba(0, 160, 143, 0.05) 100%);
    border: 1px solid rgba(0, 160, 143, 0.3);
}

/* Icon Container */
.icon-container {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(255, 255, 255, 0.05);
    transition: all 0.2s;
}

.nav-item-wrapper.active .icon-container.active-icon {
    background-color: #00A08F;
    box-shadow: 0 4px 10px rgba(0, 160, 143, 0.4);
}

.nav-item-wrapper.active .icon-container.active-icon .v-icon {
    color: white !important;
}

/* Desktop Hover */
.nav-item-wrapper:not(.mobile-item):hover {
    background-color: rgba(255, 255, 255, 0.05);
    color: #f8fafc;
}

.nav-item-wrapper:not(.mobile-item).active {
    background-color: rgba(0, 160, 143, 0.15);
    color: #00A08F;
}

/* Desktop Active Indicator */
.nav-item-wrapper:not(.mobile-item).active::before {
    content: '';
    position: absolute;
    left: -12px;
    top: 50%;
    transform: translateY(-50%);
    width: 4px;
    height: 24px;
    background-color: #00A08F;
    border-radius: 0 4px 4px 0;
    opacity: 1;
}

/* Logout Button */
.logout-btn:hover {
    background-color: rgba(239, 68, 68, 0.1) !important;
}

/* Mobile Subitems */
.border-white-opacity {
    border-color: rgba(255, 255, 255, 0.1) !important;
}

.mobile-subitem:hover {
    background-color: rgba(255, 255, 255, 0.03);
}

.mobile-subitem.active-sub {
    background-color: rgba(0, 160, 143, 0.1);
}

/* Scrollbar */
:deep(.v-navigation-drawer__content::-webkit-scrollbar) {
  width: 0px;
  background: transparent;
}
</style>
