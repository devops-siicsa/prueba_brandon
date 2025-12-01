<template>
  <v-container fluid class="bg-grey-lighten-5 fill-height align-start">
    <div class="w-100">
        <!-- Header -->
        <div class="mb-6 mb-md-8">
            <div class="text-caption text-grey mb-1">
                <v-icon size="small" class="mr-1">mdi-home</v-icon> / Sistema / Configuración
            </div>
            <h1 class="text-h5 text-md-h4 font-weight-bold text-primary mb-1">
                Configuración del Sistema
            </h1>
            <p class="text-body-2 text-md-body-1 text-grey-darken-1">
                Administra los parámetros generales, usuarios y catálogos.
            </p>
        </div>

        <!-- SECCIÓN 1: EMPRESA Y USUARIOS -->
        <div class="mb-6 mb-md-8">
            <div class="d-flex align-center mb-3 mb-md-4">
                <v-icon color="primary" class="mr-2">mdi-domain</v-icon>
                <h2 class="text-subtitle-1 text-md-h6 font-weight-bold text-grey-darken-3">Empresa y Usuarios</h2>
            </div>
            
            <v-row dense>
                <v-col cols="6" sm="4" md="3" lg="2" v-for="item in companyItems" :key="item.title">
                    <v-card 
                        class="config-card border-0 elevation-1"
                        height="110"
                        @click="openSection(item)"
                        v-ripple
                    >
                        <div class="card-corner-decoration" :class="`bg-${item.color}-lighten-5`">
                            <v-icon size="small" :color="item.color">mdi-chevron-right</v-icon>
                        </div>
                        
                        <v-card-text class="pa-3 d-flex flex-column justify-space-between h-100">
                            <div class="d-flex justify-space-between align-start">
                                <div class="icon-box" :class="`bg-${item.color}-lighten-5`">
                                    <v-icon :color="item.color" size="small">{{ item.icon }}</v-icon>
                                </div>
                            </div>
                            
                            <div>
                                <div class="text-subtitle-2 font-weight-bold text-grey-darken-3 mb-0 line-height-tight text-truncate">
                                    {{ item.title }}
                                </div>
                                <div class="text-caption text-grey" style="font-size: 0.65rem !important;">Configurar</div>
                            </div>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </div>

        <!-- SECCIÓN 2: CATÁLOGOS -->
        <div class="mb-6 mb-md-8">
            <div class="d-flex align-center mb-3 mb-md-4">
                <v-icon color="teal" class="mr-2">mdi-database</v-icon>
                <h2 class="text-subtitle-1 text-md-h6 font-weight-bold text-grey-darken-3">Catálogos de Inventario</h2>
            </div>
            
            <v-row dense>
                <v-col cols="6" sm="4" md="3" lg="2" v-for="item in catalogItems" :key="item.title">
                    <v-card 
                        class="config-card border-0 elevation-1"
                        height="110"
                        @click="openSection(item)"
                        v-ripple
                    >
                        <div class="card-corner-decoration" :class="`bg-${item.color}-lighten-5`">
                            <v-icon size="small" :color="item.color">mdi-chevron-right</v-icon>
                        </div>

                        <v-card-text class="pa-3 d-flex flex-column justify-space-between h-100">
                            <div class="d-flex justify-space-between align-start">
                                <div class="icon-box" :class="`bg-${item.color}-lighten-5`">
                                    <v-icon :color="item.color" size="small">{{ item.icon }}</v-icon>
                                </div>
                            </div>
                            
                            <div>
                                <div class="text-subtitle-2 font-weight-bold text-grey-darken-3 mb-0 line-height-tight text-truncate">
                                    {{ item.title }}
                                </div>
                                <div class="text-caption text-grey" style="font-size: 0.65rem !important;">Configurar</div>
                            </div>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </div>

        <!-- SECCIÓN 3: AUDITORÍA -->
        <div class="mb-6 mb-md-8">
            <div class="d-flex align-center mb-3 mb-md-4">
                <v-icon color="orange" class="mr-2">mdi-shield-search</v-icon>
                <h2 class="text-subtitle-1 text-md-h6 font-weight-bold text-grey-darken-3">Auditoría y Seguridad</h2>
            </div>
            
            <v-row dense>
                <v-col cols="6" sm="4" md="3" lg="2">
                    <v-card 
                        class="config-card border-0 elevation-1"
                        height="110"
                        @click="openAudit"
                        v-ripple
                    >
                        <div class="card-corner-decoration bg-orange-lighten-5">
                            <v-icon size="small" color="orange">mdi-chevron-right</v-icon>
                        </div>

                        <v-card-text class="pa-3 d-flex flex-column justify-space-between h-100">
                            <div class="d-flex justify-space-between align-start">
                                <div class="icon-box bg-orange-lighten-5">
                                    <v-icon color="orange" size="small">mdi-file-eye</v-icon>
                                </div>
                            </div>
                            
                            <div>
                                <div class="text-subtitle-2 font-weight-bold text-grey-darken-3 mb-0 line-height-tight text-truncate">
                                    Log de Auditoría
                                </div>
                                <div class="text-caption text-grey" style="font-size: 0.65rem !important;">Configurar</div>
                            </div>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </div>
    </div>

    <!-- DIÁLOGOS -->
    <v-dialog v-model="showUnifiedCatalog" :fullscreen="isMobileDevice" :max-width="isMobileDevice ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <UnifiedCatalogList 
            v-model="showUnifiedCatalog" 
            :catalog-name="currentCatalogName"
            :title="currentCatalogTitle"
            :icon="currentCatalogIcon"
            :description="currentCatalogDescription"
            :is-mobile-device="isMobileDevice"
        />
    </v-dialog>

    <ProcessorConfig v-model="showProcessorConfig" :is-mobile-device="isMobileDevice" />
    <RamConfig v-model="showRamConfig" :is-mobile-device="isMobileDevice" />
    <StorageConfig v-model="showStorageConfig" :is-mobile-device="isMobileDevice" />

    <v-dialog v-model="showFeatureDialog" max-width="600">
        <v-card class="rounded-xl">
            <v-card-title class="px-6 pt-6">{{ currentFeatureName }}</v-card-title>
            <v-card-text class="px-6 py-4">
                Esta funcionalidad está en desarrollo.
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="showFeatureDialog = false">Cerrar</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <!-- PANTALLAS COMPLETAS (Listados) -->
    <v-dialog v-model="showCompanyList" :fullscreen="isMobileDevice" :max-width="isMobileDevice ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <CompanyList v-model="showCompanyList" :is-mobile-device="isMobileDevice" />
    </v-dialog>

    <v-dialog v-model="showSedeList" :fullscreen="isMobileDevice" :max-width="isMobileDevice ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <SedeList v-model="showSedeList" :is-mobile-device="isMobileDevice" />
    </v-dialog>

    <v-dialog v-model="showUserList" :fullscreen="isMobileDevice" :max-width="isMobileDevice ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <UserList v-model="showUserList" :is-mobile-device="isMobileDevice" />
    </v-dialog>

    <v-dialog v-model="showAreaList" :fullscreen="isMobileDevice" :max-width="isMobileDevice ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <AreaList v-model="showAreaList" :is-mobile-device="isMobileDevice" />
    </v-dialog>

    <v-dialog v-model="showCargoList" :fullscreen="isMobileDevice" :max-width="isMobileDevice ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <CargoList v-model="showCargoList" :is-mobile-device="isMobileDevice" />
    </v-dialog>

    <v-dialog v-model="showAuditLog" :fullscreen="isMobileDevice" :max-width="isMobileDevice ? '100%' : '1200px'" transition="dialog-bottom-transition">
        <AuditLogList v-model="showAuditLog" :is-mobile-device="isMobileDevice" />
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import CompanyList from '@/components/Config/CompanyList.vue'
import SedeList from '@/components/Config/SedeList.vue'
import UserList from '@/components/Config/UserList.vue'
import AreaList from '@/components/Config/AreaList.vue'
import CargoList from '@/components/Config/CargoList.vue'
import AuditLogList from '@/components/Config/AuditLogList.vue'
import UnifiedCatalogList from '@/components/Config/UnifiedCatalogList.vue'
import ProcessorConfig from '@/components/Config/ProcessorConfig.vue'
import RamConfig from '@/components/Config/RamConfig.vue'
import StorageConfig from '@/components/Config/StorageConfig.vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  isMobileDevice: Boolean
})

const router = useRouter()

// Estado para diálogos
const showUnifiedCatalog = ref(false)
const showProcessorConfig = ref(false)
const showRamConfig = ref(false)
const showStorageConfig = ref(false)
const currentCatalogName = ref('')
const currentCatalogTitle = ref('')
const currentCatalogIcon = ref('')
const currentCatalogDescription = ref('')

const showCompanyList = ref(false)
const showSedeList = ref(false)
const showUserList = ref(false)
const showAreaList = ref(false)
const showCargoList = ref(false)
const showAuditLog = ref(false)
const showFeatureDialog = ref(false)
const currentFeatureName = ref('')

// Items de Sección Empresa (Color base: blue-grey o primary)
const companyItems = [
    { title: 'Mis Empresas', icon: 'mdi-domain', action: 'companies', color: 'blue-grey' },
    { title: 'Mis Sedes', icon: 'mdi-map-marker', action: 'sedes', color: 'blue-grey' },
    { title: 'Mis Usuarios', icon: 'mdi-account-group', action: 'users', color: 'blue-grey' },
    { title: 'Áreas', icon: 'mdi-chart-tree', action: 'areas', description: 'Administra las dependencias y departamentos.', color: 'blue-grey' },
    { title: 'Cargos', icon: 'mdi-badge-account', action: 'cargos', description: 'Gestiona los cargos y roles laborales.', color: 'blue-grey' },
]

// Items de Catálogos (Color base: teal)
const catalogItems = [
    { title: 'Estado Equipo', icon: 'mdi-toggle-switch', action: 'catalog', catalog: 'estados_equipo', description: 'Estados posibles de un equipo (Nuevo, Usado, etc).', color: 'teal' },
    { title: 'Tipo Equipo', icon: 'mdi-laptop', action: 'catalog', catalog: 'tipos_equipo', description: 'Tipos de dispositivos (Laptop, Desktop, Móvil).', color: 'teal' },
    { title: 'Fabricantes', icon: 'mdi-factory', action: 'catalog', catalog: 'fabricantes', description: 'Marcas y fabricantes de hardware.', color: 'teal' },
    { title: 'Modelos', icon: 'mdi-devices', action: 'catalog', catalog: 'modelos', description: 'Modelos específicos de equipos.', color: 'teal' },
    { title: 'Procesadores', icon: 'mdi-cpu-64-bit', action: 'processors', description: 'Marcas, modelos y generaciones.', color: 'teal' },
    { title: 'Memoria RAM', icon: 'mdi-memory', action: 'ram', description: 'Tipos, velocidades y factores de forma.', color: 'teal' },
    { title: 'Almacenamiento', icon: 'mdi-harddisk', action: 'storage', description: 'Discos, tipos y capacidades', color: 'teal' },
    { title: 'Puertos', icon: 'mdi-serial-port', action: 'catalog', catalog: 'puertos', description: 'Tipos de puertos y conexiones.', color: 'teal' },
    { title: 'Sistema Operativo', icon: 'mdi-monitor', action: 'catalog', catalog: 'sistemas_operativos', description: 'Sistemas operativos soportados.', color: 'teal' },
    { title: 'Ofimáticas', icon: 'mdi-file-document', action: 'catalog', catalog: 'ofimaticas', description: 'Suites de ofimática y versiones.', color: 'teal' },
    { title: 'Antivirus', icon: 'mdi-shield-check', action: 'catalog', catalog: 'antivirus', description: 'Soluciones de seguridad y antivirus.', color: 'teal' },
    { title: 'Aplicaciones', icon: 'mdi-apps', action: 'catalog', catalog: 'aplicaciones', description: 'Otras aplicaciones y software corporativo.', color: 'teal' },
]

function openCatalog(item) {
    currentCatalogName.value = item.catalog
    currentCatalogTitle.value = item.title
    currentCatalogIcon.value = item.icon
    currentCatalogDescription.value = item.description || 'Gestión de catálogo del sistema.'
    showUnifiedCatalog.value = true
}

function openAudit() {
    showAuditLog.value = true
}

function openSection(item) {
    if (item.action === 'catalog') {
        openCatalog(item)
    } else if (item.action === 'companies') {
        showCompanyList.value = true
    } else if (item.action === 'sedes') {
        showSedeList.value = true
    } else if (item.action === 'users') {
        showUserList.value = true
    } else if (item.action === 'areas') {
        showAreaList.value = true
    } else if (item.action === 'cargos') {
        showCargoList.value = true
    } else if (item.action === 'processors') {
        showProcessorConfig.value = true
    } else if (item.action === 'ram') {
        showRamConfig.value = true
    } else if (item.action === 'storage') {
        showStorageConfig.value = true
    } else {
        currentFeatureName.value = item.title
        showFeatureDialog.value = true
    }
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
