<template> 
  <router-view /> 
</template>

<style>
    /* === 1. Personalización del Scrollbar === */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f5f9;
    }

    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 5px;
        border: 2px solid #f1f5f9;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }

    /* === 2. Desbloqueo del Scroll Global === */
    
    /* Forzamos al HTML a tener scroll si es necesario */
    html {
        overflow-y: auto !important;
        overflow-x: auto !important; /* Por si acaso algo se sale a los lados */
    }
    
    /* Aseguramos que el cuerpo y la app puedan crecer infinitamente */
    body, #app, .v-application {
        min-height: 100vh !important;
        height: auto !important; /* CLAVE: Permite crecer más allá del 100% */
        overflow: visible !important;
    }
</style>