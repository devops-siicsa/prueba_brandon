<template>
  <v-app id="tabla-campanas">
    <AppHeader :imagenComercial="imagenComercial" />
    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
        <v-list v-if="false">

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

          <v-list-item @click="irGaleriaCampanas()" link>

            <v-list-item-content class="list-item-compact">

              <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/vercampanas' }"
                style="color: white; font-size: 0.93rem;">
                <v-icon class="mr-2" size="small" icon="mdi mdi-image-multiple" color="white" prepend-icon></v-icon>
                Galería
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irInformesCampañas()" link>

            <v-list-item-content>

              <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/informes-campanas' }"
                style="color: white; font-size: 0.93rem;">
                <v-icon class="mr-2" size="small" icon="mdi-chart-bar" color="white" prepend-icon></v-icon>
                Métricas
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irProspeccionTelefonica()" link>

            <v-list-item-content>

              <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/prospeccion-telefonica' }"
                style="color: white; white-space: pre-wrap; font-size: 0.93rem;">
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

          <v-list-item @click="irEmpresas()" link v-if="idCargo == '2'">

            <v-list-item-content>

              <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/contactos' }"
                style="color: white;; font-size: 0.93rem; ">
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

          <v-list-item @click="irContactos()" link v-if="idCargo == '2'">

            <v-list-item-content>

              <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/contactos' }"
                style="color: white; font-size: 0.93rem;">
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
        <div id="contenido-exportar">
          <!--SECCIÓN TITULO DE LA PAGINA-->
          <v-card elevation="3" class="pa-5 mb-5" style="
            border-radius: 18px;
            background: linear-gradient(90deg, #f5f7fa 100%, #e3f6ff 100%);
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.07);
          ">
            <v-row class="align-center justify-space-between">
              <v-col>
                <div>
                  <h2 class="mb-1" style="
                    font-weight: 750;
                    font-size: 1.3rem;
                    color: #0a1c3a;
                    letter-spacing: -1px;
                  ">
                    Métricas de campañas
                  </h2>
                  <div style="font-size: 0.9rem; color: #4b5563; font-weight: 500">
                    Panel analítico de SIICSA-BOT — Interacciones por canal y
                    rendimiento por campaña.
                  </div>
                </div>
              </v-col>
            </v-row>
          </v-card>
          <!--SECCIÓN TITULO DE LA PAGINA-->

          <!--SECCIÓN FILTROS-->
          <v-card elevation="3" class="pa-4 mb-4 filtros-campanas-card" dense>
            <h2 class="mb-2" style="
            font-weight: 750;
            font-size: 1.25rem;
            color: #0a1c3a;
            letter-spacing: -1px;
            ">
              Filtrar las Campañas
            </h2>
            <v-row dense class="align-center mb-2 d-flex justify-space-between filtros-row" gap="16px">
              <v-col cols="12" md="2">
                <v-text-field v-model="fechaInicio" label="Fecha inicial" variant="outlined" type="date"
                  density="compact" hide-details class="filtro-input" prepend-inner-icon="mdi-calendar"
                  @update:model-value="aplicarFiltros()" />
              </v-col>
              <v-col cols="12" md="2">
                <v-text-field v-model="fechaFin" label="Fecha final" variant="outlined" type="date" density="compact"
                  hide-details class="filtro-input" prepend-inner-icon="mdi-calendar"
                  @update:model-value="aplicarFiltros()" />
              </v-col>
              <v-col cols="12" md="2">
                <v-autocomplete v-model="sectorSeleccionado" :items="sectoresCampanias" label="Sector"
                  variant="outlined" density="compact" hide-details clearable class="filtro-input"
                  prepend-inner-icon="mdi-domain" @update:model-value="aplicarFiltros()" />
              </v-col>
              <v-col cols="12" md="2">
                <v-autocomplete v-model="ciudadSeleccionada" :items="ciudadesCampanias" label="Ciudad"
                  variant="outlined" density="compact" hide-details clearable class="filtro-input"
                  prepend-inner-icon="mdi-city-variant" @update:model-value="aplicarFiltros()" />
              </v-col>
              <v-col cols="12" md="2">
                <v-autocomplete v-model="campañaSeleccionada" :items="listaCampañas" item-title="nombre_campaña"
                  item-value="id" label="Nombre de campaña" variant="outlined" density="compact" clearable hide-details
                  class="filtro-input" prepend-inner-icon="mdi-view-gallery-outline"
                  @update:model-value="aplicarFiltros()" @click:clear="campañasSeleccionadas = null" />
              </v-col>

            </v-row>
            <v-row class="align-center">
              <v-col cols="12" md="8" class="d-flex align-center">
                <span class="mr-4" style="font-size: 1rem; color: #0a1c3a; font-weight: 600;">Canal</span>
                <div class="d-flex flex-row flex-wrap canal-chips">
                  <v-chip v-for="canal in canales" :key="canal.value"
                    :color="canalSeleccionado === canal.value ? canal.color : '#f3f6fa'"
                    :text-color="canalSeleccionado === canal.value ? 'white' : '#006CA1'" class="canal-chip"
                    @click="canalSeleccionado = canal.value" :disabled="canalesDeshabilitados" variant="elevated"
                    :elevation="canalSeleccionado === canal.value ? 4 : 0"
                    style="margin-right: 8px; margin-bottom: 4px; min-width: 110px; justify-content: flex-start;">
                    <v-icon left :color="canalSeleccionado === canal.value ? 'white' : canal.color" size="18">{{
                      canal.icon
                    }}</v-icon>
                    <span style="font-weight:600;" :class="canalSeleccionado === canal.value ? 'selected-label' : ''">{{
                      canal.label }}</span>
                  </v-chip>
                </div>
              </v-col>
              <v-col cols="12" md="4" class="d-flex align-center justify-end">
                <span class="mb-1 mr-2" style="color: #64748b; font-size: 1.05rem; font-weight: 500">
                  {{ listaCampañas.length }} campañas coinciden con los filtros
                </span>
                <v-btn variant="outlined" color="#006CA1" class="mr-2" @click="restablecerFiltros()"
                  style="font-weight:600; letter-spacing:0.5px;">LIMPIAR</v-btn>
                <v-btn color="#006CA1" class="btn-grow-card" style="font-weight:600; letter-spacing:0.5px;"
                  @click="aplicarFiltros()">APLICAR</v-btn>

              </v-col>
            </v-row>
          </v-card>
          <!--SECCIÓN FILTROS-->

          <!--SECCIÓN AVISOS-->
          <v-row class="mb-2 d-flex justify-center mt-2 mr-5 ml-5" style="gap: 25px;">
            <v-col v-for="(aviso, idx) in avisosPorCanal" :key="idx" cols="auto" class="pa-0"
              style="min-width: 150px; max-width: 250px; flex: 1 1 0; font-size:12px;">
              <v-card elevation="0" class="aviso-metric-calcado btn-grow-car pa-2"
                :style="`background: ${aviso.bgGradient || aviso.color || '#f5f7fa'}; color: ${aviso.textColor || '#0a1c3a'};`">
                <div class="d-flex flex-row align-center w-100 justify-center" style="gap: 0px;">
                  <span class="aviso-metric-value-calcado">{{ aviso.value }}</span>
                  <span class="aviso-metric-label-calcado ml-3">{{ aviso.label }}</span>
                  <span class="aviso-metric-emoji-calcado" v-if="aviso.emoji">{{ aviso.emoji }}</span>
                </div>
              </v-card>
            </v-col>
          </v-row>
          <!--SECCIÓN AVISOS-->

          <!--SECCIÓN DE GRÁFICOS-->

          <!--SECCIÓN DE GRÁFICOS-->

          <v-row style="height: 100%">
            <v-col style="height: 100%">
              <v-card-title class="text-subtitle-1 d-flex align-center justify-space-between"
                style="background-color: #006CA1; color:white; border-radius:8px; height: 50px;">
                <div class="d-flex align-center">
                  <v-icon icon="mdi mdi-chart-areaspline" color="white" prepend-icon></v-icon>
                  <span class="ml-2">Metricas de Interacción</span>
                </div>
                <div class="d-flex ml-4">
                  <v-btn class="btn-grow-card mr-4" size="small" color="#3f94e8" rounded elevation="2"
                    @click="exportarExcel()">
                    <v-icon left size="20">mdi-file-excel</v-icon>
                    Exportar Excel
                  </v-btn>
                  <v-btn class="btn-grow-card" size="small" color="#3f94e8" rounded elevation="2"
                    @click="exportarPDF()">
                    <v-icon class="mr-2" left size="20" color="white">mdi-file-pdf-box</v-icon>
                    <span color="white">Exportar PDF</span>
                  </v-btn>
                </div>
              </v-card-title>

              <v-row>
                <v-col cols="6" class="align-center justify-center">
                  <v-card elevation="3" class="pa-2 mb-2 d-flex flex-column align-center justify-center" style="
                    border-radius: 25px;
                    background: linear-gradient(
                      90deg,
                      #f5f7fa 100%,
                      #e3f6ff 100%
                    );
                    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.07);
                    align-items: center;
                    text-align: center;
                  ">

                    <div class="d-flex align-center justify-center mb-4" style="gap: 18px">
                      <span style="
                        font-size: 1.15rem;
                        font-weight: 700;
                        color: #0a1c3a;
                        margin: 0;
                        white-space: nowrap;
                      ">
                        {{ textoDistribucionDonut }}

                        <div v-if="[1, 3, 4].includes(canalSeleccionado)" class="mb-2" style="max-width: 220px;">
                          <v-select v-model="modoDonut" :items="[
                            { value: 'interacciones', title: 'Interacciones' },
                            { value: 'envios', title: 'Envios' }
                          ]" label="Modo de gráfico" variant="outlined" dense hide-details
                            style="font-size: 0.98rem;" />
                        </div>
                      </span>
                    </div>
                    <div style="
                      width: 100%;
                      max-width: 320px;
                      min-width: 320px;
                      margin: 0 auto;
                    ">
                      <div class="align-center mb-2"></div>
                      <div class="justify-center align-center">
                        <template
                          v-if="datosDonut.datasets && datosDonut.datasets[0] && datosDonut.datasets[0].data && datosDonut.datasets[0].data.reduce((a, b) => a + b, 0) > 0">
                          <canvas ref="myChart2" class="justify-center"
                            style="max-width: 240px; min-width: 240px; max-height: 270px; min-height: 270px;"></canvas>
                          <span class="mb-1" style="
                          color: #64748b;
                          font-size: 1.05rem;
                          font-weight: 500;
                        ">
                            {{ listaCampañas.length }} campañas coinciden con los
                            filtros.
                          </span>
                          <div v-if="leyendaDonut.length" class="donut-legend mt-4 d-flex justify-center"
                            style="gap: 0px">
                            <div v-for="item in leyendaDonut" :key="item.label"
                              class="donut-legend-item d-flex align-center" style="gap: 0px;">
                              <span :style="{
                                display: '',
                                width: '14px',
                                height: '14px',
                                borderRadius: '50%',
                                background: item.color,
                                marginRight: '',
                                border: '2px solid #e0e0e0',
                              }"></span>
                              <span style="
                              font-size: 0.98rem;
                              color: #222;
                              font-weight: 600;
                            ">{{ item.label }}</span>
                            </div>
                          </div>
                        </template>
                        <template v-else>
                          <div class="d-flex justify-center align-center"
                            style="width: 100%; min-height: 340px; min-width: 100%; max-width: 100%;">
                            <div class="text-center py-8" style="color: #888; ">
                              <v-icon size="80" color="grey">mdi-database-remove</v-icon>
                              <div class="mt-2" style="font-size: 1rem;">No hay datos disponibles</div>
                            </div>
                          </div>
                        </template>
                      </div>
                    </div>
                  </v-card>
                </v-col>
                <v-col cols="6" class="align-center justify-center">
                  <v-card elevation="3" class="pa-4 mb-4 d-flex flex-column align-center justify-center" style="
                  border-radius: 25px;
                  background: linear-gradient(90deg, #f5f7fa 100%, #e3f6ff 100%);
                  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.07);
                  align-items: center;
                  text-align: center;
                ">

                    <div class="d-flex align-center justify-center mb-2"
                      style="gap: 18px; width: 100%; justify-content: flex-start;">

                      <span
                        style="font-size: 1.15rem; font-weight: 700; color: #0a1c3a; margin: 0; white-space: nowrap;">
                        {{ textoDistribucionDonut }}
                      </span>
                      <v-autocomplete v-model="campañasSeleccionadas" :items="opcionesCampañas"
                        label="Buscar campaña(s)" multiple clearable dense variant="outlined"
                        style="max-width: 200px; min-width: 180px" hide-details :menu-props="{ maxHeight: '300px' }"
                        chips @change="renderBarChartCanvas" />
                    </div>
                    <div style="width: 100%; min-height: 340px; min-width: 100%; max-width: 100%; position: relative;">
                      <canvas ref="barChartCanvas"
                        style="width: 100% !important; height: 320px !important; min-height: 320px; max-height: 400px; display: block;"></canvas>
                    </div>

                  </v-card>
                </v-col>
              </v-row>
              <v-divider :thickness="3" color="#0A1C3A" class="border-opacity-50 mt-4 mb-4"></v-divider>
              <v-row>

                <v-col cols="12" style="height: 420px">
                  <v-card class="elevation-5 rounded-lg" style="
                    background-color: #f0f4f8;
                    display: flex;
                    flex-direction: column;
                    height: 100%;
                  ">
                    <v-card-title class="text-subtitle-1 d-flex align-center justify-space-between"
                      style="background-color: #006CA1; color:white; border-radius:8px;">
                      <div class="d-flex align-center">
                        <v-icon icon="mdi mdi-chart-areaspline" color="white" class="mr-2" />
                        <span>{{ textoDistribucionDonut }}</span>
                      </div>
                      <div class="d-flex canal-chips ml-4">
                        <v-btn class="btn-grow-card mr-2 mt-1" size="small" color="white" rounded elevation="2"
                          @click="recargarDatos(); limpiarFiltrosTabla();" title="Refrescar datos"
                          :disabled="cargandoTabla">
                          <v-icon left size="20">mdi-reload</v-icon>
                        </v-btn>
                        <!-- Botón filtros avanzados para la tabla (mismo comportamiento que en dialogo de detalles) -->
                        <v-tooltip text="Filtros avanzados" location="top">
                          <template v-slot:activator="{ props }">
                            <v-menu v-model="menuFiltrosAvanzadosTabla" :close-on-content-click="false" offset-y
                              location="start" persistent>
                              <template #activator="{ props: menuProps }">
                                <v-btn color="white" variant="elevated" v-bind="menuProps"
                                  class="ml-2 d-flex align-center rounded-xl"
                                  style="min-width: 180px; font-weight:600;">
                                  <v-icon left>mdi-tune-variant</v-icon>
                                  Filtros avanzados
                                </v-btn>
                              </template>
                              <v-card min-width="520" max-width="600" style="width:520px;">
                                <v-card-title class="text-h6 d-flex align-center"
                                  style="background-color: #006CA1; color: white;">
                                  <v-icon class="mr-2">mdi-tune-variant</v-icon>
                                  Filtros avanzados
                                </v-card-title>
                                <v-divider />
                                <v-card-text>
                                  <!-- Selector dinámico de columnas (headers) -->
                                  <v-select v-model="filtrosTablaActivos" :items="filtrosTablaDisponibles"
                                    item-title="label" item-value="key" label="Selecciona columnas" multiple chips
                                    closable-chips variant="outlined" density="comfortable" hide-details
                                    prepend-inner-icon="mdi-filter" clearable :menu-props="{ maxHeight: '300px' }"
                                    style="width:100%; max-width: 480px;" class="mb-4" autocomplete>
                                    <template #selection="{ item, index }">
                                      <v-chip v-if="index < 2" :key="item.value" size="small" color="#006CA1"
                                        text-color="white" class="mr-1">
                                        {{ item.title || item.label }}
                                      </v-chip>
                                      <span v-else-if="index === 2" class="text-caption ml-1">+{{
                                        filtrosTablaActivos.length - 2 }}</span>
                                    </template>
                                  </v-select>

                                  <!-- Inputs por columna seleccionada -->
                                  <v-row dense>
                                    <!-- Renderizamos inputs solamente para los filtros visibles (excluimos ciudad/sector y variantes) -->
                                    <v-col v-for="(filtro, idx) in filtrosTablaVisibleInputs" :key="filtro" cols="12"
                                      md="6" style="max-width: 260px;">
                                      <component :is="filtrosTablaComponentes[filtro] || 'v-autocomplete'"
                                        v-model="filtrosTablaModelos[filtro]"
                                        :items="filtrosTablaItems[filtro] && filtrosTablaItems[filtro].length ? filtrosTablaItems[filtro] : (filtrosItems()[filtro] || [])"
                                        :label="(filtrosTablaDisponibles.find(f => f.key === filtro)?.label) || filtro"
                                        variant="outlined" density="comfortable" hide-details clearable class="mb-3"
                                        :prepend-inner-icon="filtrosTablaDisponibles.find(f => f.key === filtro)?.icon || 'mdi-filter'"
                                        v-bind="filtrosTablaInputProps(filtro)" />
                                    </v-col>
                                  </v-row>
                                </v-card-text>
                                <v-card-actions>
                                  <v-spacer />
                                  <v-btn color="#006CA1" variant="flat"
                                    @click="menuFiltrosAvanzadosTabla = false">Cerrar</v-btn>
                                  <v-tooltip text="Limpiar Filtros" location="top">
                                    <template v-slot:activator="{ props }">
                                      <v-btn v-bind="props" color="#1d4ed8" icon size="small"
                                        class="ml-1 modern-btn btn-grow-card" @click="limpiarFiltrosTabla()">
                                        <v-icon>mdi mdi-broom</v-icon>
                                      </v-btn>
                                    </template>
                                  </v-tooltip>
                                </v-card-actions>
                              </v-card>
                            </v-menu>
                          </template>
                        </v-tooltip>
                        <v-chip v-for="canal in canales" :key="canal.value"
                          :color="canalSeleccionado === canal.value ? canal.color : '#f3f6fa'"
                          :text-color="canalSeleccionado === canal.value ? 'white' : '#006CA1'" class="canal-chip"
                          @click="canalSeleccionado = canal.value" :disabled="canalesDeshabilitados" variant="elevated"
                          :elevation="canalSeleccionado === canal.value ? 4 : 0"
                          style="margin-right: 8px; margin-bottom: 4px; min-width: 110px; justify-content: flex-start;">
                          <v-icon left :color="canalSeleccionado === canal.value ? 'white' : canal.color" size="18">{{
                            canal.icon }}</v-icon>
                          <span style="font-weight:600;"
                            :class="canalSeleccionado === canal.value ? 'selected-label' : ''">{{
                              canal.label }}</span>
                        </v-chip>
                      </div>
                    </v-card-title>
                    <div class="custom-scroll" style="flex: 1 1 auto; overflow-y: auto">
                      <v-data-table :headers="tablaHeadersVisiblePorCanal" :items="tablaItemsPorCanalFiltrada"
                        :custom-key-sort="customKeySort"
                        class="elevation-2 rounded-xl data-table-campanas fancy-headers fancy-rows-campanas"
                        items-per-page-text="Campañas por página" items-per-page="10"
                        :items-per-page-options="[10, 20, 50, 100]" page-text="Campañas del ({0}) al ({1}) de ({2})"
                        no-data-text="No hay campañas disponibles" fixed-header density="compact" virtual-scroll hover
                        @click:row="(_, row) => verDetallesCampana(row.item.id)"
                        :item-class="(_, i) => i % 2 === 0 ? 'row-even btn-grow-card' : 'row-odd'">
                        <!-- Headers comunes -->
                        <template #header.index="{ column }">
                          <div class="th-content"><span>{{ column.title }}</span></div>
                        </template>
                        <template #header.nombre_campaña="{ column }">
                          <div class="th-content">
                            <v-icon size="16" class="mr-2" color="#006CA1">mdi-calendar-multiple</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.fecha="{ column }">
                          <div class="th-content">
                            <v-icon size="16" class="mr-2" color="#006CA1">mdi-calendar-range</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.canal="{ column }">
                          <div class="th-content">
                            <v-icon size="16" class="mr-2" color="#006CA1">mdi-broadcast</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.ciudad="{ column }">
                          <div class="th-content">
                            <v-icon size="16" class="mr-2" color="#006CA1">mdi-city-variant</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.sector="{ column }">
                          <div class="th-content">
                            <v-icon size="16" class="mr-2" color="#006CA1">mdi-office-building</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>

                        <!-- WhatsApp headers -->
                        <template #header.interes_positivo="{ column }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-thumb-up</v-icon>
                            <div class="th-content">
                              <span class="th-content" color="#006CA1">{{ column.title }}</span>
                            </div>
                          </div>
                        </template>
                        <template #header.interes_negativo="{ column }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-thumb-down</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.enviadas="{ column }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-clock-outline</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.entregadas="{ column }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-check-circle</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.no_existe="{ column }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-cancel</v-icon>
                            <div class="th-content">
                              <span class="th-content">{{ column.title }}</span>
                            </div>
                          </div>
                        </template>
                        <template #header.sin_respuesta="{ column }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-help-circle-outline</v-icon>
                            <span class="th-content">{{ column.title }}</span>
                          </div>
                        </template>

                        <!-- Telefónico headers -->
                        <template #header.efectivo_con_lead="{ column }" v-if="canalSeleccionado === 2">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-account-check</v-icon>
                            <div class="th-content">
                              <span class="th-content">{{ column.title }}</span>
                            </div>
                          </div>
                        </template>
                        <template #header.efectivo_sin_lead="{ column }" v-if="canalSeleccionado === 2">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-account-plus</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.no_efectivo="{ column }" v-if="canalSeleccionado === 2">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-account-cancel</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>

                        <!-- Email headers -->
                        <template #header.entregadas="{ column }" v-if="canalSeleccionado === 3">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-check-circle</v-icon>
                            <span class="th-content">{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.no_entregadas="{ column }" v-if="canalSeleccionado === 3">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-cancel</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.con_respuesta="{ column }" v-if="canalSeleccionado === 3">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-email-check</v-icon>
                            <span class="th-content">{{ column.title }}</span>
                          </div>
                        </template>
                        <template #header.sin_respuesta="{ column }" v-if="canalSeleccionado === 3">
                          <div class="th-content">
                            <v-icon size="16" color="#006CA1" class="mr-1">mdi-help-circle-outline</v-icon>
                            <div class="th-content">
                              <span class="th-content">{{ column.title }}</span>
                            </div>
                          </div>
                        </template>

                        <!-- Items comunes -->
                        <template #item.index="{ index }">
                          <span class="font-weight-bold th-content" style="color: #1565c0;">{{ index + 1 }}</span>
                        </template>
                        <template #item.fecha="{ item }">
                          <span class="font-weight-medium th-content">{{ item.fecha }}</span>
                        </template>
                        <template #item.canal="{ item }">
                          <v-chip color="#0056b8" text-color="white" small>
                            <v-icon left size="18" v-if="item.canal === 2">mdi-phone</v-icon>
                            <v-icon left size="18" v-else-if="item.canal === 1">mdi-whatsapp</v-icon>
                            <v-icon left size="18" v-else-if="item.canal === 3">mdi-email</v-icon>
                            <v-icon left size="18" v-else-if="item.canal === 4">mdi-instagram</v-icon>
                            {{ canalNombre(item.canal) }}
                          </v-chip>
                        </template>
                        <template #item.ciudad="{ item }">
                          <div class="sector-grid">
                            <template v-for="(city, idx) in _splitCiudades(item.ciudad).slice(0, 4)" :key="city">
                              <v-chip class="chip-custom" color="#1565c0" text-color="#0a1c3a" size="small" label>
                                {{ city }}
                              </v-chip>
                            </template>
                            <template v-if="_splitCiudades(item.ciudad).length > 4">
                              <div class="sector-plus-cell">
                                <v-tooltip location="top">
                                  <template #activator="{ props }">
                                    <v-chip class="chip-custom" v-bind="props" color="#1565c0" text-color="#0a1c3a"
                                      size="small" label style="cursor:pointer;">
                                      +{{ _splitCiudades(item.ciudad).length - 4 }}
                                    </v-chip>
                                  </template>
                                  <span>
                                    {{ _splitCiudades(item.ciudad).slice(4).join(", ") }}
                                  </span>
                                </v-tooltip>
                              </div>
                            </template>
                          </div>
                        </template>
                        <template #item.sector="{ item }">
                          <div class="sector-grid">
                            <template
                              v-for="(sector, idx) in (item.sector ? item.sector.split(',').map(s => s.trim()).slice(0, 4) : [])"
                              :key="sector">

                              <v-chip class="chip-custom" color="#1565c0" text-color="#0a1c3a" size="small" label>
                                {{ sector }}
                              </v-chip>

                            </template>
                            <template v-if="item.sector && item.sector.split(',').length > 4">
                              <div class="sector-plus-cell">
                                <v-tooltip location="top">
                                  <template #activator="{ props }">
                                    <v-chip class="chip-custom" v-bind="props" color="#1565c0" text-color="#0a1c3a"
                                      size="small" label style="cursor:pointer;">
                                      +{{ item.sector.split(',').length - 4 }}
                                    </v-chip>
                                  </template>
                                  <span>
                                    {{item.sector.split(',').slice(4).map(s => s.trim()).join(", ")}}
                                  </span>
                                </v-tooltip>
                              </div>
                            </template>
                          </div>
                        </template>

                        <!-- WhatsApp items -->
                        <template #item.interes_positivo="{ item }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <span class="th-content">{{ item.interes_positivo ?? 0 }}</span>
                          </div>
                        </template>
                        <template #item.interes_negativo="{ item }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <span class="th-content">{{ item.interes_negativo ?? 0 }}</span>
                          </div>
                        </template>
                        <template #item.enviadas="{ item }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <span class="th-content">{{ item.enviadas ?? 0 }}</span>
                          </div>
                        </template>
                        <template #item.entregadas="{ item }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <span class="th-content">{{ item.entregadas ?? 0 }}</span>
                          </div>
                        </template>
                        <template #item.no_existe="{ item }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <span class="th-content">{{ item.no_existe ?? 0 }}</span>
                          </div>
                        </template>
                        <template #item.sin_respuesta="{ item }" v-if="canalSeleccionado === 1">
                          <div class="th-content">
                            <span class="th-content">{{ item.sin_respuesta ?? 0 }}</span>
                          </div>
                        </template>

                        <!-- Telefónico items -->
                        <template #item.efectivo_con_lead="{ item }" v-if="canalSeleccionado === 2">
                          <span class="th-content">{{ item.efectivo_con_lead ?? 0 }}</span>
                        </template>
                        <template #item.efectivo_sin_lead="{ item }" v-if="canalSeleccionado === 2">
                          <span class="th-content">{{ item.efectivo_sin_lead ?? 0 }}</span>
                        </template>
                        <template #item.no_efectivo="{ item }" v-if="canalSeleccionado === 2">
                          <span class="th-content">{{ item.no_efectivo ?? 0 }}</span>
                        </template>

                        <!-- Email items -->
                        <template #item.entregadas="{ item }" v-if="canalSeleccionado === 3">
                          <span class="th-content">{{ item.entregadas ?? 0 }}</span>
                        </template>
                        <template #item.no_entregadas="{ item }" v-if="canalSeleccionado === 3">
                          <span class="th-content">{{ item.no_entregadas ?? 0 }}</span>
                        </template>
                        <template #item.con_respuesta="{ item }" v-if="canalSeleccionado === 3">
                          <span class="th-content">{{ item.con_respuesta ?? 0 }}</span>
                        </template>
                        <template #item.sin_respuesta="{ item }" v-if="canalSeleccionado === 3">
                          <span class="th-content">{{ item.sin_respuesta ?? 0 }}</span>
                        </template>

                        <!-- Total (común a todos) -->

                        <template #header.total="{ column }">
                          <div class="th-content">
                            <v-icon size="16" class="mr-2" color="#006CA1">mdi-counter</v-icon>
                            <span>{{ column.title }}</span>
                          </div>
                        </template>

                        <!-- Sin datos -->
                        <template #no-data>
                          <div class="text-center py-8" style="color: #888">
                            <v-icon size="40" color="grey">mdi-database-remove</v-icon>
                            <div class="mt-2">No hay campañas disponibles</div>
                          </div>
                        </template>
                      </v-data-table>
                    </div>
                  </v-card>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </div>
      </v-container>
      <transition name="slide-y-reverse-transition">
        <iframe id="iframeChatID" v-if="iframeChat" :src="urlChat" transition="scroll-y-reverse-transition"
          :style="getChatStyle()" frameborder="0">
        </iframe>
      </transition>
    </v-main>

    <!--DIALOGO METRICAS DE CAMPAÑAS-->
    <!-- DIALOG: Detalles de campaña -->

    <v-dialog v-model="dialogMetricasCampana" max-width="1300" persistent @update:model-value="onDialogToggle">
      <v-card-title class="text-h6 custom-scroll"
        style="background-color: #006CA1; color: white; display: flex; align-items: center;">
        <!-- Grupo de icono + texto -->
        <div class="d-flex align-center">
          <v-icon class="mr-2">mdi-chart-bar</v-icon>
          Detalles de la Campaña
        </div>

        <v-spacer></v-spacer>

        <!-- Botón cerrar -->
        <v-btn icon="mdi-close" size="small" :disabled="readOnlyCloseButton" color="white"
          @click="closeDialogMetricas()" class="btn-grow" />
      </v-card-title>

      <v-card class="custom-scroll">

        <v-divider />

        <v-card-text class="mb-n2">
          <!-- PRIMERA FILA: MÉTRICAS + IMAGEN -->
          <v-row class=" justify-space-between">
            <!-- Columna izquierda: Título, fechas y métricas -->
            <v-col cols="12" md="7">
              <div class="d-flex align-center mb-2" style="gap: 12px;">
                <span class="text-h6 font-weight-bold" style="color: #0a1c3a;">
                  {{ selectedCampana?.nombre_campaña || '—' }}
                </span>
                <v-chip v-if="selectedCampana?.canal" class="ml-2"
                  :color="selectedCampana.canal === 2 ? '#1565c0' : selectedCampana.canal === 1 ? '#22C55E' : selectedCampana.canal === 3 ? '#e39005' : selectedCampana.canal === 4 ? '#6c4ee6' : '#888'"
                  text-color="white" size="small" style="font-weight:700; font-size: 1rem; letter-spacing: 0.5px;"
                  elevation="2">
                  <v-icon left size="18" v-if="selectedCampana.canal === 2">mdi-phone</v-icon>
                  <v-icon left size="18" v-else-if="selectedCampana.canal === 1">mdi-whatsapp</v-icon>
                  <v-icon left size="18" v-else-if="selectedCampana.canal === 3">mdi-email</v-icon>
                  <v-icon left size="18" v-else-if="selectedCampana.canal === 4">mdi-instagram</v-icon>
                  {{ canalNombre(selectedCampana.canal) }}
                </v-chip>

                <v-tooltip text="Limpiar Filtros " location="top">
                  <template v-slot:activator="{ props }">
                    <v-menu v-model="menuFiltrosAvanzadosDetalles" :close-on-content-click="false" offset-y
                      location="end" persistent>
                      <template #activator="{ props }">
                        <v-btn color="#006CA1" variant="outlined" v-bind="props" class="ml-2 d-flex align-center"
                          style="min-width: 180px; font-weight:600;">
                          <v-icon left>mdi-tune-variant</v-icon>
                          Filtros avanzados
                        </v-btn>
                      </template>
                      <v-card min-width="520" max-width="600" style="width:520px;">
                        <v-card-title class="text-h6 d-flex align-center"
                          style="background-color: #006CA1; color: white;">
                          <v-icon class="mr-2">mdi-tune-variant</v-icon>
                          Filtros avanzados
                        </v-card-title>
                        <v-divider />
                        <v-card-text>
                          <!-- Selector de filtros a mostrar -->
                          <v-select v-model="filtrosActivos" :items="filtrosDisponibles" item-title="label"
                            item-value="key" label="Selecciona filtros" multiple chips closable-chips variant="outlined"
                            density="comfortable" hide-details prepend-inner-icon="mdi-filter" clearable
                            :menu-props="{ maxHeight: '300px' }" style="width:100%; max-width: 420px;" class="mb-4"
                            autocomplete>
                            <template #selection="{ item, index }">
                              <v-chip v-if="index < 2" :key="item.value" size="small" color="#006CA1" text-color="white"
                                class="mr-1">
                                {{ item.title }}
                              </v-chip>
                              <span v-else-if="index === 2" class="text-caption ml-1">+{{ filtrosActivos.length - 2
                              }}</span>
                            </template>
                          </v-select>
                          <!-- Filtros activos en 2 columnas -->
                          <v-row dense>
                            <v-col v-for="(filtro, idx) in filtrosActivos" :key="filtro" cols="12" md="6"
                              style="max-width: 260px;">
                              <component :is="filtrosComponentes[filtro]" v-model="filtrosModelos[filtro]"
                                :items="filtrosItems[filtro]"
                                :label="filtrosDisponibles.find(f => f.key === filtro)?.label"
                                :disabled="readOnlyCloseButton" variant="outlined" density="comfortable" hide-details
                                clearable class="mb-3"
                                :prepend-inner-icon="filtrosDisponibles.find(f => f.key === filtro)?.icon" v-bind="filtro === 'interes' ? { 'item-title': 'text', 'item-value': 'value' } : 'estado' ? { 'item-title': 'text', 'item-value': 'value' } :
                                  filtro === 'status' ? { 'item-title': 'text', 'item-value': 'value' } :
                                    filtro === 'fechaInicio' || filtro === 'fechaFin' ? { type: 'date' } : {}" />
                            </v-col>
                          </v-row>
                        </v-card-text>
                        <v-card-actions>
                          <v-spacer />
                          <v-btn color="#006CA1" variant="flat"
                            @click="menuFiltrosAvanzadosDetalles = false">Cerrar</v-btn>
                          <v-tooltip text="Limpiar Filtros" location="top">
                            <template v-slot:activator="{ props }">
                              <v-btn :disabled="readOnlyCloseButton" v-bind="props" color="#1d4ed8" icon size="small"
                                class="ml-1 modern-btn btn-grow-card" @click="limpiarFiltrosMetricas()">
                                <v-icon>mdi mdi-broom</v-icon>
                              </v-btn>
                            </template>
                          </v-tooltip>
                        </v-card-actions>
                      </v-card>
                    </v-menu>
                  </template>
                </v-tooltip>

              </div>

              <div class="text-body-2 text-medium-emphasis mb-2" style="font-size: 1.05rem;">
                {{ selectedCampana?.detalle_campaña || '—' }}
              </div>

              <div class="text-body-2 text-medium-emphasis mb-4" style="font-size: 0.98rem;">
                <v-icon size="16" color="#006CA1" class="mr-1">mdi-calendar-edit</v-icon>
                Último envío: {{ formatFecha(getUltimaFechaEnvio()) }}
              </div>
              <span v-if="selectedCampana?.canal === 2"><v-icon size="16" color="#006CA1"
                  class="mr-1">mdi-phone</v-icon>
                Total Envíos: {{ numero(filteredMetricasCampana.length) }}</span>
              <span v-else-if="selectedCampana?.canal === 1"><v-icon size="16" color="#006CA1"
                  class="mr-1">mdi-whatsapp</v-icon> Total Envíos: {{ numero(filteredMetricasCampana.length) }}</span>
              <span v-else-if="selectedCampana?.canal === 3"><v-icon size="16" color="#006CA1"
                  class="mr-1">mdi-email</v-icon> Total Envíos: {{ numero(filteredMetricasCampana.length) }}</span>
              <span v-else-if="selectedCampana?.canal === 4"><v-icon size="16" color="#006CA1"
                  class="mr-1">mdi-share-variant</v-icon> Total Envíos: {{ numero(filteredMetricasCampana.length)
                }}</span>
              <!-- Métricas -->
              <v-row class="metrics-row" no-gutters>
                    <template v-if="selectedCampana?.canal === 2"><!--Canal Email-->
                      <card elevation="4" v-for="m in [
                        { icon: 'mdi-phone', color: '#1565c0', label: 'Total llamadas', val: numero(filteredMetricasCampana.length) },
                        { icon: 'mdi-account-check', color: '#19bf56', label: 'Efectivas c/Lead', val: numero(filteredMetricasCampana.filter(r => r.efectivo_con_lead === true).length) },
                        { icon: 'mdi-account-plus', color: '#3f94e8', label: 'Efectivas s/Lead', val: numero(filteredMetricasCampana.filter(r => r.efectivo_sin_lead === true).length) },
                        { icon: 'mdi-account-cancel', color: '#de8d04', label: 'No efectivas', val: numero(filteredMetricasCampana.filter(r => r.no_efectivo === true).length) }
                      ]" :key="m.label" class="metric-card btn-grow-card">
                        <div class="d-flex align-center mb-1">
                          <v-icon size="18" :color="m.color" class="ml-1">{{ m.icon }}</v-icon>
                          <span class="metric-label" :style="{ color: m.color }">{{ m.label }}</span>
                        </div>
                        <div class="metric-value">{{ m.val }}</div>
                      </card>
                    </template>
                    <template v-else-if="selectedCampana?.canal === 1"> <!--Canal Whatsapp-->
                      <card v-if="selectedCampana.plantilla_envio == 'promocionar_productos_servicios'" v-for="m in [
                        { icon: 'mdi-check-all', color: '#1565c0', label: 'Entregadas', val: numero(filteredMetricasCampana.filter(r => r.status_mensaje === 'delivered' || r.status_mensaje === 'read').length) },
                        { icon: 'mdi-check', color: '#db3030', label: 'No Entregadas', val: numero(filteredMetricasCampana.filter(r => r.status_mensaje === 'sent').length) },
                        { icon: 'mdi-cancel', color: '#de8d04', label: 'No Existe', val: numero(filteredMetricasCampana.filter(r => r.status_mensaje === 'failed').length) },
                        { icon: 'mdi-thumb-up', color: '#22C55E', label: 'Interés positivo', val: numero(filteredMetricasCampana.filter(r => r.interes === 1).length) },
                        { icon: 'mdi-thumb-down', color: '#d95323', label: 'Interés negativo', val: numero(filteredMetricasCampana.filter(r => r.interes === 2).length) },
                        { icon: 'mdi-help-circle-outline', color: '#454a52', label: 'Sin respuesta', val: numero(filteredMetricasCampana.filter(r => r.interes === 0).length) }
                      ]" :key="m.label" class="metric-card btn-grow-card">
                        <div class="d-flex align-center mb-1">
                          <v-icon size="18" :color="m.color" class="mr-1 ml-2">{{ m.icon }}</v-icon>
                          <span class="metric-label" :style="{ color: m.color }">{{ m.label }}</span>
                        </div>
                        <div class="metric-value">{{ m.val }}</div>
                      </card>
                      <card v-if="selectedCampana.plantilla_envio == 'boletin_informativo'" v-for="m in [
                        { icon: 'mdi-check-all', color: '#1565c0', label: 'Entregadas', val: numero(filteredMetricasCampana.filter(r => r.status_mensaje === 'delivered' || r.status_mensaje === 'read').length) },
                        { icon: 'mdi-check', color: '#db3030', label: 'No Entregadas', val: numero(filteredMetricasCampana.filter(r => r.status_mensaje === 'sent').length) },
                        { icon: 'mdi-cancel', color: '#de8d04', label: 'No Existe', val: numero(filteredMetricasCampana.filter(r => r.status_mensaje === 'failed').length) },
                      ]" :key="m.label" class="metric-card btn-grow-card">
                        <div class="d-flex align-center mb-1">
                          <v-icon size="18" :color="m.color" class="mr-1 ml-2">{{ m.icon }}</v-icon>
                          <span class="metric-label" :style="{ color: m.color }">{{ m.label }}</span>
                        </div>
                        <div class="metric-value">{{ m.val }}</div>
                      </card>
                    </template>
                    <template v-else-if="selectedCampana?.canal === 3">
                      <card elevation="4" v-for="m in [
                        { icon: 'mdi-check-circle', color: '#19bf56', label: 'Entregadas', val: numero(filteredMetricasCampana.filter(r => r.entregada === true).length) },
                        { icon: 'mdi-cancel', color: '#de8d04', label: 'No Recibidas', val: numero(filteredMetricasCampana.filter(r => r.entregada === false).length) },
                        { icon: 'mdi-email-check', color: '#3f94e8', label: 'Con respuesta', val: numero(filteredMetricasCampana.filter(r => r.con_respuesta === true).length) },
                        { icon: 'mdi-help-circle-outline', color: '#454a52', label: 'Sin respuesta', val: numero(filteredMetricasCampana.filter(r => r.interes === 0).length) }
                      ]" :key="m.label" class="metric-card btn-grow-card">
                        <div class="d-flex align-center mb-1">
                          <v-icon size="18" :color="m.color" class="mr-1">{{ m.icon }}</v-icon>
                          <span class="metric-label" :style="{ color: m.color }">{{ m.label }}</span>
                        </div>
                        <div class="metric-value">{{ m.val }}</div>
                      </card>
                    </template>
                    <template v-if="selectedCampana?.canal === 4">
                      <card v-for="m in [
                        { icon: 'mdi-check-circle', color: '#19bf56', label: 'Entregadas', val: numero(filteredMetricasCampana.length) },
                        { icon: 'mdi-cancel', color: '#de8d04', label: 'No Recibidas', val: numero(selectedCampana?.no_entregadas ?? 0) },
                        { icon: 'mdi-thumb-up', color: '#22C55E', label: 'Interés positivo', val: numero(filteredMetricasCampana.filter(r => r.interes === 1).length) },
                        { icon: 'mdi-thumb-down', color: '#d95323', label: 'Interés negativo', val: numero(filteredMetricasCampana.filter(r => r.interes === 2).length) },
                        { icon: 'mdi-help-circle-outline', color: '#454a52', label: 'Sin respuesta', val: numero(filteredMetricasCampana.filter(r => r.interes === 0).length) }
                      ]" :key="m.label" class="metric-card btn-grow-card">
                        <div class="d-flex align-center mb-1">
                          <v-icon size="18" :color="m.color" class="mr-1 ml-2">{{ m.icon }}</v-icon>
                          <span class="metric-label" :style="{ color: m.color }">{{ m.label }}</span>
                        </div>
                        <div class="metric-value">{{ m.val }}</div>
                      </card>
                    </template>
                  </v-row>
            </v-col>
            <!-- Columna derecha: Imagen (a la derecha en md+) -->
            <v-col cols="12" md="5" class="d-flex justify-center align-center">
              <v-sheet rounded="lg" elevation="1" class="w-100 d-flex align-center justify-center"
                style="min-height: 274px;">
                <template v-if="esVideo(selectedCampana?.url_media)">
                  <video :src="selectedCampana?.url_media" class="w-100"
                    style="max-width:460px; border-radius:12px; background:#f5f6f7;" controls height="240" width="200"
                    poster="https://img.freepik.com/vector-gratis/diseno-plantilla-reproductor-video-estilo-blanco-minimo_1017-25481.jpg?semt=ais_incoming&w=740&q=80"
                    aspect-ratio="16/9"></video>
                </template>
                <template v-else>
                  <v-img
                    :src="selectedCampana?.url_media || 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s'"
                    class="w-100" height="240" width="200" aspect-ratio="16/9" contain
                    style="object-fit:cover; object-position:center; background:#f5f6f7; border-radius:12px;"
                    @click="abrirImagenAmpliada(selectedCampana?.url_media || 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s')">
                    <template #error>
                      <v-img
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s"
                        height="240" width="200" cover
                        style="object-fit:cover; object-position:center; background:#f5f6f7; border-radius:12px;" />
                    </template>
                  </v-img>
                </template>

              </v-sheet>
            </v-col>

          </v-row>
        </v-card-text>
        <v-divider :thickness="3" color="#0A1C3A" class="border-opacity-50 mt-4 mb-4"></v-divider>
        <v-card-text>
          <v-card-title class="text-subtitle-1 d-flex align-center justify-space-between"
            style="background-color: #006CA1; color:white; border-radius:8px;">
            <div class="d-flex align-center">
              <v-icon icon="mdi mdi-chart-areaspline" color="white" class="mr-2" />
              <span>Gráficos y Estadísticas</span>
            </div>
          </v-card-title>
          <v-row dense>
            <!-- Izquierda: Barras -->
            <v-col cols="12" md="7">
              <div class="text-body-2 font-weight-bold mb-1">Rendimiento Diario</div>
              <v-sheet elevation="1" rounded="lg" class="pa-3">
                <!-- Alto fijo reducido -->
                <div style="width:100%; height:320px;">
                  <canvas ref="barCanvas"></canvas>
                </div>
              </v-sheet>
            </v-col>

            <!-- Derecha: Doughnut -->
            <v-col cols="12" md="5">
              <div class="text-body-2 font-weight-bold mb-1">Distribución de Respuestas
                <div v-if="[1, 3, 4].includes(selectedCampana?.canal)" class="mb-2"
                  style="max-width: 180px; max-height: 70px;">
                  <v-select v-model="modoDonutDetalle" :items="[
                    { value: 'interacciones', title: 'Interacciones' },
                    { value: 'envios', title: 'Envios' }
                  ]" label="Modo de gráfico" variant="outlined" dense hide-details style="font-size: 0.7rem;" />
                </div>
              </div>
              <v-sheet elevation="1" rounded="lg" class="pa-3 content-center">
                <!-- Donut + detalle -->

                <div class="d-flex flex-wrap" style="width:100%;">
                  <!-- Donut -->

                  <div style="flex:1 1 0; min-width:200px; height:232px;">

                    <canvas ref="donutCanvas"></canvas>
                  </div>

                  <!-- Detalle -->
                  <!--
                    <div style="flex:0 0 200px;" class="d-flex flex-column ml-2">
                      <div v-for="item in distribucionDetalle" :key="item.key"
                        class="d-flex align-center justify-space-between py-1 border-b">
                        <div class="d-flex align-center">
                          <v-icon class="mr-1" :color="item.color" size="16">{{ item.icon }}</v-icon>
                          <span class="text-caption" :style="{ color: item.color }">{{ item.label }}</span>
                        </div>
                        <div class="text-caption font-weight-medium">
                           {{ numero(item.value) }} <span class="text-medium-emphasis">({{ item.pct }}%)</span> 
                        </div>
                      </div>
                    </div>
                    -->
                </div>


                <!-- Leyenda compacta dinámica -->
                <div class="d-flex mt-2 justify-center" style="gap: 12px;">
                  <div v-for="item in getLeyendaDonutDetalle(selectedCampana)" :key="item.label"
                    class="d-flex align-center">
                    <v-icon size="14" :color="item.color" class="mr-1">{{ item.icon }}</v-icon>
                    <span class="text-caption" :style="{ color: item.color }">{{ item.label }}</span>
                  </div>
                </div>
              </v-sheet>
            </v-col>
          </v-row>
        </v-card-text>

        <v-divider :thickness="3" color="#0A1C3A" class="border-opacity-50 mt-2 mb-2"></v-divider>
        <!-- Tabla de Respuestas Detalladas -->
        <v-card-text>
          <v-card-title class="text-subtitle-1 d-flex"
            style="background-color: #006CA1; color:white; border-radius:8px;">
            <div class="d-flex align-center">
              <v-icon icon="mdi mdi-chart-areaspline" color="white" class="mr-2" />
              <span>Tabla de Respuestas Detalladas</span>
            </div>
            <v-spacer></v-spacer>
            <v-btn icon="mdi-download" size="small" color="white" class="mr-2 btn-grow" :disabled="readOnlyCloseButton"
              @click="verDetallesCampana(idCampaniaSeleccionada); redibujarBarCanvas();">
              <v-icon left>mdi-reload</v-icon>
            </v-btn>
            <v-tooltip text="Limpiar Filtros " location="top">
              <template v-slot:activator="{ props }">
                <v-menu v-model="menuFiltrosAvanzadosDetalles2" :close-on-content-click="false" offset-y location="end"
                  persistent>
                  <template #activator="{ props }">
                    <v-btn color="white" variant="outlined" v-bind="props" class="ml-2 d-flex align-center"
                      style="min-width: 180px; font-weight:600;">
                      <v-icon left>mdi-tune-variant</v-icon>
                      Filtros avanzados
                    </v-btn>
                  </template>
                  <v-card min-width="520" max-width="600" style="width:520px;">
                    <v-card-title class="text-h6 d-flex align-center" style="background-color: #006CA1; color: white;">
                      <v-icon class="mr-2">mdi-tune-variant</v-icon>
                      Filtros avanzados
                    </v-card-title>
                    <v-divider />
                    <v-card-text>
                      <!-- Selector de filtros a mostrar -->
                      <v-select v-model="filtrosActivos" :items="filtrosDisponibles" item-title="label" item-value="key"
                        label="Selecciona filtros" multiple chips closable-chips variant="outlined"
                        density="comfortable" hide-details prepend-inner-icon="mdi-filter" clearable
                        :menu-props="{ maxHeight: '300px' }" style="width:100%; max-width: 420px;" class="mb-4"
                        autocomplete>
                        <template #selection="{ item, index }">
                          <v-chip v-if="index < 2" :key="item.value" size="small" color="#006CA1" text-color="white"
                            class="mr-1">
                            {{ item.title }}
                          </v-chip>
                          <span v-else-if="index === 2" class="text-caption ml-1">+{{ filtrosActivos.length - 2
                          }}</span>
                        </template>
                      </v-select>
                      <!-- Filtros activos en 2 columnas -->
                      <v-row dense>
                        <v-col v-for="(filtro, idx) in filtrosActivos" :key="filtro" cols="12" md="6"
                          style="max-width: 260px;">
                          <component :is="filtrosComponentes[filtro]" v-model="filtrosModelos[filtro]"
                            :items="filtrosItems[filtro]" :label="filtrosDisponibles.find(f => f.key === filtro)?.label"
                            :disabled="readOnlyCloseButton" variant="outlined" density="comfortable" hide-details
                            clearable class="mb-3"
                            :prepend-inner-icon="filtrosDisponibles.find(f => f.key === filtro)?.icon" v-bind="filtro === 'interes' ? { 'item-title': 'text', 'item-value': 'value' } : 'estado' ? { 'item-title': 'text', 'item-value': 'value' } :
                              filtro === 'status' ? { 'item-title': 'text', 'item-value': 'value' } :
                                filtro === 'fechaInicio' || filtro === 'fechaFin' ? { type: 'date' } : {}" />
                        </v-col>
                      </v-row>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer />
                      <v-btn color="#006CA1" variant="flat"
                        @click="menuFiltrosAvanzadosDetalles2 = false">Cerrar</v-btn>
                      <v-tooltip text="Limpiar Filtros" location="top">
                        <template v-slot:activator="{ props }">
                          <v-btn :disabled="readOnlyCloseButton" v-bind="props" color="#1d4ed8" icon size="small"
                            class="ml-1 modern-btn btn-grow-card" @click="limpiarFiltrosMetricas()">
                            <v-icon>mdi mdi-broom</v-icon>
                          </v-btn>
                        </template>
                      </v-tooltip>
                    </v-card-actions>
                  </v-card>
                </v-menu>
              </template>
            </v-tooltip>

            <v-text-field v-model="searchProsp" placeholder="Buscar contacto, ciudad o sector"
              prepend-inner-icon="mdi-magnify" density="compact" variant="solo" clearable class="header-search ml-4"
              hide-details style="max-width: 320px; background: white; border-radius: 8px;" />
          </v-card-title>
          <v-data-table :headers="headersVisibles" :items="tablaRespuestasFiltrada"
            :filter-keys="['nombre_contacto', 'nombre_empresa', 'nombre_cargo', 'nombre_cat_cargo', 'nombre_departamento', 'nombre_ciudad', 'nombre_sector', 'fecha_envio', 'status_mensaje']"
            :search="null" :custom-filter="() => true" :items-per-page="10" :items-per-page-options="[10, 20, 50]"
            :row-class="rowClass"
            class="elevation-1 data-table-campanas fancy-headers fancy-rows-campanas hoverable-rows" height="300"
            @click:row="(event, row) => abrirGestion(row.item)">
            <!-- Headers personalizados -->
            <template #header.nombre_contacto="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-account</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.nombre_empresa="{ column }">
              <div class="th-content" width="300">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-office-building</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.nombre_cargo="{ column }">
              <div class="th-content" width="300">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-account-tie</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.nombre_cat_cargo="{ column }">
              <div class="th-content" width="300">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-account-details</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.nombre_sector="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-domain</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.nombre_departamento="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-city</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.nombre_ciudad="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-city-variant</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.fecha_envio="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi mdi-send-clock</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.interes="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-lightbulb-on-10</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.status_mensaje="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi mdi-chat</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>
            <template #header.estado="{ column }">
              <div class="th-content">
                <v-icon size="16" class="mr-2" color="#006CA1">mdi-check-decagram</v-icon>
                <span>{{ column.title }}</span>
              </div>
            </template>

            <!-- Interés unificado -->
            <template #item.interes="{ value }">
              <span class="th-content" :style="{ color: interesColor(value) }">
                {{ interesLabel(value) }}
              </span>
            </template>

            <!-- Status Mensaje -->
            <template #item.status_mensaje="{ value }">
              <v-chip size="small" :color="statusColor(value)" variant="tonal" class="th-content">
                {{ statusLabel(value) }}
              </v-chip>
            </template>

            <!-- Estado -->
            <template #item.estado="{ item }">
              <v-chip size="small" :color="estadoColor(item.estado)" variant="tonal" class="text-subtitle-2"
                v-if="selectedCampana?.activo === 1">
                {{ estadoLabel(item.estado) }}
              </v-chip>
            </template>

            <!-- FECHA DE ENVIO -->
            <template #item.fecha_envio="{ item }">
              <span>
                {{ formatFechaCorta(item.fecha_envio || item.fecha) }}
              </span>
            </template>
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-dialog>

    <!-- Dialogo Ciudades -->
    <v-dialog v-model="dialogCiudades" max-width="420">
      <v-card>
        <v-card-title class="d-flex align-center" style="background:#006CA1; color:white;">
          <v-icon class="mr-2">mdi-city</v-icon>
          Ciudades de la campaña
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="buscadorCiudad" prepend-inner-icon="mdi-magnify" label="Buscar ciudad"
            variant="outlined" dense clearable hide-details class="mb-3" />
          <div class="d-flex flex-wrap" style="gap: 8px;">
            <v-chip v-for="ciudad in ciudadesFiltradas" :key="ciudad" color="#1976d2" text-color="white" size="small"
              label @click="searchProsp = ciudad">
              <v-icon size="14" class="mr-1" color="#1976d2">mdi-city</v-icon>
              {{ ciudad }}
            </v-chip>
          </div>
          <div v-if="ciudadesFiltradas.length === 0" class="text-medium-emphasis mt-4 text-center">
            No se encontraron ciudades.
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="#006CA1" variant="flat" @click="dialogCiudades = false">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Dialogo Sectores -->
    <v-dialog v-model="dialogSectores" max-width="420">
      <v-card>
        <v-card-title class="d-flex align-center" style="background:#006CA1; color:white;">
          <v-icon class="mr-2">mdi-domain</v-icon>
          Sectores de la campaña
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="buscadorSector" prepend-inner-icon="mdi-magnify" label="Buscar sector"
            variant="outlined" dense clearable hide-details class="mb-3" />
          <div class="d-flex flex-wrap" style="gap: 8px;">
            <v-chip v-for="sector in sectoresFiltrados" :key="sector" color="#1976d2" text-color="white" size="small"
              class="btn-grow-card" label @click="searchProsp = sector">
              <v-icon size="14" class="mr-1" color="#1976d2">mdi-domain</v-icon>
              {{ sector }}
            </v-chip>
          </div>
          <div v-if="sectoresFiltrados.length === 0" class="text-medium-emphasis mt-4 text-center">
            No se encontraron sectores.
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="#006CA1" variant="flat" @click="dialogSectores = false">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!--FIN DIALOG: DETALLES DE CAMPAÑA-->

    <!-- DIÁLOGO: Gestionar respuesta -->
    <v-dialog v-model="dialogGestionCampanas" max-width="900" persistent>
      <v-card>
        <!-- Header -->
        <v-card-title class="py-2 px-4" style="background:#006CA1; color:#fff; display:flex; align-items:center">
          <div class="d-flex align-center">
            <v-icon size="18" class="mr-2">mdi-clipboard-text</v-icon>
            <span class="text-subtitle-1">Gestionar respuesta: {{ selectedRespuesta.nombre_contacto }}</span>
          </div>
          <v-spacer />
          <v-btn icon size="30" color="white" @click="cerrarFormularioGestionCampaña()">
            <v-icon size="20">mdi-close</v-icon>
          </v-btn>
        </v-card-title>

        <v-card-text class="pt-4 pb-4 px-4">
          <v-row dense>
            <!-- Historial -->
            <v-col cols="12" md="6">
              <div class="text-h6 font-weight-bold mb-2 d-flex justify-center">Historial de Gestión: {{
                selectedRespuesta.nombre_contacto }}</div>

              <v-sheet rounded="lg" elevation="1" class="pa-3 overflow-y-auto"
                style="max-height: 450px; padding-right: 10px;" ref="historialSheet">
                <div v-for="(h, i) in historialCampania" :key="i" class="mb-4">
                  <div class="text-h6 font-weight-bold">{{ formatFecha2(h.fecha) }}</div>
                  <div class="text-caption text-medium-emphasis">{{ h.hora }}</div>
                  <div class="mt-2"><span :style="{ color: interesColor(h.interes) }"> {{ interesLabel(h.interes) }}
                    </span></div>
                  <div class="mt-2"><span :style="{ color: estadoColor(h.estado) }"> {{ estadoLabel(h.estado) }}
                    </span>
                  </div>
                  <div class="mt-2" v-if="h.descripcion !== 'Chat WhatsApp'">{{ h.respuesta }}</div>
                  <div class="mt-2" v-if="h.descripcion === 'Chat WhatsApp'">
                    <template v-if="parseWhatsApp(h.respuesta)">
                      <div>
                        <template v-if="parseWhatsApp(h.respuesta).outgoing === 1">
                          <b style="color:#0A1C3A"><v-icon size="small">mdi-whatsapp</v-icon> {{ h.nombre_usu }}
                            dijo:</b>
                        </template>
                        <template v-else-if="parseWhatsApp(h.respuesta).outgoing === 0">
                          <b style="color:purple"><v-icon size="small">mdi-whatsapp</v-icon> Cliente dijo:</b>
                        </template>
                        <template v-else>
                          <b>Mensaje:</b>
                        </template>
                      </div>
                      <div style="margin-top:2px;">
                        <div v-if="parseWhatsApp(h.respuesta).tipo === 'text'" style="white-space: pre-line;">
                          <span v-if="!expandedMessages[i]">
                            {{ truncateText(removeHeader(parseWhatsApp(h.respuesta).mensaje), 180) }}
                            <template v-if="shouldShowExpand(parseWhatsApp(h.respuesta).mensaje, 180)">
                              <v-icon size="18" color="#006CA1" style="cursor:pointer; vertical-align:middle;"
                                @click="expandedMessages = { ...expandedMessages, [i]: true }"
                                title="Ver más">mdi-eye</v-icon> <strong
                                @click="expandedMessages = { ...expandedMessages, [i]: true }">Ver más</strong>
                            </template>
                          </span>
                          <span v-else>
                            {{ removeHeader(parseWhatsApp(h.respuesta).mensaje) }}
                            <v-icon size="18" color="#006CA1" style="cursor:pointer; vertical-align:middle;"
                              @click="expandedMessages = { ...expandedMessages, [i]: false }"
                              title="Ver menos">mdi-eye-off</v-icon> <strong
                              @click="expandedMessages = { ...expandedMessages, [i]: false }">Ver menos</strong>
                          </span>
                        </div>
                        <img v-else-if="parseWhatsApp(h.respuesta).tipo === 'image'"
                          :src="parseWhatsApp(h.respuesta).mensaje" alt="Imagen"
                          style="max-width:220px; max-height:220px; border-radius:8px; box-shadow:0 2px 8px #888; margin-top:6px; display:block;" />
                        <audio v-else-if="parseWhatsApp(h.respuesta).tipo === 'audio'" controls
                          style="margin-top:6px; max-width:220px; display:block;">
                          <source :src="parseWhatsApp(h.respuesta).mensaje">
                        </audio>
                        <video v-else-if="parseWhatsApp(h.respuesta).tipo === 'video'" controls
                          style="margin-top:6px; max-width:220px; display:block;">
                          <source :src="parseWhatsApp(h.respuesta).mensaje">
                        </video>
                        <a v-else-if="parseWhatsApp(h.respuesta).tipo === 'document'"
                          :href="parseWhatsApp(h.respuesta).mensaje" target="_blank"
                          style="color:#006CA1; text-decoration:underline; display:block; margin-top:6px;">{{
                            getFileName(parseWhatsApp(h.respuesta).mensaje) }}</a>
                        <span v-else>{{ parseWhatsApp(h.respuesta).mensaje }}</span>
                      </div>
                    </template>
                    <template v-else>
                      {{ h.respuesta }}
                    </template>
                  </div>
                  <div class="mb-2" style="font-size: 13px; color: #888;">
                    <span v-if="h.url_archivos">
                      <!-- necesitamos mostrar para cada archivo, un icono de un documento, con su nombre al lado y que sea seleccionable como hipervinculo-->
                      <div v-for="(archivo, idx) in h.url_archivos.split('----')" :key="idx">
                        <v-icon size="small" class="mr-1" color="#006CA1">mdi-file</v-icon>
                        <a :href="archivo" target="_blank" style="color: #006CA1; text-decoration: underline;">
                          {{ getFileName(archivo) }}
                        </a>
                      </div>
                    </span>
                    <span v-else>Sin archivos</span>
                  </div>
                  <v-divider class="my-3" v-if="i < historialCampania.length - 1" />
                </div>

                <div v-if="!historialCampania.length" class="text-medium-emphasis text-caption">
                  Aún no hay registros.
                </div>
              </v-sheet>
            </v-col>

            <!-- Formulario -->
            <v-col cols="12" md="6">
              <div class="text-h6 font-weight-bold mb-2 d-flex justify-center">Genera la respuesta</div>
              <v-alert v-if="tieneCasoResuelto" class="mx-0 mb-4 mt-2 modern-alert" type="error" prominent
                icon="mdi-account-alert" style="font-size: 0.9rem;">
                <span style="font-weight: 500;">No se puede registrar una nueva respueta, el caso fue registrado como
                  resuelto</span>
              </v-alert>
              <v-sheet rounded="lg" elevation="1" class="pa-3">
                <v-textarea v-model="selectedGestionCampania" label="Gestión" variant="outlined" auto-grow rows="3"
                  density="comfortable" class="mb-3" :disabled="tieneCasoResuelto" />

                <v-select v-model="selectedEstadoCampania" :items="estadoItems" item-title="label" item-value="id"
                  label="Estado" variant="outlined" density="comfortable" class="mb-3" :disabled="tieneCasoResuelto" />

                <v-select v-model="selectedInteresCampania" :items="interesItems" item-title="label" item-value="id"
                  label="Interés" variant="outlined" density="comfortable" class="mb-3" :disabled="tieneCasoResuelto" />

                <v-file-input v-model="selectedArchivoCampania" multiple label="Adjuntar archivos" variant="outlined"
                  density="comfortable" prepend-icon="mdi-paperclip" show-size class="mb-4"
                  :disabled="tieneCasoResuelto" />

                <div class="d-flex align-center justify-space-between">

                  <v-spacer />

                  <v-row>
                    <v-btn class="mb-1 ml-auto mr-8 btn-grow" size="small" icon="mdi-whatsapp"
                      @click="activarChat(this.selectedRespuesta)" style="background: rgb(153, 255, 150);"></v-btn>
                  </v-row>
                  <v-btn color="primary" class="btn-grow" @click="GuardarGestionCampaña()"
                    :disabled="tieneCasoResuelto">
                    Guardar
                  </v-btn>
                </div>
              </v-sheet>
            </v-col>
          </v-row>
        </v-card-text>


      </v-card>
    </v-dialog>
    <!--FIN DIALOGO GESTION-->

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

    <v-dialog v-model="alerta" persistent style="z-index: 10000;">
      <v-card :style="getAlertStyle()">
        <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
          class="mx-auto"></v-progress-circular>
        <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-tittle>
        <v-btn class="mt-4 mx-auto" @click="cerrarDIV()"
          style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
      </v-card>
    </v-dialog>

    <v-dialog v-model="alertaInteres" persistent>
      <v-card :style="getAlertStyle2()">
        <v-card-title
          style="color: black; text-align: center; white-space: normal; word-break: break-word; overflow: visible;">
          {{ mensajeAlertInteres }}
        </v-card-title>
        <v-card-text>
          <v-select v-model="selectedInteresCampaniaWhatsapp" :items="interesItems" item-title="label" item-value="id"
            label="Interés" variant="outlined" density="comfortable" class="mb-3" :disabled="tieneCasoResuelto"
            return-object />
        </v-card-text>
        <v-card-actions class="pt-0 mt-n6">
          <v-btn class="mr-n10" @click="agregarHistorialGestion()"
            style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;"
            :disabled="!selectedInteresCampaniaWhatsapp">Guardar</v-btn>
          <v-btn @click="alertaInteres = false; selectedInteresCampaniaWhatsapp = null; mensajesAlmacenados = [];"
            style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cancelar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import AppHeader from '../components/AppHeader.vue';
import axios from "axios";
import Pusher from 'pusher-js';
import Echo from 'laravel-echo';
import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

window.Pusher = Pusher;

import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  Filler,
  ArcElement,
  DoughnutController,
  PieController,
  BarController,
  BarElement,
} from "chart.js";

Chart.register(
  LineController,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  Filler,
  ArcElement,
  DoughnutController,
  PieController,
  BarController,
  BarElement
);

const doughnutLabelPlugin = {
  id: "doughnutLabelPlugin",
  afterDraw(chart) {
    const { ctx, data } = chart;
    if (!data || !data.datasets.length) return;
    const meta = chart.getDatasetMeta(0);
    const total = data.datasets[0].data.reduce((a, b) => a + b, 0);
    meta.data.forEach((element, i) => {
      const value = data.datasets[0].data[i];
      const percent = total ? ((value / total) * 100).toFixed(1) : 0;
      const { x, y } = element.tooltipPosition();
      ctx.save();
      ctx.font = "bold 14px Arial";
      ctx.fillStyle = "#fff";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.shadowColor = "rgba(0,0,0,0.2)";
      ctx.shadowBlur = 2;
      ctx.fillText(`${percent}%`, x, y);
      ctx.restore();
    });
  },
};

export default {
  components: {
    AppHeader
  },
  data: () => ({
    // Mapeo de keys de filtro a keys de columna
    filtroToHeaderKey: {
      contacto: 'nombre_contacto',
      empresa: 'nombre_empresa',
      cargo: 'nombre_cargo',
      categoriaCargo: 'nombre_cat_cargo',
      sector: 'nombre_sector',
      departamento: 'nombre_departamento',
      ciudad: 'nombre_ciudad',
      interes: 'interes',
      status: 'status_mensaje',
      estado: 'estado',
      fechaInicio: 'fecha_envio',
      fechaFin: 'fecha_envio',
    },
    baseURL: import.meta.env.VITE_API_BASE_URL,
    comercialId: localStorage.getItem('idUsuario'),
    nombreComercial: localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin'),
    celularComercial: localStorage.getItem('celularLogin'),
    idCargo: null,
    correoUsuario: null,
    menuAbierto: false,
    drawer: false,
    dialogCambioClave: false,
    claveActual: null,
    nuevaClave: null,
    confirmarClave: null,
    alerta: false,
    mensajeAlertLogin: "",
    mostrarClaveActual: false,
    mostrarNuevaClave: false,
    mostrarConfirmarClave: false,

    listaCampañas: [],
    campañaSeleccionada: null,
    ciudadSeleccionada: null,
    sectorSeleccionado: null,
    fechaInicio: null,
    fechaFin: null,

    filtroNombreCampania: "",

    arregloOriginal: [],
    totalOriginal: 0,
    entregadosOriginal: 0,
    positivoOriginal: 0,
    negativoOriginal: 0,
    sinrespuestaOriginal: 0,

    totalCampanasEnviadas: 0,
    totalEntregadas: 0,
    totalInteresPositivo: 0,
    totalInteresNegativo: 0,
    totalSinRespuesta: 0,

    totalxCampaña: [],
    totalxCampañaOriginal: [],

    tipoGraficoDonut: "Por Canal",
    opcionesGraficoDonut: [
      { value: "Por Canal", title: "Por Canal" },
    ],
    mostrarCiudadesDialog: false,
    ciudadesDialogList: [],

    mostrarSectoresDialog: false,
    sectoresDialogList: [],
    dialogMetricasCampana: false,
    dialogGestionCampanas: false,
    readOnlyCloseButton: true,

    listaCampañas: [

    ],

    tablaHeaders: [
      { title: 'Contacto', key: 'nombre_contacto', minWidth: 180, width: 180, align: 'center' },
      { title: 'Empresa', key: 'nombre_empresa', minWidth: 180, width: 180, align: 'center' },
      { title: 'Cargo', key: 'nombre_cargo', minWidth: 150, width: 150, align: 'center' },
      { title: 'Categoria Cargo', key: 'nombre_cat_cargo', minWidth: 180, width: 180, align: 'center' },
      { title: 'Sector', key: 'nombre_sector', minWidth: 150, width: 150, align: 'center' },
      { title: 'Departamento', key: 'nombre_departamento', minWidth: 180, width: 180, align: 'center' },
      { title: 'Ciudad', key: 'nombre_ciudad', minWidth: 150, width: 150, align: 'center' },
      { title: 'Fecha de envio', key: 'fecha_envio', align: 'center', minWidth: 180, width: 180 },
      { title: 'Interés', key: 'interes', minWidth: 150, width: 150, align: 'center' },
      { title: 'Mensaje', key: 'status_mensaje', minWidth: 150, width: 150, align: 'center' },
      { title: 'Gestión', key: 'estado', minWidth: 150, width: 150, align: 'center' },

    ],
    historialCampania: [

    ],
    estadoItems: [
      { id: 1, label: 'Nuevo' },
      { id: 2, label: 'En proceso' },
      { id: 3, label: 'Resuelto' },
    ],
    interesItems: [
      { id: 0, label: 'Sin respuesta' },
      { id: 1, label: 'Interés positivo' },
      { id: 2, label: 'Interés negativo' },
    ],
    selectedGestionCampania: null,
    selectedEstadoCampania: null,
    selectedInteresCampania: null,
    selectedArchivoCampania: [],

    selectedCampanaResponses: [],
    selectedCampana: null,
    tipoGraficoBarra: 'interacciones',
    opcionesGraficoBarra: [
      { value: 'interacciones', title: 'Por interacciones' },
      { value: 'todas', title: 'Ver todas las campañas' },
      { value: 'canales', title: 'Por canal' },
    ],
    campañasSeleccionadas: [],
    iframeChat: false,
    urlChat: '',
    estadoChat: false,
    celularSeleccionado: null,
    soundUrl2: 'https://glpi-siicsa.azurewebsites.net/notificacionSonido2.mp3',
    notificacionNueva: null,
    celularContacto: null,

    alertaInteres: false,
    mensajeAlertInteres: null,
    selectedInteresCampaniaWhatsapp: null,
    mensajesAlmacenados: [],
    tieneCasoResuelto: false,
    expandedMessages: {},

    created() {
      window.addEventListener("message", (e) => this.recibirMensaje(e));
      this.headersVisibles = this.tablaHeaders.slice();
    },
    beforeDestroy() {
      window.removeEventListener("message", (e) => this.recibirMensaje(e));
    },
    canalSeleccionado: 0,
    canales: [
      { value: 0, label: "Todos", icon: "mdi-diamond", color: "#1565c0", id: 0 },
      { value: 1, label: "WhatsApp", icon: "mdi-whatsapp", color: "#029e3b", id: 1 },
      { value: 2, label: "Telefónico", icon: "mdi-phone", color: "#5761f7", id: 2 },
      { value: 3, label: "Email", icon: "mdi-email", color: "#e39005", id: 3 },
    ],
    canalesDeshabilitados: false,
    datosCargados: false,
    modoDonut: 'interacciones',
    modoDonutDetalle: 'interacciones',

    dialogCiudades: false,
    dialogSectores: false,
    buscadorCiudad: '',
    buscadorSector: '',
    ciudadesDialog: [],
    sectoresDialog: [],

    searchProsp: '',
    menuActivo: '',

    searchProsp: '',
    menuActivo: '',

    filtroEntregadasMetricas: null,
    filtroContactoMetricas: null,
    filtroEmpresaMetricas: null,
    filtroCargoMetricas: null,
    filtroCategoriaCargoMetricas: null,
    filtroDepartamentoMetricas: null,
    filtroStatusMessageMetricas: null,
    filtroCiudadMetricas: null,
    filtroSectorMetricas: null,
    filtroInteresMetricas: null,
    filtroFechaInicioMetricas: '',
    filtroFechaFinMetricas: '',
    filtroEstadoMetricas: null,

    menuFiltrosAvanzadosDetalles: false,
    menuFiltrosAvanzadosDetalles2: false,
    // Nuevo: estado del menu de filtros para la tabla principal
    menuFiltrosAvanzadosTabla: false,
    filtroEstadoCampana: 'habilitadas', // o null


    filtrosDisponibles: [
      { key: 'contacto', label: 'Contacto', icon: 'mdi-account', tipo: 'autocomplete' },
      { key: 'empresa', label: 'Empresa', icon: 'mdi-briefcase', tipo: 'autocomplete' },
      { key: 'cargo', label: 'Cargo', icon: 'mdi-account-tie', tipo: 'autocomplete' },
      { key: 'categoriaCargo', label: 'Categoria Cargo', icon: 'mdi-format-list-bulleted-type', tipo: 'autocomplete' },
      { key: 'sector', label: 'Sector', icon: 'mdi-domain', tipo: 'autocomplete' },
      { key: 'departamento', label: 'Departamento', icon: 'mdi-city', tipo: 'autocomplete' },
      { key: 'ciudad', label: 'Ciudad', icon: 'mdi-city', tipo: 'autocomplete' },
      { key: 'interes', label: 'Interés', icon: 'mdi-lightbulb-on', tipo: 'select' },
      { key: 'status', label: 'Estado del Mensaje', icon: 'mdi-message', tipo: 'autocomplete' },
      { key: 'estado', label: 'Gestión', icon: 'mdi-account-check', tipo: 'autocomplete' },
      { key: 'fechaInicio', label: 'Fecha desde', icon: 'mdi-calendar', tipo: 'date' },
      { key: 'fechaFin', label: 'Fecha hasta', icon: 'mdi-calendar', tipo: 'date' },
    ],
    filtrosActivos: [],
    filtrosModelos: {
      contacto: null,
      empresa: null,
      cargo: null,
      categoriaCargo: null,
      departamento: null,
      status: null,
      ciudad: null,
      sector: null,
      interes: null,
      fechaInicio: '',
      fechaFin: '',
    },
    suppressFiltrosWatch: false, // Bandera para suprimir watchers durante limpieza masiva

    // Filtros específicos para la tabla principal (columnas dinámicas)
    filtrosTablaDisponibles: [],
    filtrosTablaActivos: [],
    filtrosTablaModelos: {},
    // Componentes e items por defecto (se reutilizan de los detalles)
    filtrosTablaComponentes: {},

    mensajesAlmacenados: [],
    expandedMessages: {},
    headersVisibles: [],
    idCampaniaSeleccionada: null,

    cargandoTabla: false,
  }),

  mounted() {
    this.comercialId = localStorage.getItem("idUsuario");
    this.baseURL = import.meta.env.VITE_API_BASE_URL;
    this.idUsuario = localStorage.getItem("idUsuario");
    this.idCargo = localStorage.getItem("idCargo");
    this.nombreComercial =
      localStorage.getItem("nombreLogin") +
      " " +
      localStorage.getItem("apellidoLogin");
    this.correoUsuario = localStorage.getItem("correoUsuario");
    this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?${Date.now()}`;
    this.cargarDatos();
    this.celularComercial = localStorage.getItem('celularLogin');
    window.addEventListener("message", this.recibirMensaje);

    // Inicializar filtrosTablaDisponibles
    this._rebuildFiltrosTablaDisponibles(this.tablaHeadersPorCanal);

    window.Echo = new Echo({
      broadcaster: 'pusher',
      key: '5600c60b3437cd8c2580',
      cluster: 'us2',
      forceTLS: true
    });

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

  },

  beforeUnmount() {
    window.removeEventListener("message", this.recibirMensaje);
    if (this.webhookListener) {
      window.Echo.channel("webhooks").stopListening(
        "Webhook",
        this.webhookListener
      );
      this.webhookListener = null; // importante limpiar la referencia
    }
  },

  computed: {
    // Items (options) for table filters (autocomplete/select) derived from tablaItemsPorCanal
    filtrosTablaItems() {
      // build a map of key -> unique values from tablaItemsPorCanal
      const items = {};
      const rows = Array.isArray(this.tablaItemsPorCanal) ? this.tablaItemsPorCanal : [];
      rows.forEach(r => {
        Object.keys(r).forEach(k => {
          if (!items[k]) items[k] = new Set();
          const v = r[k];
          if (v !== null && v !== undefined) items[k].add(typeof v === 'string' ? v.trim() : v);
        });
      });
      const out = {};
      Object.entries(items).forEach(([k, set]) => {
        const arr = Array.from(set).filter(x => x !== '').sort((a, b) => {
          try { return String(a).localeCompare(String(b), 'es'); } catch (e) { return 0; }
        });
        out[k] = arr;
      });
      // Ensure canal items are objects with text/value for selects
      out.canal = this.canales.filter(c => c.value !== 0).map(c => ({ value: c.value, text: c.label }));

      // Ensure id/index items are lists of available ids for autocomplete
      const ids = (this.tablaItemsPorCanal || []).map(r => r.id).filter(v => v !== null && v !== undefined);
      out.id = Array.from(new Set(ids)).sort((a, b) => Number(a) - Number(b));
      const idxs = (this.tablaItemsPorCanal || []).map(r => r.index).filter(v => v !== null && v !== undefined);
      out.index = Array.from(new Set(idxs)).sort((a, b) => Number(a) - Number(b));
      return out;
    },

    // Lista de filtros para los cuales mostramos inputs dentro del menu
    // Excluir campos que sólo deben servir para mostrar/ocultar columnas (ciudad/sector/id/index)
    filtrosTablaVisibleInputs() {
      const excluidos = ['ciudad', 'sector', 'nombre_ciudad', 'ciudades', 'sectores', 'nombre_sector', 'id', 'index', 'total', 'efectivo_con_lead', 'efectivo_sin_lead', 'no_efectivo', 'interes_positivo', 'interes_negativo', 'sin_respuesta', 'enviadas', 'entregadas', 'no_existe', 'no_entregadas', 'con_respuesta', ''];
      return (this.filtrosTablaActivos || []).filter(f => !excluidos.includes(f));
    },

    // Filtrado en base a los inputs del menú de filtros de la tabla (incluye ciudad/sector)
    // Ciudad/Sector: Opción A - token-contains (si el valor seleccionado aparece en la lista de tokens de la fila)
    tablaItemsPorCanalFiltrada() {
      const rows = Array.isArray(this.tablaItemsPorCanal) ? this.tablaItemsPorCanal.slice() : [];
      if (!this.filtrosTablaActivos || this.filtrosTablaActivos.length === 0) return rows;

      const active = this.filtrosTablaActivos.map(k => (this.filtroToHeaderKey[k] || k));

      return rows.filter(r => {
        for (const k of active) {
          const val = this.filtrosTablaModelos[k];
          if (val === null || val === undefined || val === '' || (Array.isArray(val) && val.length === 0)) continue;

          const rowVal = r[k];
          // ID / index numeric exact match
          if (k === 'id' || k === 'index') {
            if (Array.isArray(val)) {
              const any = val.some(v => Number(r.index) === Number(v));
              if (!any) return false;
            } else {
              if (Number(r.index) !== Number(val)) return false;
            }
            continue;
          }

          // Fecha: try matching the displayed formatted fecha first (r.fecha), then fallback to ISO/raw compare
          if (['fecha', 'fecha_raw', 'fechaInicio', 'fechaFin', 'fecha_envio'].includes(k)) {
            // If the user selected the formatted label (this.formatFecha) match directly
            try {
              const valStr = (val === null || val === undefined) ? '' : String(val).trim();
              const rowFormatted = (r.fecha === null || r.fecha === undefined) ? '' : String(r.fecha).trim();
              if (valStr !== '' && rowFormatted !== '' && valStr === rowFormatted) {
                // match
                continue;
              }
            } catch (e) {
              // fallthrough to parsing below
            }

            // normalize both to yyyy-mm-dd (fallback)
            const toYmd = (d) => {
              if (!d) return null;
              const s = String(d).trim();
              // try Date parsing
              try {
                const dt = new Date(s);
                if (!isNaN(dt.getTime())) {
                  const y = dt.getFullYear();
                  const m = String(dt.getMonth() + 1).padStart(2, '0');
                  const day = String(dt.getDate()).padStart(2, '0');
                  return `${y}-${m}-${day}`;
                }
              } catch (e) { }
              // if input like dd/mm/yyyy
              const parts = s.split('/');
              if (parts.length === 3) {
                const dd = parts[0].padStart(2, '0');
                const mm = parts[1].padStart(2, '0');
                const yyyy = parts[2];
                return `${yyyy}-${mm}-${dd}`;
              }
              return s;
            };
            const needle = toYmd(val);
            const rowDate = toYmd(r.fecha_raw || r.fecha);
            if (!needle || !rowDate) return false;
            if (needle !== rowDate) return false;
            continue;
          }
          // Ciudad
          if (k === 'ciudad' || k === 'nombre_ciudad') {
            const rowCities = Array.isArray(rowVal) ? rowVal : this._splitCiudades(rowVal);
            const rowNorms = rowCities.map(c => this._norm(String(c)));
            if (Array.isArray(val)) {
              const any = val.some(v => rowNorms.some(rc => rc.includes(this._norm(String(v)))));
              if (!any) return false;
            } else {
              const needle = this._norm(String(val));
              if (!rowNorms.some(rc => rc.includes(needle))) return false;
            }
            continue;
          }

          // Sector
          if (k === 'sector' || k === 'nombre_sector') {
            const rowSectors = (rowVal || '').toString().split(',').map(s => s.trim()).filter(Boolean);
            const rowNorms = rowSectors.map(s => this._norm(String(s)));
            if (Array.isArray(val)) {
              const any = val.some(v => rowNorms.some(rs => rs.includes(this._norm(String(v)))));
              if (!any) return false;
            } else {
              const needle = this._norm(String(val));
              if (!rowNorms.some(rs => rs.includes(needle))) return false;
            }
            continue;
          }

          // Resto de campos: similar a la implementación anterior
          if (rowVal === null || rowVal === undefined) return false;
          if (typeof val === 'string') {
            const needle = this._norm(String(val));
            if (!this._norm(String(rowVal)).includes(needle)) return false;
          } else if (typeof val === 'number') {
            if (Number(rowVal) !== Number(val)) return false;
          } else if (Array.isArray(val)) {
            const rowStr = String(rowVal).toLowerCase();
            const any = val.some(v => String(rowStr).includes(String(v).toLowerCase()));
            if (!any) return false;
          } else {
            if (!String(rowVal).toLowerCase().includes(String(val).toLowerCase())) return false;
          }
        }
        return true;
      });
    },

    // Custom sort functions to ensure fecha columns sort by actual date values
    customKeySort() {
      const parseTs = (v) => this.parseFechaToTimestamp(v);
      const cmp = (a, b) => {
        const ta = parseTs(a);
        const tb = parseTs(b);
        const na = Number.isFinite(ta);
        const nb = Number.isFinite(tb);
        if (na && nb) return ta - tb; // ascending
        if (na && !nb) return 1; // valid dates after invalid
        if (!na && nb) return -1;
        // fallback to string compare
        const sa = a == null ? '' : String(a);
        const sb = b == null ? '' : String(b);
        return sa.localeCompare(sb, undefined, { numeric: true, sensitivity: 'base' });
      };
      return {
        fecha: cmp,
        fecha_raw: cmp,
        fecha_envio: cmp,
        fechaInicio: cmp,
        fechaFin: cmp
      };
    },

    // Component mapping for table filters (reuse same components as dialog)
    filtrosTablaComponentesComputed() {
      return this.filtrosComponentes; // reuse
    },

    // Visible headers for the table. If no filtrosTablaActivos => show all headers for canal.
    tablaHeadersVisiblePorCanal() {
      const base = this.tablaHeadersPorCanal || [];
      // ensure filtrosTablaDisponibles is up to date
      if (!this.filtrosTablaDisponibles || this.filtrosTablaDisponibles.length === 0) {
        this._rebuildFiltrosTablaDisponibles(base);
      }
      if (!this.filtrosTablaActivos || this.filtrosTablaActivos.length === 0) {
        return base;
      }
      // map filter keys to header keys if needed *and* keep original keys so that
      // filters like 'ciudad' or 'nombre_ciudad' correctly toggle headers that may use either key
      const mapped = this.filtrosTablaActivos.flatMap(k => {
        const mappedKey = this.filtroToHeaderKey[k] || k;
        return [mappedKey, k];
      });
      const unique = [...new Set(mapped)];
      const filtered = base.filter(h => unique.includes(h.key) || unique.includes(this.filtroToHeaderKey[h.key]));
      return filtered.length ? filtered : base;
    },
    filtrosItems() {
      return {
        canal: this.canales.map(c => ({ value: c.value, text: c.label })),
        contacto: this.contactosDisponibles,
        empresa: this.empresasDisponibles,
        cargo: this.cargosDisponibles,
        categoriaCargo: this.categoriasCargoDisponibles,
        departamento: this.departamentosDisponibles,
        status: this.statusMessagesDisponibles,
        ciudad: this.ciudadesCampanaRespuestas,
        sector: this.sectoresCampanaRespuestas,
        interes: [
          { value: null, text: 'Todos' },
          { value: 1, text: 'Interés positivo' },
          { value: 2, text: 'Interés negativo' },
          { value: 0, text: 'Sin respuesta' }
        ],
        estado: [
          { value: null, text: 'Todos' },
          { value: '1', text: 'Nuevo' },
          { value: '2', text: 'En proceso' },
          { value: '3', text: 'Resuelto' }
        ]
      };
    },
    filtrosComponentes() {
      return {
        contacto: 'v-autocomplete',
        empresa: 'v-autocomplete',
        cargo: 'v-autocomplete',
        categoriaCargo: 'v-autocomplete',
        departamento: 'v-autocomplete',
        status: 'v-autocomplete',
        ciudad: 'v-autocomplete',
        sector: 'v-autocomplete',
        canal: 'v-select',
        interes: 'v-select',
        fechaInicio: 'v-text-field',
        fechaFin: 'v-text-field',
        estado: 'v-select',
        // Campos numéricos de métricas deben usar text-field numérico
        index: 'v-autocomplete',
        id: 'v-autocomplete',
        total: 'v-text-field',
        interes_positivo: 'v-text-field',
        interes_negativo: 'v-text-field',
        enviadas: 'v-text-field',
        entregadas: 'v-text-field',
        no_existe: 'v-text-field',
        sin_respuesta: 'v-text-field',
        efectivo_con_lead: 'v-text-field',
        efectivo_sin_lead: 'v-text-field',
        no_efectivo: 'v-text-field'
      };
    },
    sectoresCampanias() {
      // Junta todos los sectores, sepáralos por coma y quita duplicados
      const set = new Set();
      this.listaCampañas.forEach((c) => {
        if (c.sectores) {
          c.sectores.split(",").forEach((sector) => {
            const clean = sector.trim();
            if (clean) set.add(clean);
          });
        }
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, "es"));
    },

    ciudadesCampanias() {
      const seen = new Map(); // clave normalizada, valor con capitalización original
      this.listaCampañas.forEach((c) => {
        this._splitCiudades(c.ciudades).forEach((city) => {
          const key = this._norm(city);
          if (!seen.has(key)) seen.set(key, city);
        });
      });
      return Array.from(seen.values()).sort((a, b) =>
        a.localeCompare(b, "es", { sensitivity: "base" })
      );
    },

    leyendaDonut() {
      // Por canal (todos)
      if (this.canalSeleccionado === 0 && this.tipoGraficoDonut === "Por Canal") {
        return [
          { label: "☎️ Telefónico", color: "#1565c0" },
          { label: "✅ WhatsApp", color: "#22C55E" },
          { label: "📧 Email", color: "#F59E0B" },
        ];
      }

      // Telefónico
      if (this.canalSeleccionado === 2) {
        return [
          { label: "✅ Efectivas c/Lead", color: "#19bf56" },
          { label: "➕ Efectivas s/Lead", color: "#3f94e8" },
          { label: "➖ No efectivas", color: "#de8d04" },
        ];
      }

      // WhatsApp, Email, Redes Sociales: leyenda dinámica según modoDonut
      if ([1, 3, 4].includes(this.canalSeleccionado)) {
        if (this.modoDonut === 'envios') {
          return [
            { label: "✅ Entregadas", color: "#19bf56" },
            { label: "🚫 No entregadas", color: "#de8d04" },
          ];
        } else {
          if (this.canalSeleccionado === 3) {
            return [
              { label: "✅ Con respuesta", color: "#3f94e8" },
              { label: "❓ Sin respuesta", color: "#454a52" },
            ];
          }
          // WhatsApp y Redes Sociales
          return [
            { label: "👍 Interés positivo", color: "#22C55E" },
            { label: "👎 Interés negativo", color: "#d95323" },
            { label: "❓ Sin respuesta", color: "#454a52" },
          ];
        }
      }

      return [];
    },

    datosDonut() {
      let campañas = this.listaCampañas;
      if (this.canalSeleccionado !== 0) {
        campañas = campañas.filter(c => c.canal === this.canalSeleccionado);
      }

      // Por Canal (todos)
      if (this.canalSeleccionado === 0 && this.tipoGraficoDonut === "Por Canal") {
        const canales = [
          { id: 2, nombre: "Telefónico", color: "#1565c0" },
          { id: 1, nombre: "WhatsApp", color: "#22C55E" },
          { id: 3, nombre: "Email", color: "#F59E0B" },
        ];
        const data = canales.map(canal =>
          campañas.filter(c => c.canal === canal.id).length
        );
        return {
          labels: canales.map(c => c.nombre),
          datasets: [
            {
              label: "Por Canal",
              data,
              backgroundColor: canales.map(c => c.color),
              borderColor: "#fff",
              borderWidth: 2,
            },
          ],
        };
      }

      // Telefónico
      if (this.canalSeleccionado === 2) {
        const efectivasConLead = campañas.reduce((sum, c) => sum + (c.efectivo_con_lead || 0), 0);
        const efectivasSinLead = campañas.reduce((sum, c) => sum + (c.efectivo_sin_lead || 0), 0);
        const noEfectivas = campañas.reduce((sum, c) => sum + (c.no_efectivo || 0), 0);
        return {
          labels: ["Efectivas c/Lead", "Efectivas s/Lead", "No efectivas"],
          datasets: [
            {
              label: "Llamadas Telefónicas",
              data: [efectivasConLead, efectivasSinLead, noEfectivas],
              backgroundColor: ["#19bf56", "#3f94e8", "#de8d04"],
              borderColor: "#fff",
              borderWidth: 2,
            },
          ],
        };
      }

      // WhatsApp, Email, Redes Sociales: modoDonut
      if ([1, 3, 4].includes(this.canalSeleccionado)) {
        if (this.modoDonut === 'envios') {
          // Entregabilidad
          let entregadas = 0, noEntregadas = 0;
          if (this.canalSeleccionado === 1 || this.canalSeleccionado === 4) {
            // WhatsApp o Redes Sociales
            entregadas = campañas.reduce((sum, c) => sum + (c.entregadas || 0), 0);
            noEntregadas = campañas.reduce((sum, c) => sum + (c.no_entregadas || 0), 0);
          } else if (this.canalSeleccionado === 3) {
            // Email
            entregadas = campañas.reduce((sum, c) => sum + (c.entregadas || 0), 0);
            noEntregadas = campañas.reduce((sum, c) => sum + (c.no_entregadas || 0), 0);
          }
          return {
            labels: ["Entregadas", "No entregadas"],
            datasets: [{
              label: "envios",
              data: [entregadas, noEntregadas],
              backgroundColor: ["#19bf56", "#de8d04"],
              borderColor: "#fff",
              borderWidth: 2,
            }],
          };
        } else {
          // Interacciones
          if (this.canalSeleccionado === 1 || this.canalSeleccionado === 4) {
            const interesPositivo = campañas.reduce((sum, c) => sum + (c.interes_positivo || 0), 0);
            const interesNegativo = campañas.reduce((sum, c) => sum + (c.interes_negativo || 0), 0);
            const sinRespuesta = campañas.reduce((sum, c) => sum + (c.sin_respuesta || 0), 0);
            return {
              labels: ["Interés positivo", "Interés negativo", "Sin respuesta"],
              datasets: [{
                label: "Interacciones",
                data: [interesPositivo, interesNegativo, sinRespuesta],
                backgroundColor: ["#22C55E", "#d95323", "#454a52"],
                borderColor: "#fff",
                borderWidth: 2,
              }],
            };
          } else if (this.canalSeleccionado === 3) {
            const conRespuesta = campañas.reduce((sum, c) => sum + (c.con_respuesta || 0), 0);
            const sinRespuesta = campañas.reduce((sum, c) => sum + (c.sin_respuesta || 0), 0);
            return {
              labels: ["Con respuesta", "Sin respuesta"],
              datasets: [{
                label: "Interacciones",
                data: [conRespuesta, sinRespuesta],
                backgroundColor: ["#3f94e8", "#454a52"],
                borderColor: "#fff",
                borderWidth: 2,
              }],
            };
          }
        }
      }

      return { labels: [], datasets: [] };
    },

    tablaRespuestas() {
      const rows = Array.isArray(this.selectedCampanaResponses)
        ? this.selectedCampanaResponses : [];

      return rows.map(r => ({
        ...r,
        id: r.id || 0,
        nombre_contacto: (r.nombre_contacto || '—').trim(),
        nombre_ciudad: (r.nombre_ciudad || '—').trim(),
        // interes: 0=sin respuesta, 1=positivo, 2=negativo (dejamos el id tal cual)
        interes: Number(r.interes ?? 0),
        // estado: 0 Nuevo, 1 en proceso, 2 Resuelto (dejamos el id)
        estado: Number(r.estado ?? 0),
      }));
    },
    distribucionDetalle() {
      const c = this.selectedCampana;
      if (!c) return [];

      // Telefónico
      if (c.canal === 2) {
        const v1 = Number(c.efectivo_con_lead ?? 0);
        const v2 = Number(c.efectivo_sin_lead ?? 0);
        const v3 = Number(c.no_efectivo ?? 0);
        const total = v1 + v2 + v3 || 1;
        return [
          { key: 'efectivo_con_lead', label: 'Efectivas c/Lead', value: v1, pct: ((v1 * 100) / total).toFixed(1), color: '#19bf56', icon: 'mdi-account-check' },
          { key: 'efectivo_sin_lead', label: 'Efectivas s/Lead', value: v2, pct: ((v2 * 100) / total).toFixed(1), color: '#3f94e8', icon: 'mdi-account-plus' },
          { key: 'no_efectivo', label: 'No efectivas', value: v3, pct: ((v3 * 100) / total).toFixed(1), color: '#de8d04', icon: 'mdi-account-cancel' },
        ];
      }
      // WhatsApp
      if (c.canal === 1) {
        const entregadas = Number((c.interes_positivo ?? 0) + (c.interes_negativo ?? 0) + (c.sin_respuesta ?? 0));
        const noEntregadas = Number(c.no_entregadas ?? 0);
        const interesPos = Number(c.interes_positivo ?? 0);
        const interesNeg = Number(c.interes_negativo ?? 0);
        const sinResp = Number(c.sin_respuesta ?? 0);
        const total = entregadas + noEntregadas || 1;
        return [
          { key: 'entregadas', label: 'Entregadas', value: entregadas, pct: ((entregadas * 100) / total).toFixed(1), color: '#1565c0', icon: 'mdi-check-circle' },
          { key: 'no_entregadas', label: 'No entregadas', value: noEntregadas, pct: ((noEntregadas * 100) / total).toFixed(1), color: '#de8d04', icon: 'mdi-cancel' },
          { key: 'interes_positivo', label: 'Interés positivo', value: interesPos, pct: ((interesPos * 100) / total).toFixed(1), color: '#22C55E', icon: 'mdi-thumb-up' },
          { key: 'interes_negativo', label: 'Interés negativo', value: interesNeg, pct: ((interesNeg * 100) / total).toFixed(1), color: '#d95323', icon: 'mdi-thumb-down' },
          { key: 'sin_respuesta', label: 'Sin respuesta', value: sinResp, pct: ((sinResp * 100) / total).toFixed(1), color: '#454a52', icon: 'mdi-help-circle-outline' },
        ];
      }
      // Email
      if (c.canal === 3) {
        const entregadas = Number(c.entregadas ?? 0);
        const noEntregadas = Number(c.no_entregadas ?? 0);
        const conRespuesta = Number(c.con_respuesta ?? 0);
        const sinResp = Number(c.sin_respuesta ?? 0);
        const total = entregadas + noEntregadas + conRespuesta + sinResp || 1;
        return [
          { key: 'entregadas', label: 'Entregadas', value: entregadas, pct: ((entregadas * 100) / total).toFixed(1), color: '#19bf56', icon: 'mdi-check-circle' },
          { key: 'no_entregadas', label: 'No entregadas', value: noEntregadas, pct: ((noEntregadas * 100) / total).toFixed(1), color: '#de8d04', icon: 'mdi-cancel' },
          { key: 'con_respuesta', label: 'Con respuesta', value: conRespuesta, pct: ((conRespuesta * 100) / total).toFixed(1), color: '#3f94e8', icon: 'mdi-email-check' },
          { key: 'sin_respuesta', label: 'Sin respuesta', value: sinResp, pct: ((sinResp * 100) / total).toFixed(1), color: '#454a52', icon: 'mdi-help-circle-outline' },
        ];
      }
      // Default (sin canal)
      const pos = Number(c.interes_positivo ?? 0);
      const neg = Number(c.interes_negativo ?? 0);
      const sin = Number(c.sin_respuesta ?? 0);
      const total = pos + neg + sin || 1;
      return [
        { key: 'pos', label: 'Interés Positivo', value: pos, pct: ((pos * 100) / total).toFixed(1), color: '#2e7d32', icon: 'mdi-lightbulb-on' },
        { key: 'neg', label: 'Interés Negativo', value: neg, pct: ((neg * 100) / total).toFixed(1), color: '#c62828', icon: 'mdi-cancel' },
        { key: 'sin', label: 'Sin Respuesta', value: sin, pct: ((sin * 100) / total).toFixed(1), color: '#1976d2', icon: 'mdi-check-all' },
      ];
    },

    barSeries() {
      const rows = Array.isArray(this.filteredMetricasCampana) ? this.filteredMetricasCampana : [];
      const counts = new Map();

      for (const r of rows) {
        // Si la fecha ya es ISO (YYYY-MM-DD), úsala directamente
        let raw = r.fecha_envio || r.fecha;
        let fechaIso = '';
        if (raw && /^\d{4}-\d{2}-\d{2}/.test(raw)) {
          fechaIso = raw.slice(0, 10);
        } else if (raw) {
          // Si es string tipo "Fri, 08 Aug 2025 11:14:18 GMT"
          const dt = new Date(raw);
          if (!isNaN(+dt)) {
            // Usa la fecha local, no UTC
            fechaIso = dt.getFullYear() + '-' +
              String(dt.getMonth() + 1).padStart(2, '0') + '-' +
              String(dt.getDate()).padStart(2, '0');
          }
        }
        if (fechaIso) {
          counts.set(fechaIso, (counts.get(fechaIso) || 0) + 1);
        }
      }

      const days = Array.from(counts.keys()).sort(); // asc
      // Formatea en español, ejemplo: "08 de ago"
      const labels = days.map(d => {
        const dateObj = new Date(d + 'T00:00:00');
        return dateObj.toLocaleDateString('es-CO', { day: '2-digit', month: 'short' });
      });
      const values = days.map(d => counts.get(d));
      return { labels, values, key: days.join('|') };
    },

    opcionesCampañas() {
      let campañas = this.listaCampañas;
      if (this.canalSeleccionado !== 0) {
        campañas = campañas.filter(c => c.canal === this.canalSeleccionado);
      }
      const set = new Set(campañas.map(c => c.nombre_campaña));
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    leyendaBarra() {
      // Solo top 10 campañas/canales/interacciones según el modo y filtro
      if (this.canalSeleccionado === 0) {
        return ['Telefónico', 'WhatsApp', 'Email'];
      }
      if (this.canalSeleccionado === 2) {
        return ['Efectivas c/Lead', 'Efectivas s/Lead', 'No efectivas'];
      }
      if (this.canalSeleccionado === 1) {
        return ['Entregadas', 'Negativo', 'No entregadas', 'Positivo', 'Sin respuesta'];
      }
      if (this.canalSeleccionado === 3) {
        return ['Con respuesta', 'Entregadas', 'No entregadas', 'Sin respuesta'];
      }
      if (this.canalSeleccionado === 4) {
        return ['Entregadas', 'Negativo', 'No entregadas', 'Positivo', 'Sin respuesta'];
      }

      let nombres = [];
      if (this.tipoGraficoBarra === 'interacciones') {
        nombres = ['Positivas', 'Negativas', 'Sin respuesta'];
      } else {
        // todas
        if (this.campañasSeleccionadas.length > 0) {
          nombres = this.campañasSeleccionadas;
        } else {
          const totales = {};
          this.listaCampañas.forEach(c => {
            totales[c.nombre_campaña] = (totales[c.nombre_campaña] || 0) + (c.interes_positivo || 0) + (c.interes_negativo || 0) + (c.sin_respuesta || 0);
          });
          nombres = Object.entries(totales)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 10)
            .map(([nombre]) => nombre);
        }
      }
      return nombres;
    },

    avisosPorCanal() {
      const campañasWhatsapp = this.listaCampañas.filter(c => c.canal === 1);
      const campañasTelefonico = this.listaCampañas.filter(c => c.canal === 2);
      const campañasEmail = this.listaCampañas.filter(c => c.canal === 3);

      // Helper para color con opacidad
      const rgba = (hex, alpha) => {
        // hex: "#RRGGBB" o "#RGB"
        let c = hex.replace('#', '');
        if (c.length === 3) c = c.split('').map(x => x + x).join('');
        const num = parseInt(c, 16);
        return `rgba(${(num >> 16) & 255}, ${(num >> 8) & 255}, ${num & 255}, ${alpha})`;
      };

      if (this.canalSeleccionado === 2) {
        return [
          {
            color: rgba("#6c4ee6", 0.85),
            emoji: "📞",
            label: "Total llamadas",
            value: campañasTelefonico.length,
          },
          {
            color: rgba("#19bf56", 0.85),
            emoji: "✅",
            label: "Efectivas c/Lead",
            value: campañasTelefonico.reduce((sum, c) => sum + (c.efectivo_con_lead || 0), 0),
          },
          {
            color: rgba("#3f94e8", 0.85),
            emoji: "➕",
            label: "Efectivas s/Lead",
            value: campañasTelefonico.reduce((sum, c) => sum + (c.efectivo_sin_lead || 0), 0),
          },
          {
            color: rgba("#de8d04", 0.85),
            emoji: "➖",
            label: "No efectivas",
            value: campañasTelefonico.reduce((sum, c) => sum + (c.no_efectivo || 0), 0),
          },
        ];
      } else if (this.canalSeleccionado === 1) {
        return [
          {
            color: rgba("#19bf56", 0.85),
            emoji: "📣",
            label: "Campañas totales",
            value: campañasWhatsapp.length,
          },
          {
            color: rgba("#19bf56", 0.85),
            emoji: "📨",
            label: "Mensajes totales",
            value: campañasWhatsapp.reduce((sum, c) => sum + (c.enviadas + c.entregadas + c.fallidas + c.leidas || 0), 0),
          },
          {
            color: rgba("#1565c0", 0.85),
            emoji: "✅",
            label: "Mensajes Entregados",
            value: campañasWhatsapp.reduce((sum, c) => sum + (c.entregadas || 0) + (c.leidas || 0), 0),
          },
          {
            color: rgba("#3890f5", 0.85),
            emoji: "❎",
            label: "Mensajes No Entregadas",
            value: campañasWhatsapp.reduce((sum, c) => sum + (c.enviadas || 0), 0),
          },
          {
            color: rgba("#de8d04", 0.85),
            emoji: "🚫",
            label: "Mensajes No Existentes",
            value: campañasWhatsapp.reduce((sum, c) => sum + (c.fallidas || 0), 0),
          },
          {
            color: rgba("#19bf56", 0.85),
            emoji: "👍",
            label: "Mensajes Con Interés positivo",
            value: campañasWhatsapp.reduce((sum, c) => sum + (c.interes_positivo || 0), 0),
          },
          {
            color: rgba("#c93904", 0.85),
            emoji: "👎",
            label: "Mensajes Con Interés negativo",
            value: campañasWhatsapp.reduce((sum, c) => sum + (c.interes_negativo || 0), 0),
          },
          {
            color: rgba("#454a52", 0.85),
            emoji: "❓",
            label: "Mensajes Sin Respuesta",
            value: campañasWhatsapp.reduce((sum, c) => sum + (c.sin_respuesta || 0), 0),
          },
        ];
      } else if (this.canalSeleccionado === 3) {
        return [
          {
            color: rgba("#de8d04", 0.78),
            emoji: "📣",
            label: "Campañas totales",
            value: campañasEmail.length,
          },
          {
            color: rgba("#1565c0", 0.78),
            emoji: "📨",
            label: "Entregadas",
            value: 0,
          },
          {
            color: rgba("#6c4ee6", 0.78),
            emoji: "🚫",
            label: "No entregadas",
            value: 0,
          },
          {
            color: rgba("#19bf56", 0.78),
            emoji: "✅",
            label: "Con respuesta",
            value: 0,
          },
          {
            color: rgba("#454a52", 0.78),
            emoji: "❓",
            label: "Sin respuesta",
            value: 0,
          },
        ];
      } else {
        // TODOS LOS CANALES
        return [
          {
            color: rgba("#1565c0", 0.78),
            emoji: "📊",
            label: "Campañas Totales",
            value: this.listaCampañas.length,
          },
          {
            color: rgba("#6c4ee6", 0.78),
            emoji: "📞",
            label: "Telefónico",
            value: campañasTelefonico.length,
          },
          {
            color: rgba("#19bf56", 0.78),
            emoji: "💬",
            label: "WhatsApp",
            value: campañasWhatsapp.length,
          },
          {
            color: rgba("#e39005", 0.78),
            emoji: "✉️",
            label: "Email",
            value: campañasEmail.length,
          },
        ];
      }
    },

    textoDistribucionDonut() {
      if (this.canalSeleccionado === 0) {
        return "Distribución Por todos los Canales";
      } else if (this.canalSeleccionado === 2) {
        return "Distribución Por Tipo de Llamada";
      } else if (this.canalSeleccionado === 1) {
        return "Distribución Por WhatsApp";
      } else if (this.canalSeleccionado === 3) {
        return "Distribución Por Email";
      }
      return "Distribución";
    },

    tablaHeadersPorCanal() {
      // Comunes a todos
      const comunes = [
        { title: "ID", key: "index", align: "center", width: 40 },
        { title: "Nombre de campaña", key: "nombre_campaña", align: "start" },
        { title: "Fecha", key: "fecha", align: "center" },
        { title: "Canal", key: "canal", align: "center" },
        { title: "Ciudad", key: "ciudad", align: "center" },
        { title: "Sector", key: "sector", align: "center" },
      ];

      if (this.canalSeleccionado === 2) {
        return [
          ...comunes,
          { title: "Efectivas c/Lead", key: "efectivo_con_lead", align: "center" },
          { title: "Efectivas s/Lead", key: "efectivo_sin_lead", align: "center" },
          { title: "No efectivas", key: "no_efectivo", align: "center" },
          { title: "Total (n / %)", key: "total", align: "center" },
        ];
      } else if (this.canalSeleccionado === 1) {
        return [
          ...comunes,
          { title: "Positivo", key: "interes_positivo", align: "center" },
          { title: "Negativo", key: "interes_negativo", align: "center" },
          { title: "Enviadas", key: "enviadas", align: "center" },
          { title: "Entregadas", key: "entregadas", align: "center" },
          { title: "No existe", key: "no_existe", align: "center" },
          { title: "Sin respuesta", key: "sin_respuesta", align: "center" },
          { title: "Total (n / %)", key: "total", align: "center" },
        ];
      } else if (this.canalSeleccionado === 3) {
        return [
          ...comunes,
          { title: "Entregadas", key: "entregadas", align: "center" },
          { title: "No entregadas", key: "no_entregadas", align: "center" },
          { title: "Con respuesta", key: "con_respuesta", align: "center" },
          { title: "Sin respuesta", key: "sin_respuesta", align: "center" },
          { title: "Total (n / %)", key: "total", align: "center" },
        ];
      } else if (this.canalSeleccionado === 4) {
        return [
          ...comunes,
          { title: "Positivo", key: "interes_positivo", align: "center" },
          { title: "Negativo", key: "interes_negativo", align: "center" },
          { title: "Entregadas", key: "entregadas", align: "center" },
          { title: "No entregadas", key: "no_entregadas", align: "center" },
          { title: "Sin respuesta", key: "sin_respuesta", align: "center" },
          { title: "Total (n / %)", key: "total", align: "center" },
        ];
      } else {
        // Canal "todos"
        return [
          ...comunes,
          { title: "Total (n / %)", key: "total", align: "center" },
        ];
      }
    },

    barChartTieneDatos() {
      if (!this.datosCargados) return true;
      let chartData;
      if (this.canalSeleccionado === 0) {
        chartData = this.prepararDatosLineChartPorCanal();
      } else if (this.canalSeleccionado === 2) {
        chartData = this.prepararDatosLineChartTelefonico();
      } else if (this.canalSeleccionado === 1) {
        chartData = this.prepararDatosLineChartWhatsApp();
      } else if (this.canalSeleccionado === 3) {
        chartData = this.prepararDatosLineChartEmail();
      }
      if (!chartData || !chartData.datasets) return false;
      return chartData.datasets.some(ds => Array.isArray(ds.data) && ds.data.some(val => val > 0));
    },

    tablaItemsPorCanal() {
      // Mapea y adapta los datos según el canal
      return this.listaCampañas.map(c => {
        const base = {
          id: c.id,
          index: c.id,
          nombre_campaña: c.nombre_campaña,
          fecha_raw: c.fecha, // ISO/raw for filtering
          fecha: this.formatFecha(c.fecha),
          canal: c.canal,
          ciudad: c.ciudades || c.ciudad,
          sector: c.sectores || c.sector,
        };

        if (this.canalSeleccionado === 2) {
          const total = (c.efectivo_con_lead || 0) + (c.efectivo_sin_lead || 0) + (c.no_efectivo || 0);
          return {
            ...base,
            efectivo_con_lead: c.efectivo_con_lead || 0,
            efectivo_sin_lead: c.efectivo_sin_lead || 0,
            no_efectivo: c.no_efectivo || 0,
            total: `${total} (${total ? Math.round((total / (c.total_llamadas || total)) * 100) : 0}%)`,
          };
        } else if (this.canalSeleccionado === 1) {
          const total = (c.interes_positivo || 0) + (c.interes_negativo || 0) + (c.sin_respuesta || 0);
          return {
            ...base,
            interes_positivo: c.interes_positivo || 0,
            interes_negativo: c.interes_negativo || 0,
            entregadas: c.entregadas + c.leidas || 0,
            enviadas: c.enviadas || 0,
            no_existe: c.fallidas || 0,
            sin_respuesta: c.sin_respuesta || 0,
            total: `${total} (${total ? Math.round((total / (c.entregadas || total)) * 100) : 0}%)`,
          };
        } else if (this.canalSeleccionado === 3) {
          const total = (c.entregadas || 0) + (c.no_entregadas || 0) + (c.con_respuesta || 0) + (c.sin_respuesta || 0);
          return {
            ...base,
            entregadas: c.entregadas || 0,
            no_entregadas: c.no_entregadas || 0,
            con_respuesta: c.con_respuesta || 0,
            sin_respuesta: c.sin_respuesta || 0,
            total: `${total} (${total ? Math.round((total / (c.entregadas || total)) * 100) : 0}%)`,
          };
        } else if (this.canalSeleccionado === 4) {
          const total = (c.interes_positivo || 0) + (c.interes_negativo || 0) + (c.sin_respuesta || 0);
          return {
            ...base,
            interes_positivo: c.interes_positivo || 0,
            interes_negativo: c.interes_negativo || 0,
            entregadas: c.entregadas || 0,
            no_entregadas: c.no_entregadas || 0,
            sin_respuesta: c.sin_respuesta || 0,
            total: `${total} (${total ? Math.round((total / (c.entregadas || total)) * 100) : 0}%)`,
          };
        } else {
          // Canal "todos"
          const total = (c.interes_positivo || 0) + (c.interes_negativo || 0) + (c.sin_respuesta || 0);
          return {
            ...base,
            total: `${total} (${total ? Math.round((total / (c.envios || total)) * 100) : 0}%)`,
          };
        }
      });
    },

    sectoresCampanaRespuestas() {
      // Devuelve solo los sectores presentes en las respuestas
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_sector) set.add(r.nombre_sector.trim());
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    sectoresDisponibles() {
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_sector) {
          const val = r.nombre_sector.trim();
          if (val) set.add(val);
        }
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    empresasDisponibles() {
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_empresa) {
          const val = r.nombre_empresa.trim();
          if (val) set.add(val);
        }
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    cargosDisponibles() {
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_cargo) {
          const val = r.nombre_cargo.trim();
          if (val) set.add(val);
        }
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    categoriasCargoDisponibles() {
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_cat_cargo) {
          const val = r.nombre_cat_cargo.trim();
          if (val) set.add(val);
        }
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    departamentosDisponibles() {
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_departamento) {
          const val = r.nombre_departamento.trim();
          if (val) set.add(val);
        }
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    statusMessagesDisponibles() {
      const map = {
        sent: 'Enviado',
        delivered: 'Entregado',
        read: 'Leído',
        failed: 'Fallido'
      };
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.status_mensaje) {
          const val = r.status_mensaje;
          set.add(val);
        }
      });
      return Array.from(set).map(val => ({
        value: val,
        text: map[val] || val
      }));
    },

    contactosDisponibles() {
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_contacto) {
          const val = r.nombre_contacto.trim();
          if (val) set.add(val);
        }
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    ciudadesCampanaRespuestas() {
      // Devuelve solo las ciudades presentes en las respuestas
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_ciudad) set.add(r.nombre_ciudad.trim());
      });
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
    },

    filteredMetricasCampana() {
      let arr = Array.isArray(this.selectedCampanaResponses) ? this.selectedCampanaResponses : [];

      // Filtra por ciudad
      if (this.filtroCiudadMetricas) {
        arr = arr.filter(r => (r.nombre_ciudad || '').toLowerCase().includes(this.filtroCiudadMetricas.toLowerCase()));
      }
      // Filtro por Entregadas
      if (this.filtroEntregadasMetricas) {
        arr = arr.filter(r => {
          const status = (r.status_mensaje || '').toLowerCase();
          if (this.filtroEntregadasMetricas === 'entregada') {
            return status === 'read' || status === 'delivered';
          }
          if (this.filtroEntregadasMetricas === 'no_entregada') {
            return status === 'failed' || status === 'rejected' || status === 'sent';
          }
          return true;
        });
      }
      // Filtro por Contacto
      if (this.filtroContactoMetricas) {
        arr = arr.filter(r => (r.nombre_contacto || '').toLowerCase().includes(this.filtroContactoMetricas.toLowerCase()));
      }
      // Filtro por Empresa
      if (this.filtroEmpresaMetricas) {
        arr = arr.filter(r => (r.nombre_empresa || '').toLowerCase().includes(this.filtroEmpresaMetricas.toLowerCase()));
      }
      // Filtro por Cargo
      if (this.filtroCargoMetricas) {
        arr = arr.filter(r => (r.nombre_cargo || '').toLowerCase().includes(this.filtroCargoMetricas.toLowerCase()));
      }
      // Filtro por Categoria Cargo
      if (this.filtroCategoriaCargoMetricas) {
        arr = arr.filter(r => (r.nombre_cat_cargo || '').toLowerCase().includes(this.filtroCategoriaCargoMetricas.toLowerCase()));
      }
      // Filtro por Departamento
      if (this.filtroDepartamentoMetricas) {
        arr = arr.filter(r => (r.nombre_departamento || '').toLowerCase().includes(this.filtroDepartamentoMetricas.toLowerCase()));
      }
      // Filtra por estado
      if (this.filtroEstadoMetricas) {
        arr = arr.filter(r => String(r.estado) === String(this.filtroEstadoMetricas));
      }
      // Filtro por Status Message
      if (this.filtroStatusMessageMetricas) {
        arr = arr.filter(r => (r.status_mensaje || '').toLowerCase() === this.filtroStatusMessageMetricas.toLowerCase());
      }
      // Filtra por sector
      if (this.filtroSectorMetricas) {
        arr = arr.filter(r => (r.nombre_sector || '').toLowerCase().includes(this.filtroSectorMetricas.toLowerCase()));
      }
      // Filtra por interés
      if (this.filtroInteresMetricas !== null && this.filtroInteresMetricas !== undefined) {
        arr = arr.filter(r => Number(r.interes) === Number(this.filtroInteresMetricas));
      }
      // Filtra por fecha
      if (this.filtroFechaInicioMetricas) {
        arr = arr.filter(r => {
          const raw = r.fecha_envio || r.fecha;
          let fechaIso = '';
          if (raw && /^\d{4}-\d{2}-\d{2}/.test(raw)) {
            fechaIso = raw.slice(0, 10);
          } else if (raw) {
            const dt = new Date(raw);
            if (!isNaN(+dt)) {
              fechaIso = dt.getFullYear() + '-' +
                String(dt.getMonth() + 1).padStart(2, '0') + '-' +
                String(dt.getDate()).padStart(2, '0');
            }
          }
          return fechaIso && fechaIso >= this.filtroFechaInicioMetricas;
        });
      }
      if (this.filtroFechaFinMetricas) {
        arr = arr.filter(r => {
          const raw = r.fecha_envio || r.fecha;
          let fechaIso = '';
          if (raw && /^\d{4}-\d{2}-\d{2}/.test(raw)) {
            fechaIso = raw.slice(0, 10);
          } else if (raw) {
            const dt = new Date(raw);
            if (!isNaN(+dt)) {
              fechaIso = dt.getFullYear() + '-' +
                String(dt.getMonth() + 1).padStart(2, '0') + '-' +
                String(dt.getDate()).padStart(2, '0');
            }
          }
          return fechaIso && fechaIso <= this.filtroFechaFinMetricas;
        });
      }
      return arr;
    },

    tablaRespuestasFiltrada() {
      let arr = this.filteredMetricasCampana;

      // Filtro de búsqueda por contacto, ciudad, sector, interes (label), status mensaje (label) y estado (label)
      if (this.searchProsp && this.searchProsp.trim()) {
        const norm = this._norm(this.searchProsp);
        arr = arr.filter(r =>
          this._norm(r.nombre_contacto).includes(norm) ||
          this._norm(r.nombre_empresa).includes(norm) ||
          this._norm(r.nombre_cargo).includes(norm) ||
          this._norm(r.nombre_cat_cargo).includes(norm) ||
          this._norm(r.nombre_departamento).includes(norm) ||
          this._norm(r.nombre_ciudad).includes(norm) ||
          this._norm(r.nombre_sector).includes(norm) ||
          this._norm(this.interesLabel(r.interes)).includes(norm) ||
          this._norm(this.estadoLabel(r.estado)).includes(norm) ||
          this._norm(this.statusLabel(r.status_mensaje)).includes(norm)
        );
      }

      // Mapea para asegurar formato de columnas
      return arr.map(r => ({
        ...r,
        id: r.id || 0,
        nombre_contacto: (r.nombre_contacto || '—').trim(),
        nombre_ciudad: (r.nombre_ciudad || '—').trim(),
        nombre_sector: (r.nombre_sector || '—').trim(),
        interes: Number(r.interes ?? 0),
        estado: Number(r.estado ?? 0),
        status_mensaje: (r.status_mensaje || '—').trim(),
      }));
    },

    tieneCasoResuelto() {
      return this.historialCampania.some(h => Number(h.estado) === 3);
    },

  },
  watch: {

    filtrosActivos: {
      handler(nuevosFiltros) {
        if (!nuevosFiltros || nuevosFiltros.length === 0) {
          this.headersVisibles = this.tablaHeaders.slice();
        } else {
          // Mapear keys de filtros a keys de headers reales
          const keysParaColumnas = nuevosFiltros.map(k =>
            (k === 'fechaInicio' || k === 'fechaFin')
              ? 'fecha_envio'
              : (this.filtroToHeaderKey[k] || k)
          );
          const uniqueKeys = [...new Set(keysParaColumnas)];
          const filtrados = this.tablaHeaders.filter(h => uniqueKeys.includes(h.key));
          this.headersVisibles = filtrados.length > 0 ? filtrados : this.tablaHeaders.slice();
        }
      },
      immediate: true
    },

    historialCampania() {
      this.$nextTick(() => {
        let el = this.$refs.historialSheet;
        // Si el v-sheet tiene un solo hijo con overflow, usa ese
        if (el && el.$el) el = el.$el;
        // Busca el div con scroll si existe
        if (el && el.querySelector) {
          const scrollable = el.querySelector('.overflow-y-auto') || el;
          scrollable.scrollTo({
            top: scrollable.scrollHeight,
            behavior: 'smooth'
          });
        }
      });
    },

    'filtrosModelos.contacto'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroContactoMetricas = val;
    },
    'filtrosModelos.empresa'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroEmpresaMetricas = val;
    },
    'filtrosModelos.cargo'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroCargoMetricas = val;
    },
    'filtrosModelos.categoriaCargo'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroCategoriaCargoMetricas = val;
    },
    'filtrosModelos.departamento'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroDepartamentoMetricas = val;
    },
    'filtrosModelos.status'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroStatusMessageMetricas = val;
    },
    'filtrosModelos.ciudad'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroCiudadMetricas = val;
    },
    'filtrosModelos.sector'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroSectorMetricas = val;
    },
    'filtrosModelos.interes'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroInteresMetricas = val;
    },
    'filtrosModelos.fechaInicio'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroFechaInicioMetricas = val;
    },
    'filtrosModelos.fechaFin'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroFechaFinMetricas = val;
    },
    'filtrosModelos.estado'(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtroEstadoMetricas = val;
    },

    // Mapear modelos de filtros de la tabla hacia las variables de filtro existentes
    // Además forzamos la aplicación de filtros y la actualización de gráficos
    'filtrosTablaModelos.contacto'(val) {
      this.filtroContactoMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.empresa'(val) {
      this.filtroEmpresaMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.cargo'(val) {
      this.filtroCargoMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.categoriaCargo'(val) {
      this.filtroCategoriaCargoMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.departamento'(val) {
      this.filtroDepartamentoMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.status'(val) {
      this.filtroStatusMessageMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.interes'(val) {
      this.filtroInteresMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.fechaInicio'(val) {
      this.filtroFechaInicioMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.fechaFin'(val) {
      this.filtroFechaFinMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.ciudad'(val) {
      this.filtroCiudadMetricas = val;
      this.debouncedAplicarFiltros();
    },
    'filtrosTablaModelos.sector'(val) {
      this.filtroSectorMetricas = val;
      this.debouncedAplicarFiltros();
    },

    // Variables originales → modelos (bidireccional)
    filtroContactoMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.contacto = val;
    },
    filtroEmpresaMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.empresa = val;
    },
    filtroCargoMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.cargo = val;
    },
    filtroCategoriaCargoMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.categoriaCargo = val;
    },
    filtroDepartamentoMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.departamento = val;
    },
    filtroStatusMessageMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.status = val;
    },
    filtroCiudadMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.ciudad = val;
    },
    filtroSectorMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.sector = val;
    },
    filtroInteresMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.interes = val;
    },
    filtroFechaInicioMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.fechaInicio = val;
    },
    filtroFechaFinMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.fechaFin = val;
    },
    filtroEstadoMetricas(val) {
      if (this.suppressFiltrosWatch) return;
      this.filtrosModelos.estado = val;
    },

    tipoGraficoDonut() {
      this.iniciarChartDonut();
      this.renderBarChartCanvas();
    },

    selectedCampana() {

      this.$nextTick(() => {
        this.renderDistribucion();
        this.renderBar();
      });
    },

    beforeUnmount() {
      this.destroyDonut();
      this.destroyBar();
    },

    dialogMetricasCampana(val) {
      if (val) {
        this.readOnlyCloseButton = true;
        this.chartsPending = 2; // bar + donut
        this.$nextTick(() => {
          setTimeout(() => {
            this.renderBar();
            this.renderDistribucion();
          }, 500); // Espera 1.5 segundos antes de renderizar la barra
        });
      } else {
        this.destroyDonut();
        this.destroyBar();
        this.chartsPending = 0;
      }
    },

    tipoGraficoBarra(val) {
      // Si cambia el tipo de gráfico, limpia selección y renderiza
      if (val === 'canales') this.campañasSeleccionadas = [];
      this.renderBarChartCanvas();
    },

    campañasSeleccionadas() {
      this.renderBarChartCanvas();
    },

    canalSeleccionado() {
      this.canalesDeshabilitados = true;
      this.aplicarFiltros();
      // rebuild available column filters because headers change per canal
      this._rebuildFiltrosTablaDisponibles(this.tablaHeadersPorCanal);
      setTimeout(() => {
        this.canalesDeshabilitados = false;
      }, 1500);
    },

    // Rebuild available table column filters when headers per canal change
    tablaHeadersPorCanal() {
      this._rebuildFiltrosTablaDisponibles(this.tablaHeadersPorCanal);
    },

    modoDonut() {
      this.iniciarChartDonut();
    },

    modoDonutDetalle() {
      if (this.dialogMetricasCampana) {
        this.renderDistribucion();
        setTimeout(() => {
          this.readOnlyCloseButton = false;
        }, 1300);
      }
    },

    filtroContactoMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroEmpresaMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroCargoMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroCategoriaCargoMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroDepartamentoMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroStatusMessageMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroCiudadMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroEntregadasMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroSectorMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroInteresMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroFechaInicioMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroFechaFinMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },
    filtroEstadoMetricas() {
      if (this.suppressFiltrosWatch) return;
      this.redibujarBarCanvas();
    },

  },
  methods: {

    // Debounce helper para aplicar filtros y evitar redraws intensivos
    debouncedAplicarFiltros() {
      if (!this._aplicarFiltrosTimeout) this._aplicarFiltrosTimeout = null;
      if (this._aplicarFiltrosTimeout) clearTimeout(this._aplicarFiltrosTimeout);
      this._aplicarFiltrosTimeout = setTimeout(() => {
        this.aplicarFiltros();
        this._aplicarFiltrosTimeout = null;
      }, 300);
    },

    // Parse a variety of date formats used in the table to a timestamp (ms)
    parseFechaToTimestamp(v) {
      if (v === null || v === undefined || v === '') return NaN;
      // if already a number
      if (typeof v === 'number' && isFinite(v)) return v;
      // Date object
      if (Object.prototype.toString.call(v) === '[object Date]') {
        const t = v.getTime();
        return isNaN(t) ? NaN : t;
      }
      const s = String(v).trim();
      if (!s) return NaN;

      // Try native Date parsing first (handles RFC strings like "Fri, 17 Oct 2025 17:08:40 GMT")
      try {
        const dt = new Date(s);
        if (!isNaN(dt.getTime())) return dt.getTime();
      } catch (e) {}

      // Spanish formatted: "01 de noviembre de 2025" or "1 de noviembre de 2025"
      const months = {
        enero: 0, febrero: 1, marzo: 2, abril: 3, mayo: 4, junio: 5,
        julio: 6, agosto: 7, septiembre: 8, octubre: 9, noviembre: 10, diciembre: 11
      };
      const espMatch = s.toLowerCase().match(/^(\d{1,2})\s+de\s+([a-záéíóúñ]+)\s+de\s+(\d{4})$/i);
      if (espMatch) {
        const day = parseInt(espMatch[1], 10);
        const mname = espMatch[2].toLowerCase();
        const year = parseInt(espMatch[3], 10);
        if (mname in months) {
          const dt = new Date(year, months[mname], day);
          if (!isNaN(dt.getTime())) return dt.getTime();
        }
      }

      // dd/mm/yyyy
      const parts = s.split('/');
      if (parts.length === 3) {
        const dd = parseInt(parts[0], 10);
        const mm = parseInt(parts[1], 10) - 1;
        const yyyy = parseInt(parts[2], 10);
        const dt = new Date(yyyy, mm, dd);
        if (!isNaN(dt.getTime())) return dt.getTime();
      }

      // ISO-ish yyyy-mm-dd
      const isoMatch = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/);
      if (isoMatch) {
        const yyyy = parseInt(isoMatch[1], 10);
        const mm = parseInt(isoMatch[2], 10) - 1;
        const dd = parseInt(isoMatch[3], 10);
        const dt = new Date(yyyy, mm, dd);
        if (!isNaN(dt.getTime())) return dt.getTime();
      }

      // Last resort: try Date.parse
      const parsed = Date.parse(s);
      return isNaN(parsed) ? NaN : parsed;
    },

    // Props to bind to each filter input depending on type
    filtrosTablaInputProps(filtroKey) {
      // Do NOT force date inputs here — keep fecha as autocomplete as per user's request
      // Campos numéricos: renderizar como campo numérico
      const numericFields = ['total', 'interes_positivo', 'interes_negativo', 'enviadas', 'entregadas', 'no_existe', 'sin_respuesta', 'efectivo_con_lead', 'efectivo_sin_lead', 'no_efectivo'];
      // incluir variantes id/index
      numericFields.push('index', 'id');
      if (numericFields.includes(filtroKey)) {
        return { type: 'number' };
      }
      // If the available items are simple strings, use item-title/item-value for selects
      const items = this.filtrosTablaItems[filtroKey];
      // For canal ensure item-title/value are set
      if (filtroKey === 'canal') return { 'item-title': 'text', 'item-value': 'value' };
      if (Array.isArray(items) && items.length > 0 && typeof items[0] === 'object') {
        return { 'item-title': 'text', 'item-value': 'value' };
      }
      return {};
    },

    _rebuildFiltrosTablaDisponibles(baseHeaders) {
      // Build filtrosTablaDisponibles from the current headers for canal
      const arr = (baseHeaders || this.tablaHeadersPorCanal || []).map(h => ({ key: h.key, label: h.title, icon: 'mdi-table-column' }));
      this.filtrosTablaDisponibles = arr;
      // init component map and modelos defaults
      const compMap = {};
      const modelos = {};
      arr.forEach(a => {
        // choose component: if header key exists in filtrosComponentes use that, else autocomplete
        compMap[a.key] = (this.filtrosComponentes && this.filtrosComponentes[a.key]) ? this.filtrosComponentes[a.key] : 'v-autocomplete';
        modelos[a.key] = null;
        // also add reverse-mapped key if exists (e.g., 'contacto' -> 'nombre_contacto') so we can watch both
        const reverseKey = Object.keys(this.filtroToHeaderKey).find(k => this.filtroToHeaderKey[k] === a.key);
        if (reverseKey) {
          modelos[reverseKey] = null;
          compMap[reverseKey] = compMap[a.key];
        }
      });
      // Ensure numeric id/index models exist
      modelos['index'] = null;
      modelos['id'] = null;
      if (!compMap['index']) compMap['index'] = 'v-text-field';
      if (!compMap['id']) compMap['id'] = 'v-text-field';
      this.filtrosTablaComponentes = compMap;
      this.filtrosTablaModelos = modelos;
      // reset active filters to avoid stale keys
      this.filtrosTablaActivos = [];
    },

    limpiarFiltrosTabla() {
      this.filtrosTablaActivos = [];
      // reset modelos sin usar $set (compatibilidad Vue 3)
      Object.keys(this.filtrosTablaModelos).forEach(k => { this.filtrosTablaModelos[k] = null; });
      // reset headers visibles
      this.headersVisibles = this.tablaHeaders.slice();
      // aplicar filtros vacíos
      this.aplicarFiltros();
    },

    parseWhatsApp(respuesta) {
      try {
        return typeof respuesta === 'string' ? JSON.parse(respuesta) : respuesta;
      } catch (e) {
        return null;
      }
    },
    removeHeader(text) {
      return text.replace(/^\*[^*]+\*\s*/m, '');
    },
    truncateText(text, maxLength = 180) {
      if (!text || text.length <= maxLength) return text;
      // Corta solo hasta el último espacio antes del límite
      const truncated = text.slice(0, maxLength);
      const lastSpace = truncated.lastIndexOf(' ');
      return truncated.slice(0, lastSpace > 0 ? lastSpace : maxLength) + '...';
    },
    shouldShowExpand(text, maxLength = 180) {
      return text && text.length > maxLength;
    },
    // Extraer nombre de archivo de una URL
    getFileName(url) {
      if (!url) return '';
      try {
        return decodeURIComponent(url.split('/').pop().split('?')[0]);
      } catch (e) {
        return url;
      }
    },

    exportarPDF() {
      const elemento = document.getElementById('contenido-exportar');
      if (!elemento) return;

      // Buscar el nodo principal de scroll (v-main__wrap o v-main)
      let scrollNode = null;
      let temp = elemento;
      while (temp && temp !== document.body) {
        if (temp.classList && (temp.classList.contains('v-main__wrap') || temp.classList.contains('v-main'))) {
          scrollNode = temp;
          break;
        }
        temp = temp.parentElement;
      }
      // Si no se encuentra, usar el primer ancestro con overflowY distinto de visible
      if (!scrollNode) {
        temp = elemento;
        while (temp && temp !== document.body) {
          const style = window.getComputedStyle(temp);
          if (style.overflowY && style.overflowY !== 'visible') {
            scrollNode = temp;
            break;
          }
          temp = temp.parentElement;
        }
      }

      // Guardar estilos originales de este y sus padres
      const originalStyles = [];
      let node = elemento;
      while (node && node !== document.body) {
        originalStyles.push({
          node,
          height: node.style.height,
          overflow: node.style.overflow,
          overflowY: node.style.overflowY,
        });
        node.style.height = 'auto';
        node.style.overflow = 'visible';
        node.style.overflowY = 'visible';
        node = node.parentElement;
      }
      // También guardar y modificar el scrollNode si existe y no es ya parte de la lista
      if (scrollNode && !originalStyles.some(s => s.node === scrollNode)) {
        originalStyles.push({
          node: scrollNode,
          height: scrollNode.style.height,
          overflow: scrollNode.style.overflow,
          overflowY: scrollNode.style.overflowY,
        });
        scrollNode.style.height = 'auto';
        scrollNode.style.overflow = 'visible';
        scrollNode.style.overflowY = 'visible';
      }

      this.$nextTick(() => {
        html2canvas(elemento, { scale: 2, useCORS: true })
          .then((canvas) => {
            const imgData = canvas.toDataURL('image/png');
            const pdf = new jsPDF('p', 'mm', 'a4');
            const pageWidth = pdf.internal.pageSize.getWidth();
            const pageHeight = pdf.internal.pageSize.getHeight();

            const imgWidth = pageWidth;
            const imgHeight = (canvas.height * imgWidth) / canvas.width;

            let position = 0;
            let heightLeft = imgHeight;

            while (heightLeft > 0) {
              pdf.addImage(imgData, 'PNG', 0, position, imgWidth, imgHeight);
              heightLeft -= pageHeight;
              if (heightLeft > 0) {
                pdf.addPage();
                position = 0;
              }
            }

            pdf.save(`Campañas_${new Date().toISOString().slice(0, 10)}.pdf`);
          })
          .finally(() => {
            // Restaurar estilos originales siempre, incluso si hay error
            for (const { node, height, overflow, overflowY } of originalStyles) {
              node.style.height = height;
              node.style.overflow = overflow;
              node.style.overflowY = overflowY;
            }
            // Forzar reflow para asegurar que el scroll reaparezca
            setTimeout(() => {
              if (scrollNode) {
                // Si el scrollNode tiene scroll, forzar scrollTop
                if (scrollNode.scrollHeight > scrollNode.clientHeight) {
                  scrollNode.scrollTop = 0;
                }
              }
            }, 50);
          });
      });
    },

    canalNombre(id) {
      switch (id) {
        case 1: return 'WhatsApp';
        case 2: return 'Telefónico';
        case 3: return 'Email';
        default: return 'Desconocido';
      }
    },

    exportarExcel() {
      // 1️⃣ Mapeamos los datos visibles
      const datos = this.tablaItemsPorCanal.map((item) => {
        const fila = {};
        this.tablaHeadersPorCanal.forEach((h) => {
          if (h.key === 'canal') {
            fila[h.title] = this.canalNombre(item[h.key]);
          } else {
            fila[h.title] = item[h.key];
          }
        });
        return fila;
      });

      const hoja = XLSX.utils.json_to_sheet(datos);

      const libro = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(libro, hoja, "Campañas");

      const excelBuffer = XLSX.write(libro, { bookType: "xlsx", type: "array" });

      const blob = new Blob([excelBuffer], { type: "application/octet-stream" });
      saveAs(blob, `Campañas_${new Date().toISOString().slice(0, 10)}.xlsx`);
    },

    cargarDatos() {

      axios
        .post(this.baseURL + "/api/informesCampanias", {
          idUsuario: this.idUsuario,
        })
        .then((response) => {
          this.listaCampañas = response.data.data;
          this.arregloOriginal = [...this.listaCampañas];
          console.log("Datos cargados:", this.listaCampañas);

          // Reinicia totales antes de sumar
          this.totalCampanasEnviadas = 0;
          this.totalInteresPositivo = 0;
          this.totalInteresNegativo = 0;
          this.totalSinRespuesta = 0;
          this.totalxCampaña = [];

          this.listaCampañas.forEach((campaña) => {
            this.totalCampanasEnviadas += campaña.interes_positivo || 0;
            this.totalCampanasEnviadas += campaña.interes_negativo || 0;
            this.totalCampanasEnviadas += campaña.sin_respuesta || 0;

            this.totalInteresPositivo += campaña.interes_positivo || 0;
            this.totalInteresNegativo += campaña.interes_negativo || 0;
            this.totalSinRespuesta += campaña.sin_respuesta || 0;

            this.totalxCampaña.push({
              id: campaña.id,
              nombre: campaña.nombre_campaña,
              total:
                (campaña.interes_positivo || 0) +
                (campaña.interes_negativo || 0) +
                (campaña.sin_respuesta || 0),
            });
          });

          this.totalEntregadas = this.totalCampanasEnviadas;
          this.totalOriginal = this.totalCampanasEnviadas;
          this.entregadosOriginal = this.totalCampanasEnviadas;
          this.positivoOriginal = this.totalInteresPositivo;
          this.negativoOriginal = this.totalInteresNegativo;
          this.sinrespuestaOriginal = this.totalSinRespuesta;
          this.totalxCampañaOriginal = [...this.totalxCampaña];

          this.iniciarChartDonut();
          this.renderBarChartCanvas();
          this.datosCargados = true;
        })
        .catch((error) => {
          console.error("Error al cargar los datos:", error);
          this.datosCargados = true;
        });
    },

    // Similar to cargarDatos but does NOT reset any filters or filtrosModelos/filtrosActivos.
    // Use this when the user wants to refresh the underlying campaign data while keeping UI filters intact.
    recargarDatos() {
      this.cargandoTabla = true;
      // Keep current filter state intact
      axios
        .post(this.baseURL + "/api/informesCampanias", {
          idUsuario: this.idUsuario,
        })
        .then((response) => {
          this.listaCampañas = response.data.data;
          this.arregloOriginal = [...this.listaCampañas];
          console.log("Datos recargados (sin limpiar filtros):", this.listaCampañas);

          // Recompute totals based on the fresh data
          this.totalCampanasEnviadas = 0;
          this.totalInteresPositivo = 0;
          this.totalInteresNegativo = 0;
          this.totalSinRespuesta = 0;
          this.totalxCampaña = [];

          this.listaCampañas.forEach((campaña) => {
            this.totalCampanasEnviadas += campaña.interes_positivo || 0;
            this.totalCampanasEnviadas += campaña.interes_negativo || 0;
            this.totalCampanasEnviadas += campaña.sin_respuesta || 0;

            this.totalInteresPositivo += campaña.interes_positivo || 0;
            this.totalInteresNegativo += campaña.interes_negativo || 0;
            this.totalSinRespuesta += campaña.sin_respuesta || 0;

            this.totalxCampaña.push({
              id: campaña.id,
              nombre: campaña.nombre_campaña,
              total:
                (campaña.interes_positivo || 0) +
                (campaña.interes_negativo || 0) +
                (campaña.sin_respuesta || 0),
            });
          });

          this.totalEntregadas = this.totalCampanasEnviadas;
          this.totalOriginal = this.totalCampanasEnviadas;
          this.entregadosOriginal = this.totalCampanasEnviadas;
          this.positivoOriginal = this.totalInteresPositivo;
          this.negativoOriginal = this.totalInteresNegativo;
          this.sinrespuestaOriginal = this.totalSinRespuesta;
          this.totalxCampañaOriginal = [...this.totalxCampaña];

          // Apply existing UI filters to the freshly loaded data so the view keeps the current filters
          try {
            this.aplicarFiltros();
          } catch (e) {
            console.warn('Error aplicando filtros tras recarga:', e);
          }

          // Re-render charts with the filtered data on the next tick
          this.$nextTick(() => {
            try {
              this.iniciarChartDonut();
            } catch (e) { console.warn('Error iniciando donut tras recarga:', e); }
            try {
              this.renderBarChartCanvas();
            } catch (e) { console.warn('Error renderizando barra tras recarga:', e); }
            this.datosCargados = true;
            this.cargandoTabla = false;
          });
        })
        .catch((error) => {
          console.error("Error al recargar los datos:", error);
          this.datosCargados = true;
        });
    },

    aplicarFiltros() {
      // Normaliza fechas
      const toIsoDay = (d) => {
        const date = new Date(d);
        return isNaN(date) ? "" : date.toISOString().slice(0, 10);
      };

      let start = this.fechaInicio || null;
      let end = this.fechaFin || null;
      if (start && end && start > end) [start, end] = [end, start];

      // Normaliza ciudad y sector
      const ciudadNorm = this.ciudadSeleccionada
        ? this._norm(this.ciudadSeleccionada)
        : null;
      const sectorNorm = this.sectorSeleccionado
        ? this._norm(this.sectorSeleccionado)
        : null;

      const canalIdSeleccionado = this.canalSeleccionado === 0 ? null : this.canalSeleccionado;

      // Filtra sobre el arreglo original
      this.listaCampañas = this.arregloOriginal.filter((c) => {
        // Campaña: fuerza comparación por id, sea objeto o id
        let campanaId = null;
        if (this.campañaSeleccionada && typeof this.campañaSeleccionada === 'object') {
          campanaId = this.campañaSeleccionada.id;
        } else {
          campanaId = this.campañaSeleccionada;
        }
        const byCampana = campanaId ? c.id === campanaId : true;

        // Ciudad
        const byCiudad = ciudadNorm
          ? this._splitCiudades(c.ciudades).some(
            (city) => this._norm(city) === ciudadNorm
          )
          : true;

        // Sector
        const bySector = sectorNorm
          ? c.sectores &&
          c.sectores
            .split(",")
            .some((sector) => this._norm(sector.trim()) === sectorNorm)
          : true;

        // Fechas
        const f = toIsoDay(c.fecha);
        const byDateRange =
          (start ? f >= start : true) && (end ? f <= end : true);

        // Canal
        const byCanal = canalIdSeleccionado !== null ? c.canal === canalIdSeleccionado : true;

        setTimeout(() => {
          if (this.campañaSeleccionada) {
            this.campañasSeleccionadas = this.opcionesCampañas[0]
          } else {
            this.campañasSeleccionadas = [];
          }
        }, 1000);

        return byCampana && byCiudad && bySector && byDateRange && byCanal;
      });

      // Recalcula totales
      this.totalCampanasEnviadas = 0;
      this.totalInteresPositivo = 0;
      this.totalInteresNegativo = 0;
      this.totalSinRespuesta = 0;
      this.totalEntregadas = 0;
      this.totalxCampaña = [];

      this.listaCampañas.forEach((campaña) => {
        this.totalCampanasEnviadas += campaña.interes_positivo || 0;
        this.totalCampanasEnviadas += campaña.interes_negativo || 0;
        this.totalCampanasEnviadas += campaña.sin_respuesta || 0;
        this.totalEntregadas = this.totalCampanasEnviadas;

        this.totalInteresPositivo += campaña.interes_positivo || 0;
        this.totalInteresNegativo += campaña.interes_negativo || 0;
        this.totalSinRespuesta += campaña.sin_respuesta || 0;

        this.totalxCampaña.push({
          id: campaña.id,
          nombre: campaña.nombre_campaña,
          total:
            campaña.interes_positivo +
            campaña.interes_negativo +
            campaña.sin_respuesta,
        });
      });

      setTimeout(() => {
        this.iniciarChartDonut();
        this.renderBarChartCanvas();
      }, 500);
      console.log("Datos cargados:", this.listaCampañas);
    },

    iniciarChartDonut() {
      this.$nextTick(() => {
        const canvas = this.$refs.myChart2;
        if (canvas) {
          const ctx = canvas.getContext("2d");
          if (this.chartInstance2) {
            this.chartInstance2.destroy();
          }
          this.chartInstance2 = new Chart(ctx, {
            type: "doughnut",
            data: this.datosDonut,
            options: {
              responsive: true,
              plugins: {
                legend: {
                  display: false,
                  position: "right",
                  labels: {
                    font: { weight: "bold", size: 14 },
                    color: "#222",
                    padding: 20,
                    boxWidth: 18,
                    boxHeight: 18,
                  },
                },
                tooltip: {
                  callbacks: {
                    label: function (context) {
                      return `${context.label}: ${context.raw}`;
                    },
                  },
                },
              },
              cutout: "65%",
            },
            plugins: [doughnutLabelPlugin],
          });
        }
      });
    },


    formatDate(dateString) {
      const options = { day: "2-digit", month: "2-digit", year: "numeric" };
      return new Date(dateString).toLocaleDateString("es-ES", options);
    },

    cambiarClave() {
      const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

      if (this.nuevaClave !== this.confirmarClave) {
        this.alerta = true;
        this.mensajeAlertLogin = "Las claves no coinciden.";
        return;
      } else if (!regex.test(this.nuevaClave)) {
        this.alerta = true;
        this.mensajeAlertLogin =
          "La nueva clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.";
        return;
      } else {
        axios
          .post(this.baseURL + "api/cambiarclave", {
            idusu: localStorage.getItem("idUsuario"),
            claveActual: CryptoJS.MD5(this.claveActual).toString(),
            nuevaClave: CryptoJS.MD5(this.nuevaClave).toString(),
          })
          .then((response) => {
            if (
              response.data.data[0].respuesta ==
              "La clave actual ingresada no coincide con el usuario."
            ) {
              this.alerta = true;
              this.mensajeAlertLogin =
                "La clave actual ingresada no coincide con el usuario.";
            } else if (
              response.data.data[0].respuesta ==
              "La clave ha sido editada correctamente."
            ) {
              this.alerta = true;
              this.mensajeAlertLogin =
                "La clave ha sido editada correctamente.";
              this.dialogCambioClave = false;
              this.claveActual = null;
              this.nuevaClave = null;
              this.confirmarClave = null;
            }
          })
          .catch((error) => {
            console.error("Error al cambiar la clave:", error);
            this.alerta = true;
            this.mensajeAlertLogin = "Error al cambiar la clave.";
          });
      }
    },

    isValidPassword(password) {
      const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;
      return regex.test(password);
    },

    cerrarSesion() {
      localStorage.removeItem("idUsuario");
      localStorage.removeItem("idCargo");
      localStorage.removeItem("nombreLogin");
      localStorage.removeItem("apellidoLogin");
      localStorage.removeItem("celularLogin");
      localStorage.removeItem("logueado");
      this.$router.push("/");
    },

    irComercial() {
      this.$router.push("/comercial");
    },

    irPendientesGeneral() {
      this.$router.push("/pendiente-general");
    },

    irConfiguracion() {
      this.$router.push("/configuracion");
    },

    irPQR() {
      this.$router.push("/pqr");
    },

    irPedidos() {
      this.$router.push("/pedidos");
    },

    irCampañas() {
      this.$router.push("/campana");
    },

    irProspeccionTelefonica() {
      this.$router.push('/prospeccion-telefonica');
    },

    irSeguimientoLlamadas() {
      this.$router.push('/seguimiento-llamadas');
    },

    irGaleriaCampanas() {
      this.$router.push("/VerCampanas");
    },

    irEmpresas() {
      this.$router.push('/empresas');
    },

    irContactos() {
      this.$router.push("/contactos");
    },

    _splitCiudades(str) {
      if (!str) return [];
      const safe = str.replace(/bogotá,\s*d\.c\./gi, "Bogotá D.C."); // proteger nombre
      return safe
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean);
    },

    _norm(s) {
      return (s ?? "")
        .toString()
        .normalize("NFD")
        .replace(/\p{Diacritic}/gu, "")
        .toLowerCase()
        .replace(/\s+/g, " ")
        .trim();
    },

    cambiarImagen() {
      const input = document.createElement("input");
      input.type = "file";
      input.accept = "image/jpeg";

      input.onchange = async (event) => {
        const file = event.target.files[0];
        if (file) {
          const formData = new FormData();
          const nombre = `${this.comercialId}.jpeg`;
          formData.append("imagen", file);
          formData.append("nombre_archivo", nombre);

          try {
            await axios.post(this.baseURL + "api/subir-imagen", formData, {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            });

            // Forzar recarga para evitar caché
            this.imagenComercial = `/images/${this.comercialId
              }.jpeg?${Date.now()}`;
            this.mensajeAlertLogin =
              "Imagen actualizada correctamente, si no puedes vizualizarla, recarga la página.";
            this.alerta = true;
            this.ifCargando = false;
          } catch (error) {
            console.error("❌ Error al subir imagen:", error);
          }
        }
      };

      input.click();
    },

    restablecerFiltros() {
      this.campañaSeleccionada = null;
      this.ciudadSeleccionada = null;
      this.sectorSeleccionado = null;
      this.fechaInicio = null;
      this.fechaFin = null;
      // Restaurar lista y totales originales
      this.listaCampañas = [...this.arregloOriginal];
      this.totalCampanasEnviadas = this.totalOriginal;
      this.totalEntregadas = this.entregadosOriginal;
      this.totalInteresPositivo = this.positivoOriginal;
      this.totalInteresNegativo = this.negativoOriginal;
      this.totalSinRespuesta = this.sinrespuestaOriginal;
      this.totalxCampaña = [...this.totalxCampañaOriginal];
      this.canalSeleccionado = 0;
      // Reiniciar los gráficos
      this.iniciarChartDonut();
      this.renderBarChartCanvas();
    },

    calcularPorcentaje(valor, item) {
      const total =
        (item.interes_positivo || 0) +
        (item.interes_negativo || 0) +
        (item.sin_respuesta || 0);
      if (!total) return '';
      return `${Math.round((valor / total) * 100)}%`;
    },

    verDetallesCampana(idCampana) {
      this.idCampaniaSeleccionada = idCampana;
      // Busca el item y abre el diálogo
      this.selectedCampana = this.listaCampañas.find(c => c.id === idCampana) || null;

      this.buscadorCiudad = '';
      this.buscadorSector = '';

      this.sectoresDialog = (this.selectedCampana?.sectores || '').split(',').map(s => s.trim()).filter(Boolean);
      this.ciudadesDialog = this._splitCiudades(this.selectedCampana?.ciudades);
      console.log("CAMPAÑA SELECCIONADA:", this.selectedCampana);
      axios.post(this.baseURL + '/api/CampaniasEnviadasDetalle', {
        idCampania: idCampana
      })
        .then(response => {
          console.log('SELECTED CAMPAÑA RESPONSES:', response.data.data);
          this.selectedCampanaResponses = response.data.data
        })
        .catch(error => {
          console.error('Error al cargar los datos:', error);
        });
      this.dialogMetricasCampana = true;
      setTimeout(() => {
        this.readOnlyCloseButton = false;
      }, 1500);

    },
    closeDialogMetricas() {
      // Limpiar recursos antes de cerrar
      this.teardownCharts(); // 👈 destruye instancias de Chart.js
      this.selectedCampana = null;

      // Luego cerrar el diálogo
      this.dialogMetricasCampana = false;
      this.iframeChat = false;
      this.limpiarFiltrosMetricas();
    },

    limpiarFiltrosMetricas() {
      // Activar bandera para suprimir watchers
      this.suppressFiltrosWatch = true;

      // Limpiar todas las variables de filtro
      this.filtroContactoMetricas = null;
      this.filtroEmpresaMetricas = null;
      this.filtroCargoMetricas = null;
      this.filtroCategoriaCargoMetricas = null;
      this.filtroDepartamentoMetricas = null;
      this.filtroCanalMetricas = 0;
      this.filtroStatusMessageMetricas = null;
      this.filtroCiudadMetricas = null;
      this.filtroSectorMetricas = null;
      this.filtroInteresMetricas = null;
      this.filtroFechaInicioMetricas = '';
      this.filtroFechaFinMetricas = '';
      this.filtroEstadoMetricas = null;

      // Limpiar filtrosModelos
      this.filtrosModelos.contacto = null;
      this.filtrosModelos.empresa = null;
      this.filtrosModelos.cargo = null;
      this.filtrosModelos.categoriaCargo = null;
      this.filtrosModelos.departamento = null;
      this.filtrosModelos.status = null;
      this.filtrosModelos.ciudad = null;
      this.filtrosModelos.sector = null;
      this.filtrosModelos.interes = null;
      this.filtrosModelos.fechaInicio = '';
      this.filtrosModelos.fechaFin = '';
      this.filtrosModelos.estado = null;

      this.filtrosActivos = [];

      // Desactivar bandera y forzar un único redibujado en el siguiente tick
      this.$nextTick(() => {
        this.suppressFiltrosWatch = false;
        // Forzar redibujado de canvas después de limpiar
        this.redibujarBarCanvas();
      });
    },

    teardownCharts() {
      try { this.barChart?.stop(); this.barChart?.destroy(); } catch { }
      try { this.donutChart?.stop(); this.donutChart?.destroy(); } catch { }
      this.barChart = null;
      this.donutChart = null;
    },

    formatFecha(value) {
      if (!value) return '—';
      const d = new Date(value);
      if (isNaN(d)) return '—';
      return d.toLocaleDateString('es-CO', { day: '2-digit', month: 'long', year: 'numeric' });
    },
    numero(n) {
      const v = Number(n ?? 0);
      return isNaN(v) ? '0' : v.toLocaleString('es-CO');
    },
    totalEnvios(c) {
      if (!c) return 0;
      const pos = Number(c.interes_positivo ?? 0);
      const neg = Number(c.interes_negativo ?? 0);
      const sin = Number(c.sin_respuesta ?? 0);
      return pos + neg + sin;
    },
    seleccionarCampana(idCampana) {
      this.selectedCampana = this.listaCampañas.find(c => c.id === idCampana)
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
    statusColor(id) {
      if (id == 'sent') return 'blue';
      if (id == 'delivered') return 'green';
      if (id == 'failed') return 'red';
      if (id == 'rejected') return 'orange';
      if (id == 'read') return 'blue';
      return 'gray';
    },
    statusLabel(id) {
      const m = { 'sent': 'Enviado', 'delivered': 'Entregado', 'failed': 'No Existe', 'rejected': 'Rechazado', 'read': 'Entregado' };
      return m[id] ?? `No disponible`;
    },

    interesLabel(id) {
      const m = { 0: 'Sin respuesta', 1: 'Positivo', 2: 'Negativo' };
      return m[Number(id)] ?? '—';
    },
    interesColor(id) {
      const n = Number(id);
      if (n === 1) return '#2e7d32';   // verde
      if (n === 2) return '#c62828';   // rojo
      return '#1976d2';                // azul (sin respuesta / default)
    },

    estadoLabel(id) {
      const m = { 1: 'Nuevo', 2: 'En proceso', 3: 'Resuelto' };
      return m[Number(id)] ?? `Estado ${id}`;
    },
    estadoColor(id) {
      const n = Number(id);
      if (n === 1) return '#1976d2';
      if (n === 2) return '#2e7d32'; // Azul En proceso
      if (n === 3) return 'gray'; // gris
      return '';
    },

    abrirGestion(row) {
      this.selectedRespuesta = row;
      console.log("ROW RESPUESTA", this.selectedRespuesta);

      if (row?.id) this.cargarHistorial(row.id);

      // Abrir el diálogo
      setTimeout(() => {
        this.dialogGestionCampanas = true;
      }, 100);
    },



    cargarHistorial(id) {
      axios.post(this.baseURL + '/api/cargarHistorialCampana', {
        'idCampania': id,
      })
        .then(response => {
          this.historialCampania = response.data.data;
        })
        .catch(error => {
          console.error('Error al cargar historial de campaña:', error)
        })

    },
    renderDistribucion() {
      // Limpia instancia previa
      this.destroyDonut();

      this.readOnlyCloseButton = true;
      const ctx = this.$refs.donutCanvas?.getContext('2d');
      if (!ctx) return;

      // Obtén los datos correctos según el canal
      const { labels, data, colors } = this.getDonutMetricasFiltradas(this.selectedCampana);

      this.donutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels,
          datasets: [{
            data,
            backgroundColor: colors,
            borderWidth: 0,
          }],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '55%',
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: (ctx) => {
                  const total = data.reduce((a, b) => a + b, 0) || 1;
                  const value = ctx.parsed;
                  const pct = ((value / total) * 100).toFixed(1);
                  return `${ctx.label}: ${value} (${pct}%)`;
                },
              },
            },
          },
        },
      });
    },

    destroyDonut() {
      if (this.donutChart) {
        this.donutChart.destroy();
        this.donutChart = null;
      }
    },

    destroyBar() {
      if (this.barChart) {
        this.barChart.destroy();
        this.barChart = null;
      }
    },

    renderBar() {
      const ctx = this.$refs.barCanvas?.getContext('2d');
      if (!ctx) return;
      this.destroyBar?.();

      const { labels, values } = this.barSeries;

      this.barChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels,
          datasets: [{
            data: values,
            backgroundColor: '#1e88e5',
            borderWidth: 0,
            borderRadius: 6,
            maxBarThickness: 42,
          }],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: { callbacks: { label: t => `Envíos: ${t.parsed.y}` } }
          },
          scales: {
            x: { grid: { display: false } },
            y: { beginAtZero: true, ticks: { precision: 0 }, grid: { color: '#eee' } },
          },
        },
      });
    },

    async agregarHistorialGestion() {
      if (this.mensajesAlmacenados.length == 0) {
        this.alert = true;
        this.mensajeAlertLogin = 'No hay mensajes para guardar.';
        return;
      }

      if (this.selectedInteresCampaniaWhatsapp == null) {
        this.alertaInteres = true;
        this.mensajeAlertInteres = 'Por favor, seleccione el interés antes de guardar la gestión.';
        return;
      }

      this.mensajesAlmacenados = this.mensajesAlmacenados.filter((msg, index, self) =>
        index === self.findIndex((m) => m.id === msg.id)
      );

      try {
        const response = await axios.post(this.baseURL + 'api/agregarHistorialGestionWhatsapp', {
          idCampania: this.selectedRespuesta.id,
          idEstado: this.estadoItems[1].id,
          interes: this.selectedInteresCampaniaWhatsapp.id,
          idprospecto_contacto: this.selectedRespuesta.id_contacto,
          idUsuario: localStorage.getItem('idUsuario'),
          mensajes: this.mensajesAlmacenados
        });

        console.log('Historial de gestión agregado:', response.data);
        this.mensajesAlmacenados = [];
        this.selectedInteresCampaniaWhatsapp = null;

        this.alertaInteres = false;
        this.mensajeAlertInteres = '';
        this.mensajeAlertLogin = 'La gestión se registró correctamente.';
        this.alerta = true;

        this.cargarHistorial(this.selectedRespuesta.id);
      } catch (error) {
        console.error('Error al agregar historial de gestión:', error);
      }
    },

    GuardarGestionCampaña() {
      this.validandoActividad = true;

      if (!this.selectedGestionCampania?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite la Gestión de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (this.selectedEstadoCampania == null) {
        this.mensajeAlertLogin = 'Por favor, Digite el estado de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (this.selectedInteresCampania == null) {
        this.mensajeAlertLogin = 'Por favor, Digite el interés de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      const formData = new FormData();
      formData.append('idCampania', this.selectedRespuesta.id);
      formData.append('respuesta', this.selectedGestionCampania);
      formData.append('idEstado', this.selectedEstadoCampania);
      formData.append('interes', this.selectedInteresCampania);
      formData.append('idprospecto_contacto', this.selectedRespuesta.id_contacto);
      formData.append('idUsuario', localStorage.getItem('idUsuario'));

      axios.post(this.baseURL + 'api/EnviarHistorialCampania', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
        .then(response => {
          this.dialogNuevaActividad = false;

          setTimeout(() => {
            console.log('Respuesta guardada:', response.data);

            // Si hay archivos seleccionados, los sube; si no, solo guarda el historial
            if (Array.isArray(this.selectedArchivoCampania) && this.selectedArchivoCampania.length > 0) {
              let formData2 = new FormData();
              let formData3 = new FormData();
              let urlsCombinadas = '';
              formData2.append('id', response.data.data[0].idRespuestaCampania);
              this.idRespuestaCampania = response.data.data[0].idRespuestaCampania;
              this.selectedArchivoCampania.forEach(file => {
                formData2.append('files[]', file);
              });

              axios.post(this.baseURL + 'api/saveCampaniasFiles', formData2, {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              }).then(response => {
                console.log('Archivos guardados:', response.data.archivos);
                this.arrayArchivos = response.data.archivos;

                this.arrayArchivos.map(archivo => {
                  urlsCombinadas += archivo.url + '----';
                });

                urlsCombinadas = urlsCombinadas.slice(0, -4); // Eliminar los últimos cuatro guiones
                formData3.append('urls', urlsCombinadas);
                formData3.append('idRespuesta', this.idRespuestaCampania);

                axios.post(this.baseURL + 'api/updateCampaniasFilesUrl', formData3, {
                  headers: {
                    'Content-Type': 'multipart/form-data'
                  }
                }).then(() => {
                  this.LimpiarFormularioGestionCampaña();
                  this.mensajeAlertLogin = 'La respuesta se registró correctamente.';
                  this.alerta = true;
                  this.cargarDatos();
                  // Recargar historial para mostrar archivos sin recargar la página
                  if (this.selectedRespuesta?.id) {
                    this.cargarHistorial(this.selectedRespuesta.id);
                  }
                  if (this.selectedCampana?.id) {
                    this.readOnlyCloseButton = true;
                    this.verDetallesCampana(this.selectedCampana.id);
                    this.arrayArchivos = [];
                    this.idCampaniaSeleccionada = this.selectedCampana.id;
                    setTimeout(() => {
                      this.renderDistribucion();
                      this.renderBar();
                      this.readOnlyCloseButton = false;
                    }, 1500);
                  }
                }).catch(error => {
                  console.error('Error al guardar los archivos:', error);
                });

              }).catch(error => {
                console.error('Error al guardar los archivos:', error);
              });
            } else {
              // No hay archivos, solo limpiar y mostrar mensaje
              this.LimpiarFormularioGestionCampaña();
              this.mensajeAlertLogin = 'La respuesta se registró correctamente.';
              this.alerta = true;
              this.cargarDatos();
              if (this.selectedRespuesta?.id) {
                this.cargarHistorial(this.selectedRespuesta.id);
              }
              if (this.selectedCampana?.id) {
                this.readOnlyCloseButton = true;
                this.verDetallesCampana(this.selectedCampana.id);
                this.arrayArchivos = [];
                this.idCampaniaSeleccionada = this.selectedCampana.id;
                setTimeout(() => {
                  this.renderDistribucion();
                  this.renderBar();
                  this.readOnlyCloseButton = false;
                }, 1500);
              }
            }
          }, 600);
        })
        .catch(error => {
          console.error('Error al registrar la actividad:', error);
        })
        .finally(() => {
          this.validandoActividad = false;
          this.cargarDatos();
          if (this.selectedRespuesta?.id) {
            setTimeout(() => {
              this.cargarHistorial(this.selectedRespuesta.id);
            }, 600);
          }
        });
    },

    _toLocalIsoDay(d) {
      const y = d.getFullYear();
      const m = String(d.getMonth() + 1).padStart(2, '0');
      const day = String(d.getDate()).padStart(2, '0');
      return `${y}-${m}-${day}`; // YYYY-MM-DD (hora local)
    },

    formatFecha2(fecha) {
      const date = new Date(fecha);

      // Extraer día, mes, año
      const dia = String(date.getDate()).padStart(2, '0');
      const mes = String(date.getMonth() + 1).padStart(2, '0');
      const anio = date.getFullYear();

      // Hora en formato 12h
      let horas = date.getHours();
      const minutos = String(date.getMinutes()).padStart(2, '0');
      const ampm = horas >= 12 ? 'PM' : 'AM';

      horas = horas % 12;
      horas = horas ? horas : 12; // si es 0 -> 12

      return `${dia}-${mes}-${anio} ${horas}:${minutos} ${ampm}`;
    },

    cerrarFormularioGestionCampaña() {
      this.dialogGestionCampanas = false;
      this.selectedGestionCampania = null;
      this.selectedEstadoCampania = null;
      this.selectedInteresCampania = null;
      this.selectedArchivoCampania = null;
      this.iframeChat = false;
    },

    LimpiarFormularioGestionCampaña() {
      this.selectedGestionCampania = null;
      this.selectedEstadoCampania = null;
      this.selectedInteresCampania = null;
      this.selectedArchivoCampania = null;
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

    renderBarChartCanvas() {
      const canvas = this.$refs.barChartCanvas;
      if (!canvas) return;
      canvas.width = canvas.offsetWidth || 600;
      canvas.height = 320;
      const ctx = canvas.getContext('2d');
      if (this.barChart) { this.barChart.destroy(); }

      let chartData;
      if (this.canalSeleccionado === 0) {
        chartData = this.prepararDatosLineChartPorCanal();
      } else if (this.canalSeleccionado === 2) {
        chartData = this.prepararDatosLineChartTelefonico();
      } else if (this.canalSeleccionado === 1) {
        chartData = this.prepararDatosLineChartWhatsApp();
      } else if (this.canalSeleccionado === 3) {
        chartData = this.prepararDatosLineChartEmail();
      }

      // Solo top 10 en leyenda, pero muestra todas las líneas seleccionadas
      const topLeyenda = this.leyendaBarra;

      this.barChart = new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          layout: { padding: { left: 16, right: 16, top: 24, bottom: 24 } },
          plugins: {
            legend: {
              display: true,
              position: 'bottom',
              labels: {
                boxWidth: 24,
                boxHeight: 12,
                font: { size: 14, weight: 'bold' },
                padding: 18,
                color: '#222',
                filter: (legendItem, data) => topLeyenda.includes(legendItem.text),
              }
            },
            tooltip: {
              mode: 'index',
              intersect: false,
              callbacks: {
                title: (items) => {
                  const rawFecha = this.fechasOriginales?.[items[0].dataIndex] || items[0].label;
                  let fechaFormateada = '';
                  if (rawFecha) {
                    const dateObj = new Date(rawFecha + 'T00:00:00');
                    if (!isNaN(dateObj)) {
                      fechaFormateada = dateObj.toLocaleDateString('es-CO', { weekday: 'short', day: '2-digit', month: 'short' });
                    } else {
                      fechaFormateada = rawFecha;
                    }
                  }
                  const campañas = this.getCampañasPorFecha(rawFecha, this.canalSeleccionado);
                  let texto = fechaFormateada;
                  if (campañas.length > 0) {
                    texto += '\nCampañas: ' + campañas.join(', ');
                  }
                  return texto;
                },
                label: ctx => {
                  // Muestra el nombre de la campaña (dataset.label) y el valor
                  return `${ctx.dataset.label}: ${ctx.parsed.y}`;
                }
              }
            },
            title: {
              display: true,
              text: this.tipoGraficoBarra === 'canales' ? 'Tendencia por canal' : (this.tipoGraficoBarra === 'todas' ? 'Tendencia por todas las campañas' : 'Tendencia por interacciones'),
              font: { size: 18, weight: 'bold' },
              color: '#222',
              align: 'start',
              padding: { bottom: 10 }
            }
          },
          interaction: { mode: 'nearest', axis: 'x', intersect: false },
          scales: {
            x: {
              title: { display: true, text: 'Fecha', font: { size: 15, weight: 'bold' } },
              grid: { display: true, color: '#eee' },
              ticks: { color: '#222', font: { size: 13 } }
            },
            y: {
              beginAtZero: true,
              title: { display: true, text: 'Interacciones', font: { size: 15, weight: 'bold' } },
              grid: { display: true, color: '#eee' },
              ticks: { color: '#222', font: { size: 13 }, precision: 0 }
            }
          },
          elements: {
            line: { borderWidth: 3, tension: 0.4 },
            point: { radius: 5, hoverRadius: 7, borderWidth: 2, backgroundColor: '#fff' }
          },
        }
      });
    },

    prepararDatosLineChartPorCanal() {
      const fechas = [];
      const seriesPorCanal = {};
      const canales = [
        { id: 2, nombre: "Telefónico", color: "#1565c0" },
        { id: 1, nombre: "WhatsApp", color: "#22C55E" },
        { id: 3, nombre: "Email", color: "#F59E0B" },
      ];

      let campañasFiltradas = this.listaCampañas;
      if (this.campañasSeleccionadas && this.campañasSeleccionadas.length > 0) {
        campañasFiltradas = campañasFiltradas.filter(c =>
          this.campañasSeleccionadas.includes(c.nombre_campaña)
        );
      }

      campañasFiltradas.forEach(campaña => {
        // Normaliza la fecha a YYYY-MM-DD
        let fecha = '';
        if (campaña.fecha) {
          if (/^\d{4}-\d{2}-\d{2}/.test(campaña.fecha)) {
            fecha = campaña.fecha.slice(0, 10);
          } else {
            const d = new Date(campaña.fecha);
            if (!isNaN(d)) {
              fecha = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
            }
          }
        }
        if (fecha && !fechas.includes(fecha)) fechas.push(fecha);
        const canal = campaña.canal;
        if (!seriesPorCanal[canal]) seriesPorCanal[canal] = {};
        seriesPorCanal[canal][fecha] = (seriesPorCanal[canal][fecha] || 0) +
          (campaña.interes_positivo || 0) +
          (campaña.interes_negativo || 0) +
          (campaña.sin_respuesta || 0);
      });

      fechas.sort();
      const labels = fechas.map(f => this.formatLabelFecha(f));
      this.fechasOriginales = fechas;

      const datasets = canales.map((canal) => ({
        label: canal.nombre,
        data: fechas.map(f => (seriesPorCanal[canal.id] ? seriesPorCanal[canal.id][f] || 0 : 0)),
        borderColor: canal.color,
        backgroundColor: canal.color,
        tension: 0.4,
        fill: false,
        pointRadius: 4,
        pointHoverRadius: 6,
      }));

      return { labels, datasets };
    },

    prepararDatosLineChartTelefonico() {
      const fechas = [];
      const efectivasConLead = {};
      const efectivasSinLead = {};
      const noEfectivas = {};

      let campañasFiltradas = this.listaCampañas;
      if (this.campañasSeleccionadas && this.campañasSeleccionadas.length > 0) {
        campañasFiltradas = campañasFiltradas.filter(c =>
          this.campañasSeleccionadas.includes(c.nombre_campaña)
        );
      }

      campañasFiltradas.forEach(c => {
        if (c.canal !== 2) return;
        let fecha = '';
        if (c.fecha) {
          if (/^\d{4}-\d{2}-\d{2}/.test(c.fecha)) {
            fecha = c.fecha.slice(0, 10);
          } else {
            const d = new Date(c.fecha);
            if (!isNaN(d)) {
              fecha = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
            }
          }
        }
        if (fecha && !fechas.includes(fecha)) fechas.push(fecha);
        efectivasConLead[fecha] = (efectivasConLead[fecha] || 0) + (c.efectivo_con_lead || 0);
        efectivasSinLead[fecha] = (efectivasSinLead[fecha] || 0) + (c.efectivo_sin_lead || 0);
        noEfectivas[fecha] = (noEfectivas[fecha] || 0) + (c.no_efectivo || 0);
      });

      fechas.sort();
      const labels = fechas.map(f => this.formatLabelFecha(f));
      this.fechasOriginales = fechas;

      return {
        labels,
        datasets: [
          {
            label: 'Efectivas c/Lead',
            data: fechas.map(f => efectivasConLead[f] || 0),
            borderColor: '#19bf56',
            backgroundColor: '#19bf56',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'Efectivas s/Lead',
            data: fechas.map(f => efectivasSinLead[f] || 0),
            borderColor: '#3f94e8',
            backgroundColor: '#3f94e8',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'No efectivas',
            data: fechas.map(f => noEfectivas[f] || 0),
            borderColor: '#de8d04',
            backgroundColor: '#de8d04',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
        ],
      };
    },

    prepararDatosLineChartWhatsApp() {
      const fechas = [];
      const entregadas = {};
      const negativo = {};
      const noEntregadas = {};
      const positivo = {};
      const sinRespuesta = {};

      let campañasFiltradas = this.listaCampañas;
      if (this.campañasSeleccionadas && this.campañasSeleccionadas.length > 0) {
        campañasFiltradas = campañasFiltradas.filter(c =>
          this.campañasSeleccionadas.includes(c.nombre_campaña)
        );
      }

      campañasFiltradas.forEach(c => {
        if (c.canal !== 1) return;
        let fecha = '';
        if (c.fecha) {
          if (/^\d{4}-\d{2}-\d{2}/.test(c.fecha)) {
            fecha = c.fecha.slice(0, 10);
          } else {
            const d = new Date(c.fecha);
            if (!isNaN(d)) {
              fecha = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
            }
          }
        }
        if (fecha && !fechas.includes(fecha)) fechas.push(fecha);
        entregadas[fecha] = (entregadas[fecha] || 0) + ((c.interes_positivo || 0) + (c.interes_negativo || 0) + (c.sin_respuesta || 0));
        negativo[fecha] = (negativo[fecha] || 0) + (c.interes_negativo || 0);
        noEntregadas[fecha] = (noEntregadas[fecha] || 0) + (c.no_entregadas || 0);
        positivo[fecha] = (positivo[fecha] || 0) + (c.interes_positivo || 0);
        sinRespuesta[fecha] = (sinRespuesta[fecha] || 0) + (c.sin_respuesta || 0);
      });

      fechas.sort();
      const labels = fechas.map(f => this.formatLabelFecha(f));
      this.fechasOriginales = fechas;

      return {
        labels,
        datasets: [
          {
            label: 'Entregadas',
            data: fechas.map(f => entregadas[f] || 0),
            borderColor: '#19bf56',
            backgroundColor: '#19bf56',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'Negativo',
            data: fechas.map(f => negativo[f] || 0),
            borderColor: '#d95323',
            backgroundColor: '#d95323',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'No entregadas',
            data: fechas.map(f => noEntregadas[f] || 0),
            borderColor: '#de8d04',
            backgroundColor: '#de8d04',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'Positivo',
            data: fechas.map(f => positivo[f] || 0),
            borderColor: '#22C55E',
            backgroundColor: '#22C55E',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'Sin respuesta',
            data: fechas.map(f => sinRespuesta[f] || 0),
            borderColor: '#454a52',
            backgroundColor: '#454a52',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
        ],
      };
    },

    prepararDatosLineChartEmail() {
      const fechas = [];
      const conRespuesta = {};
      const entregadas = {};
      const noEntregadas = {};
      const sinRespuesta = {};

      let campañasFiltradas = this.listaCampañas;
      if (this.campañasSeleccionadas && this.campañasSeleccionadas.length > 0) {
        campañasFiltradas = campañasFiltradas.filter(c =>
          this.campañasSeleccionadas.includes(c.nombre_campaña)
        );
      }

      campañasFiltradas.forEach(c => {
        if (c.canal !== 3) return;
        let fecha = '';
        if (c.fecha) {
          if (/^\d{4}-\d{2}-\d{2}/.test(c.fecha)) {
            fecha = c.fecha.slice(0, 10);
          } else {
            const d = new Date(c.fecha);
            if (!isNaN(d)) {
              fecha = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
            }
          }
        }
        if (fecha && !fechas.includes(fecha)) fechas.push(fecha);
        conRespuesta[fecha] = (conRespuesta[fecha] || 0) + (c.con_respuesta || 0);
        entregadas[fecha] = (entregadas[fecha] || 0) + (c.entregadas || 0);
        noEntregadas[fecha] = (noEntregadas[fecha] || 0) + (c.no_entregadas || 0);
        sinRespuesta[fecha] = (sinRespuesta[fecha] || 0) + (c.sin_respuesta || 0);
      });

      fechas.sort();
      const labels = fechas.map(f => this.formatLabelFecha(f));
      this.fechasOriginales = fechas;

      return {
        labels,
        datasets: [
          {
            label: 'Con respuesta',
            data: fechas.map(f => conRespuesta[f] || 0),
            borderColor: '#3f94e8',
            backgroundColor: '#3f94e8',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'Entregadas',
            data: fechas.map(f => entregadas[f] || 0),
            borderColor: '#19bf56',
            backgroundColor: '#19bf56',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'No entregadas',
            data: fechas.map(f => noEntregadas[f] || 0),
            borderColor: '#de8d04',
            backgroundColor: '#de8d04',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
          {
            label: 'Sin respuesta',
            data: fechas.map(f => sinRespuesta[f] || 0),
            borderColor: '#454a52',
            backgroundColor: '#454a52',
            tension: 0.4,
            fill: false,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
        ],
      };
    },

    activarChat(contacto) {

      this.celularContacto = contacto.cel_contacto;

      if (!this.celularContacto) {
        this.mensajeAlertLogin = 'El contacto no tiene un número de celular válido para iniciar el chat.';
        console.log("Contacto sin celular:", contacto);
        this.alerta = true;
        return;
      }
      this.urlChat = `/chat-web?` + new URLSearchParams({
        ncliente: this.selectedRespuesta.nombre_contacto,
        ccliente: this.celularContacto,
        idusuario: this.comercialId,
        nusuario: this.nombreComercial,
        cusuario: this.celularComercial,
        rusuario: '5',
        idpqr: '0',
        perfilm: '0',
        isRecording: '0',
        //canal: this.canalTicketSeleccionado || 'web',
        canal: 'web',
        modulo: 'Campañas',
      }).toString();

      this.celularSeleccionado = this.celularContacto;

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
        this.contactoSeleccionado = null; // Limpia el contacto seleccionado
        setTimeout(() => {
          this.ifChatCard = true;
        }, 500);
      } else if (event.data.action === 'mensajesAlmacenados') {
        console.log('Mensajes almacenados recibidos:', event.data.data);
        this.mensajesAlmacenados = JSON.parse(event.data.data);
        console.log('Mensajes almacenados actualizados:', this.mensajesAlmacenados);
        this.agregarHistorialGestion();
      }
    },

    getChatStyle() {
      return {
        position: 'fixed',
        zIndex: '10000',
        right: '35px',
        bottom: '50px',
        borderRadius: '10px',
        boxShadow: 'rgba(0, 0, 0, 0.56) 0px 22px 70px 4px',
        height: '80vh',
        width: '28%',
      };
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
    getCampañasPorFecha(fecha, canal = null) {
      let campañas = this.listaCampañas.filter(c => c.fecha.slice(0, 10) === fecha);
      if (canal && canal !== 0) {
        campañas = campañas.filter(c => c.canal === canal);
      }
      // Si hay filtro de campañas seleccionadas, aplica también
      if (this.campañasSeleccionadas && this.campañasSeleccionadas.length > 0) {
        campañas = campañas.filter(c => this.campañasSeleccionadas.includes(c.nombre_campaña));
      }
      // Devuelve nombres únicos
      return [...new Set(campañas.map(c => c.nombre_campaña))];
    },

    canalNombre(id) {
      if (id === 1) return 'WhatsApp';
      if (id === 2) return 'Telefónico';
      if (id === 3) return 'Email';
      return '—';
    },

    getDonutMetricasCampana(campana) {
      if (!campana) return { labels: [], data: [], colors: [] };

      // WhatsApp, Email, Redes Sociales: modo seleccionable
      if ([1, 3, 4].includes(campana.canal)) {
        if (this.modoDonutDetalle === 'envios') {
          let entregadas = 0, noEntregadas = 0;
          if (campana.canal === 1 || campana.canal === 4) {
            entregadas = (campana.entregadas ?? (campana.interes_positivo ?? 0) + (campana.interes_negativo ?? 0) + (campana.sin_respuesta ?? 0));
            noEntregadas = campana.no_entregadas ?? 0;
          } else if (campana.canal === 3) {
            entregadas = campana.entregadas ?? 0;
            noEntregadas = campana.no_entregadas ?? 0;
          }
          return {
            labels: ['Entregadas', 'No entregadas'],
            data: [entregadas, noEntregadas],
            colors: ['#3f67e0', '#de8d04'],
          };
        } else {
          // Interacciones
          if (campana.canal === 1 || campana.canal === 4) {
            return {
              labels: ['Interés positivo', 'Interés negativo', 'Sin respuesta'],
              data: [
                campana.interes_positivo ?? 0,
                campana.interes_negativo ?? 0,
                campana.sin_respuesta ?? 0,
              ],
              colors: ['#22C55E', '#d95323', '#454a52'],
            };
          } else if (campana.canal === 3) {
            return {
              labels: ['Con respuesta', 'Sin respuesta'],
              data: [
                campana.con_respuesta ?? 0,
                campana.sin_respuesta ?? 0,
              ],
              colors: ['#3f94e8', '#454a52'],
            };
          }
        }
      }

      // Telefónico (igual que antes)
      if (campana.canal === 2) {
        return {
          labels: ['Efectivas c/Lead', 'Efectivas s/Lead', 'No efectivas'],
          data: [
            campana.efectivo_con_lead ?? 0,
            campana.efectivo_sin_lead ?? 0,
            campana.no_efectivo ?? 0,
          ],
          colors: ['#19bf56', '#3f94e8', '#de8d04'],
        };
      }

      // Default
      return {
        labels: ['Interés Positivo', 'Interés Negativo', 'Sin Respuesta'],
        data: [
          campana.interes_positivo ?? 0,
          campana.interes_negativo ?? 0,
          campana.sin_respuesta ?? 0,
        ],
        colors: ['#2e7d32', '#c62828', '#1976d2'],
      };
    },

    getDonutMetricasFiltradas() {
      // Usa los datos filtrados
      const arr = this.filteredMetricasCampana || [];
      // WhatsApp, Email, Redes Sociales: modo seleccionable
      if ([1, 3, 4].includes(this.selectedCampana?.canal)) {
        if (this.modoDonutDetalle === 'envios') {
          // Entregadas = todas las respuestas filtradas, No Recibidas = del objeto campaña
          const entregadas = arr.filter(r => r.status_mensaje === 'delivered' || r.status_mensaje === 'read').length;
          const noEntregadas = arr.filter(r => r.status_mensaje === 'sent').length;
          const noExiste = arr.filter(r => r.status_mensaje === 'failed').length;
          return {
            labels: ['Entregadas', 'No Entregadas', 'No Existe'],
            data: [entregadas, noEntregadas, noExiste],
            colors: ['#3f67e0', '#de8d04', '#19bf56'],
          };
        } else {
          // Interacciones
          const pos = arr.filter(r => r.interes === 1).length;
          const neg = arr.filter(r => r.interes === 2).length;
          const sin = arr.filter(r => r.interes === 0).length;
          return {
            labels: ['Interés positivo', 'Interés negativo', 'Sin respuesta'],
            data: [pos, neg, sin],
            colors: ['#22C55E', '#d95323', '#454a52'],
          };
        }
      }
      // Telefónico
      if (this.selectedCampana?.canal === 2) {
        const conLead = arr.filter(r => r.efectivo_con_lead === true).length;
        const sinLead = arr.filter(r => r.efectivo_sin_lead === true).length;
        const noEfectivo = arr.filter(r => r.no_efectivo === true).length;
        return {
          labels: ['Efectivas c/Lead', 'Efectivas s/Lead', 'No efectivas'],
          data: [conLead, sinLead, noEfectivo],
          colors: ['#19bf56', '#3f94e8', '#de8d04'],
        };
      }
      // Default
      return {
        labels: ['Interés Positivo', 'Interés Negativo', 'Sin Respuesta'],
        data: [
          arr.filter(r => r.interes === 1).length,
          arr.filter(r => r.interes === 2).length,
          arr.filter(r => r.interes === 0).length,
        ],
        colors: ['#2e7d32', '#c62828', '#1976d2'],
      };
    },

    getLeyendaDonutDetalle(campana) {
      if (!campana) return [];
      // Telefónico
      if (campana.canal === 2) {
        return [
          { icon: 'mdi-account-check', color: '#19bf56', label: 'Efectivas c/Lead' },
          { icon: 'mdi-account-plus', color: '#3f94e8', label: 'Efectivas s/Lead' },
          { icon: 'mdi-account-cancel', color: '#de8d04', label: 'No efectivas' },
        ];
      }
      // WhatsApp, Email, Redes Sociales: leyenda dinámica según modo
      if ([1, 3, 4].includes(campana.canal)) {
        if (this.modoDonutDetalle === 'envios') {
          return [
            { icon: 'mdi-check-all', color: '#3f67e0', label: 'Entregadas' },
            { icon: 'mdi-check', color: '#de8d04', label: 'No Entregadas' },
            { icon: 'mdi-cancel', color: '#19bf56', label: 'No Existe' },
          ];
        } else {
          if (campana.canal === 3) {
            return [
              { icon: 'mdi-email-check', color: '#3f94e8', label: 'Con respuesta' },
              { icon: 'mdi-help-circle-outline', color: '#454a52', label: 'Sin respuesta' },
            ];
          }
          // WhatsApp y Redes Sociales
          return [
            { icon: 'mdi-thumb-up', color: '#22C55E', label: 'Interés positivo' },
            { icon: 'mdi-thumb-down', color: '#d95323', label: 'Interés negativo' },
            { icon: 'mdi-help-circle-outline', color: '#454a52', label: 'Sin respuesta' },
          ];
        }
      }
      // Default
      return [
        { icon: 'mdi-lightbulb-on-10', color: '#2e7d32', label: 'Interés Positivo' },
        { icon: 'mdi-cancel', color: '#c62828', label: 'Interés Negativo' },
        { icon: 'mdi-check-all', color: '#1976d2', label: 'Sin Respuesta' },
      ];
    },

    esVideo(val) {
      if (!val) return false;
      // Si es un File, revisa el tipo
      if (typeof val === 'object' && val.type) return val.type.startsWith('video/');
      // Si es string (url o nombre), revisa la extensión
      return /\.(mp4|webm|ogg|mov|avi|mkv)(\?|$)/i.test(val);
    },

    formatLabelFecha(fechaStr) {
      if (!fechaStr) return '';
      // Si ya es YYYY-MM-DD
      if (/^\d{4}-\d{2}-\d{2}$/.test(fechaStr)) {
        const dateObj = new Date(fechaStr + 'T00:00:00');
        if (!isNaN(dateObj)) {
          return dateObj.toLocaleDateString('es-CO', { weekday: 'short', day: '2-digit', month: 'short' });
        }
      }
      // Si es tipo Date o string largo
      const dateObj = new Date(fechaStr);
      if (!isNaN(dateObj)) {
        return dateObj.toLocaleDateString('es-CO', { weekday: 'short', day: '2-digit', month: 'short' });
      }
      return '';
    },

    limpiarFiltroSectoresYCiudades() {
      this.buscadorCiudad = '';
      this.buscadorSector = '';
      this.searchProsp = '';
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

    setFiltrosPorDefecto() {
      this.filtroNombre = null;
      this.filtroCiudad = null;
      this.filtroSector = null;
      this.filtroCanal = 0;
      this.filtroFechaInicio = '';
      this.filtroFechaFin = '';
      this.filtroEstadoCampana = 'habilitadas';
    },

    getUltimaFechaEnvio() {
      if (!Array.isArray(this.selectedCampanaResponses) || this.selectedCampanaResponses.length === 0) return null;
      // Busca el objeto con la fecha más reciente
      const ultima = this.selectedCampanaResponses.reduce((max, curr) => {
        const fechaCurr = new Date(curr.fecha_envio || curr.fecha);
        const fechaMax = new Date(max.fecha_envio || max.fecha);
        return fechaCurr > fechaMax ? curr : max;
      });
      return ultima.fecha_envio || ultima.fecha;
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

    redibujarBarCanvas() {
      this.readOnlyCloseButton = true;
      if (this.dialogMetricasCampana) {
        this.$nextTick(() => {
          this.renderBar();
          this.renderDistribucion();
        });
      }
      setTimeout(() => {
        this.readOnlyCloseButton = false;
      }, 900);
    },

    rowClass(item) {
      return Number(item.rechazado) === 1 ? 'row-rechazado' : '';
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

    getAlertStyle2() {
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
        width: '30%',
        zIndex: '2500',
      };
    },

    cerrarDIV() {
      this.alerta = false;
    },

  },
};
</script>
<style scoped>
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

/* Estilo para el header de la v-data-table */
.v-data-table thead th {
  background-color: #006CA1 !important;
  color: white !important;
  font-weight: bold;
}

.v-data-table td[data-test="td-total"],
.v-data-table td[data-test="td-total"] .th-content,
.v-data-table td:last-child .th-content {
  color: #0a1c3a !important;
  font-weight: 700 !important;
  font-size: 0.98rem !important;
  letter-spacing: 0.1px !important;
}

.menu-link:hover {
  color: #0a1c3a;
  text-decoration: underline;
}

.donut-legend {
  display: flex;
  justify-content: center;
  gap: 32px 40px;
  /* Más espacio entre columnas y filas */
  margin-top: 12px;
  width: 100%;
  max-width: 800px;
  /* Permite que la leyenda se extienda más lateralmente */
}

.donut-legend-item {
  display: flex;
  align-items: center;
  gap: 32px;
  min-width: 150px;
  /* más compacto */
  max-width: 400px;
  flex: 0 1 150px;
  /* no se estira de más, pero permite wrap */
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 2px;
}

.city-sector-chips {
  gap: 6px 4px;
  max-width: 260px;
}

.chip-custom {
  font-size: 0.65rem !important;
  font-weight: 500 !important;
  border-radius: 16px !important;
  min-height: 28px !important;
  box-shadow: none !important;
  margin: 1px;
  text-align: center;
  align-items: center;
}

.sector-grid {
  display: grid;
  text-align: center;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, auto);
  max-width: 230px;
  min-height: 56px;
  align-items: center;
  position: relative;
}

.sector-plus-cell {
  grid-column: 4 / 4;
  grid-row: 1 / 3;
  display: flex;
  justify-content: center;
}

/* ===== Paginación bonita tipo pill ===== */
.pretty-pagination .v-pagination__list {
  gap: 6px;
  padding: 6px;
  border-radius: 999px;
  background: #f7f8fb;
  border: 1px solid rgba(0, 0, 0, .06);
}

/* Botoncitos */
.pretty-pagination .v-pagination__item .v-btn {
  min-width: 40px;
  height: 40px;
  border-radius: 12px;
  font-weight: 700;
  letter-spacing: -.2px;
}

/* Activo en color primario */
.pretty-pagination .v-pagination__item--is-active .v-btn {
  background-color: var(--v-theme-primary) !important;
  color: #fff !important;
}

/* Flechas prev/next */
.pretty-pagination .v-pagination__first,
.pretty-pagination .v-pagination__prev,
.pretty-pagination .v-pagination__next,
.pretty-pagination .v-pagination__last {
  opacity: .9;
}

/* Select “Mostrar” más compacto */
.min-140 {
  min-width: 140px;
}

.thumb-img {
  background: #f5f6f7;
  /* gris de fondo si no carga */
  border-radius: 12px;
  /* mismo radio que la card */
  overflow: hidden;
}

/*DIALOGO DE METRICAS CAMPAÑAS */

.metric-card {
  flex: 1 1 180px;
  min-width: 160px;
  max-width: 240px;
  border-radius: 14px;
  box-shadow: 0 2px 10px rgba(0, 108, 161, 0.06);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.metric-label {
  font-size: 1.08rem;
  font-weight: 600;
  opacity: 0.92;
  letter-spacing: 0.1px;
  margin-bottom: 2px;
  margin-left: 5px;
}

.metric-value {
  font-size: 1.45rem;
  font-weight: 600;
  letter-spacing: -1px;
  margin-left: 12px;
  margin-top: 1px;
  color: #0a1c3a;
}

@media (max-width: 900px) {
  .metrics-row {
    flex-direction: column;
    gap: 10px;
    padding: 10px 4px;
  }

  .metric-card {
    min-width: 100%;
    max-width: 100%;
  }
}

.metrics-row {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  padding: 18px 12px 12px 12px;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  justify-content: center;
}

.titulo-error {
  color: red !important;
}

.border-b {
  border-bottom: 1px solid rgba(0, 0, 0, .08);
}

.border-b:last-child {
  border-bottom: 0;
}

.list-group-compact {
  padding-right: 0 !important;
}

.list-item-compact {
  padding-right: 0 !important;
  margin-right: 0 !important;
}

.data-table-campanas {
  font-size: 0.97rem;
  background: #f8fafc;
  border-radius: 18px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
}

.fancy-headers :deep(.v-table__wrapper > table > thead > tr > th) {
  background-color: #006ba11b !important;
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

.row-even {
  background: #f5f7fa;
}

.row-odd {
  background: #ffffff;
}

.fancy-rows-campanas tr:hover {
  background: #e3f6ff !important;
  cursor: pointer;
}

.th-content {
  align-items: center;
  gap: 6px;
  font-weight: 700;
  color: #0a1c3a;
  font-size: 0.98rem;
  letter-spacing: 0.1px;
}

.filtros-campanas-card {
  border-radius: 18px;
  background: #fff;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.07);
}

.filtro-input {
  width: 100%;
  min-width: 120px;
  box-sizing: border-box;
}

@media (max-width: 1000px) {
  .filtro-input {
    min-width: 100px;
    font-size: 0.95rem;
  }
}

.canal-chips {
  gap: 6px;
}

.canal-chip {
  border-radius: 20px !important;
  font-weight: 600 !important;
  font-size: 0.98rem !important;
  margin-right: 4px;
  margin-bottom: 4px;
  cursor: pointer;
  transition: background 0.18s;
}

.canal-chip.v-chip--active {
  box-shadow: 0 2px 8px rgba(0, 108, 161, 0.08);
}

.canal-chip .v-icon {
  margin-right: 4px;
}

.canal-chip.selected-label {
  color: white !important;
}

@media (max-width: 1100px) {
  .canal-chips {
    flex-wrap: wrap;
    justify-content: flex-start;
    margin-bottom: 12px;
  }

  .filtros-campanas-card {
    padding: 10px !important;
  }
}

.aviso-metric-calcado {
  border-radius: 8px !important;
  min-height: 60px;
  min-width: 150px;
  max-width: 300px;
  box-shadow: none !important;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eaf2fb2f;
  transition: box-shadow 0.18s, transform 0.18s;
}

.aviso-metric-value-calcado {
  font-size: 1.1rem;
  font-weight: 1000;
  line-height: 1.1;
  color: white;
  margin-bottom: 2px;
  text-align: left;
}

.aviso-metric-label-calcado {
  font-size: 0.88rem;
  font-weight: 600;
  opacity: 1;
  color: white;
  margin-bottom: 0;
  text-align: left;
}

.aviso-metric-emoji-calcado {
  font-size: 1.5rem;
  margin-left: 14px;
  opacity: 0.96;
  filter: drop-shadow(0 1px 2px #0001);
  align-self: flex-end;
  transition: transform 0.18s;
}

@media (max-width: 900px) {
  .aviso-metric-calcado {
    min-width: 100px !important;
    max-width: 100% !important;
    padding: 8px 10px !important;
    border-radius: 10px !important;
  }

  .aviso-metric-value-calcado {
    font-size: 1.1rem !important;
  }

  .aviso-metric-label-calcado {
    font-size: 0.9rem !important;
  }

  .aviso-metric-emoji-calcado {
    font-size: 1.3rem !important;
    margin-left: 6px;
  }
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

.modern-alert {
  background: #fff0f3 !important;
  color: #b71c1c !important;
  border-radius: 10px !important;
  box-shadow: 0 2px 8px #b71c1c22;
}

.responsive-scale {
  transition: transform 0.2s;
  transform-origin: var(--scale-origin, center);
  transform: scale(1);
}

.responsive-gap {
  gap: var(--responsive-gap);
}

.responsive-size {
  transition: width 0.2s, height 0.2s;
  padding-left: 80px;
  min-width: 0;
  scroll-padding-left: 80px;
}

@media (max-width: 1024px),
(max-height: 800px) {
  .responsive-scale {
    transform: scale(var(--responsive-scale, 1));
  }

  .responsive-gap {
    gap: var(--responsive-gap, initial) !important;
  }

  .responsive-size {
    width: var(--responsive-width, initial) !important;
    height: var(--responsive-height, initial) !important;
  }

}

.row-hover:hover {
  background-color: #e3f6ff !important;
  cursor: pointer;
}

.hoverable-rows :deep(tbody tr) {
  transition: background 0.18s, box-shadow 0.18s;
  cursor: pointer;
}

.hoverable-rows :deep(tbody tr:hover) {
  background: #b8d4e7 !important;
  box-shadow: 0 2px 8px rgba(0, 108, 161, 0.10);
  filter: brightness(1.04);
}
</style>
