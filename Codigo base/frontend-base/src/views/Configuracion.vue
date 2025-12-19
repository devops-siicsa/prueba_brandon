<template>
  <v-app>


    <AppHeader :nombre-comercial="nombreComercial" :imagen-comercial="imagenComercial" :correo-usuario="correoUsuario"
      :comercial-id="comercialId" :base-u-r-l="baseURL" v-model:drawer="drawer" @imagen-actualizada="actualizarImagen"
      @cerrar-sesion="cerrarSesion" />

    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
        <!----- Contenido Principal ----->
        <v-row>
          <v-col>
            <v-card @click="abrirDialogUsuarios()" class="btn-grow-card elevation-3 "
              :style="`height: 30vh;border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-account-cog" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Usuarios
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Gestiona los usuarios del sistema, roles y permisos.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col>
            <v-card @click="abrirDialogProspectos()" class="btn-grow-card elevation-3"
              :style="`height: 30vh;border-radius: 20px;transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-office-building-cog" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Prospecto
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Administra prospectos y empresas potenciales.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col>
            <v-card @click="abrirDialogUbicacion()" class="btn-grow-card elevation-3"
              :style="`height: 30vh;border-radius: 20px;transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-map-marker-star" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Ubicación
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Configura ubicaciones geográficas relevantes.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col>
            <v-card @click="abrirDialogSector()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-format-list-bulleted-type" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Sector
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Organiza los sectores empresariales
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-card @click="abrirDialogCargos()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-account-hard-hat" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Cargos
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Gestiona los cargos y posiciones de los contactos.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col>
            <v-card @click="abrirDialogEstadosC()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-list-status" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Estados Comerciales
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Configura los estados comerciales de las oportunidades.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col>
            <v-card @click="abrirDialogPrioridades()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-alert-box" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Prioridades
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Define las prioridades para la gestión.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col>
            <v-card @click="abrirDialogProductos()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi-store-cog" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Productos
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Administra los productos y servicios.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="3">
            <v-card @click="abrirDialogValorProyectos()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                    margin: 0;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    -ms-transform: translate(-50%, -50%);
                    transform: translate(-50%, -50%);
                    width: 100%;
                  ">
                  <v-card color="#006CA1" style="
                      border-radius: 20px;
                      height: 100px;
                      width: 100px;
                      margin: 0 auto;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    ">
                    <v-icon icon="mdi-cash-100" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                      color: #2c3e50;
                      font-size: 1.35rem;
                      font-weight: 600;
                      margin-top: 18px;
                      margin-bottom: 8px;
                    ">
                    Valor Proyectos
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                      white-space: normal;
                      word-break: break-word;
                      max-width: 340px;
                      margin: 0 auto;
                      color: #555;
                      font-size: 1rem;
                      line-height: 1.3;
                    ">
                    Gestiona el valor de los proyectos y oportunidades.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col>
            <v-card @click="abrirRolesIA()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi mdi-robot-confused" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Roles IA
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Define los roles de la preguntas frecuentes.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col>
            <v-card @click="abrirIntencionIA()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi mdi-text-box-search" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Portafolio IA
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Lee pdfs de respuestas de la IA.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col>
            <v-card @click="abrirPreguntasFrecuentesIA()" class="btn-grow-card elevation-3"
              :style="`height: 30vh; border-radius: 20px; transition: box-shadow 0.3s, transform 0.2s;`">
              <v-card-text style="overflow-y: auto; height: 100%">
                <v-card-text class="text-center" style="
                      margin: 0;
                      position: absolute;
                      top: 50%;
                      left: 50%;
                      -ms-transform: translate(-50%, -50%);
                      transform: translate(-50%, -50%);
                      width: 100%;
                    ">
                  <v-card color="#006CA1" style="
                        border-radius: 20px;
                        height: 100px;
                        width: 100px;
                        margin: 0 auto;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                      ">
                    <v-icon icon="mdi mdi-frequently-asked-questions" size="80" color="white"></v-icon>
                  </v-card>
                  <h2 style="
                        color: #2c3e50;
                        font-size: 1.35rem;
                        font-weight: 600;
                        margin-top: 18px;
                        margin-bottom: 8px;
                      ">
                    Preguntas y Respuestas IA
                  </h2>
                  <v-card-subtitle class="text-h8" style="
                        white-space: normal;
                        word-break: break-word;
                        max-width: 340px;
                        margin: 0 auto;
                        color: #555;
                        font-size: 1rem;
                        line-height: 1.3;
                      ">
                    Establece las preguntas y respuestas de la IA.
                  </v-card-subtitle>
                </v-card-text>
              </v-card-text>
            </v-card>
          </v-col>

        </v-row>


        <!----- Contenido Principal ----->

        <!----- Dialogo para listar los prospectos ----->
        <v-dialog v-model="dialogProspectos" persistent width="75%">
          <v-card style="border-radius: 20px; height: 100%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-office-building-cog </v-icon>
              Listar prospectos
              <v-icon style="float: right" @click="nuevoProspecto()">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">Prospectos ({{ listaEmpresas.length }})</div>
            </v-card-subtitle>

            <v-row class="mx-2 mt-2 mb-n6">
              <v-col cols="3">
                <v-autocomplete v-model="filtroRazonSocialEmpresas" :items="listaEmpresas" return-object
                  item-title="p_razon_social" item-value="id" label="Razón Social" variant="outlined" clearable
                  autocomplete="off" density="compact" @update:model-value="filtrarEmpresas()"
                  :readonly="filtroNitEmpresas || filtroFechaDesdeEmpresas" />
              </v-col>

              <v-col cols="3">
                <v-autocomplete v-model="filtroNitEmpresas" :items="listaEmpresas" return-object :item-title="
                    (item) =>
                      `${item.p_nit}` ? `${item.p_nit}` : 'No disponible'
                  " item-value="id" label="NIT" variant="outlined" clearable autocomplete="off" density="compact"
                  @update:model-value="filtrarEmpresas()" :readonly="
                    filtroRazonSocialEmpresas || filtroFechaDesdeEmpresas
                  " />
              </v-col>

              <v-col cols="3">
                <v-text-field v-model="filtroFechaDesdeEmpresas" label="Fecha de Creación Desde" type="date"
                  variant="outlined" clearable autocomplete="off" density="compact"
                  @update:model-value="filtrarEmpresas2()" :readonly="filtroRazonSocialEmpresas || filtroNitEmpresas" />
              </v-col>

              <v-col cols="3">
                <v-text-field v-model="filtroFechaHastaEmpresas" label="Fecha de Creación Hasta" type="date"
                  variant="outlined" clearable autocomplete="off" density="compact"
                  @update:model-value="filtrarEmpresas2()" :readonly="filtroRazonSocialEmpresas || filtroNitEmpresas"
                  v-if="filtroFechaDesdeEmpresas" />
              </v-col>
            </v-row>

            <v-card-text style="overflow-y: auto; height: 100%">
              <v-row v-for="(fila, filaIndex) in filasEmpresas" :key="filaIndex" class="mb-4">
                <v-col v-for="empresa in fila" :key="empresa.id">
                  <v-card @click="
                      cargarProspecto(empresa);
                      estaEditando = true;
                    " class="empresa-card pa-3 mb-2" elevation="3">
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
                        <div class="empresa-value font-weight-medium d-flex align-center" style="color: #222">
                          <v-icon size="18" color="#1976D2" class="mr-1">mdi-phone</v-icon>
                          <span class="contact-card-text">
                            {{ empresa.p_telefono1 || "No disponible" }}</span>
                        </div>
                        <div class="empresa-label text-caption mt-1" style="color: #666">
                          Celular contacto
                        </div>
                        <div class="empresa-value font-weight-medium d-flex align-center" style="color: #222">
                          <v-icon size="18" color="#1976D2" class="mr-1">mdi-cellphone</v-icon>
                          <span class="contact-card-text">
                            {{ empresa.pc_celular || "No disponible" }}</span>
                        </div>
                      </v-col>
                      <v-col cols="6">
                        <div class="empresa-label text-caption" style="color: #666">
                          Contacto
                        </div>
                        <div class="empresa-value font-weight-medium d-flex align-center" style="color: #222">
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
                          Comercial Asignado:
                        </div>
                        <div class="empresa-label text-caption" style="
                            color: #1976d2;
                            font-weight: 500;
                            margin-top: 2px;
                          ">
                          <span>{{
                            getNombreComercial(empresa.p_comercial)
                            }}</span>
                        </div>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-col>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-btn @click="
                  dialogProspectos = false;
                  filtroRazonSocialEmpresas = null;
                  filtroNitEmpresas = null;
                  filtroFechaDesdeEmpresas = null;
                  filtroFechaHastaEmpresas = null;
                  estaEditando = false;
                " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar los prospectos ----->

        <!----- Dialogo para crear/editar los prospectos ----->
        <v-dialog v-model="dialogCrearEditarProspecto" persistent width="70%">
          <v-card style="height: 100%; border-radius: 20px">
            <v-card-title class="text-h6" style="color: white; font-weight: bold; background-color: #006ca1">
              <div v-if="!idProspectoSeleccionado">
                Crear Prospecto
                <v-icon style="float: right" @click="guardarProspecto()" :disabled="dsGuardar" icon="mdi-content-save"
                  size="small"></v-icon>
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
                      <v-autocomplete v-model="comercialSeleccionado" :items="listaComerciales" item-title="nombre"
                        item-value="id" label="Asignar Comercial" variant="outlined" clearable required :rules="[
                          (v) => !!v || 'Debes seleccionar un comercial',
                        ]" autocomplete="off" prepend-inner-icon="mdi-account-tie"
                        class="mx-5 ml-5 mb-n2"></v-autocomplete>
                    </v-col>
                    <v-col cols="11">
                      <input class="campo-input mx-5 mb-5" list="empresas" id="empresa" v-model="nit" placeholder="NIT"
                        autocomplete="off" />
                    </v-col>
                    <v-col style="margin-left: -30px">
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
                    this.mensajeAlertaRazonSocial }}</v-alert>
                  <v-row>
                    <v-col cols="11">
                      <input class="campo-input mx-5 mb-5" list="empresas2" id="empresa" v-model="razonSocial"
                        placeholder="Razón Social" autocomplete="off" />
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
                      <v-select class="ml-5" v-model="tipoId" :items="tipoIdentificacion" return-object
                        item-title="nombre" item-value="id" label="Tipo Identificación" variant="outlined" clearable
                        autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-card-account-details</v-icon>
                        </template>
                      </v-select>
                    </v-col>
                    <v-col>
                      <v-select disabled class="mr-5" v-model="tipoEmp" :items="tipoEmpresa" return-object
                        item-title="nombre" item-value="id" label="Tipo Empresa" variant="outlined" clearable
                        autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-domain</v-icon>
                        </template>
                      </v-select>
                    </v-col>
                  </v-row>
                  <v-select class="mx-5" v-model="sector" :items="sectorEmpresa" return-object item-title="nombre"
                    item-value="id" label="Sector" variant="outlined" clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">mdi-office-building</v-icon>
                    </template>
                  </v-select>
                  <v-text-field class="mx-5" v-model="direccion" label="Dirección" type="text" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">mdi-map-marker</v-icon>
                    </template>
                  </v-text-field>
                  <v-row>
                    <v-col>
                      <v-autocomplete class="ml-5" v-model="departamento" :items="departamentos" return-object
                        item-title="nombre" item-value="id" label="Departamento" variant="outlined" clearable
                        autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-home-city</v-icon>
                        </template>
                      </v-autocomplete>
                    </v-col>
                    <v-col>
                      <v-autocomplete class="mr-5" v-model="ciudad" :items="ciudades" return-object item-title="nombre"
                        item-value="id" label="Ciudad" variant="outlined" clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-city-variant</v-icon>
                        </template>
                      </v-autocomplete>
                    </v-col>
                  </v-row>
                  <v-text-field class="mx-5" v-model="web" label="Pagina Web" type="text" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">mdi-web-box</v-icon>
                    </template>
                  </v-text-field>
                  <v-text-field class="mx-5" v-model="correoEmpresa" label="Mail Empresa" type="text" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">mdi-email</v-icon>
                    </template>
                  </v-text-field>
                  <v-row>
                    <v-col>
                      <v-text-field class="ml-5" @input="filterTel1" :rules="[maxlength2].flat()" v-model="tel1"
                        label="Telefono 1" type="number" variant="outlined" clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-cellphone</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field class="mr-5" v-model="tel2" label="Telefono 2" type="number" variant="outlined"
                        clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-phone</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col style="border-left: 1px solid #ccc; padding-left: 20px">
                  <h3 class="text-center mb-4" style="background-color: #006ca1; color: white">
                    Información del Contacto
                  </h3>
                  <v-text-field class="mx-5" v-model="nombre" label="Nombre" type="text" variant="outlined" clearable
                    autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">mdi-rename</v-icon>
                    </template>
                  </v-text-field>
                  <v-text-field class="mx-5" v-model="apellido" label="Apellido" type="text" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">mdi-rename</v-icon>
                    </template>
                  </v-text-field>
                  <v-row>
                    <v-col>
                      <v-autocomplete class="mx-5" v-model="categoria" :items="categorias" return-object
                        item-title="nombre" item-value="id" label="Categoria Cargo" variant="outlined" clearable
                        autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-format-list-bulleted-type</v-icon>
                        </template>
                      </v-autocomplete>
                    </v-col>
                    <v-col>
                      <v-autocomplete class="mx-5" v-model="cargo" :items="cargos" return-object item-title="nombre"
                        item-value="id" label="Cargo" type="text" variant="outlined" clearable autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-account-tie</v-icon>
                        </template>
                      </v-autocomplete>
                    </v-col>
                  </v-row>
                  <v-text-field class="mx-5" v-model="correoContacto" label="Correo" type="text" variant="outlined"
                    clearable autocomplete="off">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">mdi-email</v-icon>
                    </template>
                  </v-text-field>
                  <v-row>
                    <v-col cols="3" class="m-0">
                      <v-text-field class="ml-5 mr-n4" v-model="extension" label="Extensión" type="number"
                        variant="outlined" autocomplete="off">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-numeric</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                    <v-col cols="9">
                      <v-text-field class="mr-5 ml-4" v-model="celular" label="Celular" type="number" variant="outlined"
                        autocomplete="off" @input="filterNumber" :rules="[rules.required, rules.phoneMax12]">
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-cellphone</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                  </v-row>
                  <v-alert v-if="alertaCelular" class="mx-5 mb-5" type="error" icon="mdi-account-alert">{{
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

        <!----- Dialogo para listar los usuarios ----->
        <v-dialog v-model="dialogUsuarios" persistent width="75%">
          <v-card style="border-radius: 20px; height: 100%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-account-cog </v-icon>
              Listar Usuarios
              <v-icon style="float: right" @click="nuevoUsuario()">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">Usuarios ({{ listaUsuarios.length }})</div>
            </v-card-subtitle>

            <v-row class="mx-2 mt-2 mb-n6">
              <v-col cols="3">
                <v-autocomplete v-model="filtroNombreUsuarios" :items="listaUsuarios" return-object
                  :item-title="(item) => `${item.u_nom} ${item.u_ape}`" item-value="u_id" label="Nombre"
                  variant="outlined" clearable autocomplete="off" density="compact"
                  @update:model-value="filtrarUsuarios()" :readonly="filtroCedulaUsuario || filtroCelularUsuario" />
              </v-col>

              <v-col cols="3">
                <v-autocomplete v-model="filtroCedulaUsuario" :items="listaUsuarios" return-object item-title="u_ced"
                  item-value="id" label="Cédula" variant="outlined" clearable autocomplete="off" density="compact"
                  @update:model-value="filtrarUsuarios()" :readonly="filtroNombreUsuarios || filtroCelularUsuario" />
              </v-col>

              <v-col cols="3">
                <v-autocomplete v-model="filtroCelularUsuario" :items="listaUsuarios" return-object item-title="u_cel"
                  item-value="id" label="Celular" variant="outlined" clearable autocomplete="off" density="compact"
                  @update:model-value="filtrarUsuarios()" :readonly="filtroNombreUsuarios || filtroCedulaUsuario" />
              </v-col>
            </v-row>

            <v-card-text style="overflow-y: auto; height: 100%">
              <v-row v-for="(fila, filaIndex) in filasUsuarios" :key="filaIndex" class="mb-4">
                <v-col v-for="usuario in fila" :key="usuario.u_id">
                  <v-card @click="cargarUsuario(usuario)" class="usuario-card pa-3 mb-2" elevation="3" style="
                      border-radius: 16px;
                      background: linear-gradient(
                        135deg,
                        #f5f8fa 80%,
                        #e3eaf2 100%
                      );
                    ">
                    <v-row align="center" no-gutters>
                      <v-col cols="auto">
                        <v-avatar color="#1976D2" size="44">
                          <v-icon color="white" size="32">mdi-account-circle</v-icon>
                        </v-avatar>
                      </v-col>
                      <v-col>
                        <div class="usuario-title font-weight-bold ml-2" style="
                            font-size: 1.15rem;
                            color: #0a1c3a;
                            white-space: normal;
                            word-break: break-word;
                          ">
                          {{ usuario.u_nom }} {{ usuario.u_ape }}
                        </div>
                        <div class="usuario-id ml-2 text-caption" style="
                            color: #1976d2;
                            font-weight: 500;
                            margin-top: 2px;
                          ">
                          <span style="margin-right: 4px">CC:</span>
                          <span>{{ usuario.u_ced }}</span>
                        </div>
                      </v-col>
                    </v-row>
                    <v-divider class="my-2"></v-divider>
                    <v-row>
                      <v-col cols="6">
                        <div class="usuario-label text-caption" style="color: #666">
                          Celular
                        </div>
                        <div class="usuario-value font-weight-medium d-flex align-center" style="color: #222">
                          <v-icon size="18" color="#1976D2" class="mr-1">mdi-cellphone</v-icon>
                          <span class="contact-card-text">{{
                            usuario.u_cel || "No disponible"
                            }}</span>
                        </div>
                        <div class="usuario-label text-caption mt-1" style="color: #666">
                          Correo
                        </div>
                        <div class="usuario-value font-weight-medium d-flex align-center" style="color: #222">
                          <v-icon size="18" color="#1976D2" class="mr-1">mdi-email</v-icon>
                          <span class="contact-card-text">{{
                            usuario.u_ema || "No disponible"
                            }}</span>
                        </div>
                      </v-col>
                      <v-col cols="6">
                        <div class="usuario-label text-caption" style="color: #666">
                          Rol
                        </div>
                        <div class="usuario-value font-weight-medium d-flex align-center" style="color: #222">
                          <v-icon size="18" color="#1976D2" class="mr-1">mdi-account-tie</v-icon>
                          <span class="contact-card-text" style="color: #1976d2;">
                            {{
                            getNombrePerfil(usuario.u_cargo) ||
                            "No disponible"
                            }}
                          </span>
                        </div>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-col>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-btn @click="
                  dialogUsuarios = false;
                  filtroNombreUsuarios = null;
                  filtroCedulaUsuario = null;
                  filtroCelularUsuario = null;
                " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar los usuarios ----->

        <!----- Dialogo para crear/editar los usuarios ----->
        <v-dialog v-model="dialogCrearEditarUsuario" persistent width="70%">
          <v-card style="height: 100%; border-radius: 20px">
            <v-card-title class="text-h6" style="color: white; font-weight: bold; background-color: #006ca1">
              <div v-if="!idUsuarioSeleccionado">
                Crear Usuario
                <v-icon style="float: right" @click="guardarUsuario()" icon="mdi-content-save" size="small"></v-icon>
              </div>
              <div v-if="idUsuarioSeleccionado">
                <v-icon class="mr-2">mdi-account-cog</v-icon>
                Editar Usuario
                <v-icon style="float: right" @click="actualizarUsuario()" icon="mdi-content-save" size="small"></v-icon>
              </div>
            </v-card-title>
            <v-card-text style="overflow-y: auto; height: 100%">
              <v-row>
                <v-col>
                  <h3 class="text-center mb-4" style="background-color: #006ca1; color: white">
                    Información del Usuario
                  </h3>

                  <v-row>
                    <v-col>
                      <v-text-field class="mx-5" v-model="nombreUsu" label="Nombre Usuario" type="text"
                        variant="outlined" clearable>
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-account</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field class="mx-5" v-model="apellidosUsu" label="Apellidos Usuario" type="text"
                        variant="outlined" clearable>
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-account</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                  </v-row>

                  <v-row class="mt-n6">
                    <v-col>
                      <v-text-field class="mx-5" v-model="cedulaUsu" label="Cédula Usuario" type="number"
                        variant="outlined" clearable>
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-card-account-details</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>

                    <v-col>
                      <v-text-field class="mx-5" v-model="emailUsu" label="Email Usuario" type="email"
                        variant="outlined" clearable>
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-email</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                  </v-row>

                  <v-row class="mt-n6">
                    <v-col>
                      <v-text-field class="mx-5" v-model="celularUsu" label="Celular Usuario" type="number"
                        variant="outlined" clearable>
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-cellphone</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>

                    <v-col>
                      <v-text-field class="mx-5" v-model="cuentaUsu" label="Cuenta Usuario" type="text"
                        variant="outlined" clearable>
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-login-variant</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>
                  </v-row>

                  <v-row class="mt-n6">
                    <v-col>
                      <v-text-field class="mx-5" v-model="metaUsuario" label="Meta Usuario" type="number"
                        variant="outlined" clearable>
                        <template v-slot:prepend-inner>
                          <v-icon color="#006CA1" style="opacity: 100%">mdi-cash-clock</v-icon>
                        </template>
                      </v-text-field>
                    </v-col>

                    <v-col>
                      <template v-if="perfilUsu ? perfilUsu.id === 5 : false">
                        <v-row>
                          <v-col cols="8">
                            <v-select class="mx-5" v-model="perfilUsu" :items="perfilesUsu" return-object item-title="nombre"
                              item-value="id" label="Perfil" variant="outlined" clearable autocomplete="off">
                              <template v-slot:prepend-inner>
                                <v-icon color="#006CA1" style="opacity: 100%">mdi-account-hard-hat</v-icon>
                              </template>
                            </v-select>
                          </v-col>
                          <v-col cols="4" class="d-flex align-center">
                            <v-checkbox
                              v-model="adminUsu"
                              label="Admin"
                              :true-value="true"
                              :false-value="false"
                              color="#006CA1"
                            ></v-checkbox>
                          </v-col>
                        </v-row>
                      </template>
                      <template v-else>
                        <v-select class="mx-5" v-model="perfilUsu" :items="perfilesUsu" return-object item-title="nombre"
                          item-value="id" label="Perfil" variant="outlined" clearable autocomplete="off">
                          <template v-slot:prepend-inner>
                            <v-icon color="#006CA1" style="opacity: 100%">mdi-account-hard-hat</v-icon>
                          </template>
                        </v-select>
                      </template>
                    </v-col>
                  </v-row>

                  <v-row class="mt-n6">
                    <v-col>
                      <v-checkbox class="mx-5" v-model="activoUsu" label="Activo" color="#006CA1" variant="outlined">
                      </v-checkbox>
                    </v-col>

                    <v-col>
                      <v-checkbox class="mx-5" v-model="contraseñaUsu" v-if="idUsuarioSeleccionado"
                        label="Restablecer Contraseña" color="#006CA1" variant="outlined">
                      </v-checkbox>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-btn variant="outlined" color="primary" class="text-none btn-grow-card" @click="
                  dialogCrearEditarUsuario = false;
                  dialogUsuarios = true;
                  limpiarCamposUsuario();
                  limpiarFiltrosUsuarios();
                ">Cerrar</v-btn>

              <v-btn color="primary" variant="flat" size="large" rounded="lg" class="text-none px-5 btn-grow-card"
                prepend-icon="mdi mdi-content-save-check-outline" :disabled="dsGuardar" v-if="!idUsuarioSeleccionado"
                @click="guardarUsuario()">Crear Usuario</v-btn>

              <v-btn color="primary" variant="flat" size="large" rounded="lg" class="text-none px-5 btn-grow-card"
                prepend-icon="mdi mdi-content-save-check-outline" :disabled="dsGuardar" v-if="idUsuarioSeleccionado"
                @click="actualizarUsuario()">Actualizar Usuario</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para crear/editar los usuarios ----->

        <!----- Dialogo para listar las ubicaciones ----->
        <v-dialog v-model="dialogUbicacion" persistent width="75%">
          <v-card style="border-radius: 20px; height: 100%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-map-marker-radius </v-icon>
              Listar Ubicaciones
              <v-icon style="float: right" @click="
                  ifbtnGuardarUbicacion = true;
                  ifbtnEditarUbicacion = false;
                  limpiarCamposUbicacion();
                " title="Crear Ubicación">
                mdi-plus-circle
              </v-icon>
              <v-icon style="float: right" @click="
                  ifbtnEditarUbicacion = true;
                  ifbtnGuardarUbicacion = false;
                  limpiarCamposUbicacion();
                " title="Editar Ubicación">
                mdi-pencil-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">
                Ubicaciones ({{ listaUbicaciones.length }})
              </div>
            </v-card-subtitle>

            <v-card-text style="overflow-y: auto; height: 100%">
              <v-row>
                <v-col>
                  <v-autocomplete v-model="nuevoDepartamento" :items="listaUbicaciones" return-object
                    item-title="nombre" item-value="id" v-if="ifbtnEditarUbicacion"
                    label="Seleccione un departamento existente para editar" variant="outlined" clearable
                    autocomplete="off" density="compact" @update:model-value="cargarCiudades()" />

                  <v-text-field v-model="nuevoNombreDepartamentoEdit" :label="
                      ifbtnEditarUbicacion
                        ? 'Editar nombre departamento'
                        : 'Nombre del nuevo departamento'
                    " v-if="nuevoDepartamento && ifbtnEditarUbicacion" variant="outlined" clearable autocomplete="off"
                    density="compact" color="#006CA1">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-list-box-outline
                      </v-icon>
                    </template>
                  </v-text-field>

                  <v-autocomplete v-model="nuevaCiudad" :items="listaCiudades" return-object item-title="nombre"
                    item-value="id" v-if="ifbtnEditarUbicacion" label="Seleccione una ciudad existente para editar"
                    variant="outlined" clearable autocomplete="off" density="compact" />

                  <v-text-field v-model="nuevoNombreCiudadEdit" label="Editar nombre de la ciudad" v-if="nuevaCiudad"
                    variant="outlined" clearable autocomplete="off" density="compact" color="#006CA1">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-city
                      </v-icon>
                    </template>
                  </v-text-field>

                  <v-text-field v-model="nuevoNombreDepartamento" label="Nombre del nuevo departamento"
                    v-if="ifbtnGuardarUbicacion" variant="outlined" clearable autocomplete="off" density="compact"
                    color="#006CA1" :disabled="nuevaDepartamentoCiudad || nuevoNombreCiudad">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-list-box-outline
                      </v-icon>
                    </template>
                  </v-text-field>

                  <div v-if="ifbtnGuardarUbicacion" class="mb-4">
                    O crear una nueva ciudad para un departamento existente:
                  </div>

                  <v-autocomplete v-model="nuevaDepartamentoCiudad" :items="listaUbicaciones" return-object
                    item-title="nombre" item-value="id" v-if="ifbtnGuardarUbicacion"
                    label="Seleccione un departamento existente para añadir una nueva ciudad" variant="outlined"
                    clearable autocomplete="off" density="compact" :disabled="nuevoNombreDepartamento"
                    @update:model-value="cargarCiudades()" />

                  <v-text-field v-model="nuevoNombreCiudad" label="Nombre de la nueva ciudad"
                    v-if="ifbtnGuardarUbicacion" variant="outlined" clearable autocomplete="off" density="compact"
                    color="#006CA1" :disabled="nuevoNombreDepartamento">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-list-box-outline
                      </v-icon>
                    </template>
                  </v-text-field>
                </v-col>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-btn v-if="ifbtnGuardarUbicacion" @click="save_ubicacion(0)" color="#006CA1" class="mb-4"
                variant="flat">Guardar</v-btn>
              <v-btn v-if="ifbtnEditarUbicacion" @click="save_ubicacion(1)" color="#006CA1" class="mb-4"
                variant="flat">Editar</v-btn>
              <v-btn @click="
                  dialogUbicacion = false;
                  ifbtnGuardarUbicacion = false;
                  ifbtnEditarUbicacion = true;
                  limpiarCamposUbicacion();
                " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar las ubicaciones ----->

        <!----- Dialogo para listar los sectores ----->
        <v-dialog v-model="dialogSector" persistent width="40%">
          <v-card style="border-radius: 20px; height: 50%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-warehouse </v-icon>
              Listar Sectores
              <v-icon style="float: right" @click="selEditarSector()" title="Editar Sector">
                mdi-pencil-circle
              </v-icon>
              <v-icon style="float: right" @click="selNuevoSector()" title="Nuevo Sector">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">
                Sectores ({{ listaSectores.length }}) - {{ labelTituloSector }}
              </div>
            </v-card-subtitle>

            <v-row class="mx-2 mt-4 mb-n6">
              <v-col cols="12">
                <v-autocomplete v-model="filtroSectores" :items="listaSectores" return-object item-title="nombre"
                  item-value="id" label="Seleccionar Sector a Editar" variant="outlined" clearable autocomplete="off"
                  @change="cargarDatosSector(filtroSectores)" v-show="mostrarSelectSector" />
              </v-col>
            </v-row>
            <v-row class="mx-0 mt-2">
              <v-text-field class="mx-5" v-model="nombreSector" :label="labelNombreSector" type="text"
                variant="outlined" autocomplete="off" clearable v-show="mostrarNombreSector">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%">mdi-account</v-icon>
                </template>
              </v-text-field>
            </v-row>
            <!--<v-row class="mx-0 mt-2">
                            <v-col cols="12" class="mx-5">
                                <v-switch v-model="estadoSector" inset color="secondary" label=" Mostrar en las listas de Sector" v-show="mostrarEstadoSector"></v-switch>
                            </v-col>
                        </v-row>-->

            <v-row class="mx-0 mt-2">
              <!-- Alerta de error -->
              <v-alert class="mx-5" v-if="mensajeError" type="error">
                {{ mensajeError }}
              </v-alert>
            </v-row>

            <v-card-actions class="mt-5">
              <v-btn @click="save_sector(1)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarSaveSector">Crear</v-btn>
              <v-btn @click="save_sector(0)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarEditSector">Editar</v-btn>
              <v-btn @click="dialogSector = false" color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar los sectores ----->

        <!----- Dialogo para listar los cargos ----->
        <v-dialog v-model="dialogCargos" persistent width="75%">
          <v-card style="border-radius: 20px; height: 100%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-account-box-multiple </v-icon>
              Listar Cargos
              <v-icon style="float: right" @click="
                  ifbtnGuardarCargo = true;
                  ifbtnEditarCargo = false;
                  limpiarCamposCargos();
                " title="Crear Cargo">
                mdi-plus-circle
              </v-icon>
              <v-icon style="float: right" @click="
                  ifbtnEditarCargo = true;
                  ifbtnGuardarCargo = false;
                  limpiarCamposCargos();
                " title="Editar Cargo">
                mdi-pencil-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">Cargos ({{ listaCargos.length }})</div>
            </v-card-subtitle>

            <v-card-text style="overflow-y: auto; height: 100%">
              <v-row>
                <v-col>
                  <v-autocomplete v-model="nuevaCategoriaCargo" :items="listaCargos" return-object item-title="nombre"
                    item-value="id" v-if="ifbtnEditarCargo" label="Seleccione una categoria existente para editar"
                    variant="outlined" clearable autocomplete="off" density="compact"
                    @update:model-value="cargarCargosxCat()" />

                  <v-text-field v-model="nuevoNombreCategoriaEdit" :label="
                      ifbtnEditarCargo
                        ? 'Editar nombre categoria'
                        : 'Nombre de la nueva categoria'
                    " v-if="nuevaCategoriaCargo && ifbtnEditarCargo" variant="outlined" clearable autocomplete="off"
                    density="compact" color="#006CA1">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-list-box-outline
                      </v-icon>
                    </template>
                  </v-text-field>

                  <v-autocomplete v-model="nuevoCargo" :items="listaCargosxCat" return-object item-title="nombre"
                    item-value="id" v-if="ifbtnEditarCargo" label="Seleccione un cargo existente para editar"
                    variant="outlined" clearable autocomplete="off" density="compact" />

                  <v-text-field v-model="nuevoNombreCargoEdit" label="Editar nombre del cargo" v-if="nuevoCargo"
                    variant="outlined" clearable autocomplete="off" density="compact" color="#006CA1">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-list-box-outline
                      </v-icon>
                    </template>
                  </v-text-field>

                  <v-text-field v-model="nuevoNombreCategoria" label="Nombre de la nueva categoria"
                    v-if="ifbtnGuardarCargo" variant="outlined" clearable autocomplete="off" density="compact"
                    color="#006CA1" :disabled="nuevaCategoriaCargo || nuevoNombreCargo">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-list-box-outline
                      </v-icon>
                    </template>
                  </v-text-field>

                  <div v-if="ifbtnGuardarCargo" class="mb-4">
                    O crear un nuevo cargo para una categoria existente
                  </div>

                  <v-autocomplete v-model="nuevaCategoriaCargo" :items="listaCargos" return-object item-title="nombre"
                    item-value="id" v-if="ifbtnGuardarCargo"
                    label="Seleccione una categoria existente para añadir un cargo" variant="outlined" clearable
                    autocomplete="off" density="compact" :disabled="nuevoNombreCategoria"
                    @update:model-value="cargarCargosxCat()" />

                  <v-text-field v-model="nuevoNombreCargo" label="Nombre del nuevo cargo" v-if="ifbtnGuardarCargo"
                    variant="outlined" clearable autocomplete="off" density="compact" color="#006CA1"
                    :disabled="nuevoNombreCategoria">
                    <template v-slot:prepend-inner>
                      <v-icon color="#006CA1" style="opacity: 100%">
                        mdi-list-box-outline
                      </v-icon>
                    </template>
                  </v-text-field>
                </v-col>
              </v-row>
            </v-card-text>

            <v-card-actions>
              <v-btn v-if="ifbtnGuardarCargo" @click="save_cargos(0)" color="#006CA1" class="mb-4"
                variant="flat">Guardar</v-btn>
              <v-btn v-if="ifbtnEditarCargo" @click="save_cargos(1)" color="#006CA1" class="mb-4"
                variant="flat">Editar</v-btn>
              <v-btn @click="
                  dialogCargos = false;
                  ifbtnGuardarCargo = false;
                  ifbtnEditarCargo = true;
                  limpiarCamposCargos();
                " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar los cargos ----->

        <!----- Dialogo para listar los estados comerciales ----->
        <v-dialog v-model="dialogEstadosC" persistent width="40%">
          <v-card style="border-radius: 20px; height: 50%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-clipboard-list </v-icon>
              Listar Estados Comerciales
              <v-icon style="float: right" @click="selEditarEstadoC()" title="Editar Estado Comercial">
                mdi-pencil-circle
              </v-icon>
              <v-icon style="float: right" @click="selNuevoEstadoC()" title="Nuevo Estado Comercial">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">
                Estados Comerciales ({{ listaEstadosC.length }}) -
                {{ labelTituloEstadosC }}
              </div>
            </v-card-subtitle>

            <v-row class="mx-2 mt-4 mb-n6">
              <v-col cols="12">
                <v-autocomplete v-model="filtroEstadosC" :items="listaEstadosC" return-object item-title="nombre"
                  item-value="id" label="Seleccionar Estado Comercial a Editar" variant="outlined" clearable
                  autocomplete="off" @change="cargarDatosEstadosC(filtroEstadosC)" v-show="mostrarSelectEstadosC" />
              </v-col>
            </v-row>
            <v-row class="mx-0 mt-2">
              <v-text-field class="mx-5" v-model="nombreEstadosC" :label="labelNombreEstadosC" type="text"
                variant="outlined" autocomplete="off" clearable v-show="mostrarNombreEstadosC">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%">mdi-account</v-icon>
                </template>
              </v-text-field>
            </v-row>

            <v-row class="mx-0 mt-2">
              <!-- Alerta de error -->
              <v-alert class="mx-5" v-if="mensajeError" type="error">
                {{ mensajeError }}
              </v-alert>
            </v-row>

            <v-card-actions class="mt-5">
              <v-btn @click="save_estados_c(1)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarSaveEstadosC">Crear</v-btn>
              <v-btn @click="save_estados_c(0)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarEditEstadosC">Editar</v-btn>
              <v-btn @click="dialogEstadosC = false" color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar los estados comerciales ----->

        <!----- Dialogo para listar las prioridades ----->
        <v-dialog v-model="dialogPrioridades" persistent width="40%">
          <v-card style="border-radius: 20px; height: 50%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-chart-arc </v-icon>
              Listar Prioridades
              <v-icon style="float: right" @click="selEditarPrioridad()" title="Editar Prioridad">
                mdi-pencil-circle
              </v-icon>
              <v-icon style="float: right" @click="selNuevoPrioridad()" title="Nuevo Prioridad">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">
                Prioridades ({{ listaPrioridades.length }}) -
                {{ labelTituloPrioridades }}
              </div>
            </v-card-subtitle>

            <v-row class="mx-2 mt-4 mb-n6">
              <v-col cols="12">
                <v-autocomplete v-model="filtroPrioridades" :items="listaPrioridades" return-object item-title="nombre"
                  item-value="id" label="Seleccionar Prioridad a Editar" variant="outlined" clearable autocomplete="off"
                  @change="cargarDatosPrioridades(filtroPrioridades)" v-show="mostrarSelectPrioridades" />
              </v-col>
            </v-row>
            <v-row class="mx-0 mt-2">
              <v-text-field class="mx-5" v-model="nombrePrioridades" :label="labelNombrePrioridades" type="text"
                variant="outlined" autocomplete="off" clearable v-show="mostrarNombrePrioridades">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%">mdi-account</v-icon>
                </template>
              </v-text-field>
            </v-row>

            <v-row class="mx-0 mt-2">
              <!-- Alerta de error -->
              <v-alert class="mx-5" v-if="mensajeError" type="error">
                {{ mensajeError }}
              </v-alert>
            </v-row>

            <v-card-actions class="mt-5">
              <v-btn @click="save_prioridades(1)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarSavePrioridades">Crear</v-btn>
              <v-btn @click="save_prioridades(0)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarEditPrioridades">Editar</v-btn>
              <v-btn @click="dialogPrioridades = false" color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar las prioridades ----->

        <!----- Dialogo para listar los productos ----->
        <v-dialog v-model="dialogProductos" persistent width="40%">
          <v-card style="border-radius: 20px; height: 50%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-list-box </v-icon>
              Listar Productos
              <v-icon style="float: right" @click="selEditarProducto()" title="Editar Producto">
                mdi-pencil-circle
              </v-icon>
              <v-icon style="float: right" @click="selNuevoProducto()" title="Nuevo Producto">
                mdi-plus-circle
              </v-icon>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">
                Productos ({{ listaProductos.length }}) -
                {{ labelTituloProducto }}
              </div>
            </v-card-subtitle>

            <v-row class="mx-2 mt-4 mb-n6">
              <v-col cols="12">
                <v-autocomplete v-model="filtroProductos" :items="listaProductos" return-object item-title="nombre"
                  item-value="id" label="Seleccionar Producto a Editar" variant="outlined" clearable autocomplete="off"
                  @change="cargarDatosProducto(filtroProductos)" v-show="mostrarSelectProducto" />
              </v-col>
            </v-row>

            <v-row class="mx-0 mt-6">
              <v-text-field class="mx-5" v-model="nombreProducto" :label="labelNombreProducto" type="text"
                variant="outlined" autocomplete="off" clearable v-show="mostrarNombreProducto">
                <template v-slot:prepend-inner>
                  <v-icon color="#006CA1" style="opacity: 100%">mdi-account</v-icon>
                </template>
              </v-text-field>
            </v-row>

            <v-row class="mx-2 mt-4 mb-n6">
              <v-col cols="12">
                <v-file-input v-model="archivoProducto" :label="
                    urlArchivo
                      ? 'Actualizar ficha técnica'
                      : 'Agregar una ficha técnica'
                  " outlined variant="outlined" v-show="mostrarNombreProducto" />
              </v-col>
            </v-row>

            <v-row class="mx-2 mb-1" v-if="urlArchivo">
              <v-col cols="12">
                <a :href="urlArchivo" target="_blank">Ver ficha técnica actual</a>
              </v-col>
            </v-row>

            <v-row class="mx-2 mt-4 mb-n6">
              <v-col cols="12">
                <v-textarea v-model="descripcionProducto" label="Descripción técnica del Producto" outlined
                  variant="outlined" v-show="mostrarNombreProducto" />
              </v-col>
            </v-row>

            <v-row class="mx-0 mt-2">
              <!-- Alerta de error -->
              <v-alert class="mx-5" v-if="mensajeError" type="error">
                {{ mensajeError }}
              </v-alert>
            </v-row>

            <v-card-actions class="mt-2">
              <v-btn @click="save_producto(1)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarSaveProducto">Crear</v-btn>
              <v-btn @click="save_producto(0)" color="#006CA1" class="mb-4" variant="flat"
                v-show="mostrarEditProducto">Editar</v-btn>
              <v-btn @click="dialogProductos = false" color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para listar los productos ----->

        <!----- Dialogo para cambiar el valor de los proyectos ----->
        <v-dialog v-model="dialogValorProyectos" persistent width="40%">
          <v-card style="border-radius: 20px; height: 50%">
            <v-card-title class="text-h6 pa-4" style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon> mdi-account-box-multiple </v-icon>
              Listar Comerciales
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2" style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">
                Comerciales ({{ listaComerciales.length }})
              </div>
            </v-card-subtitle>

            <v-row class="mx-2 mt-4 mb-n6">
              <v-col>
                <v-autocomplete v-model="selectedComercial" :items="listaComerciales" return-object item-title="nombre"
                  item-value="id" label="Seleccione un comercial" variant="outlined" clearable autocomplete="off"
                  @update:model-value="cargarProyectos()" />
              </v-col>
            </v-row>

            <v-row class="mx-2 mb-n6">
              <v-col>
                <v-autocomplete v-model="selectedProyecto" :items="listaProyectos" return-object :item-title="
                    (item) =>
                      `${item.razon_social} - ${
                        item.nombre_servicio
                          ? item.nombre_servicio
                          : 'Sin Servicio'
                      }`
                  " item-value="id" label="Seleccione un proyecto en cotización" variant="outlined" clearable
                  v-if="selectedComercial" />
              </v-col>
            </v-row>

            <v-row class="mx-2 mb-n6">
              <v-col>
                <v-text-field v-model="valorProyectoSeleccionado" label="Modificar Valor Proyecto" variant="outlined"
                  clearable v-if="selectedProyecto" type="number" />
              </v-col>
            </v-row>

            <v-card-actions class="mt-5">
              <v-btn @click="save_valor_proyecto()" color="#006CA1" class="mb-4" variant="flat">Guardar Cambios</v-btn>
              <v-btn @click="
                  dialogValorProyectos = false;
                  selectedComercial = null;
                  selectedProyecto = null;
                  valorProyectoSeleccionado = 0;
                " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!----- Dialogo para cambiar el valor de los proyectos ----->

        <!----- Dialogo para las alertas ----->
        <v-dialog v-model="alerta" persistent style="z-index: 10000">
          <v-card :style="getAlertStyle()">
            <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
              class="mx-auto"></v-progress-circular>
            <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center"></v-card-tittle>
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
              <v-text-field v-model="claveActual" label="Clave Actual" :type="mostrarClaveActual ? 'text' : 'password'"
                variant="outlined" required clearable>
                <template v-slot:append-inner>
                  <v-icon :icon="mostrarClaveActual ? 'mdi-eye' : 'mdi-eye-closed'"
                    @click="mostrarClaveActual = !mostrarClaveActual" />
                </template>
              </v-text-field>
              <v-text-field v-model="nuevaClave" label="Nueva Clave" :type="mostrarNuevaClave ? 'text' : 'password'"
                variant="outlined" required clearable>
                <template v-slot:append-inner>
                  <v-icon :icon="mostrarNuevaClave ? 'mdi-eye' : 'mdi-eye-closed'"
                    @click="mostrarNuevaClave = !mostrarNuevaClave" />
                </template>
              </v-text-field>
              <div class="text-caption mt-n4 mb-4" style="color: red" v-if="nuevaClave && !isValidPassword(nuevaClave)">
                La nueva clave debe tener al menos una mayúscula, un número, un
                caracter especial y mínimo 8 caracteres.
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
              <v-btn variant="flat" color="grey" @click="
                  dialogCambioClave = false;
                  claveActual = null;
                  nuevaClave = null;
                  confirmarClave = null;
                ">Cancelar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!----- Dialogo para ROLES IA ----->
        <v-dialog v-model="dialogRolesIA" persistent width="75%">
          <v-card style="border-radius: 20px; height: 100%" class="custom-scroll">
            <v-card-title class="text-h6 pa-4 d-flex"
              style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon class="mr-4">mdi-robot-confused</v-icon>
              Roles IA
              <v-spacer></v-spacer>
              <v-btn color="#0280bf" dark
                @click="abrirCrearRolIA(); dialogAsistenteRolIA = true; this.asistente.promptFinal = this.generarPromptFinal()"
                class="ml-2" elevation="2">
                <v-icon class="mr-2" left>mdi mdi-robot-happy</v-icon> Nuevo Rol
              </v-btn>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2 d-flex justify-space-between align-center"
              style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">Roles ({{ selectRolIA.length }})</div>
              <v-text-field v-model="searchRolIA" placeholder="Buscar en Roles IA" outlined
                prepend-inner-icon="mdi-magnify" density="compact" variant="solo" clearable class="header-search ml-4"
                hide-details style="max-width: 500px; background: white; border-radius: 8px;" />
            </v-card-subtitle>
            <v-card-text style="height: 100%" class="custom-scroll">
              <v-data-table :headers="headersRolesIA" :items="selectRolIA"
                :filter-keys="['id', 'activo', 'nombre', 'rol_content', 'usuario']" :search="searchRolIA"
                class="elevation-1 data-table-campanas fancy-headers fancy-rows" :items-per-page="10"
                style="background: #f8fafd">
                <!-- Header slots con íconos -->
                <template #header.id="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-numeric</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.activo="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-check-circle-outline</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.nombre="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-account-tie</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.rol_content="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-text-box-outline</v-icon>
                    <span>Contenido del Rol</span>
                  </div>
                </template>
                <template #header.usuario="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-account-circle</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.opciones="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-tools</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>


                <template v-slot:item.rol_content="{ item }">
                  <div @click="verRolCompleto(item)" class="btn-grow-card-items">
                    <span>
                      {{ item.rol_content.length > 200 ? item.rol_content.slice(0, 200) + '(...Ver más)' :
                      item.rol_content }}
                    </span>
                  </div>
                </template>
                <template v-slot:item.activo="{ item }">
                  <v-chip :color="item.activo === 'Activo' ? 'green' : 'red'" dark>
                    {{ item.activo }}
                  </v-chip>
                </template>
                <template v-slot:item.opciones="{ item }">
                  <div class="d-flex justify-center">
                    <v-btn size="35" icon color="primary" @click="editarRolIA(item)">
                      <v-icon size="20">mdi-pencil</v-icon>
                    </v-btn>
                  </div>
                </template>
              </v-data-table>
            </v-card-text>
            <v-card-actions class="mt-2">
              <v-btn @click="
            dialogRolesIA = false;
            " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>


          </v-card>

          <!-- Diálogo para ver rol_content completo -->
          <v-dialog v-model="dialogRolCompleto" max-width="1000px">
            <v-card style="border-radius: 18px; box-shadow: 0 8px 32px rgba(25, 118, 210, 0.12);">
              <v-card-title class="d-flex align-center"
                style="background: #006ca1; color: white; font-weight: bold; border-top-left-radius: 18px; border-top-right-radius: 18px;">
                <v-icon class="mr-2" size="28">mdi-robot-confused</v-icon>
                Detalle Rol
                <v-spacer />
                <v-btn icon color="white" @click="dialogRolCompleto = false" aria-label="Cerrar">
                  <v-icon>mdi-close</v-icon>
                </v-btn>
              </v-card-title>
              <v-card-text
                style="background: #f8fafd; max-height: 700px; overflow-y: auto; font-size: 0.9rem; color: #222; padding: 24px;">
                <pre
                  style="white-space: pre-wrap; font-family: inherit; background: #f3f6fa; border-radius: 10px; margin: 0; text-align: justify;">
        {{ rolSeleccionado.rol_content }}
      </pre>
              </v-card-text>
              <v-card-actions class="justify-end" style="padding: 16px;">
                <v-btn color="primary" variant="flat" rounded="lg" @click="dialogRolCompleto = false">
                  <v-icon left>mdi-check-circle</v-icon>
                  Cerrar
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-dialog>
        <!----- Dialogo para Ver ROl-content completo----->

        <!----- DIALOGO PARA CREAR/EDITAR ROL IA ----->
        <v-dialog v-model="dialogCrearRolIA" persistent max-width="700px">
          <v-card style="border-radius: 18px;">
            <v-card-title class="d-flex align-center" style="background: #006ca1; color: white; font-weight: bold;">

              <v-icon v-if="!editandoRolIA" class="mr-2" size="28">mdi-robot-happy</v-icon>
              <span v-if="!editandoRolIA">Crear Nuevo Rol IA</span>

              <v-icon v-if="editandoRolIA" class="mr-2" size="28">mdi mdi-robot</v-icon>
              <span v-if="editandoRolIA">Editar Rol IA</span>
              <v-spacer />

              <v-btn class="btn-grow-card" size="35" icon color="white" @click="cerrardialogCrearRolIA"
                aria-label="Cerrar">
                <v-icon size="20">mdi-close</v-icon>
              </v-btn>

            </v-card-title>
            <v-card-text style="background: #f8fafd; padding: 24px;">
              <v-row class="justify-center">
                <v-col cols="12" md="12">
                  <v-icon color="#006ca1" class="mr-2">mdi-account-tie</v-icon>
                  <span class="font-weight-bold" style="color:#006ca1;">Nombre del Rol</span>
                  <v-text-field v-model="nuevoRolNombre" class="mt-4" label="Nombre" variant="outlined" clearable
                    required prepend-inner-icon="mdi-account-tie" :rules="[v => !!v || 'El nombre es obligatorio']"
                    maxlength="80" />
                  <div class="word-preview-container">
                    <div class="word-preview-toolbar d-flex align-center mb-2">
                      <v-icon color="#006ca1" class="mr-2">mdi-file-word-box</v-icon>
                      <span class="font-weight-bold" style="color:#006ca1;">Contenido del Rol</span>
                      <v-spacer />
                      <v-tooltip text="Asistente de creación de Roles IA" location="top">
                        <template v-slot:activator="{ props }">
                          <v-btn v-bind="props" class="mr-2 btn-grow-card" icon size="small" color="primary"
                            @click="dialogAsistenteRolIA = true; resetAsistenteRolIA(); this.asistente.promptFinal = this.generarPromptFinal()">
                            <v-icon>mdi mdi-robot-confused</v-icon>
                          </v-btn>
                        </template>
                        <span>Asistente de creación de Roles IA</span>

                      </v-tooltip>
                      <!--<v-btn icon size="small" color="primary" @click="pegarDesdeWord" title="Pegar desde Word">
                      <v-icon>mdi-content-paste</v-icon>
                    </v-btn> -->
                    </div>
                    <div :class="['word-preview']">
                      <v-textarea v-model="nuevoRolContenido" label="Escribe o pega aquí el contenido del rol"
                        variant="plain" auto-grow rows="12"
                        style="background: transparent; font-size: 0.8rem; min-height: 220px; resize: none;" />
                    </div>
                  </div>
                  <v-switch v-if="editandoRolIA" v-model="nuevoRolActivo" label="Activar Rol" color="primary"
                    prepend-icon="mdi-check-circle-outline" />
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions class="justify-end" style="padding: 16px;">
              <v-btn v-if="!editandoRolIA" class="btn-grow-card" color="primary" variant="flat" rounded="lg"
                @click="guardarNuevoRolIA">
                <v-icon left>mdi-content-save-check-outline</v-icon>
                Guardar
              </v-btn>
              <v-btn v-if="editandoRolIA" class="btn-grow-card" color="primary" variant="flat" rounded="lg"
                @click="editarNuevoRolIA">
                <v-icon left>mdi-content-save-check-outline</v-icon>
                Actualizar
              </v-btn>
              <v-btn class="btn-grow-card" color="grey" variant="flat" rounded="lg" @click="cerrardialogCrearRolIA">
                <v-icon left>mdi-close-circle</v-icon>
                Cancelar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!----- DIALOGO PARA CREAR/EDITAR ROL IA ----->
        <!-- Diálogo Asistente de Creación de Rol IA -->
        <v-dialog v-model="dialogAsistenteRolIA" persistent max-width="1200px" @open="resetAsistenteRolIA()">
          <v-card style="border-radius: 18px;">
            <v-card-title class="d-flex align-center" style="background: #006ca1; color: white; font-weight: bold;">
              <v-icon class="mr-2" size="28">mdi-robot-happy</v-icon>
              Asistente para Crear Rol IA
              <v-spacer />
              <v-btn class="btn-grow-card" size="35" icon color="white" @click="cerrardialogAsistenteRolIA"
                aria-label="Cerrar">
                <v-icon size="20">mdi-close</v-icon>
              </v-btn>
            </v-card-title>
            <v-card-text style="background: #f8fafd; padding: 24px;">
              <!-- Stepper arriba -->
              <div class="asistente-stepper-bar mb-4">
                <v-stepper v-model="asistentePaso" elevation="0" class="asistente-stepper" editable>
                  <v-stepper-header>
                    <v-stepper-step v-for="n in 10" :key="n" :complete="asistentePaso > n" :step="n"
                      :color="asistentePaso === n ? '#fff' : '#fff'"
                      :class="asistentePaso === n ? 'asistente-stepper-step-active' : ''">
                      {{ asistenteLabels[n-1] }}
                    </v-stepper-step>
                  </v-stepper-header>
                </v-stepper>
              </div>
              <!-- Dos columnas -->
              <v-row class="asistente-rol-layout" no-gutters>
                <!-- Columna izquierda: paso actual -->
                <v-col cols="12" md="5" class="asistente-rol-form">
                  <!-- Paso 1: Área -->
                  <div v-if="asistentePaso === 1">
                    <b>¿Cuál es el área del asistente?</b>
                    <v-text-field v-model="asistente.area" label="Área (Ej: Mercadeo, Ventas, Soporte...)"
                      variant="outlined" />
                    <div class="mt-3" style="color:#666; font-size:0.97rem;">
                      <b>Ejemplo:</b> <span style="color:#0280bf;">Mercadeo</span>, <span style="color:#0280bf;">Soporte
                        Técnico</span>
                    </div>
                  </div>
                  <!-- Paso 2: Nombre de la empresa -->
                  <div v-if="asistentePaso === 2">
                    <b>¿Cómo se llama la empresa?</b>
                    <v-text-field v-model="asistente.nombreEmpresa"
                      label="Nombre de la empresa (Ej: SIICSA, La Duquesa Restaurante)" variant="outlined" />
                    <div class="mt-3" style="color:#666; font-size:0.97rem;">
                      <b>Ejemplo:</b> <span style="color:#0280bf;">SIICSA</span>, <span style="color:#0280bf;">La
                        Duquesa Restaurante</span>
                    </div>
                  </div>
                  <!-- Paso 3: Dirección para el público -->
                  <div v-if="asistentePaso === 3">
                    <b>¿Cuál es la dirección para el público?</b>
                    <v-text-field v-model="asistente.direccionPublico" label="Dirección (Ej: Calle 123 #45-67, Bogotá)"
                      variant="outlined" />
                    <div class="mt-3" style="color:#666; font-size:0.97rem;">
                      <b>Ejemplo:</b> <span style="color:#0280bf;">Calle 123 #45-67, Bogotá</span>
                    </div>
                  </div>
                  <!-- Paso 4: Productos y servicios -->
                  <div v-if="asistentePaso === 4">
                    <div v-if="!asistente.serviciosBot.length" class="text-center my-4">
                      <v-icon color="#0280bf" size="40">mdi-briefcase-outline</v-icon>
                      <div style="color:#888;">No has añadido ningún servicio aún.</div>
                      <v-btn color="primary" class="mt-2" @click="agregarServicioVacio">
                        <v-icon left>mdi-plus</v-icon> Añadir servicio
                      </v-btn>
                      <div class="mt-4" style="color:#666; font-size:0.97rem;">
                        <b>Ejemplo:</b><br>
                        <span style="color:#0280bf;">Título:</span> <i>Soporte Técnico</i><br>
                        <span style="color:#0280bf;">Descripción:</span> <i>Atención y solución de problemas técnicos
                          para nuestros clientes empresariales.</i>
                      </div>
                    </div>
                    <v-divider class="my-3"></v-divider>
                    <div v-if="asistente.serviciosBot.length">
                      <b>Portafolio añadidos:</b>
                      <v-btn size="small" class="ml-2" color="primary" @click="agregarServicioVacio">
                        <v-icon left>mdi-plus</v-icon> Añadir servicio
                      </v-btn>
                      <v-list>
                        <v-list-item v-for="(servicio, i) in asistente.serviciosBot" :key="i" class="mb-2">
                          <v-card elevation="1" class="pa-2 servicio-card" style="max-width: 500px; min-width: 220px;">
                            <v-card-title class="d-flex align-center py-2 px-3"
                              style="background: #006ca1; color: white; font-weight: bold; border-radius: 10px 10px 0 0;">
                              <v-icon class="mr-2" size="18">mdi-briefcase-outline</v-icon>
                              <input v-model="servicio.nombre" type="text"
                                placeholder="Título del servicio (Ej: Soporte Técnico)"
                                class="servicio-input servicio-input-nombre" />
                              <v-spacer />
                              <div class="d-flex justify-end mt-2">
                                <v-btn icon color="red" @click="eliminarServicio(i)" title="Eliminar servicio">
                                  <v-icon>mdi-delete</v-icon>
                                </v-btn>
                              </div>
                            </v-card-title>
                            <v-card-text class="py-2 px-3" style="background: #f7fbff; border-radius: 0 0 10px 10px;">
                              <textarea v-model="servicio.descripcion"
                                placeholder="Descripción breve (Ej: Atención y solución de problemas técnicos para nuestros clientes empresariales.)"
                                class="servicio-input servicio-input-desc" rows="10"></textarea>
                            </v-card-text>
                          </v-card>
                        </v-list-item>
                      </v-list>
                      <div class="mt-4" style="color:#666; font-size:0.97rem;">
                        <b>Ejemplo:</b><br>
                        <span style="color:#0280bf;">Título:</span> <i>Consultoría en Transformación Digital</i><br>
                        <span style="color:#0280bf;">Descripción:</span> <i>Asesoría personalizada para empresas que
                          buscan optimizar sus procesos mediante tecnología.</i>
                      </div>
                    </div>
                  </div>
                  <!-- Paso 5: Web y contacto -->
                  <div v-if="asistentePaso === 5">
                    <b>¿Cuál es la dirección web y el número de contacto principal?</b>
                    <v-text-field v-model="asistente.web" label="Dirección web (Ej: www.empresa.com)"
                      variant="outlined" />
                    <v-text-field v-model="asistente.contacto"
                      label="Número de contacto principal (Ej: +57 123 4567890)" variant="outlined" />
                    <div class="mt-3" style="color:#666; font-size:0.97rem;">
                      <b>Ejemplo:</b> <br>
                      <span style="color:#0280bf;">Web:</span> <i>www.empresa.com</i><br>
                      <span style="color:#0280bf;">Contacto:</span> <i>+57 123 4567890</i>
                    </div>
                  </div>
                  <!-- Paso 6: Idiomas y tonos -->
                  <div v-if="asistentePaso === 6">
                    <b>¿En qué idiomas habla el asistente?</b>
                    <v-text-field v-model="asistente.idiomas" label="Idiomas (Ej: Español, Inglés...)"
                      variant="outlined" />
                    <b class="mt-4">¿Con qué tono hablará el bot?</b>
                    <v-text-field v-model="asistente.tonos" label="Tonos (Ej: Formal, Cercano, Juvenil...)"
                      variant="outlined" />
                    <div class="mt-3" style="color:#666; font-size:0.97rem;">
                      <b>Ejemplo:</b> <br>
                      <span style="color:#0280bf;">Idiomas:</span> <i>Español, Inglés</i><br>
                      <span style="color:#0280bf;">Tonos:</span> <i>Formal corporativo, Cercano/familiar</i>
                    </div>
                  </div>
                  <!-- Paso 7: Objetivos de conversación -->
                  <div v-if="asistentePaso === 7">
                    <div v-if="!asistente.objetivosBot?.length" class="text-center my-4">
                      <v-icon color="#0280bf" size="40">mdi-lightbulb-on-outline</v-icon>
                      <div style="color:#888;">No has añadido ningún objetivo aún.</div>
                      <v-btn color="primary" class="mt-2" @click="agregarObjetivoVacio">
                        <v-icon left>mdi-plus</v-icon> Añadir objetivo
                      </v-btn>
                      <div class="mt-4" style="color:#666; font-size:0.97rem;">
                        <b>Ejemplo:</b><br>
                        <span style="color:#0280bf;">Título:</span> <i>Informar sobre productos</i><br>
                        <span style="color:#0280bf;">Descripción:</span> <i>Brindar información clara sobre los
                          productos y servicios ofrecidos.</i>
                      </div>
                    </div>
                    <v-divider class="my-3"></v-divider>
                    <div v-if="asistente.objetivosBot?.length">
                      <b>Objetivos añadidos:</b>
                      <v-btn size="small" class="ml-2" color="primary" @click="agregarObjetivoVacio">
                        <v-icon left>mdi-plus</v-icon> Añadir objetivo
                      </v-btn>
                      <v-list>
                        <v-list-item v-for="(objetivo, i) in asistente.objetivosBot" :key="i" class="mb-2">
                          <v-card elevation="1" class="pa-2 servicio-card" style="max-width: 500px; min-width: 220px;">
                            <v-card-title class="d-flex align-center py-2 px-3"
                              style="background: #006ca1; color: white; font-weight: bold; border-radius: 10px 10px 0 0;">
                              <v-icon class="mr-2" size="18">mdi-lightbulb-on-outline</v-icon>
                              <input v-model="objetivo.titulo" type="text"
                                placeholder="Título del objetivo (Ej: Informar sobre productos)"
                                class="servicio-input servicio-input-nombre" />
                              <v-spacer />
                              <div class="d-flex justify-end mt-2">
                                <v-btn icon color="red" @click="eliminarObjetivo(i)" title="Eliminar objetivo">
                                  <v-icon>mdi-delete</v-icon>
                                </v-btn>
                              </div>
                            </v-card-title>
                            <v-card-text class="py-2 px-3" style="background: #f7fbff; border-radius: 0 0 10px 10px;">
                              <textarea v-model="objetivo.descripcion"
                                placeholder="Descripción breve (Ej: Brindar información clara sobre los productos y servicios ofrecidos.)"
                                class="servicio-input servicio-input-desc" rows="3"></textarea>
                            </v-card-text>
                          </v-card>
                        </v-list-item>
                      </v-list>
                      <div class="mt-4" style="color:#666; font-size:0.97rem;">
                        <b>Ejemplo:</b><br>
                        <span style="color:#0280bf;">Título:</span> <i>Clasificar interés</i><br>
                        <span style="color:#0280bf;">Descripción:</span> <i>Detectar y clasificar el grado de interés
                          del cliente según el producto consultado.</i>
                      </div>
                    </div>
                  </div>
                  <!-- Paso 8: Reglas de cobertura iniciales (con cards estilo servicios) -->
                  <div v-if="asistentePaso === 8">
                    <div v-if="!asistente.reglasCoberturaBot?.length" class="text-center my-4">
                      <v-icon color="#0280bf" size="40">mdi-shield-check-outline</v-icon>
                      <div style="color:#888;">No has añadido ninguna regla aún.</div>
                      <v-btn color="primary" class="mt-2" @click="agregarReglaCoberturaVacia">
                        <v-icon left>mdi-plus</v-icon> Añadir regla
                      </v-btn>
                      <div class="mt-4" style="color:#666; font-size:0.97rem;">
                        <b>Ejemplo:</b><br>
                        <span style="color:#0280bf;">Título:</span> <i>¿Quiénes son?</i><br>
                        <span style="color:#0280bf;">Descripción:</span> <i>Si preguntan “¿quiénes son?” ? presenta
                          brevemente.</i>
                      </div>
                    </div>
                    <v-divider class="my-3"></v-divider>
                    <div v-if="asistente.reglasCoberturaBot?.length">
                      <b>Reglas añadidas:</b>
                      <v-btn size="small" class="ml-2" color="primary" @click="agregarReglaCoberturaVacia">
                        <v-icon left>mdi-plus</v-icon> Añadir regla
                      </v-btn>
                      <v-list>
                        <v-list-item v-for="(regla, i) in asistente.reglasCoberturaBot" :key="i" class="mb-2">
                          <v-card elevation="1" class="pa-2 servicio-card" style="max-width: 500px; min-width: 220px;">
                            <v-card-title class="d-flex align-center py-2 px-3"
                              style="background: #006ca1; color: white; font-weight: bold; border-radius: 10px 10px 0 0;">
                              <v-icon class="mr-2" size="18">mdi-shield-check-outline</v-icon>
                              <input v-model="regla.titulo" type="text"
                                placeholder="Título de la regla (Ej: ¿Quiénes son?)"
                                class="servicio-input servicio-input-nombre" />
                              <v-spacer />
                              <div class="d-flex justify-end mt-2">
                                <v-btn icon color="red" @click="eliminarReglaCobertura(i)" title="Eliminar regla">
                                  <v-icon>mdi-delete</v-icon>
                                </v-btn>
                              </div>
                            </v-card-title>
                            <v-card-text class="py-2 px-3" style="background: #f7fbff; border-radius: 0 0 10px 10px;">
                              <textarea v-model="regla.descripcion"
                                placeholder="Descripción breve (Ej: Presenta brevemente la empresa (sin calificación).)"
                                class="servicio-input servicio-input-desc" rows="3"></textarea>
                            </v-card-text>
                          </v-card>
                        </v-list-item>
                      </v-list>
                      <div class="mt-4" style="color:#666; font-size:0.97rem;">
                        <b>Ejemplo:</b><br>
                        <span style="color:#0280bf;">Título:</span> <i>Producto fuera de portafolio</i><br>
                        <span style="color:#0280bf;">Descripción:</span> <i>Si no está en el portafolio, informa que
                          será comunicado con un Analista de Mercadeo.</i>
                      </div>
                    </div>
                  </div>
                  <!-- Paso 9: Preview final -->
                  <div v-if="asistentePaso === 9" class="d-flex flex-column align-center justify-center"
                    style="min-height: 320px;">
                    <v-icon color="#0280bf" size="48" class="mb-2">mdi-eye-check-outline</v-icon>
                    <h3 class="font-weight-bold mb-2" style="color:#006ca1;">¡Revisa tu Prompt Final!</h3>
                    <div class="mb-4" style="color:#444; font-size:1.08rem; max-width: 420px; text-align: center;">
                      Antes de guardar, verifica que toda la información esté correcta y completa.<br>
                      Puedes editar el contenido en el panel derecho si lo deseas.
                    </div>
                    <v-btn color="primary" class="mt-2" @click="guardarPromptEnRolContenido">
                      <v-icon left>mdi-content-save-check-outline</v-icon>
                      Usar este prompt en el Rol IA
                    </v-btn>
                  </div>
                  <!-- Navegación -->
                  <div class="asistente-rol-nav mt-4">
                    <v-btn color="grey" v-if="asistentePaso > 1" @click="asistentePaso--">Atrás</v-btn>
                    <v-btn color="primary" v-if="asistentePaso < 9"
                      @click="asistentePaso++; this.asistente.promptFinal = this.generarPromptFinal()"
                      class="ml-2">Siguiente</v-btn>
                  </div>
                </v-col>
                <!-- Columna derecha: preview editable -->
                <v-col cols="12" md="7" class="asistente-rol-preview">
                  <div class="preview-title mb-2">
                    <v-icon color="#006ca1" class="mr-2">mdi-file-word-box</v-icon>
                    <span class="font-weight-bold" style="color:#006ca1;">Preview del Rol IA</span>
                  </div>
                  <v-textarea v-model="asistente.promptFinal" label="Prompt generado (editable)" variant="outlined"
                    auto-grow rows="16" style="background: #f3f6fa; font-size: 0.95rem;"
                    :disabled="asistentePaso !== 9" />
                  <v-btn color="primary" class="mt-2" @click="guardarPromptEnRolContenido" v-if="asistentePaso === 9">
                    <v-icon left>mdi-content-save-check-outline</v-icon>
                    Usar este prompt en el Rol IA
                  </v-btn>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-dialog>

        <!----- DIALOGO PARA CREAR/EDITAR INTENCION IA ----->
        <v-dialog v-model="dialogCrearIntencionIA" persistent max-width="700px">
          <v-card style="border-radius: 18px;">
            <v-card-title class="d-flex align-center" style="background: #006ca1; color: white; font-weight: bold;">
              <v-icon v-if="!editandoIntencionIA" class="mr-2" size="28">mdi-file-document-plus</v-icon>
              <span v-if="!editandoIntencionIA">Crear nueva Intención IA</span>
              <v-icon v-if="editandoIntencionIA" class="mr-2" size="28">mdi-file-document-edit</v-icon>
              <span v-if="editandoIntencionIA">Editar Intención IA</span>
              <v-spacer />
              <v-btn class="btn-grow-card" size="35" icon color="white" @click="cerrardialogCrearIntencionIA"
                aria-label="Cerrar">
                <v-icon size="20">mdi-close</v-icon>
              </v-btn>
            </v-card-title>
            <v-card-text style="background: #f8fafd; padding: 24px;">
              <v-row class="justify-center">
                <v-col cols="12" md="12">
                  <v-icon color="#006ca1" class="mr-2">mdi mdi-robot</v-icon>
                  <span class="font-weight-bold" style="color:#006ca1;">Rol de la Intención</span>
                  <v-select v-model="intencionRol" :items="selectRolIA" item-title="nombre" item-value="id" class="mt-4"
                    label="Rol IA" variant="outlined" clearable required prepend-inner-icon="mdi mdi-robot" />
                  <v-icon color="#006ca1" class="mr-2">mdi mdi-text-box-search</v-icon>
                  <span class="font-weight-bold" style="color:#006ca1;">Nombre de la Intención</span>
                  <v-text-field v-model="intencionNombre" class="mt-4" label="Nombre" variant="outlined" clearable
                    required prepend-inner-icon="mdi mdi-text-box-search"
                    :rules="[v => !!v || 'El nombre es obligatorio']" maxlength="80" />

                  <span class="font-weight-bold d-flex" style="color:#006ca1;"> <v-icon color="#006ca1"
                      class="mr-2">mdi-file-pdf-box</v-icon>PDF de la Intención
                    <!-- Mostrar el PDF actual si existe y no se ha seleccionado uno nuevo -->
                    <v-spacer></v-spacer>
                    <a v-if="editandoIntencionIA && intencionEditando?.url && !pdfIntencion"
                      :href="intencionEditando.url" target="_blank" style="color:#006ca1; font-weight:500;">
                      <v-icon color="#006ca1" class="mr-2">mdi mdi-file-document-check</v-icon> Ver PDF actual
                    </a>
                  </span>

                  <v-file-input v-model="pdfIntencion" class="mt-4" label="Adjuntar PDF" variant="outlined" clearable
                    accept=".pdf" prepend-inner-icon="mdi-file-pdf-box" @change="leerPDFIntencion" />

                  <p v-if="editandoIntencionIA && !intencionEditando?.url && !pdfIntencion">No hay un archivo PDF subido
                    para esta intención.</p>

                  <div class="word-preview-container">
                    <div class="word-preview-toolbar d-flex align-center mb-2">
                      <v-icon color="#006ca1" class="mr-2">mdi-file-pdf-box</v-icon>
                      <span class="font-weight-bold" style="color:#006ca1;">Visualización y Edición de Contenido</span>
                      <v-spacer />
                    </div>
                    <div :class="['word-preview']">
                      <v-textarea v-model="intencionContenido" label="Contenido extraído del PDF (puede editarlo)"
                        variant="plain" auto-grow rows="12"
                        style="background: transparent; font-size: 0.8rem; min-height: 220px; resize: none;" />
                    </div>
                  </div>
                  <v-switch v-if="editandoIntencionIA" v-model="intencionActivo" label="Activar Intención"
                    color="primary" prepend-icon="mdi-check-circle-outline" />
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions class="justify-end" style="padding: 16px;">
              <v-btn v-if="!editandoIntencionIA" class="btn-grow-card" color="primary" variant="flat" rounded="lg"
                @click="guardarNuevaIntencionIA">
                <v-icon left>mdi-content-save-check-outline</v-icon>
                Guardar
              </v-btn>
              <v-btn v-if="editandoIntencionIA" class="btn-grow-card" color="primary" variant="flat" rounded="lg"
                @click="editarNuevaIntencionIA">
                <v-icon left>mdi-content-save-check-outline</v-icon>
                Actualizar
              </v-btn>
              <v-btn class="btn-grow-card" color="grey" variant="flat" rounded="lg"
                @click="cerrardialogCrearIntencionIA">
                <v-icon left>mdi-close-circle</v-icon>
                Cancelar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!----- Dialogo para Intencion IA ----->
        <v-dialog v-model="dialogIntencionIA" persistent width="90%">
          <v-card style="border-radius: 20px; height: 100%" class="custom-scroll">
            <v-card-title class="text-h6 pa-4 d-flex"
              style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon class="mr-4">mdi mdi-text-box-search</v-icon>
              Intencion IA
              <v-spacer></v-spacer>
              <v-btn color="#0280bf" dark @click="abrirCrearIntencionIA" class="ml-2" elevation="2">
                <v-icon class="mr-2" left>mdi mdi-file-document-plus</v-icon> Nueva Intención
              </v-btn>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2 d-flex align-center justify-space-between"
              style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">Intencion ({{ selectIntencionIA.length }})</div>
              <v-text-field v-model="searchIntencionIA" placeholder="Buscar en Intencion IA" outlined
                prepend-inner-icon="mdi-magnify" density="compact" variant="solo" clearable class="header-search ml-4"
                hide-details style="max-width: 500px; background: white; border-radius: 8px;" />
            </v-card-subtitle>
            <v-card-text style="height: 100%" class="custom-scroll">
              <v-data-table :headers="headersIntencionIA" :items="selectIntencionIA" :search="searchIntencionIA"
                :filter-keys="['id', 'intencion', 'idconte', 'contenidopdf', 'url', 'fecha', 'activo']"
                class="elevation-1 data-table-campanas fancy-headers fancy-rows" :items-per-page="10"
                style="background: #f8fafd">
                <!-- Header slots con íconos -->
                <template #header.id="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-numeric</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.activo="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-check-circle-outline</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.intencion="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-account-tie</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.url="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-text-box-outline</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.contenidopdf="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-account-circle</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.fecha="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-account-circle</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.opciones="{ column }">
                  <div class="th-content d-flex align-center justify-center">
                    <v-icon size="18" color="#fff" class="mr-2">mdi-tools</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>

                <template v-slot:item.contenidopdf="{ item }">
                  <div @click="verIntencionCompleto(item)" class="btn-grow-card-items" style="">
                    <span>
                      {{
                      item.contenidopdf
                      ? item.contenidopdf.replace(/[\r\n]+/g, ' ').replace(/\s{2,}/g, ' ').trim().slice(0, 180) +
                      (item.contenidopdf.length > 120 ? '... (Ver más)' : '')
                      : ''
                      }}
                    </span>
                  </div>
                </template>
                <template v-slot:item.idconte="{ item }">
                  <span>
                    {{
                    (selectRolIA.find(r => r.id == item.idconte) || {}).nombre || item.idconte
                    }}
                  </span>
                </template>

                <template v-slot:item.fecha="{ item }">
                  <span>
                    {{ formatFecha2(item.fecha) }}
                  </span>

                </template>

                <template v-slot:item.url="{ item }">
                  <div style="">
                    <a v-if="item.url" :href="item.url" target="_blank">
                      Ver link del PDF
                    </a>
                    <p v-if="!item.url">
                      No se asigno un documento PDF
                    </p>
                  </div>
                </template>

                <template v-slot:item.activo="{ item }">
                  <v-chip :color="item.activo === 'Activo' ? 'green' : 'red'" dark>
                    {{ item.activo }}
                  </v-chip>
                </template>
                <template v-slot:item.opciones="{ item }">
                  <div class="d-flex justify-center">
                    <v-btn size="35" icon color="primary" @click="editarIntencionIA(item)">
                      <v-icon size="20">mdi-pencil</v-icon>
                    </v-btn>
                  </div>
                </template>

                <template v-slot:item.id="{ index }">
                  <span>{{ index + 1 }}</span>
                </template>
              </v-data-table>
            </v-card-text>
            <v-card-actions class="mt-2">
              <v-btn @click="
             dialogIntencionIA = false;
            " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>


          </v-card>

          <!-- Diálogo para ver rol_content completo -->
          <v-dialog v-model="dialogRolCompleto" max-width="1000px">
            <v-card style="border-radius: 18px; box-shadow: 0 8px 32px rgba(25, 118, 210, 0.12);">
              <v-card-title class="d-flex align-center"
                style="background: #006ca1; color: white; font-weight: bold; border-top-left-radius: 18px; border-top-right-radius: 18px;">
                <v-icon class="mr-2" size="28">mdi-robot-confused</v-icon>
                Detalle Rol
                <v-spacer />
                <v-btn icon color="white" @click="dialogRolCompleto = false" aria-label="Cerrar">
                  <v-icon>mdi-close</v-icon>
                </v-btn>
              </v-card-title>
              <v-card-text
                style="background: #f8fafd; max-height: 700px; overflow-y: auto; font-size: 0.9rem; color: #222; padding: 24px;">
                <pre
                  style="white-space: pre-wrap; font-family: inherit; background: #f3f6fa; border-radius: 10px; margin: 0; text-align: justify;">
        {{ rolSeleccionado.rol_content }}
      </pre>
              </v-card-text>
              <v-card-actions class="justify-end" style="padding: 16px;">
                <v-btn color="primary" variant="flat" rounded="lg" @click="dialogRolCompleto = false">
                  <v-icon left>mdi-check-circle</v-icon>
                  Cerrar
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <!-- Diálogo para ver Intención completo -->
          <v-dialog v-model="dialogIntencionCompleto" max-width="1000px">
            <v-card style="border-radius: 18px; box-shadow: 0 8px 32px rgba(25, 118, 210, 0.12);">
              <v-card-title class="d-flex align-center"
                style="background: #006ca1; color: white; font-weight: bold; border-top-left-radius: 18px; border-top-right-radius: 18px;">
                <v-icon class="mr-2" size="28">mdi mdi-file-document-edit</v-icon>
                Detalle de Intencion
                <v-spacer />
                <v-btn icon color="white" @click="dialogIntencionCompleto = false" aria-label="Cerrar">
                  <v-icon>mdi-close</v-icon>
                </v-btn>
              </v-card-title>
              <v-card-text
                style="background: #f8fafd; max-height: 700px; overflow-y: auto; font-size: 0.9rem; color: #222; padding: 24px;">
                <pre
                  style="white-space: pre-wrap; font-family: inherit; background: #f3f6fa; border-radius: 10px; margin: 0; text-align: justify;">
                  {{ intencionSeleccionado.contenidopdf }}
                </pre>
              </v-card-text>
              <v-card-actions class="justify-end" style="padding: 16px;">
                <v-btn color="primary" variant="flat" rounded="lg" @click="dialogIntencionCompleto = false">
                  <v-icon left>mdi-check-circle</v-icon>
                  Cerrar
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-dialog>
        <!----- Dialogo para Ver Intención completo completo----->

        <!----- Dialogo para Preguntas Frecuentes----->
        <v-dialog v-model="dialogPreguntasF" persistent width="90%">
          <v-card style="border-radius: 20px; height: 100%" class="custom-scroll">
            <v-card-title class="text-h6 pa-4 d-flex"
              style="color: white; font-weight: bold; background-color: #006ca1">
              <v-icon class="mr-4">mdi mdi-frequently-asked-questions</v-icon>
              Preguntas y Respuestas IA
              <v-spacer></v-spacer>
              <v-btn color="#0280bf" @click="dialogPreguntaNueva = true" style="float: right;"><v-icon class="mr-2">mdi
                  mdi-comment-question</v-icon>
                Agregar una pregunta</v-btn>
            </v-card-title>
            <v-card-subtitle class="text-h6 pa-2 d-flex align-center justify-space-between"
              style="color: white; font-weight: bold; background-color: #006ca1">
              <div class="mx-2">Intencion ({{ preguntasF.length }})</div>
              <v-text-field v-model="filtroPreguntasF" placeholder="Buscar en Preguntas y Respuestas IA" outlined
                prepend-inner-icon="mdi-magnify" density="compact" variant="solo" clearable class="header-search ml-4"
                hide-details style="max-width: 500px; background: white; border-radius: 8px;" />
            </v-card-subtitle>
            <v-card-text style="height: 100%" class="custom-scroll">
              <v-data-table :headers="headersPreguntasF" :items="preguntasF" :search="filtroPreguntasF"
                :filter-keys="['id', 'pregunta', 'respuesta', 'categoria', 'usuario', 'fecha', 'estado', 'prioridad',
                'idrol']"
                class="elevation-1 data-table-campanas fancy-headers fancy-rows-campanas"
                items-per-page-text="Preguntas por página" items-per-page="10" :items-per-page-options="[10, 20, 30]"
                style="height: 100%;" page-text="Preguntas de la ({0}) a la ({1}) de ({2})">

                <!--DATA  HEADERS-->
                <template #header.pregunta="{ column }">
                  <div class="th-content">
                    <v-icon size="16" class="mr-2" color="#ffffff">mdi-comment-question-outline</v-icon>
                    <span color="#ffffff">{{ column.title }}</span>
                  </div>
                </template>
                <template #header.fecha="{ column }">
                  <div class="th-content">
                    <v-icon size="16" class="mr-2" color="#ffffff">mdi mdi-send-clock</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.estado="{ column }">
                  <div class="th-content">
                    <v-icon size="16" class="mr-2" color="#ffffff">mdi-progress-check</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.idrol="{ column }">
                  <div class="th-content">
                    <v-icon size="16" class="mr-2" color="#ffffff">mdi-shield-account-outline</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template #header.opciones="{ column }">
                  <div class="th-content">
                    <v-icon size="16" class="mr-2" color="#ffffff">mdi-dots-vertical</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>

                <template v-slot:item.pregunta="{ item }">
                  <div class="texto-limitado">
                    {{ item.pregunta }}
                  </div>
                </template>

                <template #header.respuesta="{ column }">
                  <div class="th-content">
                    <v-icon size="16" class="mr-2" color="#ffffff">mdi-comment-check-outline</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>

                <template #header.usuario="{ column }">
                  <div class="th-content">
                    <v-icon size="16" class="mr-2" color="#ffffff">mdi mdi-account-search</v-icon>
                    <span>{{ column.title }}</span>
                  </div>
                </template>
                <template v-slot:item.categoria="{ item }">
                  <div size="small"> {{ getCategoríaNombre(item.categoria) }}
                  </div>
                </template>
                <template v-slot:item.estado="{ item }">
                  <v-chip :color="item.estado === 1 ? 'green' : item.estado === 0 ? 'red' : 'blue'" size="small"> {{
                    getEstadoNombre(item.estado) }}
                  </v-chip>
                </template>
                <template v-slot:item.prioridad="{ item }">
                  <v-chip :color="item.prioridad === 'Alta' ? 'red' : item.prioridad === 'Media' ? 'orange' : 'green'"
                    size="small">
                    {{ item.prioridad }}
                  </v-chip>
                </template>
                <template v-slot:item.usuario="{ item }">
                  <span>{{ item.usuario || 'Sin usuario' }}</span>
                </template>
                <!-- FECHA  -->
                <template #item.fecha="{ item }">
                  <span>
                    {{ formatFechaCorta(item.fecha_envio || item.fecha) }}
                  </span>
                </template>
                <template v-slot:item.idrol="{ item }">
                  <span>
                    <v-icon v-if="item.rolactivo === 0" color="red" size="18"
                      class="mr-1">mdi-alert-circle-outline</v-icon>
                    <v-chip v-if="item.rolactivo === 0" color="red lighten-4" text-color="red" size="x-small"
                      class="mr-1" style="font-weight: bold;">
                      Rol inactivo </br>
                    </v-chip>
                    {{ getCategoríaNombre(item.idrol) }}
                  </span>
                </template>
                <template v-slot:item.opciones="{ item }">
                  <v-tooltip text="Editar Pregunta Frecuente" location="top">
                    <template #activator="{ props }">
                      <div class="justify-center d-flex">
                        <v-btn v-bind="props" size="35" icon color="primary" @click="editarItemPregunta(item)"
                          class="btn-grow-card">
                          <v-icon size="15">mdi-pencil</v-icon>

                        </v-btn>
                      </div>
                    </template>
                  </v-tooltip>

                </template>

              </v-data-table>
            </v-card-text>
            <v-card-actions class="mt-2">
              <v-btn @click="
             dialogPreguntasF = false;
            " color="#006CA1" class="mb-4" variant="flat">Cerrar</v-btn>
            </v-card-actions>


          </v-card>
        </v-dialog>
        <!----- Dialogo para Ver Intención completo completo----->

        <!----- Dialogo Añadir Pregunta Frecuente-->
        <v-dialog v-model="dialogPreguntaNueva" max-width="600" persistent>
          <v-card style="border-radius: 18px;">
            <v-card-title class="d-flex align-center" style="background: #006ca1; color: white; font-weight: bold;">

              <v-icon v-if="!editandoPreguntaFrecuente" class="mr-2" size="28">mdi mdi-comment-question</v-icon>
              <span v-if="!editandoPreguntaFrecuente">Crear Pregunta Frecuente</span>

              <v-icon v-if="editandoPreguntaFrecuente" class="mr-2" size="28">mdi mdi-robot</v-icon>
              <span v-if="editandoPreguntaFrecuente">Editar Rol IA</span>
              <v-spacer />

              <v-btn class="btn-grow-card" size="35" icon color="white" @click="limpiarCamposNuevaPregunta()"
                aria-label="Cerrar">
                <v-icon size="20">mdi-close</v-icon>
              </v-btn>

            </v-card-title>
            <v-card-text style="background: #f8fafd; padding: 24px;">
              <v-alert v-if="rolInactivo" class="mx-0 mb-4 mt-2 modern-alert" type="error" prominent
                icon="mdi mdi-robot-off" style="font-size: 0.95rem;">
                <span style="font-weight: 500;">La pregunta se encuentra inhabilitada porque el rol seleccionado está
                  inactivo.</span>
              </v-alert>
              <v-row class="justify-center">
                <v-col cols="12" md="12">
                  <v-icon color="#006ca1" class="mr-2">mdi-account-tie</v-icon>
                  <span class="font-weight-bold" style="color:#006ca1;">Pregunta de IA</span>
                  <v-text-field v-model="nuevaPregunta" class="mt-4" label="Pregunta" variant="outlined" clearable
                    required prepend-inner-icon="mdi-account-tie" :disabled="idrolactivoPregunta === 0" />
                  <v-icon color="#006ca1" class="mr-2">mdi-account-tie</v-icon>
                  <span class="font-weight-bold" style="color:#006ca1;">Selecciona el rol de la pregunta</span>
                  <v-select v-model="rolNuevaPregunta" :items="selectRolIA" item-title="nombre"
                    :disabled="idrolactivoPregunta === 0" item-value="id" return-object label="Seleccionar Un Rol"
                    variant="outlined" required />
                  <v-icon color="#006ca1" class="mr-2">mdi-account-tie</v-icon>
                  <span class="font-weight-bold" style="color:#006ca1;">Respuesta del Bot a la pregunta</span>
                  <v-textarea v-model="respuestaBotNuevaPregunta" class="mt-4" label="Respuesta" variant="outlined"
                    clearable required prepend-inner-icon="mdi-account-tie" :disabled="idrolactivoPregunta === 0" />

                  <v-switch v-if="editandoPreguntaFrecuente" v-model="estadoNuevaPregunta" label="Activar Pregunta"
                    color="primary" prepend-icon="mdi-check-circle-outline" :disabled="idrolactivoPregunta === 0" />
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions class="justify-end" style="padding: 16px;">
              <v-btn v-if="!editandoPreguntaFrecuente" class="btn-grow-card" color="primary" variant="flat" rounded="lg"
                @click="guardarNuevaPreguntaF">
                <v-icon left>mdi-content-save-check-outline</v-icon>
                Guardar
              </v-btn>
              <v-btn v-if="editandoPreguntaFrecuente" class="btn-grow-card" color="primary" variant="flat" rounded="lg"
                @click="editarPreguntaF()" :disabled="idrolactivoPregunta === 0">
                <v-icon left>mdi-content-save-check-outline</v-icon>
                Actualizar
              </v-btn>
              <v-btn class="btn-grow-card" color="grey" variant="flat" rounded="lg"
                @click="limpiarCamposNuevaPregunta()">
                <v-icon left>mdi-close-circle</v-icon>
                Cancelar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!----- Dialogo Añadir Pregunta Frecuente-->

        <v-dialog v-model="dialogCargandoPDF" persistent max-width="400px" style="z-index: 9999;">
          <v-card style="border-radius: 18px; padding: 32px 24px; text-align: center;">
            <v-card-title class="mb-2" style="color: #006ca1; font-weight: bold;">
              <v-icon class="mr-2" color="#006ca1">mdi-file-pdf-box</v-icon>
              Procesando PDF...
            </v-card-title>
            <v-card-text>
              <v-progress-circular indeterminate color="primary" size="64" width="7" class="mb-4"
                style="animation: spin 1.2s linear infinite;" />
              <div style="color: #222; font-size: 1rem; min-height: 32px;">
                {{ mensajeCargandoPDF }}
              </div>
            </v-card-text>
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
    adminUsu: null,
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
    dialogRolesIA: false,
    dialogIntencionIA: false,



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
    menuActivo: '',
    selectRolIA: [],
    selectIntencionIA: [],
    dialogRolCompleto: false,
    dialogIntencionCompleto: false,
    rolSeleccionado: {},
    intencionSeleccionado: {},
    dialogCrearRolIA: false,
    dialogCrearIntencionIA: false,
    nuevoRolNombre: '',
    nuevoRolContenido: '',
    nuevoRolActivo: true,
    expandirEditor: false,
    headersRolesIA: [
      { title: 'Id', key: 'id' },
      { title: 'Activo', key: 'activo' },
      { title: 'Nombre', key: 'nombre' },
      { title: 'Rol_content', key: 'rol_content' },
      { title: 'Usuario', key: 'usuario' },
      { title: 'Opciones', key: 'opciones', sortable: false }
    ],
    headersIntencionIA: [
      { title: 'Id', key: 'id', width: '10px' },
      { title: 'Activo', key: 'activo', width: '4px' },
      { title: 'fecha', key: 'fecha', width: '150px' },
      { title: 'Nombre', key: 'intencion', width: '140px' },
      { title: 'Rol', key: 'idconte', width: '50px' },
      { title: 'Direccion URL PDF', key: 'url', width: '70px' },
      { title: 'Contenido PDF', key: 'contenidopdf', width: '400px'},
      { title: 'Opciones', key: 'opciones', sortable: false, width: '10px' }
    ],
    editandoRolIA: false,
    editandoIntencionIA: false,
    alerta: false,
    mensajeAlertLogin: null,
    idRolEditando: null,

    intencionRol: null,
    intencionNombre: '',
    pdfIntencion: null,
    intencionContenido: '',
    intencionActivo: true,
    idIntencionEditando: null,
    intencionEditando: null,

    dialogAsistenteRolIA: false,

    dialogCargandoPDF: false,
    mensajeCargandoPDF: 'Por favor espera mientras se extrae el contenido del PDF.',
    mensajesCargandoAlternativos: [
      'Esto puede tardar unos segundos, ¡gracias por tu paciencia!',
      'Estamos leyendo y analizando el PDF...',
      'Si el PDF tiene imágenes, el proceso puede ser más lento.',
      'No cierres la ventana, estamos trabajando en tu archivo.',
      '¡Casi listo! Procesando el contenido...'
    ],
    intervaloCargandoPDF: null,
  
    dialogAsistenteRolIA: false,
    asistentePaso: 1,
    asistenteLabels: [
      'Área',
      'Empresa',
      'Dirección',
      'Portafolio',
      'Web y Contacto',
      'Idiomas y Tonos',
      'Objetivos Conversación',
      'Reglas Coberturas',
      'Preview'
    ],
    nuevaReglaEspecial: { accion: '', respuesta: '' },
    nuevoServicio: { nombre: '', descripcion: '', horario: '', telefono: '', direccion: '', extras: '' },
    editandoPromptFinal: false,
    asistente: {
      objetivoBot: '',
      objetivosBot: [],
      empresaBot: '',
      publicoBot: '',
      serviciosBot: [],
      tonoBot: '',
      tonoBotOtro: '',
      canalBot: '',
      reglasBot: '',
      reglasCoberturaBot: [],
      limitesBot: '',
      promptFinal: ''
    },
    searchRolIA: '',
    searchIntencionIA: '',
    headersPreguntasF: [
      { title: 'Pregunta', key: 'pregunta' },
      { title: 'Rol', key: 'idrol', width: '240px' },
      { title: 'Respuesta', key: 'respuesta' },
      { title: 'Usuario', key: 'usuario' },
      { title: 'Estado', key: 'estado' },
      { title: 'Última Modificación', key: 'fecha' },
      { title: 'Opciones', key: 'opciones' }
    ],
    dialogPreguntasF: false,
    dialogPreguntaNueva: false,
    preguntasF: [],
    selectEstadoPreguntasFrecuentes: [
      { id: '1', nombre: 'Activo' },
      { id: '0', nombre: 'Inactivo' }
    ],
    editandoPreguntaFrecuente: false,

    nuevaPregunta: null,
    rolNuevaPregunta: null,
    respuestaBotNuevaPregunta: null,
    estadoNuevaPregunta: true,
    idrolactivoPregunta: null,
    idPreguntaEditando: null,
    rolInactivo: false,
    filtroPreguntasF: '',
    
  }),

  mounted() {
    this.baseURL = import.meta.env.VITE_API_BASE_URL; // URL base de la API
    this.imagenComercial = this.baseURL + "images/" + this.comercialId + ".jpeg";
    this.idUsuario = localStorage.getItem("idUsuario");
    this.idCargo = localStorage.getItem("idCargo");
    this.llamadoComerciales();
    this.setMenuActivoPorRuta();
    this.obtenerRolesIA();
    this.cargarPreguntasFrecuentes();
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

    pdfIntencion(newVal) {
      if (!newVal) {
        this.intencionContenido = '';
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
          idusu: 0,
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

    obtenerRolesIA() {
        axios.post(this.baseURL + 'api/cargarRolesIA', {
            'idrol': 0,
        })
            .then(response => {
            this.selectRolIA = response.data.data;
            console.log("ROLES IA: ", this.selectRolIA)
            })
            .catch(error => {
            console.log(error);
            });
        },

    obtenerIntencionIA() {
        axios.post(this.baseURL + 'api/cargarIntencionIA', {
            'idintencion': 0,
        })
            .then(response => {
            this.selectIntencionIA = response.data.data;
            console.log("selectIntencionIA : ", this.selectIntencionIA)
            })
            .catch(error => {
            console.log(error);
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
        })
        .catch((error) => {
          console.error("Error al cargar prospecto:", error);
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
          this.adminUsu = response.data.data[0].u_sta == 1 ? true : false;
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
          admin: this.adminUsu ? 1 : 0,
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
            this.filtroNombreUsuarios = null;
            this.obtenerUsuarios();
            this.limpiarCamposUsuario();
            this.obtenerPerfilesUsu();
            this.abrirDialogUsuarios()
          }, 1100);
        })
        .catch((error) => {
          this.mensajeAlertLogin = "Error Guardando Usuario, Porfavor revisa las credenciales";
          this.alerta = true;
          this.ifCargando = false;
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
          comercial: this.comercialSeleccionado,
          id: this.idProspectoSeleccionado,
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
          admin: this.adminUsu ? 1 : 0,
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
          this.mensajeAlertLogin = "Error Guardando Usuario, Porfavor revisa las credenciales";
          this.alerta = true;
          this.ifCargando = false;
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
          comercial: this.comercialSeleccionado,
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
      this.adminUsu = false;
      this.perfilUsu = null;

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

    abrirDialogProspectos() {
      this.dialogProspectos = true;
      this.limpiarCamposProspecto();
      this.obtenerEmpresas();
      this.llamadoCategorias();
      this.llamadoTipoIdentificacion();
      this.llamadoTipoEmpresa();
      this.llamadoSectores();
      this.llamadoDepartamentos();
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

    abrirRolesIA() {
      this.dialogRolesIA = true;
      this.obtenerRolesIA();
    },

    abrirIntencionIA() {
      this.dialogIntencionIA = true;
      this.obtenerIntencionIA();
      this.obtenerRolesIA();
    },

    abrirPreguntasFrecuentesIA() {
      this.dialogPreguntasF = true;
      this.obtenerRolesIA();
      this.cargarPreguntasFrecuentes();
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
          idusu: 0,
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

    setMenuActivoPorRuta() {
            const path = (this.$route.path || '').toLowerCase();
            if (path.includes('/vercampanas')) this.menuActivo = '/vercampanas';
            else if (path.includes('/campana')) this.menuActivo = '/campana';
            else if (path.includes('/contactos')) this.menuActivo = '/contactos';
            else if (path.includes('/prospeccion-telefonica')) this.menuActivo = '/prospeccion-telefonica';
            else if (path.includes('/seguimiento-llamadas')) this.menuActivo = '/seguimiento-llamadas';
            else if (path.includes('/informes-campanas')) this.menuActivo = '/informes-campanas';
            else if (path.includes('/comercial')) this.menuActivo = '/comercial';
            else if (path.includes('/pendiente-general')) this.menuActivo = '/pendiente-general';
            else if (path.includes('/pedidos')) this.menuActivo = '/pedidos'
            else if(path.includes('/pqr')) this.menuActivo = '/pqr'
            else if (path.includes('/configuracion')) this.menuActivo = '/configuracion'

            // ...agrega más si tienes otras rutas...
            else this.menuActivo = '';
        },

    verRolCompleto(item) {
      this.rolSeleccionado = item;
      this.dialogRolCompleto = true;
    },

    verIntencionCompleto(item) {
      this.intencionSeleccionado = item;
      this.dialogIntencionCompleto = true;
    },

      abrirCrearRolIA() {
      this.dialogCrearRolIA = true;
      this.nuevoRolNombre = '';
      this.nuevoRolContenido = '';
      this.nuevoRolActivo = true;
    },

    abrirCrearIntencionIA() {
      this.dialogCrearIntencionIA = true;
      this.nuevoRolNombre = '';
      this.nuevoRolContenido = '';
      this.nuevoRolActivo = true;
    },

    guardarNuevoRolIA() {
      if (!this.nuevoRolNombre || !this.nuevoRolContenido) {
        this.alerta = true;
        this.mensajeAlertLogin = 'Por favor, complete todos los campos.';
        return;
      }
      axios.post(this.baseURL + 'api/switchRolIA', {
        id : 0,
      })
      
      this.ifCargando = true;
      axios.post(this.baseURL + 'api/crearRol', {
        nombre: this.nuevoRolNombre,
        contenido: this.nuevoRolContenido,
        activo: 1,
        idusu: this.comercialId
      })
      .then(response => {
        if (response.data.status === 'success') {
          this.dialogCrearRolIA = false;
          this.obtenerRolesIA();
          this.$nextTick(() => {
            this.mensajeAlertLogin = 'Rol IA creado correctamente.';
            this.alerta = true;
            this.ifCargando = false;
          });
        } else {
          this.alerta = true;
          this.mensajeAlertLogin = response.data.message || 'No se pudo crear el rol.';
          this.ifCargando = false;
        }
      })
      .catch(error => {
        this.alerta = true;
        this.mensajeAlertLogin  = 'Error al crear el rol.';
        this.ifCargando = false;
        console.error(error);
      });
    },

    editarNuevoRolIA() {
      if (!this.nuevoRolNombre || !this.nuevoRolContenido) {
        this.alerta = true;
        this.mensajeAlertLogin = 'Por favor, complete todos los campos.';
        return;
      }
      this.ifCargando = true;
      if (this.nuevoRolActivo) {
        axios.post(this.baseURL + 'api/switchRolIA', {
          idrol: this.idRolEditando 
        });
      }
      axios.post(this.baseURL + 'api/editarRolIA', {
        idrol: this.idRolEditando,
        nombre: this.nuevoRolNombre,
        contenido: this.nuevoRolContenido,
        activo: this.nuevoRolActivo ? 1 : 0,
      })
      .then(response => {
        if (response.data.status === 'success') {
          this.dialogCrearRolIA = false;
          this.obtenerRolesIA();
          this.$nextTick(() => {
            this.mensajeAlertLogin = 'Rol IA editado correctamente.';
            this.alerta = true;
            this.ifCargando = false;
          });
        } else {
          this.alerta = true;
          this.mensajeAlertLogin = response.data.message || 'No se pudo editar el rol.';
          this.ifCargando = false;
        }
      })
      .catch(error => {
        this.alerta = true;
        this.mensajeAlertLogin  = 'Error al editar el rol.';
        this.ifCargando = false;
        console.error(error);
      });
    },

    editarRolIA(item) {
      this.editandoRolIA = true;
      this.nuevoRolNombre = item.nombre;
      this.nuevoRolContenido = item.rol_content;
      this.nuevoRolActivo = item.activo === 'Activo' ? true : false;
      this.idRolEditando = item.id; // Guarda el id para la edición
      this.dialogCrearRolIA = true;
    },

    cerrardialogCrearRolIA() {
      this.dialogCrearRolIA = false;
      this.nuevoRolNombre = '';
      this.nuevoRolContenido = '';
      this.nuevoRolActivo = true;
      this.idRolEditando = null;
      this.editandoRolIA = false;
    },

    cerrardialogAsistenteRolIA() {
      this.dialogAsistenteRolIA = false;

    },

    cerrardialogCrearIntencionIA() {
      this.dialogCrearIntencionIA = false;
      this.intencionRol = null;
      this.intencionNombre = '';
      this.pdfIntencion = null;
      this.intencionContenido = '';
      this.intencionActivo = true;
      this.editandoIntencionIA = false;
    },

    pegarDesdeWord() {
      navigator.clipboard.readText().then(text => {
        this.nuevoRolContenido += (this.nuevoRolContenido ? '\n' : '') + text;
      });
    },

    cerrardialogCrearIntencionIA() {
      this.dialogCrearIntencionIA = false;
      this.intencionRol = null;
      this.intencionNombre = '';
      this.pdfIntencion = null;
      this.intencionContenido = '';
      this.intencionActivo = true;
      this.editandoIntencionIA = false;
    },


    editarIntencionIA(item) {
      this.editandoIntencionIA = true;
      this.intencionEditando = item;  
      this.intencionRol = item.idconte;
      this.intencionNombre = item.intencion;
      this.intencionContenido = item.contenidopdf || ''; // Asigna el texto si existe
      this.intencionActivo = item.activo === 'Activo' ? true : false;
      this.idIntencionEditando = item.id;
      this.pdfIntencion = null; // No asignar la URL aquí
      this.dialogCrearIntencionIA = true;

      // Si no hay contenido pero hay PDF, extrae el texto
      if (!item.contenidopdf && item.url) {
        this.extraerTextoDesdeUrlPDF(item.url);
      }
    },

    async editarNuevaIntencionIA() {
      this.ifCargando = true;
      this.alerta = false;

      if (!this.intencionRol || !this.intencionNombre || !this.intencionContenido) {
        this.mensajeAlertLogin = 'Por favor, complete todos los campos.';
        this.alerta = true;
        this.ifCargando = false;
        return;
      }

      try {
        // 1. Actualizar datos principales de la intención (envía url vacía si no hay PDF)
        const response = await axios.post(this.baseURL + 'api/editarIntencion', {
          idIntencion: this.idIntencionEditando,
          idrol: this.intencionRol,
          intencion: this.intencionNombre,
          url: this.intencionEditando?.url || '',
          contenido: this.intencionContenido,
          activo: this.intencionActivo ? 1 : 0,
        });

        if (response.data.status === 'success') {
          // 2. Si hay un nuevo PDF, subirlo como blob
          if (this.pdfIntencion) {
            let archivoPDF = Array.isArray(this.pdfIntencion) ? this.pdfIntencion[0] : this.pdfIntencion;
            if (
              archivoPDF.type !== 'application/pdf' &&
              !(archivoPDF.name && archivoPDF.name.toLowerCase().endsWith('.pdf'))
            ) {
              this.mensajeAlertLogin = 'Solo se permite adjuntar archivos PDF.';
              this.alerta = true;
              this.ifCargando = false;
              return;
            }
            const formData = new FormData();
            formData.append('file_intencion', archivoPDF);
            formData.append('id', this.idIntencionEditando);

            await axios.post(this.baseURL + 'api/uploadIntencionesIA', formData, {
              headers: { 'Content-Type': 'multipart/form-data' }
            });
          }

          this.dialogCrearIntencionIA = false;
          setTimeout(() => {
            this.obtenerIntencionIA();
          }, 800);

          this.mensajeAlertLogin = 'Intención IA editada correctamente.';
          this.alerta = true;
        } else {
          this.alerta = true;
          this.mensajeAlertLogin = response.data.message || 'No se pudo editar la intención.';
        }
      } catch (error) {
        this.alerta = true;
        this.mensajeAlertLogin = 'Error al editar la intención.';
        console.error(error);
      } finally {
        this.ifCargando = false;
      }
    },

    async guardarNuevaIntencionIA() {
      this.ifCargando = true;
      this.alerta = false;

      // Validaciones
      if (!this.intencionRol || !this.intencionNombre || !this.intencionContenido) {
        this.mensajeAlertLogin = 'Por favor, complete todos los campos.';
        this.alerta = true;
        this.ifCargando = false;
        return;
      }

      try {
        // 1. Crear la intención IA (envía url vacía si no hay PDF)
        const response = await axios.post(this.baseURL + 'api/crearIntencionIA', {
          idrol: this.intencionRol,
          intencion: this.intencionNombre,
          contenidopdf: this.intencionContenido,
          usu: this.comercialId,
          url: ''
        });

        if (response.data.status === 'success') {
          const idIntencion = response?.data?.data?.[0]?.id || response?.data?.data?.[0]?.id;
          // 2. Si hay PDF, subirlo como blob
          if (this.pdfIntencion && idIntencion) {
            let archivoPDF = Array.isArray(this.pdfIntencion) ? this.pdfIntencion[0] : this.pdfIntencion;
            if (
              archivoPDF.type !== 'application/pdf' &&
              !(archivoPDF.name && archivoPDF.name.toLowerCase().endsWith('.pdf'))
            ) {
              this.mensajeAlertLogin = 'Solo se permite adjuntar archivos PDF.';
              this.alerta = true;
              this.ifCargando = false;
              return;
            }
            const formData = new FormData();
            formData.append('file_intencion', archivoPDF);
            formData.append('id', idIntencion);
            await axios.post(this.baseURL + 'api/uploadIntencionesIA', formData, {
              headers: { 'Content-Type': 'multipart/form-data' }
            });
          }
          this.dialogCrearIntencionIA = false;
          this.obtenerIntencionIA();
          this.mensajeAlertLogin = 'Intención IA creada correctamente.';
          this.alerta = true;
        } else {
          this.mensajeAlertLogin = response.data.message || 'No se pudo crear la intención.';
          this.alerta = true;
        }
      } catch (error) {
        this.mensajeAlertLogin = 'Error al crear la intención.';
        this.alerta = true;
        console.error(error);
      } finally {
        this.ifCargando = false;
      }
    },

    async leerPDFIntencion() {
      this.dialogCargandoPDF = true;
      this.mensajeCargandoPDF = this.mensajesCargandoAlternativos[0];
      let mensajeIndex = 0;
      this.intervaloCargandoPDF = setInterval(() => {
        mensajeIndex = (mensajeIndex + 1) % this.mensajesCargandoAlternativos.length;
        this.mensajeCargandoPDF = this.mensajesCargandoAlternativos[mensajeIndex];
      }, 3500);

      try {
        const formData = new FormData();
        formData.append('file', this.pdfIntencion);

        const response = await axios.post(this.baseURL + '/api/extraerTextoPdf', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });

        if (response.data.status === 'success') {
          this.intencionContenido = response.data.texto || '';
        } else {
          this.mensajeAlertLogin = 'No se pudo extraer el texto del PDF.';
          this.alerta = true;
        }
      } catch (error) {
        this.mensajeAlertLogin = 'Error al crear la intención.';
        this.alerta = true;
        console.error(error);
      } finally {
        clearInterval(this.intervaloCargandoPDF);
        this.dialogCargandoPDF = false;
        this.mensajeCargandoPDF = this.mensajesCargandoAlternativos[0];
      }
    },

  limpiarSaltosLinea(texto) {
    if (!texto) return '';
    // Reemplaza múltiples saltos de línea por un espacio
    return texto.replace(/[\r\n]+/g, ' ').replace(/\s{2,}/g, ' ').trim();
  },

  formatFecha2(fecha) {
    const date = new Date(fecha);
    const dia = date.getDate();
    const meses = [
      'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
      'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
    ];
    const mes = meses[date.getMonth()];
    const anio = date.getFullYear();
    let horas = date.getHours();
    const minutos = String(date.getMinutes()).padStart(2, '0');
    const ampm = horas >= 12 ? 'p. m.' : 'a. m.';
    horas = horas % 12;
    horas = horas ? horas : 12;
    return `${dia} de ${mes} de ${anio}, ${horas}:${minutos} ${ampm}`;
  },

    resetAsistenteRolIA() {
    this.asistentePaso = 1;
    this.agregandoServicio = false;
    this.nuevoServicio = { nombre: '', descripcion: '', horario: '', telefono: '', direccion: '', extras: '' };
    this.nuevaReglaEspecial = { accion: '', respuesta: '' };
    this.asistente = {
      objetivoBot: '[AREA EMPRESA]',
      empresaBot: '',
      publicoBot: '',
      serviciosBot: [],
      tonoBot: '',
      tonoBotOtro: '',
      canalBot: '',
      reglasBot: '',
      especialesBot: [],
      limitesBot: '',
      promptFinal: ''
    };
  },
  agregarServicio() {
    if (!this.nuevoServicio.nombre) return;
    this.asistente.serviciosBot.push({ ...this.nuevoServicio });
    this.nuevoServicio = { nombre: '', descripcion: '', horario: '', telefono: '', direccion: '', extras: '' };
  },

  agregarServicioVacio() {
    this.asistente.serviciosBot.push({
      nombre: '',
      descripcion: '',
      horario: '',
      telefono: '',
      direccion: '',
      extras: ''
    });
  },

  eliminarServicio(i) {
    this.asistente.serviciosBot.splice(i, 1);
  },

  agregarObjetivoVacio() {
  if (!this.asistente.objetivosBot) this.asistente.objetivosBot = [];
  this.asistente.objetivosBot.push({ titulo: '', descripcion: '' });
  },
  eliminarObjetivo(i) {
    this.asistente.objetivosBot.splice(i, 1);
  },
  agregarReglaCoberturaVacia() {
    if (!this.asistente.reglasCoberturaBot) this.asistente.reglasCoberturaBot = [];
    this.asistente.reglasCoberturaBot.push({ titulo: '', descripcion: '' });
  },
  eliminarReglaCobertura(i) {
    this.asistente.reglasCoberturaBot.splice(i, 1);
  },

  guardarPromptEnRolContenido() {
    this.nuevoRolContenido = this.asistente.promptFinal;
    this.dialogAsistenteRolIA = false;
  },

  generarPromptFinal() {
    const a = this.asistente;
    // Portafolio: lista de serviciosBot (título y descripción)
    const portafolio = (a.serviciosBot || [])
      .filter(s => s.nombre)
      .map((s, i) => `${i + 1}. ${s.nombre}${s.descripcion ? ': ' + s.descripcion : ''}`)
      .join('\n');

    // Objetivos: lista de objetivosBot (título y descripción)
    const objetivos = (a.objetivosBot || [])
      .filter(o => o.titulo)
      .map((o, i) => `${i + 6}) ${o.titulo}${o.descripcion ? ': ' + o.descripcion : ''}`)
      .join('\n');

    // Reglas de cobertura: lista de reglasCoberturaBot (título y descripción)
    const reglas = (a.reglasCoberturaBot || [])
      .filter(r => r.titulo)
      .map((r, i) => `${i + 5}) ${r.titulo}${r.descripcion ? ': ' + r.descripcion : ''}`)
      .join('\n');

    return (
      `Eres el Asistente Virtual de ${a.area ? a.area + ' ' : ''}${a.nombreEmpresa ? a.nombreEmpresa : ''}.\n` +
      `Ubicación: ${a.direccionPublico ? a.direccionPublico : ''}\n` +
      `Portafolio:\n${portafolio}\n` +
      `Web: ${a.web ? a.web : ''} – Contacto: ${a.contacto ? a.contacto : ''}\n` +
      `Hablas en ${a.idiomas ? a.idiomas : ''}, con tono ${a.tonos ? a.tonos : ''}. Enfoque B2B.\n\n` +
      `OBJETIVO DE CONVERSACIÓN\n` +
      `1) Primero informa con claridad sobre lo que el cliente pregunte (empresa, producto/servicio).\n` +
      `2) Ten siempre en cuenta de que producto nos está hablando el cliente, esto es muy importante para que puedas darle una clasificación a ese grado de interés.\n` +
      `3)	Solo cuando detectes interés real y hayas detectado de que producto está hablando el cliente, pide datos mínimos y cierra con calificación interna y producto.\n` +
      `4) Si el cliente pide precio/cotización/detalle técnico para contratar, debes activar sí o sí el disparador de calificación.\n` +
      `5)	estés evaluando constantemente el grado de interés del cliente por un producto o servicio en particular\n` +
      `${objetivos}\n\n` +
      `REGLAS DE COBERTURA INICIALES\n` +
      `1) Si preguntan “¿quiénes son?” ? presenta brevemente ${a.nombreEmpresa ? a.nombreEmpresa : ''} (sin calificación).\n` +
      `2) Si es producto/servicio del portafolio? explica beneficios/uso B2B.\n` +
      `3) Si no está en el portafolio/web ? “Ese producto/servicio no hace parte de nuestro portafolio, pero lo comunicaré con uno de nuestros Analistas de Mercadeo para revisar tu solicitud.”\n` +
      `4) Si está fuera de tecnología? “Actualmente en ${a.nombreEmpresa ? a.nombreEmpresa : ''} solo ofrecemos soluciones de tecnología y productividad empresarial.”\n` +
      `${reglas}`
    );
  },

    cargarPreguntasFrecuentes() {
      axios.post(this.baseURL + 'api/cargarPreguntasFrecuentes', {
        'idpregunta': 0,
      })
        .then(response => {
          this.preguntasF = response.data.data;
          console.log("PREGUNTAS FRECUENTES: ", this.preguntasF)
        })
        .catch(error => {
          console.log(error);
        });
    },

    getEstadoNombre(id) {
      const estado = this.selectEstadoPreguntasFrecuentes.find(e => e.id === id || e.id == id);
      return estado ? estado.nombre : id;
    },

    getCategoríaNombre(id) {
      const estado = this.selectRolIA.find(e => e.id === id || e.id == id);
      return estado ? estado.nombre : id;
    },

    formatFechaCorta(fecha) {
      if (!fecha) return '—';
      // Intenta parsear la fecha
      const d = new Date(fecha);
      if (isNaN(d)) return fecha.split('GMT')[0].trim(); // fallback: quita GMT si no es válida
      // Ejemplo: 08 ago 2025, 11:15
      return d.toLocaleString('es-CO', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      }).replace(/\.|,/g, '').replace(' a. m.', ' AM').replace(' p. m.', ' PM');
    },

    guardarNuevaPreguntaF() {
            if (!this.nuevaPregunta || !this.rolNuevaPregunta || !this.respuestaBotNuevaPregunta || !this.rolNuevaPregunta) {
              this.alerta = true;
              this.mensajeAlertLogin = response.data.message || 'No se pudo crear el rol.';
              this.ifCargando = false;
                return;
            }

            console.log('Nueva pregunta guardada:', {
                pregunta: this.nuevaPregunta,
                rol: this.rolNuevaPregunta,
                respuesta: this.respuestaBotNuevaPregunta,
                estado: this.estadoNuevaPregunta
            });

            this.ifCargando = true;
            this.alerta = true;
            this.mensajeAlertLogin = 'Guardando pregunta...';

            let data = { 
                pregunta: this.nuevaPregunta,
                respuesta: this.respuestaBotNuevaPregunta,
                usuario: this.comercialId,
                estado: 1,
                idconte: this.rolNuevaPregunta.id
            };


            axios.post(this.baseURL + 'api/CrearPreguntaFrecuente', data)
            .then(response => {
                if (response.data.status === 'warning') {
                    this.mensajeAlertLogin = response.data.message || 'Ya existe una pregunta con ese nombre.';
                    this.ifCargando = false;
                    this.alerta = true;
                } else {
                    this.mensajeAlertLogin = 'Pregunta actualizada correctamente.';
                    this.dialogPreguntaNueva = false;
                    this.limpiarCamposNuevaPregunta();
                    this.cargarPreguntasFrecuentes();
                    this.editandoPreguntaFrecuente = false;
                    setTimeout(() => {
                        this.alerta = false;
                        this.ifCargando = false;
                    }, 1200);
                }
            })
            .catch(error => {
                this.mensajeAlertLogin = 'Error al guardar la pregunta.';
                this.ifCargando = false;
                this.alerta = true;
                console.error('Error al guardar pregunta frecuente:', error);
            });

            console.log('Preguntas actuales:', this.preguntasF);
        },

        limpiarCamposNuevaPregunta() {
            this.dialogPreguntaNueva = false;
            this.nuevaPregunta = '';
            this.rolNuevaPregunta = null;
            this.respuestaBotNuevaPregunta = '';
            this.estadoNuevaPregunta = true;
            this.editandoPreguntaFrecuente = false;
            this.idPreguntaEditando = null;
            this.idrolActivoPregunta = null;
            this.rolInactivo = false;
        },

        editarItemPregunta(item) {
            // Guarda el id de la pregunta seleccionada
            this.idPreguntaEditando = item.idPregunta || item.id || item.idpregunta;
            this.idrolactivoPregunta = item.rolactivo;
            console.log("ID de la pregunta a editar:", this.idPreguntaEditando);
            console.log("Rol activo de la pregunta a editar:", this.idrolactivoPregunta);

            // Llena los campos del formulario con los datos de la pregunta seleccionada
            this.nuevaPregunta = item.pregunta;
            this.rolNuevaPregunta = this.selectRolIA.find(c => c.id == item.idrol);
            this.respuestaBotNuevaPregunta = item.respuesta;
            this.estadoNuevaPregunta = item.estado == 1 || item.estado == '1';

            // Activa modo edición
            this.editandoPreguntaFrecuente = true;
            this.dialogPreguntaNueva = true;
            if( this.idrolactivoPregunta == 0 ){
                this.rolInactivo = true;
            }
        },

        editarPreguntaF() {
            if (!this.nuevaPregunta || !this.rolNuevaPregunta || !this.respuestaBotNuevaPregunta) {
                this.alerta = true;
                this.mensajeAlertLogin = 'Por favor, complete todos los campos.';
                return;
            }

            this.ifCargando = true;
            this.alerta = true;
            this.mensajeAlertLogin = 'Actualizando pregunta...';

            const data = {
                idPregunta: this.idPreguntaEditando, // Debes tener este id guardado al seleccionar la pregunta a editar
                pregunta: this.nuevaPregunta,
                respuesta: this.respuestaBotNuevaPregunta,
                estado: this.estadoNuevaPregunta ? 1 : 0,
                idconte: this.rolNuevaPregunta.id
            };

            axios.post(this.baseURL + 'api/editarPreguntaFrecuente', data)
                .then(response => {
                    if (response.data.status === 'warning') {
                        this.mensajeAlertLogin = response.data.message || 'Ya existe una pregunta con ese nombre.';
                        this.ifCargando = false;
                        this.alerta = true;
                    } else {
                        this.mensajeAlertLogin = 'Pregunta actualizada correctamente.';
                        this.dialogPreguntaNueva = false;
                        this.limpiarCamposNuevaPregunta();
                        this.cargarPreguntasFrecuentes();
                        this.editandoPreguntaFrecuente = false;
                        setTimeout(() => {
                            this.alerta = false;
                            this.ifCargando = false;
                        }, 1200);
                    }
                })
                .catch(error => {
                    this.mensajeAlertLogin = 'Error al actualizar la pregunta.';
                    this.ifCargando = false;
                    this.alerta = true;
                    console.error('Error al editar pregunta frecuente:', error);
                });
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

.empresa-card {
  border-radius: 16px;
  background: linear-gradient(135deg, #f5f7fa 80%, #e3f2fd 100%);
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

/* Estilo para el header de la v-data-table */
.v-data-table thead th {
  background-color: #006CA1 !important;
  color: white !important;
  font-weight: bold;
}

.v-data-table td[data-test="td-total"],
.v-data-table td[data-test="td-total"] .th-content,
.v-data-table td:last-child .th-content {
  color: #ffffff !important;
  font-weight: 700 !important;
  font-size: 0.98rem !important;
  letter-spacing: 0.1px !important;
}

.data-table-campanas {
  font-size: 0.97rem;
  background: #f8fafc;
  border-radius: 18px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
}

.fancy-headers :deep(.v-table__wrapper > table > thead > tr > th) {
  background-color: #006ba1 !important;
  color: #ffffff !important;
  font-weight: 700;
  /* bold */
  font-size: 0.85rem;
  /* un poco más grande */
  text-align: center;
  letter-spacing: .2px;
  border-bottom: 2px solid rgba(255, 255, 255, .15);
}

.fancy-rows-campanas td {
  transition: background 0.2s;
}

.custom-scroll::-webkit-scrollbar {
  width: 8px;
}

.custom-scroll::-webkit-scrollbar-track {
  background: transparent;
}

.custom-scroll::-webkit-scrollbar-thumb {
  background-color: #999;
  border-radius: 4px;
}

.word-preview-container {
  background: #f3f6fa;
  border-radius: 14px;
  box-shadow: 0 2px 12px rgba(25, 118, 210, 0.08);
  padding: 18px 16px 12px 16px;
  min-height: 260px;
  max-height: 480px;
  overflow-y: auto;
  transition: max-height 0.2s;
}
.word-preview-toolbar {
  border-bottom: 1px solid #e0e6f1;
  padding-bottom: 6px;
}
.word-preview {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 1px 6px rgba(25, 118, 210, 0.06);
  padding: 12px;
  min-height: 220px;
  max-height: 320px;
  overflow-y: auto;
  transition: min-height 0.2s, max-height 0.2s;
}

.v-data-table th,
.v-data-table td {
  vertical-align: top;
  word-break: break-word;
  white-space: normal;
}

.v-data-table td {
  padding-top: 8px;
  padding-bottom: 8px;
}

.asistente-rol-layout {
  display: flex;
  gap: 32px;
  min-height: 480px;
}
.asistente-rol-form {
  flex: 1 1 340px;
  background: #dbf2ff4f;
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(25, 118, 210, 0.06);
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.asistente-rol-preview {
  flex: 2 1 480px;
  background: #f3f6fa;
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(25, 118, 210, 0.06);
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.preview-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 8px;
  color: #006ca1;
}
.asistente-stepper-bar {
  margin-bottom: 18px;
}
.asistente-stepper {
  background: transparent;
}
.asistente-rol-nav {
  margin-top: 18px;
  display: flex;
  gap: 12px;
}
@media (max-width: 900px) {
  .asistente-rol-layout {
    flex-direction: column;
    gap: 18px;
  }
  .asistente-rol-form, .asistente-rol-preview {
    max-width: 100%;
    min-width: 0;
  }
}

.asistente-stepper-bar {
  margin-bottom: 18px;
}
.asistente-stepper .v-stepper-header {
  background: #006ca1 !important;
  color: white;
  border-radius: 12px;
  padding: 8px 0;
  margin-left: 2px;
  margin-right: 2px;
}
.asistente-stepper .v-stepper-step {
  color: #fff !important;
  font-weight: 600;
  font-size: 1rem;
}
.asistente-stepper-step-active {
  background: #069ae3 !important;
  color: #fff !important;
  border-radius: 8px;
  box-shadow: 0 2px 8px #0280bf44;
}
.asistente-stepper .v-stepper-step--complete {
  background: #4caf50 !important;
  color: #fff !important;
  border-radius: 8px;
}

.servicio-card {
  border-radius: 12px;
  background: linear-gradient(135deg, #e3f2fd 80%, #f5f8fa 100%);
  box-shadow: 0 2px 8px rgba(25, 118, 210, 0.08);
  margin-bottom: 8px;
  transition: box-shadow 0.2s, transform 0.2s;
}

.servicio-detalles {
  margin-top: 6px;
  font-size: 0.8rem;
  color: #444;
}
.servicio-detalle {
  margin-bottom: 30px;
  display: flex;
  align-items: center;
}

.servicio-input {
  background: #e3f2fd;
  border: none;
  border-radius: 6px;
  font-size: 0.8rem;
  padding: 2px;
  margin: 2px 0;
  min-height: 30px;
  height: 30px;
  width: 100%;
  box-sizing: border-box;
  outline: none;
  transition: box-shadow 0.2s;
  box-shadow: 0 1px 4px #0280bf11;
}
.servicio-input:focus {
  box-shadow: 0 2px 8px #0280bf33;
  background: #d0e7fa;
}
.servicio-input-nombre {
  font-weight: bold;
  color: #006ca1;
  max-width: 280px;
}
.servicio-input-desc {
  width: 100%;
  min-height: 60px;
  max-height: 240px;
  resize: vertical;
  font-size: 0.8rem;
  margin-bottom: 6px;
  border-radius: 6px;
  background: #e3f2fd;
  border: none;
  padding: 4px 8px;
}
.servicio-detalle input {
  max-width: 300px;
  display: inline-block;
  vertical-align: middle;
}


</style>


