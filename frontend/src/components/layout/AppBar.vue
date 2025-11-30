<template>
  <v-app-bar color="white" elevation="1">
    <template v-slot:prepend>
      <!-- Hamburger Menu (Mobile Only) -->
      <v-btn 
        v-if="mobile" 
        icon="mdi-menu" 
        color="primary" 
        variant="text"
        class="menu-btn-creative mr-2"
        @click="$emit('toggle-drawer')"
      ></v-btn>
    </template>

    <v-app-bar-title class="text-primary font-weight-bold d-flex align-center">
        <v-icon icon="mdi-office-building" color="primary" class="mr-2" v-if="mobile"></v-icon>
        Sistema de Inventario
    </v-app-bar-title>

    <template v-slot:append>
      <v-btn icon="mdi-bell-outline" color="secondary" variant="text"></v-btn>
      <v-btn icon="mdi-help-circle-outline" color="secondary" variant="text"></v-btn>
    </template>
  </v-app-bar>
</template>

<script setup>
defineProps({
    mobile: Boolean
})

defineEmits(['toggle-drawer'])
</script>

<style scoped>
.menu-btn-creative {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.menu-btn-creative:active {
  transform: scale(0.9) rotate(-180deg);
}
</style>
