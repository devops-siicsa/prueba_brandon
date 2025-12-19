<template>
  <v-app>
    <!-- Cambios Angelo -->
    <v-navigation-drawer v-model="drawer" color="#006CA1" dark fixed app>
      <v-list>

        <v-list-item @click="irConfiguracion()" link v-if="idCargo == '1'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-cog" color="white" prepend-icon></v-icon>
              Configuración
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irComercial()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-account-tie" color="white" prepend-icon></v-icon>
              Comercial
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irContactos()" link v-if="false">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-contacts" color="white" prepend-icon></v-icon>
              Contactos Mercadeo
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irPendientesGeneral()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-format-list-checks" color="white" prepend-icon></v-icon>
              Pendientes
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-group value="Campañas" v-if="idCargo == '2'">
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" prepend-icon="mdi mdi-bullhorn" title="Campañas" active></v-list-item>
          </template>

          <v-list-item @click="irGaleriaCampanas()" link :class="{ 'menu-item-activo': menuActivo === '/vercampanas' }">

            <v-list-item-content class="list-item-compact">

              <v-list-item-title style="color: white; font-size: 0.93rem;">
                <v-icon class="mr-2" size="small" icon="mdi mdi-image-multiple" color="white" prepend-icon></v-icon>
                Galería
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irInformesCampañas()" link
            :class="{ 'menu-item-activo': menuActivo === '/informes-campanas' }">

            <v-list-item-content>

              <v-list-item-title style="color: white; font-size: 0.93rem;">
                <v-icon class="mr-2" size="small" icon="mdi-chart-bar" color="white" prepend-icon></v-icon>
                Métricas
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irProspeccionTelefonica()" link
            :class="{ 'menu-item-activo': menuActivo === '/prospeccion-telefonica' }">

            <v-list-item-content>

              <v-list-item-title style="color: white; white-space: pre-wrap; font-size: 0.93rem;">
                <v-icon class="mr-2" size="small" icon="mdi-phone-log" color="white" prepend-icon></v-icon>
                Prospección Telefónica
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="" link>

            <v-list-item-content>

              <v-list-item-title style="color: white; white-space: pre-wrap; font-size: 0.93rem;">
                <v-icon class="mr-2" size="small" icon="mdi-email-newsletter" color="white" prepend-icon></v-icon>
                Email Marketing
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irCampañas()" link>

            <v-list-item-content>

              <v-list-item-title style="color: white; white-space: pre-wrap; font-size: 0.93rem;"
                :class="{ 'menu-item-activo': menuActivo === '/campana' }">
                <v-icon class="mr-2" size="small" icon="mdi-whatsapp" color="white" prepend-icon></v-icon>
                WhatsApp Business
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

        </v-list-group>

        <v-list-group value="Clientes" v-if="idCargo == '2'">
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" prepend-icon="mdi-account-group" title="Clientes" active></v-list-item>
          </template>

          <v-list-item @click="irEmpresas()" :class="{ 'menu-item-activo': menuActivo === '/contactos' }" link
            v-if="idCargo == '2'">

            <v-list-item-content>

              <v-list-item-title style="color: white;; font-size: 0.93rem; ">
                <v-icon class="mr-2" size="small" icon="mdi-office-building" color="white" prepend-icon></v-icon>
                Empresas
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

        </v-list-group>

        <v-list-group value="Chat" v-if="idCargo == '2'">
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" prepend-icon="mdi-chat-processing" title="Chat" active></v-list-item>
          </template>

          <v-list-item @click="irContactos()" :class="{ 'menu-item-activo': menuActivo === '/contactos' }" link
            v-if="idCargo == '2'">

            <v-list-item-content>

              <v-list-item-title style="color: white; font-size: 0.93rem;">
                <v-icon class="mr-2" size="small" icon="mdi-contacts" color="white" prepend-icon></v-icon>
                Contactos
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

        </v-list-group>

        <v-list-item @click="irPQR()" link v-if="idCargo == '5'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-information-variant-circle" color="white" prepend-icon></v-icon>
              PQR
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irPedidos()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-package" color="white" prepend-icon></v-icon>
              Pedidos
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="abrirDialogProspectos()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-office-building-cog" color="white" prepend-icon></v-icon>
              Prospecto
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <AppHeader :nombre-comercial="nombreComercial" :imagen-comercial="imagenComercial" :correo-usuario="correoUsuario"
      :comercial-id="comercialId" :base-u-r-l="baseURL" v-model:drawer="drawer" @imagen-actualizada="actualizarImagen"
      @cerrar-sesion="cerrarSesion" />

    <!-- Cambios Angelo -->
      <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
        
        <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
        <!--DESDE AQUI VISTA CAMPAÑA-->
        <!-- Destinatarios -->
        <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
          <v-row align="center" no-gutters>
            <div v-if="!reenviarUnaCampaña">
              <v-col class="d-flex align-center" style="flex: none; width: auto;">
                <v-icon class="mr-2">mdi mdi-calendar-multiple</v-icon>
                Crear y enviar Campaña
              </v-col>
            </div>
            <div v-if="reenviarUnaCampaña">
              <v-col class="d-flex align-center" style="flex: none; width: auto;">
                <v-icon class="mr-2">mdi-reply</v-icon>
                Reenviar una Campaña
              </v-col>
            </div>
            <v-spacer />
            <v-col class="d-flex justify-end" style="flex: none; width: auto;">
              <v-btn color="#039BE5" variant="flat" size="large" rounded="lg" class="text-none px-5 btn-grow-card ml-6"
                prepend-icon="mdi mdi-view-gallery-outline" @click="irGaleriaCampanas()">
                Ver la Galería de Campañas
              </v-btn>
            </v-col>
          </v-row>
        </v-card-title>
        <v-card class="pa-6 mb-6" elevation="4">
          <v-row dense>
            <v-col cols="12" md="7">
              <v-card-title class="text-h5 font-weight-bold"> <v-icon size="25"
                  :color="tipoEnvio.length > 0 ? '#138f40' : '#000000'">mdi mdi-send-variant</v-icon> Seleccionar Tipo
                de
                Envío:</v-card-title>
              <v-combobox v-model="tipoEnvio" :items="opcionesTipoEnvio" label="Seleccionar tipos de envio" multiple
                chips outlined clearable dense prepend-inner-icon="mdi-filter" class="ml-4" />

              <span
                v-if="!tipoEnvio.includes('Por filtros de prospectos') || !tipoEnvio.includes('Registrar números manualmente')"
                class="ml-4" style="font-size:14px; color:#6e6d6d;">Selecciona la modalidad de envío de Campañas, por
                medio
                de filtros o digitando manualmente los contactos </span>

            </v-col>
            <v-col cols="7" v-if="tipoEnvio.length">

              <v-card-text>
                <div v-if="tipoEnvio.includes('Por filtros de prospectos')">
                  <v-card-title class="text-h5 font-weight-bold"> <v-icon size="25" class="mr-2"
                      :color="Object.values(filtrosBD).some(v => v) ? '#138f40' : '#000000'">mdi
                      mdi-filter-multiple</v-icon>Filtro de Destinatarios: </v-card-title>
                  <v-row dense class="mb-2">
                    <v-col cols="12">
                      <v-tooltip text="Añadir filtros de Prospectos a los cuales les enviaras la campaña"
                        location="top">
                        <template v-slot:activator="{ props }">
                          <v-combobox v-bind="props" v-model="filtros" :items="opcionesFiltros" label="Agregar filtros"
                            prepend-inner-icon="mdi mdi-filter" multiple chips clearable small-chips outlined dense
                            @update:modelValue="actualizarFiltros" @click:clear="limpiarFiltros" />
                        </template>
                      </v-tooltip>
                    </v-col>


                    <v-row dense>
                      <v-col v-for="filtroSeleccionado in filtros" :key="filtroSeleccionado" cols="12" md="6">
                        <v-autocomplete v-if="getFiltroDefByNombre(filtroSeleccionado)"
                          :label="getFiltroDefByNombre(filtroSeleccionado).nombre"
                          :items="obtenerItemsPorFiltro(getFiltroDefByNombre(filtroSeleccionado).id)"
                          v-model="filtrosEnvio[getFiltroDefByNombre(filtroSeleccionado).id]" item-title="nombre"
                          item-value="id" clearable dense outlined
                          :name="'filtro-' + getFiltroDefByNombre(filtroSeleccionado).id"
                          @update:modelValue="filtrosEnvio" />
                      </v-col>
                    </v-row>

                  </v-row>
                  <span class="ml-2" style="font-size:14px; color:#888;">Selecciona los filtros a los cuales se les
                    envíara
                    la campaña (Si no seleccionas ninguno se enviaran a todos los disponibles)</span>
                  <v-divider class="my-4" />
                </div>
                <div v-if="tipoEnvio.includes('Registrar números manualmente')">
                  <v-card-title class="text-h7 font-weight-bold d-flex align-center justify-space-between">
                    <div class="d-flex align-center" style="flex: 1;">
                      <v-icon size="28" :color="numerosManualValidos.length > 0 ? '#138f40' : '#0D47A1'" class="mr-2"
                        style="background: #e3f2fd; border-radius: 50%; padding: 4px;">
                        mdi-pencil
                      </v-icon>
                      <span class="font-weight-bold" style="color: #0A1C3A; font-size: 1.1rem;">Registrar Números
                        Manualmente</span>
                    </div>
                    <!-- Botones movidos al slot append-inner del textarea -->
                  </v-card-title>
                  <v-card-subtitle class="ml-2 mb-2" style="font-size:14px; color:#888;">
                    Puedes subir un archivo .txt o excel con los números de WhatsApp, recuerda mantener el formato
                  </v-card-subtitle>
                  <div>

                    <v-card-text class="pb-0">
                      <div
                        style="background: #e5e7eb; border-radius: 10px; border: 1.5px solid #b0b8c1; padding: 0.5rem 0.75rem 0.5rem 0.75rem;">
                        <div class="d-flex" style="align-items: flex-start;">
                          <div style="flex:1;">
                            <v-textarea v-model="numerosManual"
                              label="Números de WhatsApp (Con extención 57 y separados por coma)" rows="3" auto-grow
                              outlined clearable :rules="[validarNumerosManual]"
                              placeholder="Ejemplo: 573001234567, 573002345678" prepend-inner-icon="mdi-whatsapp"
                              @click:clear="numerosInvalidosArray = []"
                              style="background: transparent; border: none; min-height: 70px; margin-bottom: 0;" />
                          </div>
                          <div class="d-flex flex-column align-start"
                            style="gap: 8px; margin-left: 8px; margin-top: 4px;">
                            <v-tooltip location="top">
                              <template v-slot:activator="{ props }">
                                <v-btn v-bind="props" size="medium" color="#0D47A1" icon rounded
                                  style="box-shadow:none; margin-bottom:2px;" @click="dialogInforArchivoNumeros = true">
                                  <v-icon size="22" color="white">mdi-help-circle</v-icon>
                                </v-btn>
                              </template>
                              <span>Acerca del formato del archivo</span>
                            </v-tooltip>
                            <v-tooltip location="top">
                              <template v-slot:activator="{ props }">
                                <v-btn v-bind="props" size="medium" color="#138f40" icon rounded
                                  style="box-shadow:none;" @click="subirArchivoNumerosManual">
                                  <v-icon size="22" color="white">mdi-upload</v-icon>
                                </v-btn>
                              </template>
                              <span>Subir archivo con números de WhatsApp</span>
                            </v-tooltip>
                          </div>
                        </div>
                      </div>
                      <div class="text-caption mt-1"
                        :style="{ color: numerosManualValidos.length ? '#006CA1' : '#d32f2f' }">
                        {{ numerosManualValidos.length }} número{{ numerosManualValidos.length === 1 ? '' : 's' }}
                        válido{{ numerosManualValidos.length === 1 ? '' : 's' }} ingresado{{ numerosManualValidos.length
                        ===
                        1 ? '' : 's' }}.
                        <span v-if="numerosManualInvalidos.length">({{ numerosManualInvalidos.length }} inválido{{
                          numerosManualInvalidos.length === 1 ? '' : 's' }})</span>
                      </div>
                      <v-alert v-if="numerosInvalidosArray && numerosInvalidosArray.length" type="error" variant="flat"
                        class="mt-2 invalidos-alert" dense>
                        <div class="invalidos-alert-title">
                          Los siguientes números son inválidos:
                        </div>
                        <span class="invalidos-alert-content">
                          {{ numerosInvalidosArray.join(', ') }}
                        </span>
                      </v-alert>
                    </v-card-text>

                  </div>
                </div>



                <v-card v-if="!tipoEnvio.length == 0" class="pa-3 mb-2" elevation="0" style="background: #f8fafc;">
                  <div class="font-weight-bold mb-2" style="font-size: 1.1rem; color: #0A1C3A;">
                    Resumen de envíos
                  </div>
                  <v-table dense class="mb-0" style="background: transparent;">
                    <tbody>
                      <tr v-if="tipoEnvio.includes('Por filtros de prospectos')">
                        <td>
                          <v-card-subtitle class="text-h7 font-weight-bold">
                            <v-icon color="primary" size="18" class="mr-1">mdi-filter</v-icon>
                            Por filtros
                          </v-card-subtitle>
                        </td>
                        <td class="font-weight-bold" style="color: #1976d2;">{{ totalRegistrosBd }}</td>
                      </tr>
                      <tr v-if="tipoEnvio.includes('Registrar números manualmente')">
                        <td>
                          <v-card-subtitle class="text-h7 font-weight-bold">
                            <v-icon color="success" size="18" class="mr-1">mdi-pencil</v-icon>
                            Por destinatarios añadidos
                          </v-card-subtitle>
                        </td>
                        <td class="font-weight-bold" style="color: #029e3b;">{{ numerosManualValidos.length }}</td>
                      </tr>
                      <tr>
                        <td class="font-weight-bold" style="font-size: 1rem;">Total a enviar</td>
                        <td class="font-weight-bold" style="font-size: 1rem; color: #006CA1;">
                          {{ resumenTotalEnvio }}
                        </td>
                      </tr>
                    </tbody>
                  </v-table>
                </v-card>


              </v-card-text>

              <!-- Detalles de Envio de Campaña -->

              <div
                v-if="reenviarUnaCampaña && (tipoEnvio.includes('Por filtros de prospectos') || tipoEnvio.includes('Registrar números manualmente'))">
                <v-divider class="my-4" />
                <v-card-title class="text-h5 font-weight-bold"><v-icon size="25" class="mr-2"
                    :color="selectedImagenCampana != null && campnom && campdet || reenviarUnaCampaña ? '#138f40' : '#000000'">mdi
                    mdi-send-variant</v-icon>Detalles de reenvio de Campaña</v-card-title>
                <v-card-text>
                  <!-- Detalles de envío -->
                  <v-row dense>
                    <v-col cols="12" md="6">
                      <v-tooltip text="Plantilla sobre la cual se construira el modelo de la campaña " location="top">
                        <template v-slot:activator="{ props }">
                          <v-autocomplete readonly=true v-model="selectedTemplate" v-bind="props" :items="templates"
                            return-object label="Plantilla de la Campaña" prepend-icon="mdi-play-box-multiple"
                            item-title="name" item-value="name" variant="outlined" outlined dense />
                        </template>
                      </v-tooltip>
                    </v-col>
                    <v-col cols="12" md="6">
                      <v-autocomplete readonly=true v-model="campnom" :disabled="!selectedTemplate"
                        :items="publicidadFiltrada" label="Nombre de la Campaña" outlined return-object
                        item-title="nombre" item-value="id" variant="outlined"></v-autocomplete>
                    </v-col>
                    <v-col cols="12">

                      <v-textarea readonly=true v-model="campdet" v-bind="props" label="Detalle de la campaña" outlined
                        rows="2" auto-grow dense />

                    </v-col>

                  </v-row>
                </v-card-text>
              </div>
              <v-divider class="my-4" />
              <div
                v-if="!reenviarUnaCampaña && (tipoEnvio.includes('Por filtros de prospectos') || tipoEnvio.includes('Registrar números manualmente'))">
                <v-card-title class="text-h5 font-weight-bold"> <v-icon size="25" class="mr-2"
                    :color="selectedImagenCampana != null && selectedNombreCampana && selectedDetalleCampana ? '#138f40' : '#000000'">mdi
                    mdi-bullhorn</v-icon>Crear Nueva Campaña</v-card-title>
                <!--SECCIÓN DE CREAR CAMPAÑA-->
                <v-card-text>
                  <v-form ref="formNuevaCampaña" v-model="formOk">
                    <v-row dense>
                      <v-col cols="12" md="12">
                        <v-text-field v-model.trim="selectedNombreCampana" label="Nombre de la campaña"
                          prepend-inner-icon="mdi-bell" variant="outlined" density="comfortable" clearable
                          :error="validandoActividad && !selectedNombreCampana"
                          :error-messages="validandoActividad && !selectedNombreCampana ? 'Este campo es obligatorio' : ''"
                          class="mb-1" />
                        <div v-if="nombreCampaniaDuplicado"
                          style="color: #d32f2f; font-size: 14px; margin-bottom: 8px;">
                          Ya existe una campaña con ese nombre. Por favor, elige otro.
                        </div>
                        <v-textarea v-model.trim="selectedDetalleCampana" label="Digita el Prompt para el BOT"
                          prepend-inner-icon="mdi mdi-console" variant="outlined" density="comfortable"
                          auto-grow rows="2" persistent-hint :error="validandoActividad && !selectedDetalleCampana"
                          :error-messages="validandoActividad && !selectedDetalleCampana ? 'Este campo es obligatorio' : ''"
                          class="mb-1" />
                        <v-row dense>
                          <v-col cols="12" md="6">
                            <v-autocomplete v-model="selectedAreaVentas" :items="areasVentas"
                              label="Asignar Departamento" outlined return-object item-title="nombre" item-value="id"
                              variant="outlined" dense prepend-inner-icon="mdi mdi-timeline-plus-outline" />
                          </v-col>
                          <v-col cols="12" md="6">
                            <v-combobox v-model="selectedComerciales" :items="comerciales" label="Seleccionar Agente(s)" multiple
                              item-title="nombre" item-value="id"
                              prepend-inner-icon="mdi mdi-badge-account-horizontal-outline" class="ml-4" return-object />
                          </v-col>
                        </v-row>
                        <v-tooltip text="Plantilla sobre la cual se construira el modelo de la campaña " location="top">
                          <template v-slot:activator="{ props }">
                            <v-autocomplete v-model="selectedTemplate" v-bind="props" :items="templates" return-object
                              label="Seleccionar una Plantilla" prepend-icon="mdi-play-box-multiple" item-title="name"
                              item-value="name" variant="outlined" outlined dense />
                          </template>
                        </v-tooltip>
                        <div v-if="selectedTemplate">
                          <v-file-input v-model="selectedImagenCampana" label="Añadir la media de la campaña"
                            :accept="acceptCampanaFile" variant="outlined" density="comfortable" show-size clearable
                            :error="validandoActividad && !selectedImagenCampana"
                            :error-messages="validandoActividad && !selectedImagenCampana ? 'Selecciona una imagen o video' : ''"
                            class="mb-2" @change="onImagenCampanaChange" />
                          <div class="text-caption mt-1" style="color:#888;">
                            Máx. 14MB.
                            <span
                              v-if="selectedTemplate && (selectedTemplate.name === 'boletin_informativo' || selectedTemplate.name === 'promocionar_productos_servicios')">
                              Solo JPG, PNG, JPEG
                            </span>
                            <span v-else-if="selectedTemplate && selectedTemplate.name === 'video_informativo_mp4'">
                              Solo MP4
                            </span>
                            <span v-else>
                              Solo JPG, PNG, JPEG, MP4
                            </span>
                          </div>


                        </div>
                      </v-col>
                    </v-row>
                  </v-form>
                </v-card-text>
              </div>

              <v-divider class="my-4" />
              <div v-if="false">
                <v-card-title class="text-h7 font-weight-bold">Añadir Encabezado</v-card-title>
                <template v-if="template">
                  <div v-if="template.header" class="my-5">
                    <h5 class="text-h5">Encabezado</h5>
                    <v-text-field v-if="template.headercontents.length != 0" v-model="header_text" outlined class="mt-2"
                      :label="`${template.headercontents[0].text}`" variant="outlined"></v-text-field>
                    <p v-else-if="template.header.format == 'TEXT'">
                      {{ template.header.text }}
                    </p>

                    <!-- File Inputs para carga de imagen, video y documento -->
                    <v-file-input v-else-if="template.header.format == 'IMAGE'" v-model="header_img" outlined
                      class="mt-2" :label="`${template.header.format} URL`" variant="outlined" accept="image/*"
                      @change="handleFileUpload('IMAGE')" @input="clearInput('IMAGE')"></v-file-input>
                    <v-file-input v-else-if="template.header.format == 'DOCUMENT'" v-model="header_doc" outlined
                      class="mt-2" :label="`${template.header.format} URL`" variant="outlined"
                      accept=".pdf,.doc,.docx,.xls,.xlsx,.txt" @change="handleFileUpload('DOCUMENT')"
                      @input="clearInput('DOCUMENT')"></v-file-input>
                    <v-file-input v-else-if="template.header.format == 'VIDEO'" v-model="header_vid" outlined
                      class="mt-2" :label="`${template.header.format} URL`" variant="outlined" accept="video/mp4"
                      @change="handleFileUpload('VIDEO')" @input="clearInput('VIDEO')"></v-file-input>
                  </div>
                </template>
              </div>
            </v-col>
            <v-col cols="12" md="5" class="d-flex justify-center align-center"
              v-if="tipoEnvio.includes('Por filtros de prospectos') || tipoEnvio.includes('Registrar números manualmente')">
              <!-- Vista previa de la Campaña-->
              <div class="d-flex flex-column align-center justify-center mt-n4">
                <v-card-title class="text-h5 font-weight-bold ">Vista previa de la Campaña</v-card-title>

                <!-- Vista previa tipo WhatsApp -->
                <!-- Simulación de celular con la imagen PhoneScreen.png como fondo -->
                <div class="celular-container ">
                  <img src="/PhoneScreen.png" alt="Mockup" class="celular-mockup" />
                  <div style="background-color: #efeae2">
                    <div class="contenido-preview rounded-xl overflow-hidden d-flex flex-column justify-space-between"
                      style="background-color: ">
                      <div style="background-color: #fff; overflow-y: auto;">
                        <!-- Cabecera estilo WhatsApp -->
                        <div class="cabecera-chat px-2 py-3 d-flex align-center rounded-t-xl"
                          style="background-color: #075e54; color: white;">
                          <v-avatar size="28" class="mr-2">
                            <v-icon style="color: white;">mdi-whatsapp</v-icon>
                          </v-avatar>
                          <div class="font-weight-medium">SIICSA SAS</div>
                          <v-spacer />
                          <v-icon size="18">mdi-check-decagram</v-icon>
                        </div>

                        <!-- Fondo de mensaje: ocupa el área interna del mockup -->
                        <div style="
                              position: absolute;
                              top: 65px; /* Ajusta según el header del mockup */
                              left: 9px;
                              right: 33px;
                              bottom: 38px; /* Ajusta según el borde inferior del mockup */
                              background-color: #e5ddd5;
                              border-radius: 0 0 18px 18px;
                              width: calc(100% - 17px);
                              height: calc(100% - 65px);
                              display: flex;
                              flex-direction: column;
                              justify-content: flex-start;
                              align-items: flex-start;
                              overflow-y: auto;
                              z-index: 2;
                            ">

                          <!-- Mensaje estilo burbuja, pegado arriba y flexible -->
                          <v-card class="pa-3 chat-bubble-client" elevation="1" style="
                                align-self: flex-start;
                                width: 95%;
                                max-width: 96%;
                                border-radius: 16px;
                                margin-left: 5px;
                                margin-right: 0;
                                margin-bottom: 16px;
                                min-height: 120px;
                                box-sizing: border-box;
                                margin-top: 0;
                              ">

                            <div class="text-caption text-grey mb-2">Hoy</div>
                            <!-- Imagen predeterminada -->
                            <div style="z-index: 20000;">
                              <!-- Si hay campaña seleccionada y tiene url_media -->
                              <template v-if="campnom && campnom.url_media">
                                <!-- Si es imagen -->
                                <v-img v-if="/\.(jpg|jpeg|png|webp|gif)(\?|$)/i.test(campnom.url_media.split('?')[0])"
                                  :src="campnom.url_media" class="media-preview"
                                  @click="abrirImagenAmpliada(campnom.url_media)" />
                                <!-- Si es video -->
                                <video
                                  v-else-if="/\.(mp4|webm|ogg|mov|avi|mkv)(\?|$)/i.test(campnom.url_media.split('?')[0])"
                                  :src="campnom.url_media" controls class="media-preview"
                                  style="background:#000;"></video>
                                <!-- Si es otro tipo de archivo (documento) -->
                                <div v-else>
                                  <a :href="campnom.url_media" target="_blank">Ver Archivo</a>
                                </div>
                              </template>
                              <!-- Si NO hay campaña seleccionada, muestra preview del archivo subido -->
                              <template v-else-if="selectedImagenCampana">
                                <!-- Si es imagen -->
                                <v-img
                                  v-if="selectedImagenCampana.type && selectedImagenCampana.type.startsWith('image/')"
                                  :src="previewImagenCampana" class="media-preview"
                                  @click="abrirImagenAmpliada(previewImagenCampana)" />
                                <!-- Si es video -->
                                <video
                                  v-else-if="selectedImagenCampana.type && selectedImagenCampana.type.startsWith('video/')"
                                  :src="previewVideoCampana" controls class="media-preview"
                                  style="background:#000;"></video>
                              </template>
                              <!-- Si no hay nada, muestra imagen predeterminada -->
                              <template v-else>
                                <v-img :src="'https://glpi-siicsa.azurewebsites.net/SIICSA.jpg'" class="media-preview"
                                  @click="abrirImagenEnNuevaPestana('https://glpi-siicsa.azurewebsites.net/SIICSA.jpg')" />
                              </template>
                            </div>

                            <p class="pre-wrap text-body-2 mb-3 mt-2">
                              {{ template ? template.body : 'Esta es una preview de como se mostrara la campaña' }}
                            </p>

                            <div class="text-body-2 mb-3" v-if="template">
                              <v-text-field v-for="(placeholder, index) in template.body_placeholders" :key="index"
                                v-model="body_placeholders[index]" outlined :label="placeholder.text"
                                variant="outlined"></v-text-field>
                            </div>

                            <div class="text-caption text-grey mb-2">Siicsa Sas. Derechos reservados</div>

                            <div class="d-flex flex-column mt-2" v-if="template && template.buttons">
                              <v-btn v-for="(button, index) in template.buttons" :key="index" color="blue lighten-4"
                                variant="outlined" class="mb-2 text-capitalize" style="text-align: left;">
                                {{ button.text }}
                              </v-btn>
                            </div>

                            <div class="text-caption text-grey text-right mt-2">11:30 AM</div>
                          </v-card>
                        </div>
                      </div>

                    </div>
                  </div>
                </div>

              </div>
            </v-col>
            <div class="mt-0" v-if="template">
              <v-btn v-if="template.status == 'APPROVED'" color="teal darken-1" dark :loading="sending"
                @click="abrirConfirmacionEnvio">Enviar a todos los destinatarios</v-btn>

              <v-alert v-if="template.status !== 'APPROVED'" type="error">Template unapproved and can't be used to send
                messages.</v-alert>
            </div>
          </v-row>
          <v-row v-if="!tipoEnvio.length" class="mb-8">
            <v-col cols="12" md="7">
              <v-card elevation="0" class="pa-6" style="background: #f8fafc;">
                <v-row>
                  <v-col cols="12">
                    <div class="text-h5 font-weight-bold mb-2" style="color:#0A1C3A;">
                      <v-icon color="#006CA1" size="40" class="mb-2">mdi-bullhorn</v-icon> ¡Bienvenido al módulo de
                      campañas!
                    </div>
                    <div class="text-body-1 mb-3" style="color:#444;">
                      Aquí puedes crear y enviar campañas de WhatsApp a tus prospectos.
                    </div>
                    <v-divider class="mb-3" />
                    <ul class="mb-2" style="color:#666; ">
                      <li style="font-size:1.08rem; text-align: justify;">Selecciona el <b>tipo de envío</b> para
                        comenzar:
                        por filtros de prospectos o números manuales.</li>
                      <li style="font-size:0.9rem; text-align: justify;" class=" ml-4">Ten en cuenta que los números
                        manuales deben estar con la extensión 57 y separados por comas Ej: [571234567890, 570987654321]
                      </li>
                      <li style="font-size:1.08rem; text-align: justify;">Usa los <b>filtros de destinatarios</b> para
                        segmentar tus prospectos.</li>
                      <li style="font-size:1.08rem; text-align: justify;">Adjunta imágenes o videos y visualiza una
                        <b>preview</b> de cómo se verá tu campaña en WhatsApp.
                      </li>
                    </ul>
                    <v-alert type="info" border="start" color="#006CA1" class="mt-4" style="background: #006CA1;">
                      <v-icon left color="#006CA1">mdi-information-outline</v-icon>
                      <span>
                        <b>Selecciona una modalidad de envío</b> para comenzar.
                      </span>
                    </v-alert>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>
            <v-col cols="12" md="5" class="d-flex flex-column align-center justify-center">
              <v-card elevation="0" class="pa-4" style="background: #f8fafc;">
                <div class="text-h6 font-weight-bold mb-2" style="color:#0A1C3A;">
                  ¿Cómo funciona?
                </div>
                <v-timeline align-top dense color="#006CA1">
                  <v-timeline-item color="#006CA1" icon="mdi-filter" small>
                    <div><b>1. Elige modalidad</b></div>
                    <div class="text-caption">Por filtros o números manuales</div>
                  </v-timeline-item>
                  <v-timeline-item color="#006CA1" icon="mdi-account-multiple" small>
                    <div><b>2. Segmenta tu público</b></div>
                    <div class="text-caption">Filtra por sector, empresa, ciudad, etc.</div>
                  </v-timeline-item>
                  <v-timeline-item color="#006CA1" icon="mdi-image-multiple" small>
                    <div><b>3. Personaliza tu campaña</b></div>
                    <div class="text-caption">Agrega imagen, video y mensaje</div>
                  </v-timeline-item>
                  <v-timeline-item color="#006CA1" icon="mdi-whatsapp" small>
                    <div><b>4. Envía y monitorea</b></div>
                    <div class="text-caption">Visualiza el resultado y métricas</div>
                  </v-timeline-item>
                </v-timeline>
                <v-divider class="my-2" />

              </v-card>

            </v-col>
          </v-row>
        </v-card>

        <!--Hasta Aqui-->

        <!------  Dialog Cambio Perfil ------->

        <v-dialog v-model="dialogCambioPerfil" :class="{ 'w-75': isMobileView, 'w-50': !isMobileView }">
          <v-card>
            <v-row>
              <v-select prepend-icon="mdi-account-box-multiple" class="mx-5 mt-10" chips label="Perfil"
                :items="selectPerfiles" v-model="selectedPerfiles" item-title="nombre" return-object item-value="id"
                variant="solo-filled" @update:model-value="() => cambiarPerfilPagina(selectedPerfiles.id)"></v-select>
            </v-row>

            <v-card-actions>
              <v-btn color="#006CA1" @click="dialogCambioPerfil = false">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!------  Dialog Cambio Perfil ------->

        <!------  Dialog Crear Campaña  ------>

        <!-- FORMULARIO PROSPECTO-->

        <v-dialog v-model="formularioContacto" width="600" persistent>
          <v-card>
            <v-card-title class="text-h6">Nuevo Contacto</v-card-title>
            <v-card-text>
              <v-row>
                <v-col>
                  <v-text-field class="mx-5 mt-5" v-model="nombre" label="Nombre" type="text" variant="outlined"
                    clearable autocomplete="off" />
                  <v-text-field class="mx-5" v-model="apellido" label="Apellido" type="text" variant="outlined"
                    clearable autocomplete="off" />
                  <v-row>
                    <v-col>
                      <v-autocomplete class="mx-5" v-model="categoria" :items="categorias" return-object
                        item-title="nombre" item-value="id" label="Categoria Cargo" variant="outlined" clearable
                        autocomplete="off" />
                    </v-col>
                    <v-col>
                      <v-autocomplete class="mx-5" v-model="cargo" :items="cargos" return-object item-title="nombre"
                        item-value="id" label="Cargo" type="text" variant="outlined" clearable autocomplete="off" />
                    </v-col>
                  </v-row>
                  <v-text-field class="mx-5" v-model="correoContacto" label="Correo" type="text" variant="outlined"
                    clearable autocomplete="off" />
                  <v-text-field class="mx-5" v-model="celular" label="Celular" type="number" variant="outlined"
                    clearable autocomplete="off" />
                  <v-text-field class="mx-5" v-model="extension" label="Extensión" type="number" variant="outlined"
                    clearable autocomplete="off" />
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue" @click="cerrarFormularioContacto()">Cancelar</v-btn>
              <v-btn color="blue" @click="formularioContacto = false">Continuar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!-- FORMULARIO PROSPECTO-->

        <!-- FORMULARIO PROSPECTO CONTACTO-->

        <v-dialog v-model="formularioProspecto" width="1000" persistent>
          <v-card>
            <v-card-title class="text-h6">Nuevo Prospecto</v-card-title>
            <v-card-text>
              <v-row>
                <v-col>
                  <h3 class="text-center mb-4">Información de la Empresa</h3>
                  <!--<v-autocomplete class="mx-5" v-model="empresa" :items="empresas" return-object item-title="nombre"
                      item-value="id" label="Empresa" variant="outlined" clearable />-->
                  <v-alert v-if="alertaNit" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                    this.mensajeAlertaNit
                    }}</v-alert>
                  <!--<v-text-field class="mx-5" v-model="nit" label="Número de Identificación" type="number"
                      variant="outlined" clearable />-->

                  <v-row>
                    <v-col cols="11">
                      <input class="campo-input mx-5 mb-5" list="empresas" id="empresa" v-model="nit"
                        @input="sanitizeNit" placeholder="NIT" autocomplete="off" />
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
                      <v-select class="ml-5" v-model="tipoId" :items="tipoIdentificacion" return-object
                        item-title="nombre" item-value="id" label="Tipo Identificación" variant="outlined" clearable
                        autocomplete="off" />
                    </v-col>
                    <v-col>
                      <v-select disabled class="mr-5" v-model="tipoEmp" :items="tipoEmpresa" return-object
                        item-title="nombre" item-value="id" label="Tipo Empresa" variant="outlined" clearable
                        autocomplete="off" />
                    </v-col>
                  </v-row>
                  <v-select class="mx-5" v-model="sector" :items="sectorEmpresa" return-object item-title="nombre"
                    item-value="id" label="Sector" variant="outlined" clearable autocomplete="off" />
                  <v-text-field class="mx-5" v-model="direccion" label="Dirección" type="text" variant="outlined"
                    clearable autocomplete="off" />
                  <v-row>
                    <v-col>
                      <v-autocomplete class="ml-5" v-model="departamento" :items="departamentos" return-object
                        item-title="nombre" item-value="id" label="Departamento" variant="outlined" clearable
                        autocomplete="off" />
                    </v-col>
                    <v-col>
                      <v-autocomplete class="mr-5" v-model="ciudad" :items="ciudades" return-object item-title="nombre"
                        item-value="id" label="Ciudad" variant="outlined" clearable autocomplete="off" />
                    </v-col>
                  </v-row>
                  <v-text-field class="mx-5" v-model="web" label="Pagina Web" type="text" variant="outlined" clearable
                    autocomplete="off" />
                  <v-text-field class="mx-5" v-model="correoEmpresa" label="Mail Empresa" type="email"
                    variant="outlined" clearable autocomplete="off" />
                  <v-row>
                    <v-col>
                      <v-text-field class="ml-5" v-model="tel1" label="Telefono 1" type="number" variant="outlined"
                        clearable autocomplete="off" />
                    </v-col>
                    <v-col>
                      <v-text-field class="mr-5" v-model="tel2" label="Telefono 2" type="number" variant="outlined"
                        clearable autocomplete="off" />
                    </v-col>
                  </v-row>
                </v-col>
                <v-col style="border-left: 1px solid #ccc; padding-left: 20px;">
                  <h3 class="text-center mb-4">Información del Contacto</h3>
                  <v-text-field class="mx-5" v-model="nombre" label="Nombre" type="text" variant="outlined" clearable
                    autocomplete="off" />
                  <v-text-field class="mx-5" v-model="apellido" label="Apellido" type="text" variant="outlined"
                    clearable autocomplete="off" />
                  <v-row>
                    <v-col>
                      <v-autocomplete class="mx-5" v-model="categoria" :items="categorias" return-object
                        item-title="nombre" item-value="id" label="Categoria Cargo" variant="outlined" clearable
                        autocomplete="off" />
                    </v-col>
                    <v-col>
                      <v-autocomplete class="mx-5" v-model="cargo" :items="cargos" return-object item-title="nombre"
                        item-value="id" label="Cargo" type="text" variant="outlined" clearable autocomplete="off" />
                    </v-col>
                  </v-row>
                  <v-text-field class="mx-5" v-model="correoContacto" label="Correo" type="email" variant="outlined"
                    clearable autocomplete="off" />
                  <v-text-field class="mx-5" v-model="celular" label="Celular" type="number" variant="outlined"
                    clearable autocomplete="off" />
                  <v-text-field class="mx-5" v-model="extension" label="Extensión" type="number" variant="outlined"
                    clearable autocomplete="off" />
                  <v-select class="mx-5" clearable label="Servicio" v-model="selectedServicioProspecto"
                    :items="selectServiciosActividad" return-object item-title="nombre" item-value="id"
                    variant="outlined" autocomplete="off"></v-select>
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue" @click="cerrarFormularioProspecto()">Cancelar</v-btn>
              <v-btn :disabled="dsGuardar" color="blue" @click="guardarDatos()">Guardar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
    </v-main>
    <!-- FORMULARIO PROSPECTO CONTACTO-->

    <v-dialog v-model="alerta" persistent style="z-index: 10000;">
      <v-card :style="getAlertStyle()">
        <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
          class="mx-auto"></v-progress-circular>
        <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-tittle>
        <v-btn class="mt-4 mx-auto" @click="cerrarDIV()"
          style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogNuevaActividad" max-width="600px" height="100vh" persistent>
      <v-card>

        <v-card-title class="text-h6">Registrar Actividad</v-card-title>

        <v-card-text>

          <v-row class="mt-n4">
            <v-col>
              <v-autocomplete label="Cliente" prepend-inner-icon="mdi-domain" v-model="selectedClienteActividad"
                :items="selectClientesActividad" return-object item-title="p_razon_social" item-value="id"
                variant="outlined" :readonly="roClienteActividad" autocomplete="off"></v-autocomplete>
            </v-col>
          </v-row>

          <v-row class="mt-n4">
            <v-col>
              Actividad:
            </v-col>
          </v-row>

          <v-row class="mt-n2">
            <v-col>
              <v-checkbox label="Llamada realizada" prepend-icon="mdi-phone" v-model="cbLlamadaRealizada" color="red"
                density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Visita presencial" prepend-icon="mdi-handshake-outline"
                v-model="cbVisitaPresencial" color="red" density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Activación de Demo" prepend-icon="mdi-account-reactivate"
                v-model="cbActivacionDemo" color="red" density="compact"></v-checkbox>
            </v-col>

            <v-col>
              <v-checkbox label="Correo enviado" prepend-icon="mdi-email" v-model="cbCorreoEnviado" color="red"
                density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Visita virtual" prepend-icon="mdi-monitor-account"
                v-model="cbVisitaVirtual" color="red" density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Cotización" prepend-icon="mdi-network-pos" v-model="cbCotizacion"
                color="red" density="compact"></v-checkbox>
            </v-col>
          </v-row>

          <v-row class="mt-n6" v-if="ifServicioActividad">
            <v-col>
              <v-select clearable label="Servicio a cotizar" prepend-inner-icon="mdi-list-box-outline"
                v-model="selectedServicioActividad" :items="selectServiciosActividad" return-object item-title="nombre"
                item-value="id" variant="outlined" autocomplete="off"></v-select>
            </v-col>
          </v-row>

          <v-row class="mt-n6" v-if="ifValorProyecto">
            <v-col>
              <v-text-field label="Valor del Proyecto" clearable prepend-inner-icon="mdi-currency-usd"
                variant="outlined" v-model="selectedValorProyecto" type="number" autocomplete="off"></v-text-field>
            </v-col>
          </v-row>

          <v-row class="mt-n6" v-if="ifDocumentos">
            <v-col>
              <v-file-input label="Adjuntar RUT" density="compact" variant="outlined" clearable
                v-model="archivoRUT"></v-file-input>
              <v-file-input multiple label="Adjuntar documento" density="compact" variant="outlined" clearable
                v-model="archivosActividad"></v-file-input>
            </v-col>
          </v-row>

          <v-row class="mt-n6" v-if="false">
            <v-col>
              <v-btn color="green" text @click="dialogHistorico = true" density="compact"
                style="float: right;">Histórico</v-btn>
            </v-col>
          </v-row>

          <v-row class="mt-n2" v-if="ifObservaciones">
            <v-col>
              <v-textarea prepend-inner-icon="mdi-eye" label="Observaciones" rows="4" variant="outlined"
                density="compact" v-model="selectedObservacionesActividad" clearable autocomplete="off"></v-textarea>
            </v-col>
          </v-row>

          <v-row class="mt-n2">
            <v-col>
              <v-select label="Estado actual del cliente" prepend-inner-icon="mdi-list-status"
                v-model="selectedEstadoActividad" :items="selectEstadosActividad" return-object item-title="nombre"
                item-value="id" variant="outlined" :readonly="roEstadoActividad" autocomplete="off"></v-select>
            </v-col>
          </v-row>

          <v-row class="mt-n2" v-if="ifComentariosAdicionales">
            <v-col>
              <v-textarea prepend-inner-icon="mdi-text-box-outline" label="Comentarios adicionales" rows="4"
                variant="outlined" density="compact" v-model="selectedComentariosActividad" clearable
                autocomplete="off"></v-textarea>
            </v-col>
          </v-row>

          <v-row class="mt-n2">
            <v-col>
              <v-text-field type="date" clearable label="Próximo seguimiento" prepend-inner-icon="mdi-calendar"
                v-model="proximoSeguimientoActividad" variant="outlined" autocomplete="off"></v-text-field>
            </v-col>
          </v-row>

          <v-row class="mt-n4" v-if="ifProximoSeguimientoActividad">
            <v-col>
              Seguimiento a realizar:
            </v-col>
          </v-row>

          <v-row class="mt-n2" v-if="ifProximoSeguimientoActividad">
            <v-col>
              <v-checkbox label="Llamar" prepend-icon="mdi-phone" v-model="cbLlamar" color="green"
                density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Visita presencial" prepend-icon="mdi-handshake-outline"
                v-model="cbVisitarPresencial" color="green" density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Activar Demo" prepend-icon="mdi-account-reactivate"
                v-model="cbActivarDemo" color="green" density="compact"></v-checkbox>
            </v-col>

            <v-col>
              <v-checkbox label="Enviar Correo" prepend-icon="mdi-email" v-model="cbEnviarCorreo" color="green"
                density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Visita virtual" prepend-icon="mdi-monitor-account"
                v-model="cbVisitarVirtual" color="green" density="compact"></v-checkbox>
              <v-checkbox class="mt-n4" label="Cotizar" prepend-icon="mdi-network-pos" v-model="cbCotizar" color="green"
                density="compact"></v-checkbox>
            </v-col>
          </v-row>

        </v-card-text>

        <v-row class="mt-n4">
          <v-col>
            <v-btn color="blue" class="ml-2" style="float: right;" @click="registrarActividad()">Registrar
              Actividad</v-btn>
            <v-btn color="blue" style="float: right;"
              @click="dialogNuevaActividad = false; limpiarCamposDialogActividad()">Cerrar</v-btn>
          </v-col>
        </v-row>

      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogHistorico" max-width="180vh" height="70vh" persistent>
      <v-card>
        <v-row class="mt-2 mx-2">
          <v-col cols="3">
            <v-card variant="elevated" elevation="10" class="my-2 pa-2"
              style="border-radius: 10px; border: 1px solid black;" color="blue-accent-2">
              <v-row>
                <v-col>
                  <div>
                    <div style="font-weight: bold; color: white; font-size: x-large;">{{ nombreClienteActividad }}
                    </div>
                    <v-spacer />
                    <div style="font-size: medium; color: white">{{ nitClienteActividad }}</div>
                    <v-spacer />
                    <div style="font-size: medium; color: white">{{ nombreContactoActividad }}</div>
                    <v-spacer />
                    <div style="font-size: medium; color: white">{{ correoContactoActividad }}</div>
                    <v-spacer />
                    <div style="font-size: medium; color: white">{{ telefonoContactoActividad }}</div>
                    <v-spacer />

                    <v-chip :prepend-icon="iconChipHistorico" class="mt-4" size="large" variant="elevated"
                      :color="chipEstadoClienteColor">
                      {{ estadoClienteHistorico }}
                    </v-chip>
                  </div>
                </v-col>
              </v-row>
            </v-card>
          </v-col>

          <v-col cols="9">
            <v-card variant="elevated" elevation="10" class="pa-4 my-2"
              style="overflow-y: auto; overflow-x: auto; border-radius: 10px; border: 1px solid black;">
              <v-row>
                <v-timeline direction="horizontal" class="mt-2 mx-2" side="start" fill-dot line-color="black"
                  line-thickness="2">
                  <v-timeline-item :dot-color="tmColorNuevo" size="x-small">
                    <v-card :color="tmColorNuevo" class="pa-2" style="white-space: pre;">
                      <v-icon class="mt-n1">mdi-plus</v-icon> Nuevo
                    </v-card>
                  </v-timeline-item>

                  <v-timeline-item :dot-color="tmColorEnProceso" size="x-small" fill-dot>
                    <v-card :color="tmColorEnProceso" class="pa-2" style="white-space: pre;">
                      <v-icon class="mt-n1">mdi-chat-processing</v-icon> En proceso
                    </v-card>
                  </v-timeline-item>

                  <v-timeline-item :dot-color="tmColorCotizado" size="x-small" fill-dot>
                    <v-card :color="tmColorCotizado" class="pa-2" style="white-space: pre;">
                      <v-icon class="mt-n1">mdi-cash-sync</v-icon> Cotizado
                    </v-card>
                  </v-timeline-item>

                  <v-timeline-item :dot-color="tmColorCerradoE" size="x-small" fill-dot>
                    <v-card :color="tmColorCerradoE" class="pa-2" style="white-space: pre;">
                      <v-icon class="mt-n1">mdi-check</v-icon> Cerrado Exitoso
                    </v-card>
                  </v-timeline-item>

                  <v-timeline-item :dot-color="tmColorCerradoD" size="x-small" fill-dot>
                    <v-card :color="tmColorCerradoD" class="pa-2" style="white-space: pre;">
                      <v-icon class="mt-n1">mdi-close</v-icon> Cerrado Declinado
                    </v-card>
                  </v-timeline-item>
                </v-timeline>
              </v-row>

              <v-row v-for="(item, index) in estados" :key="index">
                <v-card variant="outlined" class="pa-2 my-2 mx-2">
                  <v-row>
                    <v-col cols="9" style="text-align: justify;">
                      Se realizaron diferentes actividades con el cliente, incluyendo llamadas, visitas y correos
                      electrónicos. El cliente mostró interés en los servicios ofrecidos y se programó una reunión
                      para
                      discutir detalles adicionales.
                    </v-col>

                    <v-col>
                      <v-row>
                        <v-col>
                          <div style="float: right;">01-01-2025</div>
                        </v-col>
                      </v-row>

                      <v-row class="mt-n2">
                        <v-col>
                          <v-chip :color="item.color" class="" size="small" style="float: right;" variant="elevated">
                            {{ item.nombre }}
                          </v-chip>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-card>
              </v-row>
            </v-card>
          </v-col>
        </v-row>

        <v-row class="mt-2 mx-2">
          <v-col class="text-center">
            <v-btn color="blue" text @click="dialogHistorico = false" style="float: right;">Cerrar</v-btn>
          </v-col>
        </v-row>


      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogNuevaOportunidad" max-width="70vh" height="60vh" persistent>
      <v-card>

        <v-card-title class="text-h6 mt-2">
          Nueva Oportunidad
        </v-card-title>

        <v-card-text>
          <v-row>
            <v-col>
              <v-autocomplete clearable label="Cliente" prepend-inner-icon="mdi-domain"
                v-model="selectedClienteOportunidad" :items="selectClientesOportunidad" return-object
                item-title="p_razon_social" item-value="id" variant="outlined" autocomplete="off"></v-autocomplete>
            </v-col>
          </v-row>

          <v-row class="mt-n2">
            <v-col>
              <v-select clearable label="Relacionar Servicio" prepend-inner-icon="mdi-list-box-outline"
                v-model="selectedServicioOportunidad" :items="selectServiciosOportunidad" return-object
                item-title="nombre" item-value="id" variant="outlined" autocomplete="off"></v-select>
            </v-col>
          </v-row>

          <v-row class="mt-n2" v-if=false>
            <v-col>
              <v-text-field label="Valor del Proyecto" clearable prepend-inner-icon="mdi-currency-usd"
                variant="outlined" v-model="selectedValorProyectoOportunidad" type="number"
                autocomplete="off"></v-text-field>
            </v-col>
          </v-row>

          <v-row class="mt-n2">
            <v-col>
              <v-textarea prepend-inner-icon="mdi-eye" label="Observaciones" rows="4" variant="outlined"
                density="compact" v-model="selectedObservacionesOportunidad" clearable autocomplete="off"></v-textarea>
            </v-col>
          </v-row>
        </v-card-text>

        <v-row class="mt-n10 mx-2">
          <v-col>
            <v-btn color="blue" @click="registrarOportunidad()" class="ml-2" style="float: right;">Registrar
              Oportunidad</v-btn>
            <v-btn color="blue" text @click="dialogNuevaOportunidad = false" style="float: right;">Cerrar</v-btn>
          </v-col>
        </v-row>

      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogListProspEst" max-width="90%" height="100vh" persistent>
      <v-card class="pt-5 pl-5 pr-5">
        <v-card-title class="d-flex justify-space-between align-center">
          <span>Listar Prospectos en Estado {{ estadoactual }}</span>
          <v-btn icon @click="dialogListProspEst = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <v-data-table hide-default-footer>
            <thead>
              <tr>
                <th>NIT</th>
                <th>Razón Social</th>
                <th>Costo Proyecto</th>
                <th>Servicio Interesado</th>
                <th>Fecha Pro. Seguimiento</th>
                <th>Tipo Seguimiento</th>
                <th>Observaciones</th>
                <th>Fecha Creado</th>
                <th v-if="false">ID oportunidad</th>
                <th v-if="false">ID Empresa</th>
              </tr>
            </thead>

            <tbody>
              <tr @click="abrirNuevaActividad(item)" v-for="item in itemsListProspEst" :key="item.id">
                <td>{{ item.nit }}</td>
                <td>{{ item.razon_social }}</td>
                <td>{{ item.valorproy }}</td>
                <td>{{ item.nomserv }}</td>
                <td>{{ item.fecproxseg }}</td>
                <td>{{ item.nomseg }}</td>
                <td>{{ item.obsev }}</td>
                <td>{{ item.fecha_act }}</td>
                <td v-if="false">{{ item.idproc }}</td>
                <td v-if="false">{{ item.idemp }}</td>
                <td v-if="false">{{ item.idest }}</td>
              </tr>
            </tbody>
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-dialog>

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
              variant="outlined" clearable autocomplete="off" density="compact" @update:model-value="filtrarEmpresas()"
              :readonly="filtroRazonSocialEmpresasComercial || filtroFechaDesdeEmpresasComercial" />
          </v-col>

          <v-col cols="3">
            <v-text-field v-model="filtroFechaDesdeEmpresasComercial" label="Fecha de Creación Desde" type="date"
              variant="outlined" clearable autocomplete="off" density="compact" @update:model-value="filtrarEmpresas2()"
              :readonly="filtroRazonSocialEmpresasComercial || filtroNitEmpresasComercial" />
          </v-col>

          <v-col cols="3">
            <v-text-field v-model="filtroFechaHastaEmpresasComercial" label="Fecha de Creación Hasta" type="date"
              variant="outlined" clearable autocomplete="off" density="compact" @update:model-value="filtrarEmpresas2()"
              :readonly="filtroRazonSocialEmpresasComercial || filtroNitEmpresasComercial"
              v-if="filtroFechaDesdeEmpresasComercial" />
          </v-col>
        </v-row>

        <v-card-text style="overflow-y: auto; height: 100%;">

          <v-row v-for="(fila, filaIndex) in filasEmpresas" :key="filaIndex" class="mb-4">
            <v-col v-for="empresa in fila" :key="empresa.id">
              <v-card @click="cargarProspecto(empresa)" class="pa-2 mt-4 mb-n8" color="grey" variant="outlined"
                style="background-color: #f5f5f5; border-radius: 10px;">
                <v-card-title style="color: #0A1C3A;">
                  <v-icon>
                    mdi-office-building
                  </v-icon>
                  {{ empresa.p_razon_social }}
                </v-card-title>
                <v-card-subtitle style="color: #0A1C3A;">
                  <v-row>
                    <v-col align="start" style="white-space: wrap;">
                      NIT: {{ empresa.p_nit }}
                      <v-spacer></v-spacer>
                      Teléfono: {{ empresa.p_telefono1 }}
                    </v-col>

                    <v-col align="end" style="white-space: wrap;">
                      Contacto: {{ empresa.pc_nombre }} {{ empresa.pc_apellido }}
                      <v-spacer></v-spacer>
                      Teléfono: {{ empresa.pc_celular }}
                    </v-col>
                  </v-row>
                </v-card-subtitle>
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
            <v-icon style="float: right;" @click="actualizarProspecto()" icon="mdi-content-save" size="small"></v-icon>
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
                  <input class="campo-input mx-5 mb-5" list="empresas" id="empresa" v-model="nitComercial"
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
                  <v-text-field class="ml-5" v-model="tel1Comercial" label="Telefono 1" type="number" variant="outlined"
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
              <v-text-field class="mx-5" v-model="correoContactoComercial" label="Correo" type="text" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-email</v-icon>
                </template>
              </v-text-field>

              <v-alert v-if="alertaCelular" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
                this.mensajeAlertaCelular
                }}</v-alert>
              <v-text-field class="mx-5" v-model="celularComercial" label="Celular" type="number" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-cellphone</v-icon>
                </template>
              </v-text-field>

              <v-text-field class="mx-5" v-model="extensionComercial" label="Extensión" type="number" variant="outlined"
                clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%;">mdi-numeric</v-icon>
                </template>
              </v-text-field>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions>
          <v-btn @click="dialogCrearEditarProspecto = false; dialogProspectos = true; limpiarCamposProspecto();"
            color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!----- Dialogo para crear/editar los prospectos ----->

    <v-dialog v-model="alertaArchivoGrande" max-width="400" persistent>
      <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
        <v-row align="center" no-gutters>
          <v-col class="d-flex align-center" style="flex: none; width: auto;">
            <v-icon class="mr-2">mdi-alert-circle</v-icon>
            Archivo demasiado grande
          </v-col>
          <v-spacer />
        </v-row>
      </v-card-title>
      <v-card>
        <v-card-text class="text-center py-4">
          {{ mensajeArchivoGrande }}
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="#006CA1" variant="flat" @click="alertaArchivoGrande = false">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!------  Dialog Crear Campaña  ------>

    <v-dialog v-model="dialogCrearCampaña" max-width="800" transition="dialog-bottom-transition" persistent>
      <v-card rounded="xl" elevation="3" class="dialog-card">
        <!-- Header -->
        <v-card-title class="py-3 px-4 d-flex align-center" style="background:#006CA1;color:#fff;">
          <v-icon class="mr-2">mdi-calendar-multiple</v-icon>
          <span class="text-h6">Crear nueva campaña</span>
          <v-spacer />
          <v-btn icon variant="text" color="white" @click="cerrarFormularioCampaña()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>

        <!-- Body -->
        <v-card-text class="px-4 pt-4 pb-0">
          <v-form ref="formNuevaCampaña" v-model="formOk">
            <v-row>


              <!-- Imagen derecha -->
              <v-col cols="12" md="4" class="d-flex flex-column align-center justify-center pa-0 ml-8">
                <div class="text-caption mt-2" style="color:#888;">
                  Añadir una Imagen o Vídeo<br>
                </div>
                <div class="image-upload-area" @click="() => $refs.inputImagenCampana.click()"
                  @keydown.enter="() => $refs.inputImagenCampana.click()" tabindex="0"
                  style="cursor:pointer; outline:none;">
                  <template v-if="esVideo(selectedImagenCampana?.name || previewVideoCampana)">
                    <video :src="previewVideoCampana" height="220" width="180"
                      style="border-radius:12px; object-fit:cover; background:#f5f6f7;" controls
                      :poster="previewImagenCampana" class="elevation-1"></video>
                  </template>
                  <template v-else>
                    <v-img
                      :src="previewImagenCampana || 'https://shop.myharvestfarms.com/product/holistic-morning-kit/'"
                      height="220" width="180" cover style="border-radius:12px; object-fit:cover;"
                      class="elevation-1" />
                  </template>
                  <!-- Input de archivo oculto -->
                  <input ref="inputImagenCampana" type="file" accept="image/jpeg,image/png,image/jpg,video/mp4"
                    style="display:none" @change="onImagenCampanaChange" />
                </div>
                <div class="text-caption mt-2" style="color:#888;">
                  Haz clic en la imagen para cambiar<br>
                  <span style="font-size:12px;">(Máx. 14MB. Solo JPG, PNG, JPEG, MP4)</span>
                </div>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>

        <v-divider class="my-4" />

        <!-- Footer -->
        <v-card-actions class="px-4 pb-4 pt-0">
          <v-spacer />
          <v-btn variant="outlined" color="primary" class="btn-details text-none btn-grow-card mr-2"
            @click="cerrarFormularioCampaña()">Cancelar</v-btn>
          <v-btn :disabled="nombreCampaniaDuplicado" variant="outlined" color="primary"
            class="btn-details text-none btn-grow-card " @click="GuardarFormularioCampaña()">
            Guardar
            <v-icon end class="ml-1">mdi-content-save-check</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="cargandoCampania" persistent max-width="340" transition="dialog-bottom-transition">
      <v-card class="pa-6 d-flex flex-column align-center justify-center" style="border-radius: 18px;">
        <v-progress-circular :size="70" :width="7" color="primary" indeterminate class="mb-4" />
        <v-progress-linear v-if="progresoCampania > 0 && progresoCampania < 100" :value="progresoCampania"
          color="primary" height="8" rounded class="mb-2" style="width: 90%;" />
        <div class="text-h6 font-weight-bold mb-1" style="color:#006CA1;">
          Guardando campaña...
        </div>
        <div style="color:#888; font-size:15px;">
          Por favor espera, estamos procesando tu información.
        </div>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogAvisoEnvio" max-width="500">
      <v-card>
        <v-card-title style="background:#006CA1;color:#fff" :class="{}" class="font-weight-bold">
          <v-icon v-if="tipoAvisoEnvio === 'success'" color="success" class="mr-2">mdi-check-circle</v-icon>
          <v-icon v-else-if="tipoAvisoEnvio === 'warning'" color="warning" class="mr-2">mdi-alert</v-icon>
          <v-icon v-else color="error" class="mr-2">mdi-alert-circle</v-icon>
          {{ tipoAvisoEnvio === 'success' ? '¡Envío exitoso!' : tipoAvisoEnvio === 'warning' ? 'Atención' : 'Error' }}
          <v-progress-circular v-if="ifCargando" color="yellow" indeterminate :size="30" :width="5"
            class="mx-auto ml-2"></v-progress-circular>
        </v-card-title>
        <v-card-text style="white-space: pre-line; max-height: 600px; overflow-y: auto;">
          <!-- Mostrar listas estructuradas si existen -->
          <div
            v-if="(invalidFromResultadosDisplay && invalidFromResultadosDisplay.length) || (invalidFromManualDisplay && invalidFromManualDisplay.length)">
            <div style="color:#444; margin-bottom:8px; font-weight:600;">Los siguientes números ya cuentan con una
              campaña
              enviada en las últimas 24 horas y no pueden ser incluidos en el envío de esta campaña, por lo que serán
              excluidos:</div>

            <v-list dense nav>
              <template v-if="invalidFromResultadosDisplay && invalidFromResultadosDisplay.length">
                <div class="d-flex align-center pl-0"
                  style="font-weight:700; color:#006CA1; margin-top:8px; margin-bottom:4px;">
                  <v-icon color="#006CA1" class="mr-2" size="18"
                    style="background:#e6f4ff;border-radius:50%;padding:4px;">mdi-information</v-icon>
                  <span>Desde filtros</span>
                </div>
                <v-list-item v-for="(item, idx) in invalidFromResultadosDisplay" :key="`bd-${idx}`">
                  <v-list-item-content>
                    <div style="color:#222">
                      <li>{{ item }}</li>
                    </div>
                  </v-list-item-content>
                </v-list-item>
              </template>

              <template v-if="invalidFromManualDisplay && invalidFromManualDisplay.length">
                <div class="d-flex align-center pl-0"
                  style="font-weight:700; color:#006CA1; margin-top:8px; margin-bottom:4px;">
                  <v-icon color="#006CA1" class="mr-2" size="18"
                    style="background:#e6f4ff;border-radius:50%;padding:4px;">mdi-information</v-icon>
                  <span>Números manuales</span>
                </div>
                <v-list-item v-for="(item, idx) in invalidFromManualDisplay" :key="`man-${idx}`">
                  <v-list-item-content>
                    <div style="color:#222">
                      <li>{{ item }}</li>
                    </div>
                  </v-list-item-content>
                </v-list-item>
              </template>
            </v-list>
          </div>

          <!-- Fallback: mostrar mensaje plano si no hay listas estructuradas -->
          <div v-else>
            <p v-html="mensajeAvisoEnvio"></p>
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="#006CA1" variant="flat" @click="send" v-if="!ifCargando">Deseo Continuar</v-btn>
          <v-btn color="grey" variant="flat" @click="cerrarAvisoEnvio">Cancelar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogConfirmarEnvio" max-width="420">
      <v-card v-if="!reenviandoCampania">

        <v-card-title style="background:#006CA1;color:#fff" class="font-weight-bold">
          <v-icon color="#deae00" class="mr-2">mdi-alert</v-icon>
          Confirmar envío de campaña
        </v-card-title>
        <v-card-text style="white-space: pre-line;">
          <div class="mt-1" style="color:#595301;">
            <span v-if="!reenviarUnaCampaña">
              Precaución, ten en cuenta que una vez enviada la campaña, por seguridad y fiabilidad de las métricas,
              <b>no
                podrás realizar cambios</b>.
            </span>
            <span v-if="reenviarUnaCampaña">
              Se reenviara la campaña a los destinatarios seleccionados, ten en cuenta que esta acción no es reversible.
            </span>
          </div>
          <div class="mt-3" style="color:#444;">
            ¿Estás seguro que deseas enviar la campaña?
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="grey" variant="flat"
            @click="dialogConfirmarEnvio = false, enviandoCampania = true;">Cancelar</v-btn>
          <v-btn :disabled="enviandoCampania" color="#006CA1" variant="flat" @click="send">Sí, enviar</v-btn>
        </v-card-actions>
      </v-card>
      <v-card v-if="reenviandoCampania">

        <v-card-title style="background:#006CA1;color:#fff" class="font-weight-bold">
          <v-icon color="#deae00" class="mr-2">mdi-alert</v-icon>
          Confirmar Reenvio de campaña
        </v-card-title>
        <v-card-text style="white-space: pre-line;">
          <div class="mt-1" style="color:#595301;">
            <span>
              Una vez reenviada la campaña no se puede cancelar este proceso, verifica que los datos y filtros sean
              correctos.
            </span>
          </div>
          <div class="mt-3" style="color:#444;">
            ¿Estás seguro que deseas Reenviar la campaña?
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="grey" variant="flat"
            @click="dialogConfirmarEnvio = false, enviandoCampania = true;">Cancelar</v-btn>
          <v-btn :disabled="enviandoCampania" color="#006CA1" variant="flat" @click="send">Sí, enviar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogImagenAmpliadaCampana"
      :max-width="infoImagenPreview ? (infoImagenPreview.width + 200) + 'px' : '90vw'" persistent scrollable>

      <v-card style="border-radius: 18px; background: #f8fafc;">
        <!-- Cabecera -->
        <v-card-title class="d-flex align-center justify-space-between"
          style="background: #006CA1; color: white; border-top-left-radius: 18px; border-top-right-radius: 18px;">
          <div class="d-flex align-center">
            <v-icon class="mr-2" color="white">mdi-image</v-icon>
            Vista previa de la imagen
          </div>
          <v-btn icon color="white" @click="dialogImagenAmpliadaCampana = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>

        <!-- Imagen centrada, tamaño real -->
        <v-card-text class="d-flex flex-column align-center justify-center" :style="{
          background: '#fff',
          padding: '24px',
          minHeight: infoImagenPreview ? (infoImagenPreview.height + 48) + 'px' : 'auto'
        }">
          <v-img v-if="infoImagenPreview" :src="imagenAmpliadaUrlCampana" :width="infoImagenPreview.width"
            :height="infoImagenPreview.height" :style="{
              background: '#fff',
              maxWidth: '90vw',
              maxHeight: '80vh',
              cursor: 'zoom-in'
            }" class="mb-2" contain @click="abrirImagenEnNuevaPestana(imagenAmpliadaUrlCampana)">
            <template #error>
              <div class="d-flex align-center justify-center" style="height: 200px;">
                <v-icon size="48" color="grey">mdi-image-off</v-icon>
                <span class="ml-2">No se pudo cargar la imagen</span>
              </div>
            </template>
          </v-img>
          <!-- Mientras no se carga la info, muestra un loader o placeholder -->
          <v-progress-circular v-else indeterminate color="primary" size="48" class="my-8" />
          <!-- Info de la imagen -->
          <div v-if="infoImagenPreview" class="mt-2 text-center" style="font-size: 0.97rem; color: #222;">
            <div>
              <v-icon size="18" color="#1976d2" class="mr-1">mdi-information-outline</v-icon>
              <span><b>Dimensiones:</b> {{ infoImagenPreview.width }} x {{ infoImagenPreview.height }} px</span>
            </div>
            <div>
              <v-icon size="18" color="#1976d2" class="mr-1">mdi-file-image</v-icon>
              <span><b>Formato:</b> {{ infoImagenPreview.format }}</span>
            </div>
          </div>
        </v-card-text>

        <!-- Acciones -->
        <v-card-actions class="justify-end">
          <v-btn v-if="imagenAmpliadaUrlCampana" color="primary" variant="outlined" :href="imagenAmpliadaUrlCampana"
            target="_blank" download class="mr-2">
            <v-icon left size="18">mdi-download</v-icon>
            Descargar
          </v-btn>
          <v-btn color="grey" variant="flat" @click="dialogImagenAmpliadaCampana = false">
            <v-icon left size="18">mdi-close</v-icon>
            Cerrar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Dialog informativo para archivos con numeros manuales -->
    <v-dialog v-model="dialogInforArchivoNumeros" max-width="1100" height="700" class="responsive-size"
      style="--responsive-width: 1000px; --responsive-height: 600px;">
      <v-card>
        <v-card-title style="background:#006CA1;color:#fff" class="font-weight-bold">
          <v-icon color="white" class="mr-2">mdi-information</v-icon>
          Formatos de archivo aceptados
          <v-btn color="white" variant="flat" @click="dialogInforArchivoNumeros = false"
            style="float: right; border-radius: 15px;"><v-icon>mdi-close</v-icon></v-btn>
        </v-card-title>
        <v-card-text style="padding-bottom: 0;">
          <div style="color:#444; font-size: 1.04rem; margin-bottom: 18px;">
            Selecciona el tipo de archivo disponible para ver su formato.
            <v-btn color="#006CA1" variant="flat" class="ml-4" style="float: right;"
              @click="descargarPlantilla()">Descargar
              plantilla</v-btn>
          </div>
          <v-tabs v-model="tabFormatoArchivo" background-color="#e3f2fd" color="#006CA1" grow>
            <v-tab value="excel"><v-icon class="mr-2">mdi-file-excel</v-icon> Excel (.xlsx .xls)</v-tab>
          </v-tabs>
          <v-window v-model="tabFormatoArchivo" class="mt-3">
            <v-window-item value="excel">
              <div
                style="display: flex; justify-content: center; align-items: center; min-height: 520px; max-height: 600px; background: #888;">
                <div
                  style="position: absolute; top: 8px; left: 16px; color: #fff; background: rgba(0, 0, 0, 0.5); padding: 4px 8px; border-radius: 4px;">
                  En este formato asegúrate de colocar los números en la segunda columna (B)
                </div>
                <img :src="formatoExcel" class="mt-6" alt="Ejemplo archivo plano" width="900" height="450"
                  style="background: #fff; border-radius: 12px; box-shadow: 0 1px 14px #1976d2; cursor: zoom-in; object-fit: fill; max-width: 100%; max-height: 520px;"
                  @click="abrirImagenEnNuevaPestana(formatoExcel)" />
              </div>
            </v-window-item>
          </v-window>
        </v-card-text>
      </v-card>
    </v-dialog>


  </v-app>
</template>


<script>
import formatoExcel from '../assets/formatoEXCEL.png';

import axios from 'axios';
import CryptoJS from "crypto-js";
import AppHeader from '../components/AppHeader.vue';

export default {
  components: {
    AppHeader,
  },
  data: () => ({
    baseURL: '', // URL base de la API
    comercialId: 0, // ID del usuario comercial
    nombreComercial: null, // Nombre del usuario comercial
    correoUsuario: null, // Correo del usuario
    fecha: new Date().toISOString().substr(0, 10), // Formato YYYY-MM-DD
    fechaInicio: '',
    fechaFin: '',
    estadoactual: '',

    imagenComercial: null,

    empresaSeleccionada: null,
    empresas: [],

    productoSeleccionado: null,
    productos: [],

    mensajeAlertaRazonSocial: '',
    alertaNit: false,
    mensajeAlertaNit: '',
    alertaRazonSocial: false,
    prospecto: null,
    prospectos: [],
    alertaProspecto: false,
    dsCrear: false,
    formularioContacto: false,
    formularioProspecto: false,
    nombre: null,
    apellido: null,
    categoria: null,
    categorias: [],
    cargo: null,
    cargos: [],
    correoContacto: null,
    celular: null,
    extension: null,
    selectedServicioProspecto: null,
    empresa: null,
    alerta: false,
    mensajeAlerta: '',
    dsGuardar: false,
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
    tel1: null,
    tel2: null,
    mensajeAlertLogin: '',
    idUsuario: null,
    idCargo: null,

    progress: 0,
    porcMetaMensual: 0,
    ctaMetaMensual: 0,
    ctaProspecto: 0,
    ctaEnProceso: 0,
    ctaCotizados: 0,
    ctaGanado: 0,
    ctaAcumulado: 0,
    itemsProspecto: [],
    itemsEnProceso: [],
    itemsCotizados: [],
    itemsGanado: [],

    canal: null,
    canales: [
      { id: 1, nombre: 'Lead' },
      { id: 2, nombre: 'Comercial' }
    ],

    estados: [
      {
        id: 1,
        nombre: 'Prospecto',
        cantidad: 0,
        color: 'blue',
        total: 0,
        items: []
      },
      {
        id: 2,
        nombre: 'En Proceso',
        cantidad: 0,
        color: 'purple',
        total: 0,
        items: []
      },
      {
        id: 3,
        nombre: 'Cotizados',
        cantidad: 0,
        color: 'orange',
        total: 0,
        items: []
      },
      {
        id: 4,
        nombre: 'Ganado',
        cantidad: 0,
        color: 'green',
        total: 0,
        items: []
      },
      {
        id: 5,
        nombre: 'Perdido',
        cantidad: 0,
        color: 'red',
        total: 0,
        items: []
      }
    ],

    dialogNuevaActividad: false,
    dialogHistorico: false,
    dialogNuevaOportunidad: false,

    mensajeAlertLogin: '',

    selectedClienteActividad: null,
    roClienteActividad: true,
    selectClientesActividad: [],

    idActividad: null,

    cbLlamadaRealizada: false,
    cbVisitaPresencial: false,
    cbActivacionDemo: false,
    cbCorreoEnviado: false,
    cbVisitaVirtual: false,
    cbCotizacion: false,

    selectedObservacionesActividad: null,

    selectedEstadoActividad: null,
    selectEstadosActividad: [],
    roEstadoActividad: false,

    proximoSeguimientoActividad: null,

    idSeguimiento: null,

    cbLlamar: false,
    cbVisitarPresencial: false,
    cbActivarDemo: false,
    cbEnviarCorreo: false,
    cbVisitarVirtual: false,
    cbCotizar: false,

    selectedServicioActividad: null,
    selectServiciosActividad: [],

    selectedValorProyecto: null,

    archivoRUT: null,
    archivosActividad: [],

    selectedComentariosActividad: null,

    ifServicioActividad: false,
    ifValorProyecto: false,
    ifDocumentos: false,
    ifObservaciones: true,
    ifComentariosAdicionales: false,

    ifProximoSeguimientoActividad: false,

    nombreClienteActividad: 'Del Alba S.A.S',
    nitClienteActividad: '900123456-7',
    nombreContactoActividad: 'Carolina Ruiz',
    correoContactoActividad: 'carolina@delalba.com',
    telefonoContactoActividad: '+57 310 1234567',

    estadoClienteHistorico: 'Cerrado Exitoso',
    iconChipHistorico: 'mdi-check',
    chipEstadoClienteColor: 'red',

    tmColorNuevo: 'grey',
    tmColorEnProceso: 'grey',
    tmColorCotizado: 'grey',
    tmColorCerradoE: 'red',
    tmColorCerradoD: 'grey',

    selectedClienteOportunidad: null,
    selectClientesOportunidad: [],
    selectedServicioOportunidad: null,
    selectServiciosOportunidad: [],
    selectedValorProyectoOportunidad: 0,
    selectedObservacionesOportunidad: null,

    idOportunidad: null,

    ifSeleccionarFechas: false,
    rangoFechas: null,

    tareas: 0,
    fechaInicio: '',
    fechaFin: '',
    dialogListProspEst: false,

    itemsListProspEst: [],

    headersListProspEst: [
      { text: 'NIT', value: 'nit', sortable: true },
      { text: 'Razón Social', value: 'razon_social' },
      { text: 'Costo Proyecto', value: 'valorproy' },
      { text: 'Servicio Interesado', value: 'nomserv' },
      { text: 'Fecha Pro. Seguimiento', value: 'fecproxseg' },
      { text: 'Tipo Seguimiento', value: 'nomseg' },
      { text: 'Observaciones', value: 'obsev' },
      { text: 'Fecha Creado', value: 'fecha_act' },
    ],

    listaEmpresas: [],
    listaEmpresas2: [],

    // Cambios Angelo
    imagenComercial: null,
    drawer: false,
    inicio: 1,

    ifCargando: false,

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

    //VARIABLES DE LA PESTAÑA CAMPAÑA
    template: null,
    templates: [],
    selectedTemplate: null,
    campnom: null,
    campdet: null,
    header_text: null,
    opcionesFiltros: [],
    // FILTROS PARA ENVIAR MENSAJE DE CAMPAÑA - SE REALIZA BUSQUEDA EN LA BASE DE DATOS
    filtros: [],
    filtroSector: null,
    itemsSector: [],
    filtroEmpresa: null,
    itemsEmpresa: [],
    filtroCatCargo: null,
    itemsCatCargo: [],
    filtroCargo: null,
    itemsCargo: [],
    filtroDpto: null,
    itemsDpto: [],
    filtroCiudad: null,
    itemsCiudad: [],
    filtrosBD: {
      idsector: null,
      idempresa: null,
      idcatcargo: null,
      idcargo: null,
      iddpto: null,
      idciudad: null,
    },
    resultados: [],
    publicidad: [],
    publicidadFiltrada: [],
    totalRegistrosBd: 'Registros a enviar: 0',

    header_text: null,
    header_img: null,
    header_img_url: null,
    header_doc: null,
    header_doc_url: null,
    header_vid: null,
    header_vid_url: null,
    footer: null,
    showAlert: false,
    alertMessage: '',
    alertType: 'success', // 'success', 'error', 'info', 'warning'

    numerosManual: '',


    alertaArchivoGrande: false,
    mensajeArchivoGrande: '',

    dialogCrearCampaña: false,

    selectedNombreCampana: null,
    selectedDetalleCampana: null,
    selectedGuionCampaña: null,
    selectedUrlmediaCampaña: null,

    selectedImagenCampana: null,
    previewImagenCampana: 'https://shop.myharvestfarms.com/product/holistic-morning-kit/',
    selectedImagenCampanaEditar: null,
    previewImagenCampanaEditar: null,
    previewVideoCampana: null,

    opcionesTipoEnvio: [
      'Por filtros de prospectos',
      'Registrar números manualmente'
    ],
    tipoEnvio: [],

    campnomKey: 0,

    cargandoCampania: false,
    progresoCampania: 0,
    dialogAvisoEnvio: false,
    mensajeAvisoEnvio: '',
    tipoAvisoEnvio: '', // 'success', 'warning', 'error'
    // Listas estructuradas para mostrar inválidos de forma visual
    invalidFromResultadosDisplay: [],
    invalidFromManualDisplay: [],

    dialogImagenAmpliadaCampana: false,
    imagenAmpliadaUrlCampana: '',
    infoImagenPreview: null,
    menuActivo: '',

    dialogConfirmarEnvio: false,
    enviandoCampania: true,

    reenviarUnaCampaña: false,

    filtrosDefinidos: [],
    filtrosEnvio: {},

    archivoNumerosManuales: null,
    dialogInforArchivoNumeros: false,
    tabFormatoArchivo: 'excel',
    formatoExcel,
    numerosInvalidosArray: [],
    
    
    selectedAreaVentas: null,
    areasVentas: [],
    selectedComerciales: null,
    comerciales: [],
  }),

  mounted() {
    //axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL; // URL base de la API
    this.cargarFiltroSector();
    this.cargarFiltroEmpresa();
    this.cargarFiltroCatCargo();
    this.cargarFiltroCargo();
    this.cargarFiltroDepartamento();
    this.cargarFiltroCiudad();

    this.baseURL = import.meta.env.VITE_API_BASE_URL; // URL base de la API
    this.datosIniciales();
    this.idUsuario = localStorage.getItem('idUsuario');
    this.idCargo = localStorage.getItem('idCargo');
    this.llamadoServicios();
    this.llamadoEmpresas();

    this.cargarClientesActividad();
    this.cargarEstadosActividad();
    this.cargarServiciosActividad();
    this.obtenerEmpresas();
    this.cargarMetaUsu();

    //Añadiendo toda la pagina Campaña
    this.nombreLogin = localStorage.getItem('nombreLogin');
    this.correoUsuario = localStorage.getItem('correo');

    const imagenGuardada = localStorage.getItem('imagenComercial');
    if (imagenGuardada) {
      this.imagenComercial = imagenGuardada;
    } else {
      this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg`;
    }

    this.cargarPublicidad();
    this.cargarDatos();
    console.log("this.comercialId: " + this.comercialId);

    this.setMenuActivoPorRuta();
    this.llamadoFiltrosDestinatarios();
    this.cargarDatosBaseFiltros();
    this.cargarareascomerciales();

    this.loadTemplates().then(() => {
      if (localStorage.getItem('reenviarUnaCampaña') === 'true') {
        console.log("LOCALSTORAGE", localStorage.getItem('campanaReenviar'))
        this.mensajeAlertLogin = 'Cargando Información de la campaña.';
        this.alerta = true;
        this.ifCargando = true;
        setTimeout(() => {
          this.alerta = false;
          this.ifCargando = false;

          const campana = JSON.parse(localStorage.getItem('campanaReenviar') || '{}');
          if (campana && campana.id) {
            this.reenviarUnaCampaña = true;

            const campItem = this.publicidad.find(c => c.id === campana.id);
            if (campItem) {
              this.campdet = campItem.detalle || '';
              this.previewImagenCampana = campItem.url_media || '';
              this.selectedImagenCampana = campItem.url_media
            }

            // Cargar filtrosEnvio
            if (campana.filtrosEnvio) {
              let filtros = typeof campana.filtrosEnvio === 'string' ? JSON.parse(campana.filtrosEnvio) : campana.filtrosEnvio;
              this.filtrosEnvio = { ...filtros };
              this.filtros = this.filtrosDefinidos
                .filter(fd => filtros[fd.id] && filtros[fd.id] !== 0)
                .map(fd => fd.nombre);
            }

            // Cargar números manuales
            if (campana.numeros_manual) {
              this.numerosManual = campana.numeros_manual;
            }

            // Seleccionar tipo de envío
            let tipoEnvioArr = [];
            if (campana.filtrosEnvio && Object.values(this.filtrosEnvio).some(v => v && v !== 0)) {
              tipoEnvioArr.push('Por filtros de prospectos');
            }
            if (campana.numeros_manual && campana.numeros_manual.trim().length > 0) {
              tipoEnvioArr.push('Registrar números manualmente');
            }
            this.tipoEnvio = tipoEnvioArr;

            const plantillaEnvio = campana.plantilla_envio || campana.plantillaEnvio || campana.template || '';

            // Busca el template ignorando mayúsculas/minúsculas y espacios
            const foundTemplate = this.templates.find(
              t => (t.name || '').trim().toLowerCase() === plantillaEnvio.trim().toLowerCase()
            );

            if (foundTemplate) {
              this.selectedTemplate = foundTemplate;
              this.campnom = campItem;
            } else {
              this.selectedTemplate = null;
            }

          }
          localStorage.removeItem('reenviarUnaCampaña');
        }, 2000);
      }
    });



  },
  watch: {
    '$route.path'() {
      this.setMenuActivoPorRuta();
    },

    selectedAreaVentas(newValue) {
      this.cargarcomerciales(newValue ? newValue.id : 0);
    },

    tipoIdComercial(newVal) {
      if (!newVal) return;

      if (newVal.nombre === 'NIT') {
        this.tipoEmpComercial = this.tipoEmpresa.find(item => item.nombre === 'Jurídica');
      } else {
        this.tipoEmpComercial = this.tipoEmpresa.find(item => item.nombre === 'Natural');
      }
    },

    empresaSeleccionada(newValue) {
      this.datosIniciales();

    },

    productoSeleccionado(newValue) {
      this.datosIniciales();

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
      this.validarNit(newNitComercial);
    },

    razonSocialComercial(newRazonSocialComercial) {
      this.validarRazonSocial(newRazonSocialComercial);
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

    cbCotizacion(newValue) {
      if (newValue) {
        this.ifServicioActividad = true;
        this.ifValorProyecto = true;
        this.ifDocumentos = true;
        this.ifObservaciones = false;
        this.ifComentariosAdicionales = true;
        this.roEstadoActividad = true;
        this.selectedEstadoActividad = this.selectEstadosActividad.find(e => e.id === 3);

        this.idActividad = 6;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbVisitaVirtual = false;
        this.cbActivacionDemo = false;
      } else {
        this.ifServicioActividad = false;
        this.ifValorProyecto = false;
        this.ifDocumentos = false;
        this.ifObservaciones = true;
        this.ifComentariosAdicionales = false;
        this.roEstadoActividad = false;
        this.selectedEstadoActividad = null;
        this.idActividad = null;
      }
    },

    selectedEstadoActividad(newValue) {
      if (newValue) {
        if (newValue.id === 3) {
          this.ifServicioActividad = true;
          this.ifValorProyecto = true;
          this.ifDocumentos = true;
          this.ifObservaciones = false;
          this.ifComentariosAdicionales = true;
          this.roEstadoActividad = true;
          this.cbCotizacion = true;
        } else {
          this.ifServicioActividad = false;
          this.ifValorProyecto = false;
          this.ifDocumentos = false;
          this.ifObservaciones = true;
          this.ifComentariosAdicionales = false;
          this.roEstadoActividad = false;
          this.cbCotizacion = false;
        }
      }
    },

    proximoSeguimientoActividad(newValue) {
      if (newValue) {
        this.ifProximoSeguimientoActividad = true;
      } else {
        this.ifProximoSeguimientoActividad = false;
        this.cbLlamar = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      }
    },

    cbLlamadaRealizada(newValue) {
      if (newValue) {
        this.idActividad = 1;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbActivacionDemo = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbCorreoEnviado(newValue) {
      if (newValue) {
        this.idActividad = 2;
        this.cbLlamadaRealizada = false;
        this.cbVisitaPresencial = false;
        this.cbActivacionDemo = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbVisitaPresencial(newValue) {
      if (newValue) {
        this.idActividad = 3;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbActivacionDemo = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbVisitaVirtual(newValue) {
      if (newValue) {
        this.idActividad = 4;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbActivacionDemo = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbActivacionDemo(newValue) {
      if (newValue) {
        this.idActividad = 5;
        this.cbLlamadaRealizada = false;
        this.cbCorreoEnviado = false;
        this.cbVisitaPresencial = false;
        this.cbVisitaVirtual = false;
        this.cbCotizacion = false;
      } else {
        this.idActividad = null;
      }
    },

    cbLlamar(newValue) {
      if (newValue) {
        this.idSeguimiento = 1;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbEnviarCorreo(newValue) {
      if (newValue) {
        this.idSeguimiento = 2;
        this.cbLlamar = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbVisitarPresencial(newValue) {
      if (newValue) {
        this.idSeguimiento = 3;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbActivarDemo = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbVisitarVirtual(newValue) {
      if (newValue) {
        this.idSeguimiento = 4;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbActivarDemo = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbActivarDemo(newValue) {
      if (newValue) {
        this.idSeguimiento = 5;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbVisitarVirtual = false;
        this.cbCotizar = false;
      } else {
        this.idSeguimiento = null;
      }
    },

    cbCotizar(newValue) {
      if (newValue) {
        this.idSeguimiento = 6;
        this.cbLlamar = false;
        this.cbEnviarCorreo = false;
        this.cbVisitarPresencial = false;
        this.cbVisitarVirtual = false;
        this.cbActivarDemo = false;
      } else {
        this.idSeguimiento = null;
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

    // WATCH DE LA VISTA CAMPAÑA

    selectedTemplate() {
      // Solo limpiar si NO es reenvío de campaña
      if (!this.reenviarUnaCampaña) {
        this.campnom = null;
        this.selectedImagenCampana = null;
        this.previewImagenCampana = 'https://shop.myharvestfarms.com/product/holistic-morning-kit/';
      }
      this.body_placeholders = [];
      this.header_url = null;
      this.header_text = null;
      this.header_img = null;
      this.header_doc = null;
      this.header_vid = null;
      this.header_img_url = null;
      this.header_vid_url = null;
      this.header_doc_url = null;
      this.template = null;

      const formatosImagen = /\.(jpg|jpeg|png|webp|gif)(\?|$)/i;
      const formatosVideo = /\.(mp4|webm|ogg|mov|avi|mkv)(\?|$)/i;

      if (this.selectedTemplate && this.selectedTemplate.name) {
        if (
          this.selectedTemplate.name === 'boletin_informativo' ||
          this.selectedTemplate.name === 'promocionar_productos_servicios'
        ) {
          this.publicidadFiltrada = this.publicidad.filter(
            camp =>
              camp.url_media &&
              formatosImagen.test(camp.url_media.split('?')[0])
          );
          this.publicidadFiltrada = this.publicidadFiltrada.filter(camp => camp.tipo === 1);
        } else if (this.selectedTemplate.name === 'video_informativo_mp4') {
          this.publicidadFiltrada = this.publicidad.filter(
            camp =>
              camp.url_media &&
              formatosVideo.test(camp.url_media.split('?')[0])
          );
          this.publicidadFiltrada = this.publicidadFiltrada.filter(camp => camp.tipo === 1);
        } else {
          this.publicidadFiltrada = this.publicidad.filter(
            camp => camp.url_media
          );
        }
      } else {
        this.publicidadFiltrada = [];
      }

      // Asigna el template seleccionado y sus componentes
      const foundTemplate = this.templates.find(t => t.name === (this.selectedTemplate ? this.selectedTemplate.name : ''));
      if (foundTemplate) {
        this.template = { ...foundTemplate };
        foundTemplate.components.forEach((data) => {
          if (data.type === 'HEADER') {
            this.template.header = data;
            this.template.headercontents = data.text ? this.findPlaceholders(data.text) : [];
          } else if (data.type === 'BODY') {
            this.template.body = data.text;
            this.template.body_placeholders = this.findPlaceholders(data.text);
          } else if (data.type === 'FOOTER') {
            this.template.footer = data.text;
          } else if (data.type === 'BUTTONS') {
            this.template.buttons = data.buttons;
          }
        });
      } else {
        this.template = null;
      }
    },

    filtrosEnvio: {
      handler(newVal) {
        this.filtrosBD.idsector = this.itemsSector.find(item => item.id === newVal[1]) || null;
        this.filtrosBD.idempresa = this.itemsEmpresa.find(item => item.id === newVal[2]) || null;
        this.filtrosBD.idcatcargo = this.itemsCatCargo.find(item => item.id === newVal[3]) || null;
        this.filtrosBD.idcargo = this.itemsCargo.find(item => item.id === newVal[4]) || null;
        this.filtrosBD.iddpto = this.itemsDpto.find(item => item.id === newVal[5]) || null;
        this.filtrosBD.idciudad = this.itemsCiudad.find(item => item.id === newVal[6]) || null;
        this.cargarDatos();
      },
      deep: true
    },

    filtros(newVal, oldVal) {
      if (!newVal.includes('Sector')) this.filtrosBD.idsector = null;
      if (!newVal.includes('Empresa')) this.filtrosBD.idempresa = null;
      if (!newVal.includes('Categoría Cargo')) this.filtrosBD.idcatcargo = null;
      if (!newVal.includes('Cargo')) this.filtrosBD.idcargo = null;
      if (!newVal.includes('Departamento')) this.filtrosBD.iddpto = null;
      if (!newVal.includes('Ciudad')) this.filtrosBD.idciudad = null;
    },

    dialogImagenAmpliadaCampana(val) {
      if (val && this.imagenAmpliadaUrlCampana) {
        this.infoImagenPreview = null; // Limpia antes de cargar
        this.cargarInfoImagenPreview(this.imagenAmpliadaUrlCampana);
      } else {
        this.infoImagenPreview = null;
      }
    },
    imagenAmpliadaUrlCampana(val) {
      if (this.dialogImagenAmpliadaCampana && val) {
        this.infoImagenPreview = null; // Limpia antes de cargar
        this.cargarInfoImagenPreview(val);
      }
    },

    tipoEnvio(newval) {
      if (newval && !this.reenviarUnaCampaña) {
        this.selectedTemplate = null;
      }
    },


  },

  computed: {
    filasEmpresas() {
      const columnas = 3;
      const filas = [];
      for (let i = 0; i < this.listaEmpresasComercial.length; i += columnas) {
        filas.push(this.listaEmpresasComercial.slice(i, i + columnas));
      }
      return filas;
    },
    numerosManualValidos() {
      // Extrae números válidos (ej: 573001234567)
      if (!this.numerosManual) return [];
      return this.numerosManual
        .split(/[\s,;\n]+/)
        .map(n => n.trim())
        .filter(n => /^57\d{10}$/.test(n));
    },
    numerosManualInvalidos() {
      if (!this.numerosManual) return [];
      return this.numerosManual
        .split(/[\s,;\n]+/)
        .map(n => n.trim())
        .filter(n => n && !/^57\d{10}$/.test(n));
    },
    totalRegistrosEnviar() {
      // Suma los registros de filtros + manuales únicos
      const registrosFiltros = Array.isArray(this.resultados) ? this.resultados.length : 0;
      return registrosFiltros + this.numerosManualValidos.length;
    },

    resumenTotalEnvio() {
      let total = 0;
      if (this.tipoEnvio.includes('Por filtros de prospectos')) total += this.totalRegistrosBd;
      if (this.tipoEnvio.includes('Registrar números manualmente')) total += this.numerosManualValidos.length;
      return total;
    },

    nombreCampaniaDuplicado() {
      if (!this.selectedNombreCampana) return false;
      return this.publicidad.some(
        c => c.nombre?.trim().toLowerCase() === this.selectedNombreCampana.trim().toLowerCase()
      );
    },

    acceptCampanaFile() {
      if (!this.selectedTemplate) return 'image/jpeg,image/png,image/jpg,video/mp4';
      if (
        this.selectedTemplate.name === 'boletin_informativo' ||
        this.selectedTemplate.name === 'promocionar_productos_servicios'
      ) {
        return 'image/jpeg,image/png,image/jpg';
      }
      if (this.selectedTemplate.name === 'video_informativo_mp4') {
        return 'video/mp4';
      }
      return 'image/jpeg,image/png,image/jpg,video/mp4';
    },

  },

  methods: {
    descargarPlantilla() {
      // Ruta relativa al archivo dentro de "public"
      const url = '/plantilla excel.xlsx';
      const link = document.createElement('a');
      link.href = url;
      link.download = 'plantilla.xlsx'; // nombre del archivo al descargar
      link.click();
    },

    abrirImagenEnNuevaPestana(url) {
      // Si es un require(), resuelve el path real
      if (typeof url === 'object' && url.default) url = url.default;
      window.open(url, '_blank');
    },

    subirArchivoNumerosManual() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.txt,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel';
      input.onchange = (event) => {
        const file = event.target.files[0];
        if (file) {
          this.archivoNumerosManuales = file;
        }
      };
      input.click();

      // ejecutar el metodo procesarArchivoManual despues de que el archivo se haya seleccionado
      input.addEventListener('change', () => {
        this.procesarArchivoManual();
      });
    },

    async procesarArchivoManual() {
      if (!this.archivoNumerosManuales) return;

      try {
        const formData = new FormData();
        formData.append('archivo', this.archivoNumerosManuales);

        const response = await axios.post(this.baseURL + 'api/procesarArchivoNumeros', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        let numerosRaw = response.data.data;
        if (typeof numerosRaw === 'string') {
          // Paso 1: separar por coma y espacio
            let numeros = numerosRaw.split(',').map(n => n.trim());
            let numerosValidos = [];
            let numerosInvalidos = [];
            // Usamos un Set para evitar duplicados. La "key" canónica será
            // los últimos 10 dígitos cuando el valor contenga solo dígitos
            // (esto permite identificar 57XXXXXXXXXX y XXXXXXXXXX como el mismo número).
            const vistos = new Set();

            numeros.forEach(num => {
              // Paso 2: quitar todos los espacios
              let limpio = num.replace(/\s+/g, '');
              // Paso 3: quitar + si existe al inicio
              limpio = limpio.replace(/^\+/, '');

              // Construir la key canónica para deduplicar
              let key;
              if (/^\d+$/.test(limpio) && limpio.length >= 10) {
                // tomar los últimos 10 dígitos (maneja tanto 57XXXXXXXXXX como XXXXXXXXXX)
                key = limpio.slice(-10);
              } else {
                // si no es un número estándar, usar la versión limpia tal cual
                key = limpio;
              }

              // Si ya vimos esta key, saltamos para no duplicar
              if (vistos.has(key)) return;

              let numeroFormateado = '';
              // Si ya tiene formato 57XXXXXXXXXX
              if (/^57\d{10}$/.test(limpio)) {
                numeroFormateado = limpio;
              } else if (/^\d{10}$/.test(limpio)) {
                // Si tiene 10 dígitos, anteponer 57
                numeroFormateado = '57' + limpio;
              } else {
                // No válido, guardar en arreglo de inválidos (ya sin espacios y sin +)
                numerosInvalidos.push(limpio);
                vistos.add(key);
                return;
              }

              // Validar que los 3 dígitos después de 57 estén entre 300 y 399
              const prefijo = numeroFormateado.substring(2, 5);
              if (/^3\d{2}$/.test(prefijo) && Number(prefijo) >= 300 && Number(prefijo) <= 399) {
                numerosValidos.push(numeroFormateado);
              } else {
                numerosInvalidos.push(numeroFormateado);
              }

              // Marcar la key como vista para evitar duplicados posteriores
              vistos.add(key);
            });
          // Paso 4: volver a juntar válidos
          let numerosString = numerosValidos.join(', ');
          // Paso 5: asignar
          this.numerosManual = numerosString;
          this.numerosInvalidosArray = numerosInvalidos;
          if (numerosInvalidos.length > 0) {
            console.log('Números inválidos:', numerosInvalidos);
          }
        } else {
          // fallback si no es string
          this.numerosManual = response.data.data;
          this.numerosInvalidosArray = [];
        }
      } catch (error) {
        console.error('Error al procesar el archivo manual:', error);
      }
    },

    sanitizeNit() {
      // quita todo lo que NO sea dígito
      const soloDigitos = this.nit.replace(/\D+/g, '')
      if (soloDigitos !== this.nit) {
        this.nit = soloDigitos
      }
    },

    esCorreoValido(correo) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(correo);
    },

    esUrlValida(url) {
      const regex = /^(https?:\/\/)?([\w.-]+)+(:\d+)?(\/[\w./#-]*)*\/?$/;
      return regex.test(url);
    },

    obtenerEmpresas() {
      axios.post(this.baseURL + 'api/cargarpp', {
        'idusu': this.comercialId,
      })
        .then(response => {
          this.listaEmpresas = response.data.data;
          this.listaEmpresas2 = response.data.data;
          this.listaEmpresasComercial = response.data.data;
          this.listaEmpresasComercial2 = response.data.data;
        })
        .catch(error => {
          console.error('Error al cargar empresas:', error)
        })
    },

    validarNit(nit) {

      axios.post(this.baseURL + 'api/validarnitraz', {
        'nit': nit,
        'raz': '',
      })
        .then(response => {
          if (response.data.data != '') {
            this.mensajeAlertaNit = 'Esta empresa ya se encuentra asignada a: ' + response.data.data[0].comercial;
            this.dsGuardar = true;
            this.alertaNit = true;
          } else {
            this.alertaNit = false;
            this.mensajeAlertaNit = '';
            this.dsGuardar = false;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    validarRazonSocial(newRazonSocial) {

      axios.post(this.baseURL + 'api/validarnitraz', {
        'nit': '',
        'raz': newRazonSocial,
      })
        .then(response => {
          if (response.data.data != '') {
            this.mensajeAlertaRazonSocial = 'Esta empresa ya se encuentra asignada a: ' + response.data.data[0].comercial;
            this.dsGuardar = true;
            this.alertaRazonSocial = true;
          } else {
            this.alertaRazonSocial = false;
            this.mensajeAlertaRazonSocial = '';
            this.dsGuardar = false;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    validarCelular(newCelular) {

      axios.post(this.baseURL + 'api/validarcel', {
        'id': this.idProspectoSeleccionado ? this.idProspectoSeleccionado : 0,
        'cel': newCelular,
      })
        .then(response => {
          console.log('Validación de celular:', response.data);
          if (response.data.data[0].res == 1) {
            this.mensajeAlertaCelular = 'Este número de celular ya se encuentra asignado a otro contacto';
            this.alertaCelular = true;
          } else {
            this.alertaCelular = false;
            this.mensajeAlertaCelular = '';
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    cerrarDIV() {
      this.alerta = false;
    },

    getAlertStyle() {
      if (this.isMobileView == true) {
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
          width: '75%'
        };
      } else {
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
      }
    },

    async guardarDatos() {

      var contacto = false;
      // if (!this.nombre || !this.apellido || !this.cargo || !this.correoContacto || !this.celular || !this.extension) {
      // Valida los campos del contacto que son obligatorios
      if (!this.razonSocial) {
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
      else if (this.nombre && this.apellido) {
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
              this.refrescar();
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
          this.refrescar();
        }, 600);
      }
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

    verificarEmpresa(id) {

      axios.post(this.baseURL + 'api/empcomer', {
        'idemp': id,
        'idcom': this.idUsuario,
      })
        .then(response => {
          if (response.data.data != '') {
            this.mensajeAlerta = response.data.data;
            this.alertaProspecto = true;
            this.dsCrear = true;
          }
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

    llamadoFiltrosDestinatarios() {

      axios.get(this.baseURL + 'api/cargarfiltrosDestinatarios')
        .then(response => {
          this.filtrosDefinidos = response.data.data;
          this.opcionesFiltros = this.filtrosDefinidos.map(fd => fd.nombre);
          console.log("FILTROS DESTINATARIOS", this.filtrosDefinidos);
        })
        .catch(error => {
          console.log(error);
        });
    },

    cargarareascomerciales() {
      axios.get(this.baseURL + 'api/cargarareascomerciales')
        .then(response => {
          console.log("Áreas comerciales cargadas:", response.data.data);
          this.areasVentas = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    cargarcomerciales(idac) {
      console.log("Área de ventas seleccionada:", idac);
      axios.post(this.baseURL + 'api/cargarcomerciales', {
        'idac': idac,
      })
        .then(response => {
          console.log("Comerciales cargados:", response.data.data);
          this.comerciales = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    abrirFormularioProspecto() {
      this.llamadoEmpresas();
      this.llamadoTipoIdentificacion();
      this.llamadoSectores();
      this.llamadoTipoEmpresa();
      this.llamadoDepartamentos();
      this.llamadoCategorias();
      this.formularioProspecto = true;
      this.prospecto = null;
    },

    refrescar() {
      this.datosIniciales();
    },


    async datosIniciales() {
      this.comercialId = localStorage.getItem('idUsuario'); // ID del usuario comercial
      this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin'); // Nombre del usuario comercial
      this.ctaMetaMensual = 0;
      this.ctaProspecto = 0;
      this.ctaEnProceso = 0;
      this.ctaCotizados = 0;
      this.ctaGanado = 0;
      this.tareas = 0;
      this.estados.forEach(estado => {
        estado.cantidad = 0;
        estado.total = 0;
        estado.items = [];
      });
      console.log("Datos Iniciales Cargados");
      console.log(this.estados);
      var fecini = this.fechaInicio;
      var fecfin = this.fechaFin;

      console.log("Fecha Inicio: " + this.fechaInicio);
      console.log("Fecha Fin: " + this.fechaFin);

      if (!this.fechaInicio || !this.fechaFin) {
        fecini = '';
        fecfin = '';
      }

      console.log("Fecha Inicio: " + fecini);
      console.log("Fecha Fin: " + fecfin);
      console.log("Empresa Seleccionada: ", this.empresaSeleccionada ? this.empresaSeleccionada.id : 0);
      console.log("Producto Seleccionado: ", this.productoSeleccionado ? this.productoSeleccionado.id : 0);



      // Actualizar los items de cada estado
      await axios.post(this.baseURL + 'api/cargarlisest', {
        'fecini': fecini, //this.fecha,
        'fecfin': fecfin, //this.fecha,
        'idprosp': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
        'idserv': this.productoSeleccionado ? this.productoSeleccionado.id : 0,
        'idusu': this.comercialId,
      })
        .then(response => {
          const data = response.data.data;
          console.log("Inicio", this.inicio);
          this.inicio++;
          console.log(data);
          data.forEach(item => {
            const estadoIndex = item.idest - 1; // Ajustamos índice (estado 1 → index 0, etc.)
            if (estadoIndex == 0) {
              this.ctaProspecto = item.total_por_estado;
              this.estados[0].cantidad = item.total_por_estado;
              this.tareas = item.pendt;

            } else if (estadoIndex == 1) {
              this.ctaEnProceso = item.total_por_estado;
              this.estados[1].cantidad = item.total_por_estado;
              this.tareas = item.pendt;
            } else if (estadoIndex == 2) {
              this.ctaCotizados = item.total_por_estado;
              this.estados[2].cantidad = item.total_por_estado;
              this.tareas = item.pendt;
            } else if (estadoIndex == 3) {
              this.ctaGanado = item.total_por_estado;
              this.estados[3].cantidad = item.total_por_estado;
              this.tareas = item.pendt;

            } else if (estadoIndex == 4) {
              this.estados[4].cantidad = item.total_por_estado;
              this.tareas = item.pendt;

            }

            this.ctaMetaMensual = item.meta;

            console.log("IDmedio", this.idmedio)

            if (this.estados[estadoIndex]) {

              this.estados[estadoIndex].items.push({
                idproccom: item.idproc,
                idcli: item.idprosp,
                nombre: item.razon_social,
                producto: item.nomserv ? item.nomserv : 'Sin Producto',
                fecha: item.fecha_act,
                valor: item.valorproy,
                idestado: item.idest,
                telefono: item.telprosp,
                contacto: item.nomcontacto,
                celular: item.nomcelu,
                direccion: item.direccion,
                ciudad: item.nomciudad,
                departamento: item.nomdpto,
                medio: item.medio,
              });
            }

          });
          //this.empresaSeleccionada = response.data.data; // Seleccionar la primera empresa por defecto
        })
        .catch(error => {
          console.log(error);
        });



      // Calcular totales por estado
      for (const estado of this.estados) {
        //estado.total = estado.items.reduce((sum, item) => sum + (item.valor || 0), 0);        
        estado.total = estado.items.reduce((sum, item) => sum + (item.valor || 0), 0);
      }

      //this.ctaAcumulado = this.estados.reduce((sum, estado) => sum + estado.total, 0); // Acumulado de todos los estados
      const cotiztot = this.estados[this.estados.length - 3]?.total || 0; // Último estado total - Estado cotizado
      const ganadotot = this.estados[this.estados.length - 2]?.total || 0; // Último estado total - Estado ganado
      this.ctaAcumulado = cotiztot + ganadotot;
      if (ganadotot == 0 && this.ctaMetaMensual == 0) {
        this.progress = 0;
      } else if (ganadotot == 0) {
        this.progress = 0;
      } else {
        this.porcMetaMensual = ((ganadotot / this.ctaMetaMensual));
        this.progress = this.porcMetaMensual * 100;
      }
    },

    async cargaProspEst(idestado, nombre) {
      this.comercialId = localStorage.getItem('idUsuario'); // ID del usuario comercial
      this.estadoactual = nombre; // Nombre del estado actual
      this.itemsListProspEst = [];
      var fecini = this.fechaInicio;
      var fecfin = this.fechaFin;


      if (!this.fechaInicio || !this.fechaFin) {
        fecini = '';
        fecfin = '';
      }

      // Actualizar los items de cada estado
      await axios.post(this.baseURL + 'api/cargarlispropest', {
        'fecini': fecini, //this.fecha,
        'fecfin': fecfin, //this.fecha,
        'idprosp': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
        'idserv': this.productoSeleccionado ? this.productoSeleccionado.id : 0,
        'idest': idestado,
        'idusu': this.comercialId,

      })
        .then(response => {
          this.itemsListProspEst = response.data.data;
          console.log(this.itemsListProspEst);
        })
        .catch(error => {
          console.log(error);
        });
      this.dialogListProspEst = true;
    },



    cargarClientesActividad() {
      axios.post(this.baseURL + 'api/cargarpp', {
        'idusu': localStorage.getItem('idUsuario'),
      })
        .then(response => {
          this.selectClientesActividad = response.data.data;
          this.selectClientesOportunidad = response.data.data;
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
    },

    cargarEstadosActividad() {
      axios.get(this.baseURL + 'api/cargares')
        .then(response => {
          this.selectEstadosActividad = response.data.data;
        })
        .catch(error => {
          console.log(response.data[0].error);
        });
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

    limpiarCamposDialogActividad() {
      this.selectedClienteActividad = null;
      this.cbLlamadaRealizada = false;
      this.cbVisitaPresencial = false;
      this.cbActivacionDemo = false;
      this.cbCorreoEnviado = false;
      this.cbVisitaVirtual = false;
      this.cbCotizacion = false;

      this.selectedObservacionesActividad = null;

      this.selectedEstadoActividad = null;

      this.proximoSeguimientoActividad = null;

      this.cbLlamar = false;
      this.cbVisitarPresencial = false;
      this.cbActivarDemo = false;
      this.cbEnviarCorreo = false;
      this.cbVisitarVirtual = false;
      this.cbCotizar = false;

      this.selectedServicioActividad = null;
      this.selectedValorProyecto = null;

      this.archivoRUT = null;
      this.archivosActividad = [];

      this.selectedComentariosActividad = null;
    },

    limpiarCamposDialogOportunidad() {
      this.selectedClienteOportunidad = null;
      this.selectedServicioOportunidad = null;
      this.selectedValorProyectoOportunidad = 0;
      this.selectedObservacionesOportunidad = null;
    },

    async registrarOportunidad() {
      const isValid = this.selectedClienteOportunidad && this.selectedObservacionesOportunidad;

      if (!isValid) {
        this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos.';
        this.alerta = true;
        return;
      }

      let data = {
        idcliente: this.selectedClienteOportunidad.id,
        idservicio: this.selectedServicioOportunidad ? this.selectedServicioOportunidad.id : 0,
        valor_proy: this.selectedValorProyectoOportunidad ? this.selectedValorProyectoOportunidad : 0,
        observacion: this.selectedObservacionesOportunidad,
        idmedio: 1,
        idcom: localStorage.getItem('idUsuario'),
        idcampania: 0,
      };
      console.log('Datos de la oportunidad:');
      console.log(data);

      await axios.post(this.baseURL + 'api/newproccom', data)
        .then(response => {
          this.dialogNuevaOportunidad = false;
          this.limpiarCamposDialogOportunidad();
          this.cargarClientesActividad();
          this.cargarEstadosActividad();

          this.dialogNuevaActividad = false;

          console.log('Oportunidad registrada:', response.data.data);

          this.mensajeAlertLogin = 'La oportunidad se ha registrado correctamente.';
          this.alerta = true;
          this.datosIniciales();
        })
        .catch(error => {
          console.error('Error al registrar la oportunidad:', error);
        });
    },

    registrarActividad() {
      let cbCotizacion = this.cbCotizacion;

      const isValid1 = this.selectClientesActividad && this.idActividad !== null && this.selectedObservacionesActividad && this.selectedEstadoActividad;

      const isValid2 = this.selectClientesActividad && this.idActividad !== null && this.selectedEstadoActividad && this.selectServiciosActividad && this.selectedValorProyecto && this.archivoRUT !== null && this.selectedComentariosActividad;
      if (cbCotizacion) {

        if (!isValid2) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos.';
          this.alerta = true;
          return;
        }
      } else {
        if (!isValid1) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos';
          this.alerta = true;
          return;
        }

      }
      let formData = new FormData();
      formData.append('procom', this.idOportunidad);
      formData.append('cli', this.selectedClienteActividad.id);
      formData.append('act', this.idActividad);
      formData.append('obs', this.selectedObservacionesActividad);
      formData.append('estado', this.selectedEstadoActividad.id);
      formData.append('fpseg', this.proximoSeguimientoActividad ? this.proximoSeguimientoActividad : '');
      formData.append('idseg', this.idSeguimiento ? this.idSeguimiento : 0);
      formData.append('idmedio', 1);
      formData.append('file', this.archivoRUT);
      axios.post(this.baseURL + 'api/newproccomact', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => {
        this.dialogNuevaActividad = false;
        this.limpiarCamposDialogActividad();
        this.cargarClientesActividad();
        this.cargarEstadosActividad();

        console.log('Actividad registrada:', response.data.data);

        setTimeout(() => {
          this.mensajeAlertLogin = 'La actividad se ha registrado correctamente.';
          this.alerta = true;
        }, 600);
      })
        .catch(error => {
          console.error('Error al registrar la actividad:', error);
        });

    },

    abrirNuevaActividad(actividad) {
      localStorage.setItem('idproccom', actividad.idproc);
      localStorage.setItem('idempresa', actividad.idemp);
      localStorage.setItem('razon_soc', actividad.razon_social);
      localStorage.setItem('idestado', actividad.idest);

      this.$router.push('/pendiente');

    },

    // Cambios Angelo

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
          console.log('Prospecto actualizado:', response.data);
          this.ifCargando = false;
          this.alerta = true;
          this.mensajeAlertLogin = 'Prospecto actualizado correctamente';
          setTimeout(() => {
            this.obtenerEmpresas();
            this.limpiarCamposProspecto();
            this.dialogCrearEditarProspecto = false;
            this.dialogProspectos = true;
          }, 1000);
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

    cerrarSesion() {
      localStorage.removeItem('idUsuario')
      localStorage.removeItem('idCargo')
      localStorage.removeItem('nombreLogin')
      localStorage.removeItem('apellidoLogin')
      localStorage.removeItem('celularLogin')
      localStorage.removeItem('logueado')
      this.$router.push('/')
    },

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

    irProspeccionTelefonica() {
      this.$router.push('/prospeccion-telefonica');
    },

    irSeguimientoLlamadas() {
      this.$router.push('/seguimiento-llamadas');
    },

    irGaleriaCampanas() {
      this.$router.push('/VerCampanas');
    },

    irEmpresas() {
      this.$router.push('/empresas');
    },

    irContactos() {
      this.$router.push('/contactos');
    },

    cargarMetaUsu() {
      var data = { id: this.idUsuario };

      axios.post(this.baseURL + 'api/cargarMetaUsu', data)
        .then(response => {
          this.ctaMetaMensual = response.data.data[0].meta;
        })
        .catch(error => {
          console.error('Error al cargar empresas:', error)
        })
    },
    //-------------------------- METODOS DE LA VISTA CAMPAÑA-------------------------


    async loadTemplates() {
      const { data } = await axios.get('https://siicsa-glpiwhbe.azurewebsites.net/messages_templates');
      const nombresDeseados = ['boletin_informativo', 'promocionar_productos_servicios', 'video_informativo_mp4'];
      this.templates = data.filter(item => nombresDeseados.includes(item.name));
      console.log("TEMPLATES: ", this.templates);
    },

    formatTemplate() {
      this.header = null
      this.body = null
      this.footer = null
      this.buttons = null

      this.templates.forEach((element) => {
        if (element.name === this.selectedTemplate.name) {
          this.template = element
          /*element.components.forEach((data) => {
              if (data.type === 'HEADER') this.header = data 
              else if (data.type === 'BODY') {
                  this.body = data.text
                  this.body_placeholders = this.findPlaceholders(data.text)
              } else if (data.type === 'FOOTER')
                  this.footer = data.text
              else if (data.type === 'BUTTONS')
                  this.buttons = data.buttons
          })*/
        }

      })
      console.log("Empieza")
      console.log(this.template)
      console.log(this.header)
      console.log(this.body)
      console.log(this.footer)
      console.log(this.buttons)
      console.log(this.body_placeholders)
    },

    async send() {
      this.dialogConfirmarEnvio = false;
      this.dialogAvisoEnvio = false;

      const enviarPorFiltros = this.tipoEnvio.includes('Por filtros de prospectos');
      const enviarPorManual = this.tipoEnvio.includes('Registrar números manualmente');
      const numerosManualValidos = this.numerosManualValidos;


      if (this.reenviarUnaCampaña) {
        if (!this.campnom || !this.selectedTemplate) {
          this.tipoAvisoEnvio = 'warning';
          this.mensajeAvisoEnvio = "No se encontró la campaña o la plantilla para reenviar.";
          this.dialogAvisoEnvio = true;
          return;
        }

      } else {

        if (!this.selectedImagenCampana) {
          this.mensajeAvisoEnvio = 'Por favor seleccione una imagen para la campaña.';
          this.tipoAvisoEnvio = 'warning';
          this.dialogAvisoEnvio = true;
          return;
        }
        if (!this.selectedTemplate) {
          this.tipoAvisoEnvio = 'warning';
          this.mensajeAvisoEnvio = "Por favor seleccione una plantilla";
          this.dialogAvisoEnvio = true;
          return;
        }
        if (!this.selectedNombreCampana || !this.selectedDetalleCampana || !this.selectedImagenCampana) {
          this.tipoAvisoEnvio = 'warning';
          this.mensajeAvisoEnvio = "Por favor complete todos los campos de la campaña";
          this.dialogAvisoEnvio = true;
          return;
        }


        this.cargandoCampania = true;
        this.progresoCampania = 0;
        await this.GuardarFormularioCampaña();
        this.selectedNombreCampana = null;
        this.selectedDetalleCampana = null;
        this.selectedImagenCampana = null;
      }

      const formData = new FormData();
      formData.append('campid', this.campnom.id);
      formData.append('campnom', this.campnom.nombre);
      formData.append('template', this.selectedTemplate.name);
      formData.append('idusu', localStorage.getItem('idUsuario'));
      formData.append('archivo', this.campnom.url_media || '');

      // Construye el objeto de filtros dinámicos
      let filtrosEnvioObj = {};
      if (enviarPorFiltros) {
        this.filtrosDefinidos.forEach(fd => {
          const valor = this.filtrosEnvio[fd.id];
          filtrosEnvioObj[fd.id] = (valor !== null && valor !== undefined && valor !== '') ? valor : 0;
        });
        formData.append('filtrosEnvio', JSON.stringify(filtrosEnvioObj));
      } else {
        this.filtrosDefinidos.forEach(fd => {
          filtrosEnvioObj[fd.id] = 0;
        });
        formData.append('filtrosEnvio', JSON.stringify(filtrosEnvioObj));
        formData.append('soloManual', 'true');
      }

      // Números manuales
      if (enviarPorManual && numerosManualValidos.length > 0) {
        formData.append('numerosManual', numerosManualValidos.join(','));
      }

      axios.post(this.baseURL + 'api/envia_campania', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(response => {
          const mensaje = response.data.data;
          if (mensaje.includes("Los siguientes números")) {
            alert("⚠️ Atención: " + mensaje);
          } else {
            this.mensajeAlertLogin = 'Campaña Creada y Enviada Exitosamente.';
            this.alerta = true;
            this.validandoActividad = false;
            this.campnom = null;
            location.reload();
          }
          this.progresoCampania = 100;
          this.cargandoCampania = false;
        })
        .catch(error => {
          console.error(error);
          this.cargandoCampania = false;
          this.progresoCampania = 0;
          alert('Hubo un error al enviar la campaña: \nPor favor comunicate con el administrador del sistema');
        });
    },

    sendSoloManual() {
      if (!this.numerosManualValidos.length) {
        alert('No hay números válidos para enviar.');
        return;
      }
      if (this.selectedTemplate == null || this.selectedTemplate == '') {
        alert('Por favor seleccione una plantilla');
        return;
      }
      if (this.campnom == null || this.campnom == '') {
        alert('Por favor seleccione una campaña');
        return;
      }

      const formData = new FormData();
      formData.append('campid', this.campnom.id);
      formData.append('campnom', this.campnom.nombre);
      formData.append('template', this.selectedTemplate.name);
      formData.append('idusu', localStorage.getItem('idUsuario'));
      // Envía un flag especial
      formData.append('soloManual', 'true');
      // Envía los filtros en -1 para que el backend los ignore
      formData.append('filtroSector', -1);
      formData.append('filtroEmpresa', -1);
      formData.append('filtroCatCargo', -1);
      formData.append('filtroCargo', -1);
      formData.append('filtroDpto', -1);
      formData.append('filtroCiudad', -1);
      formData.append('numerosManual', this.numerosManualValidos.join(','));

      // Adjunta archivo si aplica
      if (this.selectedTemplate.name == 'boletin_informativo') {
        formData.append('archivo', this.header_img);
      } else if (this.selectedTemplate.name == 'video_informativo_mp4') {
        formData.append('archivo', this.header_vid);
      } else if (this.selectedTemplate.name == 'promocionar_productos_servicios') {
        formData.append('archivo', this.header_img);
      }

      axios.post(this.baseURL + 'api/envia_campania', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(response => {
          const mensaje = response.data.data;
          if (mensaje.includes("Los siguientes números")) {
            alert("⚠️ Atención: " + mensaje);
          } else {
            alert("✅ " + mensaje);
            location.reload();
          }
        })
        .catch(error => {
          console.error(error);
          alert('Hubo un error al enviar la campaña: \nPor favor comunicate con el admnistrador del sistema');
        });
    },

    async cargarDatos() {
      console.log("Entra a cargar datos");

      const idsectorFiltro = this.filtrosBD.idsector?.id || 0;
      const idempresaFiltro = this.filtrosBD.idempresa?.id || 0;
      const idcatcargoFiltro = this.filtrosBD.idcatcargo?.id || 0;
      const idcargoFiltro = this.filtrosBD.idcargo?.id || 0;
      const iddptoFiltro = this.filtrosBD.iddpto?.id || 0;
      const idciudadFiltro = this.filtrosBD.idciudad?.id || 0;

      let formData = new FormData();
      formData.append('idsector', idsectorFiltro);
      formData.append('idempresa', idempresaFiltro);
      formData.append('idcatcargo', idcatcargoFiltro);
      formData.append('idcargo', idcargoFiltro);
      formData.append('iddpto', iddptoFiltro);
      formData.append('idciudad', idciudadFiltro);

      const res = await axios.post(this.baseURL + 'api/cargardatosfiltcamp', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      console.log("RES: ", res)

      this.resultados = Array.isArray(res.data.data) ? res.data.data : [];
      this.totalRegistrosBd = this.resultados.length;

      if (this.resultados.length > 0) {
        this.itemsSector = await this.extraerUnicos('idsector', 'nombresector');
        this.itemsEmpresa = await this.extraerUnicos('idempresa', 'nombreempresa');
        this.itemsCatCargo = await this.extraerUnicos('idcategoriacargo', 'nombrecategoriacargo');
        this.itemsCargo = await this.extraerUnicos('idcargo', 'nombrecargo');
        this.itemsDpto = await this.extraerUnicos('iddpto', 'nombredpto');
        this.itemsCiudad = await this.extraerUnicos('idciudad', 'nombreciudad');
      } else if (
        !this.filtrosBD.idsector &&
        !this.filtrosBD.idempresa &&
        !this.filtrosBD.idcatcargo &&
        !this.filtrosBD.idcargo &&
        !this.filtrosBD.iddpto &&
        !this.filtrosBD.idciudad
      ) {
        // ✅ Si todos los filtros están vacíos, recargo los filtros base
        await this.cargarFiltroSector();
        await this.cargarFiltroEmpresa();
        await this.cargarFiltroCatCargo();
        await this.cargarFiltroCargo();
        await this.cargarFiltroDepartamento();
        await this.cargarFiltroCiudad();
      } else {
        // ❌ Solo limpio si sí hay filtros activos y no se encontraron resultados
        this.itemsSector = [];
        this.itemsEmpresa = [];
        this.itemsCatCargo = [];
        this.itemsCargo = [];
        this.itemsDpto = [];
        this.itemsCiudad = [];
      }
      console.log("This.Dpto:", this.itemsDpto);
      console.log("This.ciudad: ", this.itemsCiudad);
    },

    extraerUnicos(idKey, nombreKey) {
      const mapa = new Map();
      this.resultados.forEach(item => {
        if (item[idKey] && !mapa.has(item[idKey])) {
          mapa.set(item[idKey], { id: item[idKey], nombre: item[nombreKey] });
        }
      });
      return Array.from(mapa.values());
    },

    async cargarPublicidad() {
      try {
        const response = await axios.get(this.baseURL + 'api/cargarCampanas');
        this.publicidad = response.data.data;
        console.log("PUBLICIDAD: ", this.publicidad);
      } catch (error) {
        console.log(error);
      }
    },

    cargarFiltroSector() {
      axios.get(this.baseURL + 'api/cargarse')
        .then(response => {
          this.itemsSector = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    cargarFiltroEmpresa() {
      axios.get(this.baseURL + 'api/cargarEm')
        .then(response => {
          this.itemsEmpresa = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    cargarFiltroCatCargo() {
      axios.get(this.baseURL + 'api/cargarCatCargo')
        .then(response => {
          this.itemsCatCargo = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    cargarFiltroCargo() {
      axios.get(this.baseURL + 'api/cargarCargo')
        .then(response => {
          this.itemsCargo = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    cargarFiltroDepartamento() {
      axios.get(this.baseURL + 'api/cargarDep')
        .then(response => {
          this.itemsDpto = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    cargarFiltroCiudad() {
      axios.get(this.baseURL + 'api/cargarCiudad')
        .then(response => {
          this.itemsCiudad = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    limpiarFiltros() {
      this.filtrosBD.idsector = null;
      this.filtrosBD.idempresa = null;
      this.filtrosBD.iddpto = null;
      this.filtrosBD.idciudad = null;
      this.filtrosBD.idcatcargo = null;
      this.filtrosBD.idcargo = null;
      this.cargarDatos();
    },

    findPlaceholders(text) {
      const regexp = /{{(.*?)}}/g
      const exec = text.matchAll(regexp)
      const matches = []

      for (const match of exec) {
        matches.push({ text: match[0], value: '' })
      }
      return matches
    },

    handleFileUpload(type) {
      const file = type === 'IMAGE' ? this.header_img : type === 'VIDEO' ? this.header_vid : this.header_doc;

      if (file) {
        // Limitar tamaño a 14 MB (14 * 1024 * 1024 bytes)
        const maxSize = 14 * 1024 * 1024;
        if (file.size > maxSize) {
          this.mensajeArchivoGrande = 'El archivo debe ser menor o igual a 14 MB.';
          this.alertaArchivoGrande = true;
          // Limpiar el input
          if (type === 'IMAGE') {
            this.header_img = null;
          } else if (type === 'VIDEO') {
            this.header_vid = null;
          }
          return;
        }

        if (type === 'IMAGE') {
          this.header_img_url = URL.createObjectURL(file);
          this.header_vid_url = null;
          this.header_doc_url = null;
        } else if (type === 'VIDEO') {
          this.header_vid_url = URL.createObjectURL(file);
          this.header_img_url = null;
          this.header_doc_url = null;
        } else if (type === 'DOCUMENT') {
          this.header_doc_url = URL.createObjectURL(file);
          this.header_img_url = null;
          this.header_vid_url = null;
        }
      }
    },

    // Limpiar los archivos y las URLs cuando el input es borrado
    clearInput(type) {
      if (type === 'IMAGE') {
        this.header_img = null;
        this.header_img_url = null;
      } else if (type === 'VIDEO') {
        this.header_vid = null;
        this.header_vid_url = null;
      } else if (type === 'DOCUMENT') {
        this.header_doc = null;
        this.header_doc_url = null;
      }

      // Mostrar imagen predeterminada si no hay imagen cargada
      if (!this.header_img_url && !this.header_vid_url && !this.header_doc_url) {
        this.header_img_url = 'https://glpi-siicsa.azurewebsites.net/SIICSA.jpg'; // Restaurar la imagen predeterminada
      }
    },

    validarNumerosManual() {
      if (this.numerosManualInvalidos.length) {
        return `Hay ${this.numerosManualInvalidos.length} número(s) inválido(s).`;
      }
      return true;
    },

    cerrarFormularioCampaña() {
      this.dialogCrearCampaña = false;
      this.selectedNombreCampana = null;
      this.selectedDetalleCampana = null;
      this.selectedGuionCampaña = null;
      this.selectedImagenCampana = null;
      this.validandoActividad = false;
    },

    async GuardarFormularioCampaña() {
      this.validandoActividad = true;

      if (!this.selectedNombreCampana?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el nombre de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      const nombreExiste = this.publicidad.some(
        c => c.nombre?.trim().toLowerCase() === this.selectedNombreCampana.trim().toLowerCase()
      );
      if (nombreExiste) {
        this.mensajeAlertLogin = 'Ya existe una campaña con ese nombre. Por favor, elige otro.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (!this.selectedDetalleCampana?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el detalle de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (!this.selectedImagenCampana) {
        this.mensajeAlertLogin = 'Por favor, Seleccione una imagen para la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      try {
        // 1. Crear la campaña
        const response = await axios.post(this.baseURL + '/api/CrearCampania', {
          'nombre': this.selectedNombreCampana,
          'detalle': this.selectedDetalleCampana,
          'guion': this.selectedGuionCampaña || '',
          'idusu': localStorage.getItem('idUsuario'),
          'canal': 1,
          'idCampania': 0,
          'tipo': 0,
          'url_media': '',
          'age': this.selectedComerciales.map(c => c.id).join(','),
        });
        this.progresoCampania = 40;

        // 2. Subir la imagen
        const idCampania = response?.data?.data?.[0]?.id || response?.data?.data?.[0]?.idCampania;
        if (this.selectedImagenCampana && idCampania) {
          const formImage = new FormData();
          formImage.append('files', this.selectedImagenCampana);
          formImage.append('id', idCampania);

          await axios.post(this.baseURL + '/api/uploadfileblobMediaCampania', formImage, {
            headers: { 'Content-Type': 'multipart/form-data' },
          });
        }

        // 3. Recargar la publicidad y asignar el nuevo ítem
        this.progresoCampania = 100;
        await this.cargarPublicidad();
        const nuevoItem = this.publicidad.find(
          c => c.nombre?.trim().toLowerCase() === this.selectedNombreCampana.trim().toLowerCase()
        );
        if (nuevoItem) {
          this.campnom = nuevoItem;
        }

      } catch (error) {
        this.cargandoCampania = false;
        this.progresoCampania = 0;
        console.error('Error al crear campaña:', error);
        this.mensajeAlertLogin = 'Error al crear la campaña.';
        this.alerta = true;
        this.validandoActividad = false;
      }
    },

    irCrearCampanas() {
      this.dialogCrearCampaña = true;
    },

    onImagenCampanaChange(e) {
      const file = e.target.files ? e.target.files[0] : e;
      if (!file) return;

      // Define los tipos permitidos según el template
      let tiposPermitidos = [];
      if (
        this.selectedTemplate &&
        (this.selectedTemplate.name === 'boletin_informativo' ||
          this.selectedTemplate.name === 'promocionar_productos_servicios')
      ) {
        tiposPermitidos = ['image/jpeg', 'image/png', 'image/jpg', 'image/webp', 'image/gif'];
      } else if (
        this.selectedTemplate &&
        this.selectedTemplate.name === 'video_informativo_mp4'
      ) {
        tiposPermitidos = ['video/mp4', 'video/webm', 'video/ogg', 'video/mov', 'video/avi', 'video/mkv'];
      } else {
        tiposPermitidos = ['image/jpeg', 'image/png', 'image/jpg', 'video/mp4'];
      }

      // Validación estricta del tipo
      if (!tiposPermitidos.includes(file.type)) {
        this.mensajeAlertLogin = 'El archivo seleccionado no es válido para esta plantilla.';
        this.alerta = true;
        this.selectedImagenCampana = null;
        this.previewImagenCampana = '';
        this.previewVideoCampana = null;
        return;
      }

      // Validación de tamaño
      if (file.size > 14 * 1024 * 1024) {
        this.mensajeAlertLogin = 'El archivo debe ser menor a 14MB.';
        this.alerta = true;
        this.selectedImagenCampana = null;
        this.previewImagenCampana = '';
        this.previewVideoCampana = null;
        return;
      }

      this.selectedImagenCampana = file;
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (ev) => {
          this.previewImagenCampana = ev.target.result;
          this.previewVideoCampana = null;
        };
        reader.readAsDataURL(file);
      } else if (file.type.startsWith('video/')) {
        this.previewVideoCampana = URL.createObjectURL(file);
        // Opcional: genera un poster del primer frame
        const video = document.createElement('video');
        video.preload = 'metadata';
        video.muted = true;
        video.src = this.previewVideoCampana;
        video.onloadeddata = () => {
          const canvas = document.createElement('canvas');
          canvas.width = video.videoWidth;
          canvas.height = video.videoHeight;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
          this.previewImagenCampana = canvas.toDataURL('image/png');
          URL.revokeObjectURL(video.src);
        };
        video.onerror = () => {
          this.previewImagenCampana = '';
          URL.revokeObjectURL(video.src);
        };
      }
    },

    esVideo(val) {
      if (!val) return false;
      // Si es un File, revisa el tipo
      if (typeof val === 'object' && val.type) return val.type.startsWith('video/');
      // Si es string (url o nombre), revisa la extensión
      return /\.(mp4|webm|ogg|mov|avi|mkv)(\?|$)/i.test(val);
    },

    cerrarAvisoEnvio() {
      this.dialogAvisoEnvio = false;
      // limpiar listas estructuradas al cerrar el diálogo
      this.invalidFromResultadosDisplay = [];
      this.invalidFromManualDisplay = [];
      if (this.tipoAvisoEnvio === 'success') {
        location.reload();
      }
    },


    imagenAmpliadaUrlCampana(val) {
      if (this.dialogImagenAmpliadaCampana && val) {
        this.cargarInfoImagenPreview(val);
      }
    },

    abrirImagenAmpliada(url) {
      console.log("DEBERÏA ABRIRSE EL DIALOGO")
      this.imagenAmpliadaUrlCampana = url;
      this.dialogImagenAmpliadaCampana = true;
      this.imagenAmpliadaUrlCampana = url || (this.campnom?.url_media || 'https://glpi-siicsa.azurewebsites.net/SIICSA.jpg');
      this.dialogImagenAmpliadaCampana = true;
    },

    abrirImagenEnNuevaPestana(url) {
      if (url) window.open(url, '_blank');
    },

    cargarInfoImagenPreview(url) {
      if (!url) {
        this.infoImagenPreview = null;
        return;
      }
      const img = new window.Image();
      img.onload = () => {
        let format = '';
        if (url.startsWith('blob:')) {
          format = 'Desconocido';
        } else {
          const ext = url.split('.').pop().split('?')[0].toUpperCase();
          format = ['JPG', 'JPEG', 'PNG', 'WEBP', 'GIF'].includes(ext) ? ext : 'Desconocido';
        }
        this.infoImagenPreview = {
          width: img.naturalWidth,
          height: img.naturalHeight,
          format,
        };
      };
      img.onerror = () => {
        this.infoImagenPreview = {
          width: 320,
          height: 240,
          format: 'Desconocido',
        };
      };
      img.src = url;
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

    abrirConfirmacionEnvio() {
      // Si es reenvío, solo valida que existan los objetos requeridos
      if (this.reenviarUnaCampaña) {
        if (!this.campnom || !this.selectedTemplate) {
          this.tipoAvisoEnvio = 'warning';
          this.mensajeAvisoEnvio = "No se encontró la campaña o la plantilla para reenviar.";
          this.dialogAvisoEnvio = true;
          return;
        }
      } else {
        // Validación para nueva campaña
        if (!this.selectedComerciales) {
          this.tipoAvisoEnvio = 'warning';
          this.mensajeAvisoEnvio = "Por favor asigne Agente(s) para esa Campaña.";
          this.dialogAvisoEnvio = true;
          return;
        }
        if (!this.selectedImagenCampana) {
          this.mensajeAvisoEnvio = 'Por favor seleccione una imagen para la campaña.';
          this.tipoAvisoEnvio = 'warning';
          this.dialogAvisoEnvio = true;
          return;
        }
        if (!this.selectedNombreCampana || !this.selectedDetalleCampana) {
          this.tipoAvisoEnvio = 'warning';
          this.mensajeAvisoEnvio = "Por favor complete todos los campos de la campaña";
          this.dialogAvisoEnvio = true;
          return;
        }
        if (this.resumenTotalEnvio == 0) {
          this.tipoAvisoEnvio = 'warning';
          this.mensajeAvisoEnvio = "No hay números para enviar la campaña. Por favor ajuste los filtros o ingrese números manualmente.";
          this.dialogAvisoEnvio = true;
          return;
        }
      }

      let telefonosParaValidar = [];

      this.numerosManualValidos.forEach(num => {
        telefonosParaValidar.push(num);
      });

      if (this.tipoEnvio.includes('Por filtros de prospectos')) {
        // Agregar números desde this.resultados
        this.resultados.forEach(item => {
          if (item.celular && !telefonosParaValidar.includes(item.celular)) {
            telefonosParaValidar.push(item.celular);
          }
        });
      }

      this.dialogAvisoEnvio = true;
      this.ifCargando = true;
      this.mensajeAvisoEnvio = "Validando números para el envío de la campaña, por favor espere...";
      this.tipoAvisoEnvio = 'warning';

      axios.post(this.baseURL + 'api/validar_numeros_campania', {
        'telefonos': telefonosParaValidar
      })
        .then(response => {
          // Recorrer todo el response y buscar si al menos 1 resultado tiene novalido = 1
          const resultados = response.data.data || [];
          const invalidItems = resultados.filter(item => Number(item.novalido) === 1 || item.novalido === '1');

          if (invalidItems.length > 0) {
            // Clasificar inválidos: si vienen de numerosManualValidos mostrar solo el número,
            // si vienen de this.resultados intentar obtener nombre + apellido buscando por celular
            const invalidFromManual = [];
            const invalidFromResultados = [];

            // Normalizar funciones para comparar
            const normalize = v => (v === null || v === undefined) ? '' : String(v).replace(/\s|\+|-/g, '');
            const manualSet = new Set((this.numerosManualValidos || []).map(n => normalize(n)));

            // Helper para intentar extraer nombre + apellido de un item de this.resultados
            const extractNameFromResultado = (resItem) => {
              if (!resItem) return null;
              // Try common fields in order
              const firstCandidates = [
                (resItem.pc_nombre && resItem.pc_apellido) ? `${resItem.pc_nombre} ${resItem.pc_apellido}` : null,
                (resItem.nombre && resItem.apellido) ? `${resItem.nombre} ${resItem.apellido}` : null,
                (resItem.nombres && resItem.apellidos) ? `${resItem.nombres} ${resItem.apellidos}` : null,
                (resItem.nombre_contacto && resItem.apellido_contacto) ? `${resItem.nombre_contacto} ${resItem.apellido_contacto}` : null,
                (resItem.razon_social) ? `${resItem.razon_social}` : null,
              ];
              for (const c of firstCandidates) if (c && c.trim()) return c.trim();
              return null;
            };

            invalidItems.forEach(it => {
              const numero = normalize(it.numero || it.tel || it.cel || it.phone || it.telefono || it.mobile);
              if (!numero) return;

              if (manualSet.has(numero)) {
                invalidFromManual.push(numero);
              } else {
                // buscar en this.resultados por campo celular (normalizado)
                const matched = (this.resultados || []).find(r => normalize(r.celular || r.pc_celular || r.p_celular || r.cel || r.telefono) === numero);
                if (matched) {
                  const nombre = extractNameFromResultado(matched) || '';
                  const empresa = matched.nombreempresa || matched.p_nombreempresa || matched.razon_social || '';
                  if (nombre) {
                    if (empresa) invalidFromResultados.push(`${nombre} - ${empresa} (${numero})`);
                    else invalidFromResultados.push(`${nombre} (${numero})`);
                  } else if (empresa) {
                    invalidFromResultados.push(`${empresa} (${numero})`);
                  } else {
                    invalidFromResultados.push(numero);
                  }
                } else {
                  // si no encontramos registro, mostrar solo el número
                  invalidFromResultados.push(numero);
                }
              }
            });

            // Guardar listas en estado para renderizado estructurado en el diálogo
            this.invalidFromResultadosDisplay = invalidFromResultados;
            this.invalidFromManualDisplay = invalidFromManual;
            this.ifCargando = false;

            // Mensaje de fallback/encabezado (se usa solo si las listas están vacías)
            this.mensajeAvisoEnvio = 'Los siguientes números son inválidos y no pueden ser incluidos en el envío de la campaña.';
            this.tipoAvisoEnvio = 'warning';
            this.dialogAvisoEnvio = true;
            return;
          } else {
            // No hay inválidos: limpiar cualquier estado previo de inválidos
            this.invalidFromResultadosDisplay = [];
            this.invalidFromManualDisplay = [];
            this.dialogAvisoEnvio = false;
            this.ifCargando = false;
            this.mensajeAvisoEnvio = '';
            // Abre el diálogo de confirmación y deshabilita el botón por 2 segundos
            this.dialogConfirmarEnvio = true;
            this.enviandoCampania = true;
            setTimeout(() => {
              this.enviandoCampania = false;
            }, 2000);
          }
        })
        .catch(error => {
          console.error('Error al validar el envío de la campaña:', error);
          this.invalidFromResultadosDisplay = [];
          this.invalidFromManualDisplay = [];
          this.tipoAvisoEnvio = 'error';
          this.mensajeAvisoEnvio = "Hubo un error al validar el envío de la campaña. Por favor, inténtelo de nuevo más tarde.";
          this.dialogAvisoEnvio = true;
          return;
        });


    },

    obtenerItemsPorFiltro(id) {
      // Devuelve los items según el filtro (puedes usar un switch/case o un objeto)
      switch (id) {
        case 1: return this.itemsSector;
        case 2: return this.itemsEmpresa;
        case 3: return this.itemsCatCargo;
        case 4: return this.itemsCargo;
        case 5: return this.itemsDpto;
        case 6: return this.itemsCiudad;
        default: return [];
      }
    },

    actualizarFiltros() {
      // Elimina los valores de filtros que ya no están seleccionados
      const seleccionados = this.filtrosDefinidos
        .filter(fd => this.filtros.includes(fd.nombre))
        .map(fd => fd.id);

      Object.keys(this.filtrosEnvio).forEach(id => {
        if (!seleccionados.includes(Number(id))) {
          this.$set(this.filtrosEnvio, id, null);
        }
      });
    },

    getFiltroDefByNombre(nombre) {
      return this.filtrosDefinidos.find(fd => fd.nombre === nombre);
    },

    async cargarDatosBaseFiltros() {
      this.todosSectores = await axios.get(this.baseURL + 'api/cargarse').then(r => r.data.data);
      this.todasEmpresas = await axios.get(this.baseURL + 'api/cargarEm').then(r => r.data.data);
      this.todasCategoriasCargo = await axios.get(this.baseURL + 'api/cargarCatCargo').then(r => r.data.data);
      this.todosCargos = await axios.get(this.baseURL + 'api/cargarCargo').then(r => r.data.data);
      this.todosDepartamentos = await axios.get(this.baseURL + 'api/cargarDep').then(r => r.data.data);
      this.todasCiudades = await axios.get(this.baseURL + 'api/cargarCiudad').then(r => r.data.data);
    },



  },

}


</script>

<style scoped>
.float-right {
  float: right;
}

.progress-label .label-text {
  color: white;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
  font-weight: bold;
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

.celular-container {
  position: relative;
  align-items: center;
  align-content: center;
  width: 350px;
  height: 650px;
  margin-left: 25%;
}

.cabecera-chat {
  background-color: #075e54;
  color: white;
  flex-shrink: 0;
  margin-top: 12px;
}

.celular-mockup {
  width: 80%;
  height: 80%;
  object-fit: contain;
  z-index: 1;
  position: absolute;
  top: 0;
  left: 0;
  pointer-events: none;
  background-color: transparent;
}

.contenido-preview {
  width: 70%;
  height: 78%;
  position: absolute;
  top: 0px;
  left: 18px;
  right: 35px;
  bottom: 100px;
  z-index: 0;
  background-color: transparent;
}

.barra-input {
  background-color: white;
}




.chat-bubble-client {
  max-width: 90%;
  border-radius: 12px;
  background-color: #dcf8c6;
  /* verde claro tipo WhatsApp */
  word-break: break-word;
}

.chat-bubble-user {
  max-width: 95%;
  border-radius: 12px;
  background-color: white;
  word-break: break-word;
  border: 1px solid #ddd;
}

.chat-bubble::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: -10px;
  width: 0;
  height: 0;
  border: 10px solid transparent;
  border-top-color: white;
  border-right-color: white;
  transform: rotate(45deg);
}

.media-preview {
  width: 100%;
  max-width: 280px;
  min-width: 210px;
  height: 180px;
  min-height: 180px;
  max-height: 240px;
  object-fit: cover;
  border-radius: 8px;
  display: block;
  margin-left: -8px;
  margin-right: auto;
  cursor: pointer;
  z-index: 2000;
  /* Asegura que esté por encima */
  position: relative;
  /* Necesario para z-index */
  pointer-events: auto;
  /* Asegura que reciba el click */
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

.btn-details {
  font-weight: 700;
  /* Texto más grueso */
  font-size: 0.95rem;
  /* Un poco más grande */
  letter-spacing: -0.2px;
  /* Más compacto */
  height: 40px;
  width: 250px;
  /* Altura similar al mock */
  border-radius: 8px;
  /* Bordes redondeados */
  padding: 0 16px;
  /* Espaciado interno */
}

.v-btn--outlined.btn-details {
  border-color: #00277d;
  /* Borde del mismo color del texto */
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

.invalidos-alert {
  background: #ffebee !important;
  color: #b71c1c !important;
  max-height: 8.2em;
  overflow-y: auto;
  font-size: 0.95em;
  white-space: pre-line;
  border-left: 6px solid #e57373 !important;
  box-shadow: none !important;
}

.invalidos-alert-title {
  font-weight: bold;
  margin-bottom: 0.3em;
  color: #b71c1c;
  background: #ffebee;
}

.invalidos-alert-content {
  word-break: break-all;
  background: #ffebee;
  display: block;
  color: #b71c1c;
  display: flex;
  justify-content: center;
}

.responsive-scale {
  transition: transform 0.2s;
  transform-origin: var(--scale-origin, center);
  transform: scale(1);
}

.responsive-size {
  transition: width 0.2s, height 0.2s;
}

@media (max-width: 1024px),
(max-height: 800px) {
  .responsive-scale {
    transform: scale(var(--responsive-scale, 1));
  }

  .responsive-size {
    width: var(--responsive-width, initial) !important;
    height: var(--responsive-height, initial) !important;
  }

}
</style>
