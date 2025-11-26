<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <v-card class="rounded-xl elevation-0">
      <!-- Header -->
      <div class="px-6 pt-6 pb-2 d-flex align-center justify-space-between">
        <div class="d-flex align-center">
            <div class="header-icon-box mr-3">
                <v-icon color="primary" size="24">mdi-map-marker</v-icon>
            </div>
            <div>
                <h2 class="text-h6 font-weight-bold text-grey-darken-3" style="line-height: 1.2;">
                    {{ sede ? 'Editar Sede' : 'Registrar Nueva Sede' }}
                </h2>
                <p class="text-caption text-grey mt-1">
                    Complete la información para {{ sede ? 'actualizar la' : 'dar de alta una nueva' }} sede.
                </p>
            </div>
        </div>
        <v-btn icon="mdi-close" variant="text" color="grey-darken-1" density="comfortable" @click="dialog = false"></v-btn>
      </div>

      <v-divider class="mx-6 my-2"></v-divider>

      <v-card-text class="px-6 py-2 scroll-container" style="max-height: 60vh; overflow-y: auto;">
        <v-form ref="form" @submit.prevent="save">
            <v-row dense>
                <!-- Empresa -->
                <v-col cols="12">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">EMPRESA ASOCIADA</label>
                    <v-autocomplete
                        v-model="formData.EmpresaId"
                        :items="companies"
                        item-title="RazonSocial"
                        item-value="Id"
                        placeholder="Seleccionar empresa..."
                        variant="outlined"
                        density="compact"
                        prepend-inner-icon="mdi-domain"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :rules="[v => !!v || 'Requerido']"
                        hide-details="auto"
                    ></v-autocomplete>
                </v-col>

                <!-- Nombre Sede -->
                <v-col cols="12">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">NOMBRE DE LA SEDE</label>
                    <v-text-field 
                        v-model="formData.NombreSede" 
                        placeholder="Ej. Sede Principal, Oficina Norte..." 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-store-marker-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :rules="[v => !!v || 'Requerido']"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>

                <!-- Departamento -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">DEPARTAMENTO</label>
                    <v-autocomplete
                        v-model="selectedDept"
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
                        return-object
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
                        :disabled="!selectedDept"
                        :rules="[v => !!v || 'Requerido']"
                        hide-details="auto"
                    ></v-autocomplete>
                </v-col>

                <!-- Dirección -->
                <v-col cols="12">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">DIRECCIÓN FÍSICA</label>
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

                <!-- Teléfono -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">TELÉFONO DE CONTACTO</label>
                    <v-text-field 
                        v-model="formData.Telefono" 
                        placeholder="(+57) 601 000 0000" 
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
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">ESTADO DE LA SEDE</label>
                    <div class="status-box d-flex align-center justify-space-between px-3 py-0 rounded-lg" :class="formData.Activo ? 'bg-blue-lighten-5' : 'bg-grey-lighten-4'">
                        <div class="d-flex align-center">
                            <v-icon :color="formData.Activo ? 'primary' : 'grey'" class="mr-2" size="16">
                                {{ formData.Activo ? 'mdi-check-circle' : 'mdi-minus-circle' }}
                            </v-icon>
                            <span class="text-caption font-weight-medium" :class="formData.Activo ? 'text-primary' : 'text-grey-darken-1'">
                                {{ formData.Activo ? 'Sede Activa' : 'Sede Inactiva' }}
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
            :loading="loading"
            elevation="0"
            density="comfortable"
        >
            {{ sede ? 'Actualizar' : 'Guardar' }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
    modelValue: Boolean,
    sede: Object,
    companies: Array
})

const emit = defineEmits(['update:modelValue', 'save'])

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

const form = ref(null)
const loading = ref(false)
const departments = ref([])
const cities = ref([])
const selectedDept = ref(null)

const formData = ref({
    EmpresaId: null,
    NombreSede: '',
    Direccion: '',
    Telefono: '',
    CiudadId: null,
    Activo: true
})

async function loadDepartments() {
    try {
        const res = await axios.get('http://localhost:5000/api/config/departments', { withCredentials: true })
        departments.value = res.data
    } catch (e) {
        console.error(e)
    }
}

async function loadCities(dept) {
    if (!dept) {
        cities.value = []
        return
    }
    try {
        const res = await axios.get(`http://localhost:5000/api/config/cities/${dept.Id}`, { withCredentials: true })
        cities.value = res.data
    } catch (e) {
        console.error(e)
    }
}

// Helper para encontrar depto (idealmente el backend enviaría el DeptId)
async function findDepartmentByCity(cityId) {
    // Nota: Esto sigue siendo un workaround. Lo ideal es que el backend devuelva el DeptId.
    // Por ahora, no bloquearemos la carga si no se encuentra.
}

async function save() {
    const { valid } = await form.value.validate()
    if (!valid) return
    
    loading.value = true
    try {
        const url = props.sede 
            ? `http://localhost:5000/api/config/sedes/${props.sede.Id}`
            : 'http://localhost:5000/api/config/sedes'
        
        const method = props.sede ? 'put' : 'post'
        
        await axios[method](url, formData.value, { withCredentials: true })
        emit('save')
        dialog.value = false
    } catch (error) {
        console.error(error)
        alert('Error al guardar: ' + (error.response?.data?.message || error.message))
    } finally {
        loading.value = false
    }
}

watch(() => props.sede, async (val) => {
    if (val) {
        formData.value = { ...val }
        // Si hay ciudad, intentaríamos cargar el depto, pero por ahora lo dejamos limpio
        // para que el usuario seleccione si edita.
        selectedDept.value = null 
        cities.value = []
    } else {
        formData.value = {
            EmpresaId: null,
            NombreSede: '',
            Direccion: '',
            Telefono: '',
            CiudadId: null,
            Activo: true
        }
        selectedDept.value = null
        cities.value = []
    }
})

onMounted(() => {
    loadDepartments()
})
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
