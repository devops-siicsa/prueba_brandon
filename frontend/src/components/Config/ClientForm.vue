<template>
  <v-dialog 
    v-model="dialog" 
    :max-width="isMobileDevice ? '100%' : '600'" 
    :fullscreen="isMobileDevice"
    :transition="isMobileDevice ? 'dialog-bottom-transition' : 'dialog-transition'"
    persistent
  >
    <v-card class="rounded-xl elevation-0" :class="{'rounded-0': isMobileDevice}">
      <!-- Header -->
      <div class="px-6 pt-6 pb-2 d-flex align-center justify-space-between">
        <div class="d-flex align-center">
            <div class="header-icon-box mr-3">
                <v-icon color="primary" size="24">mdi-account-tie</v-icon>
            </div>
            <div>
                <h2 class="text-h6 font-weight-bold text-grey-darken-3" style="line-height: 1.2;">
                    {{ company ? 'Editar Cliente' : 'Registrar Nuevo Cliente' }}
                </h2>
                <p class="text-caption text-grey mt-1">
                    Complete la información para {{ company ? 'actualizar el' : 'dar de alta un nuevo' }} cliente.
                </p>
            </div>
        </div>
        <v-btn icon="mdi-close" variant="text" color="grey-darken-1" density="comfortable" @click="dialog = false"></v-btn>
      </div>

      <v-divider class="mx-6 my-2"></v-divider>

      <v-card-text class="px-6 py-2 scroll-container" :style="isMobileDevice ? 'height: calc(100vh - 140px); overflow-y: auto;' : 'max-height: 60vh; overflow-y: auto;'">
        <v-form ref="form" @submit.prevent="save">
            <v-row dense>
                <!-- NIT -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">NIT / IDENTIFICACIÓN</label>
                    <v-text-field 
                        v-model="formData.NIT" 
                        placeholder="Ej. 900.123.456-7" 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-pound"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :rules="[v => !!v || 'Requerido']"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>

                <!-- Razón Social -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">RAZÓN SOCIAL</label>
                    <v-text-field 
                        v-model="formData.RazonSocial" 
                        placeholder="Nombre del cliente" 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-domain"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :rules="[v => !!v || 'Requerido']"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>

                <!-- Dirección -->
                <v-col cols="12">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">DIRECCIÓN PRINCIPAL</label>
                    <v-text-field 
                        v-model="formData.Direccion" 
                        placeholder="Calle, Carrera, Avenida..." 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-map-marker-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>

                <!-- Departamento -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">DEPARTAMENTO</label>
                    <v-autocomplete
                        v-model="formData.DepartamentoId"
                        :items="departments"
                        item-title="Nombre"
                        item-value="Id"
                        placeholder="Seleccionar..."
                        variant="outlined"
                        density="compact"
                        prepend-inner-icon="mdi-map-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        @update:model-value="loadCities"
                        hide-details="auto"
                    ></v-autocomplete>
                </v-col>

                <!-- Ciudad -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">CIUDAD</label>
                    <v-autocomplete
                        v-model="formData.CiudadId"
                        :items="cities"
                        item-title="Nombre"
                        item-value="Id"
                        placeholder="Seleccionar..."
                        variant="outlined"
                        density="compact"
                        prepend-inner-icon="mdi-map-marker-radius-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :disabled="!formData.DepartamentoId"
                        hide-details="auto"
                    ></v-autocomplete>
                </v-col>

                <!-- Teléfono -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">TELÉFONO DE CONTACTO</label>
                    <v-text-field 
                        v-model="formData.Telefono" 
                        placeholder="(+57) 300 000 0000" 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-phone-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>

                <!-- Estado -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">ESTADO DEL CLIENTE</label>
                    <div class="status-box d-flex align-center justify-space-between px-3 py-0 rounded-lg" :class="formData.Activo ? 'bg-blue-lighten-5' : 'bg-grey-lighten-4'">
                        <div class="d-flex align-center">
                            <v-icon :color="formData.Activo ? 'primary' : 'grey'" class="mr-2" size="16">
                                {{ formData.Activo ? 'mdi-check-circle' : 'mdi-minus-circle' }}
                            </v-icon>
                            <span class="text-caption font-weight-medium" :class="formData.Activo ? 'text-primary' : 'text-grey-darken-1'">
                                {{ formData.Activo ? 'Cliente Activo' : 'Cliente Inactivo' }}
                            </span>
                        </div>
                        <v-switch 
                            v-model="formData.Activo" 
                            color="primary" 
                            hide-details 
                            density="compact"
                            inset
                            class="scale-switch"
                        ></v-switch>
                    </div>
                </v-col>
            </v-row>
        </v-form>
      </v-card-text>

      <v-card-actions class="px-6 pb-6 pt-4 bg-white">
        <v-spacer></v-spacer>
        <v-btn 
            variant="text" 
            class="text-capitalize text-grey-darken-1 mr-2" 
            @click="dialog = false"
            density="comfortable"
        >
            Cancelar
        </v-btn>
        <v-btn 
            color="blue-grey-darken-4" 
            variant="flat"
            class="text-white text-capitalize rounded-lg px-6" 
            height="40"
            prepend-icon="mdi-content-save-outline"
            @click="save" 
            :loading="saving"
            elevation="0"
            density="comfortable"
        >
            {{ company ? 'Actualizar' : 'Guardar' }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios'

const props = defineProps({
    modelValue: Boolean,
    company: Object,
    isMobileDevice: Boolean
})

const emit = defineEmits(['update:modelValue', 'saved'])

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

const formData = ref({
    NIT: '',
    RazonSocial: '',
    Direccion: '',
    DepartamentoId: null,
    CiudadId: null,
    Telefono: '',
    Activo: true,
    EsCliente: true // Siempre true para clientes
})

const departments = ref([])
const cities = ref([])
const saving = ref(false)

async function loadDepartments() {
    try {
        const res = await axios.get('/api/config/departments', { withCredentials: true })
        departments.value = res.data
    } catch (e) {
        console.error(e)
    }
}

async function loadCities(deptId) {
    if (!deptId) {
        cities.value = []
        return
    }
    try {
        const res = await axios.get(`/api/config/cities/${deptId}`, { withCredentials: true })
        cities.value = res.data
    } catch (e) {
        console.error(e)
    }
}

async function save() {
    saving.value = true
    try {
        const url = props.company 
            ? `/api/config/companies/${props.company.Id}`
            : '/api/config/companies'
        
        const method = props.company ? 'put' : 'post'
        
        // Asegurar EsCliente = true
        formData.value.EsCliente = true
        
        await axios[method](url, formData.value, { withCredentials: true })
        
        emit('saved')
        dialog.value = false
    } catch (e) {
        alert("Error al guardar: " + (e.response?.data?.message || e.message))
    } finally {
        saving.value = false
    }
}

watch(() => props.company, async (val) => {
    if (val) {
        formData.value = { ...val, EsCliente: true }
        if (val.DepartamentoId) {
            loadCities(val.DepartamentoId)
        }
    } else {
        formData.value = {
            NIT: '',
            RazonSocial: '',
            Direccion: '',
            DepartamentoId: null,
            CiudadId: null,
            Telefono: '',
            Activo: true,
            EsCliente: true
        }
        cities.value = []
    }
})

onMounted(loadDepartments)
</script>

<style scoped>
.header-icon-box {
    width: 42px;
    height: 42px;
    background-color: #e3f2fd;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.status-box {
    border: 1px solid #e0e0e0;
    height: 36px;
}

.scale-switch {
    transform: scale(0.8);
    transform-origin: right center;
}

:deep(.v-field__outline) {
    --v-field-border-opacity: 0.15;
}

:deep(.v-field--focused .v-field__outline) {
    --v-field-border-opacity: 0.5;
}

/* Custom Scrollbar Styling */
.scroll-container {
    scrollbar-width: thin;
    scrollbar-color: #e0e0e0 transparent;
}

.scroll-container::-webkit-scrollbar {
    width: 6px;
}

.scroll-container::-webkit-scrollbar-track {
    background: transparent;
}

.scroll-container::-webkit-scrollbar-thumb {
    background-color: #e0e0e0;
    border-radius: 20px;
    border: 2px solid transparent;
    background-clip: content-box;
}

.scroll-container::-webkit-scrollbar-thumb:hover {
    background-color: #bdbdbd;
}
</style>
