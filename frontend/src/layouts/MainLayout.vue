<template>
  <v-app>
    <AppDrawer />
    <AppBar />
    
    <v-main class="bg-grey-lighten-4">
      <v-container fluid class="pa-6">
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import AppDrawer from '@/components/layout/AppDrawer.vue'
import AppBar from '@/components/layout/AppBar.vue'
</script>
