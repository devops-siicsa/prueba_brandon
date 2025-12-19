<template>
  <v-app>
    <AppHeader :imagenComercial="imagenComercial" />

    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-row class="mx-auto my-auto pt-2" style="color: #666 !important;">
        <v-card-text class="pt-0">
          <v-row class="mb-4">
            <!-- IZQUIERDA -->
            <v-col>
              <div class="text-subtitle-1">
                <v-row>
                  <v-col>
                    <h1>Lista de tareas </h1>
                  </v-col>

                  <v-col>
                    <v-tooltip text="Regresar al Panel Principal" location="top">
                      <template #activator="{ props }">
                        <v-icon @click="$router.push('/comercial')" v-bind="props" size="30" class="mt-4 ml-n16 btn-grow"
                          color="#006CA1">
                          mdi-arrow-left-circle-outline
                        </v-icon>
                      </template>
                    </v-tooltip>
                  </v-col>
                </v-row>
              </div>
              <div class="text-subtitle-2 font-bold">
                <h2>{{ razon_social }}
                  <v-tooltip location="top">
                    <template #activator="{ props }">
                      <v-icon v-bind="props" color="#006CA1" icon="mdi-eye-circle" class="cursor-pointer"
                        @click="infoParaMostrarProspecto(idempresa);"></v-icon>
                    </template>
                    <div>
                      <div><strong>Nombre:</strong> {{ nombreClienteInfo && nombreClienteInfo !== 'null' ?
                        nombreClienteInfo
                        : '' }}</div>
                      <div><strong>Teléfono:</strong> {{ telefonoClienteInfo && telefonoClienteInfo !== 'null' ?
                        telefonoClienteInfo : '' }}</div>
                      <div><strong>Contacto:</strong> {{ contactoClienteInfo && contactoClienteInfo !== 'null' ?
                        contactoClienteInfo : '' }}</div>
                      <div><strong>Celular:</strong> {{ celularClienteInfo && celularClienteInfo !== 'null' ?
                        celularClienteInfo : '' }}</div>
                      <div><strong>Dirección:</strong> {{ direccionClienteInfo && direccionClienteInfo !== 'null' ?
                        direccionClienteInfo : '' }}</div>
                      <div><strong>Departamento:</strong> {{ departamentoClienteInfo && departamentoClienteInfo !==
                        'null' ?
                        departamentoClienteInfo : '' }}</div>
                      <div><strong>Ciudad:</strong> {{ ciudadClienteInfo && ciudadClienteInfo !== 'null' ?
                        ciudadClienteInfo
                        : '' }}</div>
                    </div>
                  </v-tooltip>
                </h2>
              </div>

            </v-col>

            <!-- CENTRO -->
            <v-col v-if="estadoSeguimientos != 4 && estadoSeguimientos != 5">
              <v-tooltip text="Añadir una nueva actividad a la lista" location="top">
                <template #activator="{ props }">
                  <v-btn color="#006CA1" class="mt-4 btn-grow" @click="crearNuevaActividad()"
                    :readonly="ifBotonActividadCargando" :loading="ifBotonActividadCargando" v-bind="props" icon>
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </template>
              </v-tooltip>
            </v-col>

            <!-- DERECHA -->
            <v-col v-if="false">
              <v-card variant="tonal" color="blue" class="pa-4 rounded-xl	"
                style="width: 100%; max-width: 400px; float: right;">
                <div>
                  <span style="font-weight: bold;">Actividad reciente: {{ ultact }}:</span>
                  {{ ultactfec }}
                </div>
                <div>
                  <span style="font-weight: bold;">Actividad a seguir: {{ ultseg }}:</span>
                  {{ ultsegfec }}
                </div>
              </v-card>
            </v-col>
            <v-tooltip text="Ver el historial de actividades y notificaciones" location="left">
              <template #activator="{ props }">
                <v-btn color="#006CA1" class="mt-7 mr-4 btn-grow"
                  @click="dialogHistorico = true; cargarObservaciones(); cargarHistorialLlamadas();" v-bind="props"
                  icon>
                  <v-icon>mdi mdi-archive-clock</v-icon>
                </v-btn>
              </template>
            </v-tooltip>
          </v-row>
        </v-card-text>
      </v-row>

      <v-container fluid class="pa-0">
        <v-row class="mx-auto mt-n12">
          <v-col v-for="(column, index) in estados" :key="index" cols="12" sm="6" md="4" lg="2">
            <v-card elevation="4" class="rounded-lg fill-height" style="overflow-y: auto;">
              <v-card-title :class="column.color" class="text-white text-subtitle-1 font-weight-bold">

                <v-row class="pa-4" style="align-items: center;">
                  <div style="white-space: pre-wrap;">
                    <v-icon size="16">
                      {{
                        column.id === 1 ? 'mdi-phone' :
                          column.id === 2 ? 'mdi-gmail' :
                            column.id === 3 ? 'mdi-calendar-cursor-outline' :
                              column.id === 4 ? 'mdi-monitor-account' :
                                column.id === 5 ? 'mdi-laptop' :
                                  column.id === 6 ? 'mdi-point-of-sale' : 'mdi-calendar'
                      }}
                    </v-icon>
                    {{ column.nombre }} {{ column.items.length > 0 ? '(' + column.items.length + ')' : '' }}
                  </div>

                  <v-tooltip location="top">
                    <template #activator="{ }">
                      <v-img v-if="column.id == ultsegAct && (this.estadoactual <= 3)" src="/icon-bell.gif"
                        :src="`${this.baseURL}images/icon-bell.gif?${Date.now()}`" width="20" height="20" />
                    </template>
                  </v-tooltip>
                </v-row>
              </v-card-title>
              <v-card-text class="pa-2">

                <!--Card de Recordatorio-->

                <v-card v-if="column.id == ultsegAct && (this.estadoactual <= 3)" class="mx-auto btn-grow-card mb-4"
                  :style="{ backgroundColor: '#e8fafc', }" elevation="5" max-width="600"
                  @click="dialogObsCompleta = true" style="cursor: pointer;">
                  <v-card-title :style="{ backgroundColor: '#00ACC1', color: 'white' }"
                    class="text-subtitle-1 font-weight-bold">
                    <template #activator="{ }">
                      <v-img v-if="column.id == ultsegAct" src="/icon-bell.gif"
                        :src="`${this.baseURL}images/icon-bell.gif?${Date.now()}`" width="30" height="0" />
                    </template>
                    Recordatorio de Seguimiento
                  </v-card-title>

                  <v-card-text>

                    <v-row class="mb-3 mt-3" align="center" no-gutters>
                      <v-col cols="auto">
                        <v-icon color="#015154" class="mr-2">mdi-clipboard-check-outline</v-icon>
                      </v-col>
                      <v-col>
                        <span class="font-weight-medium" style="color: #014042"> Última Actividad:</span>
                        <span class="ml-2">
                          <p></p>
                          {{ ultact || 'No disponible' }}
                        </span>
                      </v-col>
                    </v-row>
                    <!-- Titulo de Fecha

                <v-row class="mb-3 mt-3" align="center" no-gutters>
                  <v-col cols="auto">
                    <v-icon color="#015154" class="mr-2">mdi-calendar-clock</v-icon>
                  </v-col>
                  <v-col>
                    <span class="font-weight-medium" style="color:#014042">Fecha:</span>
                    <span class="ml-2" >
                      <p></p>
                      {{  ultactfec || 'No disponible' }}
                    </span>
                  </v-col>
                </v-row>
                -->

                    <v-row align="start" no-gutters>
                      <v-col cols="auto">
                        <v-icon color="#015154" class="mr-2 mt-1">mdi-text-box-outline</v-icon>
                      </v-col>
                      <v-col>
                        <div class="font-weight-medium">
                          <p style="color: #014042">Observaciones: </p>
                        </div>
                        <div class="text-body-2 mt-1"
                          style="text-align: justify; line-height: 1.1; word-break: break-word;">
                          {{ textoObservacionCorto || 'Sin observaciones registradas.' }}
                        </div>
                      </v-col>
                    </v-row>
                  </v-card-text>
                </v-card>

                <!--DIALOGO DEL CARD DE RECORDATORIO-->
                <v-dialog v-model="dialogObsCompleta" max-width="600" :scrim="'rgba(0, 0, 0, 0.5)'">
                  <v-card>
                    <v-card-title class="text-h6" style="background-color: #00ACC1; color: white;">
                      <v-icon class="mr-2">mdi-bell-alert</v-icon>
                      Detalle del Seguimiento
                    </v-card-title>

                    <v-card-text>
                      <v-row class="mb-100" align="center">
                        <v-col cols="auto ">
                          <v-icon color="#015154">mdi-clipboard-check-outline</v-icon>
                        </v-col>
                        <v-col>
                          <span class="font-weight-bold">Última Actividad:</span>
                          <div>
                            <span class="">{{ ultact || 'No disponible' }}</span>
                          </div>

                        </v-col>
                      </v-row>

                      <v-row class="mb-100" align="start">
                        <v-col cols="auto">
                          <v-icon color="#015154" class="mt-1">mdi-text-box-outline</v-icon>
                        </v-col>
                        <v-col>
                          <span class="font-weight-bold">Observaciones:</span>
                          <div class="text-body-2 mt-1"
                            style="text-align: justify; line-height: 1.3; word-break: break-word;">
                            {{ ultsegObser || 'Sin observaciones registradas.' }}
                          </div>
                        </v-col>
                      </v-row>

                      <v-row class="mb-100" align="center">
                        <v-col cols="auto">
                          <v-icon color="#015154">mdi-calendar-clock</v-icon>
                        </v-col>
                        <v-col>
                          <span class="font-weight-bold">Fecha Programada del Seguimiento:</span>
                          <div>
                            <span class="">{{ formatDate(this.ultsegfec) || 'No disponible' }}</span>
                          </div>

                        </v-col>
                      </v-row>
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer />
                      <v-btn color="primary" text @click="dialogObsCompleta = false">Cerrar</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-tooltip v-for="(item, i) in column.items" :key="i" :open-on-hover="true" content-class="bg-blue"
                  max-width="400">
                  <template v-slot:activator="{ props }">
                    <v-card @click="abrirFormularioActividad(item, column)" class="mb-3 btn-grow-card"
                      variant="elevated" rounded="lg" elevation="4" v-bind="props" :style="{
                        backgroundColor: item.colorrec || '#e8fafc',
                        padding: '10px 16px',
                        border: '1px #d0d7de',
                        cursor: 'pointer'
                      }">
                      <v-row no-gutters>
                        <v-col>
                          <div class="font-weight-bold text-subtitle-2 mb-1">
                            {{ item.name }}
                            <v-icon size="20" color="green">
                              {{ 'mdi-check-all' }}
                            </v-icon>
                          </div>
                          <div class="text-caption text-grey-darken-1 mb-1">
                            {{ item.description }}
                          </div>
                          <div v-if="item.date" class="text-caption d-flex align-center mb-1">
                            <v-icon size="16" class="mr-1">
                              {{
                                column.id === 1 ? 'mdi-phone' :
                                  column.id === 2 ? 'mdi-gmail' :
                                    column.id === 3 ? 'mdi-calendar-cursor-outline' :
                                      column.id === 4 ? 'mdi-monitor-account' :
                                        column.id === 5 ? 'mdi-laptop' :
                                          column.id === 6 ? 'mdi-point-of-sale' : 'mdi-calendar'
                              }}
                            </v-icon>
                            {{ item.date }}
                          </div>

                          <div v-if="item.estadoCotizado === 'Cotizado'" class="text-caption text-grey-darken-2">
                            Cotizado
                          </div>

                          <div
                            v-if="item.colorrec == '#f3f5cd' || item.colorrec == '#f5cdcd' || item.colorrec == '#cdf5d5'"
                            class="text-caption mt-1">
                            Actividad Reciente
                          </div>
                        </v-col>

                        <v-col cols="auto" class="d-flex flex-column justify-space-between align-end">
                          <v-icon size="20" color="nlack" v-if="item.iconoEstado">
                            {{ item.iconoEstado }}
                          </v-icon>
                        </v-col>
                      </v-row>
                    </v-card>
                  </template>

                  <span style="white-space: pre-line;">{{ item.obsev }}</span>
                </v-tooltip>

              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

      <v-dialog v-model="dialogNuevaActividad" max-width="600px" height="100vh" class="mb-100" persistent>
        <v-card-title class="text-h6"
          style="background-color: #006CA1; color: white; display: flex; align-items: center;">

          <div class="d-flex align-center">
            <v-icon class="mr-2">mdi mdi-pencil-plus </v-icon>
            Registrar Tarea
          </div>

          <v-spacer></v-spacer>

          <v-tooltip text="Ver historico" location="top" v-if="ifHistorico">
            <template #activator="{ props }">
              <v-btn icon="mdi mdi-archive-clock" size="small" color="white"
                @click="dialogHistorico = true; cargarObservaciones(); cargarHistorialLlamadas();" class="btn-grow mr-4"
                v-bind="props" />
            </template>

          </v-tooltip>

          <v-btn icon="mdi-close" size="small" color="white"
            @click="limpiarCamposDialogActividad(); dialogNuevaActividad = false; cargarEstadosActividad();"
            class="btn-grow" />

        </v-card-title>
        <v-card>
          <v-card-title class="font-weight-bold mt-2 ml-2"> Estado Actual:</v-card-title>


          <v-card-text>

            <v-row class="mt-n4">
              <v-col>
                <v-autocomplete label="Cliente" v-model="selectedClienteActividad" :items="selectClientesActividad"
                  return-object item-title="p_razon_social" item-value="id" variant="outlined"
                  :readonly="roClienteActividad">
                  <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-domain</v-icon>
                  </template>
                </v-autocomplete>
              </v-col>

            </v-row>

            <v-row class="mt-n2">
              <v-col>
                <v-select label="Estado actual del cliente" v-model="selectedEstadoActividad"
                  :items="selectEstadosActividad" return-object item-title="nombre" item-value="id" variant="outlined"
                  :readonly="roEstadoActividad">
                  <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-list-status</v-icon>
                  </template>
                </v-select>
              </v-col>
            </v-row>

            <v-row class="mt-n6">
              <v-col>
                <v-select label="Servicio" :readonly="readonlyServicioSeleccionado" v-model="selectedServicioActividad"
                  :items="selectServiciosActividad" return-object item-title="nombre" item-value="id"
                  variant="outlined">
                  <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-list-box-outline</v-icon>
                  </template>
                </v-select>
              </v-col>
            </v-row>

            <v-row class="mt-n6" v-if="ifValorProyecto">
              <v-col>
                <v-text-field label="Valor del Proyecto" variant="outlined" v-model="selectedValorProyecto"
                  type="number">
                  <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-currency-usd</v-icon>
                  </template>
                </v-text-field>
              </v-col>
            </v-row>

            <v-row class="mt-n4 mt-2"
              v-if="(rutaCot && rutaRut && rutaCot !== 'null' && rutaRut !== 'null') || ifHistorico || (selectedEstadoActividad?.id == 3 && ifDocumentos)">
              <v-col>
                <!-- Documento Cotización -->
                <div class="font-weight-bold mb-1">Documento Cotización:</div>
                <div class="d-flex align-center flex-row mb-4" style="gap: 16px;">
                  <a v-if="rutaCot && rutaCot !== 'null'" :href="rutaCot" target="_blank" class="ml-2"
                    style="display: flex; align-items: center; text-decoration: none;">
                    <v-tooltip text="Ver documento cotización" location="top">
                      <template #activator="{ props }">
                        <v-icon class="btn-grow" color="#1976D2" size="30" v-bind="props" style="cursor:pointer;">mdi
                          mdi-text-box</v-icon>
                      </template>
                    </v-tooltip>
                  </a>
                  <v-tooltip text="Actualizar documento cotización" location="top"
                    v-if="!(selectedEstadoActividad?.id === 3 && !rutaCot)">
                    <template #activator="{ props }">
                      <v-icon v-if="ifActCotizado && rutaCot && rutaCot !== 'null'" color="#006CA1" class="btn-grow"
                        style="cursor:pointer;" v-bind="props" size="28"
                        @click="mostrarInputCot = !mostrarInputCot">mdi-pencil</v-icon>
                    </template>
                  </v-tooltip>
                  <v-file-input
                    v-if="subirArchivoDOC && ifDocumentos && (selectedEstadoActividad?.id === 3 && !rutaCot || rutaCot === 'null' || mostrarInputCot)"
                    label="Adjuntar documento" density="compact" variant="outlined" clearable
                    v-model="archivosActividad" class="pt-4 pl-2" style="width: 100%;"></v-file-input>
                  <span
                    v-if="validandoActividad && !this.rutaCot && (!this.archivosActividad || this.archivosActividad.length === 0)"
                    class="titulo-error pa-0 a" style="font-size: 14px;">
                    Este campo es obligatorio
                  </span>
                </div>


                <!-- Documento RUT -->
                <div class="font-weight-bold mb-0 mt-2">Documento RUT:</div>
                <div class="d-flex align-center flex-row mb-4" style="gap: 16px;">
                  <a v-if="rutaRut && rutaRut !== 'null'" :href="rutaRut" target="_blank" rel="noopener" class="ml-2"
                    style="display: flex; align-items: center; text-decoration: none;">
                    <v-tooltip text="Ver documento RUT" location="top">
                      <template #activator="{ props }">
                        <v-icon class="btn-grow" color="#1976D2" size="34" v-bind="props" style="cursor:pointer;">mdi
                          mdi-text-box</v-icon>
                      </template>
                    </v-tooltip>
                  </a>
                  <v-tooltip text="Actualizar documento RUT" location="top"
                    v-if="!(selectedEstadoActividad?.id === 3 && !rutaRut)">
                    <template #activator="{ props }">
                      <v-icon v-if="ifActCotizado && rutaRut && rutaRut !== 'null'" color="#006CA1" class="btn-grow"
                        style="cursor:pointer;" v-bind="props" size="28"
                        @click="mostrarInputRUT = !mostrarInputRUT">mdi-pencil</v-icon>
                    </template>
                  </v-tooltip>
                  <v-file-input
                    v-if="subirArchivoRUT && ifDocumentos && (selectedEstadoActividad?.id === 3 && !rutaRut || rutaRut === 'null' || mostrarInputRUT)"
                    label="Adjuntar RUT" density="compact" variant="outlined" clearable v-model="archivoRUT"
                    class="pt-4 pl-2" style="width: 100%;"></v-file-input>
                  <span v-if="validandoActividad && !this.rutaRut && (!this.archivoRUT || this.archivoRUT.length === 0)"
                    class="titulo-error pa-0 ma-0" style="font-size: 14px;">
                    Este campo es obligatorio
                  </span>
                </div>

              </v-col>
            </v-row>

            <v-row class="mt-n4" v-if="ifActividad || ifActCotizado">
              <v-col>
                <h3 class="font-weight-bold" :class="{ 'titulo-error': validandoActividad && !idActividad }">Actividad
                  Realizada:
                </h3>
                <div v-if="validandoActividad && !idActividad" class="titulo-error" style="font-size: 14px;">
                  Este campo es obligatorio
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col class="mt-n2 mb-n2">
                <v-select v-model="selectedActividad" :items="opcionesActividadSelected"
                  v-if="!ifCerradoDeclinado && !ifCerradoExitoso" label="Que actividad he realizado" item-value="id"
                  variant="outlined" return-object :error="validandoActividad && !selectedActividad"
                  :error-messages="validandoActividad && !selectedActividad ? 'Este campo es obligatorio' : ''">
                  <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-clipboard-list</v-icon>
                  </template>
                  <template #item="{ item, props }">
                    <!-- Se filtran props para evitar duplicado -->
                    <v-list-item :key="item.raw.id" @click="props.onClick" :value="props.value"
                      class="d-flex align-center">
                      <v-icon class="me-2">{{ item.raw.icono }}</v-icon>
                      <span>{{ item.raw.nombre }}</span>
                    </v-list-item>
                  </template>

                  <template #selection="{ item }">
                    <div class="d-flex align-center">
                      <v-icon class="me-2" color="#006CA1">{{ item.raw.icono }}</v-icon>
                      {{ item.raw.nombre }}
                    </div>
                  </template>
                </v-select>
              </v-col>
            </v-row>


            <v-row class="mt-n2" v-if="ifObservaciones">
              <v-col class="mb-0">
                <v-textarea label="Observaciones sobre la actividad que se realizo" rows="4" variant="outlined"
                  v-if="!ifCerradoDeclinado || !ifCerradoExitoso" density="compact"
                  v-model="selectedObservacionesActividad" clearable>
                  <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-eye</v-icon>
                  </template>
                </v-textarea>
              </v-col>
            </v-row>


            <v-row class="mt-n2" v-if="ifComentariosAdicionales">
              <v-col>
                <v-textarea label="Comentarios adicionales" rows="4" variant="outlined" density="compact"
                  v-model="selectedComentariosActividad" clearable
                  :error="validandoActividad && !proximoSeguimientoActividad"
                  :error-messages="validandoActividad && !proximoSeguimientoActividad ? 'Este campo es obligatorio' : ''"
                  color="red">
                  <template v-slot:prepend-inner>
                    <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-text-box-outline</v-icon>
                  </template>
                </v-textarea>
              </v-col>
            </v-row>
            <section v-if="this.selectedActividad">
              <v-row class="mt-n4" v-if="ifProximoSeguimientoActividad">
                <v-col>
                  <h3 :class="{ 'titulo-error': validandoActividad && !idActividad }">Próximo Seguimiento a Realizar:
                  </h3>
                  <div v-if="validandoActividad && !idActividad" class="titulo-error" style="font-size: 14px;">
                    Este campo es obligatorio
                  </div>
                </v-col>
              </v-row>

              <v-row>

                <v-col class="mt-n2" v-if="ifProximoSeguimientoActividad">
                  <v-text-field type="date" clearable label="Próximo seguimiento" v-model="proximoSeguimientoActividad"
                    variant="outlined" :min="fechaActual" :error="validandoActividad && !proximoSeguimientoActividad"
                    :error-messages="validandoActividad && !proximoSeguimientoActividad ? 'Este campo es obligatorio' : ''"
                    color="red">
                    <template v-slot:prepend-inner>
                      <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-calendar</v-icon>
                    </template>
                  </v-text-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col class="mt-n2">
                  <v-select v-model="selectedSeguimiento" :items="opcionesSeguimientoSelected"
                    label="Que Seguimiento se realizará" item-value="id" variant="outlined" return-object
                    :error="validandoActividad && !selectedActividad"
                    :error-messages="validandoActividad && !selectedActividad ? 'Este campo es obligatorio' : ''"
                    v-if="ifProximoSeguimientoActividad">
                    <template v-slot:prepend-inner>
                      <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-clipboard-plus</v-icon>
                    </template>
                    <template #item="{ item, props }">
                      <!-- Se filtran props para evitar duplicado -->
                      <v-list-item :key="item.raw.id" @click="props.onClick" :value="props.value"
                        class="d-flex align-center">
                        <v-icon class="me-2">{{ item.raw.icono }}</v-icon>
                        <span>{{ item.raw.nombre }}</span>
                      </v-list-item>
                    </template>

                    <template #selection="{ item }">
                      <div class="d-flex align-center">
                        <v-icon color="#006CA1" class="me-2">{{ item.raw.icono }}</v-icon>
                        {{ item.raw.nombre }}
                      </div>
                    </template>
                  </v-select>
                </v-col>
              </v-row>

              <v-row class="mt-n2" v-if="ifProximoSeguimientoActividad">
                <v-col>
                  <v-textarea label="Observaciones del Seguimiento a Realizar" rows="4" variant="outlined"
                    density="compact" v-model="selectedObservacionesSeguimiento" clearable>
                    <template v-slot:prepend-inner>
                      <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-eye</v-icon>
                    </template>
                  </v-textarea>
                </v-col>
              </v-row>
            </section>

          </v-card-text>

          <v-row class="mt-n4">
            <v-col>
              <v-btn v-if="ifBtnRegistrarActividad" color="blue" class="ml-2 btn-grow-card" style="float: right;"
                @click="registrarActividad()">Registrar
                Actividad</v-btn>
              <v-btn color="blue" class="btn-grow-card" style="float: right;"
                @click="limpiarCamposDialogActividad(); dialogNuevaActividad = false; cargarEstadosActividad();">Cerrar</v-btn>
            </v-col>
          </v-row>

        </v-card>
      </v-dialog>

      <v-dialog v-model="dialogHistorico" max-width="200vh" height="100vh" persistent>
        <v-card class="pa-4" style="height: 100%;">
          <v-card variant="outlined" elevation="5" class="pa-4 rounded-xl d-flex flex-column" style="height: 100%;">

            <!-- Encabezado -->
            <div style="position: sticky; top: 0; z-index: 2; margin-bottom: 2vh;" class="rounded-xs">

              <v-alert color="#027cb8" class="mb-4 pa-4 rounded-xs ">
                <v-row align="center" justify="space-between" class="ma-0 pa-0">
                  <!-- Título a la izquierda -->
                  <v-col cols="12" md="4" class="d-flex align-center">
                    <v-icon size="26" color="white ">mdi-clock-outline</v-icon>
                    <h2 class="ml-2 mb-0" style="">Observación General del Proyecto</h2>

                  </v-col>
                  <!-- Buscadores y botón a la derecha -->
                  <v-col cols="12" md="8" class="d-flex justify-end align-center" style="gap: 20px;">
                    <!-- Buscar por observación -->
                    <v-text-field v-model="busquedaHistorial" placeholder="Buscar por observación…" density="compact"
                      variant="solo" bg-color="rgba(255,255,255, 0.9)" base-color="rgba(255,255,255, 0.9)" color="white"
                      prepend-inner-icon="mdi-magnify" clearable rounded="lg" hide-details style="max-width: 320px;" />

                    <!-- Buscar por fecha (input nativo) -->
                    <v-text-field v-model="busquedaFecha" type="date" density="compact" variant="solo"
                      bg-color="rgba(255,255,255, 0.9)" base-color="rgba(255,255,255, 0.9)" color="white"
                      prepend-inner-icon="mdi-calendar" clearable rounded="lg" hide-details style="max-width: 220px;" />

                    <!-- Botón con tooltip hacia arriba -->
                    <v-tooltip text="Ordenar Lista en orden descendente" location="top">
                      <template #activator="{ props }">
                        <v-btn icon size="small" v-bind="props" @click="ordenLista = !ordenLista">
                          <v-icon color="black">mdi mdi-order-bool-descending</v-icon>
                        </v-btn>
                      </template>
                    </v-tooltip>
                    <v-tooltip text="Recargar Todas las observaciones" location="top">
                      <template #activator="{ props }">
                        <v-btn icon size="small" v-bind="props"
                          @click="filtroEstadoId = null; limpiarCamposHistorial(), cargarObservaciones(); cargarHistorialLlamadas();">
                          <v-icon color="black">mdi-cached</v-icon>
                        </v-btn>
                      </template>
                    </v-tooltip>
                    <v-tooltip text="Cerrar Historial de Actividades" location="top">
                      <template #activator="{ props }">
                        <v-btn icon size="small" class=" btn-grow" v-bind="props" @click="dialogHistorico = false">
                          <v-icon color="black">mdi mdi-window-close</v-icon>
                        </v-btn>
                      </template>
                    </v-tooltip>
                  </v-col>
                  <div class="font-weight-bold text-subtitle-1 mb-1 ml-11">
                    <h5 style="color: white;">{{ observacionGeneral }}</h5>
                  </div>
                </v-row>
              </v-alert>
            </div>

            <div>
              <v-row style="overflow-x: auto;">
                <v-timeline direction="horizontal" class="mx-2 mb-2" side="start" fill-dot line-color="black"
                  line-thickness="2">
                  <v-timeline-item v-for="estado in estados2" :key="estado.id"
                    :dot-color="filtroEstadoId === estado.id ? estado.color : '#bdbdbd'" size="x-small" fill-dot>
                    <v-card @click="filtroEstadoId = filtroEstadoId === estado.id ? null : estado.id"
                      :color="filtroEstadoId === estado.id ? estado.color : estado.color" class="pa-2 btn-grow"
                      style="white-space: pre; cursor:pointer; min-width:120px; text-align:center; font-weight:600;"
                      :elevation="filtroEstadoId === estado.id ? 8 : 2">
                      <v-icon class="mt-n1 mr-1" color="white">{{ estado.icon }}</v-icon>
                      <span color="white">{{ estado.nombre }}</span>
                    </v-card>
                  </v-timeline-item>
                </v-timeline>
              </v-row>
            </div>

            <!-- Cuerpo scroll -->
            <!-- Contenedor scrollable con scrollbar estilizado -->
            <div style="overflow-y: auto; flex: 1; max-height: 60vh;" class="mt-2 mb-2 ml-2 custom-scroll">
              <p class="text-h6 font-weight-bold ml-10">Historial de Llamadas</p>
              <div class="timeline-container pa-4" style="height: 200px; overflow-y: auto;">
                <div v-for="(gestion, idx) in historialGestion" :key="gestion.id" class="timeline-item">
                  <!-- Línea vertical y punto -->
                  <div class="timeline-marker" :class="timelineColor(gestion.interes)">
                    <v-icon :color="timelineIconColor(gestion.interes)" size="22">
                      {{ timelineIcon(gestion.interes) }}
                    </v-icon>
                  </div>
                  <div class="timeline-content">
                    <p class="mt-2"><strong>Nombre Campaña: </strong>{{
                      gestion.nombre_campaña
                    }}</p>
                    <div class="d-flex align-center justify-space-between">
                      <span class="timeline-date">{{ formatDate2(gestion.fecha)
                      }}</span>
                      <span class="timeline-type">
                        <v-icon size="18" :color="timelineIconColor(gestion.interes)">
                          {{ timelineIcon(gestion.interes) }}
                        </v-icon>
                        {{ interesToText(gestion.interes) }}
                      </span>
                      <span v-if="gestion.Editado == 'Si'" class="ml-2"
                        style="font-size: 10px; color: red; font-weight: bold;">
                        🖋️ Editado
                      </span>
                      <v-btn v-if="gestion.Editado == 'Si'" icon variant="text" color="primary" class="ml-2"
                        title="Ver historial de ediciones" @click="abrirHistorialEdiciones(gestion)">
                        <v-icon style="font-size: 16px;">mdi-history</v-icon>
                      </v-btn>
                    </div>
                    <div class="timeline-text mt-n2">
                      <p style="margin-top: 0;">"<strong>Agente de Mercadeo:</strong> {{
                        gestion.usuario_mercadeo }}"</p>
                      <p style="margin-top: 0;" class="mb-4">"<strong>Gestión:</strong> {{
                        gestion.respuesta }}"</p>
                    </div>
                  </div>
                  <!-- Línea vertical entre items -->
                  <div v-if="idx < historialGestion.length - 1" class="timeline-connector">
                  </div>
                </div>
              </div>

              <p class="text-h6 font-weight-bold ml-10 mb-4">Historial de Actividades</p>

              <v-row v-for="(item, index) in eventosFiltrados" :key="index" class="mb-2 align-start" no-gutters>
                <!-- Avatar -->
                <v-col cols="auto" class="pr-2 d-flex justify-center">
                  <v-avatar size="30" :color="item.color">
                    <v-icon dark size="20">
                      {{estados2.find(e => e.id === item.idEstado)?.icon || 'mdi-help-circle'}}
                    </v-icon>
                  </v-avatar>
                </v-col>

                <!-- Tarjeta del evento -->
                <v-col>
                  <v-card class="pa-2" variant="outlined" style="border-radius: 10px; font-size: 2vh; " :style="{
                    backgroundColor: item.estado == 4 ? '#E8F5E9' :
                      item.estado == 5 ? '#FFEBEE' : 'white'
                  }">
                    <div class="d-flex justify-space-between align-center">
                      <strong>
                        <span class="" style="color: #311B92;">
                          {{estados2.find(e => e.id === item.idEstado)?.nombre || 'Sistema'}}
                        </span>
                      </strong>
                      <span class="" style="font-size: 1.5vh; ">{{ item.fecha }}</span>

                    </div>

                    <!-- Descripción -->
                    <div class=" mt-1" style="font-size: 1.9vh;">
                      <div class="d-flex justify-space-between align-center">
                        <span>{{ item.descripcion }}</span>
                        <div class="d-flex align-center" style="gap: 8px;">
                          <v-tooltip location="top" :text="item.rutacot ? getFileName(item.rutacot) : 'Sin archivo'">
                            <template v-slot:activator="{ props }">
                              <v-btn :href="item.rutacot" target="_blank" color="primary" size="small"
                                class="mr-2 btn-grow" v-bind="props" v-if="item.rutacot && item.rutacot !== 'null'">
                                <v-icon left>mdi-file-download</v-icon>
                                Ver Cotización
                              </v-btn>
                            </template>
                          </v-tooltip>
                          <v-tooltip location="top" :text="item.rutarut ? getFileName(item.rutarut) : 'Sin archivo'">
                            <template v-slot:activator="{ props }">
                              <v-btn :href="item.rutarut" target="_blank" color="secondary" size="small" v-bind="props"
                                v-if="item.rutarut && item.rutarut !== 'null'">
                                <v-icon left>mdi-file-download</v-icon>
                                Ver Rut
                              </v-btn>
                            </template>
                          </v-tooltip>
                        </div>
                      </div>
                    </div>

                    <!-- Detalles producto -->
                    <div v-if="item.idEstado == 6" class="text-caption mt-1" style="font-size: 1.8vh;">
                      <strong><span style="font-size: 1.8vh; color: #311B92;">Producto:</span><span
                          style="font-size: 1.8vh"> {{ item.idservicio }}</span> </strong>
                    </div>
                    <div v-if="item.idEstado == 6 && item.valor_proyecto" class="text-caption mt-1">
                      <strong><span style="font-size: 1.8vh; color: #311B92;">Valor Producto:</span><span
                          style="font-size: 1.8vh">{{ item.valor_proyecto }} </span> </strong>
                    </div>

                    <!-- Icono finalización -->
                    <div v-if="(item.estado == 4 || item.estado == 5) && item.idEstado == 6"
                      class="mt-1 d-flex justify-end">
                      <v-icon v-if="item.estado == 4 || item.estado == 5" size="20"
                        :color="item.estado == 4 ? 'green' : 'red'">
                        {{ item.estado == 4 ? 'mdi-medal-outline' : 'mdi-emoticon-sad-outline' }}
                      </v-icon>
                    </div>
                  </v-card>
                </v-col>
              </v-row>
            </div>
            <v-card-actions class="justify-end">

              <v-btn color="primary" class="btn-grow justify-end" @click="dialogHistorico = false">
                Cerrar
              </v-btn>
            </v-card-actions>

          </v-card>

        </v-card>
      </v-dialog>


      <v-dialog v-model="alerta" persistent>
        <v-card :style="getAlertStyle()">
          <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
            class="mx-auto"></v-progress-circular>
          <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-tittle>
          <v-btn class="mt-4 mx-auto" @click="cerrarDIV()" :readonly="ifCargando"
            style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
        </v-card>
      </v-dialog>

      <!-- DIALOGO VALIDACIÓN-->
      <v-dialog v-model="dialogValidarCotizacion" max-width="900px">
        <v-card>
          <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
            <v-icon class="mr-2">mdi-alert-circle-outline</v-icon>
            Información incompleta para cotizar
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <v-alert type="error" border="start" color="#1976D2" class="mb-3">
              {{ mensajeValidacionCotizacion }}
            </v-alert>
            <v-divider class="mb-3"></v-divider>
            <v-row>
              <v-col cols="12" md="6">
                <v-card class="mb-2" outlined>
                  <v-card-title class="text-subtitle-1 font-weight-bold" style="color:#006CA1;">Datos de la
                    Empresa
                    <v-icon left class="btn-grow" size="18" @click="actualizarInfoProspecto()">mdi-refresh</v-icon>
                  </v-card-title>
                  <v-card-text>
                    <div class="mb-1"><strong>NIT:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'NIT')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'NIT')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Razón Social:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'Razón Social')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'Razón Social')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Tipo Identificación:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'Tipo Identificación')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'Tipo Identificación')?.valor || 'N/A'}}</span>
                    </div>
                    <div class="mb-1"><strong>Sector:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'Sector')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'Sector')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Dirección:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'Dirección')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'Dirección')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Departamento:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'Departamento')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'Departamento')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Ciudad:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'Ciudad')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'Ciudad')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Correo Empresa:</strong> <span
                        :style="{ color: infoProspectoDialog.find(c => c.nombre === 'Correo Empresa')?.faltante ? 'red' : '#222' }">{{
                          infoProspectoDialog.find(c => c.nombre === 'Correo Empresa')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1">
                      <strong>Teléfono:</strong>
                      <span :style="{
                        color: (infoProspectoDialog.find(c => c.nombre === 'Teléfono 1')?.faltante &&
                          infoProspectoDialog.find(c => c.nombre === 'Teléfono 2')?.faltante) ? 'red' : '#222'
                      }">
                        {{
                          infoProspectoDialog.find(c => c.nombre === 'Teléfono 1')?.valor || infoProspectoDialog.find(c =>
                            c.nombre === 'Teléfono 2')?.valor || 'N/A'}}
                      </span>
                    </div>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-card class="mb-2" outlined>
                  <v-card-title class="text-subtitle-1 font-weight-bold" style="color:#006CA1;">Datos del
                    Contacto
                    <v-icon left class="btn-grow" size="18" @click="actualizarInfoProspecto()">mdi-refresh</v-icon>
                  </v-card-title>
                  <v-card-text>
                    <div class="mb-1"><strong>Nombre:</strong> <span
                        :style="{ color: infoContactoDialog.find(c => c.nombre === 'Nombre')?.faltante ? 'red' : '#222' }">{{
                          infoContactoDialog.find(c => c.nombre === 'Nombre')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Apellido:</strong> <span
                        :style="{ color: infoContactoDialog.find(c => c.nombre === 'Apellido')?.faltante ? 'red' : '#222' }">{{
                          infoContactoDialog.find(c => c.nombre === 'Apellido')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Correo:</strong> <span
                        :style="{ color: infoContactoDialog.find(c => c.nombre === 'Correo')?.faltante ? 'red' : '#222' }">{{
                          infoContactoDialog.find(c => c.nombre === 'Correo')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Celular:</strong> <span
                        :style="{ color: infoContactoDialog.find(c => c.nombre === 'Celular')?.faltante ? 'red' : '#222' }">{{
                          infoContactoDialog.find(c => c.nombre === 'Celular')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Categoría:</strong> <span
                        :style="{ color: infoContactoDialog.find(c => c.nombre === 'Categoría')?.faltante ? 'red' : '#222' }">{{
                          infoContactoDialog.find(c => c.nombre === 'Categoría')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Cargo:</strong> <span
                        :style="{ color: infoContactoDialog.find(c => c.nombre === 'Cargo')?.faltante ? 'red' : '#222' }">{{
                          infoContactoDialog.find(c => c.nombre === 'Cargo')?.valor || 'N/A'}}</span></div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn color="primary" @click="editProspecto()">Ir a Editar Prospecto</v-btn>
            <v-btn color="primary" @click="dialogValidarCotizacion = false">Cerrar</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!-- FINAL DIALOGO VALIDACIÓN-->

      <!-- DIALOGO DE VER INFO CONTACTO-->
      <v-dialog v-model="dialogValidarInfoContacto" max-width="900px">
        <v-card>
          <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
            <v-icon class="mr-2">mdi mdi-account-box</v-icon>
            Información De Contacto
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <v-divider class="mb-3"></v-divider>
            <v-row>
              <v-col cols="12" md="6">
                <v-card class="mb-2" outlined>
                  <v-card-text>
                    <div class="mb-1"><strong>NIT:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'NIT')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'NIT')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Razón Social:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'Razón Social')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'Razón Social')?.valor || 'N/A'}}</span>
                    </div>
                    <div class="mb-1"><strong>Tipo Identificación:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'Tipo Identificación')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'Tipo Identificación')?.valor || 'N/A'
                        }}</span>
                    </div>
                    <div class="mb-1"><strong>Sector:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'Sector')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'Sector')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Dirección:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'Dirección')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'Dirección')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Departamento:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'Departamento')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'Departamento')?.valor || 'N/A'}}</span>
                    </div>
                    <div class="mb-1"><strong>Ciudad:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'Ciudad')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'Ciudad')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Correo Empresa:</strong> <span
                        :style="{ color: (infoProspectoDialog || []).find(c => c.nombre === 'Correo Empresa')?.faltante ? 'red' : '#222' }">{{
                          (infoProspectoDialog || []).find(c => c.nombre === 'Correo Empresa')?.valor || 'N/A'}}</span>
                    </div>
                    <div class="mb-1">
                      <strong>Teléfono:</strong>
                      <span
                        :style="{ color: ((infoProspectoDialog || []).find(c => c.nombre === 'Teléfono 1')?.faltante && (infoProspectoDialog || []).find(c => c.nombre === 'Teléfono 2')?.faltante) ? 'red' : '#222' }">
                        {{(infoProspectoDialog || []).find(c => c.nombre === 'Teléfono 1')?.valor ||
                          (infoProspectoDialog
                            || []).find(c => c.nombre === 'Teléfono 2')?.valor || 'N/A'}}
                      </span>
                    </div>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-card class="mb-2" outlined>
                  <v-card-title class="text-subtitle-1 font-weight-bold" style="color:#006CA1;">Datos del
                    Contacto</v-card-title>
                  <v-card-text>
                    <div class="mb-1"><strong>Nombre:</strong> <span
                        :style="{ color: (infoContactoDialog || []).find(c => c.nombre === 'Nombre')?.faltante ? 'red' : '#222' }">{{
                          (infoContactoDialog || []).find(c => c.nombre === 'Nombre')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Apellido:</strong> <span
                        :style="{ color: (infoContactoDialog || []).find(c => c.nombre === 'Apellido')?.faltante ? 'red' : '#222' }">{{
                          (infoContactoDialog || []).find(c => c.nombre === 'Apellido')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Correo:</strong> <span
                        :style="{ color: (infoContactoDialog || []).find(c => c.nombre === 'Correo')?.faltante ? 'red' : '#222' }">{{
                          (infoContactoDialog || []).find(c => c.nombre === 'Correo')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Celular:</strong> <span
                        :style="{ color: (infoContactoDialog || []).find(c => c.nombre === 'Celular')?.faltante ? 'red' : '#222' }">{{
                          (infoContactoDialog || []).find(c => c.nombre === 'Celular')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Categoría:</strong> <span
                        :style="{ color: (infoContactoDialog || []).find(c => c.nombre === 'Categoría')?.faltante ? 'red' : '#222' }">{{
                          (infoContactoDialog || []).find(c => c.nombre === 'Categoría')?.valor || 'N/A'}}</span></div>
                    <div class="mb-1"><strong>Cargo:</strong> <span
                        :style="{ color: (infoContactoDialog || []).find(c => c.nombre === 'Cargo')?.faltante ? 'red' : '#222' }">{{
                          (infoContactoDialog || []).find(c => c.nombre === 'Cargo')?.valor || 'N/A'}}</span></div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn color="primary" @click="dialogValidarInfoContacto = false">Cerrar</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!-- FINAL DIALOGO VER INFO CONTACTO-->

      <!----- Dialogo para listar los prospectos ----->
      <v-dialog v-model="dialogProspectos" persistent width="75%">
        <v-card style="border-radius: 20px; height: 100%;">
          <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006CA1;">
            <v-icon>
              mdi-office-building-cog
            </v-icon>
            Listar prospectos
          </v-card-title>
          <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006CA1;">
            <div class="mx-2">
              Prospectos ({{ listaEmpresasComercial.length }})
            </div>
          </v-card-subtitle>

          <v-row class="mx-2 mt-2 mb-n6">
            <v-col cols="3">
              <v-autocomplete v-model="filtroRazonSocialEmpresasComercial" :items="listaEmpresasComercial" return-object
                item-title="p_razon_social" item-value="id" label="Razón Social" variant="outlined" clearable
                autocomplete="off" density="compact" @update:model-value="filtrarEmpresas()"
                :readonly="filtroNitEmpresasComercial || filtroFechaDesdeEmpresasComercial" />
            </v-col>

            <v-col cols="3">
              <v-autocomplete v-model="filtroNitEmpresasComercial" :items="listaEmpresasComercial" return-object
                :item-title="item => `${item.p_nit}` ? `${item.p_nit}` : 'No disponible'" item-value="id" label="NIT"
                variant="outlined" clearable autocomplete="off" density="compact"
                @update:model-value="filtrarEmpresas()"
                :readonly="filtroRazonSocialEmpresasComercial || filtroFechaDesdeEmpresasComercial" />
            </v-col>

            <v-col cols="3">
              <v-text-field v-model="filtroFechaDesdeEmpresasComercial" label="Fecha de Creación Desde" type="date"
                variant="outlined" clearable autocomplete="off" density="compact"
                @update:model-value="filtrarEmpresas2()"
                :readonly="filtroRazonSocialEmpresasComercial || filtroNitEmpresasComercial" />
            </v-col>

            <v-col cols="3">
              <v-text-field v-model="filtroFechaHastaEmpresasComercial" label="Fecha de Creación Hasta" type="date"
                variant="outlined" clearable autocomplete="off" density="compact"
                @update:model-value="filtrarEmpresas2()"
                :readonly="filtroRazonSocialEmpresasComercial || filtroNitEmpresasComercial"
                v-if="filtroFechaDesdeEmpresasComercial" />
            </v-col>
          </v-row>

          <v-card-text style="overflow-y: auto; height: 100%;">

            <v-row v-for="(fila, filaIndex) in filasEmpresas" :key="filaIndex" class="mb-2" cols="12" md="3" lg="3">
              <v-col v-for="empresa in fila" :key="empresa.id" cols="12" md="6" lg="4">
                <v-card @click="cargarProspecto(empresa); estaEditando = true" class="empresa-card pa-4 mb-2"
                  elevation="3">
                  <v-row align="center" no-gutters>
                    <v-col cols="auto">
                      <v-avatar color="#1976D2" size="44">
                        <v-icon color="white" size="32">mdi-office-building</v-icon>
                      </v-avatar>
                    </v-col>
                    <v-col>
                      <div class="empresa-title font-weight-bold ml-2"
                        style="font-size: 1.15rem; color: #0A1C3A; white-space: normal; word-break: break-word;">
                        {{ empresa.p_razon_social }}
                      </div>
                      <div class="empresa-nit ml-2 text-caption"
                        style="color: #1976D2; font-weight: 500; margin-top: 2px;">
                        <span style="margin-right: 4px;">NIT:</span>
                        <span>{{ empresa.p_nit }}</span>
                      </div>
                    </v-col>
                  </v-row>
                  <v-divider class="my-2"></v-divider>
                  <v-row>
                    <v-col cols="6">
                      <div class="empresa-label text-caption" style="color: #666;">Teléfono empresa</div>
                      <div class="empresa-value font-weight-medium d-flex align-center" style="color: #222;">
                        <v-icon size="18" color="#1976D2" class="mr-1">mdi-phone</v-icon>
                        <span class="contact-card-text">{{ empresa.p_telefono1 || 'No disponible' }}</span>
                      </div>
                      <div class="empresa-label text-caption mt-1" style="color: #666;">Celular contacto</div>
                      <div class="empresa-value font-weight-medium d-flex align-center" style="color: #222;">
                        <v-icon size="18" color="#1976D2" class="mr-1">mdi-cellphone</v-icon>
                        <span class="contact-card-text">{{ empresa.pc_celular || 'No disponible' }}</span>
                      </div>
                    </v-col>
                    <v-col cols="6">
                      <div class="empresa-label text-caption" style="color: #666;">Contacto</div>
                      <div class="empresa-value font-weight-medium d-flex align-center" style="color: #222;">
                        <v-icon size="18" color="#1976D2" class="mr-1">mdi-account-tie</v-icon>
                        <span style="white-space: normal; word-break: break-word;">{{ empresa.pc_nombre }} {{
                          empresa.pc_apellido }}</span>
                      </div>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>


          <v-card-actions>
            <v-btn
              @click="dialogProspectos = false; filtroRazonSocialEmpresasComercial = null; filtroNitEmpresasComercial = null; filtroFechaDesdeEmpresasComercial = null; filtroFechaHastaEmpresasComercial = null;"
              color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!----- Dialogo para listar los prospectos ----->

      <!----- Dialogo para crear/editar los prospectos ----->
      <v-dialog v-model="dialogCrearEditarProspecto" persistent width="70%">
        <v-card style="height: 100%; border-radius: 20px;">
          <v-card-title class="text-h6" style="color: white; font-weight: bold; background-color: #006CA1;">
            <div v-if="idProspectoSeleccionado">
              Editar Prospecto
              <v-icon style="float: right;" @click="actualizarProspecto()" icon="mdi-content-save" size="small"
                :disabled="dsGuardar"></v-icon>
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
                    <input class="campo-input mx-5 mb-5" type="number" list="empresas" id="empresa"
                      v-model="nitComercial" placeholder="NIT" autocomplete="off" />
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
                  <option v-for="(empresa, index) in listaEmpresas2Comercial" :key="empresa.id"
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
                <v-select class="mx-5" v-model="sectorComercial" :items="sectorEmpresa" return-object
                  item-title="nombre" item-value="id" label="Sector" variant="outlined" clearable autocomplete="off">
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
                      item-title="nombre" item-value="id" label="Ciudad" variant="outlined" clearable
                      autocomplete="off">
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
                    <v-text-field class="ml-5" @input="filterTel1Comercial" :rules="[maxlength2].flat()"
                      v-model="tel1Comercial" label="Telefono 1" type="number" variant="outlined" clearable
                      autocomplete="off">
                      <template v-slot:prepend-inner>
                        <v-icon color="#006CA1" style="opacity: 100%;">mdi-cellphone</v-icon>
                      </template>
                    </v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field class="mr-5" v-model="tel2Comercial" label="Telefono 2" type="number"
                      variant="outlined" clearable autocomplete="off">
                      <template v-slot:prepend-inner>
                        <v-icon color="#006CA1" style="opacity: 100%;">mdi-phone</v-icon>
                      </template>
                    </v-text-field>
                  </v-col>
                </v-row>
              </v-col>
              <v-col style="border-left: 1px solid #ccc; padding-left: 20px;">
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
                <v-text-field class="mx-5" v-model="correoContactoComercial" label="Correo" type="text"
                  variant="outlined" clearable autocomplete="off">
                  <template v-slot:prepend-inner>
                    <v-icon color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                  </template>
                </v-text-field>

                <v-row>
                  <v-col cols="3" class="m-0">

                    <v-text-field class="ml-5 mr-n4" v-model="extensionComercial" label="Extensión" type="number"
                      variant="outlined" autocomplete="off">
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
      <!----- Dialogo para crear/editar los prospectos ----->

      <!-- Dialog historial de ediciones -->
      <v-dialog v-model="dialogHistorialEdiciones" max-width="200vh" height="100vh" persistent>
        <v-card class="pa-4" style="height: 100%;">
          <v-card variant="outlined" elevation="5" class="pa-4 rounded-xl d-flex flex-column" style="height: 100%;">
            <!-- Encabezado -->
            <div style="position: sticky; top: 0; z-index: 2; margin-bottom: 2vh;" class="rounded-xs">
              <v-alert color="#027cb8" class="mb-4 pa-4 rounded-xs ">
                <v-row align="center" justify="space-between" class="ma-0 pa-0">
                  <v-col cols="12" md="4" class="d-flex align-center">
                    <v-icon size="26" color="white">mdi-history</v-icon>
                    <h2 class="ml-2 mb-0">Historial de Ediciones de Observaciones</h2>
                  </v-col>
                  <v-col cols="12" md="8" class="d-flex justify-end align-center" style="gap: 20px;">
                    <v-text-field v-model="buscadorHistorialGeneral" placeholder="Buscar en historial…"
                      density="compact" variant="solo" bg-color="rgba(255,255,255, 0.9)"
                      base-color="rgba(255,255,255, 0.9)" color="white" prepend-inner-icon="mdi-magnify" clearable
                      rounded="lg" hide-details style="max-width: 320px;" />
                    <v-text-field v-model="busquedaFechaHistorialInicio" type="date" density="compact" variant="solo"
                      :bg-color="busquedaFechaHistorialFin && !busquedaFechaHistorialInicio ? '#fffbe6' : 'rgba(255,255,255, 0.9)'"
                      prepend-inner-icon="mdi-calendar" clearable rounded="lg" hide-details style="max-width: 200px;"
                      label="Desde" :max="busquedaFechaHistorialFin || undefined"
                      :error="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialInicio > busquedaFechaHistorialFin"
                      :hint="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialInicio > busquedaFechaHistorialFin ? 'La fecha desde no puede ser mayor que la fecha hasta' : (busquedaFechaHistorialFin && !busquedaFechaHistorialInicio ? 'Selecciona fecha desde' : '')"
                      persistent-hint />
                    <v-text-field v-model="busquedaFechaHistorialFin" type="date" density="compact" variant="solo"
                      :bg-color="busquedaFechaHistorialInicio && !busquedaFechaHistorialFin ? '#fffbe6' : 'rgba(255,255,255, 0.9)'"
                      prepend-inner-icon="mdi-calendar" clearable rounded="lg" hide-details style="max-width: 200px;"
                      label="Hasta" :min="busquedaFechaHistorialInicio || undefined"
                      :error="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialFin < busquedaFechaHistorialInicio"
                      :hint="busquedaFechaHistorialInicio && busquedaFechaHistorialFin && busquedaFechaHistorialFin < busquedaFechaHistorialInicio ? 'La fecha hasta no puede ser menor que la fecha desde' : (busquedaFechaHistorialInicio && !busquedaFechaHistorialFin ? 'Selecciona fecha hasta' : '')"
                      persistent-hint />
                    <v-tooltip text="Cerrar Historial" location="top">
                      <template #activator="{ props }">
                        <v-btn icon size="small" class="btn-grow" v-bind="props"
                          @click="dialogHistorialEdiciones = false; buscadorHistorialGeneral = null; busquedaFechaHistorialInicio = null; busquedaFechaHistorialFin = null;">
                          <v-icon color="black">mdi-window-close</v-icon>
                        </v-btn>
                      </template>
                    </v-tooltip>
                  </v-col>
                </v-row>
              </v-alert>
            </div>
            <!-- Cuerpo scroll -->
            <div style="overflow-y: auto; flex: 1; max-height: 60vh;" class="mt-2 mb-2 ml-2 custom-scroll">
              <v-row v-for="(item, index) in filteredHistorialEdiciones" :key="index" class="mb-2 align-start"
                no-gutters>
                <!-- Avatar usuario -->
                <v-col cols="auto" class="pr-2 d-flex justify-center">
                  <v-avatar size="36" color="#1976d2">
                    <v-icon color="white" size="22">mdi-account-edit</v-icon>
                  </v-avatar>
                </v-col>
                <!-- Tarjeta de edición -->
                <v-col>
                  <v-card class="pa-3" variant="outlined" style="border-radius: 10px; font-size: 2vh;">
                    <div class="d-flex justify-space-between align-center mb-1">
                      <div class="d-flex align-center">
                        <v-icon size="18" color="#1976d2" class="mr-1">mdi-account</v-icon>
                        <span style="font-weight: 600; color: #1976d2;">{{ item.nombre_usu }}</span>
                      </div>
                      <div class="d-flex align-center">
                        <v-icon size="16" color="#027cb8" class="mr-1">mdi-calendar-clock</v-icon>
                        <span style="font-size: 1.5vh;">Edición: {{ formatDate2(item.fecha_edicion)
                        }}</span>
                      </div>
                    </div>
                    <div class="d-flex align-center mb-2">
                      <v-icon size="16" color="#757575" class="mr-1">mdi-calendar-edit</v-icon>
                      <span class="text-caption">Original: {{
                        formatDate2(item.fecha_original_historial)
                      }}</span>
                    </div>
                    <v-divider class="my-2" />
                    <div class="mb-2">
                      <v-icon size="18" color="#43a047" class="mr-1">mdi-pencil</v-icon>
                      <span style="font-weight: 500; color: #43a047;">Observación editada:</span>
                      <span class="ml-2">{{ item.texto_editado }}</span>
                    </div>
                    <div class="mb-2">
                      <v-icon size="18" color="#fbc02d" class="mr-1">mdi-history</v-icon>
                      <span style="font-weight: 500; color: #fbc02d;">Observación original:</span>
                      <span class="ml-2">{{ item.texto_original }}</span>
                    </div>
                  </v-card>
                </v-col>
              </v-row>
            </div>
          </v-card>
        </v-card>
      </v-dialog>
      <!-- Dialog historial de ediciones -->
    </v-main>
  </v-app>
</template>

<script>

import AppHeader from '../components/AppHeader.vue';
import axios from 'axios'
import CryptoJS from "crypto-js";

export default {
  components: {
    AppHeader
  },

  data() {

    return {
      opcionesActividadSelected: null,
      // Opciones para seguimiento a realizar
      opcionesSeguimientoSelected: null,
      selectedActividad: null,
      selectedSeguimiento: null,


      estados: [
        {
          id: 1,
          nombre: 'Llamada Realizada',
          color: 'bg-indigo-darken-3',
          items: []
        },
        {
          id: 2,
          nombre: 'Correo Enviado',
          color: 'bg-light-blue-darken-3',
          items: []
        },
        {
          id: 3,
          nombre: 'Visita Presencial',
          color: 'bg-orange-darken-3',
          items: []
        },
        {
          id: 4,
          nombre: 'Visita Virtual',
          color: 'bg-teal-darken-4',
          items: []
        },
        {
          id: 5,
          nombre: 'Activación de Demo',
          color: 'bg-purple-darken-1',
          items: []
        },
        {
          id: 6,
          nombre: 'Cotización',
          color: 'bg-brown-darken-3',
          items: []
        }
      ],


      estados2: [
        {
          id: 1,
          nombre: 'Llamada Realizada',
          color: '#1565C0',
          icon: 'mdi-phone',
          items: []
        },
        {
          id: 2,
          nombre: 'Correo Enviado',
          color: '#2095c9',
          icon: 'mdi-gmail',
          items: []
        },
        {
          id: 3,
          nombre: 'Visita Presencial',
          color: 'orange-darken-2',
          icon: 'mdi-calendar-cursor-outline',
          items: []
        },
        {
          id: 4,
          nombre: 'Visita Virtual',
          color: 'teal-darken-1',
          icon: 'mdi-monitor-account',
          items: []
        },
        {
          id: 5,
          nombre: 'Activación de Demo',
          color: '#8E24AA',
          icon: 'mdi-laptop',
          items: []
        },
        {
          id: 6,
          nombre: 'Cotización',
          color: 'brown-darken-3',
          icon: 'mdi-point-of-sale',
          items: []
        }
      ],

      idCargo: null,

      ordenLista: true,
      opcionesActividadSelected: null,
      mostrarInputCot: false,
      mostrarInputRUT: false,
      observacionGeneral: null,
      tmColorNuevo: 'bg-blue-darken-3',
      tmColorEnProceso: 'bg-light-blue-darken-3',
      tmColorCotizado: 'bg-orange-darken-3',
      tmColorCerradoE: 'bg-green-darken-3',
      tmColorCerradoD: 'bg-#1A237E',
      tmColorCotizacion: 'bg-grey-darken-3',

      baseURL: '',
      dialogNuevaActividad: false,
      selectedClienteActividad: null,
      selectClientesActividad: [],
      roClienteActividad: true,
      cbLlamadaRealizada: false,
      cbVisitaPresencial: false,
      cbActivacionDemo: false,
      cbCorreoEnviado: false,
      cbVisitaVirtual: false,
      ifServicioActividad: false,
      ifServicio: true,
      selectedServicioActividad: null,
      selectServiciosActividad: [],
      ifValorProyecto: false,
      selectedValorProyecto: null,
      archivoRUT: null,
      archivosActividad: null,
      ifDocumentos: false,
      ifObservaciones: false,
      selectedObservacionesActividad: '',
      selectedObservacionesSeguimiento: '',
      selectedEstadoActividad: null,
      selectEstadosActividad: [],
      roEstadoActividad: false,
      roValorProyecto: true,
      ifComentariosAdicionales: false,
      selectedComentariosActividad: '',
      proximoSeguimientoActividad: null,
      ifProximoSeguimientoActividad: false,
      ifSeguimientosCotizados: false,
      cbLlamar: false,
      cbVisitarPresencial: false,
      cbActivarDemo: false,
      cbEnviarCorreo: false,
      cbVisitarVirtual: false,
      cbCotizar: false,
      dialogHistorico: false,
      itemSeleccionado: null,

      idproccom: null,
      nombreComercial: null,
      drawer: false,
      menuAbierto: false,

      idtipac: null,
      razon_social: null,
      idprospecto: null,
      ultact: null,
      ultactfec: null,
      ultseg: null,
      ultsegfec: null,
      ultsegAct: null,
      ultsegObser: null,

      alerta: false,
      mensajeAlertLogin: '',

      rutaCot: null,
      rutaRut: null,

      ifActividad: true,
      ifActCotizado: false,
      idSeguimiento: null,
      ifCargando: false,

      dialogCambioClave: false,
      claveActual: null,
      nuevaClave: null,
      confirmarClave: null,
      mostrarClaveActual: false,
      mostrarNuevaClave: false,
      mostrarConfirmarClave: false,
      subirArchivoRUT: false,
      subirArchivoDOC: false,
      idActividad: null,
      estadoSeguimientos: null,
      ifHistorico: false,
      ifBtnRegistrarActividad: true,
      dsServicio: true,
      estadoactual: null,
      nombreClienteInfo: '',
      telefonoClienteInfo: '',
      contactoClienteInfo: '',
      celularClienteInfo: '',
      direccionClienteInfo: '',
      departamentoClienteInfo: '',
      ciudadClienteInfo: '',
      readonlyServicioSeleccionado: false,
      proximoSeguimientoErrorMsg: '',
      validandoActividad: false,
      ifBotonActividadCargando: true,
      ultSeguimiento: null,
      selectedFechaUltimaActividad: '',
      dialogObsCompleta: false,
      ifCerradoDeclinado: false,
      ifCerradoExitoso: false,
      fechaActual: new Date().toISOString().split('T')[0],
      bloqueaSincronizacion: false,
      busquedaHistorial: '',
      busquedaFecha: '',
      dialogObsCompleta: false,
      selectedItem: null,

      dialogValidarCotizacion: false,
      dialogValidarInfoContacto: false,
      infoContactoValida: false,
      mensajeValidacionCotizacion: '',

      mostrarInputsDocs: false,

      sectores: [],
      tiposEmpresa: [],
      tiposIdentificacion: [],
      categorias: [],
      departamentos: [],
      ciudades: [],
      cargos: [],
      tipoEmpresa: [],

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
      tel1Comercial: '57',
      tel2Comercial: null,
      nombreComercial2: null,
      apellidoComercial: null,
      categoriaComercial: null,
      cargoComercial: null,
      correoContactoComercial: null,
      celularComercial: '573',
      extensionComercial: '57',
      idProspectoSeleccionado: null,
      listaEmpresasComercial: [],
      listaEmpresasComercial2: [],
      listaEmpresasFiltradas: [],
      tipoEmpComercial: null,

      dialogProspectos: false,
      dialogCrearEditarProspecto: false,
      filtroRazonSocialEmpresasComercial: null,
      filtroNitEmpresasComercial: null,
      filtroFechaDesdeEmpresasComercial: null,
      filtroFechaHastaEmpresasComercial: null,
      mensajeAlertaCelular: null,
      alertaCelular: false,
      filtrosActivos: true,
      listaEmpresas: [],
      listaEmpresas2: [],
      dsGuardar: false,
      empresas: [],
      mensajeAlertaRazonSocial: '',
      alertaNit: false,
      mensajeAlertaNit: '',
      alertaRazonSocial: false,
      prospecto: null,
      prospectos: [],
      alertaProspecto: false,

      maxlength2: [v => !v || String(v).length < 13 || "Error. Máximo 10 dígitos"],
      filtroEstadoId: null,
      historialActividades: [],

      historialGestion: [],
      historialEdiciones: [],
      dialogHistorialEdiciones: false,
      buscadorHistorialGeneral: null,
      busquedaFechaHistorialInicio: null,
      busquedaFechaHistorialFin: null,

    };
  },

  mounted() {
    this.baseURL = import.meta.env.VITE_API_BASE_URL;
    this.idCargo = localStorage.getItem('idCargo');
    this.razon_social = localStorage.getItem('razon_soc');
    this.estadoactual = localStorage.getItem('idestado');
    //this.cargarDatos();
    this.cargarClientesActividad();
    this.cargarServiciosActividad();
    this.cargarEstadosActividad();

    this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');
    this.idproccom = localStorage.getItem('idproccom');
    this.idempresa = localStorage.getItem('idempresa');
    this.comercialId = localStorage.getItem('idUsuario');
    this.nombreClienteInfo = localStorage.getItem('razon_soc');
    this.telefonoClienteInfo = localStorage.getItem('telefonoCliente');
    this.contactoClienteInfo = localStorage.getItem('contactoCliente');
    this.celularClienteInfo = localStorage.getItem('celularCliente');
    this.direccionClienteInfo = localStorage.getItem('direccionCliente');
    this.departamentoClienteInfo = localStorage.getItem('departamentoCliente');
    this.ciudadClienteInfo = localStorage.getItem('ciudadCliente');

    setTimeout(() => {
      this.cargarActividades();
      this.cargarListaDeActividades();
      this.cargarListaSeguimientos(0);
    }, 1000);
    this.cargarSectores();
    this.cargarTiposEmpresa();
    this.cargarTiposIdentificacion();
    this.cargarCategorias();
    this.cargarDepartamentos();
    this.cargarCiudades();
    this.cargarCargos();

  },

  computed: {

    filteredHistorialEdiciones() {
      // Filtros de texto y fechas para historial de ediciones
      let result = this.historialEdiciones;

      // Filtro por texto (usuario, observaciones editadas u originales)
      if (this.buscadorHistorialGeneral && this.buscadorHistorialGeneral.trim() !== '') {
        const search = this.buscadorHistorialGeneral.trim().toLowerCase();
        result = result.filter(item => {
          const nombreUsu = (item.nombre_usu || '').toLowerCase();
          const textoEditado = (item.texto_editado || '').toLowerCase();
          const textoOriginal = (item.texto_original || '').toLowerCase();
          return nombreUsu.includes(search) || textoEditado.includes(search) || textoOriginal.includes(search);
        });
      }

      // Filtro solo por fecha de edición
      if (this.busquedaFechaHistorialInicio || this.busquedaFechaHistorialFin) {
        // Ajustar fechas para comparar solo por día y que el rango sea inclusivo
        const start = this.busquedaFechaHistorialInicio
          ? new Date(this.busquedaFechaHistorialInicio + 'T00:00:00')
          : null;
        const end = this.busquedaFechaHistorialFin
          ? new Date(this.busquedaFechaHistorialFin + 'T23:59:59.999')
          : null;
        result = result.filter(item => {
          const fechaEdicion = item.fecha_edicion ? new Date(item.fecha_edicion) : null;
          if (!fechaEdicion) return false;
          if (start && end) {
            return fechaEdicion >= start && fechaEdicion <= end;
          } else if (start) {
            return fechaEdicion >= start;
          } else if (end) {
            return fechaEdicion <= end;
          }
          return true;
        });
      }
      return result;
    },

    itemsCombinadosOrdenados() {
      // Unir todos los items de todos los estados
      let todos = this.estados2.flatMap(estado =>
        estado.items.map(item => ({
          ...item,
          estadoNombre: estado.nombre,
          color: estado.color,
          idEstado: estado.id,
        }))
      );

      // Si hay filtro, aplicarlo
      if (this.filtroEstadoId) {
        todos = todos.filter(item => item.idEstado === this.filtroEstadoId);
      }

      // Invertir el orden si es necesario
      return this.ordenLista ? todos : todos.slice().reverse();
    },

    readonlyServicioSeleccionado() {
      // Si no hay servicio seleccionado, lo dejas editable
      if (!this.selectedServicioActividad) return false;
      // Solo editable si es 9 o "Presentación Corporativa"
      return !(localStorage.getItem('servicio') === 9 || localStorage.getItem('servicio') === 'Presentación Corporativa');
    },

    textoObservacionCorto() {
      const texto = this.ultsegObser || 'Sin observaciones registradas.';
      const palabras = texto.trim().split(/\s+/);
      if (palabras.length > 14) {
        return palabras.slice(0, 14).join(' ') + '...';
      }
      return texto;
    },
    eventosFiltrados() {
      let eventos = this.historialActividades.slice();

      // Filtro por estado
      if (this.filtroEstadoId) {
        eventos = eventos.filter(item => item.idEstado === this.filtroEstadoId);
      }

      // Filtro por texto
      if (this.busquedaHistorial) {
        eventos = eventos.filter(item =>
          item.descripcion?.toLowerCase().includes(this.busquedaHistorial.toLowerCase())
        );
      }

      // Filtro por fecha
      if (this.busquedaFecha) {
        eventos = eventos.filter(item =>
          item.fecha.startsWith(this.busquedaFecha)
        );
      }

      // Ordenar por fecha descendente (más reciente primero)
      eventos.sort((a, b) => new Date(b.fecha) - new Date(a.fecha));

      return this.ordenLista ? eventos : eventos.slice().reverse();
    },

    eventosAgrupadosPorFecha() {
      const agrupados = {};
      for (const item of this.eventosFiltrados) {
        const fecha = item.fecha.split(' ')[0];
        if (!agrupados[fecha]) agrupados[fecha] = [];
        agrupados[fecha].push(item);
      }
      return agrupados;
    },

    filasEmpresas() {
      const columnas = 3;
      const filas = [];
      for (let i = 0; i < this.listaEmpresasComercial.length; i += columnas) {
        filas.push(this.listaEmpresasComercial.slice(i, i + columnas));
      }
      return filas;
    },
  },

  watch: {

    tipoIdComercial(newVal) {
      if (!newVal) return;

      if (newVal.nombre === 'NIT') {
        this.tipoEmpComercial = this.tipoEmpresa.find(item => item.nombre === 'Jurídica');
      } else {
        this.tipoEmpComercial = this.tipoEmpresa.find(item => item.nombre === 'Natural');
      }
    },

    selectedActividad(newValue) {
      if (!newValue || this.bloqueaSincronizacion) return;

      this.validarActividad();
      this.idActividad = newValue.id;
      this.idAct = newValue.id;
      this.selectedSeguimiento = null;

      if (newValue.id === 6) {
        // Forzar estado Cotizado
        const estadoCotizado = this.selectEstadosActividad.find(e => e.id === 3);
        if (estadoCotizado && this.selectedEstadoActividad?.id !== 3) {
          this.bloqueaSincronizacion = true;
          this.selectedEstadoActividad = estadoCotizado;
          this.bloqueaSincronizacion = false;
        }
        this.cargarListaSeguimientos(1);

        // Mostrar secciones específicas
        this.ifServicioActividad = true;
        this.ifValorProyecto = true;
        this.ifDocumentos = true;
        this.subirArchivoRUT = true;
        this.subirArchivoDOC = true;
        this.ifObservaciones = false;
        this.ifComentariosAdicionales = true;

      } else if (newValue.id < 6) {
        // Forzar estado Interesado
        const estadoInteresado = this.selectEstadosActividad.find(e => e.id === 2);
        if (estadoInteresado && this.selectedEstadoActividad?.id !== 2) {
          this.bloqueaSincronizacion = true;
          this.selectedEstadoActividad = estadoInteresado;
          this.bloqueaSincronizacion = false;
        }
        this.cargarListaSeguimientos(0);
      }
    },

    selectedSeguimiento(newValue) {
      if (newValue) {
        this.validarSeguimiento();
        this.idSeguimiento = newValue.id;
      } else {

      }
    },


    selectedEstadoActividad(newValue) {
      if (!newValue || this.bloqueaSincronizacion) return;

      if (newValue.id === 3) {
        // Validar antes de cotizar
        this.validarInfoAntesCotizar(this.idprospecto);
        // Forzar actividad Cotización (id=6)
        const actividadCotizacion = this.opcionesActividadSelected?.find(act => act.id === 6);
        if (actividadCotizacion) {
          this.selectedActividad = actividadCotizacion;
          this.idActividad = actividadCotizacion.id;
          this.idAct = actividadCotizacion.id;
        }
        // Si no hay cotización previa, mostrar inputs obligatorios
        const noHayCotizacionPrevia = !this.rutaCot && !this.rutaRut;
        this.ifSeguimientosCotizados = false;
        this.ifServicioActividad = true;
        this.ifValorProyecto = true;
        this.ifServicio = true;
        this.ifDocumentos = true;
        this.ifObservaciones = false;
        this.ifComentariosAdicionales = true;
        this.ifActCotizado = true;
        this.subirArchivoRUT = true;
        this.subirArchivoDOC = true;
        // Si ya hay cotización previa, los archivos no son obligatorios
        if (!noHayCotizacionPrevia) {
          this.subirArchivoRUT = false;
          this.subirArchivoDOC = false;
        }
      } else {
        this.ifValorProyecto = false;
        this.ifServicio = false;
        this.ifServicioActividad = false;
        this.ifDocumentos = false;
        this.subirArchivoRUT = false;
        this.subirArchivoDOC = false;
        this.ifObservaciones = true;
        this.ifComentariosAdicionales = false;
        this.ifActCotizado = false;
      }

      if (newValue.id === 4) {
        this.ifCerradoExitoso = false;
        this.ifCerradoDeclinado = false;
        this.ifActCotizado = false;
        this.ifCerradoExitoso = true;
        this.ifProximoSeguimientoActividad = false;
        this.ifObservaciones = true;
      } else if (newValue.id === 5) {
        this.ifCerradoExitoso = false;
        this.ifCerradoDeclinado = false;
        this.ifActCotizado = false;
        this.ifCerradoDeclinado = true;
        this.ifProximoSeguimientoActividad = false;
        this.ifObservaciones = true;
      } else {
        this.ifCerradoDeclinado = false;
        this.ifCerradoExitoso = false;
      }

      if (![3, 4, 5].includes(newValue.id)) {
        this.ifProximoSeguimientoActividad = true;
        this.ifSeguimientosCotizados = true;
      }
      // Solo limpiar actividad si es un cambio manual (no sincronizado)
      if (newValue.id < 3 && !this.bloqueaSincronizacion) {
        this.selectedActividad = null;
      }
    },

    proximoSeguimientoActividad(newValue) {
      if (newValue) {
        this.ifProximoSeguimientoActividad = true;
      } else {
        this.ifProximoSeguimientoActividad = true;
      }
    },

    fechaInicio(newValue) {
      // Si ya había fechaFin y es anterior a la nueva inicio,
      // la limpiamos para forzar al usuario a elegir de nuevo.
      if (this.fechaInicio == null) {
        this.fechaFin = null;
      }
      else if (this.fechaFin && this.fechaFin < newValue) {
        this.fechaFin = this.fechaInicio;
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

    prospecto(newValue) {
      if (newValue == null) {
        this.alertaProspecto = false;
        this.mensajeAlerta = '';
        this.dsCrear = false;
        return;
      }
      this.verificarEmpresa(newValue.id);
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

    irComercial() {
      this.$router.push('/comercial');
    },

    irPendientesGeneral() {
      this.$router.push('/pendiente-general');
    },

    irConfiguracion() {
      this.$router.push('/configuracion');
    },

    irPQR() {
      this.$router.push('/pqr');
    },

    irPedidos() {
      this.$router.push('/pedidos');
    },

    irCampañas() {
      this.$router.push('/campana');
    },

    irInformesCampañas() {
      this.$router.push('/informes-campanas');
    },

    irGaleriaCampanas() {
      this.$router.push('/VerCampanas');
    },

    irContactos() {
      this.$router.push('/contactos');
    },

    colorVcard(item) {

      switch (item.colorrec) {
        case 'cdf5d5':
          return true;
        case '#f5cdcd':
          return true;
        case '#f3f5cd':
          return true;
        case 'white':
          return false;
        default:
          return false;
      }

    },

    cargarObservaciones() {
      axios.post(this.baseURL + 'api/histprocom', {
        'idproccom': this.idproccom,
        'idusu': localStorage.getItem('idUsuario'),
      })
        .then(response => {
          const data = response.data.data;

          // Limpiar los items de cada estado
          this.estados2.forEach(estado => {
            estado.items = [];
          });

          // Guardar observación general (de la primera fila que venga)
          if (data.length > 0) {
            this.observacionGeneral = data[0].observproy || '';
          }

          // Llenar items por estado (para otras vistas)
          data.forEach(item => {
            let estadoId = item.estado;
            const estado = this.estados2.find(e => e.id === item.idactividad);
            if (estado) {
              estado.items.push({
                descripcion: item.observact,
                fecha: item.fecha_act,
                idservicio: this.getNombreServicio(item.idservicio),
                valor_proyecto: item.cosproy,
                estado: estadoId,
                rutacot: item.rutacot,
                rutarut: item.rutarut,
                idEstado: item.idactividad, // importante para el filtro
              });
            }
          });

          // === NUEVO: llenar la lista plana para el historial ===
          this.historialActividades = data
            .filter(item => this.estados2.some(e => e.id === item.idactividad)) // Solo actividades válidas
            .map(item => ({
              descripcion: item.observact,
              fecha: item.fecha_act,
              idservicio: this.getNombreServicio(item.idservicio),
              valor_proyecto: item.cosproy,
              estado: item.estado,
              rutacot: item.rutacot,
              rutarut: item.rutarut,
              idEstado: item.idactividad,
              estadoNombre: (this.estados2.find(e => e.id === item.idactividad) || {}).nombre,
              color: (this.estados2.find(e => e.id === item.idactividad) || {}).color,
            }));
        })
        .catch(error => {
          console.log(error);
        });
    },

    cargarHistorialLlamadas() {

      axios.post(this.baseURL + 'api/cargarhistorialgestion2', {
        'idproccom': this.idproccom ? this.idproccom : 0,
      })
        .then(response => {
          this.historialGestion = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    editProspecto() {
      // Abre el diálogo y después de 0.5s coloca la razón social en el filtro
      this.limpiarCamposDialogActividad();
      this.dialogNuevaActividad = false;
      this.cargarEstadosActividad()
      this.abrirDialogProspectos();
      setTimeout(() => {
        const razonSocial = this.infoProspectoDialog?.find(c => c.nombre === 'Razón Social')?.valor || '';
        if (razonSocial) {
          const empresa = this.listaEmpresasComercial.find(e => e.p_razon_social === razonSocial);
          this.filtroRazonSocialEmpresasComercial = empresa || null;
          this.filtrarEmpresas();
        }
      }, 800);
    },

    abrirFormularioActividad(item, column) {
      // Estado y empresa actuales
      const idEstado = Number(item?.idestado ?? localStorage.getItem('idestado') ?? 0);
      const idEmpresa = item?.idprosp ?? localStorage.getItem('idempresa');

      // Selecciones base
      this.selectedClienteActividad = this.selectClientesActividad.find(e => e.id == idEmpresa) || null;
      this.selectedServicioActividad = this.selectServiciosActividad.find(
        e => e.nombre == (localStorage.getItem('servicio') || item?.nomserv)
      ) || null;
      this.selectedValorProyecto = localStorage.getItem('valorproy') ?? null;

      // Rutas (links + botón Histórico)
      const rutaCotLocal = localStorage.getItem('rutacot');
      const rutaRutLocal = localStorage.getItem('rutarut');
      this.rutaCot = item?.rutaCot || rutaCotLocal || null;
      this.rutaRut = item?.rutaRut || rutaRutLocal || null;

      console.log("Rutas cargadas:");
      console.log("rutaCot:", this.rutaCot);
      console.log("rutaRut:", this.rutaRut);
      this.ifHistorico = (
        this.rutaCot &&
        this.rutaRut &&
        this.rutaCot !== 'null' &&
        this.rutaRut !== 'null'
      );

      // Copia master de estados (evita degradar por filtros)
      if (!this._estadosActividadMaster) {
        this._estadosActividadMaster = Array.isArray(this.selectEstadosActividad)
          ? [...this.selectEstadosActividad]
          : [];
      }

      // Reset de flags (igual que en crearNuevaActividad)
      this.ifBtnRegistrarActividad = true;
      this.ifActividad = false;
      this.ifActCotizado = false;
      this.ifServicio = false;
      this.ifValorProyecto = false;
      this.ifDocumentos = false;
      this.subirArchivoRUT = false;
      this.subirArchivoDOC = false;
      this.ifComentariosAdicionales = false;
      this.ifProximoSeguimientoActividad = false;
      this.ifSeguimientosCotizados = false;
      this.ifObservaciones = false;
      this.mostrarInputsDocs = false;
      this.dsServicio = true;
      this.roValorProyecto = true;
      this.readonlyServicioSeleccionado = true;
      this.ifCerradoExitoso = false;
      this.ifCerradoDeclinado = false;
      this.roEstadoActividad = false;

      // --- 1) Cerrado Declinado (5) → SOLO Histórico
      if (idEstado === 5) {
        this.dialogHistorico = true;
        this.ifCerradoDeclinado = true;
        this.ifProximoSeguimientoActividad = false;
        this.ifObservaciones = true;
        this.cargarObservaciones();
        return;
      }

      // --- 2) Cerrado Exitoso (4) → Formulario "simple" (observaciones+docs, sin lápiz)
      if (idEstado === 4) {
        this.ifCerradoExitoso = true;
        this.dialogNuevaActividad = true;
        this.ifProximoSeguimientoActividad = false;
        this.ifObservaciones = true;

        const base = this._estadosActividadMaster.length
          ? [...this._estadosActividadMaster]
          : [...this.selectEstadosActividad];
        this.selectEstadosActividad = base.filter(e => e.id === 4);
        this.selectedEstadoActividad = this.selectEstadosActividad[0] || null;
        this.roEstadoActividad = true;

        this.ifServicio = true;           // servicio solo lectura
        this.ifObservaciones = true;      // textarea
        this.ifDocumentos = true;         // para ver links
        this.ifBtnRegistrarActividad = false; // no registrar actividad aquí
        // (no mostramos ifActCotizado ni valor de proyecto)
        return;
      }

      // --- 3) Cotización (columna 6 / estado 3) → igual a crearNuevaActividad (≥3)
      if (column?.id === 6) {
        this.dialogNuevaActividad = true;

        // Flags como en crearNuevaActividad (rama ≥ 3)
        this.ifComentariosAdicionales = true;
        this.ifServicio = true;
        this.ifValorProyecto = true;
        this.ifActCotizado = true;     // título con lápiz
        this.ifDocumentos = true;      // bloque docs
        this.subirArchivoRUT = true;   // necesarios para que el lápiz muestre inputs
        this.subirArchivoDOC = true;
        this.ifObservaciones = false;  // (en tu crearNuevaActividad lo dejas en false)
        this.ifBtnRegistrarActividad = true;

        const base = this._estadosActividadMaster.length
          ? [...this._estadosActividadMaster]
          : [...this.selectEstadosActividad];
        this.selectEstadosActividad = base.filter(e => [3, 4, 5].includes(e.id));
        this.selectedEstadoActividad =
          this.selectEstadosActividad.find(e => e.id == idEstado) ||
          this.selectEstadosActividad.find(e => e.id == 3) ||
          null;

        // Reset para que al reabrir exija seleccionar actividad y se muestre "Próximo seguimiento"
        this.selectedActividad = null;
        this.selectedSeguimiento = null;
        this.proximoSeguimientoActividad = null;
        // ifProximoSeguimientoActividad se queda en false hasta que elijan actividad

      } else {
        // Otras columnas → Histórico
        this.dialogHistorico = true;
        this.cargarObservaciones();
        this.ifActividad = true;
        this.cargarEstadosActividad();
        this.ifProximoSeguimientoActividad = true;
      }

      // Bloquear cambio de estado si es > 3
      this.roEstadoActividad = idEstado > 3;
    },

    limpiarCamposDialogActividad() {
      this.selectedClienteActividad = null;
      this.selectedActividad = null;
      this.selectedSeguimiento = null;

      this.selectedObservacionesActividad = null;
      this.selectedObservacionesSeguimiento = null;
      this.proximoSeguimientoActividad = null;

      this.selectedServicioActividad = null;
      this.selectedValorProyecto = null;

      this.archivoRUT = null;
      this.archivosActividad = null;

      this.selectedComentariosActividad = null;
      this.validandoActividad = false;

    },

    cargarEstadosActividad() {
      axios.get(this.baseURL + 'api/cargares')
        .then(response => {
          this.selectEstadosActividad = response.data.data;
          this.selectEstadosActividad.shift();
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
    },

    cargarServiciosActividad() {
      axios.get(this.baseURL + 'api/cargarsv')
        .then(response => {
          // Filtra para ocultar el servicio con nombre 'Presentación Corporativa'
          const serviciosFiltrados = response.data.data.filter(s => s.nombre?.toLowerCase() !== 'presentacion comercial');
          this.selectServiciosActividad = serviciosFiltrados;
          this.selectServiciosOportunidad = serviciosFiltrados;
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
    },

    cargarClientesActividad() {
      axios.post(this.baseURL + 'api/cargarpp', {
        'idusu': localStorage.getItem('idUsuario')
      })
        .then(response => {
          this.selectClientesActividad = response.data.data;
          this.selectClientesOportunidad = response.data.data;
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
    },

    registrarActividad() {


      var isValid1 = '';
      var isValid2 = '';
      var servicio = '';
      var fechaProxSeg = '';
      var seguimiento = '';
      var idAct = '';
      var valorproyecto = '';
      let mensajeFaltantes1 = '';
      let mensajeFaltantes2 = '';
      this.validandoActividad = true;

      // Si no hay una actividad inicial 
      if (this.estados.every(e => e.items.length === 0) && (this.selectedEstadoActividad.id === 5)) {
        this.ifBotonActividadCargando = false;
        this.mensajeAlertLogin = 'No se puede registrar el caso como Cerrado o Ganado, sin antes registar una actividad inicial.';
        this.alerta = true;
        return;
      }



      if (this.selectedEstadoActividad == null) {
        this.mensajeAlertLogin = 'Por favor, seleccione un estado de actividad.';
        this.alerta = true;
        return;
      }
      if (this.selectedEstadoActividad.id === 3) {
        // Validación específica para estado "Cotización": no exigir próximo seguimiento
        const isValidCot = this.selectClientesActividad
          && this.idActividad !== null
          && this.idSeguimiento !== null
          && this.selectedEstadoActividad
          && this.selectedServicioActividad
          && this.selectedValorProyecto
          && this.selectedComentariosActividad;

        // Construir mensaje de campos faltantes para cotización
        let mensajeFaltantesCot = this.selectClientesActividad ? '' : 'Cliente, ';
        mensajeFaltantesCot += this.idActividad !== null ? '' : 'Actividad, ';
        mensajeFaltantesCot += this.selectedValorProyecto ? '' : 'Valor del Proyecto, ';
        mensajeFaltantesCot += this.selectedComentariosActividad ? '' : 'Comentarios Adicionales, ';
        mensajeFaltantesCot += this.proximoSeguimientoActividad ? '' : 'Fecha de Próximo Seguimiento, ';
        mensajeFaltantesCot += this.idSeguimiento !== null ? '' : 'Seguimiento, ';

        if (!isValidCot) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos:\n' + mensajeFaltantesCot;
          this.alerta = true;
          return;
        }
      }

      if (this.selectedEstadoActividad.id === 4) {
        isValid1 = this.selectClientesActividad && this.selectedObservacionesActividad && this.selectedEstadoActividad;
        isValid2 = this.selectClientesActividad && this.selectedEstadoActividad && this.selectedValorProyecto;

        mensajeFaltantes1 = this.selectClientesActividad ? '' : 'Cliente, ';
        mensajeFaltantes1 += this.selectedObservacionesActividad ? '' : 'Observaciones, ';
        mensajeFaltantes1 += this.selectedEstadoActividad ? '' : 'Estado de Actividad';

        mensajeFaltantes2 = this.selectClientesActividad ? '' : 'Cliente, ';
        mensajeFaltantes2 += this.selectedEstadoActividad ? '' : 'Estado de Actividad, ';
        mensajeFaltantes2 += this.selectedValorProyecto ? '' : 'Valor del Proyecto';
      } else if (this.selectedEstadoActividad.id === 5) {
        isValid1 = this.selectClientesActividad && this.selectedObservacionesActividad && this.selectedEstadoActividad;
        isValid2 = this.selectClientesActividad && this.selectedEstadoActividad && this.selectedValorProyecto;

        mensajeFaltantes1 = this.selectClientesActividad ? '' : 'Cliente, ';
        mensajeFaltantes1 += this.selectedObservacionesActividad ? '' : 'Observaciones, ';
        mensajeFaltantes1 += this.selectedEstadoActividad ? '' : 'Estado de Actividad';

        mensajeFaltantes2 = this.selectClientesActividad ? '' : 'Cliente, ';
        mensajeFaltantes2 += this.selectedEstadoActividad ? '' : 'Estado de Actividad, ';
        mensajeFaltantes2 += this.selectedValorProyecto ? '' : 'Valor del Proyecto';
      } else {
        isValid1 = this.selectClientesActividad && this.idActividad !== null && this.selectedEstadoActividad && this.proximoSeguimientoActividad && this.idSeguimiento;
        isValid2 = this.selectClientesActividad && this.idActividad !== null && this.selectedEstadoActividad && this.selectServiciosActividad && this.selectedValorProyecto && this.selectedComentariosActividad && this.proximoSeguimientoActividad && this.idSeguimiento;

        mensajeFaltantes1 = this.selectClientesActividad ? '' : 'Cliente, ';
        mensajeFaltantes1 += this.idActividad !== null ? '' : 'Actividad, ';
        mensajeFaltantes1 += this.selectedEstadoActividad ? '' : 'Estado de Actividad, ';
        mensajeFaltantes1 += this.proximoSeguimientoActividad ? '' : 'Fecha de Próximo Seguimiento, ';
        mensajeFaltantes1 += this.idSeguimiento ? '' : 'Seguimiento';

        mensajeFaltantes2 = this.selectClientesActividad ? '' : 'Cliente, ';
        mensajeFaltantes2 += this.idActividad !== null ? '' : 'Actividad, ';
        mensajeFaltantes2 += this.selectedEstadoActividad ? '' : 'Estado de Actividad, ';
        mensajeFaltantes2 += this.selectServiciosActividad ? '' : 'Servicio, ';
        mensajeFaltantes2 += this.selectedValorProyecto ? '' : 'Valor del Proyecto, ';
        mensajeFaltantes2 += this.selectedComentariosActividad ? '' : 'Comentarios Adicionales, ';
        mensajeFaltantes2 += this.proximoSeguimientoActividad ? '' : 'Fecha de Próximo Seguimiento, ';
        mensajeFaltantes2 += this.idSeguimiento ? '' : 'Seguimiento';

      }

      if (this.selectedServicioActividad === null || this.selectedServicioActividad === undefined) {
        servicio = 0;
      } else {
        servicio = this.selectedServicioActividad.id;
      }

      if (this.idSeguimiento === null) {
        seguimiento = 0;
      } else {
        seguimiento = this.idSeguimiento;
      }

      if (this.proximoSeguimientoActividad === null) {
        fechaProxSeg = '';
      } else {
        fechaProxSeg = this.proximoSeguimientoActividad;
      }

      if (this.idActividad === null) {
        idAct = 0;
      } else {
        idAct = this.selectedActividad.id;
      }


      if (this.selectedValorProyecto === null) {
        valorproyecto = 0;
      } else {
        valorproyecto = this.selectedValorProyecto;
      }

      if (this.selectedEstadoActividad.id == 3 && !this.rutaRut && (!this.archivoRUT || this.archivoRUT.length === 0)) {
        this.mensajeAlertLogin = 'Por favor, adjunte el archivo RUT.';
        this.alerta = true;
        return;
      }
      if (this.selectedEstadoActividad.id == 3 && !this.rutaCot && (!this.archivosActividad || this.archivosActividad.length === 0)) {
        this.mensajeAlertLogin = 'Por favor, adjunte el documento requerido.';
        this.alerta = true;
        return;
      }

      if (this.selectedEstadoActividad.id == 3) {

        if (!isValid2) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos: \n' + mensajeFaltantes2;
          this.alerta = true;
          return;
        }
      } else {
        if (!isValid1) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos: \n' + mensajeFaltantes1;
          this.alerta = true;
          return;
        }

      }

      // Bloque el campo del estado de actividad si el estado es cerrado exitoso o cerrado declinado
      if (this.estadoactual < 3 && this.selectedEstadoActividad.id == 4) {
        this.mensajeAlertLogin = 'No se puede registrar una actividad con estado Cerrado Exitoso, sin haber registrado una cotización.';
        this.alerta = true;
        return;
      }
      if (this.selectedServicioActividad.id == 9 && this.selectedEstadoActividad.id == 3) {
        this.mensajeAlertLogin = 'No se puede Cotizar un proyecto en estado presentación Corporativa';
        this.alerta = true;
        return;
      }


      let formData = new FormData();
      let formData2 = new FormData();
      formData.append('procom', this.idproccom);
      formData.append('act', idAct);
      formData.append('obs', this.selectedObservacionesActividad ? this.selectedObservacionesActividad : this.selectedComentariosActividad);
      formData.append('estado', this.selectedEstadoActividad.id);
      formData.append('fpseg', fechaProxSeg);
      formData.append('idseg', seguimiento);
      formData.append('idcom', localStorage.getItem('idUsuario'));
      formData.append('cosproy', valorproyecto);
      formData.append('idserv', servicio);
      formData.append('obs_seg', this.selectedObservacionesSeguimiento ? this.selectedObservacionesSeguimiento : 'No se indico una observación de Seguimiento');

      formData2.append('fileRUT', this.archivoRUT ? this.archivoRUT : '');
      formData2.append('fileCOT', this.archivosActividad ? this.archivosActividad : '');

      this.mensajeAlertLogin = 'Guardando tarea...';
      this.alerta = true;
      this.ifCargando = true;

      console.log('Subiendo archivos...');
      console.log('Archivo RUT:', this.archivoRUT);
      console.log('Archivos COT:', this.archivosActividad);

      if (this.selectedEstadoActividad.id == 3 && (this.archivoRUT || this.archivosActividad)) {

        //si ambos archivos tienen el mismo nombre, el proceso se detiene
        if (this.archivosRut && this.archivosActividad) {
          if (this.archivoRUT.name === this.archivosActividad.name) {
            this.mensajeAlertLogin = 'Los archivos no pueden tener el mismo nombre.';
            this.alerta = true;
            this.ifCargando = false;
            return;
          }
        }

        axios.post(this.baseURL + 'api/uploadFilesActividad', formData2, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          console.log('Archivos subidos:', response.data);
          console.log('Ruta RUT:', response.data.urlRUT);
          console.log('Ruta COT:', response.data.urlCOT);

          if (response.data.urlCOT) {
            localStorage.setItem('rutacot', response.data.urlCOT);
            formData.append('rutacot', response.data.urlCOT ? response.data.urlCOT : '');
          }
          if (response.data.urlRUT) {
            localStorage.setItem('rutarut', response.data.urlRUT);
            formData.append('rutarut', response.data.urlRUT ? response.data.urlRUT : '');
          }

          return;

        }).catch(error => {
          console.error('Error al subir archivos:', error);
          this.ifCargando = false;
          this.mensajeAlertLogin = 'Error al subir los archivos.';
          this.alerta = true;
          this.validandoActividad = false;

        }).then(() => {

          axios.post(this.baseURL + 'api/newproccomact', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }).then(response => {
            localStorage.setItem('idestado', this.selectedEstadoActividad.id);
            // Guarda el servicio seleccionado
            if (this.selectedServicioActividad && this.selectedServicioActividad.nombre) {
              localStorage.setItem('servicio', this.selectedServicioActividad.nombre);
            }
            localStorage.setItem('idestado', this.selectedEstadoActividad.id);
            this.estadoactual = this.selectedEstadoActividad.id;
            this.dialogNuevaActividad = false;
            this.limpiarCamposDialogActividad();
            this.cargarClientesActividad();
            this.cargarEstadosActividad();

            console.log('Tarea registrada:', response.data.data);

            if (this.selectedEstadoActividad != 9) {
              this.readonlyServicio = true;
            }
            this.resetFormularioActividad();

            setTimeout(() => {
              this.mensajeAlertLogin = 'La tarea se ha registrado correctamente.';
              this.alerta = true;
              this.ifCargando = false;
              this.mostrarInputCot = false;
              this.mostrarInputRUT = false;
              this.cargarActividades();
            }, 600);
          })
        })
          .catch(error => {
            console.error('Error al registrar la tarea:', error);
          });

      } else {

        axios.post(this.baseURL + 'api/newproccomact', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          localStorage.setItem('idestado', this.selectedEstadoActividad.id);
          // Guarda el servicio seleccionado
          if (this.selectedServicioActividad && this.selectedServicioActividad.nombre) {
            localStorage.setItem('servicio', this.selectedServicioActividad.nombre);
          }
          localStorage.setItem('idestado', this.selectedEstadoActividad.id);
          this.estadoactual = this.selectedEstadoActividad.id;
          this.dialogNuevaActividad = false;
          this.limpiarCamposDialogActividad();
          this.cargarClientesActividad();
          this.cargarEstadosActividad();

          console.log('Tarea registrada:', response.data.data);

          if (this.selectedEstadoActividad != 9) {
            this.readonlyServicio = true;
          }
          this.resetFormularioActividad();

          setTimeout(() => {
            this.mensajeAlertLogin = 'La tarea se ha registrado correctamente.';
            this.alerta = true;
            this.ifCargando = false;
            this.cargarActividades();
          }, 600);
        })
          .catch(error => {
            console.error('Error al registrar la tarea:', error);
          });
      }
    },

    cargarActividades() {
      const data = {
        idproccom: this.idproccom,
      };

      axios.post(this.baseURL + 'api/cargarprosppend', data)
        .then(response => {
          console.log("Actividades cargadas:", response.data.data);

          if (response.data.data.length > 0) {
            this.estadoSeguimientos = response.data.data[0].idest;
          }

          if (response.data.data.length === 0) {
            this.ifBotonActividadCargando = false;
            this.registrarActividadInicial();
            //Filtrar los estados para que no muestre "Cerrado Exitoso" y "Cerrado Declinado" Sin antes tener una actividad Inicial
            this.selectEstadosActividad = this.selectEstadosActividad.filter(
              e => e.id !== 4 && e.id !== 5
            );
            this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 2);

            return;
          }

          const datos = response.data?.data;

          this.estados.forEach(estado => {
            estado.items = [];
          });

          var i = 1;
          datos.forEach(item => {
            const etapa = item.nomact || 'Sin etapa';

            const estadoEncontrado = this.estados.find(e => e.nombre === etapa);

            var nuevoItem = [];

            if (i == 1) {
              this.razon_social = item.razon_social;
              this.idprospecto = item.idprosp;
              this.ultact = item.nomact;
              this.ultactfec = item.fecha_act;
              this.ultseg = item.nomseg;
              this.ultsegfec = item.fecproxseg;
              this.ultsegAct = item.idseg;
              this.ultsegObser = item.segobs;
              localStorage.setItem('valorproy', item.valorproy);
              localStorage.setItem('rutacot', item.rutacot);
              localStorage.setItem('rutarut', item.rutarut);

              nuevoItem = {
                name: item.razon_social,
                description: item.nomserv,
                date: item.fecha_act,
                idproc: item.idproc,
                obsev: item.obsev,
                obseg: item.obseg,
                idprosp: item.idprosp,
                idest: item.idest,
                idtipoact: item.idpcact,
                colorrec: item.idest == 4 ? "#cdf5d5" : item.idest == 5 ? "#f5cdcd" : "#f3f5cd",
                rutaCot: item.rutacot,
                rutaRut: item.rutarut,
                iconoEstado: item.idest == 4 ? "mdi-trophy" : item.idest == 5 ? "mdi-emoticon-sad" : null,
                estadoCotizado: item.estcot > 0 ? "Cotizado" : null,

              };
              i++;
            }
            else {
              nuevoItem = {
                name: item.razon_social,
                description: item.nomserv,
                date: item.fecha_act,
                idproc: item.idproc,
                obsev: item.obsev,
                obseg: item.obseg,
                idprosp: item.idprosp,               ///EL ITEM
                idest: item.idest,
                idtipoact: item.idpcact,
                colorrec: 'white',
                rutaCot: item.rutacot,
                rutaRut: item.rutarut,
                iconoEstado: null,
                estadoCotizado: item.estcot > 0 ? "Cotizado" : null,
              };
            }



            if (estadoEncontrado) {
              estadoEncontrado.items.push(nuevoItem);
            } else {
              // Si no coincide con ningún estado, lo pone en "Sin etapa"
              const sinEtapa = this.estados.find(e => e.nombre === 'Sin etapa');
              if (sinEtapa) {
                sinEtapa.items.push(nuevoItem);
              }
            }
          });
          this.ifBotonActividadCargando = false;

        })
        .catch(error => {
          console.error('Error al cargar actividades:', error);
        });
    },

    irComercial() {
      this.$router.push('/comercial');
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

    registrarActividadInicial() {

      let idempresa = localStorage.getItem('idempresa');
      let idestado = localStorage.getItem('idestado');
      let idproccom = localStorage.getItem('idproccom');
      let idserv = localStorage.getItem('servicio');
      let valorpro = localStorage.getItem('valorproy');
      let idprospecto = localStorage.getItem('idempresa');

      console.log('ID Empresa:', idempresa);
      console.log('ID Estado:', idestado);
      console.log('ID Proceso Comercial:', idproccom);
      console.log('ID servicio:', idserv);
      console.log('Valor proyecto:', valorpro);
      console.log('ID Prospecto:', idprospecto);

      this.dialogNuevaActividad = true;

      setTimeout(() => {
        this.mensajeAlertLogin = 'No se encontraron actividades registradas. Se procederá a registrar una actividad inicial.';
        this.alerta = true;
        this.selectedClienteActividad = this.selectClientesActividad.find(item => item.id == idempresa);
        this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id == idestado);
        if (idestado == 1) {
          this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id == 2);
        }
        this.selectedServicioActividad = this.selectServiciosActividad.find(e => e.nombre == idserv);
        this.selectedValorProyecto = valorpro;
        this.idproccom = idproccom;
        this.ifProximoSeguimientoActividad = true;
        this.ifServicio = false;
        this.idprospecto = idprospecto;
        console.log("ID PROSPECTO: ", this.idpropsecto)
      }, 1000);
    },

    crearNuevaActividad() {
      const idEmpresa = localStorage.getItem('idempresa');

      // Selecciones base
      this.selectedClienteActividad = this.selectClientesActividad.find(e => e.id == idEmpresa) || null;
      this.selectedServicioActividad = this.selectServiciosActividad.find(
        e => e.nombre == localStorage.getItem('servicio')
      ) || null;
      this.selectedValorProyecto = localStorage.getItem('valorproy') ?? null;

      // Rutas (para links e histórico)
      const rutaCotLocal = localStorage.getItem('rutacot');
      const rutaRutLocal = localStorage.getItem('rutarut');
      this.rutaCot = rutaCotLocal || null;
      this.rutaRut = rutaRutLocal || null;

      console.log("Rutas cargadas:");
      console.log("rutaCot:", this.rutaCot);
      console.log("rutaRut:", this.rutaRut);
      this.ifHistorico = (
        this.rutaCot &&
        this.rutaRut &&
        this.rutaCot !== 'null' &&
        this.rutaRut !== 'null'
      );

      // Reset flags comunes 
      this.dialogNuevaActividad = true;
      this.ifBtnRegistrarActividad = true;
      this.ifActividad = false;
      this.ifActCotizado = false;
      this.ifServicio = false;
      this.ifValorProyecto = false;
      this.ifDocumentos = false;
      this.subirArchivoRUT = false;
      this.subirArchivoDOC = false;
      this.ifComentariosAdicionales = false;      // <-- reset aquí
      this.ifProximoSeguimientoActividad = false; // <-- reset aquí
      this.ifSeguimientosCotizados = false;
      this.ifObservaciones = false;
      this.mostrarInputsDocs = false;
      this.dsServicio = true;
      this.roValorProyecto = true;
      this.readonlyServicioSeleccionado = true;
      this.roEstadoActividad = false;

      // === ESTADO ACTUAL DEL PIPE ===
      if (this.estadoSeguimientos >= 3) {
        // ----- COTIZACIÓN -----
        this.ifComentariosAdicionales = true;
        this.ifServicio = true;
        this.ifValorProyecto = true;
        this.ifActCotizado = true;
        this.ifDocumentos = true;
        this.subirArchivoRUT = true;
        this.subirArchivoDOC = true;
        this.ifObservaciones = false;
        this.ifBtnRegistrarActividad = true;

        const noHayActividades = this.estados.every(e => (e.items?.length || 0) === 0);
        let base = Array.isArray(this.selectEstadosActividad) ? [...this.selectEstadosActividad] : [];
        if (noHayActividades) base = base.filter(e => e.id !== 4 && e.id !== 5);

        this.selectEstadosActividad = base.filter(e => [3, 4, 5].includes(e.id));
        this.selectedEstadoActividad =
          this.selectEstadosActividad.find(e => e.id == 3) ||
          this.selectEstadosActividad[0] ||
          null;

        // Reset para que, al reabrir, elija actividad y entonces se muestre el bloque
        this.selectedActividad = null;
        this.selectedSeguimiento = null;
        this.proximoSeguimientoActividad = null;
        // ifProximoSeguimientoActividad e ifComentariosAdicionales se quedan en false aquí

        return;
      }

      // ----- Estados < 3 (antes de cotizar) -----
      this.ifServicio = false;
      this.ifValorProyecto = false;
      this.dsServicio = true;
      this.ifSeguimientosCotizados = true;
      this.roValorProyecto = true;
      this.subirArchivoRUT = true;
      this.subirArchivoDOC = true;
      this.ifObservaciones = true;

      this.selectedEstadoActividad = this.selectEstadosActividad.find(
        e => e.id == localStorage.getItem('idestado')
      ) || null;

      this.ifActividad = true;
      if (typeof this.cargarActividades === 'function') this.cargarActividades();

      this.ifProximoSeguimientoActividad = true;  // <-- prender bloque de próximo seguimiento
      this.ifComentariosAdicionales = true;       // <-- y comentarios adicionales
    },

    cambiarClave() {
      const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

      if (this.nuevaClave !== this.confirmarClave) {
        this.alerta = true;
        this.mensajeAlertLogin = 'Las claves no coinciden.';
        return;
      } else if (!regex.test(this.nuevaClave)) {
        this.alerta = true;
        this.mensajeAlertLogin = 'La nueva clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.';
        return;
      } else {
        axios.post(this.baseURL + 'api/cambiarclave', {
          idusu: localStorage.getItem('idUsuario'),
          claveActual: CryptoJS.MD5(this.claveActual).toString(),
          nuevaClave: CryptoJS.MD5(this.nuevaClave).toString(),
        })
          .then(response => {
            if (response.data.data[0].respuesta == 'La clave actual ingresada no coincide con el usuario.') {
              this.alerta = true;
              this.mensajeAlertLogin = 'La clave actual ingresada no coincide con el usuario.';
            } else if (response.data.data[0].respuesta == 'La clave ha sido editada correctamente.') {
              this.alerta = true;
              this.mensajeAlertLogin = 'La clave ha sido editada correctamente.';
              this.dialogCambioClave = false;
              this.claveActual = null;
              this.nuevaClave = null;
              this.confirmarClave = null;
            }
          })
          .catch(error => {
            console.error('Error al cambiar la clave:', error);
            this.alerta = true;
            this.mensajeAlertLogin = 'Error al cambiar la clave.';
          });
      }
    },

    isValidPassword(password) {
      const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;
      return regex.test(password);
    },

    cerrarSesion() {
      localStorage.removeItem('idUsuario')
      localStorage.removeItem('idCargo')
      localStorage.removeItem('nombreLogin')
      localStorage.removeItem('apellidoLogin')
      localStorage.removeItem('celularLogin')
      localStorage.removeItem('logueado')
      this.$router.push('/')
    },


    validarActividad() {
      // Validar actividad realizada
      if (!this.selectedActividad) {
        this.idActividad = null;
      } else {
        this.idActividad = this.selectedActividad.id;
      }
    },
    validarSeguimiento() {
      // Validar seguimiento a realizar
      if (!this.selectedSeguimiento) {
        this.idSeguimiento = null;
      } else {
        this.idSeguimiento = this.selectedSeguimiento;
      }
    },

    cargarListaDeActividades() {
      var data = null;
      axios.get(this.baseURL + 'api/cargaActividades')

        .then(response => {

          data = response.data.data;
          console.log("Data : ", data);
          this.opcionesActividadSelected = data;

        })
        .catch(error => {
          console.error('Error al cargar la lista de actividades:', error);
        });


    },

    cargarListaSeguimientos(cotiz) {
      var data = null;
      var dato = {
        cotiz: cotiz
      };
      this.opcionesSeguimientoSelected = [];
      axios.post(this.baseURL + 'api/cargaSeguimiento', dato)

        .then(response => {

          data = response.data.data;
          console.log("Data : ", data);
          this.opcionesSeguimientoSelected = data;

        })
        .catch(error => {
          console.error('Error al cargar la lista de actividades:', error);
        });


    },
    resetFormularioActividad() {
      this.selectedActividad = null;
      this.idActividad = null;
      this.idAct = null;
      this.idSeguimiento = null;
      this.selectedEstadoActividad = null;
      this.selectedSeguimiento = null;
      this.proximoSeguimientoActividad = null;
      this.selectedComentariosActividad = null;
      this.selectedServicioActividad = null;
      this.ifServicioActividad = false;
      this.ifValorProyecto = false;
      this.ifDocumentos = false;
      this.ifObservaciones = true;
      this.ifComentariosAdicionales = false;
      this.ifActCotizado = false;
      this.ifProximoSeguimientoActividad = true;
      this.ifCerradoExitoso = false;
      this.ifCerradoDeclinado = false;
      this.subirArchivoRUT = false;
      this.subirArchivoDOC = false;
      this.archivoRUT = null;
      this.archivoDOC = null;
      this.validandoActividad = false;
    },

    abrirDialog(item) {
      this.selectedItem = item;
      this.dialogObsCompleta = true;
    },
    formatDate(dateString) {
      // Si la fecha contiene hora en formato AM/PM, lo transformamos
      if (dateString.includes('AM') || dateString.includes('PM')) {
        // Reemplazamos el espacio entre la fecha y la hora con 'T' para que sea un formato ISO 8601
        let [date, time] = dateString.split(' ');  // Separamos la fecha de la hora

        // Convertir la hora AM/PM a 24 horas
        let [hours, minutes] = time.split(':');
        let period = minutes.substring(2);  // 'AM' o 'PM'
        minutes = minutes.substring(0, 2);

        // Ajuste para AM/PM
        if (period === 'AM' && hours === '12') {
          hours = '00'; // 12 AM es medianoche
        } else if (period === 'PM' && hours !== '12') {
          hours = (parseInt(hours) + 12).toString(); // 12 PM es mediodía, el resto se suma 12
        }

        // Reconstruimos la fecha con formato 'YYYY-MM-DDTHH:mm:ss'
        let formattedDate = `${date}T${hours}:${minutes}:00`;

        // Creamos el objeto Date
        let fecha = new Date(formattedDate);

        if (isNaN(fecha)) {
          return 'Fecha no válida';
        }

        // Obtener el día, mes y año
        let day = fecha.getDate().toString().padStart(2, '0'); // Asegura que el día tenga dos dígitos
        let month = (fecha.getMonth() + 1).toString().padStart(2, '0'); // Asegura que el mes tenga dos dígitos
        let year = fecha.getFullYear();

        // Formato: dd/mm/yyyy
        return `${day}/${month}/${year}`;
      } else {
        // Si no tiene hora en AM/PM, lo parseamos directamente
        let fecha = new Date(dateString);
        if (isNaN(fecha)) {
          return 'Fecha no válida';
        }

        // Obtener el día, mes y año
        let day = fecha.getDate().toString().padStart(2, '0'); // Asegura que el día tenga dos dígitos
        let month = (fecha.getMonth() + 1).toString().padStart(2, '0'); // Asegura que el mes tenga dos dígitos
        let year = fecha.getFullYear();

        // Formato: dd/mm/yyyy
        return `${day}/${month}/${year}`;
      }
    },
    formatDate2(dateString) {
            const date = new Date(dateString);
            const day = String(date.getUTCDate()).padStart(2, '0');
            const month = String(date.getUTCMonth() + 1).padStart(2, '0');
            const year = date.getUTCFullYear();
            const hours = String(date.getUTCHours()).padStart(2, '0');
            const minutes = String(date.getUTCMinutes()).padStart(2, '0');
            return `${day}/${month}/${year} ${hours}:${minutes}`;
        },
    validarInfoAntesCotizar(idProspecto) {
      console.log("idProspecto:", idProspecto);
      axios.post(this.baseURL + 'api/cargaproscon', {
        idprosp: idProspecto
      })
        .then(async response => {
          const data = response.data.data[0];
          await this.cargarCiudadesAsync(data.p_dpto);
          await this.llamadoCargosAsync(data.pc_categoria);
          console.log("Data prospecto: ", data);

          const getNombre = (arr, id) => {
            if (!id) return '';
            const obj = arr.find(e => e.id == id);
            return obj ? (obj.nombre || obj.descripcion || obj.valor || obj.tipo || obj.categoria || obj.sector) : id;
          };

          const camposProspecto = [
            { nombre: 'NIT', valor: data.p_nit },
            { nombre: 'Razón Social', valor: data.p_razon_social },
            { nombre: 'Tipo Identificación', valor: getNombre(this.tiposIdentificacion, data.p_tipo_identif) },
            { nombre: 'Sector', valor: getNombre(this.sectores, data.p_sector) },
            { nombre: 'Dirección', valor: data.p_direccion },
            { nombre: 'Departamento', valor: getNombre(this.departamentos, data.p_dpto) },
            { nombre: 'Ciudad', valor: getNombre(this.ciudades, data.p_ciudad) },
            { nombre: 'Teléfono 1', valor: data.p_telefono1 },
            { nombre: 'Teléfono 2', valor: data.p_telefono2 },
            { nombre: 'Correo Empresa', valor: data.p_correo }
          ];

          const camposContacto = [
            { nombre: 'Nombre', valor: data.pc_nombre },
            { nombre: 'Apellido', valor: data.pc_apellido },
            { nombre: 'Correo', valor: data.pc_correo },
            { nombre: 'Celular', valor: data.pc_celular },
            { nombre: 'Categoría', valor: getNombre(this.categorias, data.pc_categoria) },
            { nombre: 'Cargo', valor: getNombre(this.cargos, data.pc_cargo) }
          ];

          function isEmpty(val) {
            return val === null || val === undefined || (typeof val === 'string' && val.trim() === '');
          }

          let faltantesProspecto = [];
          let faltantesContacto = [];
          // Solo exigir uno de los teléfonos
          const telefono1Vacio = isEmpty(data.p_telefono1);
          const telefono2Vacio = isEmpty(data.p_telefono2);
          camposProspecto.forEach(campo => {
            if (campo.nombre === 'Teléfono 1' || campo.nombre === 'Teléfono 2') return;
            if (isEmpty(campo.valor)) faltantesProspecto.push(campo.nombre);
          });
          if (telefono1Vacio && telefono2Vacio) {
            faltantesProspecto.push('Teléfono');
          }
          camposContacto.forEach(campo => {
            if (isEmpty(campo.valor)) faltantesContacto.push(campo.nombre);
          });

          // Guarda la info para mostrar en el diálogo
          this.infoProspectoDialog = camposProspecto.map(campo => ({
            ...campo,
            faltante: isEmpty(campo.valor)
          }));
          this.infoContactoDialog = camposContacto.map(campo => ({
            ...campo,
            faltante: isEmpty(campo.valor)
          }));

          this.mensajeValidacionCotizacion =
            (faltantesProspecto.length > 0 ? 'Faltan datos de la empresa: ' + faltantesProspecto.join(', ') + '.\n' + '.\n' : '') +
            (faltantesContacto.length > 0 ? 'Faltan datos del contacto: ' + faltantesContacto.join(', ') + '.' : '');

          if (faltantesProspecto.length > 0 || faltantesContacto.length > 0) {
            this.dialogValidarCotizacion = true;
            this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 2); // Regresa a "En Proceso"
          }
          // Si no hay faltantes, no muestra el diálogo y permite continuar
          this.ifProximoSeguimientoActividad = true;
        })
        .catch(error => {
          this.mensajeValidacionCotizacion = 'Error al consultar la información del prospecto.';
          this.dialogValidarCotizacion = true;
          this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 2);
        });
    },

    infoParaMostrarProspecto(idProspecto) {
      console.log("idProspecto:", idProspecto);
      axios.post(this.baseURL + 'api/cargaproscon', {
        idprosp: idProspecto
      })
        .then(async response => {
          const data = response.data.data[0];
          await this.cargarCiudadesAsync(data.p_dpto);
          await this.llamadoCargosAsync(data.pc_categoria);
          console.log("Data prospecto: ", data);

          const getNombre = (arr, id) => {
            if (!id) return '';
            const obj = arr.find(e => e.id == id);
            return obj ? (obj.nombre || obj.descripcion || obj.valor || obj.tipo || obj.categoria || obj.sector) : id;
          };

          const camposProspecto = [
            { nombre: 'NIT', valor: data.p_nit },
            { nombre: 'Razón Social', valor: data.p_razon_social },
            { nombre: 'Tipo Identificación', valor: getNombre(this.tiposIdentificacion, data.p_tipo_identif) },
            { nombre: 'Sector', valor: getNombre(this.sectores, data.p_sector) },
            { nombre: 'Dirección', valor: data.p_direccion },
            { nombre: 'Departamento', valor: getNombre(this.departamentos, data.p_dpto) },
            { nombre: 'Ciudad', valor: getNombre(this.ciudades, data.p_ciudad) },
            { nombre: 'Teléfono 1', valor: data.p_telefono1 },
            { nombre: 'Teléfono 2', valor: data.p_telefono2 },
            { nombre: 'Correo Empresa', valor: data.p_correo }
          ];

          const camposContacto = [
            { nombre: 'Nombre', valor: data.pc_nombre },
            { nombre: 'Apellido', valor: data.pc_apellido },
            { nombre: 'Correo', valor: data.pc_correo },
            { nombre: 'Celular', valor: data.pc_celular },
            { nombre: 'Categoría', valor: getNombre(this.categorias, data.pc_categoria) },
            { nombre: 'Cargo', valor: getNombre(this.cargos, data.pc_cargo) }
          ];

          function isEmpty(val) {
            return val === null || val === undefined || (typeof val === 'string' && val.trim() === '');
          }

          let faltantesProspecto = [];
          let faltantesContacto = [];
          // Solo exigir uno de los teléfonos
          const telefono1Vacio = isEmpty(data.p_telefono1);
          const telefono2Vacio = isEmpty(data.p_telefono2);
          camposProspecto.forEach(campo => {
            if (campo.nombre === 'Teléfono 1' || campo.nombre === 'Teléfono 2') return;
            if (isEmpty(campo.valor)) faltantesProspecto.push(campo.nombre);
          });
          if (telefono1Vacio && telefono2Vacio) {
            faltantesProspecto.push('Teléfono');
          }
          camposContacto.forEach(campo => {
            if (isEmpty(campo.valor)) faltantesContacto.push(campo.nombre);
          });

          // Guarda la info para mostrar en el diálogo
          this.infoProspectoDialog = camposProspecto.map(campo => ({
            ...campo,
            faltante: isEmpty(campo.valor)
          }));
          this.infoContactoDialog = camposContacto.map(campo => ({
            ...campo,
            faltante: isEmpty(campo.valor)
          }));

          this.dialogValidarInfoContacto = true;

        })
        .catch(error => {
          this.mensajeValidacionCotizacion = 'Error al consultar la información del prospecto.';
          this.dialogValidarCotizacion = true;
          this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 2);
        });
    },

    cargarSectores() {
      axios.get(this.baseURL + 'api/cargarse')
        .then(response => { this.sectores = response.data.data; })
        .catch(error => { console.error('Error al cargar sectores:', error); });
    },
    cargarTiposEmpresa() {
      axios.get(this.baseURL + 'api/cargarte')
        .then(response => { this.tiposEmpresa = response.data.data; })
        .catch(error => { console.error('Error al cargar tipos de empresa:', error); });
    },
    cargarTiposIdentificacion() {
      axios.get(this.baseURL + 'api/cargarti')
        .then(response => { this.tiposIdentificacion = response.data.data; })
        .catch(error => { console.error('Error al cargar tipos de identificación:', error); });
    },
    cargarCategorias() {
      axios.get(this.baseURL + 'api/cargarcc')
        .then(response => { this.categorias = response.data.data; })
        .catch(error => { console.error('Error al cargar categorías:', error); });
    },
    cargarDepartamentos() {
      axios.get(this.baseURL + 'api/cargarde')
        .then(response => { this.departamentos = response.data.data; })
        .catch(error => { console.error('Error al cargar departamentos:', error); });
    },

    cargarCiudades(idDepto) {
      // Si no se pasa idDepto, traer todas las ciudades
      const payload = idDepto ? { 'iddpto': idDepto } : {};
      axios.post(this.baseURL + 'api/cargarci', payload)
        .then(response => { this.ciudades = response.data.data; console.log("CIUDADES: ", response) })
        .catch(error => { console.error('Error al cargar ciudades:', error); });

    },
    cargarCargos() {
      axios.post(this.baseURL + 'api/cargaCargos', { 'idusu': 0 })
        .then(response => { this.cargos = response.data.data; console.log("Cargos: ", response) })
        .catch(error => { console.error('Error al cargar cargos:', error); });

    },

    cargarCiudadesAsync(idDepto) {
      return axios.post(this.baseURL + 'api/cargarci', { 'iddpto': idDepto })
        .then(response => { this.ciudades = response.data.data; console.log("Ciudades Async: ", response) });
    },
    llamadoCargosAsync(idCategoria) {
      return axios.post(this.baseURL + 'api/cargaCargos', { 'idcat': idCategoria })
        .then(response => { this.cargos = response.data.data; console.log("Cargos async: ", response) });
    },

    abrirDialogProspectos() {
      this.dialogProspectos = true;
      this.limpiarCamposProspecto();
      this.obtenerEmpresas();
      this.llamadoCategorias();
      this.llamadoTipoIdentificacion();
      this.llamadoTipoEmpresa();
      this.llamadoSectores();
      this.llamadoDepartamentos();
      this.drawer = false;
    },

    cargarProspecto(empresa) {

      this.dialogProspectos = false;
      this.dialogCrearEditarProspecto = true;

      this.idProspectoSeleccionado = empresa.id;

      axios.post(this.baseURL + 'api/cargaproscon', {
        idprosp: empresa.id
      })
        .then(response => {
          console.log('Prospecto cargado:', response.data);
          this.nitComercial = response.data.data[0].p_nit;
          this.razonSocialComercial = response.data.data[0].p_razon_social;
          this.tipoIdComercial = this.tipoIdentificacion.find(item => item.id == response.data.data[0].p_tipo_identif);
          this.sectorComercial = this.sectorEmpresa.find(item => item.id == response.data.data[0].p_sector);
          this.direccionComercial = response.data.data[0].p_direccion;
          this.departamentoComercial = this.departamentos.find(item => item.id == response.data.data[0].p_dpto);
          setTimeout(() => {
            this.ciudadComercial = this.ciudades.find(item => item.id == response.data.data[0].p_ciudad);
          }, 1000);
          this.webComercial = response.data.data[0].p_web;
          this.correoEmpresaComercial = response.data.data[0].p_correo;
          this.tel1Comercial = response.data.data[0].p_telefono1;
          this.tel2Comercial = response.data.data[0].p_telefono2;

          this.nombreComercial2 = response.data.data[0].pc_nombre;
          this.apellidoComercial = response.data.data[0].pc_apellido;
          this.categoriaComercial = this.categorias.find(item => item.id == response.data.data[0].pc_categoria);
          setTimeout(() => {
            this.cargoComercial = this.cargos.find(item => item.id == response.data.data[0].pc_cargo);
          }, 1000);
          this.correoContactoComercial = response.data.data[0].pc_correo;
          this.celularComercial = response.data.data[0].pc_celular;
          this.extensionComercial = response.data.data[0].pc_extension;

        })
        .catch(error => {
          console.error('Error al cargar prospecto:', error);
        });

    },

    async actualizarProspecto() {
      this.mensajeAlertLogin = 'Actualizando prospecto...';
      this.alerta = true;
      this.ifCargando = true;

      console.log('este es el sector', this.sectorComercial);

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
        'comercial': this.comercialId,
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
          console.log('Prospecto actualizado:', response.data);

          setTimeout(() => {
            this.obtenerEmpresas();
            this.limpiarCamposProspecto();
            this.dialogCrearEditarProspecto = false;
            this.dialogProspectos = true;
            // Llama a actualizarInfoProspecto justo después de actualizar el contacto
            this.dialogProspectos = false;
            this.filtroRazonSocialEmpresasComercial = null;
            this.filtroNitEmpresasComercial = null;
            this.filtroFechaDesdeEmpresasComercial = null;
            this.filtroFechaHastaEmpresasComercial = null;
            this.ifCargando = false;
            this.alerta = false;
            this.mensajeAlertLogin = 'Prospecto actualizado correctamente';
            this.actualizarInfoProspecto(this.idProspectoSeleccionado);
          }, 700);
        })
        .catch(error => {
          console.log(error);
        });
    },

    filtrarEmpresas() {
      if (this.filtroRazonSocialEmpresasComercial && !this.filtroNitEmpresasComercial && !this.filtroFechaDesdeEmpresasComercial && !this.filtroFechaHastaEmpresasComercial) {
        this.listaEmpresasFiltradas = this.listaEmpresasComercial;
        const razonSocial = this.filtroRazonSocialEmpresasComercial.p_razon_social;

        this.listaEmpresasComercial = this.listaEmpresasComercial.filter(empresa => {
          return empresa.p_razon_social.toLowerCase().includes(razonSocial.toLowerCase());
        });
        return;
      } else {
        if (this.listaEmpresasFiltradas.length > 0) {
          this.listaEmpresasComercial = this.listaEmpresasFiltradas;
        }
      }

      if (!this.filtroRazonSocialEmpresasComercial && this.filtroNitEmpresasComercial && !this.filtroFechaDesdeEmpresasComercial && !this.filtroFechaHastaEmpresasComercial) {
        this.listaEmpresasFiltradas = this.listaEmpresasComercial;
        const nit = this.filtroNitEmpresasComercial.p_nit;

        this.listaEmpresasComercial = this.listaEmpresasComercial.filter(empresa => {
          return empresa.p_nit.toLowerCase().includes(nit.toLowerCase());
        });
        return;
      } else {
        if (this.listaEmpresasFiltradas.length > 0) {
          this.listaEmpresasComercial = this.listaEmpresasFiltradas;
        }
      }
    },

    filtrarEmpresas2() {

      if (!this.filtroRazonSocialEmpresasComercial && !this.filtroNitEmpresasComercial) {
        if (this.filtroFechaDesdeEmpresasComercial && this.filtroFechaHastaEmpresasComercial) {
          this.listaEmpresasFiltradas = this.listaEmpresasComercial;
          const fechaDesde = this.filtroFechaDesdeEmpresasComercial;
          const fechaHasta = this.filtroFechaHastaEmpresasComercial;

          if (fechaDesde > fechaHasta) {
            this.mensajeAlertLogin = 'La fecha de inicio no puede ser mayor que la fecha final';
            this.alerta = true;
            this.filtroFechaHastaEmpresasComercial = null;
            return;
          }

          this.listaEmpresasComercial = this.listaEmpresasComercial.filter(empresa => {
            //formatear empresa.p_fecha_sistema a fecha en formato YYYY-MM-DD
            const fechaSistema = new Date(empresa.p_fecha_sistema);
            const fechaDesdeObj = new Date(fechaDesde);
            const fechaHastaObj = new Date(fechaHasta);
            // Compara solo la fecha (sin hora)
            return fechaSistema.toISOString().split('T')[0] >= fechaDesdeObj.toISOString().split('T')[0] &&
              fechaSistema.toISOString().split('T')[0] <= fechaHastaObj.toISOString().split('T')[0];
          });
          return;
        } else {
          if (this.listaEmpresasFiltradas.length > 0) {
            this.listaEmpresasComercial = this.listaEmpresasFiltradas;
          }
        }
      }
    },

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

    filterNumber() {
      if (this.celular < 573) {
        this.celular = 573;
      }

      if (this.celular && this.celular.length > 12) {
        // Si tiene más de 10 dígitos, truncar el valor
        this.celular = this.celular.slice(0, 12);
      }
    },
    filterNumberComercial() {
      if (this.celularComercial < 573) {
        this.celularComercial = 573;
      }

      if (this.celularComercial && this.celularComercial.length > 12) {
        // Si tiene más de 10 dígitos, truncar el valor
        this.celularComercial = this.celularComercial.slice(0, 12);
      }
    },

    obtenerEmpresas() {
      axios.post(this.baseURL + 'api/cargarpp', {
        'idusu': this.comercialId,
      })
        .then(response => {
          // Solo empresas del usuario
          this.listaEmpresas = response.data.data;
          this.listaEmpresas2 = response.data.data;
          this.listaEmpresasComercial = response.data.data;
          this.listaEmpresasComercial2 = response.data.data;
        })
        .catch(error => {
          console.error('Error al cargar empresas:', error)
        })
    },
    validarNitEditarProspecto(nit) {
      // Busca el NIT original de la empresa que estás editando
      const empresaActual = this.listaEmpresasComercial.find(e => e.id === this.idProspectoSeleccionado);
      const nitOriginal = empresaActual ? empresaActual.p_nit : null;

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

    validarRazonSocialEditarProspecto(newRazonSocial) {
      // Busca la Razón Social original de la empresa que estás editando
      const empresaActual = this.listaEmpresasComercial.find(e => e.id === this.idProspectoSeleccionado);
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

    llamadoCategorias() {

      axios.get(this.baseURL + 'api/cargarcc')
        .then(response => {
          this.categorias = response.data.data;
        })
        .catch(error => {
          console.log(error);
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

    llamadoTipoEmpresa() {

      axios.get(this.baseURL + 'api/cargarte')
        .then(response => {
          this.tipoEmpresa = response.data.data;
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

    llamadoDepartamentos() {

      axios.get(this.baseURL + 'api/cargarde')
        .then(response => {
          this.departamentos = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    validarNitEditarProspecto(nit) {
      // Busca el NIT original de la empresa que estás editando
      const empresaActual = this.listaEmpresasComercial.find(e => e.id === this.idProspectoSeleccionado);
      const nitOriginal = empresaActual ? empresaActual.p_nit : null;

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

    validarRazonSocialEditarProspecto(newRazonSocial) {
      // Busca la Razón Social original de la empresa que estás editando
      const empresaActual = this.listaEmpresasComercial.find(e => e.id === this.idProspectoSeleccionado);
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


    llamadoDepartamentos() {

      axios.get(this.baseURL + 'api/cargarde')
        .then(response => {
          this.departamentos = response.data.data;
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

    llamadoSectores() {

      axios.get(this.baseURL + 'api/cargarse')
        .then(response => {
          this.sectorEmpresa = response.data.data;
        })
        .catch(error => {
          console.log(error);
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

    llamadoEmpresas() {

      axios.post(this.baseURL + 'api/cargarpp', {
        'idusu': localStorage.getItem('idUsuario'),
      })
        .then(response => {
          this.empresas = response.data.data;
          this.prospectos = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    llamadoServicios() {

      axios.get(this.baseURL + 'api/cargarsv')
        .then(response => {
          this.productos = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    _updateDsGuardar(val = true) {
      this.dsGuardar = val;
    },

    async actualizarInfoProspecto() {
      // Vuelve a cargar la información del prospecto y contacto, y la muestra en el diálogo de validación
      await axios.post(this.baseURL + 'api/cargaproscon', {
        idprosp: this.idprospecto
      })
        .then(async response => {
          const data = response.data.data[0];
          await this.cargarCiudadesAsync(data.p_dpto);
          await this.llamadoCargosAsync(data.pc_categoria);
          console.log("Data prospecto: ", data);

          const getNombre = (arr, id) => {
            if (!id) return '';
            const obj = arr.find(e => e.id == id);
            return obj ? (obj.nombre || obj.descripcion || obj.valor || obj.tipo || obj.categoria || obj.sector) : id;
          };

          const camposProspecto = [
            { nombre: 'NIT', valor: data.p_nit },
            { nombre: 'Razón Social', valor: data.p_razon_social },
            { nombre: 'Tipo Identificación', valor: getNombre(this.tipoIdentificacion, data.p_tipo_identif) },
            { nombre: 'Sector', valor: getNombre(this.sectorEmpresa, data.p_sector) },
            { nombre: 'Dirección', valor: data.p_direccion },
            { nombre: 'Departamento', valor: getNombre(this.departamentos, data.p_dpto) },
            { nombre: 'Ciudad', valor: getNombre(this.ciudades, data.p_ciudad) },
            { nombre: 'Teléfono 1', valor: data.p_telefono1 },
            { nombre: 'Teléfono 2', valor: data.p_telefono2 },
            { nombre: 'Correo Empresa', valor: data.p_correo }
          ];

          const camposContacto = [
            { nombre: 'Nombre', valor: data.pc_nombre },
            { nombre: 'Apellido', valor: data.pc_apellido },
            { nombre: 'Correo', valor: data.pc_correo },
            { nombre: 'Celular', valor: data.pc_celular },
            { nombre: 'Categoría', valor: getNombre(this.categorias, data.pc_categoria) },
            { nombre: 'Cargo', valor: getNombre(this.cargos, data.pc_cargo) }
          ];

          function isEmpty(val) {
            return val === null || val === undefined || (typeof val === 'string' && val.trim() === '');
          }

          let faltantesProspecto = [];
          let faltantesContacto = [];
          // Solo exigir uno de los teléfonos
          const telefono1Vacio = isEmpty(data.p_telefono1);
          const telefono2Vacio = isEmpty(data.p_telefono2);
          camposProspecto.forEach(campo => {
            if (campo.nombre === 'Teléfono 1' || campo.nombre === 'Teléfono 2') return;
            if (isEmpty(campo.valor)) faltantesProspecto.push(campo.nombre);
          });
          if (telefono1Vacio && telefono2Vacio) {
            faltantesProspecto.push('Teléfono');
          }
          camposContacto.forEach(campo => {
            if (isEmpty(campo.valor)) faltantesContacto.push(campo.nombre);
          });

          // Guarda la info para mostrar en el diálogo
          this.infoProspectoDialog = camposProspecto.map(campo => ({
            ...campo,
            faltante: isEmpty(campo.valor)
          }));
          this.infoContactoDialog = camposContacto.map(campo => ({
            ...campo,
            faltante: isEmpty(campo.valor)
          }));

          this.mensajeValidacionCotizacion =
            (faltantesProspecto.length > 0 ? 'Faltan datos de la empresa: ' + faltantesProspecto.join(', ') + '.\n' + '.\n' : '') +
            (faltantesContacto.length > 0 ? 'Faltan datos del contacto: ' + faltantesContacto.join(', ') + '.' : '');

          if (faltantesProspecto.length > 0 || faltantesContacto.length > 0) {
            this.dialogValidarCotizacion = true;
            this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 2); // Regresa a "En Proceso"
          }
          // Si no hay faltantes, no muestra el diálogo y permite continuar
          this.ifProximoSeguimientoActividad = true;
        })
        .catch(error => {
          this.dialogValidarCotizacion = true;
          this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 2);
        });

      // Forzar actualización visual del diálogo
      if (this.dialogValidarCotizacion) {
        this.dialogValidarCotizacion = false;
        this.$nextTick(() => {
          this.dialogValidarCotizacion = true;
        });
      }
    },

    filterTel1Comercial() {
      if (this.tel1Comercial < 57) {
        this.tel1Comercial = 57;
      }
      if (this.tel1Comercial && this.tel1Comercial.length > 12) {
        // Si tiene más de 10 dígitos, truncar el valor
        this.tel1Comercial = this.tel1Comercial.slice(0, 12);
      }
    },

    getFileName(url) {
      if (!url) return 'Sin archivo';
      try {
        // Extrae la parte antes del '?'
        const base = url.split('?')[0];
        // Extrae el nombre del archivo después del último '/'
        let filename = base.substring(base.lastIndexOf('/') + 1);
        // Decodifica caracteres especiales (por ejemplo, %3D, %20, etc.)
        filename = decodeURIComponent(filename);
        if (!filename || filename === '/' || filename.match(/^\s*$/)) return 'Sin archivo';
        return filename;
      } catch (e) {
        return 'Archivo';
      }
    },

    getNombreServicio(idservicio) {
      const servicio = this.selectServiciosActividad.find(s => s.id == idservicio);
      return servicio ? servicio.nombre : 'Servicio no asignado';
    },

    limpiarCamposHistorial() {
      this.filtroEstadoId = null;
      this.busquedaHistorial = '';
      this.busquedaFecha = '';
      this.ordenLista = true;
    },

    abrirHistorialEdiciones(gestion) {
      axios.post(this.baseURL + 'api/historialEdiciones', {
        'id_historial': gestion.id
      })
        .then(response => {
          this.historialEdiciones = response.data.data;
          this.dialogHistorialEdiciones = true;
        })
        .catch(error => {
          console.log(error);
          this.mensajeAlert = 'Error al cargar el historial de ediciones';
          this.alerta = true;
          this.ifCargando = false;
        });
    },

    timelineColor(interes) {
      if (interes === 0) return 'timeline-green';
      if (interes === 1) return 'timeline-blue';
      if (interes === 2) return 'timeline-red';
      return 'timeline-neutral';
    },
    timelineIcon(interes) {
      if (interes === 0) return 'mdi-check-circle';
      if (interes === 1) return 'mdi-phone';
      if (interes === 2) return 'mdi-close-circle';
      return 'mdi-help-circle';
    },
    timelineIconColor(interes) {
      if (interes === 0) return 'green';
      if (interes === 1) return 'blue';
      if (interes === 2) return 'red';
      return 'grey';
    },

    interesToText(interes) {
      if (interes === 0) return 'Llamada Efectiva con Lead';
      if (interes === 1) return 'Llamada Efectiva sin Lead';
      if (interes === 2) return 'Llamada No Efectiva';
      return '';
    },

    // .
  }
};


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

.titulo-error {
  color: red !important;
}


.custom-scroll::-webkit-scrollbar {
  width: 6px;
}

.custom-scroll::-webkit-scrollbar-track {
  background: transparent;
}

.custom-scroll::-webkit-scrollbar-thumb {
  background-color: #999;
  border-radius: 4px;
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

.empresa-card {
  transition: transform 0.2s;
  cursor: pointer;
  border-radius: 10px;
  overflow: hidden;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.empresa-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.empresa-title {
  font-size: 1.1rem;
  color: #0A1C3A;
  white-space: normal;
  word-break: break-word;
}

.empresa-nit {
  color: #1976D2;
  font-weight: 500;
}

.empresa-label {
  color: #666;
  font-size: 0.9rem;
}

.empresa-value {
  color: #222;
  font-weight: 500;
  display: flex;
  align-items: center;
}

.contact-card-text {
  margin-left: 4px;
  margin-right: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.timeline-container {
  position: relative;
  margin-left: 20px;
  margin-right: 10px;
}

.timeline-item {
  display: flex;
  align-items: flex-start;
  position: relative;
  margin-bottom: 32px;
  background: #fff;
  border: 1.5px solid #000000;
  border-radius: 12px;
  box-shadow: 0 2px 8px 0 #006ca11a;
  transition: box-shadow 0.2s, border 0.2s;

}

.timeline-marker {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 16px;
  flex-shrink: 0;
  border: 2px solid #bdbdbd;
  margin-top: 10px;
  margin-left: 10px;

}

.timeline-green {
  border-color: #43a047;
  background: #d2f8e5;
}

.timeline-blue {
  border-color: #1976d2;
  background: #d2e6fa;
}

.timeline-red {
  border-color: #e53935;
  background: #f8d2d2;
}

.timeline-neutral {
  border-color: #bdbdbd;
  background: #f5f5f5;
}

.timeline-1565C0 {
  border-color: #1565c0;
  background: #d2e6fa;
}

.timeline-2095c9 {
  border-color: #2095c9;
  background: #d2e6fa;
}

.timeline-orange-darken-2 {
  border-color: #f57c00;
  background: #fff3e0;
}

.timeline-teal-darken-1 {
  border-color: #00897b;
  background: #e0f2f1;
}

.timeline-8E24AA {
  border-color: #8e24aa;
  background: #f3e5f5;
}

.timeline-brown-darken-3 {
  border-color: #5d4037;
  background: #efebe9;
}

.timeline-content {
  flex: 1;
  min-width: 0;
}

.timeline-date {
  font-size: 13px;
  font-weight: bold;
  color: #006CA1;
}

.timeline-type {
  font-size: 12px;
  font-weight: 500;
  margin-left: 8px;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 10px 10px;
}

.timeline-text {
  font-size: 12px;
  margin-top: 4px;
}

.timeline-connector {
  position: absolute;
  left: 25px;
  top: 45px;
  width: 2px;
  height: calc(100% - 60px + 10px);
  background: #bdbdbd;
  z-index: 0;
}

@media (max-width: 600px) {
  .timeline-container {
    margin-left: 8px;
  }

  .timeline-marker {
    width: 24px;
    height: 24px;
    margin-right: 8px;
  }

  .timeline-content {
    font-size: 11px;
  }
}
</style>
