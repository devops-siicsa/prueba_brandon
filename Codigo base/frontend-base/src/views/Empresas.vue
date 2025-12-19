<template>
    <v-app>
    <AppHeader :nombre-comercial="nombreComercial" :imagen-comercial="imagenComercial" :correo-usuario="correoUsuario"
      :comercial-id="comercialId" :base-u-r-l="baseURL" v-model:drawer="drawer" @imagen-actualizada="actualizarImagen"
      @cerrar-sesion="cerrarSesion" />

    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
                <!----- Contenido Principal ----->
                <v-row style="border-radius: 15px; background-color: #006ca1">
                    <v-col>
                        <v-row>
                            <v-col style="color: white; font-weight: bold; ">
                                <v-icon> mdi-office-building </v-icon>
                                Listar prospectos
                                <v-icon style="float: right" @click="nuevoProspecto()">
                                    mdi-plus-circle
                                </v-icon>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col style="color: white; font-weight: bold;">
                                <div class="mx-2">Prospectos ({{ listaEmpresas.length }})</div>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>

                <v-row class="mt-4 mb-n6">
                    <v-col cols="3">
                        <v-autocomplete v-model="filtroRazonSocialEmpresas" :items="listaEmpresas" return-object
                            item-title="p_razon_social" item-value="id" label="Razón Social" variant="outlined"
                            clearable autocomplete="off" density="compact" @update:model-value="filtrarEmpresas()"
                            :readonly="filtroNitEmpresas || filtroFechaDesdeEmpresas" />
                    </v-col>

                    <v-col cols="3">
                        <v-autocomplete v-model="filtroNitEmpresas" :items="listaEmpresas" return-object :item-title="(item) =>
                            `${item.p_nit}` ? `${item.p_nit}` : 'No disponible'
                            " item-value="id" label="NIT" variant="outlined" clearable autocomplete="off"
                            density="compact" @update:model-value="filtrarEmpresas()" :readonly="filtroRazonSocialEmpresas || filtroFechaDesdeEmpresas
                                " />
                    </v-col>

                    <v-col cols="3">
                        <v-text-field v-model="filtroFechaDesdeEmpresas" label="Fecha de Creación Desde" type="date"
                            variant="outlined" clearable autocomplete="off" density="compact"
                            @update:model-value="filtrarEmpresas2()"
                            :readonly="filtroRazonSocialEmpresas || filtroNitEmpresas" />
                    </v-col>

                    <v-col cols="3">
                        <v-text-field v-model="filtroFechaHastaEmpresas" label="Fecha de Creación Hasta" type="date"
                            variant="outlined" clearable autocomplete="off" density="compact"
                            @update:model-value="filtrarEmpresas2()"
                            :readonly="filtroRazonSocialEmpresas || filtroNitEmpresas"
                            v-if="filtroFechaDesdeEmpresas" />
                    </v-col>
                </v-row>

                <v-card style="height: 80%; overflow-y: auto;" class="mt-4">
                    <v-row v-for="(fila, filaIndex) in filasEmpresas" :key="filaIndex" class="mb-4">
                        <v-col v-for="empresa in fila" :key="empresa.id">
                            <v-card @click="
                                cargarProspecto(empresa);
                            estaEditando = true;
                            " :class="{ 'empresa-card-activa pa-3 mb-2': empresa.p_activo == 1, 'empresa-card-inactiva pa-3 mb-2': empresa.p_activo != 1 }"
                                elevation="3">
                                <v-row align="center" no-gutters>
                                    <v-col cols="auto">
                                        <v-avatar color="#1976D2" size="44">
                                            <v-icon color="white" size="32">mdi-office-building</v-icon>
                                        </v-avatar>
                                    </v-col>
                                    <v-col>
                                        <div class="empresa-title font-weight-bold ml-2" style="
                            font-size: 1.25rem;
                            color: #0a1c3a;
                            white-space: normal;
                            word-break: break-word;
                          ">
                                            {{ empresa.p_razon_social }}
                                            <span v-if="empresa.p_activo != 1" style="float: right; font-size: 1rem;">🚫
                                                No
                                                autorizado</span>
                                        </div>

                                        <div class="empresa-nit ml-2 text-caption" style="
                            color: #1976d2;
                            font-weight: 500;
                            margin-top: 2px;
                          ">
                                            <span style="margin-right: 4px">NIT:</span>
                                            <span>{{ empresa.p_nit }}</span>
                                        </div>
                                    </v-col>
                                </v-row>
                                <v-divider class="my-2"></v-divider>
                                <v-row>
                                    <v-col cols="6">
                                        <div class="empresa-label text-caption" style="color: #666">
                                            Teléfono empresa
                                        </div>
                                        <div class="empresa-value font-weight-medium d-flex align-center"
                                            style="color: #222">
                                            <v-icon size="18" color="#1976D2" class="mr-1">mdi-phone</v-icon>
                                            <span class="contact-card-text">
                                                {{ empresa.p_telefono1 || "No disponible" }}</span>
                                        </div>
                                        <div class="empresa-label text-caption mt-1" style="color: #666">
                                            Celular contacto
                                        </div>
                                        <div class="empresa-value font-weight-medium d-flex align-center"
                                            style="color: #222">
                                            <v-icon size="18" color="#1976D2" class="mr-1">mdi-cellphone</v-icon>
                                            <span class="contact-card-text">
                                                {{ empresa.pc_celular || "No disponible" }}</span>
                                        </div>
                                    </v-col>
                                    <v-col cols="6">
                                        <div class="empresa-label text-caption" style="color: #666">
                                            Contacto
                                        </div>
                                        <div class="empresa-value font-weight-medium d-flex align-center"
                                            style="color: #222">
                                            <v-icon size="18" color="#1976D2" class="mr-1">mdi-account-tie</v-icon>
                                            <span :style="{
                                                whiteSpace: 'normal',
                                                wordBreak: 'break-word',
                                                fontSize:
                                                    (empresa.pc_nombre + ' ' + empresa.pc_apellido)
                                                        .length > 15
                                                        ? '0.8rem'
                                                        : '0.9rem',
                                                fontWeight: 'bold',
                                                color: '#222',
                                            }">{{ empresa.pc_nombre }}
                                                {{ empresa.pc_apellido }}</span>
                                        </div>
                                        <div class="empresa-label text-caption mt-1" style="color: #666">
                                            Usuario Asignado:
                                        </div>
                                        <div class="empresa-label text-caption" style="
                            color: #1976d2;
                            font-weight: 500;
                            margin-top: 2px;
                          ">
                                            <span>{{
                                                getNombreComercial(empresa.p_mercadeo)
                                            }}</span>
                                        </div>
                                    </v-col>
                                </v-row>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-card>

                <!----- Contenido Principal ----->

                <!----- Dialogo para crear/editar los prospectos ----->
                <v-dialog v-model="dialogCrearEditarProspecto" persistent width="70%">
                    <v-card style="height: 100%; border-radius: 20px">
                        <v-card-title class="text-h6"
                            style="color: white; font-weight: bold; background-color: #006ca1">
                            <div v-if="!idProspectoSeleccionado">
                                Crear Prospecto
                                <v-icon style="float: right" @click="guardarProspecto()" :disabled="dsGuardar"
                                    icon="mdi-content-save" size="small"></v-icon>
                            </div>
                            <div v-if="idProspectoSeleccionado">
                                Editar Prospecto
                                <v-icon style="float: right" @click="actualizarProspecto()" :disabled="dsGuardar"
                                    icon="mdi-content-save" size="small"></v-icon>
                            </div>
                        </v-card-title>
                        <v-card-text style="overflow-y: auto; height: 100%">
                            <v-row class="my-1">
                                <v-col>
                                    <h3 class="text-center mb-4" style="background-color: #006ca1; color: white">
                                        Información de la Empresa
                                    </h3>
                                    <v-alert v-if="alertaNit" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                                        this.mensajeAlertaNit }}</v-alert>

                                    <v-row>
                                        <v-col cols="11">
                                            <v-autocomplete v-model="comercialSeleccionado" :items="listaComerciales"
                                                item-title="nombre" item-value="id" label="Asignar Comercial"
                                                variant="outlined" clearable required :rules="[
                                                    (v) => !!v || 'Debes seleccionar un comercial',
                                                ]" autocomplete="off" prepend-inner-icon="mdi-account-tie"
                                                class="mx-5 ml-5 mb-n2"></v-autocomplete>
                                        </v-col>
                                        <v-col cols="11">
                                            <input class="campo-input mx-5 mb-5" list="empresas" id="empresa"
                                                v-model="nit" placeholder="NIT" autocomplete="off" />
                                        </v-col>
                                        <v-col style="margin-left: -30px">
                                            <v-icon class="mt-2" @click="nit = null">
                                                mdi-close-circle
                                            </v-icon>
                                        </v-col>
                                    </v-row>

                                    <datalist id="empresas">
                                        <option v-for="(empresa, index) in listaEmpresas" :key="empresa.id"
                                            :value="`${empresa.p_nit}`"></option>
                                    </datalist>

                                    <v-alert v-if="alertaRazonSocial" class="mx-5 mb-5" type="error"
                                        icon="mdi-account-alert">{{
                                            this.mensajeAlertaRazonSocial }}</v-alert>
                                    <v-row>
                                        <v-col cols="11">
                                            <input class="campo-input mx-5 mb-5" list="empresas2" id="empresa"
                                                v-model="razonSocial" placeholder="Razón Social" autocomplete="off" />
                                        </v-col>
                                        <v-col style="margin-left: -30px">
                                            <v-icon class="mt-2" @click="razonSocial = null">
                                                mdi-close-circle
                                            </v-icon>
                                        </v-col>
                                    </v-row>

                                    <datalist id="empresas2">
                                        <option v-for="(empresa, index) in listaEmpresas2" :key="empresa.id"
                                            :value="`${empresa.p_razon_social}`"></option>
                                    </datalist>
                                    <v-row>
                                        <v-col>
                                            <v-select class="ml-5" v-model="tipoId" :items="tipoIdentificacion"
                                                return-object item-title="nombre" item-value="id"
                                                label="Tipo Identificación" variant="outlined" clearable
                                                autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1"
                                                        style="opacity: 100%">mdi-card-account-details</v-icon>
                                                </template>
                                            </v-select>
                                        </v-col>
                                        <v-col>
                                            <v-select disabled class="mr-5" v-model="tipoEmp" :items="tipoEmpresa"
                                                return-object item-title="nombre" item-value="id" label="Tipo Empresa"
                                                variant="outlined" clearable autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1" style="opacity: 100%">mdi-domain</v-icon>
                                                </template>
                                            </v-select>
                                        </v-col>
                                    </v-row>
                                    <v-select class="mx-5" v-model="sector" :items="sectorEmpresa" return-object
                                        item-title="nombre" item-value="id" label="Sector" variant="outlined" clearable
                                        autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#006CA1" style="opacity: 100%">mdi-office-building</v-icon>
                                        </template>
                                    </v-select>
                                    <v-text-field class="mx-5" v-model="direccion" label="Dirección" type="text"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#006CA1" style="opacity: 100%">mdi-map-marker</v-icon>
                                        </template>
                                    </v-text-field>
                                    <v-row>
                                        <v-col>
                                            <v-autocomplete class="ml-5" v-model="departamento" :items="departamentos"
                                                return-object item-title="nombre" item-value="id" label="Departamento"
                                                variant="outlined" clearable autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1" style="opacity: 100%">mdi-home-city</v-icon>
                                                </template>
                                            </v-autocomplete>
                                        </v-col>
                                        <v-col>
                                            <v-autocomplete class="mr-5" v-model="ciudad" :items="ciudades"
                                                return-object item-title="nombre" item-value="id" label="Ciudad"
                                                variant="outlined" clearable autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1"
                                                        style="opacity: 100%">mdi-city-variant</v-icon>
                                                </template>
                                            </v-autocomplete>
                                        </v-col>
                                    </v-row>
                                    <v-text-field class="mx-5" v-model="web" label="Pagina Web" type="text"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#006CA1" style="opacity: 100%">mdi-web-box</v-icon>
                                        </template>
                                    </v-text-field>
                                    <v-text-field class="mx-5" v-model="correoEmpresa" label="Mail Empresa" type="text"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#006CA1" style="opacity: 100%">mdi-email</v-icon>
                                        </template>
                                    </v-text-field>
                                    <v-row>
                                        <v-col>
                                            <v-text-field class="ml-5" @input="filterTel1" :rules="[maxlength2].flat()"
                                                v-model="tel1" label="Telefono 1" type="number" variant="outlined"
                                                clearable autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1" style="opacity: 100%">mdi-cellphone</v-icon>
                                                </template>
                                            </v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field class="mr-5" v-model="tel2" label="Telefono 2" type="number"
                                                variant="outlined" clearable autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1" style="opacity: 100%">mdi-phone</v-icon>
                                                </template>
                                            </v-text-field>
                                        </v-col>
                                    </v-row>

                                    <v-row>
                                        <v-col class="mt-n5" cols="4">
                                            <v-checkbox class="ml-5 mt-10" v-model="activoProspecto" label="¿Activo?"
                                                color="#006CA1" :true-value="1" :false-value="0"></v-checkbox>
                                        </v-col>
                                        <v-col class="mt-n5" cols="8">
                                            <v-textarea class="mr-5" v-model="comentarioActivoInactivo"
                                                label="Comentarios Activo/Inactivo" color="#006CA1" variant="outlined"
                                                clearable autocomplete="off"></v-textarea>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <v-btn @click="verComentarios()" color="#006CA1"
                                                variant="outlined">Historial
                                                Comentarios
                                            </v-btn>
                                        </v-col>
                                    </v-row>
                                    <!-- Diálogo para historial de comentarios -->
                                    <v-dialog v-model="dialogComentarios" max-width="600px" persistent>
                                        <v-card style="border-radius: 16px; overflow: hidden;">
                                            <v-card-title class="text-h6"
                                                style="background-color: #006ca1; color: white; font-weight: bold;">
                                                <v-icon class="mr-2">mdi-comment-multiple-outline</v-icon>
                                                Historial de Comentarios
                                            </v-card-title>
                                            <v-card-text
                                                style="background: #f5f7fa; max-height: 350px; overflow-y: auto;">
                                                <v-timeline dense>
                                                    <v-timeline-item v-for="(comentario, idx) in comentariosHistorial"
                                                        :key="idx" color="#1976D2" small>
                                                        <template v-slot:opposite>
                                                            <span style="font-size: 0.85rem; color: #888;">{{
                                                                comentario.fecha_original }}</span>
                                                        </template>
                                                        <v-card elevation="2"
                                                            style="padding: 10px; border-radius: 10px;">
                                                            <div style="font-weight: bold; color: #1976D2;">{{
                                                                comentario.nombre_usuario }}</div>
                                                            <div style="color: #222; margin-top: 4px;">{{
                                                                comentario.texto_original }}
                                                            </div>
                                                        </v-card>
                                                    </v-timeline-item>
                                                </v-timeline>
                                                <div v-if="comentariosHistorial.length === 0" class="text-center"
                                                    style="color: #888; margin-top: 20px;">
                                                    No hay comentarios registrados.
                                                </div>
                                            </v-card-text>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn color="#006CA1" variant="flat" @click="dialogComentarios = false"
                                                    style="border-radius: 20px;">Cerrar</v-btn>
                                            </v-card-actions>
                                        </v-card>
                                    </v-dialog>
                                </v-col>
                                <v-col style="border-left: 1px solid #ccc; padding-left: 20px">
                                    <h3 class="text-center mb-4" style="background-color: #006ca1; color: white">
                                        Información del Contacto
                                    </h3>
                                    <v-text-field class="mx-5" v-model="nombre" label="Nombre" type="text"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#006CA1" style="opacity: 100%">mdi-rename</v-icon>
                                        </template>
                                    </v-text-field>
                                    <v-text-field class="mx-5" v-model="apellido" label="Apellido" type="text"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#006CA1" style="opacity: 100%">mdi-rename</v-icon>
                                        </template>
                                    </v-text-field>
                                    <v-row>
                                        <v-col>
                                            <v-autocomplete class="mx-5" v-model="categoria" :items="categorias"
                                                return-object item-title="nombre" item-value="id"
                                                label="Categoria Cargo" variant="outlined" clearable autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1"
                                                        style="opacity: 100%">mdi-format-list-bulleted-type</v-icon>
                                                </template>
                                            </v-autocomplete>
                                        </v-col>
                                        <v-col>
                                            <v-autocomplete class="mx-5" v-model="cargo" :items="cargos" return-object
                                                item-title="nombre" item-value="id" label="Cargo" type="text"
                                                variant="outlined" clearable autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1"
                                                        style="opacity: 100%">mdi-account-tie</v-icon>
                                                </template>
                                            </v-autocomplete>
                                        </v-col>
                                    </v-row>
                                    <v-text-field class="mx-5" v-model="correoContacto" label="Correo" type="text"
                                        variant="outlined" clearable autocomplete="off">
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#006CA1" style="opacity: 100%">mdi-email</v-icon>
                                        </template>
                                    </v-text-field>
                                    <v-row>
                                        <v-col cols="3" class="m-0">
                                            <v-text-field class="ml-5 mr-n4" v-model="extension" label="Extensión"
                                                type="number" variant="outlined" autocomplete="off">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1" style="opacity: 100%">mdi-numeric</v-icon>
                                                </template>
                                            </v-text-field>
                                        </v-col>
                                        <v-col cols="9">
                                            <v-text-field class="mr-5 ml-4" v-model="celular" label="Celular"
                                                type="number" variant="outlined" autocomplete="off"
                                                @input="filterNumber" :rules="[rules.required, rules.phoneMax12]">
                                                <template v-slot:prepend-inner>
                                                    <v-icon color="#006CA1" style="opacity: 100%">mdi-cellphone</v-icon>
                                                </template>
                                            </v-text-field>
                                        </v-col>
                                    </v-row>
                                    <v-alert v-if="alertaCelular" class="mx-5 mb-5" type="error"
                                        icon="mdi-account-alert">{{
                                            this.mensajeAlertaCelular }}</v-alert>
                                </v-col>
                            </v-row>
                        </v-card-text>

                        <v-card-actions>
                            <v-btn @click="
                                dialogCrearEditarProspecto = false;
                            dialogProspectos = true;
                            limpiarCamposProspecto();
                            " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
                <!----- Dialogo para crear/editar los prospectos ----->

                <!----- Dialogo para las alertas ----->
                <v-dialog v-model="alerta" persistent style="z-index: 10000">
                    <v-card :style="getAlertStyle()">
                        <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
                            class="mx-auto"></v-progress-circular>
                        <v-card-tittle v-text="mensajeAlertLogin"
                            style="color: black; text-align: center"></v-card-tittle>
                        <v-btn class="mt-4 mx-auto" @click="cerrarDIV()" :readonly="ifCargando" style="
                border-radius: 20px;
                color: black;
                background-color: rgb(188, 209, 255);
                margin: 0 auto;
                display: block;
              ">Cerrar</v-btn>
                    </v-card>
                </v-dialog>
                <!----- Dialogo para las alertas ----->

                <v-dialog v-model="dialogCambioClave" persistent max-width="400px">
                    <v-card-title class="text-h6" style="background-color: #006ca1; color: white">
                        <v-icon class="mr-2">mdi mdi-pen-lock</v-icon>
                        Cambiar Clave
                    </v-card-title>
                    <v-card class="pa-4">
                        <v-card-text>
                            <v-text-field v-model="claveActual" label="Clave Actual"
                                :type="mostrarClaveActual ? 'text' : 'password'" variant="outlined" required clearable>
                                <template v-slot:append-inner>
                                    <v-icon :icon="mostrarClaveActual ? 'mdi-eye' : 'mdi-eye-closed'"
                                        @click="mostrarClaveActual = !mostrarClaveActual" />
                                </template>
                            </v-text-field>
                            <v-text-field v-model="nuevaClave" label="Nueva Clave"
                                :type="mostrarNuevaClave ? 'text' : 'password'" variant="outlined" required clearable>
                                <template v-slot:append-inner>
                                    <v-icon :icon="mostrarNuevaClave ? 'mdi-eye' : 'mdi-eye-closed'"
                                        @click="mostrarNuevaClave = !mostrarNuevaClave" />
                                </template>
                            </v-text-field>
                            <div class="text-caption mt-n4 mb-4" style="color: red"
                                v-if="nuevaClave && !isValidPassword(nuevaClave)">
                                La nueva clave debe tener al menos una mayúscula, un número, un
                                caracter especial y mínimo 8 caracteres.
                            </div>
                            <v-text-field v-model="confirmarClave" label="Confirmar Nueva Clave"
                                :type="mostrarConfirmarClave ? 'text' : 'password'" variant="outlined" required
                                clearable>
                                <template v-slot:append-inner>
                                    <v-icon :icon="mostrarConfirmarClave ? 'mdi-eye' : 'mdi-eye-closed'"
                                        @click="mostrarConfirmarClave = !mostrarConfirmarClave" />
                                </template>
                            </v-text-field>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn variant="flat" color="#006CA1" @click="cambiarClave()">Guardar</v-btn>
                            <v-btn variant="flat" color="grey" @click="
                                dialogCambioClave = false;
                            claveActual = null;
                            nuevaClave = null;
                            confirmarClave = null;
                            ">Cancelar</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
import axios from "axios";
import CryptoJS from "crypto-js";
import AppHeader from '../components/AppHeader.vue';

export default {
    components: {
        AppHeader,
    },
    data: () => ({
        baseURL: "",
        comercialId: localStorage.getItem("idUsuario"),
        nombreComercial:
            localStorage.getItem("nombreLogin") +
            " " +
            localStorage.getItem("apellidoLogin"),
        imagenComercial: null,

        listaEmpresas: [],
        listaEmpresas2: [],
        listaEmpresasFiltradas: [],

        listaUsuarios: [],
        listaUsuariosFiltrados: [],

        listaUbicaciones: [],
        listaCiudades: [],

        listaSectores: [],

        listaCargos: [],
        listaCargosxCat: [],

        listaEstadosC: [],

        listaPrioridades: [],

        listaProductos: [],

        listaComerciales: [],

        alerta: false,
        mensajeAlertLogin: "",

        ifCargando: false,
        drawer: false,

        filtroRazonSocialEmpresas: null,
        filtroNitEmpresas: null,
        filtroFechaDesdeEmpresas: null,
        filtroFechaHastaEmpresas: null,
        mensajeAlertaRazonSocial: "",
        alertaNit: false,
        mensajeAlertaNit: "",
        alertaRazonSocial: false,
        alertaCelular: false,
        mensajeAlertaCelular: "",
        nombre: null,
        apellido: null,
        categoria: null,
        categorias: [],
        cargo: null,
        cargos: [],
        correoContacto: null,
        celular: "573",
        extension: "57",
        empresa: null,
        nit: null,
        razonSocial: null,
        tipoId: null,
        tipoIdentificacion: [],
        tipoEmp: null,
        tipoEmpresa: [],
        sector: null,
        sectorEmpresa: [],
        direccion: null,
        departamento: null,
        departamentos: [],
        ciudad: null,
        ciudades: [],
        web: null,
        correoEmpresa: null,
        tel1: "57",
        tel2: null,

        filtroNombreUsuarios: null,
        filtroCedulaUsuario: null,
        filtroCelularUsuario: null,
        nombreUsu: null,
        apellidosUsu: null,
        cedulaUsu: null,
        emailUsu: null,
        cuentaUsu: null,
        metaUsuario: 0,
        celularUsu: null,
        perfilUsu: null,
        perfilesUsu: [],
        activoUsu: true,
        contraseñaUsu: false,

        filtroUbicaciones: null,

        filtroSectores: null,

        filtroCargos: null,

        filtroEstadosC: null,

        filtroPrioridades: null,

        filtroProductos: null,

        idProspectoSeleccionado: null,
        idUsuarioSeleccionado: null,
        idUsuario: null,
        idCargo: null,

        dialogUsuarios: false,
        dialogProspectos: false,
        dialogCampañas: false,
        dialogPQRS: false,
        dialogUbicacion: false,
        dialogSector: false,
        dialogCargos: false,
        dialogEstadosC: false,
        dialogPrioridades: false,
        dialogProductos: false,
        dialogCrearEditarProspecto: false,
        dialogCrearEditarUsuario: false,
        dialogValorProyectos: false,

        dialogCambioClave: false,
        claveActual: null,
        nuevaClave: null,
        confirmarClave: null,
        mostrarClaveActual: false,
        mostrarNuevaClave: false,
        mostrarConfirmarClave: false,

        // creado por leo - inicio
        nombreSector: null,
        mostrarNombreSector: false,
        mostrarSaveSector: false,
        mostrarEditSector: false,
        mostrarSelectSector: true,
        nuevoSector: false,
        labelNombreSector: "Por favor, edita el Nombre del Sector",
        labelTituloSector: "Editar Nombre del Sector",
        mensajeError: "",
        estadoSector: true, // Estado del sector, por defecto activo
        mostrarEstadoSector: true, // Mostrar el switch de estado del sector
        // creado por leo - fin

        nombreProducto: null,
        mostrarNombreProducto: false,
        mostrarSaveProducto: false,
        mostrarEditProducto: false,
        mostrarSelectProducto: true,
        nuevoProducto: false,
        labelNombreProducto: "Por favor, edita el Nombre del Producto",
        labelTituloProducto: "Editar Nombre del Producto",
        mensajeErrorProducto: "",
        estadoProducto: true, // Estado del producto, por defecto activo
        mostrarEstadoProducto: true, // Mostrar el switch de estado del producto
        archivoProducto: null,
        descripcionProducto: null,
        urlArchivo: null,

        nombreEstadosC: null,
        mostrarNombreEstadosC: false,
        mostrarSaveEstadosC: false,
        mostrarEditEstadosC: false,
        mostrarSelectEstadosC: true,
        nuevoEstadoC: false,
        labelNombreEstadosC: "Por favor, edita el Nombre del Estado Comercial",
        labelTituloEstadosC: "Editar Nombre del Estado Comercial",
        mensajeErrorEstadosC: "",
        estadoEstadosC: true, // Estado del estado comercial, por defecto activo
        mostrarEstadoEstadosC: true, // Mostrar el switch de estado del estado comercial

        nombrePrioridades: null,
        mostrarNombrePrioridades: false,
        mostrarSavePrioridades: false,
        mostrarEditPrioridades: false,
        mostrarSelectPrioridades: true,
        nuevoPrioridad: false,
        labelNombrePrioridades: "Por favor, edita el Nombre de la Prioridad",
        labelTituloPrioridades: "Editar Nombre de la Prioridad",
        mensajeErrorPrioridades: "",
        estadoPrioridades: true, // Estado de la prioridad, por defecto activo
        mostrarEstadoPrioridades: true, // Mostrar el switch de estado de la prioridad

        selectedDepartamento: null,
        selectedCiudad: null,

        ifbtnGuardarCargo: false,
        ifbtnEditarCargo: true,
        nuevaCategoriaCargo: null,
        nuevoCargo: null,
        nuevoNombreCategoria: null,
        nuevoNombreCategoriaEdit: null,
        nuevoNombreCargo: null,
        nuevoNombreCargoEdit: null,

        ifbtnEditarUbicacion: true,
        ifbtnGuardarUbicacion: false,
        nuevoDepartamento: null,
        nuevoNombreDepartamentoEdit: null,
        nuevoNombreCiudadEdit: null,
        nuevaCiudad: null,
        nuevoNombreDepartamento: null,
        nuevaDepartamentoCiudad: null,
        nuevoNombreCiudad: null,

        selectedComercial: null,
        selectedProyecto: null,
        valorProyectoSeleccionado: 0,
        listaProyectos: [],

        estaEditando: false,
        esElMismoNombrecomercial: false,
        nitOriginal: null,
        razonOriginal: null,

        menuActivo: "",
        comentarioActivoInactivo: null,

        dialogComentarios: false,
        comentariosHistorial: [],

        listaComerciales: [],
        comercialSeleccionado: null,
        rules: {
            required: (v) => String(v ?? "").trim().length > 0 || "Requerido",

            // Teléfono: máximo 12 dígitos (ej: 57 + 10)
            phoneMax12: (v) => {
                const s = String(v ?? "");
                if (!s) return true; // permite vacío si no usas 'required'
                const digits = s.replace(/\D/g, ""); // cuenta solo dígitos
                return digits.length <= 12 || "Máximo 12 dígitos";
            },

            // Ejemplo genérico de "máximo 12 caracteres" (no solo dígitos)

            maxLen12: (v) => {
                const s = String(v ?? "");
                if (!s) return true;
                return s.length <= 12 || "Máximo 12 caracteres";
            },
        },
        activoProspecto: null,
    }),

    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL; // URL base de la API
        this.imagenComercial = this.baseURL + "images/" + this.comercialId + ".jpeg";
        this.idUsuario = localStorage.getItem("idUsuario");
        this.idCargo = localStorage.getItem("idCargo");
        this.llamadoComerciales();

        this.limpiarCamposProspecto();
        this.obtenerEmpresas();
        this.llamadoCategorias();
        this.llamadoTipoIdentificacion();
        this.llamadoTipoEmpresa();
        this.llamadoSectores();
        this.llamadoDepartamentos();
    },
    watch: {
        categoria(newValue) {
            this.llamadoCargos(newValue ? newValue.id : 0);
        },

        tipoId(newVal) {
            if (!newVal) return;

            if (newVal.nombre === "NIT") {
                this.tipoEmp = this.tipoEmpresa.find(
                    (item) => item.nombre === "Jurídica"
                );
            } else {
                this.tipoEmp = this.tipoEmpresa.find(
                    (item) => item.nombre === "Natural"
                );
            }
        },

        departamento(newValue) {
            this.llamadoCiudades(newValue ? newValue.id : 0);
        },

        razonSocial(newRazonSocial) {
            this.validarRazonSocialUnificado(newRazonSocial);
        },

        nit(newNit) {
            this.validarNitUnificado(newNit);
        },

        celular(newCelular) {
            this.validarCelular(newCelular);
        },

        // creado por leo
        filtroSectores(newFiltro) {
            this.cargarDatosSector(newFiltro);
        },

        filtroProductos(newFiltro) {
            this.cargarDatosProducto(newFiltro);
        },

        filtroEstadosC(newFiltro) {
            this.cargarDatosEstadosC(newFiltro);
        },
        filtroPrioridades(newFiltro) {
            this.cargarDatosPrioridades(newFiltro);
        },

        // creado por leo
        nuevoSector(nuevoValor) {
            this.labelNombreSector = nuevoValor
                ? "Por favor, digita el Nombre del Sector a crear"
                : "Por favor, edita el Nombre del Sector";
        },

        nuevoProducto(nuevoValor) {
            this.labelNombreProducto = nuevoValor
                ? "Por favor, digita el Nombre del Producto a crear"
                : "Por favor, edita el Nombre del Producto";
        },

        nuevoEstadoC(nuevoValor) {
            this.labelNombreEstadosC = nuevoValor
                ? "Por favor, digita el Nombre del Estado Comercial a crear"
                : "Por favor, edita el Nombre del Estado Comercial";
        },

        nuevoPrioridad(nuevoValor) {
            this.labelNombrePrioridades = nuevoValor
                ? "Por favor, digita el Nombre de la Prioridad a crear"
                : "Por favor, edita el Nombre de la Prioridad";
        },

        nuevaCategoriaCargo(newValue) {
            if (newValue) {
                this.nuevoNombreCategoriaEdit = newValue.nombre;
            } else {
                this.nuevoNombreCategoriaEdit = null;
            }
        },

        nuevoCargo(newValue) {
            if (newValue) {
                this.nuevoNombreCargoEdit = newValue.nombre;
            } else {
                this.nuevoNombreCargoEdit = null;
            }
        },

        nuevoDepartamento(newValue) {
            if (newValue) {
                this.nuevoNombreDepartamentoEdit = newValue.nombre;
            } else {
                this.nuevoNombreDepartamentoEdit = null;
            }
        },

        nuevaCiudad(newValue) {
            if (newValue) {
                this.nuevoNombreCiudadEdit = newValue.nombre;
            } else {
                this.nuevoNombreCiudadEdit = null;
            }
        },

        selectedProyecto(newValue) {
            if (newValue) {
                this.valorProyectoSeleccionado = newValue.valor_proyecto;
            } else {
                this.valorProyectoSeleccionado = null;
            }
        },
    },

    computed: {
        filasEmpresas() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaEmpresas.length; i += columnas) {
                filas.push(this.listaEmpresas.slice(i, i + columnas));
            }
            return filas;
        },

        filasUsuarios() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaUsuarios.length; i += columnas) {
                filas.push(this.listaUsuarios.slice(i, i + columnas));
            }
            return filas;
        },

        filasUbicaciones() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaUbicaciones.length; i += columnas) {
                filas.push(this.listaUbicaciones.slice(i, i + columnas));
            }
            return filas;
        },

        filasSectores() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaSectores.length; i += columnas) {
                filas.push(this.listaSectores.slice(i, i + columnas));
            }
            return filas;
        },

        filasCargos() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaCargos.length; i += columnas) {
                filas.push(this.listaCargos.slice(i, i + columnas));
            }
            return filas;
        },

        filasEstadosC() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaEstadosC.length; i += columnas) {
                filas.push(this.listaEstadosC.slice(i, i + columnas));
            }
            return filas;
        },

        filasPrioridades() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaPrioridades.length; i += columnas) {
                filas.push(
                    this.listarlistaPrioridadesPrioridades.slice(i, i + columnas)
                );
            }
            return filas;
        },

        filasProductos() {
            const columnas = 3;
            const filas = [];
            for (let i = 0; i < this.listaProductos.length; i += columnas) {
                filas.push(this.listaProductos.slice(i, i + columnas));
            }
            return filas;
        },

        dsGuardar() {
            return this.alertaNit || this.alertaRazonSocial || this.alertaCelular;
        },
    },
    methods: {

        verComentarios() {
            this.dialogComentarios = true;
        },



        // creado por leo
        cargarDatosSector(filtroSectores) {
            if (filtroSectores) {
                this.nombreSector = filtroSectores.nombre;
                this.mostrarNombreSector = true;
                this.mostrarSaveSector = false;
                this.mostrarEditSector = true;
            } else {
                this.nombreSector = "";
                if (this.nuevoSector) {
                    this.mostrarSelectSector = false;
                    this.mostrarNombreSector = true;
                    this.mostrarSaveSector = true;
                    this.mostrarEditSector = false;
                } else {
                    this.mostrarSelectSector = true;
                    this.mostrarNombreSector = false;
                    this.mostrarSaveSector = false;
                    this.mostrarEditSector = false;
                }
            }
        },

        cargarDatosProducto(filtroProductos) {
            if (filtroProductos) {
                console.log("Cargar datos del producto:", filtroProductos);
                this.nombreProducto = filtroProductos.nombre;
                this.descripcionProducto = filtroProductos.detalle;
                this.urlArchivo = filtroProductos.url_archivo;
                this.mostrarNombreProducto = true;
                this.mostrarSaveProducto = false;
                this.mostrarEditProducto = true;
            } else {
                this.nombreProducto = "";
                if (this.nuevoProducto) {
                    this.mostrarSelectProducto = false;
                    this.mostrarNombreProducto = true;
                    this.mostrarSaveProducto = true;
                    this.mostrarEditProducto = false;
                } else {
                    this.mostrarSelectProducto = true;
                    this.mostrarNombreProducto = false;
                    this.mostrarSaveProducto = false;
                    this.mostrarEditProducto = false;
                }
            }
        },

        cargarDatosEstadosC(filtroEstadosC) {
            if (filtroEstadosC) {
                this.nombreEstadosC = filtroEstadosC.nombre;
                this.mostrarNombreEstadosC = true;
                this.mostrarSaveEstadosC = false;
                this.mostrarEditEstadosC = true;
            } else {
                this.nombreEstadosC = "";
                if (this.nuevoEstadoC) {
                    this.mostrarSelectEstadosC = false;
                    this.mostrarNombreEstadosC = true;
                    this.mostrarSaveEstadosC = true;
                    this.mostrarEditEstadosC = false;
                } else {
                    this.mostrarSelectEstadosC = true;
                    this.mostrarNombreEstadosC = false;
                    this.mostrarSaveEstadosC = false;
                    this.mostrarEditEstadosC = false;
                }
            }
        },

        cargarDatosPrioridades(filtroPrioridades) {
            if (filtroPrioridades) {
                this.nombrePrioridades = filtroPrioridades.nombre;
                this.mostrarNombrePrioridades = true;
                this.mostrarSavePrioridades = false;
                this.mostrarEditPrioridades = true;
            } else {
                this.nombrePrioridades = "";
                if (this.nuevoPrioridad) {
                    this.mostrarSelectPrioridades = false;
                    this.mostrarNombrePrioridades = true;
                    this.mostrarSavePrioridades = true;
                    this.mostrarEditPrioridades = false;
                } else {
                    this.mostrarSelectPrioridades = true;
                    this.mostrarNombrePrioridades = false;
                    this.mostrarSavePrioridades = false;
                    this.mostrarEditPrioridades = false;
                }
            }
        },

        // creado por leo
        selNuevoSector() {
            this.mensajeError = "";
            this.nuevoSector = true;
            this.mostrarSelectSector = false;
            this.mostrarNombreSector = true;
            this.mostrarSaveSector = true;
            this.mostrarEditSector = false;
            this.nombreSector = "";
            this.labelTituloSector = "Nuevo Sector";
            this.filtroSectores = null;
        },

        selNuevoProducto() {
            this.mensajeErrorProducto = "";
            this.nuevoProducto = true;
            this.mostrarSelectProducto = false;
            this.mostrarNombreProducto = true;
            this.mostrarSaveProducto = true;
            this.mostrarEditProducto = false;
            this.nombreProducto = null;
            this.descripcionProducto = null;
            this.urlArchivo = null;
            this.archivoProducto = null;
            this.labelTituloProducto = "Nuevo Producto";
            this.filtroProductos = null;
        },

        selNuevoEstadoC() {
            this.mensajeErrorEstadosC = "";
            this.nuevoEstadoC = true;
            this.mostrarSelectEstadosC = false;
            this.mostrarNombreEstadosC = true;
            this.mostrarSaveEstadosC = true;
            this.mostrarEditEstadosC = false;
            this.nombreEstadosC = "";
            this.labelTituloEstadosC = "Nuevo Estado Comercial";
            this.filtroEstadosC = null;
        },

        selNuevoPrioridad() {
            this.mensajeErrorPrioridades = "";
            this.nuevoPrioridad = true;
            this.mostrarSelectPrioridades = false;
            this.mostrarNombrePrioridades = true;
            this.mostrarSavePrioridades = true;
            this.mostrarEditPrioridades = false;
            this.nombrePrioridades = "";
            this.labelTituloPrioridades = "Nueva Prioridad";
            this.filtroPrioridades = null;
        },

        // creado por leo
        selEditarSector() {
            if (this.nuevoSector) {
                this.mensajeError = "";
                this.nuevoSector = false;
                this.filtroSectores = null;
                this.mostrarSelectSector = true;
                this.mostrarNombreSector = false;
                this.mostrarSaveSector = false;
                this.mostrarEditSector = true;
                this.labelTituloSector = "Editar Nombre del Sector";
            }
        },

        selEditarProducto() {
            if (this.nuevoProducto) {
                this.mensajeErrorProducto = null;
                this.descripcionProducto = null;
                this.urlArchivo = null;
                this.archivoProducto = null;
                this.nuevoProducto = false;
                this.filtroProductos = null;
                this.mostrarSelectProducto = true;
                this.mostrarNombreProducto = false;
                this.mostrarSaveProducto = false;
                this.mostrarEditProducto = true;
                this.labelTituloProducto = "Editar Nombre del Producto";
            }
        },

        selEditarEstadoC() {
            if (this.nuevoEstadoC) {
                this.mensajeErrorEstadosC = "";
                this.nuevoEstadoC = false;
                this.filtroEstadosC = null;
                this.mostrarSelectEstadosC = true;
                this.mostrarNombreEstadosC = false;
                this.mostrarSaveEstadosC = false;
                this.mostrarEditEstadosC = true;
                this.labelTituloEstadosC = "Editar Nombre del Estado Comercial";
            }
        },

        selEditarPrioridad() {
            if (this.nuevoPrioridad) {
                this.mensajeErrorPrioridades = "";
                this.nuevoPrioridad = false;
                this.filtroPrioridades = null;
                this.mostrarSelectPrioridades = true;
                this.mostrarNombrePrioridades = false;
                this.mostrarSavePrioridades = false;
                this.mostrarEditPrioridades = true;
                this.labelTituloPrioridades = "Editar Nombre de la Prioridad";
            }
        },

        // creado por leo
        save_sector(tiposavesector) {
            var tiposavesector = tiposavesector || 0; // Por defecto, si no se pasa un tipo, se considera nuevo (0)
            this.mensajeError = "";

            // Aquí puedes implementar la lógica para guardar el sector
            if (!this.nombreSector) {
                this.mensajeAlertLogin = "El nombre del sector es obligatorio";
                this.alerta = true;
                return;
            }

            // Verificar si el nombre del sector ya existe - Cuando es nuevo
            const nombreIngresado = this.nombreSector.toLowerCase().trim();
            const existe = (this.listaSectores || []).some((sector) => {
                const nombreEnLista = (sector?.nombre || "").toLowerCase().trim();
                return nombreEnLista === nombreIngresado;
            });
            if (tiposavesector === 0 && existe) {
                this.mensajeError =
                    "Ese nombre del sector ya existe. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Verificar si el nombre del sector ya existe - Cuando es editar
            const existeEnOtro = (this.listaSectores || []).some((sector) => {
                const nombreSectorLista = (sector?.nombre || "").toLowerCase().trim();
                return (
                    nombreSectorLista === nombreIngresado &&
                    sector.id !== this.idSectorActual // ❗️excluir el actual
                );
            });
            if (tiposavesector === 1 && existeEnOtro) {
                this.mensajeError =
                    "Ese nombre del sector ya existe con otro id. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Aquí puedes implementar la lógica para guardar el sector
            console.log(
                "Guardando sector:",
                this.nombreSector,
                "Tipo:",
                tiposavesector,
                "ID:",
                this.filtroSectores ? this.filtroSectores.id : 0
            );
            axios
                .post(this.baseURL + "api/saveSector", {
                    nombre: this.nombreSector,
                    id: this.filtroSectores ? this.filtroSectores.id : 0,
                    tipo: tiposavesector,
                })
                .then((response) => {
                    if (response.data.data) {
                        if (tiposavesector > 0) {
                            this.mensajeAlertLogin = "Sector creado correctamente";
                        } else {
                            this.mensajeAlertLogin = "Sector editado correctamente";
                        }
                        this.alerta = true;
                        this.dialogSector = false;
                        this.nuevoSector = false;
                        this.mostrarSelectSector = true;
                        this.mostrarNombreSector = false;
                        this.mostrarSaveSector = false;
                        this.nombreSector = "";
                        this.mostrarEditSector = false;

                        axios
                            .post(this.baseURL + "api/cargaSector", {
                                id: 0,
                            })
                            .then((response) => {
                                this.listaSectores = response.data.data;
                            })
                            .catch((error) => {
                                console.log(error);
                            });
                    } else {
                        if (tiposavesector > 0) {
                            this.mensajeAlertLogin = "Error al crear el sector";
                        } else {
                            this.mensajeAlertLogin = "Error al editar el sector";
                        }
                        this.alerta = true;
                    }
                })
                .catch((error) => {
                    console.error("Error al editar el sector:", error);
                    this.mensajeAlertLogin = "Error al editar el sector";
                    this.alerta = true;
                });
        },

        save_cargos(tiposave) {
            const nombreCatEdit = this.nuevoNombreCategoriaEdit
                ? this.nuevoNombreCategoriaEdit
                : "";
            const nombreCat = this.nuevoNombreCategoria
                ? this.nuevoNombreCategoria
                : "";
            const idCat = this.nuevaCategoriaCargo ? this.nuevaCategoriaCargo.id : 0;
            const nombreCargo = this.nuevoNombreCargo ? this.nuevoNombreCargo : "";
            const nombreCargoEdit = this.nuevoNombreCargoEdit
                ? this.nuevoNombreCargoEdit
                : "";
            const idCargo = this.nuevoCargo ? this.nuevoCargo.id : 0;
            let tipoCreate = 0;
            let tipoEdit = 0;
            let errorCount = 0;

            // Validaciones para editar
            if (tiposave == 1) {
                if (idCat == 0) {
                    this.mensajeAlertLogin = "Debe seleccionar una categoria de cargo";
                    this.alerta = true;
                    errorCount++;
                    return;
                } else {
                    // Validar que el nombre ingresado para la categoria no esté vacio
                    if (nombreCatEdit.trim() === "") {
                        this.mensajeAlertLogin =
                            "El nombre de la categoria no puede estar vacío";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }

                    // Validar si el nombre ingresado para la categoria ya existe en listaCargos
                    this.listaCargos.forEach((cargo) => {
                        console.log(
                            "Validando categoria:",
                            cargo.nombre,
                            "con nombreCat:",
                            nombreCatEdit
                        );
                        if (
                            cargo.nombre == nombreCatEdit.trim() &&
                            nombreCargoEdit.trim() == ""
                        ) {
                            this.mensajeAlertLogin = "El nombre de la categoria ya existe";
                            this.alerta = true;
                            errorCount++;
                            return;
                        }
                    });

                    // Validar que el nombre a editar ingresado para el cargo no esté vacio
                    if (nombreCargoEdit.trim() === "" && idCargo != 0) {
                        this.mensajeAlertLogin = "El nombre del cargo no puede estar vacío";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }

                    // Validar si el nombre a editar ingresado para el cargo ya existe en listaCargosxCat
                    this.listaCargosxCat.forEach((cargo) => {
                        console.log(
                            "Validando cargo:",
                            cargo.nombre,
                            "con nombreCargo:",
                            nombreCargo
                        );
                        if (cargo.nombre == nombreCargoEdit.trim()) {
                            this.mensajeAlertLogin = "El nombre del cargo ya existe";
                            this.alerta = true;
                            errorCount++;
                            return;
                        }
                    });

                    // Está editando categoria
                    if (idCat != 0 && nombreCatEdit.trim() !== "" && idCargo == 0) {
                        tipoEdit = 1; // Indica que se está editando una categoria
                    } else if (idCargo != 0 && nombreCargoEdit.trim() !== "") {
                        tipoEdit = 2; // Indica que se está editando un cargo para una categoria existente
                    }
                }
            } else if (tiposave == 0) {
                // Validaciones para crear

                // Validar que el nombre ingresado para la categoria no esté vacio
                if (nombreCat.trim() === "" && idCat == 0) {
                    this.mensajeAlertLogin =
                        "El nombre de la categoria no puede estar vacío";
                    this.alerta = true;
                    errorCount++;
                    return;
                }

                // Validar que el nombre ingresado para la categoria no exista en listaCargos
                this.listaCargos.forEach((cargo) => {
                    if (cargo.nombre == nombreCat.trim()) {
                        this.mensajeAlertLogin = "El nombre de la categoria ya existe";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }
                });

                //validar que la categoria seleccionada no esté vacia
                if (idCat == 0 && nombreCat.trim() === "") {
                    this.mensajeAlertLogin = "Debe seleccionar una categoria de cargo";
                    this.alerta = true;
                    errorCount++;
                    return;
                }

                // Validar que el nombre ingresado para el cargo no esté vacio
                if (nombreCargo.trim() === "" && nombreCat.trim() === "") {
                    this.mensajeAlertLogin = "El nombre del cargo no puede estar vacío";
                    this.alerta = true;
                    errorCount++;
                    return;
                }

                // Validar si el nombre a editar ingresado para el cargo ya existe en listaCargosxCat
                this.listaCargosxCat.forEach((cargo) => {
                    console.log(
                        "Validando cargo:",
                        cargo.nombre,
                        "con nombreCargo:",
                        nombreCargo
                    );
                    if (cargo.nombre == nombreCargo.trim()) {
                        this.mensajeAlertLogin = "El nombre del cargo ya existe";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }
                });

                // Está creando nueva categoria
                if (nombreCat.trim() !== "" && idCat == 0) {
                    tipoCreate = 1; // Indica que se está creando una nueva categoria
                } else if (nombreCat.trim() === "" && idCat != 0) {
                    tipoCreate = 2; // Indica que se está creando un nuevo cargo para una categoria existente
                }
            }

            if (errorCount > 0) {
                return; // Si hay errores, no continuar con el guardado
            } else {
                axios
                    .post(this.baseURL + "api/saveCargo", {
                        // Globales
                        tipo: tiposave,
                        idCat: idCat,
                        idCargo: idCargo,
                        tipoEdit: tipoEdit,
                        tipoCreate: tipoCreate,
                        // Edit
                        nombreCatEdit: nombreCatEdit,
                        nombreCargoEdit: nombreCargoEdit,
                        // Crear
                        nombreCat: nombreCat,
                        nombreCargo: nombreCargo,
                    })
                    .then((response) => {
                        if (response.data.data) {
                            if (tiposave > 0) {
                                this.mensajeAlertLogin =
                                    "Categoría o Cargo editados correctamente";
                            } else {
                                this.mensajeAlertLogin =
                                    "Categoría o Cargo creados correctamente";
                            }
                            this.alerta = true;
                            this.dialogCargos = false;
                            this.ifbtnGuardarCargo = false;
                            this.ifbtnEditarCargo = true;
                            this.nuevaCategoriaCargo = null;
                            this.nuevoCargo = null;
                            this.nuevoNombreCategoria = null;
                            this.nuevoNombreCategoriaEdit = null;
                            this.nuevoNombreCargo = null;
                            this.nuevoNombreCargoEdit = null;
                        } else {
                            if (tiposave > 0) {
                                this.mensajeAlertLogin = "Error al editar la categoría o cargo";
                            } else {
                                this.mensajeAlertLogin = "Error al crear la categoría o cargo";
                            }
                            this.alerta = true;
                        }
                    })
                    .catch((error) => {
                        console.error("Error al guardar el cargo:", error);
                        this.mensajeAlertLogin = "Error al guardar el cargo";
                        this.alerta = true;
                    });
            }
        },

        save_ubicacion(tiposave) {
            const idDeptoEdit = this.nuevoDepartamento
                ? this.nuevoDepartamento.id
                : 0;
            const nombreDeptoEdit = this.nuevoNombreDepartamentoEdit
                ? this.nuevoNombreDepartamentoEdit
                : "";
            const idCiudad = this.nuevaCiudad ? this.nuevaCiudad.id : 0;
            const nombreCiudadEdit = this.nuevoNombreCiudadEdit
                ? this.nuevoNombreCiudadEdit
                : "";
            const nombreDepto = this.nuevoNombreDepartamento
                ? this.nuevoNombreDepartamento
                : "";
            const idDepto = this.nuevaDepartamentoCiudad
                ? this.nuevaDepartamentoCiudad.id
                : 0;
            const nombreCiudad = this.nuevoNombreCiudad ? this.nuevoNombreCiudad : "";
            let tipoCreate = 0;
            let tipoEdit = 0;
            let errorCount = 0;

            // Validaciones para editar
            if (tiposave == 1) {
                if (idDeptoEdit == 0 && nombreDeptoEdit.trim() === "") {
                    this.mensajeAlertLogin = "Debe seleccionar un departamento";
                    this.alerta = true;
                    errorCount++;
                    return;
                } else {
                    // Validar que el nombre ingresado para el departamento no esté vacio
                    if (nombreDeptoEdit.trim() === "") {
                        this.mensajeAlertLogin =
                            "El nombre del departamento no puede estar vacío";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }

                    // Validar si el nombre ingresado para el departamento ya existe en listaUbicaciones
                    this.listaUbicaciones.forEach((depto) => {
                        console.log(
                            "Validando departamento:",
                            depto.nombre,
                            "con nombreDepto:",
                            nombreDeptoEdit
                        );
                        if (
                            depto.nombre == nombreDeptoEdit.trim() &&
                            nombreCiudadEdit.trim() == ""
                        ) {
                            this.mensajeAlertLogin = "El nombre del departamento ya existe";
                            this.alerta = true;
                            errorCount++;
                            return;
                        }
                    });

                    // Validar que el nombre a editar ingresado para la ciudad no esté vacio
                    if (nombreCiudadEdit.trim() === "" && idCiudad != 0) {
                        this.mensajeAlertLogin =
                            "El nombre de la ciudad no puede estar vacío";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }

                    // Validar si el nombre a editar ingresado para la ciudad ya existe en listaUbicaciones
                    this.listaCiudades.forEach((ciudad) => {
                        console.log(
                            "Validando ciudad:",
                            ciudad.nombre,
                            "con nombreCiudad:",
                            nombreCiudad
                        );
                        if (ciudad.nombre == nombreCiudadEdit.trim()) {
                            this.mensajeAlertLogin = "El nombre de la ciudad ya existe";
                            this.alerta = true;
                            errorCount++;
                            return;
                        }
                    });

                    // Está editando departamento
                    if (
                        idDeptoEdit != 0 &&
                        nombreDeptoEdit.trim() !== "" &&
                        idCiudad == 0
                    ) {
                        tipoEdit = 1; // Indica que se está editando un departamento
                    } else if (idCiudad != 0 && nombreCiudadEdit.trim() !== "") {
                        tipoEdit = 2; // Indica que se está editando una ciudad para un departamento existente
                    }
                }
            } else if (tiposave == 0) {
                // Validaciones para crear

                // Validar que el nombre ingresado para el departamento no esté vacio
                if (nombreDepto.trim() === "" && idDepto == 0) {
                    this.mensajeAlertLogin =
                        "El nombre del departamento no puede estar vacío";
                    this.alerta = true;
                    errorCount++;
                    return;
                }

                // Validar que el nombre ingresado para el departamento no exista en listaUbicaciones
                this.listaUbicaciones.forEach((depto) => {
                    if (depto.nombre == nombreDepto.trim()) {
                        this.mensajeAlertLogin = "El nombre del departamento ya existe";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }
                });

                //validar que el departamento seleccionado no esté vacio
                if (idDepto == 0 && nombreDepto.trim() === "") {
                    this.mensajeAlertLogin = "Debe seleccionar un departamento";
                    this.alerta = true;
                    errorCount++;
                    return;
                }

                // Validar que el nombre ingresado para la ciudad no esté vacio
                if (
                    nombreCiudad.trim() === "" &&
                    idCiudad == 0 &&
                    nombreDepto.trim() === ""
                ) {
                    this.mensajeAlertLogin =
                        "El nombre de la ciudad no puede estar vacío";
                    this.alerta = true;
                    errorCount++;
                    return;
                }

                // Validar que el nombre ingresado para la ciudad no exista en listaCiudades
                this.listaCiudades.forEach((ciudad) => {
                    if (ciudad.nombre == nombreCiudad.trim()) {
                        this.mensajeAlertLogin = "El nombre de la ciudad ya existe";
                        this.alerta = true;
                        errorCount++;
                        return;
                    }
                });

                // Está creando nuevo departamento
                if (nombreDepto.trim() !== "" && idDepto == 0) {
                    tipoCreate = 1; // Indica que se está creando un nuevo departamento
                } else if (nombreDepto.trim() === "" && idDepto != 0) {
                    tipoCreate = 2; // Indica que se está creando una nueva ciudad para un departamento existente
                }
            }

            if (errorCount > 0) {
                return; // Si hay errores, no continuar con el guardado
            } else {
                axios
                    .post(this.baseURL + "api/saveUbicacion", {
                        // Globales
                        tipo: tiposave,
                        idDeptoEdit: idDeptoEdit,
                        idDepto: idDepto,
                        idCiudad: idCiudad,
                        tipoEdit: tipoEdit,
                        tipoCreate: tipoCreate,
                        // Edit
                        nombreDeptoEdit: nombreDeptoEdit,
                        nombreCiudadEdit: nombreCiudadEdit,
                        // Crear
                        nombreDepto: nombreDepto,
                        nombreCiudad: nombreCiudad,
                    })
                    .then((response) => {
                        if (response.data.data) {
                            if (tiposave > 0) {
                                this.mensajeAlertLogin =
                                    "Departamento o Ciudad editados correctamente";
                            } else {
                                this.mensajeAlertLogin =
                                    "Departamento o Ciudad creados correctamente";
                            }
                            this.alerta = true;
                            this.dialogUbicacion = false;
                            this.ifbtnGuardarUbicacion = false;
                            this.ifbtnEditarUbicacion = true;
                            this.limpiarCamposUbicacion();
                        } else {
                            if (tiposave > 0) {
                                this.mensajeAlertLogin =
                                    "Error al editar el departamento o ciudad";
                            } else {
                                this.mensajeAlertLogin =
                                    "Error al crear el departamento o ciudad";
                            }
                            this.alerta = true;
                        }
                    })
                    .catch((error) => {
                        console.error("Error al guardar el departamento o ciudad:", error);
                        this.mensajeAlertLogin =
                            "Error al guardar el departamento o ciudad";
                        this.alerta = true;
                    });
            }
        },

        save_producto(tiposaveproducto) {
            var tiposaveproducto = tiposaveproducto || 0; // Por defecto, si no se pasa un tipo, se considera nuevo (0)
            this.mensajeErrorProducto = "";

            // Aquí puedes implementar la lógica para guardar el producto
            if (!this.nombreProducto) {
                this.mensajeAlertLogin = "El nombre del producto es obligatorio";
                this.alerta = true;
                return;
            }

            // Verificar si el nombre del producto ya existe - Cuando es nuevo
            const nombreIngresado = this.nombreProducto.toLowerCase().trim();
            const existe = (this.listaProductos || []).some((producto) => {
                const nombreEnLista = (producto?.nombre || "").toLowerCase().trim();
                return nombreEnLista === nombreIngresado;
            });
            if (tiposaveproducto === 0 && existe) {
                this.mensajeErrorProducto =
                    "Ese nombre del producto ya existe. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Verificar si el nombre del producto ya existe - Cuando es editar
            const existeEnOtro = (this.listaProductos || []).some((producto) => {
                const nombreProductoLista = (producto?.nombre || "")
                    .toLowerCase()
                    .trim();
                return (
                    nombreProductoLista === nombreIngresado &&
                    producto.id !== this.idProductoActual // ❗️excluir el actual
                );
            });
            if (tiposaveproducto === 1 && existeEnOtro) {
                this.mensajeErrorProducto =
                    "Ese nombre del producto ya existe con otro id. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Aquí puedes implementar la lógica para guardar el producto
            console.log(
                "Guardando producto:",
                this.nombreProducto,
                "Tipo:",
                tiposaveproducto,
                "ID:",
                this.filtroProductos ? this.filtroProductos.id : 0
            );

            let formData = new FormData();
            formData.append("ficha_tecnica", this.archivoProducto);

            this.mensajeAlertLogin = "Guardando producto...";
            this.alerta = true;
            this.ifCargando = true;

            axios
                .post(this.baseURL + "api/saveProducto", {
                    nombre: this.nombreProducto,
                    id: this.filtroProductos ? this.filtroProductos.id : 0,
                    tipo: tiposaveproducto,
                    descripcion: this.descripcionProducto ? this.descripcionProducto : "",
                })
                .then((response) => {
                    if (response.data.data) {
                        formData.append("id", response.data.data[0].id);

                        if (this.archivoProducto) {
                            axios
                                .post(this.baseURL + "api/uploadFichaTecnica", formData, {
                                    headers: {
                                        "Content-Type": "multipart/form-data",
                                    },
                                })
                                .then((response) => {
                                    if (response.data.data) {
                                        if (tiposaveproducto > 0) {
                                            this.mensajeAlertLogin =
                                                "Producto con ficha técnica creado correctamente";
                                            this.alerta = true;
                                            this.ifCargando = false;
                                        } else {
                                            this.mensajeAlertLogin =
                                                "Producto con ficha técnica editado correctamente";
                                            this.alerta = true;
                                            this.ifCargando = false;
                                        }
                                    } else {
                                        this.mensajeAlertLogin = "Error al subir la ficha técnica";
                                        this.alerta = true;
                                        this.ifCargando = false;
                                    }
                                })
                                .catch((error) => {
                                    console.log(error);
                                });
                        } else {
                            if (tiposaveproducto > 0) {
                                this.mensajeAlertLogin = "Producto creado correctamente";
                                this.alerta = true;
                                this.ifCargando = false;
                            } else {
                                this.mensajeAlertLogin = "Producto editado correctamente";
                                this.alerta = true;
                                this.ifCargando = false;
                            }
                        }

                        this.dialogProductos = false;
                        this.nuevoProducto = false;
                        this.mostrarSelectProducto = true;
                        this.mostrarNombreProducto = false;
                        this.mostrarSaveProducto = false;
                        this.nombreProducto = null;
                        this.descripcionProducto = null;
                        this.urlArchivo = null;
                        this.archivoProducto = null;
                        this.mostrarEditProducto = false;
                        axios
                            .post(this.baseURL + "api/cargaProducto", {
                                id: 0,
                            })
                            .then((response) => {
                                this.listaProductos = response.data.data;
                            })
                            .catch((error) => {
                                console.log(error);
                            });
                    } else {
                        if (tiposaveproducto > 0) {
                            this.mensajeAlertLogin = "Error al crear el producto";
                            this.alerta = true;
                            this.ifCargando = false;
                        } else {
                            this.mensajeAlertLogin = "Error al editar el producto";
                            this.alerta = true;
                            this.ifCargando = false;
                        }
                    }
                })
                .catch((error) => {
                    console.error("Error al editar el producto:", error);
                    this.mensajeAlertLogin = "Error al editar el producto";
                    this.alerta = true;
                    this.ifCargando = false;
                });
        },

        save_estados_c(tiposaveestado) {
            var tiposaveestado = tiposaveestado || 0; // Por defecto, si no se pasa un tipo, se considera nuevo (0)
            this.mensajeErrorEstadosC = "";

            // Aquí puedes implementar la lógica para guardar el estado comercial
            if (!this.nombreEstadosC) {
                this.mensajeAlertLogin =
                    "El nombre del estado comercial es obligatorio";
                this.alerta = true;
                return;
            }

            // Verificar si el nombre del estado comercial ya existe - Cuando es nuevo
            const nombreIngresado = this.nombreEstadosC.toLowerCase().trim();
            const existe = (this.listaEstadosC || []).some((estado) => {
                const nombreEnLista = (estado?.nombre || "").toLowerCase().trim();
                return nombreEnLista === nombreIngresado;
            });
            if (tiposaveestado === 0 && existe) {
                this.mensajeErrorEstadosC =
                    "Ese nombre del estado comercial ya existe. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Verificar si el nombre del estado comercial ya existe - Cuando es editar
            const existeEnOtro = (this.listaEstadosC || []).some((estado) => {
                const nombreEstadoLista = (estado?.nombre || "").toLowerCase().trim();
                return (
                    nombreEstadoLista === nombreIngresado &&
                    estado.id !== this.idEstadoActual // ❗️excluir el actual
                );
            });
            if (tiposaveestado === 1 && existeEnOtro) {
                this.mensajeErrorEstadosC =
                    "Ese nombre del estado comercial ya existe con otro id. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Aquí puedes implementar la lógica para guardar el estado comercial
            console.log(
                "Guardando estado comercial:",
                this.nombreEstadosC,
                "Tipo:",
                tiposaveestado,
                "ID:",
                this.filtroEstadosC ? this.filtroEstadosC.id : 0
            );
            axios
                .post(this.baseURL + "api/saveEstadoComercial", {
                    nombre: this.nombreEstadosC,
                    id: this.filtroEstadosC ? this.filtroEstadosC.id : 0,
                    tipo: tiposaveestado,
                })
                .then((response) => {
                    if (response.data.data) {
                        if (tiposaveestado > 0) {
                            this.mensajeAlertLogin = "Estado Comercial creado correctamente";
                        } else {
                            this.mensajeAlertLogin = "Estado Comercial editado correctamente";
                        }
                        this.alerta = true;
                        this.dialogEstadosC = false;
                        this.nuevoEstadoC = false;
                        this.mostrarSelectEstadosC = true;
                        this.mostrarNombreEstadosC = false;
                        this.mostrarSaveEstadosC = false;
                        this.nombreEstadosC = "";
                        this.mostrarEditEstadosC = false;
                        axios
                            .post(this.baseURL + "api/cargaEstadoComercial", {
                                id: 0,
                            })
                            .then((response) => {
                                this.listaEstadosC = response.data.data;
                            })
                            .catch((error) => {
                                console.log(error);
                            });
                    } else {
                        if (tiposaveestado > 0) {
                            this.mensajeAlertLogin = "Error al crear el estado comercial";
                        } else {
                            this.mensajeAlertLogin = "Error al editar el estado comercial";
                        }
                        this.alerta = true;
                    }
                })
                .catch((error) => {
                    console.error("Error al editar el estado comercial:", error);
                    this.mensajeAlertLogin = "Error al editar el estado comercial";
                    this.alerta = true;
                });
        },

        save_prioridades(tiposaveprioridad) {
            var tiposaveprioridad = tiposaveprioridad || 0; // Por defecto, si no se pasa un tipo, se considera nuevo (0)
            this.mensajeErrorPrioridades = "";

            // Aquí puedes implementar la lógica para guardar la prioridad
            if (!this.nombrePrioridades) {
                this.mensajeAlertLogin = "El nombre de la prioridad es obligatorio";
                this.alerta = true;
                return;
            }

            // Verificar si el nombre de la prioridad ya existe - Cuando es nuevo
            const nombreIngresado = this.nombrePrioridades.toLowerCase().trim();
            const existe = (this.listaPrioridades || []).some((prioridad) => {
                const nombreEnLista = (prioridad?.nombre || "").toLowerCase().trim();
                return nombreEnLista === nombreIngresado;
            });
            if (tiposaveprioridad === 0 && existe) {
                this.mensajeErrorPrioridades =
                    "Ese nombre de la prioridad ya existe. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Verificar si el nombre de la prioridad ya existe - Cuando es editar
            const existeEnOtro = (this.listaPrioridades || []).some((prioridad) => {
                const nombrePrioridadLista = (prioridad?.nombre || "")
                    .toLowerCase()
                    .trim();
                return (
                    nombrePrioridadLista === nombreIngresado &&
                    prioridad.id !== this.idPrioridadActual // ❗️excluir el actual
                );
            });
            if (tiposaveprioridad === 1 && existeEnOtro) {
                this.mensajeErrorPrioridades =
                    "Ese nombre de la prioridad ya existe con otro id. Por favor pruebe nuevamente con un nombre distinto";
                return;
            }

            // Aquí puedes implementar la lógica para guardar la prioridad
            console.log(
                "Guardando prioridad:",
                this.nombrePrioridades,
                "Tipo:",
                tiposaveprioridad,
                "ID:",
                this.filtroPrioridades ? this.filtroPrioridades.id : 0
            );
            axios
                .post(this.baseURL + "api/savePrioridad", {
                    nombre: this.nombrePrioridades,
                    id: this.filtroPrioridades ? this.filtroPrioridades.id : 0,
                    tipo: tiposaveprioridad,
                })
                .then((response) => {
                    if (response.data.data) {
                        if (tiposaveprioridad > 0) {
                            this.mensajeAlertLogin = "Prioridad creada correctamente";
                        } else {
                            this.mensajeAlertLogin = "Prioridad editada correctamente";
                        }
                        this.alerta = true;
                        this.dialogPrioridades = false;
                        this.nuevoPrioridad = false;
                        this.mostrarSelectPrioridades = true;
                        this.mostrarNombrePrioridades = false;
                        this.mostrarSavePrioridades = false;
                        this.nombrePrioridades = "";
                        this.mostrarEditPrioridades = false;
                        axios
                            .post(this.baseURL + "api/cargaPrioridad", {
                                id: 0,
                            })
                            .then((response) => {
                                this.listaPrioridades = response.data.data;
                            })
                            .catch((error) => {
                                console.log(error);
                            });
                    } else {
                        if (tiposaveprioridad > 0) {
                            this.mensajeAlertLogin = "Error al crear la prioridad";
                        } else {
                            this.mensajeAlertLogin = "Error al editar la prioridad";
                        }
                        this.alerta = true;
                    }
                })
                .catch((error) => {
                    console.error("Error al editar la prioridad:", error);
                    this.mensajeAlertLogin = "Error al editar la prioridad";
                    this.alerta = true;
                });
        },

        save_valor_proyecto() {
            if (!this.valorProyectoSeleccionado) {
                this.mensajeAlertLogin = "El valor del proyecto es obligatorio";
                this.alerta = true;
                return;
            }

            if (this.valorProyectoSeleccionado <= 0) {
                this.mensajeAlertLogin = "El valor del proyecto debe ser mayor a 0";
                this.alerta = true;
                return;
            }

            axios
                .post(this.baseURL + "api/saveValorProyecto", {
                    id: this.selectedProyecto.id,
                    valor_proyecto: this.valorProyectoSeleccionado,
                })
                .then((response) => {
                    if (response.data.data) {
                        this.mensajeAlertLogin =
                            "Valor del proyecto actualizado correctamente";
                        this.alerta = true;
                        this.valorProyectoSeleccionado = 0;
                        this.selectedProyecto = null;
                        this.selectedComercial = null;
                        this.dialogValorProyectos = false;
                    } else {
                        this.mensajeAlertLogin =
                            "Error al actualizar el valor del proyecto";
                        this.alerta = true;
                    }
                })
                .catch((error) => {
                    console.error("Error al actualizar el valor del proyecto:", error);
                    this.mensajeAlertLogin = "Error al actualizar el valor del proyecto";
                    this.alerta = true;
                });
        },

        filtrarUsuarios() {
            if (
                this.filtroNombreUsuarios &&
                !this.filtroCedulaUsuario &&
                !this.filtroCelularUsuario
            ) {
                this.listaUsuariosFiltrados = this.listaUsuarios;
                const nombreCompleto =
                    this.filtroNombreUsuarios.u_nom +
                    " " +
                    this.filtroNombreUsuarios.u_ape;

                this.listaUsuarios = this.listaUsuarios.filter((usuario) => {
                    const usuarioCompleto = usuario.u_nom + " " + usuario.u_ape;
                    return usuarioCompleto
                        .toLowerCase()
                        .includes(nombreCompleto.toLowerCase());
                });
                return;
            } else {
                if (this.listaUsuariosFiltrados.length > 0) {
                    this.listaUsuarios = this.listaUsuariosFiltrados;
                }
            }

            if (
                !this.filtroNombreUsuarios &&
                this.filtroCedulaUsuario &&
                !this.filtroCelularUsuario
            ) {
                this.listaUsuariosFiltrados = this.listaUsuarios;

                this.listaUsuarios = this.listaUsuarios.filter((usuario) => {
                    return usuario.u_ced
                        .toLowerCase()
                        .includes(this.filtroCedulaUsuario.u_ced.toLowerCase());
                });
                return;
            } else {
                if (this.listaUsuariosFiltrados.length > 0) {
                    this.listaUsuarios = this.listaUsuariosFiltrados;
                }
            }

            if (
                !this.filtroNombreUsuarios &&
                !this.filtroCedulaUsuario &&
                this.filtroCelularUsuario
            ) {
                this.listaUsuariosFiltrados = this.listaUsuarios;

                this.listaUsuarios = this.listaUsuarios.filter((usuario) => {
                    return usuario.u_cel
                        .toLowerCase()
                        .includes(this.filtroCelularUsuario.u_cel.toLowerCase());
                });
                return;
            } else {
                if (this.listaUsuariosFiltrados.length > 0) {
                    this.listaUsuarios = this.listaUsuariosFiltrados;
                }
            }
        },

        filtrarEmpresas() {
            if (
                this.filtroRazonSocialEmpresas &&
                !this.filtroNitEmpresas &&
                !this.filtroFechaDesdeEmpresas &&
                !this.filtroFechaHastaEmpresas
            ) {
                this.listaEmpresasFiltradas = this.listaEmpresas;
                const razonSocial = this.filtroRazonSocialEmpresas.p_razon_social;

                this.listaEmpresas = this.listaEmpresas.filter((empresa) => {
                    return empresa.p_razon_social
                        .toLowerCase()
                        .includes(razonSocial.toLowerCase());
                });
                return;
            } else {
                if (this.listaEmpresasFiltradas.length > 0) {
                    this.listaEmpresas = this.listaEmpresasFiltradas;
                }
            }

            if (
                !this.filtroRazonSocialEmpresas &&
                this.filtroNitEmpresas &&
                !this.filtroFechaDesdeEmpresas &&
                !this.filtroFechaHastaEmpresas
            ) {
                this.listaEmpresasFiltradas = this.listaEmpresas;
                const nit = this.filtroNitEmpresas.p_nit;

                this.listaEmpresas = this.listaEmpresas.filter((empresa) => {
                    return empresa.p_nit.toLowerCase().includes(nit.toLowerCase());
                });
                return;
            } else {
                if (this.listaEmpresasFiltradas.length > 0) {
                    this.listaEmpresas = this.listaEmpresasFiltradas;
                }
            }
        },

        filtrarEmpresas2() {
            if (!this.filtroRazonSocialEmpresas && !this.filtroNitEmpresas) {
                if (this.filtroFechaDesdeEmpresas && this.filtroFechaHastaEmpresas) {
                    this.listaEmpresasFiltradas = this.listaEmpresas;
                    const fechaDesde = this.filtroFechaDesdeEmpresas;
                    const fechaHasta = this.filtroFechaHastaEmpresas;

                    if (fechaDesde > fechaHasta) {
                        this.mensajeAlertLogin =
                            "La fecha de inicio no puede ser mayor que la fecha final";
                        this.alerta = true;
                        this.filtroFechaHastaEmpresas = null;
                        return;
                    }

                    this.listaEmpresas = this.listaEmpresas.filter((empresa) => {
                        //formatear empresa.p_fecha_sistema a fecha en formato YYYY-MM-DD
                        const fechaSistema = new Date(empresa.p_fecha_sistema);
                        const fechaDesdeObj = new Date(fechaDesde);
                        const fechaHastaObj = new Date(fechaHasta);
                        // Compara solo la fecha (sin hora)
                        return (
                            fechaSistema.toISOString().split("T")[0] >=
                            fechaDesdeObj.toISOString().split("T")[0] &&
                            fechaSistema.toISOString().split("T")[0] <=
                            fechaHastaObj.toISOString().split("T")[0]
                        );
                    });
                    return;
                } else {
                    if (this.listaEmpresasFiltradas.length > 0) {
                        this.listaEmpresas = this.listaEmpresasFiltradas;
                    }
                }
            }
        },

        obtenerEmpresas() {
            axios
                .post(this.baseURL + "api/cargarpp", {
                    idusu: this.idUsuario,
                })
                .then((response) => {
                    this.listaEmpresas = response.data.data;
                    this.listaEmpresas2 = response.data.data;
                    console.log("lista Empresas: ", this.listaEmpresas);
                })
                .catch((error) => {
                    console.error("Error al cargar empresas:", error);
                });
        },

        obtenerUsuarios() {
            axios
                .post(this.baseURL + "api/cargausus", {
                    idusu: 0,
                    tipo: 0, // 0 para cargar todos los usuarios
                })
                .then((response) => {
                    this.listaUsuarios = response.data.data;
                    console.log("Lista de Usuarios:", this.listaUsuarios);
                })
                .catch((error) => {
                    console.error("Error al cargar usuarios:", error);
                });
        },

        obtenerPerfilesUsu() {
            axios
                .post(this.baseURL + "api/cargaPerfiles")
                .then((response) => {
                    this.perfilesUsu = response.data.data;
                })
                .catch((error) => {
                    console.error("Error al cargar perfiles de usuario:", error);
                });
        },

        obtenerUbicaciones() {
            axios
                .post(this.baseURL + "api/cargaUbi", {
                    idusu: 0,
                })
                .then((response) => {
                    this.listaUbicaciones = response.data.data;
                })
                .catch((error) => {
                    console.error("Error al cargar las ubicaciones:", error);
                });
        },

        obtenerCargos() {
            axios
                .post(this.baseURL + "api/cargaCargos", {
                    idusu: 0,
                })
                .then((response) => {
                    this.listaCargos = response.data.data;
                })
                .catch((error) => {
                    console.error("Error al cargar los cargos:", error);
                });
        },

        cargarCiudades() {
            axios
                .post(this.baseURL + "api/cargaCiudades", {
                    idusu: 0,
                    depto: this.nuevoDepartamento ? this.nuevoDepartamento.id : 0,
                })
                .then((response) => {
                    this.nuevaCiudad = null;
                    this.listaCiudades = response.data.data;
                })
                .catch((error) => {
                    console.error("Error al cargar las ciudades:", error);
                });
        },

        cargarCargosxCat() {
            axios
                .post(this.baseURL + "api/cargaCargosxCat", {
                    idusu: 0,
                    cat: this.nuevaCategoriaCargo ? this.nuevaCategoriaCargo.id : 0,
                })
                .then((response) => {
                    this.nuevoCargo = null;
                    this.listaCargosxCat = response.data.data;
                })
                .catch((error) => {
                    console.error("Error al cargar los cargos:", error);
                });
        },

        cargarProspecto(empresa) {
            this.dialogProspectos = false;
            this.dialogCrearEditarProspecto = true;
            this.comercialSeleccionado = empresa.p_comercial || null;
            this.idProspectoSeleccionado = empresa.id;
            this.estaEditando = true;
            // Limpiar alertas al abrir prospecto para edición
            this.alertaNit = false;
            this.mensajeAlertaNit = "";
            this.alertaRazonSocial = false;
            this.mensajeAlertaRazonSocial = "";
            this.cargarHistorialComentarios(this.idProspectoSeleccionado);

            axios
                .post(this.baseURL + "api/cargaproscon", {
                    idprosp: empresa.id,
                })
                .then((response) => {
                    console.log("Prospecto cargado:", response.data);
                    this.nit = response.data.data[0].p_nit;
                    this.razonSocial = response.data.data[0].p_razon_social;
                    this.tipoId = this.tipoIdentificacion.find(
                        (item) => item.id == response.data.data[0].p_tipo_identif
                    );
                    this.sector = this.sectorEmpresa.find(
                        (item) => item.id == response.data.data[0].p_sector
                    );
                    this.direccion = response.data.data[0].p_direccion;
                    this.departamento = this.departamentos.find(
                        (item) => item.id == response.data.data[0].p_dpto
                    );
                    setTimeout(() => {
                        this.ciudad = this.ciudades.find(
                            (item) => item.id == response.data.data[0].p_ciudad
                        );
                    }, 1000);
                    this.web = response.data.data[0].p_web;
                    this.correoEmpresa = response.data.data[0].p_correo;
                    this.tel1 = response.data.data[0].p_telefono1;
                    this.tel2 = response.data.data[0].p_telefono2;

                    this.nombre = response.data.data[0].pc_nombre;
                    this.apellido = response.data.data[0].pc_apellido;
                    this.categoria = this.categorias.find(
                        (item) => item.id == response.data.data[0].pc_categoria
                    );
                    setTimeout(() => {
                        this.cargo = this.cargos.find(
                            (item) => item.id == response.data.data[0].pc_cargo
                        );
                    }, 1000);
                    this.correoContacto = response.data.data[0].pc_correo;
                    this.celular = response.data.data[0].pc_celular;
                    this.extension = response.data.data[0].pc_extension;
                    this.activoProspecto = response.data.data[0].p_activo;
                    this.comercialSeleccionado = this.listaComerciales.find(
                        (item) => item.id == response.data.data[0].p_mercadeo
                    );
                })
                .catch((error) => {
                    console.error("Error al cargar prospecto:", error);
                });
        },

        cargarHistorialComentarios(idProspecto){

            axios
                .post(this.baseURL + "api/historialActivoProspecto", {
                    idUsu: this.idUsuario,
                    idProspecto: idProspecto,
                })
                .then((response) => {
                    this.comentariosHistorial = response.data.data;
                    console.log("Historial de comentarios cargado:", this.comentariosHistorial);
                })
                .catch((error) => {
                    console.error("Error al cargar el historial de comentarios:", error);
                });

        },

        cargarUsuario(usuario) {
            this.dialogUsuarios = false;
            this.dialogCrearEditarUsuario = true;

            this.idUsuarioSeleccionado = usuario.u_id;

            axios
                .post(this.baseURL + "api/cargausus", {
                    idusu: usuario.u_id,
                    tipo: 0, // 0 para cargar un usuario específico
                })
                .then((response) => {
                    console.log("Usuario cargado:", response.data);
                    this.nombreUsu = response.data.data[0].u_nom;
                    this.apellidosUsu = response.data.data[0].u_ape;
                    this.cedulaUsu = response.data.data[0].u_ced;
                    this.emailUsu = response.data.data[0].u_ema;
                    this.cuentaUsu = response.data.data[0].u_cta;
                    this.metaUsuario = response.data.data[0].u_meta
                        ? response.data.data[0].u_meta
                        : 0;
                    this.activoUsu = response.data.data[0].u_act == 1 ? true : false;
                    this.celularUsu = response.data.data[0].u_cel;
                    this.idUsuarioSeleccionado = response.data.data[0].u_id;
                    this.perfilUsu = this.perfilesUsu.find(
                        (item) => item.id == response.data.data[0].u_cargo
                    );
                })
                .catch((error) => {
                    console.error("Error al cargar prospecto:", error);
                });
        },

        async actualizarUsuario() {
            this.mensajeAlertLogin = "Actualizando usuario...";
            this.alerta = true;
            this.ifCargando = true;

            await axios
                .post(this.baseURL + "api/editusu", {
                    nom: this.nombreUsu,
                    ape: this.apellidosUsu,
                    ced: this.cedulaUsu,
                    ema: this.emailUsu,
                    cue: this.cuentaUsu,
                    cel: this.celularUsu,
                    met: this.metaUsuario ? this.metaUsuario : 0,
                    sta: 0,
                    act: this.activoUsu ? 1 : 0,
                    idu: this.idUsuarioSeleccionado,
                    perfil: this.perfilUsu ? this.perfilUsu.id : 0,
                    clave: this.contraseñaUsu
                        ? CryptoJS.MD5(this.cedulaUsu).toString()
                        : "",
                })
                .then((response) => {
                    console.log("Usuario actualizado:", response.data);
                    this.ifCargando = false;
                    this.alerta = true;
                    this.mensajeAlertLogin = "Usuario actualizado correctamente";
                    setTimeout(() => {
                        this.obtenerUsuarios();
                        this.limpiarCamposUsuario();
                        this.dialogCrearEditarUsuario = false;
                        this.dialogUsuarios = true;
                    }, 1000);
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        async actualizarProspecto() {
            this.mensajeAlertLogin = "Actualizando prospecto...";
            this.alerta = true;
            this.ifCargando = true;
            console.log("Comercial Seleccionado: ", this.comercialSeleccionado);

            console.log("este es el sector", this.sector);

            if (!this.comercialSeleccionado) {
                this.ifCargando = false;
                this.mensajeAlertLogin =
                    "Debes seleccionar un comercial para asignar el prospecto.";
                this.alerta = true;
                return;
            }

            await axios
                .post(this.baseURL + "api/editprospecto", {
                    nit: this.nit,
                    razon_social: this.razonSocial,
                    tipo_identif: this.tipoId ? this.tipoId.id : 0,
                    tipo_emp: this.tipoEmp ? this.tipoEmp.id : 0,
                    sector: this.sector ? this.sector.id : 0,
                    direccion: this.direccion,
                    dpto: this.departamento ? this.departamento.id : 0,
                    ciudad: this.ciudad ? this.ciudad.id : 0,
                    web: this.web,
                    correo: this.correoEmpresa,
                    telefono1: this.tel1,
                    telefono2: this.tel2,
                    comercial: 0,
                    id: this.idProspectoSeleccionado,
                    activo: this.activoProspecto,
                    mercadeo: this.comercialSeleccionado
                })
                .then((response) => {
                    console.log("Prospecto actualizado:", response.data);
                })
                .catch((error) => {
                    console.log(error);
                });

            await axios
                .post(this.baseURL + "api/editprospectocontacto", {
                    nombre: this.nombre,
                    apellido: this.apellido,
                    categoria: this.categoria ? this.categoria.id : 0,
                    cargo: this.cargo ? this.cargo.id : 0,
                    correo: this.correoContacto,
                    celular: this.celular,
                    extension: this.extension,
                    id: this.idProspectoSeleccionado,
                })
                .then((response) => {
                    console.log("Prospecto actualizado:", response.data);
                    this.ifCargando = false;
                    this.alerta = true;
                    this.mensajeAlertLogin = "Prospecto actualizado correctamente";
                    setTimeout(() => {
                        this.guardarComentarios(this.idProspectoSeleccionado);
                        this.obtenerEmpresas();
                        this.limpiarCamposProspecto();
                        this.dialogCrearEditarProspecto = false;
                        this.dialogProspectos = true;
                    }, 1000);
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        async guardarUsuario() {
            this.mensajeAlertLogin = "Guardando usuario...";
            this.alerta = true;
            this.ifCargando = true;

            await axios
                .post(this.baseURL + "api/newusu", {
                    nom: this.nombreUsu,
                    ape: this.apellidosUsu,
                    ced: this.cedulaUsu,
                    ema: this.emailUsu,
                    cue: this.cuentaUsu,
                    cel: "57" + this.celularUsu,
                    met: this.metaUsuario ? this.metaUsuario : 0,
                    sta: 0,
                    act: this.activoUsu ? 1 : 0,
                    idu: this.idUsuarioSeleccionado,
                    perfil: this.perfilUsu ? this.perfilUsu.id : 0,
                    clave: CryptoJS.MD5(this.cedulaUsu).toString(),
                })
                .then((response) => {
                    console.log("Usuario creado:", response.data);
                    this.ifCargando = false;
                    this.alerta = true;
                    this.mensajeAlertLogin = "Usuario creado correctamente";
                    setTimeout(() => {
                        this.obtenerUsuarios();
                        this.limpiarCamposUsuario();
                        this.dialogCrearEditarUsuario = false;
                        this.dialogUsuarios = true;
                    }, 1000);
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        validarNitUnificado(nit) {
            let nitOriginal = null;
            if (
                this.idProspectoSeleccionado &&
                Array.isArray(this.listaEmpresasComercial)
            ) {
                const empresaActual = this.listaEmpresasComercial.find(
                    (e) => e.id === this.idProspectoSeleccionado
                );
                nitOriginal = empresaActual ? empresaActual.p_nit : null;
            }
            // Si está editando y el NIT es el mismo que el original, no mostrar alerta
            if (this.idProspectoSeleccionado && nit === nitOriginal) {
                this.alertaNit = false;
                this.mensajeAlertaNit = "";
                this.dsGuardar = false;
                return;
            }
            axios
                .post(this.baseURL + "api/validarnitraz", { nit: nit, raz: "" })
                .then(({ data }) => {
                    const row = data?.data?.[0];
                    if (!row) {
                        this.alertaNit = false;
                        this.mensajeAlertaNit = "";
                        this.dsGuardar = false;
                        return;
                    }
                    // Si está editando, solo mostrar aviso si el NIT ya existe en otra empresa (no importa el comercial)
                    if (this.idProspectoSeleccionado) {
                        // Si el NIT existe en otra empresa distinta a la que se está editando
                        if (row.id !== this.idProspectoSeleccionado) {
                            this.mensajeAlertaNit = "Ya existe una empresa con este NIT.";
                            this.alertaNit = true;
                            this.dsGuardar = true;
                        } else {
                            this.alertaNit = false;
                            this.mensajeAlertaNit = "";
                            this.dsGuardar = false;
                        }
                        return;
                    }
                    // Si está creando, mostrar aviso normal
                    if (
                        row.comercial &&
                        row.comercial.toLowerCase() ===
                        (this.nombreComercial || "").toLowerCase()
                    ) {
                        this.mensajeAlertaNit =
                            "Este NIT ya está registrado en tu cartera.";
                    } else {
                        this.mensajeAlertaNit = `Este NIT ya se encuentra asignado al comercial: ${row.comercial}`;
                    }
                    this.alertaNit = true;
                    this.dsGuardar = true;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        // Método unificado para validar Razón Social en crear/editar prospecto
        validarRazonSocialUnificado(newRazonSocial) {
            let razonOriginal = null;
            if (
                this.idProspectoSeleccionado &&
                Array.isArray(this.listaEmpresasComercial)
            ) {
                const empresaActual = this.listaEmpresasComercial.find(
                    (e) => e.id === this.idProspectoSeleccionado
                );
                razonOriginal = empresaActual ? empresaActual.p_razon_social : null;
            }
            // Si está editando y la razón social es la misma que la original, no mostrar alerta
            if (this.idProspectoSeleccionado && newRazonSocial === razonOriginal) {
                this.alertaRazonSocial = false;
                this.mensajeAlertaRazonSocial = "";
                this.dsGuardar = false;
                return;
            }
            axios
                .post(this.baseURL + "api/validarnitraz", {
                    nit: "",
                    raz: newRazonSocial,
                })
                .then(({ data }) => {
                    const row = data?.data?.[0];
                    if (!row) {
                        this.alertaRazonSocial = false;
                        this.mensajeAlertaRazonSocial = "";
                        this.dsGuardar = false;
                        return;
                    }
                    // Si está editando, solo mostrar aviso si la razón social ya existe en otra empresa
                    if (this.idProspectoSeleccionado) {
                        if (row.id !== this.idProspectoSeleccionado) {
                            this.mensajeAlertaRazonSocial =
                                "Ya existe una empresa con esta razón social.";
                            this.alertaRazonSocial = true;
                            this.dsGuardar = true;
                        } else {
                            this.alertaRazonSocial = false;
                            this.mensajeAlertaRazonSocial = "";
                            this.dsGuardar = false;
                        }
                        return;
                    }
                    // Si está creando, mostrar aviso normal
                    if (
                        row.comercial &&
                        row.comercial.toLowerCase() ===
                        (this.nombreComercial || "").toLowerCase()
                    ) {
                        this.mensajeAlertaRazonSocial =
                            "Esta razón social ya está registrada en tu cartera.";
                    } else {
                        this.mensajeAlertaRazonSocial = `Esta razón social ya se encuentra asignada al comercial: ${row.comercial}`;
                    }
                    this.alertaRazonSocial = true;
                    this.dsGuardar = true;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        validarCelular(newCelular) {
            const onlyDigits = (s) => String(s ?? "").replace(/\D/g, "");
            const last10 = (s) => onlyDigits(s).slice(-10);

            const entered10 = last10(newCelular);

            if (!entered10) {
                this.alertaCelular = false;
                this.mensajeAlertaCelular = "";
                if (typeof this._updateDsGuardar === "function")
                    this._updateDsGuardar(false);
                else this.dsGuardar = false;
                return;
            }

            const myId = String(this.idProspectoSeleccionado ?? "0");
            const poolsForId = [
                this.listaEmpresasComercial,
                this.listaEmpresas,
                this.listaEmpresasComercial2,
                this.listaEmpresas2,
            ].filter(Array.isArray);

            let myRecord = null;
            for (const arr of poolsForId) {
                const hit = arr.find((e) => String(e?.id) === myId);
                if (hit) {
                    myRecord = hit;
                    break;
                }
            }
            const myPhone10 = last10(
                myRecord?.pc_celular || myRecord?.p_telefono1 || myRecord?.p_telefono2
            );

            if (
                this.estaEditando &&
                myId !== "0" &&
                myPhone10 &&
                myPhone10 === entered10
            ) {
                this.alertaCelular = false;
                this.mensajeAlertaCelular = "";
                if (typeof this._updateDsGuardar === "function")
                    this._updateDsGuardar(false);
                else this.dsGuardar = false;
                return;
            }

            axios
                .post(this.baseURL + "api/validarcel", {
                    id: this.idProspectoSeleccionado ? this.idProspectoSeleccionado : 0,
                    cel: newCelular,
                })
                .then(({ data }) => {
                    console.log("Validando celular...", data);
                    const row = data?.data?.[0];

                    if (!row || String(row.res) !== "1") {
                        this.alertaCelular = false;
                        this.mensajeAlertaCelular = "";
                        if (typeof this._updateDsGuardar === "function")
                            this._updateDsGuardar(false);
                        else this.dsGuardar = false;
                        return;
                    }

                    // Si el API trae nombre_comercial, úsalo como nombre comercial
                    const nombreComercialApi = row.nombre_comercial;
                    console.log("NOMBRE COMERCIAL API");

                    // Buscar en listas locales a otro dueño del mismo número
                    const pools = [
                        this.listaEmpresasComercial,
                        this.listaEmpresas,
                        this.listaEmpresasComercial2,
                        this.listaEmpresas2,
                    ].filter(Array.isArray);

                    let match = null;
                    for (const arr of pools) {
                        const found = arr.find((e) => {
                            const phone10 = last10(
                                e?.pc_celular || e?.p_telefono1 || e?.p_telefono2
                            );
                            return phone10 && phone10 === entered10 && String(e?.id) !== myId;
                        });
                        if (found) {
                            match = found;
                            break;
                        }
                    }

                    if (match) {
                        const razon =
                            (match.p_razon_social || match.razon_social || "")
                                .toString()
                                .trim() || "no disponible";
                        const ownerRaw = nombreComercialApi.trim();

                        const mismoOwner = this._equalsName
                            ? this._equalsName(ownerRaw, this.nombreComercial)
                            : (ownerRaw || "").toLowerCase() ===
                            (this.nombreComercial || "").toLowerCase();

                        if (mismoOwner) {
                            this.alertaCelular = true;
                            this.mensajeAlertaCelular = `Este número ya está registrado en tu cartera: empresa: "${razon}".`;
                            this.dsGuardar = true;
                        } else {
                            this.alertaCelular = true;
                            this.mensajeAlertaCelular =
                                `Este número de celular ya se encuentra asignado al contacto de la empresa "${razon}", ` +
                                `manejado por el comercial: "${ownerRaw}" ".`;
                            this.dsGuardar = true;
                        }
                        return;
                    }

                    // Si el API dijo que existe pero no pude identificar dueño en memoria → usa nombre_comercial del API
                    if (nombreComercialApi) {
                        this.alertaCelular = true;
                        this.mensajeAlertaCelular = `Este número de celular ya se encuentra asignado al contacto: ${nombreComercialApi}.`;
                        this.dsGuardar = true;
                    } else {
                        this.alertaCelular = true;
                        this.mensajeAlertaCelular =
                            "Este número de celular ya se encuentra asignado a otro contacto.";
                        this.dsGuardar = true;
                    }
                })
                .catch((err) => {
                    console.log(err);
                    this.alertaCelular = false;
                    this.mensajeAlertaCelular = "";
                });
        },

        async guardarProspecto() {
            var contacto = false;
            // if (!this.nombre || !this.apellido || !this.cargo || !this.correoContacto || !this.celular || !this.extension) {
            // Valida los campos del contacto que son obligatorios
            if (!this.razonSocial) {
                this.mensajeAlertLogin =
                    "Por favor, digite la razón social de la empresa";
                this.alerta = true;
                return;
            } else if (!this.departamento) {
                this.mensajeAlertLogin =
                    "Por favor, seleccione el departamento de la empresa";
                this.alerta = true;
                return;
            } else if (!this.ciudad) {
                this.mensajeAlertLogin =
                    "Por favor, seleccione la ciudad de la empresa";
                this.alerta = true;
                return;
            }
            if (!this.comercialSeleccionado) {
                this.mensajeAlertLogin =
                    "Debes seleccionar un comercial para asignar el prospecto.";
                this.alerta = true;
                return;
            }
            console.log("tipoId:", this.tipoId ? this.tipoId.id : 0);
            console.log("url:" + this.baseURL);

            this.mensajeAlertLogin = "Guardando prospecto...";
            this.alerta = true;
            this.ifCargando = true;

            await axios
                .post(this.baseURL + "api/newprospecto", {
                    nit: this.nit,
                    razon_social: this.razonSocial,
                    tipo_identif: this.tipoId ? this.tipoId.id : 0,
                    tipo_emp: this.tipoEmp ? this.tipoEmp.id : 0,
                    sector: this.sector ? this.sector.id : 0,
                    direccion: this.direccion,
                    dpto: this.departamento ? this.departamento.id : 0,
                    ciudad: this.ciudad ? this.ciudad.id : 0,
                    web: this.web,
                    correo: this.correoEmpresa,
                    telefono1: this.tel1,
                    telefono2: this.tel2,
                    comercial: 0,
                    activo: this.activoProspecto,
                    mercadeo: this.comercialSeleccionado,
                })
                .then((response) => {
                    this.idEmpresa = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });

            if (this.nombre && !this.apellido) {
                this.mensajeAlertLogin = "Por favor, digite el apellido del contacto";
                this.alerta = true;
            } else if (!this.nombre && this.apellido) {
                this.mensajeAlertLogin = "Por favor, digite el nombre del contacto";
                this.alerta = true;
            } else if (this.nombre && this.apellido) {
                await axios
                    .post(this.baseURL + "api/newprospectocontacto", {
                        nombre: this.nombre,
                        apellido: this.apellido,
                        cargo: this.cargo ? this.cargo.id : 0,
                        correo: this.correoContacto,
                        celular: this.celular,
                        extension: this.extension,
                        idemp: this.idEmpresa[0].id,
                    })
                    .then((response) => {
                        contacto = true;
                        this.mensajeAlertLogin = "Prospecto creado exitosamente";
                        this.alerta = true;
                        this.ifCargando = false;
                        setTimeout(() => {
                            this.guardarComentarios(this.idEmpresa[0].id);
                            this.obtenerEmpresas();
                            this.limpiarCamposProspecto();
                            this.dialogCrearEditarProspecto = false;
                            this.dialogProspectos = true;
                        }, 1000);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
            if (!contacto) {
                this.mensajeAlertLogin = "Prospecto creado exitosamente";
                this.alerta = true;
                this.ifCargando = false;
                setTimeout(() => {
                    this.obtenerEmpresas();
                    this.limpiarCamposProspecto();
                    this.dialogCrearEditarProspecto = false;
                    this.dialogProspectos = true;
                }, 1000);
            }
        },

        guardarComentarios(idProspecto) {

            axios
                .post(this.baseURL + "api/comentariosActivoProspecto", {
                    idUsu: this.idUsuario,
                    comentarios: this.comentarioActivoInactivo,
                    idProspecto: idProspecto,
                    activo: this.activoProspecto,
                })
                .then((response) => {
                    console.log("Comentario guardado:", response.data);
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        limpiarCamposProspecto() {
            this.nit = null;
            this.razonSocial = null;
            this.tipoId = null;
            this.tipoEmp = null;
            this.sector = null;
            this.direccion = null;
            this.departamento = null;
            this.ciudad = null;
            this.web = null;
            this.correoEmpresa = null;
            this.tel1 = null;
            this.tel2 = null;

            this.nombre = null;
            this.apellido = null;
            this.categoria = null;
            this.cargo = null;
            this.correoContacto = null;
            this.celular = null;
            this.extension = null;

            this.idProspectoSeleccionado = null;
            this.alertaNit = false;
            this.mensajeAlertaNit = "";
            this.dsGuardar = false;

            this.alertaRazonSocial = false;
            this.mensajeAlertaRazonSocial = "";
            this.estaEditando = false;

            this.comentarioActivoInactivo = null;
        },

        limpiarCamposUsuario() {
            this.nombreUsu = null;
            this.apellidosUsu = null;
            this.cedulaUsu = null;
            this.emailUsu = null;
            this.cuentaUsu = null;
            this.metaUsuario = 0;
            this.celularUsu = null;
            this.activoUsu = true;

            this.idUsuarioSeleccionado = null;
        },

        limpiarCamposCargos() {
            this.nuevaCategoriaCargo = null;
            this.nuevoCargo = null;
            this.nuevoNombreCategoria = null;
            this.nuevoNombreCategoriaEdit = null;
            this.nuevoNombreCargo = null;
            this.nuevoNombreCargoEdit = null;
        },

        limpiarCamposUbicacion() {
            this.nuevoDepartamento = null;
            this.nuevoNombreDepartamentoEdit = null;
            this.nuevoNombreCiudadEdit = null;
            this.nuevaCiudad = null;
            this.nuevoNombreDepartamento = null;
            this.nuevaDepartamentoCiudad = null;
            this.nuevoNombreCiudad = null;
        },

        limpiarFiltrosUsuarios() {
            this.filtroNombreUsuarios = null;
            this.filtroCedulaUsuario = null;
            this.filtroCelularUsuario = null;

            if (this.listaUsuariosFiltrados.length > 0) {
                this.listaUsuarios = this.listaUsuariosFiltrados;
            } else {
                this.obtenerUsuarios();
            }
        },

        nuevoProspecto() {
            this.dialogProspectos = false;
            this.dialogCrearEditarProspecto = true;
            this.limpiarCamposProspecto();
        },

        abrirDialogUsuarios() {
            this.dialogUsuarios = true;
            this.obtenerUsuarios();
            this.obtenerPerfilesUsu();
        },

        nuevoUsuario() {
            this.dialogUsuarios = false;
            this.dialogCrearEditarUsuario = true;
            this.limpiarCamposUsuario();
        },

        abrirDialogUbicacion() {
            this.dialogUbicacion = true;
            this.obtenerUbicaciones();
        },

        // editado por leo
        abrirDialogSector() {
            this.nuevoSector = false;
            this.mostrarSelectSector = true;
            this.mostrarNombreSector = false;
            this.mostrarSaveSector = false;
            this.nombreSector = "";
            this.mostrarEditSector = false;

            axios
                .post(this.baseURL + "api/cargaSector", {
                    id: 0,
                })
                .then((response) => {
                    this.listaSectores = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.filtroSectores = null;
            this.dialogSector = true;
        },

        abrirDialogCargos() {
            this.dialogCargos = true;
            this.obtenerCargos();
        },

        abrirDialogEstadosC() {
            this.nuevoEstadoC = false;
            this.mostrarSelectEstadosC = true;
            this.mostrarNombreEstadosC = false;
            this.mostrarSaveEstadosC = false;
            this.nombreEstadosC = "";
            this.mostrarEditEstadosC = false;
            axios
                .post(this.baseURL + "api/cargaEstadoComercial", {
                    id: 0,
                })
                .then((response) => {
                    this.listaEstadosC = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.filtroEstadosC = null;
            this.dialogEstadosC = true;
        },

        abrirDialogPrioridades() {
            this.nuevoPrioridad = false;
            this.mostrarSelectPrioridades = true;
            this.mostrarNombrePrioridades = false;
            this.mostrarSavePrioridades = false;
            this.nombrePrioridades = "";
            this.mostrarEditPrioridades = false;
            axios
                .post(this.baseURL + "api/cargaPrioridad", {
                    id: 0,
                })
                .then((response) => {
                    this.listaPrioridades = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.filtroPrioridades = null;
            this.dialogPrioridades = true;
        },

        abrirDialogProductos() {
            this.nuevoProducto = false;
            this.mostrarSelectProducto = true;
            this.mostrarNombreProducto = false;
            this.mostrarSaveProducto = false;
            this.nombreProducto = null;
            this.descripcionProducto = null;
            this.urlArchivo = null;
            this.archivoProducto = null;
            this.mostrarEditProducto = false;

            axios
                .post(this.baseURL + "api/cargaProducto", {
                    id: 0,
                })
                .then((response) => {
                    this.listaProductos = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.filtroProductos = null;
            this.dialogProductos = true;
        },

        abrirDialogValorProyectos() {
            this.dialogValorProyectos = true;
            this.llamadoComerciales();
        },

        cargarProyectos() {
            axios
                .post(this.baseURL + "api/cargarproyectos", {
                    idComercial: this.selectedComercial ? this.selectedComercial.id : 0,
                })
                .then((response) => {
                    this.listaProyectos = response.data.data;
                })
                .catch((error) => {
                    console.error("Error al cargar proyectos:", error);
                });
        },

        llamadoCategorias() {
            axios
                .get(this.baseURL + "api/cargarcc")
                .then((response) => {
                    this.categorias = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        llamadoCargos(id) {
            axios
                .post(this.baseURL + "api/cargarca", {
                    idcat: id,
                })
                .then((response) => {
                    this.cargos = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        llamadoTipoIdentificacion() {
            axios
                .get(this.baseURL + "api/cargarti")
                .then((response) => {
                    this.tipoIdentificacion = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        llamadoTipoEmpresa() {
            axios
                .get(this.baseURL + "api/cargarte")
                .then((response) => {
                    this.tipoEmpresa = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        llamadoSectores() {
            axios
                .get(this.baseURL + "api/cargarse")
                .then((response) => {
                    this.sectorEmpresa = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        llamadoDepartamentos() {
            axios
                .get(this.baseURL + "api/cargarde")
                .then((response) => {
                    this.departamentos = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        llamadoCiudades(id) {
            axios
                .post(this.baseURL + "api/cargarci", {
                    iddpto: id,
                })
                .then((response) => {
                    this.ciudades = response.data.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        cerrarDIV() {
            this.alerta = false;
        },

        getAlertStyle() {
            return {
                borderRadius: "20px",
                position: "fixed",
                top: "50%",
                left: "50%",
                transform: "translate(-50%, -50%)",
                backgroundColor: "rgb(227, 231, 252)",
                padding: "20px",
                border: "1px solid black",
                borderRadius: "10px",
                boxShadow: "0 6px 15px rgba(0, 0, 0, 0.5)",
                transition: "box-shadow 0.3s ease-in-out",
                width: "20%",
            };
        },



        filterNumber() {
            if (this.celular < 573) {
                this.celular = 573;
            }

            if (this.celular && this.celular.length > 12) {
                // Si tiene más de 10 dígitos, truncar el valor
                this.celular = this.celular.slice(0, 12);
            }
        },

        _isDigitsOnly(s) {
            const x = String(s ?? "").trim();
            // permite dígitos y separadores comunes (.,-_/ y espacios)
            return !!x && /^[\d\.\-\_\/\s]+$/.test(x);
        },
        _digitsCanon(s) {
            // solo dígitos y sin ceros a la izquierda
            const d = String(s ?? "").replace(/\D+/g, "");
            return d.replace(/^0+/, "") || "0";
        },
        _normalize(s) {
            // deja tu versión mejorada para texto
            return String(s ?? "")
                .toLowerCase()
                .normalize("NFD")
                .replace(/\p{Diacritic}/gu, "")
                .replace(/\s+/g, " ")
                .trim();
        },
        _equalsName(a, b) {
            const sa = String(a ?? "").trim();
            const sb = String(b ?? "").trim();

            // si ambos son "numéricos"
            if (this._isDigitsOnly(sa) && this._isDigitsOnly(sb)) {
                return this._digitsCanon(sa) === this._digitsCanon(sb);
            }
            // si no, comparación de texto insensible
            return this._normalize(sa) === this._normalize(sb);
        },

        mensajeSegunComercialNIT(comercial) {
            const esMismo = this._equalsName(comercial, this.nombreComercial);

            if (esMismo) {
                if (this.estaEditando) {
                    // EDITANDO: no alertar
                    this.alertaNit = false;
                    this.mensajeAlertaNit = "";
                    this.dsGuardar = false;
                    return null;
                } else {
                    // CREANDO: alertar "registrada"
                    const msg = "Esta empresa ya se encuentra asignada a ti";
                    this.alertaNit = true;
                    this.mensajeAlertaNit = msg;
                    this.dsGuardar = true;
                    return msg;
                }
            }

            // Diferente comercial → alertar "asignada a"
            const msg = `Esta empresa ya se encuentra asignada a: ${comercial}`;
            this.alertaNit = true;
            this.mensajeAlertaNit = msg;
            this.dsGuardar = true;
            return msg;
        },

        mensajeSegunComercialRazonSocial(comercial) {
            const esMismo = this._equalsName(comercial, this.nombreComercial);

            if (esMismo) {
                if (this.estaEditando) {
                    // EDITANDO: no alertar
                    this.alertaRazonSocial = false;
                    this.mensajeAlertaRazonSocial = "";
                    this.dsGuardar = false;
                    return null;
                } else {
                    // CREANDO: alertar "registrada"
                    const msg = "Esta empresa ya se encuentra asignada a ti";
                    this.alertaRazonSocial = true;
                    this.mensajeAlertaRazonSocial = msg;
                    this.dsGuardar = true;
                    return msg;
                }
            }

            // Diferente comercial → alertar "asignada a"
            const msg = `Esta empresa ya se encuentra asignada a: ${comercial}`;
            this.alertaRazonSocial = true;
            this.mensajeAlertaRazonSocial = msg;
            this.dsGuardar = true;
            return msg;
        },

        validarNombreComercial(comercial) {
            return (this.esElMismoNombrecomercial =
                this._normalize(comercial) === this._normalize(this.nombreComercial));
        },



        filterTel1() {
            if (this.tel1 < 57) {
                this.tel1 = 57;
            }
            if (this.tel1 && this.tel1.length > 12) {
                // Si tiene más de 10 dígitos, truncar el valor
                this.tel1 = this.tel1.slice(0, 12);
            }
        },

        llamadoComerciales() {
            axios
                .post(this.baseURL + "api/cargausus", {
                    idusu: this.idUsuario,
                    tipo: 1, // 1 para cargar los usuarios del rol comercial
                })
                .then((response) => {
                    this.listaComerciales = response.data.data.map((c) => ({
                        id: c.u_id,
                        nombre: `${c.u_nom} ${c.u_ape}`,
                    }));
                })
                .catch((error) => {
                    console.error("Error al cargar comerciales:", error);
                });
        },

        getNombreComercial(id) {
            const comercial = this.listaComerciales.find((c) => c.id === id);
            return comercial ? comercial.nombre : "Sin comercial";
        },

        getNombrePerfil(id) {
            const perfil = this.perfilesUsu?.find((p) => p.id === id);
            return perfil ? perfil.nombre : null;
        },
    },
};
</script>

<style scoped>
.campo-input {
    width: 91%;
    padding: 8px 12px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    outline: none;
    transition: border 0.3s;
}

.campo-input:focus {
    border-color: #007bff;
    /* azul al enfocar */
    box-shadow: 0 0 3px rgba(0, 123, 255, 0.5);
}

.menu-link {
    color: #1976d2;
    cursor: pointer;
    text-decoration: underline;
    font-size: 1rem;
    margin-bottom: 8px;
    font-weight: 500;
    transition: color 0.2s;
    width: fit-content;
}

.menu-link:hover {
    color: #0a1c3a;
    text-decoration: underline;
}

.empresa-card-activa {
    border-radius: 16px;
    background: linear-gradient(135deg, #f5f7fa 80%, #e3f2fd 90%);
    transition: box-shadow 0.2s, transform 0.2s;
    cursor: pointer;
}

.empresa-card-inactiva {
    border-radius: 16px;
    background: linear-gradient(135deg, #f5f7fa 50%, #fde3e3 90%);
    transition: box-shadow 0.2s, transform 0.2s;
    cursor: pointer;
}

.empresa-card:hover {
    box-shadow: 0 8px 32px rgba(25, 118, 210, 0.12);
    transform: translateY(-2px) scale(1.01);
}

.empresa-title {
    letter-spacing: 0.5px;
}

.empresa-label {
    font-size: 0.95rem;
}

.empresa-value {
    font-size: 1.05rem;
}

.contact-card-text {
    font-size: 0.9rem;
    /* tamaño normal para pantallas grandes */
}

.btn-grow-card-items {
    transition: transform 0.2s;
}

.btn-grow-card-items:hover {
    transform: scale(1.01);
    z-index: 1.1;
}

.btn-grow-card {
    transition: transform 0.2s;
}

.btn-grow-card:hover {
    transform: scale(1.05);
    z-index: 1.5;
}

.btn-grow-card-items {
    transition: transform 0.2s;
}

.btn-grow-card-items:hover {
    transform: scale(1.01);
    z-index: 1.1;
}

@media (max-width: 1040px) {
    .contact-card-text {
        font-size: 0.8rem;
        /* tamaño reducido para pantallas pequeñas */
    }
}

.menu-item-activo {
    background: #fff !important;
    color: #006CA1 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 12px 0 #006ca11a;
    transition: background 0.2s, color 0.2s;
    padding-top: 5px;
    padding-bottom: 5px;
}

.menu-item-activo .v-list-item-title,
.menu-item-activo .v-icon {
    color: #006CA1 !important;
}
</style>
