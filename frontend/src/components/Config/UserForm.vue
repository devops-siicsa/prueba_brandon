<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <v-card class="rounded-xl elevation-0">
      <!-- Header -->
      <div class="px-6 pt-6 pb-2 d-flex align-center justify-space-between">
        <div class="d-flex align-center">
            <div class="header-icon-box mr-3">
                <v-icon color="primary" size="24">mdi-account</v-icon>
            </div>
            <div>
                <h2 class="text-h6 font-weight-bold text-grey-darken-3" style="line-height: 1.2;">
                    {{ user ? 'Editar Usuario' : 'Registrar Nuevo Usuario' }}
                    <span v-if="clientMode" class="text-caption text-primary ml-2">(Modo Cliente)</span>
                    <span v-else class="text-caption text-grey ml-2">(Modo Sistema)</span>
                </h2>
                <p class="text-caption text-grey mt-1">
                    Complete la información para {{ user ? 'actualizar el' : 'dar de alta un nuevo' }} usuario.
                </p>
            </div>
        </div>
        <v-btn icon="mdi-close" variant="text" color="grey-darken-1" density="comfortable" @click="dialog = false"></v-btn>
      </div>

      <v-divider class="mx-6 my-2"></v-divider>

      <v-card-text class="px-6 py-2 scroll-container" style="max-height: 60vh; overflow-y: auto;">
        <v-form ref="form" @submit.prevent="save">
            <v-row dense>
                <!-- Nombre y Apellido -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">NOMBRE</label>
                    <v-text-field 
                        v-model="formData.Nombre" 
                        placeholder="Ej. Juan" 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-account-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :rules="[v => !!v || 'Requerido']"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">APELLIDO</label>
                    <v-text-field 
                        v-model="formData.Apellido" 
                        placeholder="Ej. Pérez" 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-account-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :rules="[v => !!v || 'Requerido']"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>

                <!-- Correo y Celular -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">CORREO ELECTRÓNICO</label>
                    <v-text-field 
                        v-model="formData.Correo" 
                        placeholder="juan.perez@empresa.com" 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-email-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        :rules="[v => !!v || 'Requerido', v => /.+@.+\..+/.test(v) || 'Correo inválido']"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">CELULAR</label>
                    <v-text-field 
                        v-model="formData.Celular" 
                        placeholder="(+57) 300 000 0000" 
                        variant="outlined" 
                        density="compact"
                        prepend-inner-icon="mdi-phone-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        hide-details="auto"
                    ></v-text-field>
                </v-col>

                <!-- Cargo y Área -->
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">CARGO</label>
                    <v-autocomplete
                        v-model="formData.CargoId"
                        :items="cargos"
                        item-title="Nombre"
                        item-value="Id"
                        placeholder="Seleccionar..."
                        variant="outlined"
                        density="compact"
                        prepend-inner-icon="mdi-badge-account-horizontal-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        hide-details="auto"
                    ></v-autocomplete>
                </v-col>
                <v-col cols="12" md="6">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">ÁREA</label>
                    <v-autocomplete
                        v-model="formData.AreaId"
                        :items="areas"
                        item-title="Nombre"
                        item-value="Id"
                        placeholder="Seleccionar..."
                        variant="outlined"
                        density="compact"
                        prepend-inner-icon="mdi-chart-tree"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        hide-details="auto"
                    ></v-autocomplete>
                </v-col>

                <!-- Sede -->
                <v-col cols="12">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">SEDE ASIGNADA</label>
                    <v-autocomplete
                        v-model="formData.SedeId"
                        :items="filteredSedes"
                        item-title="NombreSede"
                        item-value="Id"
                        placeholder="Seleccionar sede..."
                        variant="outlined"
                        density="compact"
                        prepend-inner-icon="mdi-map-marker-outline"
                        bg-color="grey-lighten-5"
                        class="rounded-lg"
                        hide-details="auto"
                    ></v-autocomplete>
                </v-col>

                <v-col cols="12"><v-divider class="my-2"></v-divider></v-col>

                <!-- Usuario de Sistema -->
                <v-col cols="12">
                    <div class="d-flex align-center justify-space-between">
                        <div>
                            <label class="text-caption font-weight-bold text-grey-darken-1 mb-0 d-block">ACCESO AL SISTEMA</label>
                            <span class="text-caption text-grey">Habilitar credenciales de acceso</span>
                        </div>
                        <v-switch 
                            v-model="formData.EsUsuarioSistema" 
                            color="primary" 
                            hide-details 
                            density="compact"
                            inset
                            class="scale-switch"
                        ></v-switch>
                    </div>
                </v-col>

                <template v-if="formData.EsUsuarioSistema">
                    <!-- Rol -->
                    <v-col cols="12">
                        <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">ROL DE USUARIO</label>
                        <v-autocomplete
                            v-model="formData.RolId"
                            :items="filteredRoles"
                            item-title="Nombre"
                            item-value="Id"
                            placeholder="Seleccionar rol..."
                            variant="outlined"
                            density="compact"
                            prepend-inner-icon="mdi-shield-account-outline"
                            bg-color="grey-lighten-5"
                            class="rounded-lg"
                            :rules="[v => !!v || 'Requerido para usuarios de sistema']"
                            hide-details="auto"
                            @update:model-value="onRoleChange"
                        ></v-autocomplete>
                    </v-col>

                    <!-- Permisos Específicos -->
                    <v-col cols="12">
                        <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">PERMISOS ADICIONALES (GRANULARES)</label>
                        
                        <div class="d-flex align-center mb-2">
                            <v-btn
                                color="blue-grey-lighten-5"
                                variant="flat"
                                class="text-blue-grey-darken-3 text-capitalize rounded-lg flex-grow-1"
                                prepend-icon="mdi-shield-edit-outline"
                                height="40"
                                @click="permissionsDialog = true"
                                border
                            >
                                Asignar Permisos Adicionales
                            </v-btn>
                            <v-chip
                                v-if="formData.PermisosEspecificos.length > 0"
                                color="primary"
                                class="ml-2 font-weight-bold"
                                size="large"
                            >
                                {{ formData.PermisosEspecificos.length }}
                            </v-chip>
                        </div>

                        <!-- Resumen de permisos seleccionados (Chips) -->
                        <div v-if="formData.PermisosEspecificos.length > 0" class="d-flex flex-wrap gap-1 mt-1">
                            <v-chip
                                v-for="permId in formData.PermisosEspecificos"
                                :key="permId"
                                size="small"
                                color="blue-grey"
                                variant="tonal"
                                class="mr-1 mb-1"
                            >
                                {{ getPermissionName(permId) }}
                            </v-chip>
                        </div>
                    </v-col>

                    <!-- Modal de Selección de Permisos -->
                    <v-dialog v-model="permissionsDialog" max-width="900" scrollable>
                        <v-card class="rounded-xl bg-white">
                            <!-- Header Modal -->
                            <div class="px-5 py-4 d-flex align-center justify-space-between border-bottom">
                                <div class="d-flex align-center">
                                    <v-icon color="primary" class="mr-2">mdi-shield-outline</v-icon>
                                    <span class="text-h6 font-weight-bold text-grey-darken-3">Permisos Granulares</span>
                                </div>
                                <div class="d-flex align-center">
                                    <span class="text-caption text-grey mr-4">{{ activePermissionsCount }} activos</span>
                                    <v-btn icon="mdi-close" variant="text" density="comfortable" color="grey" @click="permissionsDialog = false"></v-btn>
                                </div>
                            </div>
                            
                            <v-divider></v-divider>
                            
                            <v-card-text class="px-5 py-5 bg-grey-lighten-5" style="max-height: 75vh;">
                                <v-row>
                                    <v-col cols="12" md="6" v-for="category in visibleCategories" :key="category.name">
                                        <v-card 
                                            class="rounded-lg h-100 transition-swing" 
                                            elevation="0" 
                                            border 
                                            style="border-color: #e0e0e0;"
                                            :class="{ 'opacity-50': isCategoryDisabled(category.name) }"
                                        >
                                            <!-- Header de Categoría -->
                                            <div class="px-4 py-3 bg-white d-flex align-center justify-space-between">
                                                <div class="d-flex align-center text-indigo-darken-1 font-weight-bold text-subtitle-2">
                                                    <v-icon :icon="category.icon" size="small" class="mr-2"></v-icon>
                                                    {{ category.name }}
                                                </div>
                                                <v-checkbox-btn
                                                    :model-value="isCategorySelected(category)"
                                                    @update:model-value="val => toggleCategory(category, val)"
                                                    :disabled="isCategoryDisabled(category.name) || isSuperAdmin"
                                                    density="compact"
                                                    color="indigo-lighten-1"
                                                    hide-details
                                                    class="ma-0 pa-0"
                                                ></v-checkbox-btn>
                                            </div>
                                            
                                            <!-- Lista de Permisos -->
                                            <div class="px-4 pb-3 pt-0">
                                                <div v-for="sub in category.submodules" :key="sub.name" class="mb-1">
                                                    <!-- Subtítulo si hay subcategoría específica -->
                                                    <div v-if="sub.name !== 'General' && category.submodules.length > 1" class="text-caption font-weight-bold text-grey-darken-1 mb-2 mt-2 pl-1">
                                                        {{ sub.name.replace('Sección ', '') }}
                                                    </div>
                                                    
                                                    <div v-for="perm in sub.permissions" :key="perm.Id" class="d-flex align-center mb-1 permission-row">
                                                        <v-checkbox-btn
                                                            v-model="formData.PermisosEspecificos"
                                                            :value="perm.Id"
                                                            :disabled="isCategoryDisabled(category.name) || isSuperAdmin"
                                                            density="compact"
                                                            color="indigo-lighten-1"
                                                            hide-details
                                                            class="mr-2"
                                                        ></v-checkbox-btn>
                                                        <span class="text-body-2 text-grey-darken-2" style="line-height: 1.2;">
                                                            {{ perm.Descripcion }}
                                                        </span>
                                                    </div>
                                                </div>
                                            </div>
                                        </v-card>
                                    </v-col>
                                </v-row>
                                
                                <v-alert v-if="isSuperAdmin" type="success" variant="tonal" density="compact" class="mt-6 text-caption bg-green-lighten-5 text-green-darken-2" icon="mdi-shield-check" border="start" style="border-color: #4CAF50;">
                                    <template v-slot:title>
                                        <span class="text-green-darken-3 font-weight-bold">Acceso Total</span>
                                    </template>
                                    El rol "SUPER ADMINISTRADOR" tiene acceso a todos los permisos del sistema automáticamente.
                                </v-alert>

                                <v-alert v-else type="info" variant="tonal" density="compact" class="mt-6 text-caption bg-blue-lighten-5 text-blue-darken-2" icon="mdi-information-outline" border="start" style="border-color: #2196F3;">
                                    <template v-slot:title>
                                        <span class="text-blue-darken-3 font-weight-bold">Modo Personalizado</span>
                                    </template>
                                    Al modificar manualmente cualquier casilla, el rol cambiará automáticamente a "Personalizado".
                                    <br>
                                    <strong>Nota:</strong> Algunas secciones requieren activar permisos de "Navegación" primero.
                                </v-alert>
                            </v-card-text>
                            <v-divider></v-divider>
                            <v-card-actions class="px-4 pb-4 pt-2">
                                <v-spacer></v-spacer>
                                <v-btn color="primary" variant="flat" class="text-capitalize rounded-lg px-6" @click="permissionsDialog = false">
                                    Listo
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>

                    <!-- Password -->
                    <v-col cols="12" md="6">
                        <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">CONTRASEÑA</label>
                        <v-text-field 
                            v-model="formData.Password" 
                            :placeholder="user ? 'Dejar en blanco para mantener' : 'Contraseña'" 
                            variant="outlined" 
                            density="compact"
                            prepend-inner-icon="mdi-lock-outline"
                            bg-color="grey-lighten-5"
                            class="rounded-lg"
                            type="password"
                            :rules="passwordRules"
                            hide-details="auto"
                        ></v-text-field>
                    </v-col>
                </template>

                <v-col cols="12"><v-divider class="my-2"></v-divider></v-col>

                <!-- Estado -->
                <v-col cols="12">
                    <label class="text-caption font-weight-bold text-grey-darken-1 mb-1 d-block">ESTADO DEL USUARIO</label>
                    <div class="status-box d-flex align-center justify-space-between px-3 py-0 rounded-lg" :class="formData.Activo ? 'bg-blue-lighten-5' : 'bg-grey-lighten-4'">
                        <div class="d-flex align-center">
                            <v-icon :color="formData.Activo ? 'primary' : 'grey'" class="mr-2" size="16">
                                {{ formData.Activo ? 'mdi-check-circle' : 'mdi-minus-circle' }}
                            </v-icon>
                            <span class="text-caption font-weight-medium" :class="formData.Activo ? 'text-primary' : 'text-grey-darken-1'">
                                {{ formData.Activo ? 'Usuario Activo' : 'Usuario Inactivo' }}
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
            {{ user ? 'Actualizar' : 'Guardar' }}
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
    user: Object,
    allowedRoles: {
        type: Array,
        default: () => []
    },
    clientMode: {
        type: Boolean,
        default: false
    }
})

const emit = defineEmits(['update:modelValue', 'save'])

const dialog = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
})

// ... (refs existentes)

// Roles filtrados según props
const filteredRoles = computed(() => {
    if (props.allowedRoles.length === 0) return roles.value
    return roles.value.filter(r => props.allowedRoles.includes(r.Nombre))
})

// Determinar si es contexto de cliente (para ocultar permisos de sistema)
const isClientContext = computed(() => {
    return props.allowedRoles.length > 0 && props.allowedRoles.some(r => r.includes('CLIENTE'))
})

// Categorías visibles en el modal
const visibleCategories = computed(() => {
    if (!isClientContext.value) return structuredPermissions.value
    
    // Si es cliente, ocultar categorías de sistema global
    // O mostrar solo las específicas
    const allowedCategories = [
        'Navegación / Menú Principal',
        'Panel: Configuración Cliente',
        'Inventario y Dashboard',
        'Ficha de Equipo (Detalle)'
    ]
    
    // Permisos específicos a ocultar en contexto cliente
    const hiddenPermissions = [
        'Ver Configuración del Sistema',
        'Ver Dashboard Global (Todos)',
        'Ver Inventario Global'
    ]

    return structuredPermissions.value
        .filter(c => allowedCategories.includes(c.name))
        .map(category => {
            // Clonar la categoría para no mutar el original
            const newCategory = { ...category }
            
            // Filtrar submodulos y sus permisos
            newCategory.submodules = category.submodules.map(sub => ({
                ...sub,
                permissions: sub.permissions.filter(p => !hiddenPermissions.includes(p.Descripcion))
            })).filter(sub => sub.permissions.length > 0) // Eliminar submodulos vacíos

            // Recalcular allPermissions para la categoría filtrada
            newCategory.allPermissions = newCategory.submodules.flatMap(s => s.permissions)

            return newCategory
        })
        .filter(c => c.allPermissions.length > 0) // Eliminar categorías vacías
})

// ... (resto del código)

const form = ref(null)
const loading = ref(false)
const permissionsDialog = ref(false) // Control del modal
const roles = ref([])
const permissions = ref([])
const groupedPermissions = ref([])
const structuredPermissions = ref([]) // Nuevo ref para grid
const sedes = ref([])
const companies = ref([])
const cargos = ref([])
const areas = ref([])

// Helper para obtener nombre del permiso por ID
const getPermissionName = (id) => {
    const perm = permissions.value.find(p => p.Id === id)
    return perm ? perm.Descripcion : 'Desconocido'
}

const formData = ref({
    Nombre: '',
    Apellido: '',
    Correo: '',
    Celular: '',
    CargoId: null,
    AreaId: null,
    SedeId: null,
    RolId: null,
    PermisosEspecificos: [],
    EsUsuarioSistema: false,
    Password: '',
    Activo: true
})

const passwordRules = computed(() => {
    if (!formData.value.EsUsuarioSistema) return []
    if (props.user && !formData.value.Password) return [] // Editando y vacía = no cambiar
    return [v => !!v || 'Requerida']
})

async function loadCatalogs() {
    try {
        const [rolesRes, permsRes, sedesRes, cargosRes, areasRes, companiesRes] = await Promise.all([
            axios.get('http://localhost:5000/api/config/roles', { withCredentials: true }),
            axios.get('http://localhost:5000/api/config/permissions', { withCredentials: true }),
            axios.get('http://localhost:5000/api/config/sedes', { withCredentials: true }),
            axios.get('http://localhost:5000/api/config/catalogs/cargos', { withCredentials: true }),
            axios.get('http://localhost:5000/api/config/catalogs/areas', { withCredentials: true }),
            axios.get('http://localhost:5000/api/config/companies', { withCredentials: true })
        ])
        roles.value = rolesRes.data
        permissions.value = permsRes.data
        
        // Agrupar permisos por Módulo y SubMódulo
        const grouped = {}
        permissions.value.forEach(p => {
            const mod = p.Modulo || 'Otros'
            const sub = p.SubModulo || 'General'
            
            if (!grouped[mod]) grouped[mod] = {}
            if (!grouped[mod][sub]) grouped[mod][sub] = []
            
            grouped[mod][sub].push(p)
        })

        // Mapeo de Iconos (Coincidiendo con Screenshot)
        const iconMap = {
            'Seguridad y Acceso': 'mdi-lock-outline',
            'Navegación / Menú Principal': 'mdi-view-grid-outline',
            'Panel: Configuración del Sistema': 'mdi-server',
            'Panel: Configuración Cliente': 'mdi-account-cog-outline',
            'Inventario y Dashboard': 'mdi-package-variant',
            'Ficha de Equipo (Detalle)': 'mdi-wrench-outline',
            'Otros': 'mdi-shield-star-outline'
        }
        
        // Orden deseado de categorías (según diseño)
        const categoryOrder = [
            'Navegación / Menú Principal',
            'Panel: Configuración del Sistema',
            'Panel: Configuración Cliente',
            'Inventario y Dashboard',
            'Ficha de Equipo (Detalle)',
            'Seguridad y Acceso'
        ]

        // Estructurar para el Grid (Array de Categorías)
        structuredPermissions.value = Object.keys(grouped)
            .sort((a, b) => {
                const indexA = categoryOrder.indexOf(a)
                const indexB = categoryOrder.indexOf(b)
                // Si no está en la lista, ponerlo al final
                return (indexA === -1 ? 999 : indexA) - (indexB === -1 ? 999 : indexB)
            })
            .map(mod => {
                const submodulesObj = grouped[mod]
                const submodules = Object.keys(submodulesObj).sort().map(sub => ({
                    name: sub,
                    permissions: submodulesObj[sub]
                }))
                
                // Aplanar permisos para facilitar "Seleccionar Todo"
                const allPerms = submodules.flatMap(s => s.permissions)
                
                return {
                    name: mod,
                    icon: iconMap[mod] || 'mdi-circle-small',
                    submodules: submodules,
                    allPermissions: allPerms
                }
            })

        sedes.value = sedesRes.data
        cargos.value = cargosRes.data
        areas.value = areasRes.data
        companies.value = companiesRes.data
    } catch (e) {
        console.error(e)
    }
}

const filteredSedes = computed(() => {
    return sedes.value.filter(s => {
        if (!s.Activo) return false
        // Use loose equality (==) to handle potential string/number mismatch
        const comp = companies.value.find(c => c.Id == s.EmpresaId)
        
        if (!comp) {
            console.warn(`Sede ${s.NombreSede} has no company (Id: ${s.EmpresaId})`)
            return false
        }
        
        const isActive = comp.Activo
        
        // Filter based on clientMode prop
        const matchesMode = props.clientMode ? comp.EsCliente : !comp.EsCliente

        return matchesMode && isActive
    })
})

// Helper para obtener ID por Código
const getPermissionIdByCode = (code) => {
    const perm = permissions.value.find(p => p.Codigo === code)
    return perm ? perm.Id : null
}

// Verificar si una categoría debe estar deshabilitada
const isCategoryDisabled = (categoryName) => {
    const sysConfigId = getPermissionIdByCode('menu:view_sys_config')
    const clientConfigId = getPermissionIdByCode('menu:view_client_config')
    
    // Si no se han cargado los permisos aún
    if (!sysConfigId || !clientConfigId) return false

    const hasSysConfig = formData.value.PermisosEspecificos.includes(sysConfigId)
    const hasClientConfig = formData.value.PermisosEspecificos.includes(clientConfigId)

    if (categoryName === 'Panel: Configuración del Sistema') {
        return !hasSysConfig
    }
    
    if (categoryName === 'Panel: Configuración Cliente') {
        return !hasClientConfig
    }
    
    return false
}

// Contador de permisos activos
const activePermissionsCount = computed(() => {
    return formData.value.PermisosEspecificos.length
})

// Lógica para "Seleccionar Todo" en una categoría
const toggleCategory = (category, isSelected) => {
    if (isSuperAdmin.value) return // No permitir cambios si es Super Admin
    if (isCategoryDisabled(category.name)) return // No permitir si está deshabilitado
    
    const permIds = category.allPermissions.map(p => p.Id)
    if (isSelected) {
        // Agregar los que no estén ya
        permIds.forEach(id => {
            if (!formData.value.PermisosEspecificos.includes(id)) {
                formData.value.PermisosEspecificos.push(id)
            }
        })
    } else {
        // Remover todos los de esta categoría
        formData.value.PermisosEspecificos = formData.value.PermisosEspecificos.filter(id => !permIds.includes(id))
    }
}

// Verificar si todos los permisos de una categoría están seleccionados
const isCategorySelected = (category) => {
    if (!category.allPermissions.length) return false
    return category.allPermissions.every(p => formData.value.PermisosEspecificos.includes(p.Id))
}

// Computed para saber si es Super Admin
const isSuperAdmin = computed(() => {
    const selectedRol = roles.value.find(r => r.Id === formData.value.RolId)
    return selectedRol && selectedRol.Nombre === 'SUPER ADMINISTRADOR'
})

// Manejar cambio de rol
const onRoleChange = (newRolId) => {
    const selectedRol = roles.value.find(r => r.Id === newRolId)
    if (selectedRol) {
        if (selectedRol.Nombre === 'SUPER ADMINISTRADOR') {
            // Asignar TODOS los permisos
            formData.value.PermisosEspecificos = permissions.value.map(p => p.Id)
        } else if (selectedRol.Permisos) {
            // Asignar permisos del rol
            formData.value.PermisosEspecificos = [...selectedRol.Permisos]
        } else {
            formData.value.PermisosEspecificos = []
        }
    }
}

async function save() {
    const { valid } = await form.value.validate()
    if (!valid) return
    
    loading.value = true
    try {
        const url = props.user 
            ? `http://localhost:5000/api/config/users/${props.user.Id}`
            : 'http://localhost:5000/api/config/users'
        
        const method = props.user ? 'put' : 'post'
        
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

watch(() => props.user, (val) => {
    if (val) {
        formData.value = { 
            ...val, 
            Password: '', // No mostrar hash
            EsUsuarioSistema: !!val.RolId // Inferir si es usuario de sistema si tiene rol
        }
    } else {
        formData.value = {
            Nombre: '',
            Apellido: '',
            Correo: '',
            Celular: '',
            CargoId: null,
            AreaId: null,
            SedeId: null,
            RolId: null,
            EsUsuarioSistema: false,
            Password: '',
            Activo: true
        }
    }
})

watch(() => props.modelValue, (val) => {
    if (val) {
        loadCatalogs()
    }
})

onMounted(() => {
    loadCatalogs()
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
