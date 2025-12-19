<template>
    <v-app>
    <AppHeader :nombre-comercial="nombreComercial" :imagen-comercial="imagenComercial" :correo-usuario="correoUsuario"
      :comercial-id="comercialId" :base-u-r-l="baseURL" :idCargo="idCargo" v-model:drawer="drawer" @imagen-actualizada="actualizarImagen"
      @cerrar-sesion="cerrarSesion" />

    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">

        <v-row style="height: 100%; width: 100%;">
          <v-col style="height: 100%; width: 100%;" cols="4">
            <v-card class=" elevation-8" style="height: 100%; width: 100%;">
              <v-card-title class="text-h7 d-flex "
                                style="color: white; background-color: #006CA1;">

                                <div class="d-flex align-center">
                                    <v-icon size="23" class="mr-2">mdi mdi-contacts</v-icon>
                                    <p style="font-size: 1.2rem;">Contactos ({{ listaContactos.length }})</p>
                                </div>
                                <v-spacer></v-spacer>

                                <div @click="dialogAgregarContacto = !dialogAgregarContacto" v-bind="props" class="d-flex flex-column align-center mr-2 btn-grow-card"
                                            style="cursor:pointer;">
                                            <v-icon color="white" size="28">mdi-plus</v-icon>
                                            <span class="mt-n1"
                                                style="font-size: 0.85rem; color: white; font-weight: 500;">Añadir
                                                contacto</span>
                                        </div>
                                        
                                <v-menu v-model="menuBuscar" offset-y transition="scale-transition"
                                    :close-on-content-click="false">
                                    <template #activator="{ props }">
                                        <div v-bind="props" class="d-flex flex-column align-center btn-grow-card"
                                            style="cursor:pointer;">
                                            <v-icon color="white" size="28">mdi-magnify</v-icon>
                                            <span class="mt-n1"
                                                style="font-size: 0.85rem; color: white; font-weight: 500;">Buscar
                                                contacto</span>
                                        </div>
                                    </template>
                                    <v-card
                                        style="min-width: 240px; background: rgba(255,255,255,0.98); box-shadow: 0 4px 24px rgba(0,0,0,0.08); border-radius: 12px; padding: 16px;">
                                        <v-text-field v-model="filtroNombre" density="compact" variant="solo"
                                            bg-color="rgba(255,255,255, 0.9)" base-color="rgba(255,255,255, 0.9)"
                                            color="#006CA1" clearable rounded="lg" hide-details
                                            style="max-width: 190px; min-height: 40px;"
                                            placeholder="Filtrar por nombre..." autofocus />
                                    </v-card>
                                </v-menu>
                            </v-card-title>
                            <v-card-text style="height: calc(100vh - 180px); padding: 0;">
                                <v-virtual-scroll :items="contactosFiltrados" :item-height="116"
                                    style="height: 100%; width: 100%;">
                                    <template #default="{ item }">
                                        <v-card
                                            :class="selectedChat === item ? 'contact-card-selected mt-2 mx-2 btn-grow-card' : 'contact-card mt-2 mx-2 btn-grow-card'"
                                            elevation="2" @click="activarChat(item)"
                                            style="border-radius: 14px; overflow: hidden; position: relative; min-height: 88px;">
                                            <v-row no-gutters align="center" class="pa-2" style="gap: 0;">
                                                <v-col cols="auto"
                                                    class="d-flex flex-column align-center justify-center"
                                                    style="position: relative; min-width: 48px;">
                                                    <v-avatar size="40" color="#006CA1" class="elevation-2">
                                                        <template v-if="item.nombreContacto">
                                                            <span
                                                                style="color: white; font-size: 1.2rem; font-weight: bold;">
                                                                {{ item.nombreContacto.charAt(0).toUpperCase() }}
                                                            </span>
                                                        </template>
                                                        <template v-else>
                                                            <v-icon color="white" size="28">mdi-account-circle</v-icon>
                                                        </template>
                                                    </v-avatar>
                                                </v-col>
                                                <v-col class="pl-2 pr-1" style="min-width: 0;">
                                                    <div class="d-flex align-center justify-space-between mb-1"
                                                        style="gap: 6px;">
                                                        <div class="font-weight-bold contact-card-text"
                                                            style="font-size: 0.95rem; color: #0A1C3A; max-width: 160px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                                                            {{ item.nombreContacto }}
                                                        </div>
                                                        <div class="phone-pill contact-card-text ml-1"
                                                            style="background: #e3f2fd; color: #0A1C3A; font-weight: 600; font-size: 0.85rem; padding: 3px 10px; border-radius: 10px;">
                                                            <v-icon size="16" color="#1976D2"
                                                                class="mr-1">mdi-cellphone</v-icon>{{ item.celular }}
                                                        </div>
                                                    </div>
                                                    <div class="d-flex align-center mb-1" style="gap: 8px;">
                                                        <div class="contact-email px-2 py-1"
                                                            style="background: #f5f7fa; border-radius: 7px; color: #444; font-size: 0.89rem; max-width: 250px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                                                            <v-icon size="15" color="#1976D2"
                                                                class="mr-1">mdi-email</v-icon>
                                                            {{ item.correo ? item.correo : 'No disponible' }}
                                                        </div>
                                                    </div>
                                                    <div class="d-flex align-center mt-1" style="gap: 7px;">
                                                        <span class="meta-chip"
                                                            style="background: #e3f2fd; color: #0A1C3A; border-radius: 7px; padding: 3px 8px; font-size: 0.80rem;">
                                                            <v-icon size="14" color="#1976D2"
                                                                class="mr-1">mdi-domain</v-icon>{{ item.razon_social ?
                                                                    item.razon_social : 'No disponible' }}
                                                        </span>
                                                        <span class="meta-chip"
                                                            style="background: #e3f2fd; color: #0A1C3A; border-radius: 7px; padding: 3px 8px; font-size: 0.80rem;">
                                                            <v-icon size="14" color="#1976D2"
                                                                class="mr-1">mdi-card-account-details</v-icon>{{
                                                                    item.nit ?
                                                                        item.nit : 'No disponible' }}
                                                        </span>
                                                        <v-spacer></v-spacer>
                                                        <v-badge v-if="item.mostrarIconoWsp" location="top right"
                                                            color="green" :content="item.contadorWsp"
                                                            class="wsp-badge mr-2">
                                                            <v-icon color="success" icon="mdi-phone-alert-outline"
                                                                size="22"></v-icon>
                                                        </v-badge>
                                                    </div>
                                                </v-col>
                                            </v-row>
                                        </v-card>
                                    </template>
                                </v-virtual-scroll>
                            </v-card-text>

                        </v-card>
                    </v-col>

                    <v-col style="height: 100%; width: 100%;">
                        <v-card v-if="ifChatCard" class="rounded-xl elevation-8" style="height: 100%; width: 102%;">
                            <v-card-title class="py-2 px-4"
                                style="background:#006CA1; color:#fff; display:flex; align-items:center">
                                <div class="d-flex align-center">
                                    <v-icon size="small" class="mr-2">mdi mdi-forum-outline</v-icon>
                                    <span class="text-h6"> Chat</span>
                                </div>
                            </v-card-title>
                            <v-card-text style="overflow-y: auto; height: 100%; width: 100%;" class="pa-4">
                                <h2 class="d-flex justify-center align-middle">Seleccione un contacto para iniciar el
                                    chat.</h2>
                                <div class="d-flex justify-center align-middle">
                                    <img class="mt-4 " src="../assets/Logo.png"
                                        style="max-width: 100%; opacity: 100%; height: auto; object-fit: contain;" />
                                </div>
                            </v-card-text>
                        </v-card>

                        <transition name="slide-x-transition">
                            <iframe id="iframeChatID" v-if="iframeChat" :src="urlChat"
                                transition="scroll-y-reverse-transition" :style="getChatStyle()" frameborder="0">
                            </iframe>
                        </transition>
                    </v-col>
                </v-row>

            </v-container>
        </v-main>

        <audio ref="audio2" :src="soundUrl2"></audio>

        <!-----DIALOGO AÑADIR CONTACTO------->
        <v-dialog v-model="dialogAgregarContacto" persistent max-width="560px">
            <v-card style="border-radius: 18px; overflow: hidden; box-shadow: 0 8px 32px rgba(0,108,161,0.10);">
                <v-card-title
                class="text-h5 font-weight-bold d-flex align-center "
                style="color: #0A1C3A; background-color: #006CA1; box-shadow: 0 2px 8px rgba(0,108,161,0.07);"
                >
                <v-icon class="mr-2 ml-2" color="white" size="28">mdi-account-plus</v-icon>
                <span style="color: white;">Registrar Nuevo Contacto</span>
                <v-spacer />
                <v-btn icon size="small" @click="dialogAgregarContacto = false" style="color: black;">
                    <v-icon size="small">mdi-close</v-icon>
                </v-btn>
                </v-card-title>
                <v-divider />
                <v-card-text class="pa-6" style="background: #f7fafd;">
                <v-form ref="formNuevoContacto">
                    <v-row class="d-flex justify-space-between">
                        <v-col >
                            <div class="mb-2" style="color: #0A1C3A; font-weight: 600; font-size: 0.9rem;">
                                <v-icon size="18" color="#1976D2" class="mr-1">mdi-account</v-icon>
                                Nombre del Contacto
                            </div>
                        </v-col>
                        <v-col>
                            <div class="mb-2 " style="color: #0A1C3A; font-weight: 600; font-size: 0.9rem;">
                                <v-icon size="18" color="#1976D2" class="mr-1">mdi-cellphone</v-icon>
                                Número de Celular
                            </div>
                        </v-col>
                    </v-row>

                    <v-row dense>
                        
                        <v-col cols="12" sm="6">
                            <v-text-field
                            v-model="nuevoContactoNombre"
                            label="Nombre"
                            prepend-inner-icon="mdi-account"
                            variant="solo"
                            color="#1976D2"
                            class="modern-input"
                            autocomplete="off"
                            :rules="[v => !!v || 'El nombre es requerido']"
                            />
                        </v-col>
                        
                        <v-col cols="12" sm="6">
                            <v-text-field
                            v-model="nuevoContactoTelefono"
                            type="number"
                            label="Teléfono"
                            prepend-inner-icon="mdi-cellphone"
                            variant="solo"
                            color="#1976D2"
                            class="modern-input"
                            autocomplete="off"
                            :rules="telefonoRules"
                            @input="filterNumberNuevoContacto"
                            />
                        </v-col>
                        <v-row>
                            <v-col cols="12">
                                <v-alert
                                v-if="alertaCelular"
                                class="mx-0 mb-4 mt-2 modern-alert"
                                type="error"
                                prominent
                                icon="mdi-account-alert"
                                style="font-size: 0.95rem;"
                                >
                                <span style="font-weight: 500;">{{ mensajeAlertaCelular }}</span>
                                </v-alert>
                            </v-col>
                        </v-row>
                        <div class="mb-2" style="color: #0A1C3A; font-weight: 600; font-size: 0.95rem;">
                        <v-icon size="18" color="#1976D2" class="mr-1">mdi-email</v-icon>
                        Información de Correo electronico
                        </div>
                        <v-col cols="12">
                            <v-text-field
                            v-model="nuevoContactoCorreo"
                            label="Correo Electrónico"
                            prepend-inner-icon="mdi-email"
                            variant="solo"
                            color="#1976D2"
                            class="modern-input"
                            autocomplete="off"
                            :rules="[v => !v || /.+@.+\..+/.test(v) || 'Correo inválido']"
                            />
                        </v-col>
                    </v-row>
                    <v-divider class="my-4" />
                    <div class="mb-2" style="color: #0A1C3A; font-weight: 600; font-size: 0.95rem;">
                    <v-icon size="18" color="#1976D2" class="mr-1">mdi-office-building</v-icon>
                    Información de Empresa
                    </div>
                    <v-row dense>
                    <v-col cols="12" sm="10">
                        <v-select
                        v-model="nuevoContactoEmpresa"
                        :items="empresas"
                        label="Asociar a una empresa"
                        return-object item-title="p_razon_social" item-value="id"
                        variant="solo"
                        color="#1976D2"
                        class="modern-input"
                        prepend-inner-icon="mdi-domain"
                        :menu-props="{ maxHeight: '200px' }"
                        clearable
                        />
                    </v-col>
                    <v-col cols="12" sm="2" class="d-flex align-start mt-2">
                        <v-tooltip text="Añadir Prospecto" location="top">
                            <template #activator="{ props }">
                        <v-btn v-bind="props" color="#1d4ed8" icon variant="flat" size="small" class="ml-1 modern-btn btn-grow-card" title="Agregar empresa" @click="abrirFormularioProspecto()">
                        <v-icon>mdi-plus</v-icon>
                        </v-btn>
                        </template>
                        </v-tooltip>
                        <v-tooltip text="Editar Prospecto" location="top">
                            <template #activator="{ props }">
                        <v-btn  v-bind="props" color="#1d4ed8" icon variant="flat" size="small" class="ml-1 modern-btn btn-grow-card" title="Agregar empresa" @click="cargarProspecto(nuevoContactoEmpresa)" :disabled="nuevoContactoEmpresa == null">
                        <v-icon>mdi mdi-pencil</v-icon>
                        </v-btn>
                        </template>
                        </v-tooltip>
                    </v-col>
                    </v-row>
                    <v-divider class="my-4" />
                    <v-row>
                    <v-col cols="12" class="d-flex justify-center">
                        <v-btn
                        color="#1d4ed8"
                        class="modern-btn px-8 py-3 btn-grow-card"
                        :disabled="dsGuardar || !$refs.formNuevoContacto?.validate()"
                        style="font-weight: bold; font-size: 1.1rem; border-radius: 10px; box-shadow: 0 2px 8px #1976D233;"
                        type="submit"
                        block
                        >
                        <v-icon class="mr-2" left>mdi-account-plus</v-icon>
                        REGISTRAR CONTACTO
                        </v-btn>
                    </v-col>
                    </v-row>
                </v-form>
                </v-card-text>
            </v-card>
        </v-dialog>
        <!-----DIALOGO AÑADIR CONTACTO------->

        <!------DIALOGO CREAR PROSPECTO------>
        <!-- FORMULARIO PROSPECTO CONTACTO-->

        <v-dialog v-model="formularioProspecto" width="800" persistent>
        <v-card-title class="text-h6"
            style="background-color: #006CA1; color: white; display: flex; align-items: center;">

            <div class="d-flex align-center">
            <v-icon class="mr-2">mdi mdi-account-group </v-icon>
            Nuevo Prospecto
            </div>

            <v-spacer></v-spacer>
            <v-btn icon="mdi-close" size="small" color="white" @click="cerrarFormularioProspecto()" class="btn-grow" />
        </v-card-title>

        <v-card>
            <v-card-text>
            <v-row>
                <v-col>
                <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">Información de la Empresa
                </h3>
                <!--<v-autocomplete class="mx-5" v-model="empresa" :items="empresas" return-object item-title="nombre"
                        item-value="id" label="Empresa" variant="outlined" clearable />-->
                <v-alert v-if="alertaNit" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                    this.mensajeAlertaNit
                }}</v-alert>
                <!--<v-text-field class="mx-5" v-model="nit" label="Número de Identificación" type="number"
                        variant="outlined" clearable />-->

                <v-row>
                    <v-col cols="11">
                    <input class="campo-input mx-5 mb-5"  list="empresas" id="empresa" v-model="nit" placeholder="NIT"
                        autocomplete="off" type="number"/>
                    </v-col>
                    <v-col style="margin-left: -30px;">
                    <v-icon class="mt-2" @click="nit = null">
                        mdi-close-circle
                    </v-icon>
                    </v-col>
                </v-row>

                <datalist id="empresas">
                    <option v-for="(empresa, index) in listaEmpresas" :key="empresa.id" :value="`${empresa.p_nit}`">
                    </option>
                </datalist>

                <v-alert v-if="alertaRazonSocial" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                    this.mensajeAlertaRazonSocial
                }}</v-alert>
                <!--<v-text-field class="mx-5" v-model="razonSocial" label="Razón Social" type="text" variant="outlined"
                        clearable />-->
                <v-row>
                    <v-col cols="11">
                    <input class="campo-input mx-5 mb-5" list="empresas2" id="empresa" v-model="razonSocial"
                        placeholder="Razón Social" autocomplete="off" />
                    </v-col>
                    <v-col style="margin-left: -30px;">
                    <v-icon class="mt-2" @click="razonSocial = null">
                        mdi-close-circle
                    </v-icon>
                    </v-col>
                </v-row>

                <datalist id="empresas2">
                    <option v-for="(empresa, index) in listaEmpresas2" :key="empresa.id"
                    :value="`${empresa.p_razon_social}`">
                    </option>
                </datalist>
                <v-row>
                    <v-col>
                    <v-select class="ml-5" v-model="tipoId" :items="tipoIdentificacion" return-object item-title="nombre"
                        item-value="id" label="Tipo Identificación" variant="outlined" clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-card-account-details</v-icon>
                        </template>
                    </v-select>
                    </v-col>
                    <v-col>
                    <v-select disabled class="mr-5" v-model="tipoEmp" :items="tipoEmpresa" return-object
                        item-title="nombre" item-value="id" label="Tipo Empresa" variant="outlined" clearable
                        autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-domain</v-icon>
                        </template>
                    </v-select>
                    </v-col>
                </v-row>
                <v-select class="mx-5" v-model="sector" :items="sectorEmpresa" return-object item-title="nombre"
                    item-value="id" label="Sector" variant="outlined" clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-office-building</v-icon>
                    </template>
                </v-select>
                <v-text-field class="mx-5" v-model="direccion" label="Dirección" type="text" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-map-marker</v-icon>
                    </template>
                </v-text-field>
                <v-row>
                    <v-col>
                    <v-autocomplete class="ml-5" v-model="departamento" :items="departamentos" return-object
                        item-title="nombre" item-value="id" label="Departamento" variant="outlined" clearable
                        autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-home-city</v-icon>
                        </template>
                    </v-autocomplete>
                    </v-col>
                    <v-col>
                    <v-autocomplete class="mr-5" v-model="ciudad" :items="ciudades" return-object item-title="nombre"
                        item-value="id" label="Ciudad" variant="outlined" clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-city-variant</v-icon>
                        </template>
                    </v-autocomplete>
                    </v-col>
                </v-row>
                <v-text-field class="mx-5" v-model="web" label="Pagina Web" type="text" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-web</v-icon>
                    </template>
                </v-text-field>
                <v-text-field class="mx-5" v-model="correoEmpresa" label="Mail Empresa" type="email" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                    </template>
                </v-text-field>
                <v-row>
                    <v-col>
                    <v-text-field class="ml-5" @input="filterTel1" :rules="[maxlength2].flat()" v-model="tel1" label="Telefono 1" type="number" variant="outlined"
                        clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-cellphone</v-icon>
                        </template>
                    </v-text-field>
                    </v-col>
                    <v-col>
                    <v-text-field class="mr-5" v-model="tel2" label="Telefono 2" type="number" variant="outlined"
                        clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-phone</v-icon>
                        </template>
                    </v-text-field>
                    </v-col>

                </v-row>
                <v-select class="mx-5" clearable label="Servicio" v-model="selectedServicioProspecto"
                    :items="selectServiciosActividad" return-object item-title="nombre" item-value="id" variant="outlined"
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-briefcase</v-icon>
                    </template></v-select>

                </v-col>
                <v-col v-if="false" style="border-left: 1px solid #ccc; padding-left: 20px;">
                <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">Información del Contacto</h3>
                <v-text-field class="mx-5" v-model="nombre" label="Nombre" type="text" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                    </template>
                </v-text-field>
                <v-text-field class="mx-5" v-model="apellido" label="Apellido" type="text" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                    </template>
                </v-text-field>
                <v-row>
                    <v-col>
                    <v-autocomplete class="mx-5" v-model="categoria" :items="categorias" return-object item-title="nombre"
                        item-value="id" label="Categoria Cargo" variant="outlined" clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-format-list-bulleted-type</v-icon>
                        </template>
                    </v-autocomplete>
                    </v-col>
                    <v-col>
                    <v-autocomplete class="mx-5 ml-0" v-model="cargo" :items="cargos" return-object item-title="nombre"
                        item-value="id" label="Cargo" type="text" variant="outlined" clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-account-tie</v-icon>
                        </template>
                    </v-autocomplete>
                    </v-col>
                </v-row>
                <v-text-field class="mx-5" v-model="correoContacto" label="Correo" type="email" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                    </template>
                </v-text-field>

                <v-row>
                    <v-col cols="4" class="m-0">
                    <v-text-field class="mx-5 mr-0" v-model="extension" label="Extensión" type="number" variant="outlined"
                        clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-phone-in-talk</v-icon>
                        </template>
                    </v-text-field>
                    </v-col>
                    <v-col cols="8">
                    <v-text-field @input="filterNumber" :rules="[maxlength2].flat()" class="mx-5 ml-0 pl-0"
                        v-model="celular" label="Celular" type="number" variant="outlined" autocomplete="off">
                        <template v-slot:prepend-inner>
                        <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-cellphone</v-icon>
                        </template>
                    </v-text-field>
                    </v-col>
                    <v-col>
                    <v-alert v-if="alertaCelular" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                        this.mensajeAlertaCelular
                    }}</v-alert>
                    </v-col>
                </v-row>



                </v-col>
            </v-row>
            </v-card-text>
            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn variant="outlined" color="primary" class=" text-none btn-grow-card"
                @click="cerrarFormularioProspecto()">Cancelar</v-btn>

            <v-btn color="primary" variant="flat" size="large" rounded="lg" class="text-none px-5 btn-grow-card"
                prepend-icon="mdi mdi-content-save-check-outline" :disabled="dsGuardar"
                @click="guardarDatos()">Guardar</v-btn>
            </v-card-actions>
        </v-card>
        </v-dialog>

        <!-- FORMULARIO PROSPECTO CONTACTO-->
        <!------DIALOGO CREAR PROSPECTO------>

        <!-- Dialog Cambio Clave -->
        <v-dialog v-model="dialogCambioClave" persistent max-width="400px">
            <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
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
                    <div class="text-caption mt-n4 mb-4" style="color: red;"
                        v-if="nuevaClave && !isValidPassword(nuevaClave)">
                        La
                        nueva
                        clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8
                        caracteres.
                    </div>
                    <v-text-field v-model="confirmarClave" label="Confirmar Nueva Clave"
                        :type="mostrarConfirmarClave ? 'text' : 'password'" variant="outlined" required clearable>
                        <template v-slot:append-inner>
                            <v-icon :icon="mostrarConfirmarClave ? 'mdi-eye' : 'mdi-eye-closed'"
                                @click="mostrarConfirmarClave = !mostrarConfirmarClave" />
                        </template>
                    </v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn variant="flat" color="#006CA1" @click="cambiarClave()">Guardar</v-btn>
                    <v-btn variant="flat" color="grey"
                        @click="dialogCambioClave = false; claveActual = null; nuevaClave = null; confirmarClave = null;">Cancelar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <!-- Dialog Cambio Clave -->

        <!-- Dialog Alertas -->
        <v-dialog v-model="alerta" persistent style="z-index: 10000;">
        <v-card :style="getAlertStyle()">
            <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
            class="mx-auto"></v-progress-circular>
            <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-tittle>
            <v-btn class="mt-4 mx-auto" @click="cerrarDIV()"
            style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
        </v-card>
        </v-dialog>
        <!-- Dialog Alertas -->

        <v-dialog v-model="dialogCrearEditarProspecto" persistent width="800">
      <v-card style="height: 100%; border-radius: 20px;">
        <v-card-title class="text-h6" style="color: white; font-weight: bold; background-color: #006CA1;">
          <div v-if="idProspectoSeleccionado">
            <v-icon class="mr-2">mdi-account-cog</v-icon>
            Editar Prospecto
            <v-icon style="float: right;" @click="actualizarProspecto()" icon="mdi-content-save" size="small" :disabled="dsGuardar"></v-icon>
          </div>
        </v-card-title>
        <v-card-text style="overflow-y: auto; height: 100%;">
          <v-row class="my-1">
            <v-col>
              <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">
                Información de
                la Empresa</h3>
              <v-alert v-if="alertaNit" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                this.mensajeAlertaNit
              }}</v-alert>

              <v-row>
                <v-col cols="11">
                  <input class="campo-input mx-5 mb-5" type="number" list="empresas" id="empresa" v-model="nitComercial"
                    placeholder="NIT" autocomplete="off" />
                </v-col>
                <v-col style="margin-left: -30px;">
                  <v-icon class="mt-2" @click="nitComercial = null">
                    mdi-close-circle
                  </v-icon>
                </v-col>
              </v-row>

              <datalist id="empresas">
                <option v-for="(empresa, index) in listaEmpresasComercial" :key="empresa.id"
                  :value="`${empresa.p_nit}`">
                </option>
              </datalist>

              <v-alert v-if="alertaRazonSocial" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                this.mensajeAlertaRazonSocial
              }}</v-alert>
              <v-row>
                <v-col cols="11">
                  <input class="campo-input mx-5 mb-5" list="empresas2" id="empresa" v-model="razonSocialComercial"
                    placeholder="Razón Social" autocomplete="off" />
                </v-col>
                <v-col style="margin-left: -30px;">
                  <v-icon class="mt-2" @click="razonSocialComercial = null">
                    mdi-close-circle
                  </v-icon>
                </v-col>
              </v-row>

              <datalist id="empresas2">
                <option v-for="(empresa, index) in listaEmpresasComercial2" :key="empresa.id"
                  :value="`${empresa.p_razon_social}`">
                </option>
              </datalist>
              <v-row>
                <v-col>
                  <v-select class="ml-5" v-model="tipoIdComercial" :items="tipoIdentificacion" return-object
                    item-title="nombre" item-value="id" label="Tipo Identificación" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-card-account-details</v-icon>
                    </template>
                  </v-select>
                </v-col>
                <v-col>
                  <v-select disabled class="mr-5" v-model="tipoEmpComercial" :items="tipoEmpresa" return-object
                    item-title="nombre" item-value="id" label="Tipo Empresa" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-domain</v-icon>
                    </template>
                  </v-select>
                </v-col>
              </v-row>
              <v-select class="mx-5" v-model="sectorComercial" :items="sectorEmpresa" return-object item-title="nombre"
                item-value="id" label="Sector" variant="outlined" clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-office-building</v-icon>
                </template>
              </v-select>
              <v-text-field class="mx-5" v-model="direccionComercial" label="Dirección" type="text" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-map-marker</v-icon>
                </template>
              </v-text-field>
              <v-row>
                <v-col>
                  <v-autocomplete class="ml-5" v-model="departamentoComercial" :items="departamentos" return-object
                    item-title="nombre" item-value="id" label="Departamento" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-home-city</v-icon>
                    </template>
                  </v-autocomplete>
                </v-col>
                <v-col>
                  <v-autocomplete class="mr-5" v-model="ciudadComercial" :items="ciudades" return-object
                    item-title="nombre" item-value="id" label="Ciudad" variant="outlined" clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-city-variant</v-icon>
                    </template>
                  </v-autocomplete>
                </v-col>
              </v-row>
              <v-text-field class="mx-5" v-model="webComercial" label="Pagina Web" type="text" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-web-box</v-icon>
                </template>
              </v-text-field>
              <v-text-field class="mx-5" v-model="correoEmpresaComercial" label="Mail Empresa" type="text"
                variant="outlined" clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                </template>
              </v-text-field>
              <v-row>
                <v-col>
                  <v-text-field class="ml-5" @input="filterTel1Comercial" :rules="[maxlength2].flat()" v-model="tel1Comercial" label="Telefono 1" type="number" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-cellphone</v-icon>
                    </template>
                  </v-text-field>
                </v-col>
                <v-col>
                  <v-text-field class="mr-5" v-model="tel2Comercial" label="Telefono 2" type="number" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-phone</v-icon>
                    </template>
                  </v-text-field>
                </v-col>
              </v-row>
            </v-col>
            <v-col v-if="false" style="border-left: 1px solid #ccc; padding-left: 20px;">
              <h3 class="text-center mb-4" style="background-color: #006CA1; color: white">
                Información del
                Contacto</h3>
              <v-text-field class="mx-5" v-model="nombreComercial2" label="Nombre" type="text" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                </template>
              </v-text-field>
              <v-text-field class="mx-5" v-model="apellidoComercial" label="Apellido" type="text" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-rename</v-icon>
                </template>
              </v-text-field>
              <v-row>
                <v-col>
                  <v-autocomplete class="mx-5" v-model="categoriaComercial" :items="categorias" return-object
                    item-title="nombre" item-value="id" label="Categoria Cargo" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-format-list-bulleted-type</v-icon>
                    </template>
                  </v-autocomplete>
                </v-col>
                <v-col>
                  <v-autocomplete class="mx-5" v-model="cargoComercial" :items="cargos" return-object
                    item-title="nombre" item-value="id" label="Cargo" type="text" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%;">mdi-account-tie</v-icon>
                    </template>
                  </v-autocomplete>
                </v-col>
              </v-row>
              <v-text-field class="mx-5" v-model="correoContactoComercial" label="Correo" type="text" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                </template>
              </v-text-field>

              <v-row>
              <v-col cols="3" class="m-0">

               <v-text-field class="ml-5 mr-n4" v-model="extensionComercial" label="Extensión" type="number" variant="outlined"
                autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-numeric</v-icon>
                </template>
              </v-text-field>

              </v-col>
              <v-col cols="9">
              <v-text-field class="mr-5 ml-2" @input="filterNumberComercial" :rules="[maxlength2].flat()"
                v-model="celularComercial" label="Celular" type="number" variant="outlined" clearable
                autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-cellphone</v-icon>
                </template>
              </v-text-field>
              </v-col>
              </v-row>
               <v-alert v-if="alertaCelular" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                this.mensajeAlertaCelular
              }}</v-alert>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions>
          <v-btn variant="outlined" color="primary" class=" text-none btn-grow-card"
            @click="dialogCrearEditarProspecto = false; dialogProspectos = true; limpiarCamposProspecto();">Cerrar</v-btn>

          <v-btn color="primary" variant="flat" size="large" rounded="lg" class="text-none px-5 btn-grow-card"
            prepend-icon="mdi mdi-content-save-check-outline" :disabled="dsGuardar"
            @click="actualizarProspecto()">Guardar</v-btn>
  
        </v-card-actions>
      </v-card>
    </v-dialog>

    </v-app>
</template>

<script>

import axios from 'axios';
import CryptoJS from "crypto-js";
import Pusher from 'pusher-js';
import Echo from 'laravel-echo';
import AppHeader from '../components/AppHeader.vue';

window.Pusher = Pusher;

export default {
    components: {
        AppHeader,
    },
    data: () => ({
        baseURL: '', // URL base de la API
        comercialId: 0, // ID del usuario comercial
        idCargo: null,
        nombreComercial: null, // Nombre del usuario comercial
        correoUsuario: null, // Correo del usuario
        celularComercial: null, // Celular del usuario
        drawer: false, // Estado del menú lateral
        imagenComercial: null,

        maxlength2: [v => !v || String(v).length < 13 || "Error. Máximo 10 dígitos"],
        telefonoRules: [
            v => !!v || "El teléfono es requerido",
            v => /^\d{12}$/.test(v) || "El teléfono debe tener 12 dígitos (ej: 573XXXXXXXXX)"
        ],



        mensajeAlert: null,
        alerta: false,
        ifCargando: false,

        listaContactos: [],

        iframeChat: false,
        ifChatCard: true,
        estadoChat: false,

        celularSeleccionado: null,

        soundUrl2: 'https://glpi-siicsa.azurewebsites.net/notificacionSonido2.mp3',

        selectedChat: null,
        notificacionNueva: null,

        filtroNombre: '',
        menuBuscar: false,
        mensajeAlertLogin: '',

        webhookListener: null,
        pusher_key: import.meta.env.VITE_PUSHER_KEY,
        dialogAgregarContacto: false,

        nuevoContactoNombre: '',
        nuevoContactoTelefono: '57',
        nuevoContactoCorreo: '',
        nuevoContactoEmpresa: null,

        alertaCelular: false,
        mensajeAlertaCelular: null,
        dsGuardar: false,

        selectClientesOportunidad: [],

        //DATA DE FORMULARIO CREAR PROSPECTO
        formularioProspecto: false,
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
        tel1: '57',
        tel2: null,
        selectedServicioProspecto: null,
        selectServiciosActividad: [],
        mensajeAlertaRazonSocial: '',
        alertaNit: false,
        mensajeAlertaNit: '',
        alertaRazonSocial: false,
        nombre: null,
        apellido: null,
        categoria: null,
        categorias: [],
        cargo: null,
        cargos: [],
        correoContacto: null,
        celular: '57',
        extension: '57',
        idUsuario: null,

        menuActivo: '',

        //DATA DE FORMULARIO EDITAR PROSPECTO
        dialogCrearEditarProspecto: false,
        idProspectoSeleccionado: null,
        nitComercial: null,
        razonSocialComercial: null,
        tipoIdentificacionComercial: null,
        tipoEmpresaComercial: null,
        tipoIdComercial: null,
        sectorComercial: null,
        direccionComercial: null,
        departamentoComercial: null,
        ciudadComercial: null,
        webComercial: null,
        correoEmpresaComercial: null,
        tel1Comercial: null,
        tel2Comercial: null,
        nombreComercial2: null,
        apellidoComercial: null,
        categoriaComercial: null,
        cargoComercial: null,
        correoContactoComercial: null,
        celularComercial: null,
        extensionComercial: null,
        listaEmpresasComercial: [],
        listaEmpresasComercial2: [],
        tipoEmpresa: [],
        tipoIdentificacion: [],
        sectorEmpresa: [],
        departamentos: [],
        ciudades: [],
        categorias: [],
        cargos: [],
        alertaNit: false,
        mensajeAlertaNit: '',
        alertaRazonSocial: false,
        mensajeAlertaRazonSocial: '',
        dsGuardar: false,
        alerta: false,
        mensajeAlertLogin: '',
        ifCargando: false,
        nombreComercial: '', // El nombre del comercial actual
        idUsuario: null, // El id del usuario actual
    }),

    created() {
        window.addEventListener("message", (e) => this.recibirMensaje(e));
    },
    beforeDestroy() {
        window.removeEventListener("message", (e) => this.recibirMensaje(e));
    },

    mounted() {
        this.idUsuario = localStorage.getItem('idUsuario');
        //preguntar por el permiso para notificacion
        Notification.requestPermission().then((permission) => {
            if (permission === "granted") {
                console.log("Permiso de notificación concedido");
            } else {
                console.log("Permiso de notificación denegado");
            }
        });

        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.comercialId = localStorage.getItem('idUsuario');
        this.imagenComercial = this.baseURL + "images/" + this.comercialId + ".jpeg";
        this.idCargo = localStorage.getItem('idCargo');
        console.log('Contactos.vue - idCargo cargado:', this.idCargo, 'tipo:', typeof this.idCargo);
        this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');
        this.celularComercial = localStorage.getItem('celularLogin');

        window.Echo = new Echo({
            broadcaster: 'pusher',
            key: this.pusher_key,
            cluster: 'us2',
            forceTLS: true
        });

        this.cargarContactos();
        this.setMenuActivoPorRuta();

        // Evitar duplicación de listeners
        if (!this.webhookListener) {
            this.webhookListener = (res) => {
                console.log("Webhook received:", res);

                const message = res?.message;
                const changed = res?.change;
                const outgoing = message.outgoing;
                const optionbutton = message.option_button;
                const status = message.status;
                const idmensaje = message.id;
                const body = message.body;
                const celu = message.wa_id;
                const type = message.type;

                this.cargarContactos2();

                setTimeout(() => {
                    if (
                        this.estadoChat == false &&
                        outgoing == 0 &&
                        optionbutton === "asesor en proceso"
                    ) {
                        console.log("entro desde canal a 1");

                        if (document.hasFocus()) {
                            this.iconoWsp(message.wa_id);
                        } else {
                            this.lanzarNotificacion(
                                "SIICSA - CRM: " +
                                this.listaContactos.find((c) => c.celular === celu)
                                    ?.nombreContacto,
                                body,
                                celu
                            );
                        }
                    } else if (
                        this.estadoChat == true &&
                        outgoing == 0 &&
                        message.wa_id != this.celularSeleccionado &&
                        optionbutton === "asesor en proceso"
                    ) {
                        console.log("entro desde canal a 2");

                        if (document.hasFocus()) {
                            this.iconoWsp(message.wa_id);
                        } else {
                            this.lanzarNotificacion(
                                "SIICSA - CRM: " +
                                this.listaContactos.find((c) => c.celular === celu)
                                    ?.nombreContacto,
                                body,
                                celu
                            );
                        }
                    } else if (
                        this.estadoChat == true &&
                        outgoing == 0 &&
                        message.wa_id == this.celularSeleccionado &&
                        optionbutton === "asesor en proceso"
                    ) {
                        console.log("entro desde canal a 3");
                        if (document.hasFocus()) {
                            // No hace nada porque el chat está activo con el contacto que envió el mensaje
                        } else {
                            this.lanzarNotificacion(
                                "SIICSA - CRM: " +
                                this.listaContactos.find((c) => c.celular === celu)
                                    ?.nombreContacto,
                                body,
                                celu
                            );
                        }
                    }
                }, 1000);
            };

            window.Echo.channel("webhooks").listen("Webhook", this.webhookListener);
        }
        this.cargarClientesActividad();
        this.cargarServiciosActividad();
        this.llamadoTipoIdentificacion();
        this.llamadoSectores();
        this.llamadoTipoEmpresa();
        this.llamadoDepartamentos();
        this.llamadoCategorias();
    },
    

    beforeUnmount() {
        if (this.webhookListener) {
            window.Echo.channel("webhooks").stopListening(
                "Webhook",
                this.webhookListener
            );
            this.webhookListener = null; // importante limpiar la referencia
        }
    },

    computed: {

        badgeContent() {
            return this.listaContactos.length.toString();
        },
        /*contactosFiltrados() {
            if (!this.filtroNombre) return this.listaContactos;
            const filtro = this.filtroNombre.toLowerCase();
            return this.listaContactos.filter(c =>
                c.nombreContacto && c.nombreContacto.toLowerCase().includes(filtro)
            );
        },*/
        contactosFiltrados() {
            if (!this.filtroNombre) return this.listaContactos;

            // Función para quitar tildes
            const quitarTildes = (texto) => {
                return texto
                    .normalize("NFD")                 // separa letras de tildes
                    .replace(/[\u0300-\u036f]/g, "") // elimina las tildes
                    .toLowerCase();
            };

            const filtro = quitarTildes(this.filtroNombre);

            return this.listaContactos.filter(c => {
                if (!c.nombreContacto) return false;
                return quitarTildes(c.nombreContacto).includes(filtro);
            });
        },
        
    },

    watch: {

        nuevoContactoTelefono(newCelular) {
        this.validarCelular(newCelular);
        },

        tipoId(newVal) {
        if (!newVal) return;

        if (newVal.nombre === 'NIT') {
            this.tipoEmp = this.tipoEmpresa.find(item => item.nombre === 'Jurídica');
        } else {
            this.tipoEmp = this.tipoEmpresa.find(item => item.nombre === 'Natural');
        }
        },

        razonSocial(newRazonSocial) {
        this.validarRazonSocial(newRazonSocial);
        },

        nit(newNit) {
        this.validarNit(newNit);
        },

        nitComercial(newNitComercial) {
        this.validarNitEditarProspecto(newNitComercial);
        },

        razonSocialComercial(newRazonSocialComercial) {
        this.validarRazonSocialEditarProspecto(newRazonSocialComercial);
        },

        celular(newCelular) {
        this.validarCelular(newCelular);
        },

        celularComercial(newCelularComercial) {
        this.validarCelular(newCelularComercial);
        },

        departamento(newValue) {
        this.llamadoCiudades(newValue ? newValue.id : 0);
        },

        departamentoComercial(newValue) {
        this.llamadoCiudades(newValue ? newValue.id : 0);
        },

        categoria(newValue) {
        this.llamadoCargos(newValue.id);
        },

        categoriaComercial(newValue) {
        if (newValue) {
            this.llamadoCargos(newValue.id);
        } else {
            this.cargoComercial = null;
        }
        },

    },

    methods: {
        // Método para actualizar la imagen del usuario cuando cambia
        actualizarImagen(nuevaImagen) {
            this.imagenComercial = nuevaImagen;
        },

        lanzarNotificacion(titulo, mensaje, celular) {
            if (Notification.permission === 'granted') {
                console.log('lanzo notificacion 1')
                this.notificacionNueva = new Notification(titulo, {
                    body: mensaje,
                    icon: '/logo.png'
                })

                this.playSound2(); // Reproducir el sonido de notificación

                this.notificacionNueva.onclick = () => {
                    console.log('Notificación clicada!')
                    window.focus() // Si ya está abierta, enfoca
                    this.iconoWsp(celular);
                }

            } else {
                Notification.requestPermission().then(permiso => {
                    if (permiso === 'granted') {
                        console.log('lanzo notificacion 2')
                        this.notificacionNueva = new Notification(titulo, {
                            body: mensaje,
                            icon: '/logo.png'
                        })

                        this.playSound2(); // Reproducir el sonido de notificación

                        // También debes agregar el onclick aquí
                        this.notificacionNueva.onclick = () => {
                            console.log('Notificación clicada!')
                            window.focus()
                            this.iconoWsp(celular)
                        }

                    } else {
                        this.iconoWsp(celular)
                    }
                })
            }
        },

        cargarContactos() {
            axios.post(this.baseURL + 'api/contactos')
                .then(response => {
                    this.listaContactos = response.data.data;

                    console.log('Contactos cargados:', this.listaContactos);
                })
                .catch(error => {
                    console.error('Error al cargar contactos:', error);
                });
        },

        cargarContactos2() {
            axios.post(this.baseURL + 'api/contactos')
                .then(response => {
                    console.log('Contactos actualizados:', response.data.data);
                    // Se añaden unicamente los nuevos resultados dejando los originales intactos
                    const nuevosContactos = response.data.data.filter(nuevo => {
                        return !this.listaContactos.some(contacto => contacto.celular === nuevo.celular);
                    });
                    this.listaContactos.push(...nuevosContactos);
                })
                .catch(error => {
                    console.error('Error al cargar contactos:', error);
                });
        },

        iconoWsp(wa_id) {

            console.log('wa_id entrante:', wa_id);

            this.listaContactos.forEach((contacto, i) => {
                var contadorWspTemp = contacto.contadorWsp;

                if (contacto.celular == wa_id && contacto.estadoChat == false) {
                    console.log('contacto dentro:', contacto.celular);
                    console.log('contacto estado dentro:', contacto.estadoChat);
                    console.log('contadorWspTemp del contacto:', contadorWspTemp);

                    this.listaContactos[i]['mostrarIconoWsp'] = true;
                    this.listaContactos[i]['tiempoActualizacion'] = Date.now();
                    contadorWspTemp++;

                    setTimeout(() => {
                        this.listaContactos[i]['contadorWsp'] = contadorWspTemp;
                    }, 200);
                    setTimeout(() => {
                        this.listaContactos.sort((a, b) => {
                            if (a.mostrarIconoWsp !== b.mostrarIconoWsp) {
                                return a.mostrarIconoWsp ? -1 : 1;
                            } else {
                                return b.tiempoActualizacion - a.tiempoActualizacion; // Ordenar por tiempo de actualización más reciente
                            }
                        });
                        //this.scrollToTop();
                    }, 200);
                    this.playSound2();
                }
            });
        },

        playSound2() {
            this.$refs.audio2.play();
        },

        getCardStyle(item) {
            return {
                backgroundColor: this.selectedChat === item ? 'red' : 'blue'
            };
        },

        activarChat(contacto) {

            this.selectedChat = contacto;

            const contacto1 = this.listaContactos.find(c => c.celular === this.celularSeleccionado);
            if (contacto1) {
                contacto1.estadoChat = false;
            }

            for (let i = 0; i < this.listaContactos.length; i++) {

                const contacto1 = this.listaContactos[i];

                if (contacto1.celular == contacto.celular) {

                    this.listaContactos[i]['estadoChat'] = true;
                    this.listaContactos[i]['contadorWsp'] = 0;
                    this.listaContactos[i]['tiempoActualizacion'] = Date.now();
                    this.listaContactos[i]['mostrarIconoWsp'] = false;

                }
            }

            this.urlChat = `/chat-web?` + new URLSearchParams({
                ncliente: contacto.nombreContacto,
                ccliente: contacto.celular,
                idusuario: this.comercialId,
                nusuario: this.nombreComercial,
                cusuario: this.celularComercial,
                rusuario: '5',
                idpqr: '0',
                perfilm: '0',
            }).toString();

            this.celularSeleccionado = contacto.celular;

            contacto.mostrarIconoWsp = false;

            console.log('Activando chat con URL:', this.urlChat);

            this.ifChatCard = false;
            this.iframeChat = true;
            this.estadoChat = true;

            document.getElementById('iframeChatID').src = this.urlChat;
        },

        recibirMensaje(event) {
            if (event.data.action === 'cerrarIframe') {
                this.iframeChat = false;
                this.estadoChat = false;
                this.selectedChat = null;

                const contacto = this.listaContactos.find(c => c.celular === this.celularSeleccionado);
                if (contacto) {
                    contacto.estadoChat = false;
                }
                setTimeout(() => {
                    this.ifChatCard = true;
                }, 500);
            }
        },



        getChatStyle() {
            return {
                borderRadius: '10px',
                boxShadow: 'rgba(0, 0, 0, 0.56) 0px 22px 70px 4px',
                height: '100%',
                width: '102%',
            };
        },

        getAlertStyle() {
            return {
                borderRadius: '20px',
                position: 'fixed',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                backgroundColor: 'rgb(227, 231, 252)',
                padding: '20px',
                border: '1px solid black',
                borderRadius: '10px',
                boxShadow: '0 6px 15px rgba(0, 0, 0, 0.5)',
                transition: 'box-shadow 0.3s ease-in-out',
                width: '20%'
            };
        },



        cerrarDIV() {
            this.alerta = false;
        },

        filterNumberNuevoContacto() {
        if (this.nuevoContactoTelefono < 573) {
            this.nuevoContactoTelefono = 573;
        }

        if (this.nuevoContactoTelefono && this.nuevoContactoTelefono.length > 12) {
            // Si tiene más de 10 dígitos, truncar el valor
            this.nuevoContactoTelefono = this.nuevoContactoTelefono.slice(0, 12);
        }
        },

        validarCelular(newCelular) {
            const onlyDigits = s => String(s ?? '').replace(/\D/g, '');
            const last10 = s => onlyDigits(s).slice(-10);

            const entered10 = last10(newCelular);

            if (!entered10) {
                this.alertaCelular = false;
                this.mensajeAlertaCelular = '';
        if (typeof this._updateDsGuardar === 'function') this._updateDsGuardar(false);
        else this.dsGuardar = false;
                return;
            }

            const myId = String(this.idProspectoSeleccionado ?? '0');
            const poolsForId = [this.listaEmpresasComercial, this.listaEmpresas, this.listaEmpresasComercial2, this.listaEmpresas2]
                .filter(Array.isArray);

            let myRecord = null;
            for (const arr of poolsForId) {
                const hit = arr.find(e => String(e?.id) === myId);
                if (hit) { myRecord = hit; break; }
            }
            const myPhone10 = last10(myRecord?.pc_celular || myRecord?.p_telefono1 || myRecord?.p_telefono2);

            if (this.estaEditando && myId !== '0' && myPhone10 && myPhone10 === entered10) {
                this.alertaCelular = false;
                this.mensajeAlertaCelular = '';
                if (typeof this._updateDsGuardar === 'function') this._updateDsGuardar();
                else this.dsGuardar = false;
                return;
            }

            axios.post(this.baseURL + 'api/validarcel', {
                id: this.idProspectoSeleccionado ? this.idProspectoSeleccionado : 0,
                cel: newCelular,
            })
                .then(({ data }) => {
                console.log("Validando celular...", data);
                const row = data?.data?.[0];

                if (!row || !row.res || String(row.res) === '0') {
                    this.alertaCelular = false;
                    this.mensajeAlertaCelular = '';
                    if (typeof this._updateDsGuardar === 'function') this._updateDsGuardar(false);
                    else this.dsGuardar = false;
                    return;
                }

                // Buscar en listas locales todas las empresas con ese celular
                const pools = [this.listaEmpresasComercial, this.listaEmpresas, this.listaEmpresasComercial2, this.listaEmpresas2]
                    .filter(Array.isArray);

                let empresasConCelular = [];
                for (const arr of pools) {
                    const encontrados = arr.filter(e => {
                    const phone10 = last10(e?.pc_celular || e?.p_telefono1 || e?.p_telefono2);
                    return phone10 && phone10 === entered10;
                    });
                    empresasConCelular = empresasConCelular.concat(encontrados);
                }

                // Si hay más de una empresa con ese celular, mostrar todas las razones sociales
                if (empresasConCelular.length > 1) {
                    const razones = empresasConCelular.map(e => e.p_razon_social || e.razon_social || '').filter(Boolean);
                    const nombres = razones.length ? razones.join(', ') : 'no disponible';
                    this.alertaCelular = true;
                    this.mensajeAlertaCelular = `Este número de celular está registrado en varias empresas: ${nombres}.`;
                    this.dsGuardar = true;
                    return;
                }

                // Si hay una sola empresa local con ese celular, mostrar el aviso normal
                if (empresasConCelular.length === 1) {
                    const razon = (empresasConCelular[0].p_razon_social || empresasConCelular[0].razon_social || '').toString().trim() || 'no disponible';
                    const ownerRaw = (row.nombre_comercial || row.nombre_contacto || empresasConCelular[0].comercial || empresasConCelular[0].nombre_contacto || empresasConCelular[0].vendedor || '').toString().trim() || 'no disponible';

                    const mismoOwner = this._equalsName
                    ? this._equalsName(ownerRaw, this.nombreComercial)
                    : (ownerRaw || '').toLowerCase() === (this.nombreComercial || '').toLowerCase();

                    if (mismoOwner) {
                    this.alertaCelular = true;
                    this.mensajeAlertaCelular = `Este número ya está registrado en tu cartera: empresa: "${razon}".`;
                    this.dsGuardar = true;
                    } else {
                    this.alertaCelular = true;
                    this.mensajeAlertaCelular =
                        `Este número de celular ya se encuentra asignado al contacto de la empresa "${razon}", manejado por el comercial: "${ownerRaw}".`;
                    this.dsGuardar = true;
                    }
                    return;
                }

                // Si el API dijo que existe pero no pude identificar dueño en memoria → usa nombre_comercial o nombre_contacto del API
                const nombreComercialApi = row.nombre_comercial || row.nombre_contacto || '';
                if (nombreComercialApi) {
                    this.alertaCelular = true;
                    this.mensajeAlertaCelular = `Este número de celular ya se encuentra asignado al contacto: ${nombreComercialApi}.`;
                    this.dsGuardar = true;
                } else {
                    this.alertaCelular = true;
                    this.mensajeAlertaCelular = 'Este número de celular ya se encuentra asignado a otro contacto.';
                    this.dsGuardar = true;
                }
                })
                .catch(err => {
                console.log(err);
                this.alertaCelular = false;
                this.mensajeAlertaCelular = '';
                if (typeof this._updateDsGuardar === 'function') this._updateDsGuardar(false);
                else this.dsGuardar = false;
                });
            },

            //AQUI COMIENZAN CASI QUE TODO LO QUE ES PROPIO DEL DIALOG DE CREAR PROSPECTO-->

             abrirFormularioProspecto() {
                this.cargarClientesActividad();
                this.llamadoTipoIdentificacion();
                this.llamadoSectores();
                this.llamadoTipoEmpresa();
                this.llamadoDepartamentos();
                this.llamadoCategorias();
                this.formularioProspecto = true;
                this.prospecto = null;
            },

            cerrarFormularioProspecto() {
            this.formularioProspecto = false;
            this.empresa = null;
            this.nit = null;
            this.tipoId = null;
            this.tipoEmp = null;
            this.sector = null;
            this.departamento = null;
            this.ciudad = null;
            this.web = null;
            this.correoEmpresa = null;
            this.tel1 = null;
            this.tel2 = null;
            this.razonSocial = null;
            this.direccion = null;
            this.alerta = false;
            this.mensajeAlerta = '';
            this.dsGuardar = false;
            },

            cargarClientesActividad() {
            axios.post(this.baseURL + 'api/cargarpp', {
                'idusu': localStorage.getItem('idUsuario'),
            })
                .then(response => {
                this.selectClientesActividad = response.data.data;
                this.empresas = response.data.data;
                console.log("this.empresas", this.empresas);
                this.prospectos = response.data.data;
                })
                .catch(error => {
                console.log(response.data[0].error);
                });
            },

            llamadoTipoIdentificacion() {

            axios.get(this.baseURL + 'api/cargarti')
                .then(response => {
                this.tipoIdentificacion = response.data.data;
                })
                .catch(error => {
                console.log(error);
                });
            },

            llamadoSectores() {
            axios.get(this.baseURL + 'api/cargarse')
                .then(response => {
                this.sectorEmpresa = response.data.data;
                })
                .catch(error => {
                console.log(error);
                });
            },

            llamadoTipoEmpresa() {

            axios.get(this.baseURL + 'api/cargarte')
                .then(response => {
                this.tipoEmpresa = response.data.data;
                })
                .catch(error => {
                console.log(error);
                });
            },

            llamadoDepartamentos() {
            axios.get(this.baseURL + 'api/cargarde')
                .then(response => {
                this.departamentos = response.data.data;
                })
                .catch(error => {
                console.log(error);
                });
            },

            llamadoCategorias() {
            axios.get(this.baseURL + 'api/cargarcc')
                .then(response => {
                this.categorias = response.data.data;
                })
                .catch(error => {
                console.log(error);
                });
            },

            llamadoCiudades(id) {

            axios.post(this.baseURL + 'api/cargarci', {
                'iddpto': id,
            })
                .then(response => {
                this.ciudades = response.data.data;
                })
                .catch(error => {
                console.log(error);
                });
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

            cargarServiciosActividad() {
            axios.get(this.baseURL + 'api/cargarsv')
                .then(response => {
                this.selectServiciosActividad = response.data.data;
                this.selectServiciosOportunidad = response.data.data;
                })
                .catch(error => {
                console.log(response.data[0].error);
                });
            },

            validarNit(nit) {
            axios.post(this.baseURL + 'api/validarnitraz', { nit, raz: '' })
                .then(({ data }) => {
                const row = data?.data?.[0];
                if (!row) {
                    this.alertaNit = false;
                    this.mensajeAlertaNit = '';
                    this.dsGuardar = false;
                    return;
                }
                if (row.comercial && row.comercial.toLowerCase() === (this.nombreComercial || '').toLowerCase()) {
                    this.mensajeAlertaNit = 'Este NIT ya está registrado en tu cartera.';
                } else {
                    this.mensajeAlertaNit = `Este NIT ya se encuentra asignado al comercial: ${row.comercial}`;
                }
                this.alertaNit = true;
                this.dsGuardar = true;
                })
                .catch(err => {
                console.log(err);
                });
            },

            // Valida Razón Social y muestra mensaje según el comercial asignado
            validarRazonSocial(newRazonSocial) {
            axios.post(this.baseURL + 'api/validarnitraz', { nit: '', raz: newRazonSocial })
                .then(({ data }) => {
                const row = data?.data?.[0];
                if (!row) {
                    this.alertaRazonSocial = false;
                    this.mensajeAlertaRazonSocial = '';
                    this.dsGuardar = false;
                    return;
                }
                if (row.comercial && row.comercial.toLowerCase() === (this.nombreComercial || '').toLowerCase()) {
                    this.mensajeAlertaRazonSocial = 'Esta razón social ya está registrada en tu cartera.';
                } else {
                    this.mensajeAlertaRazonSocial = `Esta razón social ya se encuentra asignada al comercial: ${row.comercial}`;
                }
                this.alertaRazonSocial = true;
                this.dsGuardar = true;
                })
                .catch(err => {
                console.log(err);
                });
            },

            mensajeSegunComercialNIT(comercial) {
            const esMismo = this._equalsName(comercial, this.nombreComercial);

            if (esMismo) {
                if (this.estaEditando) {
                // EDITANDO: no alertar
                this.alertaNit = false;
                this.mensajeAlertaNit = '';
                this.dsGuardar = false;
                return null;
                } else {
                // CREANDO: alertar "registrada"
                const msg = 'Esta empresa ya se encuentra asignada a ti';
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
                this.mensajeAlertaRazonSocial = '';
                this.dsGuardar = false;
                return null;
                } else {
                // CREANDO: alertar "registrada"
                const msg = 'Esta empresa ya se encuentra asignada a ti';
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
            return this.esElMismoNombrecomercial = this._normalize(comercial) === this._normalize(this.nombreComercial)
            },

            llamadoCargos(id) {

            axios.post(this.baseURL + 'api/cargarca', {
                'idcat': id,
            })
                .then(response => {
                this.cargos = response.data.data;
                })
                .catch(error => {
                console.log(error);
                });
            },

            async guardarDatos() {

        var contacto = false;
        // if (!this.nombre || !this.apellido || !this.cargo || !this.correoContacto || !this.celular || !this.extension) {
        // Valida los campos del contacto que son obligatorios
        if (!this.nit) {
            this.mensajeAlertLogin = 'Por favor, digite el NIT de la empresa';
            this.alerta = true;
            return;
        }
        else if (!this.razonSocial) {
            this.mensajeAlertLogin = 'Por favor, digite la razón social de la empresa';
            this.alerta = true;
            return;
        }
        else if (!this.departamento) {
            this.mensajeAlertLogin = 'Por favor, seleccione el departamento de la empresa';
            this.alerta = true;
            return;
        }
        else if (!this.ciudad) {
            this.mensajeAlertLogin = 'Por favor, seleccione la ciudad de la empresa';
            this.alerta = true;
            return;
        }

        if (this.web && !this.esUrlValida(this.web)) {
            this.mensajeAlertLogin = 'Por favor, ingrese una URL válida.';
            this.alerta = true;
            return;
        }

        if (this.correoEmpresa && !this.esCorreoValido(this.correoEmpresa)) {
            this.mensajeAlertLogin = 'Por favor, ingrese un correo válido.';
            this.alerta = true;
            return;
        }

        if (!this.selectedServicioProspecto) {
            this.mensajeAlertLogin = 'Por favor, Selecciona un servicio para el contacto';
            this.alerta = true;
            return;
        }
        const nitDuplicado = await this.validarNit(this.nit);
        const razonDuplicada = await this.validarRazonSocial(this.razonSocial);

        if (nitDuplicado || razonDuplicada || this.dsGuardar) {
            this.mensajeAlertLogin = this.mensajeAlertaNit || this.mensajeAlertaRazonSocial || 'Ya existe un prospecto con este NIT o razón social';
            this.alerta = true;
            this.ifCargando = false;
            return;
        }

        if (this.nombre && !this.apellido) {
            this.mensajeAlertLogin = 'Por favor, digite el apellido del contacto';
            this.alerta = true;
            return;
        }
        else if (!this.nombre && this.apellido) {
            this.mensajeAlertLogin = 'Por favor, digite el nombre del contacto';
            this.alerta = true;
            return;
        }
        else if (this.correoContacto && !this.esCorreoValido(this.correoContacto)) {
            this.mensajeAlertLogin = 'Por favor, ingrese un correo válido.';
            this.alerta = true;
            return;
        }

        console.log('tipoId:', this.tipoId ? this.tipoId.id : 0);
        console.log("url:" + this.baseURL);

        this.mensajeAlertLogin = 'Guardando prospecto...';
        this.alerta = true;
        this.ifCargando = true;


        console.log('Servicio: ', this.selectedServicioProspecto ? this.selectedServicioProspecto.id : 0);

        await axios.post(this.baseURL + 'api/newprospecto', {
            'nit': this.nit,
            'razon_social': this.razonSocial,
            'tipo_identif': this.tipoId ? this.tipoId.id : 0,
            'tipo_emp': this.tipoEmp ? this.tipoEmp.id : 0,
            'sector': this.sector ? this.sector.id : 0,
            'direccion': this.direccion ? this.direccion : '',
            'dpto': this.departamento ? this.departamento.id : 0,
            'ciudad': this.ciudad ? this.ciudad.id : 0,
            'web': this.web ? this.web : '',
            'correo': this.correoEmpresa ? this.correoEmpresa : '',
            'telefono1': this.tel1 ? this.tel1 : '',
            'telefono2': this.tel2 ? this.tel2 : '',
            'comercial': this.idUsuario,
            'servicio': this.selectedServicioProspecto ? this.selectedServicioProspecto.id : 0,
        })
            .then(response => {
            this.idEmpresa = response.data.data;
            })
            .catch(error => {
            console.log(error);
            });


        console.log('ID Empresa:', this.idEmpresa);
        
        if (this.nombre && this.apellido) {
            await axios.post(this.baseURL + 'api/newprospectocontacto', {
            'nombre': this.nombre ? this.nombre : '',
            'apellido': this.apellido ? this.apellido : '',
            'cargo': this.cargo ? this.cargo.id : 0,
            'correo': this.correoContacto ? this.correoContacto : '',
            'celular': this.celular ? this.celular : '',
            'extension': this.extension ? this.extension : '',
            'idemp': this.idEmpresa[0].id,
            })
            .then(response => {
                
                this.cerrarFormularioProspecto();
                this.cerrarFormularioContacto();
                contacto = true;
                setTimeout(() => {
                this.mensajeAlertLogin = 'Prospecto creado exitosamente';
                this.alerta = true;
                this.ifCargando = false;
                }, 600);
            })
            .catch(error => {
                console.log(error);
            });
        }
        if (!contacto) {
            this.cerrarFormularioProspecto();
            this.cerrarFormularioContacto();

            setTimeout(() => {
            this.mensajeAlertLogin = 'Prospecto creado exitosamente';
            this.alerta = true;
            this.ifCargando = false;
            }, 600);
        }
        this.cargarClientesActividad();
        },

        cerrarFormularioContacto() {
            this.formularioContacto = false;
            this.nombre = null;
            this.apellido = null;
            this.cargo = null;
            this.correoContacto = null;
            this.celular = null;
            this.extension = null;
            this.categoria = null;
        },

        esCorreoValido(correo) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(correo);
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

        esUrlValida(url) {
            const regex = /^(https?:\/\/)?([\w.-]+)+(:\d+)?(\/[\w./#-]*)*\/?$/;
            return regex.test(url);
        },

        setMenuActivoPorRuta() {
            const path = (this.$route.path || '').toLowerCase();
            if (path.includes('/vercampanas')) this.menuActivo = '/vercampanas';
            else if (path.includes('/campana')) this.menuActivo = '/campana';
            else if (path.includes('/contactos')) this.menuActivo = '/contactos';
            else if (path.includes('/prospeccion-telefonica')) this.menuActivo = '/prospeccion-telefonica';
            else if (path.includes('/seguimiento-llamadas')) this.menuActivo = '/seguimiento-llamadas';
            else if (path.includes('/informes-campanas')) this.menuActivo = '/informes-campanas';
            // ...agrega más si tienes otras rutas...
            else this.menuActivo = '';
            
        },

    //AQUI TERMINA CASI QUE TODOS LOS METODOS NECESARIOS PARA EL DIALOG DE CREAR PROSPECTO-->

    //METODOS NECESARIOS PARA EDITAR PROSPECTO:

    cargarProspecto(empresa) {
        this.dialogCrearEditarProspecto = true;
        this.idProspectoSeleccionado = empresa.id;
        this.dsGuardar = true;
        axios.post(this.baseURL + 'api/cargaproscon', {
        idprosp: empresa.id
        })
        .then(response => {
            const data = response.data.data[0];
            this.nitComercial = data.p_nit;
            this.razonSocialComercial = data.p_razon_social;
            this.tipoIdComercial = this.tipoIdentificacion.find(item => item.id == data.p_tipo_identif);
            this.sectorComercial = this.sectorEmpresa.find(item => item.id == data.p_sector);
            this.direccionComercial = data.p_direccion;
            this.departamentoComercial = this.departamentos.find(item => item.id == data.p_dpto);
            setTimeout(() => {
            this.ciudadComercial = this.ciudades.find(item => item.id == data.p_ciudad);
            }, 500);
            this.webComercial = data.p_web;
            this.correoEmpresaComercial = data.p_correo;
            this.tel1Comercial = data.p_telefono1;
            this.tel2Comercial = data.p_telefono2
            this.nombreComercial2 = data.pc_nombre;
            this.apellidoComercial = data.pc_apellido;
            this.categoriaComercial = this.categorias.find(item => item.id == data.pc_categoria);
            setTimeout(() => {
            this.cargoComercial = this.cargos.find(item => item.id == data.pc_cargo);
            this.dsGuardar = false;
            }, 500);
            this.correoContactoComercial = data.pc_correo;
            this.celularComercial = data.pc_celular;
            this.extensionComercial = data.pc_extension;
        })
        .catch(error => {
            console.error('Error al cargar prospecto:', error);
        });
    },

    validarNitEditarProspecto(nit) {
      // Busca el NIT original de la empresa que estás editando
      const empresaActual = this.findEmpresaActual(this.idProspectoSeleccionado);
      const nitOriginal = empresaActual ? String(empresaActual.p_nit || empresaActual.nit) : null;
      console.log("empresa Actual:", empresaActual);
      console.log("nit Original:", nitOriginal);

      axios.post(this.baseURL + 'api/validarnitraz', { nit: nit, raz: '' })
        .then(({ data }) => {
          const row = data?.data?.[0];
          // Si no hay duplicado, limpiar alertas
          if (!row) {
            this.alertaNit = false;
            this.mensajeAlertaNit = '';
            this.dsGuardar = false;
            return;
          }
          // Si el NIT encontrado es el mismo que el original, no mostrar alerta
          if (nit === nitOriginal) {
            this.alertaNit = false;
            this.mensajeAlertaNit = '';
            this.dsGuardar = false;
            return;
          }
          // Si el comercial es el mismo, mostrar mensaje personalizado
          if (row.comercial && row.comercial.toLowerCase() === (this.nombreComercial || '').toLowerCase()) {
            this.mensajeAlertaNit = 'Este NIT ya está registrado en tu cartera.';
          } else {
            this.mensajeAlertaNit = `Este NIT ya se encuentra asignado al comercial: ${row.comercial}`;
          }
          this.alertaNit = true;
          this.dsGuardar = true;
        })
        .catch(error => {
          console.log(error);
        });
    },

  // Validar Razón Social al editar
  validarRazonSocialEditarProspecto(newRazonSocial) {
      // Busca la Razón Social original de la empresa que estás editando
      const empresaActual = this.findEmpresaActual(this.idProspectoSeleccionado)
      const razonOriginal = empresaActual ? empresaActual.p_razon_social : null;

      axios.post(this.baseURL + 'api/validarnitraz', { nit: '', raz: newRazonSocial })
        .then(({ data }) => {
          const row = data?.data?.[0];
          // Si no hay duplicado, limpiar alertas
          if (!row) {
            this.alertaRazonSocial = false;
            this.mensajeAlertaRazonSocial = '';
            this.dsGuardar = false;
            return;
          }
          // Si la razón social encontrada es la misma que la original, no mostrar alerta
          if (newRazonSocial === razonOriginal) {
            this.alertaRazonSocial = false;
            this.mensajeAlertaRazonSocial = '';
            this.dsGuardar = false;
            return;
          }
          // Si el comercial es el mismo, mostrar mensaje personalizado
          if (row.comercial && row.comercial.toLowerCase() === (this.nombreComercial || '').toLowerCase()) {
            this.mensajeAlertaRazonSocial = 'Esta razón social ya está registrada en tu cartera.';
          } else {
            this.mensajeAlertaRazonSocial = `Esta razón social ya se encuentra asignada al comercial: ${row.comercial}`;
          }
          this.alertaRazonSocial = true;
          this.dsGuardar = true;
        })
        .catch(error => {
          console.log(error);
        });
    },

    // Guardar cambios del prospecto editado
    async actualizarProspecto() {
        this.mensajeAlertLogin = 'Actualizando prospecto...';
        this.alerta = true;
        this.ifCargando = true;

        await axios.post(this.baseURL + 'api/editprospecto', {
        'nit': this.nitComercial,
        'razon_social': this.razonSocialComercial,
        'tipo_identif': this.tipoIdComercial ? this.tipoIdComercial.id : 0,
        'tipo_emp': this.tipoEmpresaComercial ? this.tipoEmpresaComercial.id : 0,
        'sector': this.sectorComercial ? this.sectorComercial.id : 0,
        'direccion': this.direccionComercial,
        'dpto': this.departamentoComercial ? this.departamentoComercial.id : 0,
        'ciudad': this.ciudadComercial ? this.ciudadComercial.id : 0,
        'web': this.webComercial,
        'correo': this.correoEmpresaComercial,
        'telefono1': this.tel1Comercial,
        'telefono2': this.tel2Comercial,
        'comercial': this.idUsuario,
        'id': this.idProspectoSeleccionado,
        })
        .then(response => {
            console.log('Prospecto actualizado:', response.data);
        })
        .catch(error => {
            console.log(error);
        });

        await axios.post(this.baseURL + 'api/editprospectocontacto', {
        'nombre': this.nombreComercial2,
        'apellido': this.apellidoComercial,
        'categoria': this.categoriaComercial ? this.categoriaComercial.id : 0,
        'cargo': this.cargoComercial ? this.cargoComercial.id : 0,
        'correo': this.correoContactoComercial,
        'celular': this.celularComercial,
        'extension': this.extensionComercial,
        'id': this.idProspectoSeleccionado,
        })
        .then(response => {
            this.empresas = [];
            this.nuevoContactoEmpresa = null; 
            this.cargarClientesActividad();
            this.ifCargando = false;
            this.alerta = true;
            this.mensajeAlertLogin = 'Prospecto actualizado correctamente';
            setTimeout(() => {
            this.limpiarCamposProspecto();
            this.dialogCrearEditarProspecto = false;
            
            }, 1000);
        })
        .catch(error => {
            console.log(error);
        });
    },

    // Limpiar campos del prospecto
    limpiarCamposProspecto() {
        this.nitComercial = null;
        this.razonSocialComercial = null;
        this.tipoIdentificacionComercial = null;
        this.tipoEmpresaComercial = null;
        this.tipoIdComercial = null;
        this.sectorComercial = null;
        this.direccionComercial = null;
        this.departamentoComercial = null;
        this.ciudadComercial = null;
        this.webComercial = null;
        this.correoEmpresaComercial = null;
        this.tel1Comercial = null;
        this.tel2Comercial = null;
        this.nombreComercial2 = null;
        this.apellidoComercial = null;
        this.categoriaComercial = null;
        this.cargoComercial = null;
        this.correoContactoComercial = null;
        this.celularComercial = null;
        this.extensionComercial = null;
        this.idProspectoSeleccionado = null;
    },

    findEmpresaActual(id) {
    // Busca en empresas (del select) y en nuevoContactoEmpresa si está presente
    if (this.empresas && Array.isArray(this.empresas)) {
        const empresa = this.empresas.find(e => String(e.id) === String(id));
        if (empresa) return empresa;
    }
    if (this.nuevoContactoEmpresa && String(this.nuevoContactoEmpresa.id) === String(id)) {
        return this.nuevoContactoEmpresa;
    }
    return null;
    }
    
    }
}

</script>

<style scoped>
.btn-grow {
    transition: transform 0.2s;
}

.btn-grow:hover {
    transform: scale(1.15);
    z-index: 2;
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

.contact-card {
    background: linear-gradient(180deg, #ffffff 0%, #fafbff 100%);
    border: 1px solid rgba(0, 108, 161, .12);
    /* tu azul #006CA1, muy sutil */
    box-shadow: 0 2px 8px rgba(17, 24, 39, .06);
    transition: box-shadow .18s ease, transform .18s ease, border-color .18s ease;
}

.contact-card-selected {
    background: linear-gradient(100deg, #ffffff 60%, #e3f2fd 100%);
    border: 2.7px solid #1976D2;
    box-shadow: 0 6px 24px rgba(25, 118, 210, 0.18);
    transition: box-shadow .18s ease, transform .18s ease, border-color .18s ease;
}

.contact-card:hover {
    box-shadow: 0 10px 24px rgba(17, 24, 39, .12);
    border-color: rgba(0, 108, 161, .25);
}

/* Efecto grow que pediste */
.btn-grow-card {
    transform: translateZ(0);
}

.btn-grow-card:hover {
    transform: translateY(-2px);
}

/* Header */
.contact-header {
    padding: 12px 16px 8px;
}

.contact-title-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}

.contact-name {
    margin: 0;
    font-weight: 700;
    font-size: 16px;
    color: #0c1b2a;
}

.phone-pill {
    font-weight: 600;
    font-size: 13px;
    background: rgba(0, 108, 161, .12);
    color: #0b3a52;
    padding: 6px 10px;
    border-radius: 10px;
}

/* Body */
.contact-body {
    padding: 8px 16px 14px;
    border-top: 1px solid rgba(0, 0, 0, .06);
}

.contact-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}

/* Campos */
.contact-email {
    font-size: 13px;
    color: rgba(0, 0, 0, .62);
}

/* Chips suaves para empresa y NIT */
.meta-chip {
    display: inline-flex;
    align-items: center;
    padding: 4px 10px;
    border-radius: 10px;
    border: 1px solid rgba(0, 0, 0, .06);
    background: rgba(0, 0, 0, .035);
    color: #11161e;
    font-size: 12px;
}

/* Badge de WhatsApp posicionado bonito */
.wsp-badge {
    align-self: flex-start;
}

.menu-link {
    color: #1976D2;
    cursor: pointer;
    text-decoration: underline;
    font-size: 1rem;
    margin-bottom: 8px;
    font-weight: 500;
    transition: color 0.2s;
    width: fit-content;
}

.menu-link:hover {
    color: #0A1C3A;
    text-decoration: underline;
}

.contact-card-text {
    font-size: 0.9rem;
    /* tamaño normal para pantallas grandes */
}

.modern-input .v-input__control {
  background: #f0f4fa !important;
  border-radius: 10px !important;
  box-shadow: none !important;
  border: 1.5px solid #e3eaf5 !important;
  transition: border-color 0.2s;
}
.modern-input .v-input__control:focus-within {
  border-color: #1976D2 !important;
}

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
  border-color: #007BFF;
  /* azul al enfocar */
  box-shadow: 0 0 3px rgba(0, 123, 255, 0.5);
}


@media (max-width: 1060px) {
    .contact-card {
        min-height: 56px !important;
        padding: 2px 3px !important;
    }

    .contact-card-selected {
        min-height: 56px !important;
        padding: 2px 3px !important;
    }

    .contact-card-text {
        font-size: 0.68rem;
        max-width: 90px;
    }

    .phone-pill {
        font-size: 0.68rem;
        padding: 1px 5px;
        max-width: 90px;
    }

    .contact-email {
        font-size: 0.68rem;
        max-width: 100px;
        padding: 1px 4px;
    }

    .meta-chip {
        font-size: 0.62rem;
        padding: 1px 4px;
        max-width: 70px;
    }

    .v-avatar {
        width: 24px !important;
        height: 24px !important;
        font-size: 0.85rem !important;
    }

    .pa-2 {
        padding: 1px !important;
    }

    .mr-1,
    .ml-1 {
        margin-right: 2px !important;
        margin-left: 2px !important;
    }

    .d-flex {
        gap: 3px !important;
    }

}

.modern-alert {
  background: #fff0f3 !important;
  color: #b71c1c !important;
  border-radius: 10px !important;
  box-shadow: 0 2px 8px #b71c1c22;
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