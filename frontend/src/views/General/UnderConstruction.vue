<template>
    <v-container class="fill-height d-flex flex-column align-center justify-center text-center">
        <v-icon size="120" color="grey-lighten-2" class="mb-6">mdi-cone</v-icon>
        <h1 class="text-h3 font-weight-bold text-grey-darken-2 mb-2">En Construcción</h1>
        <p class="text-h6 text-grey mb-8">Estamos trabajando en esta sección. ¡Vuelve pronto!</p>
        
        <v-btn 
            color="primary" 
            size="large" 
            prepend-icon="mdi-package-variant-closed"
            :to="{ name: 'InventoryHome' }"
        >
            Ir a Inventario
        </v-btn>
    </v-container>
</template>

<script setup>
// Placeholder view
</script>
