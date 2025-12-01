<template>
  <v-container fluid class="bg-grey-lighten-5 fill-height align-start">
    <div class="w-100">
        <!-- Header -->
        <div class="mb-8">
            <div class="text-caption text-grey mb-1">
                <v-icon size="small" class="mr-1">mdi-home</v-icon> / Configuración / Clientes
            </div>
            <h1 class="text-h4 font-weight-bold text-primary mb-1">
                Gestión de Clientes
            </h1>
            <p class="text-body-1 text-grey-darken-1">
                Administra el directorio de clientes, sus sedes y contactos.
            </p>
        </div>

        <!-- SECCIÓN: DIRECTORIO DE CLIENTES -->
        <div class="mb-8">
            <div class="d-flex align-center mb-4">
                <v-icon color="primary" class="mr-2">mdi-account-group</v-icon>
                <h2 class="text-h6 font-weight-bold text-grey-darken-3">Directorio</h2>
            </div>
            
            <v-row>
                <v-col cols="12" sm="6" md="3" lg="2" v-for="item in clientItems" :key="item.title">
                    <v-card 
                        class="config-card border-0 elevation-1"
                        height="120"
                        @click="openSection(item)"
                        v-ripple
                    >
                        <div class="card-corner-decoration" :class="`bg-${item.color}-lighten-5`">
                            <v-icon size="small" :color="item.color">mdi-chevron-right</v-icon>
                        </div>
                        
                        <v-card-text class="pa-3 d-flex flex-column justify-space-between h-100">
                            <div class="icon-box" :class="`bg-${item.color}-lighten-5`">
                                <v-icon size="24" :color="item.color">{{ item.icon }}</v-icon>
                            </div>
                            
                            <div>
                                <div class="text-subtitle-2 font-weight-bold text-grey-darken-3 mb-0 line-height-tight">
                                    {{ item.title }}
                                </div>
                                <div class="text-caption text-grey" style="font-size: 0.7rem !important;">Administrar</div>
                            </div>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </div>
    </div>

    <!-- DIÁLOGOS -->
    <v-dialog v-model="showFeatureDialog" max-width="600">
        <v-card>
            <v-card-title>En Construcción</v-card-title>
            <v-card-text>
                La funcionalidad <strong>{{ currentFeatureName }}</strong> está siendo implementada.
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="showFeatureDialog = false">Cerrar</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <!-- Diálogo de Gestión de Contactos -->
    <v-dialog v-model="showContactsDialog" :fullscreen="isMobileApp" :max-width="isMobileApp ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <UserList 
            v-model="showContactsDialog"
            :filter-roles="['ADMINISTRADOR CLIENTE', 'SOPORTE CLIENTE', 'AUDITOR EXTERNO']"
            title="Gestión de Contactos"
            client-mode
            :is-mobile-device="isMobileApp"
        />
    </v-dialog>

    <!-- Diálogo de Gestión de Clientes -->
    <ClientList v-model="showClientsDialog" />

    <!-- Diálogo de Gestión de Sedes de Clientes -->
    <ClientSedeList v-model="showClientSedesDialog" />

  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import UserList from '@/components/Config/UserList.vue'
import ClientList from '@/components/Config/ClientList.vue'
import ClientSedeList from '@/components/Config/ClientSedeList.vue'
import { useMobileDetection } from '@/composables/useMobileDetection'

const { isMobileApp } = useMobileDetection()

const router = useRouter()

const showFeatureDialog = ref(false)
const showContactsDialog = ref(false)
const showClientsDialog = ref(false)
const showClientSedesDialog = ref(false)
const currentFeatureName = ref('')

// Items de Configuración Cliente
const clientItems = [
    { title: 'Clientes', icon: 'mdi-account-tie', action: 'clients', color: 'indigo' },
    { title: 'Sedes Clientes', icon: 'mdi-office-building-marker', action: 'client_sedes', color: 'indigo' },
    { title: 'Contactos', icon: 'mdi-card-account-details', action: 'contacts', color: 'indigo' },
]

function openSection(item) {
    if (item.action === 'contacts') {
        showContactsDialog.value = true
        return
    }
    if (item.action === 'clients') {
        showClientsDialog.value = true
        return
    }
    if (item.action === 'client_sedes') {
        showClientSedesDialog.value = true
        return
    }
    currentFeatureName.value = item.title
    showFeatureDialog.value = true
}
</script>

<style scoped>
.config-card {
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    border-radius: 12px !important;
}

.config-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.08) !important;
}

.icon-box {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}

.card-corner-decoration {
    position: absolute;
    top: 0;
    right: 0;
    width: 40px;
    height: 40px;
    border-bottom-left-radius: 40px;
    display: flex;
    align-items: flex-start;
    justify-content: flex-end;
    padding-top: 8px;
    padding-right: 8px;
    opacity: 0;
    transform: translate(10px, -10px);
    transition: all 0.3s ease;
}

.config-card:hover .card-corner-decoration {
    opacity: 1;
    transform: translate(0, 0);
    width: 50px;
    height: 50px;
    border-bottom-left-radius: 50px;
}

.line-height-tight {
    line-height: 1.1;
}
</style>
