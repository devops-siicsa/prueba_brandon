<template>
  <v-app>
    <v-main class="d-flex align-center justify-center bg-primary">
      <v-container fluid class="fill-height pa-0">
        <v-row no-gutters class="fill-height justify-center align-center">
            <v-col cols="12" sm="8" md="4" lg="3">
                <router-view></router-view>
            </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
// Layout simple para login
</script>
