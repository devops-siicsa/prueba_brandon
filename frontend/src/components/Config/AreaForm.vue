<template>
  <v-dialog 
    v-model="dialog" 
    :max-width="isMobileApp ? '100%' : '500'" 
    :fullscreen="isMobileApp"
    :transition="isMobileApp ? 'dialog-bottom-transition' : 'dialog-transition'"
    persistent
  >
    <v-card class="rounded-xl" :class="{'rounded-0': isMobileApp}">
        <v-card-title class="px-6 pt-6 pb-2 d-flex align-center justify-space-between">
            <span class="text-h6 font-weight-bold text-grey-darken-3">
                {{ area.Id ? 'Editar Área' : 'Nueva Área' }}
            </span>
            <v-btn icon="mdi-close" variant="text" color="grey" density="comfortable" @click="dialog = false"></v-btn>
        </v-card-title>
        
        <v-divider class="mx-6"></v-divider>

        <v-card-text class="px-6 py-4">
            <v-form ref="form" @submit.prevent="save">
                <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">NOMBRE DEL ÁREA</label>
                <v-text-field
                    v-model="formData.Nombre"
                    placeholder="Ej. Recursos Humanos"
                    variant="outlined"
                    density="compact"
                    bg-color="grey-lighten-5"
                    class="rounded-lg mb-4"
                    :rules="[v => !!v || 'El nombre es requerido']"
                    hide-details="auto"
                    autofocus
                ></v-text-field>

                <div v-if="area.Id">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">ESTADO</label>
                    <v-switch
                        v-model="formData.Activo"
                        color="primary"
                        :label="formData.Activo ? 'Activo' : 'Inactivo'"
                        hide-details
                        inset
                    ></v-switch>
                </div>
            </v-form>
        </v-card-text>

        <v-card-actions class="px-6 pb-6 pt-2">
            <v-spacer></v-spacer>
            <v-btn variant="text" color="grey-darken-1" class="text-capitalize" @click="dialog = false">Cancelar</v-btn>
            <v-btn 
                color="#1e293b" 
                variant="flat" 
                class="text-white text-capitalize rounded-lg px-6"
                @click="save"
                :loading="loading"
            >
                {{ area.Id ? 'Actualizar' : 'Guardar' }}
            </v-btn>
        </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useDisplay } from 'vuetify'
import axios from 'axios'

import { useMobileDetection } from '@/composables/useMobileDetection'

const props = defineProps({
    modelValue: Boolean,
    area: {
        type: Object,
        default: () => ({})
    }
})

const emit = defineEmits(['update:modelValue', 'save'])
const { isMobileApp } = useMobileDetection()

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

const form = ref(null)
const loading = ref(false)
const formData = ref({
    Nombre: '',
    Activo: true
})

watch(() => props.area, (val) => {
    if (val && val.Id) {
        formData.value = { ...val }
    } else {
        formData.value = {
            Nombre: '',
            Activo: true
        }
    }
}, { immediate: true })

async function save() {
    const { valid } = await form.value.validate()
    if (!valid) return

    loading.value = true
    try {
        const url = '/api/config/catalogs/areas'
        
        if (props.area.Id) {
            await axios.put(`${url}/${props.area.Id}`, formData.value, { withCredentials: true })
        } else {
            await axios.post(url, { Nombre: formData.value.Nombre }, { withCredentials: true })
        }
        
        emit('save')
        dialog.value = false
    } catch (e) {
        console.error(e)
        alert("Error al guardar: " + (e.response?.data?.message || e.message))
    } finally {
        loading.value = false
    }
}
</script>
