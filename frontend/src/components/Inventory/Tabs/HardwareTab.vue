<template>
    <v-row>
        <!-- PROCESADOR -->
        <v-col cols="12">
            <v-card class="rounded-xl border-thin elevation-0 mb-6">
                <v-card-item class="py-4 px-6 bg-grey-lighten-5 border-b-thin">
                    <template v-slot:prepend>
                        <v-avatar color="blue-grey-lighten-5" size="40" class="mr-2">
                            <v-icon color="blue-grey-darken-1" size="24">mdi-cpu-64-bit</v-icon>
                        </v-avatar>
                    </template>
                    <v-card-title class="text-h6 font-weight-bold text-blue-grey-darken-3">
                        Procesador
                    </v-card-title>
                    <v-card-subtitle>
                        Especificaciones del CPU
                    </v-card-subtitle>
                </v-card-item>
                
                <v-card-text class="pa-6">
                    <div v-if="equipo.Procesadores && equipo.Procesadores.length > 0">
                        <v-row>
                            <v-col cols="12" md="4">
                                <v-select
                                    label="Marca"
                                    v-model="equipo.Procesadores[0].MarcaId"
                                    :items="marcasProcesador"
                                    item-title="Nombre"
                                    item-value="Id"
                                    variant="outlined"
                                    density="comfortable"
                                    color="blue-grey"
                                    bg-color="white"
                                    :readonly="!isEditing"
                                    hide-details="auto"
                                    prepend-inner-icon="mdi-label-outline"
                                    @update:model-value="onMarcaChange"
                                ></v-select>
                            </v-col>
                            <v-col cols="12" md="4">
                                <v-select
                                    label="Tipo / Familia"
                                    v-model="equipo.Procesadores[0].TipoId"
                                    :items="filteredTiposProcesador"
                                    item-title="Nombre"
                                    item-value="Id"
                                    variant="outlined"
                                    density="comfortable"
                                    color="blue-grey"
                                    bg-color="white"
                                    :readonly="!isEditing"
                                    hide-details="auto"
                                    prepend-inner-icon="mdi-chip"
                                    @update:model-value="onTipoChange"
                                    :disabled="!equipo.Procesadores[0].MarcaId"
                                ></v-select>
                            </v-col>
                            <v-col cols="12" md="4">
                                <v-select
                                    label="Generación"
                                    v-model="equipo.Procesadores[0].GeneracionId"
                                    :items="filteredGeneracionesProcesador"
                                    item-title="Nombre"
                                    item-value="Id"
                                    variant="outlined"
                                    density="comfortable"
                                    color="blue-grey"
                                    bg-color="white"
                                    :readonly="!isEditing"
                                    hide-details="auto"
                                    prepend-inner-icon="mdi-timeline-clock-outline"
                                    :disabled="!equipo.Procesadores[0].TipoId"
                                ></v-select>
                            </v-col>
                        </v-row>
                    </div>
                    <div v-else class="text-center text-grey py-4">
                        <v-icon size="large" color="grey-lighten-1" class="mb-2">mdi-cpu-64-bit-off</v-icon>
                        <div>No hay procesador asignado.</div>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>

        <!-- RAM -->
        <v-col cols="12" md="6">
            <v-card class="rounded-xl border-thin elevation-0 mb-6 h-100 d-flex flex-column">
                <v-card-item class="py-4 px-6 bg-grey-lighten-5 border-b-thin">
                    <template v-slot:prepend>
                        <v-avatar color="teal-lighten-5" size="40" class="mr-2">
                            <v-icon color="teal-darken-1" size="24">mdi-memory</v-icon>
                        </v-avatar>
                    </template>
                    <v-card-title class="text-h6 font-weight-bold text-teal-darken-3">
                        Memoria RAM
                    </v-card-title>
                    <template v-slot:append>
                        <v-btn 
                            v-if="isEditing" 
                            variant="tonal" 
                            color="teal" 
                            size="small"
                            prepend-icon="mdi-plus"
                            @click="addRamSlot"
                            class="text-none font-weight-bold"
                        >
                            Agregar Slot
                        </v-btn>
                    </template>
                </v-card-item>

                <v-card-text class="pa-6 flex-grow-1">
                    <div v-if="equipo.MemoriasRAM && equipo.MemoriasRAM.length > 0" class="d-flex flex-column gap-4">
                        <v-scale-transition group>
                            <div 
                                v-for="(slot, index) in equipo.MemoriasRAM" 
                                :key="index" 
                                class="ram-slot-card rounded-lg border-thin pa-4 position-relative bg-white"
                            >
                                <div class="d-flex align-center justify-space-between mb-3">
                                    <v-chip size="small" color="teal" variant="flat" class="font-weight-bold">
                                        Slot {{ index + 1 }}
                                    </v-chip>
                                    <v-btn 
                                        v-if="isEditing" 
                                        icon="mdi-delete-outline" 
                                        variant="text" 
                                        color="error" 
                                        density="compact"
                                        @click="removeRamSlot(index)"
                                    ></v-btn>
                                </div>
                                
                                <v-row dense>
                                    <v-col cols="12">
                                        <v-select 
                                            v-model="slot.TipoId"
                                            :items="tiposRam"
                                            item-title="Nombre"
                                            item-value="Id"
                                            density="comfortable" 
                                            label="Tipo" 
                                            variant="outlined" 
                                            hide-details="auto"
                                            color="teal"
                                            prepend-inner-icon="mdi-memory"
                                            @update:model-value="onRamTypeChange(slot)"
                                        ></v-select>
                                    </v-col>
                                    <v-col cols="6">
                                        <v-select 
                                            v-model="slot.CapacidadId"
                                            :items="capacidadesRam"
                                            item-title="Nombre"
                                            item-value="Id"
                                            density="comfortable" 
                                            label="Capacidad" 
                                            variant="outlined" 
                                            hide-details="auto"
                                            color="teal"
                                        ></v-select>
                                    </v-col>
                                    <v-col cols="6">
                                        <v-select 
                                            v-model="slot.VelocidadId"
                                            :items="getFilteredBuses(slot.TipoId)"
                                            item-title="Nombre"
                                            item-value="Id"
                                            density="comfortable" 
                                            label="Bus" 
                                            variant="outlined" 
                                            hide-details="auto"
                                            color="teal"
                                            :disabled="!slot.TipoId"
                                        ></v-select>
                                    </v-col>
                                </v-row>
                            </div>
                        </v-scale-transition>
                    </div>
                    <div v-else class="text-center text-grey py-8">
                        <v-icon size="48" color="grey-lighten-2" class="mb-2">mdi-memory</v-icon>
                        <div>No hay memorias RAM registradas</div>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>

        <!-- ALMACENAMIENTO -->
        <v-col cols="12" md="6">
            <v-card class="rounded-xl border-thin elevation-0 mb-6 h-100 d-flex flex-column">
                <v-card-item class="py-4 px-6 bg-grey-lighten-5 border-b-thin">
                    <template v-slot:prepend>
                        <v-avatar color="indigo-lighten-5" size="40" class="mr-2">
                            <v-icon color="indigo-darken-1" size="24">mdi-harddisk</v-icon>
                        </v-avatar>
                    </template>
                    <v-card-title class="text-h6 font-weight-bold text-indigo-darken-3">
                        Almacenamiento
                    </v-card-title>
                    <template v-slot:append>
                        <v-btn 
                            v-if="isEditing" 
                            variant="tonal" 
                            color="indigo" 
                            size="small"
                            prepend-icon="mdi-plus"
                            @click="addStorageSlot"
                            class="text-none font-weight-bold"
                        >
                            Agregar Disco
                        </v-btn>
                    </template>
                </v-card-item>

                <v-card-text class="pa-6 flex-grow-1">
                    <div v-if="equipo.Almacenamiento && equipo.Almacenamiento.length > 0" class="d-flex flex-column gap-4">
                        <v-scale-transition group>
                            <div 
                                v-for="(disk, index) in equipo.Almacenamiento" 
                                :key="index" 
                                class="storage-slot-card rounded-lg border-thin pa-4 position-relative bg-white"
                            >
                                <div class="d-flex align-center justify-space-between mb-3">
                                    <v-chip size="small" color="indigo" variant="flat" class="font-weight-bold">
                                        Disco {{ index + 1 }}
                                    </v-chip>
                                    <v-btn 
                                        v-if="isEditing" 
                                        icon="mdi-delete-outline" 
                                        variant="text" 
                                        color="error" 
                                        density="compact"
                                        @click="removeStorageSlot(index)"
                                    ></v-btn>
                                </div>
                                
                                <v-row dense>
                                    <v-col cols="12" md="6">
                                        <v-select 
                                            v-model="disk.TipoId"
                                            :items="tiposAlmacenamiento"
                                            item-title="Nombre"
                                            item-value="Id"
                                            density="comfortable" 
                                            label="Tipo" 
                                            variant="outlined" 
                                            hide-details="auto"
                                            color="indigo"
                                            prepend-inner-icon="mdi-harddisk"
                                            @update:model-value="onStorageTypeChange(disk)"
                                        ></v-select>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <v-select 
                                            v-model="disk.CapacidadId"
                                            :items="capacidadesAlmacenamiento"
                                            item-title="Nombre"
                                            item-value="Id"
                                            density="comfortable" 
                                            label="Capacidad" 
                                            variant="outlined" 
                                            hide-details="auto"
                                            color="indigo"
                                        ></v-select>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <v-select 
                                            v-model="disk.ProtocoloId"
                                            :items="getFilteredProtocols(disk.TipoId)"
                                            item-title="Nombre"
                                            item-value="Id"
                                            density="comfortable" 
                                            label="Protocolo" 
                                            variant="outlined" 
                                            hide-details="auto"
                                            color="indigo"
                                            prepend-inner-icon="mdi-connection"
                                            :disabled="!disk.TipoId"
                                        ></v-select>
                                    </v-col>
                                    <v-col cols="12" md="6">
                                        <v-select 
                                            v-model="disk.FactorFormaId"
                                            :items="getFilteredFormFactors(disk.TipoId)"
                                            item-title="Nombre"
                                            item-value="Id"
                                            density="comfortable" 
                                            label="Factor Forma" 
                                            variant="outlined" 
                                            hide-details="auto"
                                            color="indigo"
                                            prepend-inner-icon="mdi-ruler-square"
                                            :disabled="!disk.TipoId"
                                        ></v-select>
                                    </v-col>
                                </v-row>
                            </div>
                        </v-scale-transition>
                    </div>
                    <div v-else class="text-center text-grey py-8">
                        <v-icon size="48" color="grey-lighten-2" class="mb-2">mdi-harddisk-off</v-icon>
                        <div>No hay discos registrados</div>
                    </div>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useCatalogsStore } from '@/stores/catalogs'
import { storeToRefs } from 'pinia'

const props = defineProps({
    equipo: Object,
    isEditing: Boolean
})

const catalogsStore = useCatalogsStore()
const { 
    marcasProcesador, tiposProcesador, generacionesProcesador,
    tiposRam, capacidadesRam, busesRam,
    tiposAlmacenamiento, capacidadesAlmacenamiento,
    protocolosAlmacenamiento, factoresFormaAlmacenamiento
} = storeToRefs(catalogsStore)

function addRamSlot() {
    if (!props.equipo.MemoriasRAM) props.equipo.MemoriasRAM = []
    props.equipo.MemoriasRAM.push({ TipoId: null, CapacidadId: null, VelocidadId: null })
}

function removeRamSlot(index) {
    props.equipo.MemoriasRAM.splice(index, 1)
}

function addStorageSlot() {
    if (!props.equipo.Almacenamiento) props.equipo.Almacenamiento = []
    props.equipo.Almacenamiento.push({ TipoId: null, CapacidadId: null, ProtocoloId: null, FactorFormaId: null })
}

function removeStorageSlot(index) {
    props.equipo.Almacenamiento.splice(index, 1)
}

const filteredTiposProcesador = computed(() => {
    const marcaId = props.equipo.Procesadores?.[0]?.MarcaId
    if (!marcaId) return []
    return tiposProcesador.value.filter(t => t.MarcaId === marcaId)
})

const filteredGeneracionesProcesador = computed(() => {
    const tipoId = props.equipo.Procesadores?.[0]?.TipoId
    if (!tipoId) return []
    return generacionesProcesador.value.filter(g => g.TipoId === tipoId)
})

function onMarcaChange() {
    if (props.equipo.Procesadores?.[0]) {
        props.equipo.Procesadores[0].TipoId = null
        props.equipo.Procesadores[0].GeneracionId = null
    }
}

function onTipoChange() {
    if (props.equipo.Procesadores?.[0]) {
        props.equipo.Procesadores[0].GeneracionId = null
    }
}

function getFilteredBuses(tipoId) {
    if (!tipoId) return []
    return busesRam.value.filter(b => b.TipoRAMId === tipoId)
}

function onRamTypeChange(slot) {
    slot.VelocidadId = null
}

function getFilteredProtocols(tipoId) {
    if (!tipoId) return []
    return protocolosAlmacenamiento.value.filter(p => p.TipoId === tipoId)
}

function getFilteredFormFactors(tipoId) {
    if (!tipoId) return []
    return factoresFormaAlmacenamiento.value.filter(f => f.TipoId === tipoId)
}

function onStorageTypeChange(disk) {
    disk.ProtocoloId = null
    disk.FactorFormaId = null
}

onMounted(() => {
    catalogsStore.fetchCatalogs([
        'marcasProcesador', 'tiposProcesador', 'generacionesProcesador',
        'tiposRam', 'capacidadesRam', 'busesRam',
        'tiposAlmacenamiento', 'capacidadesAlmacenamiento',
        'protocolosAlmacenamiento', 'factoresFormaAlmacenamiento'
    ])
    
    // Ensure arrays exist
    if (!props.equipo.MemoriasRAM || props.equipo.MemoriasRAM.length === 0) {
        props.equipo.MemoriasRAM = [{ TipoId: null, CapacidadId: null, VelocidadId: null }]
    }
    if (!props.equipo.Almacenamiento || props.equipo.Almacenamiento.length === 0) {
        props.equipo.Almacenamiento = [{ TipoId: null, CapacidadId: null, ProtocoloId: null, FactorFormaId: null }]
    }
    if (!props.equipo.Procesadores || props.equipo.Procesadores.length === 0) {
        props.equipo.Procesadores = [{ MarcaId: null, TipoId: null, GeneracionId: null }]
    }
})
</script>



<style scoped>
.border-thin { border: 1px solid rgba(0,0,0,0.08) !important; }
.gap-4 { gap: 16px; }
</style>
