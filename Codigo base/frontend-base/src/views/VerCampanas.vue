<template>
  <!--src/views/VerCampanas.vue actual-->
  <v-app>
    <AppHeader :nombreComercial="nombreComercial" :imagenComercial="imagenComercial" :correoUsuario="correoUsuario" :comercialId="comercialId" :baseURL="baseURL" :idCargo="idCargo" v-model:drawer="drawer" @imagenActualizada="actualizarImagen" @cerrarSesion="cerrarSesion" />
<v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
  
  <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
        <!-- CONTENIDO PRINCIPAL: GALERÍA DE CAMPAÑAS -->
        <!-- HEADER VER CAMPAÑAS -->
        <v-sheet color="transparent" class="py-4">
          <v-row class="align-center ga-2">
            <v-col cols="12" md="auto" class="flex-grow-1">
              <v-tooltip text="Ver el historial de Galería" location="right">
                <template #activator="{ props }">
                  <div class="page-title text-h4 font-weight-bold">
                    Galerías de Campañas <v-btn color="#006CA1" class=" ml-2 btn-grow"
                      @click="abrirDialogHistorialGeneral" v-bind="props" icon>
                      <v-icon>mdi mdi-archive-clock</v-icon>
                    </v-btn>
                  </div>
                </template>
              </v-tooltip>
            </v-col>

            <v-col cols="12" md="auto" class="d-flex justify-end">

              <v-btn v-if="false" color="primary" variant="flat" size="large" rounded="lg"
                class="text-none px-5 btn-grow" prepend-icon="mdi-plus" @click="irCrearCampanas()">
                Crear nueva campaña
              </v-btn>

              <v-btn color="#039BE5" variant="flat" size="large" rounded="lg" class="text-none px-5 btn-grow ml-6"
                prepend-icon="mdi mdi-send-clock" @click="irEnviarCampana()">
                Enviar una Campaña
              </v-btn>
            </v-col>
          </v-row>
        </v-sheet>
        <!---AQUI TERMINA HEADER-->
        <!--Empieza FILTROS-->
        <v-card color="transparent" class="pt-1">
          <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
            <v-icon class="mr-2">mdi mdi-search-web</v-icon>
            Buscar Campañas
          </v-card-title>
          <v-container fluid class="mb-0">
            <v-row class="align-center flex-wrap">
              <!-- Buscar campaña -->
              <v-col cols="12" md="3" class="mb-2">
                <v-autocomplete v-model="filtroNombre" :items="nombresCampanias"
                  placeholder="Buscar Nombre de la Campaña" prepend-inner-icon="mdi-magnify" variant="outlined"
                  density="comfortable" hide-details clearable outlined dense />
              </v-col>
              <!-- Rango de fechas -->
              <v-col cols="6" md="2" class="mb-2">
                <v-text-field v-model="filtroFechaInicio" type="date" label="Desde" variant="outlined"
                  density="comfortable" hide-details clearable />
              </v-col>
              <v-col cols="6" md="2" class="mb-2">
                <v-text-field v-model="filtroFechaFin" type="date" label="Hasta" variant="outlined"
                  density="comfortable" hide-details clearable />
              </v-col>
              <!-- Canal -->
              <v-col cols="12" md="3" class="mb-2">
                <v-autocomplete v-model="filtroCanal" :items="[{ id: 0, nombre: 'Todos' }, ...canalesYMedios]"
                  item-title="nombre" item-value="id" label="Canal" variant="outlined" density="comfortable"
                  hide-details clearable prepend-inner-icon="mdi-access-point" />
              </v-col>
              <!-- Botón de filtros avanzados -->
              <v-col cols="12" md="2" class="mb-2 d-flex align-center">
                <v-menu v-model="menuFiltrosAvanzados" :close-on-content-click="false" offset-y location="end"
                  persistent>
                  <template #activator="{ props }">
                    <v-btn color="#006CA1" variant="outlined" v-bind="props" class="ml-2 d-flex align-center"
                      style="min-width: 180px; font-weight:600;">
                      <v-icon left>mdi-tune-variant</v-icon>
                      Filtros avanzados
                    </v-btn>
                  </template>

                  <v-card min-width="340">
                    <v-card-title class="text-h6 d-flex align-center" style="background-color: #006CA1; color: white;">
                      <v-icon class="mr-2">mdi-tune-variant</v-icon>
                      Filtros avanzados
                    </v-card-title>
                    <v-divider />
                    <v-card-text>
                      <v-autocomplete v-model="filtroPlantilla" :items="plantillasCampanias" label="Plantilla"
                        variant="outlined" density="comfortable" hide-details clearable
                        prepend-inner-icon="mdi-clipboard-list" class="mb-3" v-if="filtroCanal == 1" return-object
                        item-value="id" item-title="nombre" />
                      <v-autocomplete v-model="filtroCiudad" :items="ciudadesCampanias" label="Ciudad"
                        variant="outlined" density="comfortable" hide-details clearable prepend-inner-icon="mdi-city"
                        class="mb-3" />
                      <v-autocomplete v-model="filtroSector" :items="sectoresCampanias" label="Sector"
                        variant="outlined" density="comfortable" hide-details clearable prepend-inner-icon="mdi-domain"
                        class="mb-3" />
                      <v-select v-model="filtroEstadoCampana" :items="[
                        { value: 'todas', text: 'Todas' },
                        { value: 'habilitadas', text: 'Habilitadas' },
                        { value: 'deshabilitadas', text: 'Deshabilitadas' }
                      ]" item-title="text" item-value="value" label="Estado" variant="outlined" density="comfortable"
                        hide-details clearable prepend-inner-icon="mdi-toggle-switch" class="mb-3" />

                    </v-card-text>
                    <v-card-actions>
                      <v-spacer />
                      <v-btn color="#006CA1" variant="flat" @click="menuFiltrosAvanzados = false">Cerrar</v-btn>
                      <v-tooltip text="Limpiar Filtros " location="top">
                        <template v-slot:activator="{ props }">
                          <v-btn v-bind="props" color="#1d4ed8" icon size="small" class="ml-1 modern-btn btn-grow-card"
                            @click="this.setFiltrosPorDefecto()">
                            <v-icon>mdi mdi-broom</v-icon>
                          </v-btn>
                        </template>
                      </v-tooltip>
                    </v-card-actions>
                  </v-card>
                </v-menu>

              </v-col>
            </v-row>
          </v-container>
        </v-card>

        <!--Termina FILTROS-->
        <!--Empiezan las Cards de Campañas-->

        <!-- GRID DE CARDS -->
        <v-row class="justify-center cards-container mt-2">
          <v-col v-for="campanas in paginatedCampanas" :key="campanas.id" cols="12" sm="8" md="6" lg="4">
            <v-card rounded="xs" elevation="2" class="campaign-card mx-auto" bg-color="#006CA1"
              :style="campanas.activo === 0 ? 'opacity: 0.45; filter: grayscale(0.2);' : ''">
              <!--pointer-events: none-->
              <v-icon :color="getCanalInfo(campanas.canal).color"
                style="position: absolute; top: 45px; right: 18px; opacity: 0.03; font-size: 90px; pointer-events: none; z-index: 0;">
                {{ getCanalInfo(campanas.canal).icon }}
              </v-icon>
              <div :style="{
                height: '3.5px',
                width: '103%',
                borderTopLeftRadius: '8px',
                borderTopRightRadius: '8px',
                background: getCanalInfo(campanas.canal).color,
              }"></div>
              <v-card-title class="text-h7 d-flex justify-space-between align-center"
                style="background-color: #006CA1; color: white;">
                <div class="d-flex align-center">
                  <v-icon class="mr-2" size="28" :color="white">
                    {{ getCanalInfo(campanas.canal).icon }}
                  </v-icon>
                  <span style="font-weight: 700;" :style="{
                    fontSize: campanas.nombre_campaña && campanas.nombre_campaña.length > 30 ? '0.85rem' : '1.15rem'
                  }">
                    {{ campanas.nombre_campaña }}
                  </span>
                </div>
                <v-spacer></v-spacer>
                <v-chip v-if="campanas?.canal" class="ml-3" :color="getCanalInfo(campanas.canal).color"
                  text-color="white" size="small"
                  style="font-weight:700; font-size: 0.95rem; letter-spacing: 0.5px; background-color: white;"
                  elevation="2" label>
                  {{ getCanalInfo(campanas.canal).nombre || campanas.canal }}
                </v-chip>

              </v-card-title>
              <v-card-text class="pa-4">
                <div class="d-flex ga-4">
                  <!-- Col izquierda -->
                  <div class="justify-center align-center d-flex flex-column">
                    <template v-if="esVideo(campanas.url_media)">
                      <video :src="campanas.url_media" height="280" width="180"
                        style="border-radius:12px; object-fit:cover; background:#f5f6f7;" controls cover
                        poster="https://img.freepik.com/vector-gratis/diseno-plantilla-reproductor-video-estilo-blanco-minimo_1017-25481.jpg?semt=ais_incoming&w=740&q=80"
                        class="thumb-img"></video>
                    </template>
                    <template v-else>
                      <v-img
                        :src="campanas.url_media ? campanas.url_media : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s'"
                        aspect-ratio="9/12" height="220" width="180" cover position="center" class="thumb-img"
                        rounded="lg"
                        @click="abrirImagenAmpliada(campanas.url_media || 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s')" />
                    </template>
                  </div>

                  <!-- Col derecha -->
                  <div class="flex-grow-1 d-flex flex-column">
                    <!--<v-icon class="mr-2">mdi mdi-store-outline </v-icon> -->

                    <div class="font-weight-bold mb-2" :style="{
                      fontSize: campanas.nombre_campaña.length > 18
                        ? '1.3rem'
                        : '1.3rem',
                      textOverflow: 'ellipsis',
                      maxWidth: '100%'
                    }">
                      {{ campanas.nombre_campaña }}
                    </div>
                    <div class="text-body-1 text-medium-emphasis mb-3">

                      {{ new Date(campanas.fecha).toLocaleDateString('es-MX', {
                        day: '2-digit', month: 'long',
                        year: 'numeric'
                      }) }}
                    </div>

                    <!-- Métricas -->
                    <div class="text-body-1">
                      <div class="label">
                        <v-icon class="mr-2" size="small">mdi mdi-send-check</v-icon>
                        Envíos: {{ campanas.interes_positivo + campanas.interes_negativo + campanas.sin_respuesta }}
                      </div>
                      <div class="metric" v-for="m in getMetricasCardCampana(campanas)" :key="m.label">
                        <v-icon class="mr-2" size="small" :color="m.color">{{ m.icon }}</v-icon>
                        <span class="label">{{ m.label }}:</span>
                        <span class="value">{{ m.value ? m.value : 0 }}</span>
                      </div>
                    </div>

                    <div class="text-body-1 mt-3">

                      <div class="mt-2 d-flex flex-wrap align-center" style="gap: 6px; max-width: 100%;">
                        <template v-if="mostrarCiudades(campanas.ciudades).length === 0">
                          <v-chip size="small" color="#006CA1" text-color="white" class="city-chip"
                            style="font-weight: 600; font-size: 0.8rem; background: #e0e7ef;" label outlined>
                            <v-icon size="14" class="mr-1" color="#006CA1">mdi-alert-circle-outline</v-icon>
                            La campaña aún no se ha enviado
                          </v-chip>
                        </template>
                        <template v-else>
                          <template v-for="(ciudad, idx) in mostrarCiudades(campanas.ciudades)" :key="ciudad">
                            <v-chip size="small" color="#006CA1" text-color="white" class="city-chip"
                              style="font-weight: 600; font-size: 0.92rem;" label>
                              <v-icon size="14" class="mr-1" color="#1976d2">mdi-city</v-icon>
                              {{ ciudad }}
                            </v-chip>
                          </template>
                          <template v-if="ciudadesRestantes(campanas.ciudades).length > 0">
                            <v-tooltip location="top">
                              <template #activator="{ props }">
                                <v-chip v-bind="props" size="small" color="#006CA1" text-color="white" class="city-chip"
                                  style="font-weight: 600; font-size: 0.92rem; cursor:pointer;" label>
                                  +{{ ciudadesRestantes(campanas.ciudades).length }}
                                </v-chip>
                              </template>
                              <div style="max-width: 220px;">
                                <div v-for="ciudad in ciudadesRestantes(campanas.ciudades)" :key="ciudad">
                                  <v-icon size="14" class="mr-1" color="#1976d2">mdi-city</v-icon>
                                  {{ ciudad }}
                                </div>
                              </div>
                            </v-tooltip>
                          </template>
                        </template>
                      </div>

                    </div>

                  </div>

                </div>

              </v-card-text>

              <v-card-actions class="pa-4 pt-1">
                <v-tooltip text="Ver las metricas de la campaña" location="top">
                  <template #activator="{ props }">

                    <v-btn v-bind="props" variant="outlined" color="primary" class="btn-details text-none btn-grow-card"
                      append-icon="mdi-arrow-right"
                      @click="verDetallesCampana(campanas.id), dialogMetricasCampana = true, readOnlyCloseButton = true">
                      Ver detalles
                    </v-btn>
                  </template>
                </v-tooltip>
                <v-spacer />
                <v-tooltip text="Reenviar la Campaña" location="top">
                  <template v-slot:activator="{ props }">
                    <v-btn v-if="campanas.canal === 1" v-bind="props" @click="reenviarCampana(campanas)" icon
                      variant="text" color="primary" density="comfortable" class="refresh-btn btn-grow-card"
                      :disabled="isRefreshing">
                      <v-icon v-if="!isRefreshing">mdi mdi-send-variant</v-icon>
                      <v-progress-circular v-else indeterminate size="18" width="2" />
                    </v-btn>
                  </template>
                </v-tooltip>
                <v-tooltip text="Deshabilitar o Habilitar Campaña" location="top">
                  <template v-slot:activator="{ props }">
                    <v-btn v-bind="props" icon variant="text" :color="campanas.activo === 1 ? 'primary' : 'grey'"
                      density="comfortable" class="refresh-btn btn-grow-card" :disabled="isRefreshing"
                      @click="toggleEstadoCampana(campanas)">
                      <v-icon v-if="!isRefreshing">
                        {{ campanas.activo === 1 ? 'mdi-minus-circle-outline' : 'mdi-check-circle-outline' }}
                      </v-icon>
                      <v-progress-circular v-else indeterminate size="18" width="2" />
                    </v-btn>
                  </template>
                </v-tooltip>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row class="mt-4">
          <v-col cols="12" class="d-flex justify-center">
            <v-pagination v-model="page" :length="totalPages" total-visible="7" prev-icon="mdi-chevron-left"
              next-icon="mdi-chevron-right" class="pretty-pagination" />
          </v-col>

          <!-- Rango mostrado -->
          <v-col cols="12" class="text-center text-medium-emphasis">
            {{ ((page - 1) * itemsPerPage) + 1 }} – {{ Math.min(page * itemsPerPage, filteredCampanas.length) }}
            de {{ filteredCampanas.length }}
          </v-col>

          <!-- Selector "mostrar" -->
          <v-col cols="12" class="d-flex justify-center align-center">
            <span class="mr-3">Mostrar</span>
            <v-select v-model="itemsPerPage" :items="[9, 18, 27, 36, 45]" variant="outlined" density="comfortable"
              hide-details class="filter-chip min-140" style="max-width:140px" />
            <span class="ml-2">por página</span>
          </v-col>
        </v-row>


        <!--Terminan las Card de Campañanas-->

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
                                item-value="key" label="Selecciona filtros" multiple chips closable-chips
                                variant="outlined" density="comfortable" hide-details prepend-inner-icon="mdi-filter"
                                clearable :menu-props="{ maxHeight: '300px' }" style="width:100%; max-width: 420px;"
                                class="mb-4" autocomplete>
                                <template #selection="{ item, index }">
                                  <v-chip v-if="index < 2" :key="item.value" size="small" color="#006CA1"
                                    text-color="white" class="mr-1">
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
                                    :disabled="readOnlyCloseButton" variant="outlined" density="comfortable"
                                    hide-details clearable class="mb-3"
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
                                  <v-btn :disabled="readOnlyCloseButton" v-bind="props" color="#1d4ed8" icon
                                    size="small" class="ml-1 modern-btn btn-grow-card"
                                    @click="limpiarFiltrosMetricas()">
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
                      class="mr-1">mdi-phone</v-icon> Total Envíos: {{ numero(filteredMetricasCampana.length) }}</span>
                  <span v-else-if="selectedCampana?.canal === 1"><v-icon size="16" color="#006CA1"
                      class="mr-1">mdi-whatsapp</v-icon> Total Envíos: {{ numero(filteredMetricasCampana.length)
                      }}</span>
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
                        style="max-width:460px; border-radius:12px; background:#f5f6f7;" controls height="240"
                        width="200"
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
                <v-btn icon="mdi-download" size="small" color="white" class="mr-2 btn-grow"
                  :disabled="readOnlyCloseButton"
                  @click="verDetallesCampana(idCampaniaSeleccionada); redibujarBarCanvas();">
                  <v-icon left>mdi-reload</v-icon>
                </v-btn>
                <v-tooltip text="Limpiar Filtros " location="top">
                  <template v-slot:activator="{ props }">
                    <v-menu v-model="menuFiltrosAvanzadosDetalles2" :close-on-content-click="false" offset-y
                      location="end" persistent>
                      <template #activator="{ props }">
                        <v-btn color="white" variant="outlined" v-bind="props" class="ml-2 d-flex align-center"
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
                  <v-chip size="small" :color="estadoColor(item.estado)" variant="tonal" @click="abrirGestion(item)"
                    class="text-subtitle-2" v-if="selectedCampana?.activo === 1">
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
                <v-chip v-for="ciudad in ciudadesFiltradas" :key="ciudad" color="#1976d2" text-color="white"
                  size="small" label @click="searchProsp = ciudad">
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
                <v-chip v-for="sector in sectoresFiltrados" :key="sector" color="#1976d2" text-color="white"
                  size="small" class="btn-grow-card" label @click="searchProsp = sector">
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

        <!-- DIALOGO FORMULARIO GESTION -->
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
                    <span style="font-weight: 500;">No se puede registrar una nueva respueta, el caso fue registrado
                      como
                      resuelto</span>
                  </v-alert>
                  <v-sheet rounded="lg" elevation="1" class="pa-3">
                    <v-textarea v-model="selectedGestionCampania" label="Gestión" variant="outlined" auto-grow rows="3"
                      density="comfortable" class="mb-3" :disabled="tieneCasoResuelto" />

                    <v-select v-model="selectedEstadoCampania" :items="estadoItems" item-title="label" item-value="id"
                      label="Estado" variant="outlined" density="comfortable" class="mb-3"
                      :disabled="tieneCasoResuelto" />

                    <v-select v-model="selectedInteresCampania" :items="interesItems" item-title="label" item-value="id"
                      label="Interés" variant="outlined" density="comfortable" class="mb-3"
                      :disabled="tieneCasoResuelto" />

                    <v-file-input v-model="selectedArchivoCampania" multiple label="Adjuntar archivos"
                      variant="outlined" density="comfortable" prepend-icon="mdi-paperclip" show-size class="mb-4"
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
                  <!-- Formulario izquierdo -->
                  <v-col cols="12" md="7" class="d-flex flex-column pa-0 ml-2 mt-2">
                    <v-text-field v-model.trim="selectedNombreCampaña" label="Nombre de la campaña"
                      prepend-inner-icon="mdi-bell" variant="outlined" density="comfortable" clearable class="mb-3" />
                    <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                      Este campo es obligatorio
                    </div>

                    <v-textarea v-model.trim="selectedDetalleCampaña" label="Detalle de la campaña"
                      prepend-inner-icon="mdi-account-details-outline" variant="outlined" density="comfortable"
                      auto-grow rows="2" hint="Digitá la descripción que tendrá la campaña" persistent-hint
                      class="mb-3" />
                    <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                      Este campo es obligatorio
                    </div>

                    <v-textarea v-model.trim="selectedGuionCampaña" label="Guion de la campaña"
                      prepend-inner-icon="mdi-text-box-multiple-outline" variant="outlined" density="comfortable"
                      auto-grow rows="5" hint="Guión que se necesitará para realizar la campaña." persistent-hint />
                    <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                      Este campo es obligatorio
                    </div>
                  </v-col>

                  <!-- Imagen derecha -->
                  <v-col cols="12" md="4" class="d-flex flex-column align-center justify-center pa-0 ml-8">
                    <div class="image-upload-area" @click="() => $refs.inputImagenCampana.click()"
                      @keydown.enter="() => $refs.inputImagenCampana.click()" tabindex="0"
                      style="cursor:pointer; outline:none; border-radius:16px; border:2px dashed #b0bec5; min-height:220px; min-width:180px; display:flex; align-items:center; justify-content:center; position:relative; background:#f8fafc;">
                      <template v-if="esVideo(selectedImagenCampaña?.name || previewImagenCampana)">
                        <video :src="previewImagenCampana" height="220" width="180"
                          style="border-radius:12px; object-fit:cover; background:#f5f6f7;" controls
                          poster="https://www.freepik.es/fotos-vectores-gratis/play-video" class="elevation-1"></video>
                      </template>
                      <template v-else>
                        <v-img
                          :src="previewImagenCampana || 'https://shop.myharvestfarms.com/product/holistic-morning-kit/'"
                          height="220" width="180" cover style="border-radius:12px; object-fit:cover;"
                          class="elevation-1" />
                      </template>
                      <!-- Input de archivo oculto -->
                      <input ref="inputImagenCampana" type="file" accept="image/*,video/*" style="display:none"
                        @change="onImagenCampanaChange" />
                    </div>
                    <div class="text-caption mt-2" style="color:#888;">
                      Haz clic en la imagen para cambiarla<br>
                      <span style="font-size:12px;">(Máx. 14MB.)</span>
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
              <v-btn variant="outlined" color="primary" class="btn-details text-none btn-grow-card"
                @click="GuardarFormularioCampaña()">
                Guardar
                <v-icon end class="ml-1">mdi-content-save-check</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!------  Dialog Editar Campaña  ------>

        <v-dialog v-model="dialogEditarCampañas" max-width="800" transition="dialog-bottom-transition" persistent>
          <v-card rounded="xl" elevation="3" class="dialog-card">
            <!-- Header -->
            <v-card-title class="py-3 px-4 d-flex align-center" style="background:#3949AB;color:#fff;">
              <v-icon class="mr-2">mdi mdi-pen</v-icon>
              <span class="text-h6">Editar Campaña: {{ selectedCampana?.nombre_campaña }}</span>
              <v-spacer />
              <v-btn icon variant="text" color="white" @click="cerrarFormularioEditarCampaña()">
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-card-title>

            <!-- Body -->
            <!-- Imagen editable en el diálogo de editar campaña -->
            <v-card-text class="px-4 pt-4 pb-0">
              <v-form ref="formNuevaCampaña" v-model="formOk">
                <v-row>
                  <!-- Formulario izquierdo -->
                  <v-col cols="12" md="7" class="d-flex flex-column pa-0 ml-2 mt-2">
                    <v-text-field v-model.trim="selectedNombreCampaña" label="Nombre de la campaña"
                      prepend-inner-icon="mdi-bell" variant="outlined" density="comfortable" clearable class="mb-3" />
                    <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                      Este campo es obligatorio
                    </div>

                    <v-textarea v-model.trim="selectedDetalleCampaña" label="Detalle de la campaña"
                      prepend-inner-icon="mdi-account-details-outline" variant="outlined" density="comfortable"
                      auto-grow rows="2" hint="Digitá la descripción que tendrá la campaña" persistent-hint
                      class="mb-3" />
                    <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                      Este campo es obligatorio
                    </div>

                    <v-textarea v-model.trim="selectedGuionCampaña" label="Guion de la campaña"
                      prepend-inner-icon="mdi-text-box-multiple-outline" variant="outlined" density="comfortable"
                      auto-grow rows="5" hint="Guión que se necesitará para realizar la campaña." persistent-hint />
                    <div v-if="validandoActividad" class="titulo-error" style="font-size: 14px;">
                      Este campo es obligatorio
                    </div>
                  </v-col>

                  <!-- Imagen derecha -->
                  <v-col cols="12" md="4" class="d-flex flex-column align-center justify-center pa-0 ml-8">
                    <div class="image-upload-area" @click="() => $refs.inputImagenCampanaEditar.click()"
                      @keydown.enter="() => $refs.inputImagenCampanaEditar.click()" tabindex="0"
                      style="cursor:pointer; outline:none; border-radius:16px; border:2px dashed #b0bec5; min-height:220px; min-width:180px; display:flex; align-items:center; justify-content:center; position:relative; background:#f8fafc;">
                      <template
                        v-if="esVideo(selectedImagenCampanaEditar?.name || previewImagenCampanaEditar || selectedCampana?.url_media)">
                        <video :src="previewImagenCampanaEditar || selectedCampana?.url_media" height="220" width="180"
                          style="border-radius:12px; object-fit:cover; background:#f5f6f7;" controls
                          poster="https://www.freepik.es/fotos-vectores-gratis/play-video" class="elevation-1"></video>
                      </template>
                      <template v-else>
                        <v-img
                          :src="previewImagenCampanaEditar || selectedCampana?.url_media || 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s'"
                          height="220" width="180" cover style="border-radius:12px; object-fit:cover;"
                          class="elevation-1" />
                      </template>
                      <!-- Input de archivo oculto -->
                      <input ref="inputImagenCampanaEditar" type="file" accept="image/*,video/*" style="display:none"
                        @change="onImagenCampanaEditarChange" />
                    </div>
                    <div class="text-caption mt-2" style="color:#888;">
                      Haz clic en la imagen para cambiarla<br>
                      <span style="font-size:12px;">(Máx. 14MB)</span>
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
                @click="cerrarFormularioEditarCampaña()">Cancelar</v-btn>
              <v-btn variant="outlined" color="primary" class="btn-details text-none btn-grow-card"
                @click="EditarFormularioCampaña(this.selectedCampana.id)">
                Editar
                <v-icon end class="ml-1">mdi mdi-pen-plus</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

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
      <transition name="slide-y-reverse-transition">
        <iframe id="iframeChatID" v-if="iframeChat" :src="urlChat" transition="scroll-y-reverse-transition"
          :style="getChatStyle()" frameborder="0">
        </iframe>
      </transition>
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

    <v-dialog v-model="dialogCambioClave" persistent max-width="400px">
      <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
        <v-icon class="mr-2">mdi mdi-pen-lock</v-icon>
        Cambiar Clave
      </v-card-title>
      <v-card class="pa-4 ">
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
          <div class="text-caption mt-n4 mb-4" style="color: red;" v-if="nuevaClave && !isValidPassword(nuevaClave)">
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

    <!--DIALOGO DE HISTORIAL-->
    <v-dialog v-model="dialogHistorialGeneral" max-width="200vh" height="100vh" persistent>
      <v-card class="pa-4" style="height: 100%;">
        <v-card variant="outlined" elevation="5" class="pa-4 rounded-xl d-flex flex-column" style="height: 100%;">

          <!-- Encabezado -->
          <div style="position: sticky; top: 0; z-index: 2; margin-bottom: 2vh;" class="rounded-xs">

            <v-alert color="#027cb8" class="mb-4 pa-4 rounded-xs ">
              <v-row align="center" justify="space-between" class="ma-0 pa-0">
                <!-- Título a la izquierda -->
                <v-col cols="12" md="4" class="d-flex align-center">
                  <v-icon size="26" color="white ">mdi-clock-outline</v-icon>
                  <h2 class="ml-2 mb-0" style="">Historial Actividad de Campañas</h2>

                </v-col>
                <!-- Buscadores y botón a la derecha -->
                <v-col cols="12" md="8" class="d-flex justify-end align-center" style="gap: 20px;">
                  <v-text-field v-model="buscadorHistorialGeneral" placeholder="Buscar en historial…" density="compact"
                    variant="solo" bg-color="rgba(255,255,255, 0.9)" base-color="rgba(255,255,255, 0.9)" color="white"
                    prepend-inner-icon="mdi-magnify" clearable rounded="lg" hide-details style="max-width: 320px;" />
                  <!-- Buscar por fecha (input nativo) -->
                  <v-text-field v-model="busquedaFechaHistorialInicio" type="date" density="compact" variant="solo"
                    bg-color="rgba(255,255,255, 0.9)" prepend-inner-icon="mdi-calendar" clearable rounded="lg"
                    hide-details style="max-width: 200px;" label="Desde" />
                  <v-text-field v-model="busquedaFechaHistorialFin" type="date" density="compact" variant="solo"
                    bg-color="rgba(255,255,255, 0.9)" prepend-inner-icon="mdi-calendar" clearable rounded="lg"
                    hide-details style="max-width: 200px;" label="Hasta" />

                  <v-tooltip text="Recargar Todas las observaciones" location="top">
                    <template #activator="{ props }">
                      <v-btn icon size="small" v-bind="props"
                        @click="canalFiltro = null; limpiarCamposHistorial(), abrirDialogHistorialGeneral()">
                        <v-icon color="black">mdi-cached</v-icon>
                      </v-btn>
                    </template>
                  </v-tooltip>
                  <v-tooltip text="Cerrar Historial" location="top">
                    <template #activator="{ props }">
                      <v-btn icon size="small" class="btn-grow" v-bind="props" @click="dialogHistorialGeneral = false">
                        <v-icon color="black">mdi-window-close</v-icon>
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
                <v-timeline-item
                  v-for="canal in [{ id: 0, nombre: 'Todos', color: '#888', icon: 'mdi-access-point' }, ...canalesYMedios]"
                  :key="canal.id" :dot-color="canalFiltro === canal.id ? canal.color : '#bdbdbd'" size="x-small"
                  fill-dot>
                  <v-card @click="canalFiltro = canalFiltro === canal.id ? 0 : canal.id"
                    :color="canalFiltro === canal.id ? canal.color : '#f5f5f5'" class="pa-2 btn-grow"
                    style="white-space: pre; cursor:pointer; min-width:120px; text-align:center; font-weight:600;"
                    :elevation="canalFiltro === canal.id ? 8 : 2">
                    <v-icon class="mt-n1 mr-1" :color="canalFiltro === canal.id ? 'white' : canal.color">{{ canal.icon
                    }}</v-icon>
                    <span :style="{ color: canalFiltro === canal.id ? 'white' : canal.color }">{{ canal.nombre }}</span>
                  </v-card>
                </v-timeline-item>
              </v-timeline>
            </v-row>
          </div>
          <!-- Cuerpo scroll -->
          <!-- Historial de campañas y respuestas -->
          <div style="overflow-y: auto; flex: 1; max-height: 60vh;" class="mt-2 mb-2 ml-2 custom-scroll">
            <v-progress-circular v-if="historialGeneralFiltrado.length === 0" indeterminate color="#006CA1" size="50"
              width="7" class="mx-10" />
            <v-row v-for="(item, index) in historialGeneralFiltrado" :key="index" class="mb-2 align-start" no-gutters>
              <!-- Avatar -->
              <v-col cols="auto" class="pr-2 d-flex justify-center">
                <v-avatar size="30" :color="item.color">
                  <v-icon color="white" dark size="20">{{ item.icon }}</v-icon>
                </v-avatar>
              </v-col>
              <!-- Tarjeta del evento -->
              <v-col>
                <v-card class="pa-2" variant="outlined" style="border-radius: 10px; font-size: 2vh;">
                  <div class="d-flex justify-space-between align-center">
                    <strong>
                      <span style="color: #311B92;">
                        {{ item.tipo === 'creacion'
                          ? 'Creación de campaña: '
                          : item.tipo === 'modificacion'
                            ? 'Edición de campaña: '
                            : 'Respuesta de campaña: '
                        }}
                      </span>
                      <span class="mb-1" style="font-size: 1.7vh; color: #1976d2;"> {{ item.nombre_campaña }} </span>
                    </strong>
                    <span style="font-size: 1.5vh;">{{ item.fecha }}</span>
                  </div>
                  <!-- NUEVO: Mostrar nombre de campaña si es respuesta -->

                  <div class="d-flex justify-space-between align-center" style="font-size: 1.9vh;">
                    <div>
                      {{ item.descripcion }}
                      <span v-if="item.interes" class="ml-2" :style="{ color: item.color }">
                        ({{ item.interes }})
                      </span>

                    </div>

                    <div v-if="item.canal" class="" style="font-size: 1.7vh;">
                      <v-icon size="18" class="mr-1" :color="getCanalInfo(item.canal).color">
                        {{ getCanalInfo(item.canal).icon }}
                      </v-icon>
                      <span :style="{ color: getCanalInfo(item.canal).color, fontWeight: 500 }">
                        {{ getCanalInfo(item.canal).nombre }}
                      </span>
                    </div>

                  </div>
                  <div v-if="item.ciudad" class="text-caption mt-1">
                    <v-icon size="16" color="#1976d2" class="mr-1">mdi-city</v-icon>
                    {{ item.ciudad }}

                  </div>
                  <template
                    v-if="item.tipo === 'creacion' && (!item.ciudad || item.ciudad === '' || item.ciudad === null)">
                    <v-chip size="small" color="#006CA1" text-color="white" class="city-chip"
                      style="font-weight: 600; font-size: 0.8rem; background: #e0e7ef;" label outlined>
                      <v-icon size="14" class="mr-1" color="#006CA1">mdi-alert-circle-outline</v-icon>
                      La campaña aún no se ha enviado
                    </v-chip>
                  </template>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </v-card>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogImagenAmpliada"
      :max-width="infoImagenPreview ? (infoImagenPreview.width + 200) + 'px' : '90vw'" persistent scrollable>
      <v-card-title class="d-flex align-center justify-space-between"
        style="background: #006CA1; color: white; border-top-left-radius: 18px; border-top-right-radius: 18px;">
        <div class="d-flex align-center">
          <v-icon class="mr-2" color="white">mdi-image</v-icon>
          Vista previa de la imagen
        </div>
        <v-btn icon color="white" @click="dialogImagenAmpliada = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-title>
      <v-card style="border-radius: 18px; background: #f8fafc;">
        <!-- Cabecera -->


        <!-- Imagen centrada, tamaño real -->
        <v-card-text class="d-flex flex-column align-center justify-center" :style="{
          background: '#fff',
          padding: '24px',
          minHeight: infoImagenPreview ? (infoImagenPreview.height + 48) + 'px' : 'auto'
        }">
          <v-img v-if="infoImagenPreview" :src="imagenAmpliadaUrl" :width="infoImagenPreview.width"
            :height="infoImagenPreview.height" :style="{
              background: '#fff',
              maxWidth: '90vw',
              maxHeight: '80vh',
              cursor: 'zoom-in'
            }" class="mb-2" contain @click="abrirImagenEnNuevaPestana(imagenAmpliadaUrl)">
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
          <v-btn v-if="imagenAmpliadaUrl" color="primary" variant="outlined" :href="imagenAmpliadaUrl" target="_blank"
            download class="mr-2">
            <v-icon left size="18">mdi-download</v-icon>
            Descargar
          </v-btn>
          <v-btn color="grey" variant="flat" @click="dialogImagenAmpliada = false">
            <v-icon left size="18">mdi-close</v-icon>
            Cerrar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <!---->
  </v-app>
</template>


<script>
import AppHeader from '../components/AppHeader.vue';
import axios from 'axios';
import CryptoJS from "crypto-js";
import Pusher from 'pusher-js';
import Echo from 'laravel-echo';

window.Pusher = Pusher;

import {
  Chart,
  BarController, BarElement,
  CategoryScale, LinearScale,
  DoughnutController, ArcElement,
  Tooltip, Legend,
} from 'chart.js';

Chart.register(DoughnutController, ArcElement, Tooltip, Legend);
Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend);

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

    alertaInteres: false,
    mensajeAlertInteres: null,
    selectedInteresCampaniaWhatsapp: null,

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
    canalesYMedios: [
      { id: 2, nombre: "Telefónico", color: "#3f94e8", icon: "mdi-phone" },
      { id: 1, nombre: "WhatsApp", color: "#029e3b", icon: "mdi-whatsapp" },
      { id: 3, nombre: "Email", color: "#e39005", icon: "mdi-email" },
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
    menuAbierto: false,
    drawer: false,
    inicio: 1,

    ifCargando: false,

    dialogCambioClave: false,
    claveActual: null,
    nuevaClave: null,
    confirmarClave: null,
    mostrarClaveActual: false,
    mostrarNuevaClave: false,
    mostrarConfirmarClave: false,

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


    //VARIABLES DE Ver Campañas

    page: 1,
    itemsPerPage: 9,

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

    filtroNombre: null,
    filtroPlantilla: null,
    filtroCiudad: null,
    filtroSector: null,
    filtroCanal: 0,
    filtroFechaInicio: '',
    filtroFechaFin: '',
    dialogMetricasCampana: false,
    dialogGestionCampanas: false,
    donutChart: null,
    barChart: null,
    itemsCiudad: [],
    itemsSector: [],
    readOnlyCloseButton: true,
    chartsPending: 0,
    dialogCrearCampaña: false,
    dialogEditarCampañas: false,
    selectedNombreCampaña: null,
    selectedDetalleCampaña: null,
    selectedGuionCampaña: null,
    selectedUrlmediaCampaña: null,
    selectedMedioCampaña: null,
    isRefreshing: false,

    idRespuestaCampania: null,
    arrayArchivos: [],

    iframeChat: false,
    urlChat: '',
    estadoChat: false,
    celularSeleccionado: null,
    soundUrl2: 'https://glpi-siicsa.azurewebsites.net/notificacionSonido2.mp3',
    notificacionNueva: null,
    celularContacto: null,
    created() {
      window.addEventListener("message", (e) => this.recibirMensaje(e));
      this.headersVisibles = this.tablaHeaders.slice();
    },
    beforeDestroy() {
      window.removeEventListener("message", (e) => this.recibirMensaje(e));
    },
    selectedImagenCampaña: null,
    previewImagenCampana: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s',
    selectedImagenCampanaEditar: null,
    previewImagenCampanaEditar: null,

    modoDonutDetalle: 'interacciones',

    dialogCiudades: false,
    dialogSectores: false,

    dialogHistorialGeneral: false,
    busquedaFechaHistorialInicio: '',
    busquedaFechaHistorialFin: '',
    historialGeneral: [],
    canalFiltro: 0,

    dialogImagenAmpliada: false,
    imagenAmpliadaUrl: '',
    infoImagenPreview: null,

    searchProsp: '',
    menuFiltrosAvanzados: false,
    menuFiltrosAvanzadosDetalles: false,
    menuFiltrosAvanzadosDetalles2: false,
    filtroEstadoCampana: 'habilitadas', // o null

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

    selectedRespuesta: null,

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

    mensajesAlmacenados: [],
    expandedMessages: {},
    headersVisibles: [],

    plantillasCampanias: [
      { id: 1, nombre: 'CTA', nombre_llave: 'promocionar_productos_servicios' },
      { id: 2, nombre: 'Informativa', nombre_llave: 'boletin_informativo' },
    ]
  }),

  mounted() {

    this.baseURL = import.meta.env.VITE_API_BASE_URL; // URL base de la API
    this.idUsuario = localStorage.getItem("idUsuario");
    this.idCargo = localStorage.getItem("idCargo");
    this.nombreComercial =
      localStorage.getItem("nombreLogin") +
      " " +
      localStorage.getItem("apellidoLogin");
    this.correoUsuario = localStorage.getItem("correoUsuario");
    this.celularComercial = localStorage.getItem('celularLogin');
    this.imagenComercial = `${this.baseURL}images/${this.idUsuario}.jpeg?${Date.now()}`;
    window.addEventListener("message", this.recibirMensaje);
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

    // Metodos de Ver campañas
    this.cargarCampanas();
    this.setMenuActivoPorRuta();


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

    filtroNombre() { this.page = 1; },
    filtroPlantilla() { this.page = 1; },
    filtroCiudad() { this.page = 1; },
    filtroSector() { this.page = 1; },
    filtroFechaInicio() { this.page = 1; },
    filtroFechaFin() { this.page = 1; },
    itemsPerPage() { this.page = 1; },

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

    modoDonutDetalle() {
      if (this.dialogMetricasCampana) {
        this.renderDistribucion();
        setTimeout(() => {
          this.readOnlyCloseButton = false;
        }, 1300);
      }
    },

    dialogImagenAmpliada(val) {
      if (val && this.imagenAmpliadaUrl) {
        this.cargarInfoImagenPreview(this.imagenAmpliadaUrl);
      } else {
        this.infoImagenPreview = null;
      }
    },

    imagenAmpliadaUrl(val) {
      if (this.dialogImagenAmpliada && val) {
        this.cargarInfoImagenPreview(val);
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

  computed: {
    filtrosItems() {
      return {
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
        interes: 'v-select',
        fechaInicio: 'v-text-field',
        fechaFin: 'v-text-field',
        estado: 'v-select'
      };
    },
    filasEmpresas() {
      const columnas = 3;
      const filas = [];
      for (let i = 0; i < this.listaEmpresasComercial.length; i += columnas) {
        filas.push(this.listaEmpresasComercial.slice(i, i + columnas));
      }
      return filas;
    },

    totalPages() {
      return Math.ceil(this.filteredCampanas.length / this.itemsPerPage) || 1;
    },

    nombresCampanias() {
      const set = new Set(this.listaCampañas.map(c => c.nombre_campaña).filter(Boolean));
      return Array.from(set).sort((a, b) => a.localeCompare(b, 'es'));
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
      this.listaCampañas.forEach(c => {
        this._splitCiudades(c.ciudades).forEach(city => {
          const key = this._norm(city);
          if (!seen.has(key)) seen.set(key, city);
        });
      });
      return Array.from(seen.values())
        .sort((a, b) => a.localeCompare(b, 'es', { sensitivity: 'base' }));
    },


    filteredCampanas() {
      const toIsoDay = (d) => {
        const date = new Date(d);
        return isNaN(date) ? '' : date.toISOString().slice(0, 10);
      };

      let start = this.filtroFechaInicio || null;
      let end = this.filtroFechaFin || null;
      if (start && end && start > end) [start, end] = [end, start];

      const filtroCiudadNorm = this._norm(this.filtroCiudad);

      // Filtra campañas
      let arr = this.listaCampañas.filter(c => {
        const byName = this.filtroNombre
          ? this._norm(c.nombre_campaña).includes(this._norm(this.filtroNombre))
          : true;

        const bySector = this.filtroSector
          ? this._norm(c.sectores).includes(this._norm(this.filtroSector))
          : true;

        const byPlantilla = this.filtroPlantilla && this.filtroCanal == 1
          ? this._norm(c.plantilla_envio) === this._norm(this.filtroPlantilla.nombre_llave)
          : true;

        const byCiudad = this.filtroCiudad
          ? this._splitCiudades(c.ciudades)
            .some(city => this._norm(city).includes(filtroCiudadNorm))
          : true;

        const byCanal = this.filtroCanal && this.filtroCanal !== 0
          ? c.canal === this.filtroCanal
          : true;

        const f = toIsoDay(c.fecha);
        const byDateRange = (start ? f >= start : true) && (end ? f <= end : true);

        let byEstado = true;
        if (this.filtroEstadoCampana === 'habilitadas') {
          byEstado = c.activo === 1;
        } else if (this.filtroEstadoCampana === 'deshabilitadas') {
          byEstado = c.activo === 0;
        }

        return byName && byPlantilla && bySector && byCiudad && byDateRange && byCanal && byEstado;
      });

      // Ordena por fecha descendente (más recientes primero)
      arr = arr.slice().sort((a, b) => new Date(b.fecha) - new Date(a.fecha));

      return arr;
    },

    paginatedCampanas() {
      const start = (this.page - 1) * this.itemsPerPage;
      return this.filteredCampanas.slice(start, start + this.itemsPerPage);
    },

    distribucionDetalle() {
      const pos = Number(this.selectedCampana?.interes_positivo ?? 0);
      const neg = Number(this.selectedCampana?.interes_negativo ?? 0);
      const sin = Number(this.selectedCampana?.sin_respuesta ?? 0);
      const total = Math.max(pos + neg + sin, 0);

      const pct = (v) => total ? (v * 100 / total).toFixed(1) : '0.0';

      return [
        { key: 'pos', label: 'Interés Positivo', value: pos, pct: pct(pos), color: '#2e7d32', icon: 'mdi-lightbulb-on' },
        { key: 'neg', label: 'Interés Negativo', value: neg, pct: pct(neg), color: '#c62828', icon: 'mdi-cancel' },
        { key: 'sin', label: 'Sin Respuesta', value: sin, pct: pct(sin), color: '#1976d2', icon: 'mdi-check-all' },
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

    canalesFiltrados() {
      // Solo muestra los canales con eventos (o todos si filtro=0)
      const canales = [{ id: 0, nombre: 'Todos', color: '#888', icon: 'mdi-access-point' }, ...this.canalesYMedios];
      if (this.canalFiltro === 0) {
        return canales.filter(c => c.id !== 0 && (this.historialPorCanal[c.id]?.length || 0) > 0);
      }
      return canales.filter(c => c.id === this.canalFiltro);
    },


    historialGeneralFiltrado() {
      let arr = this.historialGeneral;
      if (this.canalFiltro && this.canalFiltro !== 0) {
        arr = arr.filter(item => Number(item.canal) === Number(this.canalFiltro));
      }
      if (this.buscadorHistorialGeneral) {
        const norm = this._norm(this.buscadorHistorialGeneral);
        arr = arr.filter(item =>
          this._norm(item.nombre_campaña || '').includes(norm) ||
          this._norm(item.descripcion || '').includes(norm)
        );
      }
      // Filtro por rango de fechas
      if (this.busquedaFechaHistorialInicio || this.busquedaFechaHistorialFin) {
        const inicio = this.busquedaFechaHistorialInicio;
        const fin = this.busquedaFechaHistorialFin;
        arr = arr.filter(item => {
          const fechaItem = item.fecha ? new Date(item.fecha) : null;
          if (!fechaItem || isNaN(fechaItem)) return false;
          const fechaIso = fechaItem.toISOString().slice(0, 10);
          return (!inicio || fechaIso >= inicio) && (!fin || fechaIso <= fin);
        });
      }
      return arr;
    },


    historialPorCanal() {
      // Agrupa los eventos filtrados por canal
      const map = {};
      for (const canal of this.canalesYMedios) {
        map[canal.id] = [];
      }
      for (const item of this.historialGeneralFiltrado) {
        if (map[item.canal]) map[item.canal].push(item);
      }
      return map;
    },

    historialCampanaCompleto() {
      // 1. Evento de creación de campaña
      const eventos = [];
      if (this.selectedCampana) {
        eventos.push({
          tipo: 'creacion',
          fecha: this.formatFecha2(this.selectedCampana.fecha),
          descripcion: `Se creó la campaña "${this.selectedCampana.nombre_campaña}"`,
          estado: null,
          icon: 'mdi-calendar-plus',
          color: '#1976d2',
          contacto: null,
          ciudad: this.selectedCampana.ciudades,
        });
      }
      // 2. Respuestas de campaña
      if (Array.isArray(this.selectedCampanaResponses)) {
        this.selectedCampanaResponses.forEach(resp => {
          eventos.push({
            tipo: 'respuesta',
            fecha: this.formatFecha2(resp.fecha_envio || resp.fecha),
            descripcion: `Respuesta de ${resp.nombre_contacto || '—'} (${resp.nombre_ciudad || '—'})`,
            estado: resp.estado,
            icon: resp.estado === 3 ? 'mdi-check-circle' : resp.estado === 2 ? 'mdi-progress-clock' : 'mdi-email',
            color: resp.estado === 3 ? '#22C55E' : resp.estado === 2 ? '#e39005' : '#1976d2',
            contacto: resp.nombre_contacto,
            ciudad: resp.nombre_ciudad,
            interes: this.interesLabel(resp.interes),
          });
        });
      }
      // Ordenar por fecha descendente (opcional)
      return eventos.sort((a, b) => new Date(b.fecha) - new Date(a.fecha));
    },

    sectoresCampanaRespuestas() {
      // Devuelve solo los sectores presentes en las respuestas
      const set = new Set();
      (this.selectedCampanaResponses || []).forEach(r => {
        if (r.nombre_sector) set.add(r.nombre_sector.trim());
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

    entregadasCampanaRespuestas() {
      return [
        { text: 'Entregadas', value: 'entregada' },
        { text: 'No Entregadas', value: 'no_entregada' }
      ];
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
      // Filtra por estado
      if (this.filtroEstadoMetricas) {
        arr = arr.filter(r => String(r.estado) === String(this.filtroEstadoMetricas));
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

  methods: {
    // Actualizar imagen del usuario cuando cambia desde AppHeader
    actualizarImagen(nuevaUrl) {
      this.imagenComercial = nuevaUrl;
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

    cambiarImagen() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/jpeg';

      input.onchange = async (event) => {
        const file = event.target.files[0];
        if (file) {
          const formData = new FormData();
          const nombre = `${this.comercialId}.jpeg`;
          formData.append('imagen', file);
          formData.append('nombre_archivo', nombre);

          try {
            await axios.post(this.baseURL + 'api/subir-imagen', formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            });

            // Forzar recarga para evitar caché
            this.imagenComercial = `/images/${this.comercialId}.jpeg?${Date.now()}`;
            this.mensajeAlertLogin = 'Imagen actualizada correctamente, si no puedes vizualizarla, recarga la página.';
            this.alerta = true;
            this.ifCargando = false;
          } catch (error) {
            console.error('❌ Error al subir imagen:', error);
          }
        }
      };

      input.click();
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

    irPendientes() {
      this.$router.push('/pendiente');
    },

    irEnviarCampana() {
      this.$router.push('/campana');
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

    irGaleriaCampanas() {
      this.$router.push('/VerCampanas');
    },

    irEmpresas() {
      this.$router.push('/empresas');
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
    //-------------------------- METODOS DE VER VISTA CAMPAÑA-------------------------

    irCrearCampanas() {
      this.dialogCrearCampaña = true;
    },

    irEditarCampanas(idCampana) {
      this.selectedCampana = this.listaCampañas.find(c => c.id === idCampana)
      this.dialogEditarCampañas = true;

      axios.post(this.baseURL + 'api/infoCampania', {
        idCampania: idCampana
      })
        .then(response => {
          console.log('DATOS DE:', response.data.data);
          this.selectedNombreCampaña = response.data.data[0].nombre;
          this.selectedDetalleCampaña = response.data.data[0].detalle;
          this.selectedGuionCampaña = response.data.data[0].guion;
          this.selectedUrlmediaCampaña = response.data.data[0].url_media;
          this.selectedMedioCampaña = response.data.data[0].tipo;
          //this.listaCampañas = response.data.data;

        }).catch(error => {
          console.error('Error al cargar las campañas:', error);
        });
      this.previewImagenCampanaEditar = this.selectedCampana?.url_media || null;
      this.selectedImagenCampanaEditar = null;
    },

    cargarCampanas() {
      axios.post(this.baseURL + "/api/registros", {
        idUsuario: this.idUsuario,
      })
        .then((response) => {
          console.log("Datos cargados:", response.data.data);
        })
        .catch((error) => {
          console.error("Error al cargar los datos:", error);
        });
      axios.post(this.baseURL + 'api/informesCampanias', {
        idUsuario: this.idUsuario
      })
        .then(response => {
          this.listaCampañas = response.data.data
          console.log('Datos cargados CAMPAÑIA:', response.data.data);

        }).catch(error => {
          console.error('Error al cargar las campañas:', error);
        });
    },

    seleccionarCampana(idCampana) {
      this.selectedCampana = this.listaCampañas.find(c => c.id === idCampana)
    },

    verDetallesCampana(idCampana) {
      this.idCampaniaSeleccionada = idCampana;
      // Busca el item y abre el diálogo
      this.selectedCampana = this.listaCampañas.find(c => c.id === idCampana) || null;

      this.sectoresDialog = (this.selectedCampana?.sectores || '').split(',').map(s => s.trim()).filter(Boolean);
      this.ciudadesDialog = this._splitCiudades(this.selectedCampana?.ciudades);


      axios.post(this.baseURL + '/api/CampaniasEnviadasDetalle', {
        idCampania: idCampana
      })
        .then(response => {
          console.log('api/CampaniasEnviadasDetalle response:', response.data);
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

    formatFecha(value) {
      if (!value) return '—';
      const d = new Date(value);
      if (isNaN(d)) return '—';
      return d.toLocaleDateString('es-CO', { day: '2-digit', month: 'long', year: 'numeric' });
    },

    formatFecha2(fecha) {
      const date = new Date(fecha);
      const day = String(date.getUTCDate()).padStart(2, '0');
      const month = String(date.getUTCMonth() + 1).padStart(2, '0');
      const year = date.getUTCFullYear();
      const hours = String(date.getUTCHours()).padStart(2, '0');
      const minutes = String(date.getUTCMinutes()).padStart(2, '0');
      return `${day}/${month}/${year} ${hours}:${minutes}`;
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

    numero(n) {
      const v = Number(n ?? 0);
      return isNaN(v) ? '0' : v.toLocaleString('es-CO');
    },

    porcentaje(p) {
      if (p === null || p === undefined || isNaN(Number(p))) return '0%';
      return `${Number(p).toFixed(0)}%`;
    },

    totalEnvios(c) {
      if (!c) return 0;
      const pos = Number(c.interes_positivo ?? 0);
      const neg = Number(c.interes_negativo ?? 0);
      const sin = Number(c.sin_respuesta ?? 0);
      return pos + neg + sin;
    },


    // DATOS DE LA CAMPAÑA

    destroyDonut() {
      if (this.donutChart) {
        this.donutChart.destroy();
        this.donutChart = null;
      }
    },

    renderDistribucion() {
      // Limpia instancia previa
      this.destroyDonut();

      this.readOnlyCloseButton = true;
      const ctx = this.$refs.donutCanvas?.getContext('2d');
      if (!ctx) return;

      // Obtén los datos correctos según el canal
      const { labels, data, colors } = this.getDonutMetricasFiltradas();

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

    abrirGestion(row) {
      this.selectedRespuesta = row;
      console.log("ROW RESPUESTA", this.selectedRespuesta);

      if (row?.id) this.cargarHistorial(row.id);

      // Abrir el diálogo
      setTimeout(() => {
        this.dialogGestionCampanas = true;
      }, 100);
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

    rechazadoLabel(id) {
      const m = { 1: 'Rechazado', 0: 'Entregado' };
      return m[Number(id)] ?? `Estado ${id}`;
    },
    estadoColor(id) {
      if (id == 1) return '#4caf50'; // Verde Nuevo
      if (id == 2) return '#2196f3'; // Azul En proceso
      if (id == 3) return '#f44336'; // Rojo Resuelto
      return '#ff9800'; // Naranja default
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
    closeDialogMetricas() {
      // Limpiar recursos antes de cerrar
      this.teardownCharts(); // 👈 destruye instancias de Chart.js
      this.selectedCampana = null;

      // Luego cerrar el diálogo
      this.dialogMetricasCampana = false;
      this.iframeChat = false;
      this.limpiarFiltrosMetricas();
    },

    teardownCharts() {
      try { this.barChart?.stop(); this.barChart?.destroy(); } catch { }
      try { this.donutChart?.stop(); this.donutChart?.destroy(); } catch { }
      this.barChart = null;
      this.donutChart = null;
    },

    // quita acentos, baja a minúsculas, colapsa espacios
    _norm(s) {
      return (s ?? '')
        .toString()
        .normalize('NFD').replace(/\p{Diacritic}/gu, '')
        .toLowerCase()
        .replace(/\s+/g, ' ')
        .trim();
    },

    // separa ciudades de un string y corrige "Bogotá, D.C."
    _splitCiudades(str) {
      if (!str) return [];
      const safe = str.replace(/bogotá,\s*d\.c\./gi, 'Bogotá D.C.'); // proteger nombre
      return safe
        .split(',')
        .map(s => s.trim())
        .filter(Boolean);
    },

    cerrarFormularioCampaña() {
      this.dialogCrearCampaña = false;
      this.selectedNombreCampaña = null;
      this.selectedDetalleCampaña = null;
      this.selectedGuionCampaña = null;
      this.selectedImagenCampaña = null;
      this.previewImagenCampana = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s";
      this.validandoActividad = false;
    },

    cerrarFormularioEditarCampaña() {
      this.dialogEditarCampañas = false;
      this.selectedNombreCampaña = null;
      this.selectedDetalleCampaña = null;
      this.selectedGuionCampaña = null;
      this.validandoActividad = false;
    },

    GuardarFormularioCampaña() {
      this.validandoActividad = true;

      if (!this.selectedNombreCampaña?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el nombre de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (!this.selectedDetalleCampaña?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el detalle de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (!this.selectedGuionCampaña?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el guion de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }
      let formImage = new FormData();
      axios.post(this.baseURL + '/api/CrearCampania', {
        'nombre': this.selectedNombreCampaña,
        'detalle': this.selectedDetalleCampaña,
        'guion': this.selectedGuionCampaña,
        'idusu': localStorage.getItem('idUsuario'),
        'canal': 1,
        'idCampania': 0, // 0 Para crear
        'tipo': 0, // 0 Para crear
        'url_media': '',
        'canal': this.selectedMedioCampaña,
      })
        .then(response => {
          // Si hay imagen, subirla con el id de la campaña creada
          const idCampania = response?.data?.data?.[0]?.id || response?.data?.data?.[0]?.idCampania;
          if (this.selectedImagenCampaña && idCampania) {
            const formImage = new FormData();
            formImage.append('files', this.selectedImagenCampaña);
            formImage.append('id', idCampania);

            return axios.post(this.baseURL + '/api/uploadfileblobMediaCampania', formImage, {
              headers: { 'Content-Type': 'multipart/form-data' }
            });
          }
          console.log("Formulario Campaña: " + formImage)
          return null;
        })
        .then(() => {
          this.cerrarFormularioCampaña();
          this.cargarCampanas();
          this.mensajeAlertLogin = 'Campaña Creada Exitosamente.';
          this.alerta = true;
          this.validandoActividad = false;
        })
        .catch(error => {
          console.error('Error al crear campaña:', error);
          this.mensajeAlertLogin = 'Error al crear la campaña.';
          this.alerta = true;
          this.validandoActividad = false;
        });

    },

    //EDITAR CAMPAÑAA

    EditarFormularioCampaña(idCampania) {
      this.validandoActividad = true;

      if (!this.selectedNombreCampaña?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el nombre de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (!this.selectedDetalleCampaña?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el detalle de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }

      if (!this.selectedGuionCampaña?.trim()) {
        this.mensajeAlertLogin = 'Por favor, Digite el guion de la Campaña.';
        this.alerta = true;
        this.validandoActividad = false;
        return;
      }
      console.log("IdCampania: " + idCampania)

      let formImage = new FormData();
      axios.post(this.baseURL + '/api/CrearCampania', {
        'nombre': this.selectedNombreCampaña,
        'detalle': this.selectedDetalleCampaña,
        'guion': this.selectedGuionCampaña,
        'idusu': localStorage.getItem('idUsuario'),
        'idCampania': idCampania,
        'tipo': 1, // 1 Para Editar,
        'canal': this.selectedMedioCampaña,
        'url_media': this.selectedUrlmediaCampaña,
      })
        .then(response => {
          // 2. Si hay nueva imagen, subirla con el id de la campaña editada
          if (this.selectedImagenCampanaEditar && idCampania) {
            const formImage = new FormData();
            formImage.append('files', this.selectedImagenCampanaEditar);
            formImage.append('id', idCampania);

            return axios.post(this.baseURL + '/api/saveCampaniasMedia', formImage, {
              headers: { 'Content-Type': 'multipart/form-data' }
            });
          }
          return null;
        })
        .then(() => {
          this.cerrarFormularioEditarCampaña();
          this.cargarCampanas();
          this.mensajeAlertLogin = 'Campaña Editada Exitosamente.';
          this.alerta = true;
          this.validandoActividad = false;
        })
        .catch(error => {
          console.error('Error al editar campaña:', error);
          this.mensajeAlertLogin = 'Error al editar la campaña.';
          this.alerta = true;
          this.validandoActividad = false;
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
                  this.cargarCampanas();
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
              this.cargarCampanas();
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
          this.cargarCampanas();
          if (this.selectedRespuesta?.id) {
            setTimeout(() => {
              this.cargarHistorial(this.selectedRespuesta.id);
            }, 600);
          }
        });
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

    _toLocalIsoDay(d) {
      const y = d.getFullYear();
      const m = String(d.getMonth() + 1).padStart(2, '0');
      const day = String(d.getDate()).padStart(2, '0');
      return `${y}-${m}-${day}`; // YYYY-MM-DD (hora local)
    },

    cambiarImagen() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/jpeg';

      input.onchange = async (event) => {
        const file = event.target.files[0];
        if (file) {
          const formData = new FormData();
          const nombre = `${this.comercialId}.jpeg`;
          formData.append('imagen', file);
          formData.append('nombre_archivo', nombre);

          try {
            await axios.post(this.baseURL + 'api/subir-imagen', formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            });

            // Forzar recarga para evitar caché
            this.imagenComercial = `/images/${this.comercialId}.jpeg?${Date.now()}`;
            this.mensajeAlertLogin = 'Imagen actualizada correctamente, si no puedes vizualizarla, recarga la página.';
            this.alerta = true;
            this.ifCargando = false;
          } catch (error) {
            console.error('❌ Error al subir imagen:', error);
          }
        }
      };

      input.click();
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

    mostrarCiudades(ciudadesStr) {
      // Usa _splitCiudades para unir Bogotá D.C.
      if (!ciudadesStr) return [];
      const arr = this._splitCiudades(ciudadesStr);
      return arr.slice(0, 6);
    },
    ciudadesRestantes(ciudadesStr) {
      if (!ciudadesStr) return [];
      const arr = this._splitCiudades(ciudadesStr);
      return arr.length > 6 ? arr.slice(6) : [];
    },

    getCanalInfo(canal) {
      // canal puede ser id (número) o nombre (string)
      if (typeof canal === 'number') {
        return this.canalesYMedios.find(c => c.id === canal) || {};
      }
      return this.canalesYMedios.find(c => c.nombre === canal) || {};
    },

    getMetricasCardCampana(campana) {
      // Telefónico
      if (campana.canal === 2) {
        return [
          { icon: 'mdi-phone', color: '#1565c0', label: 'Total llamadas', value: campana.total_llamadas ?? 0 },
          { icon: 'mdi-account-check', color: '#19bf56', label: 'Efectivas c/Lead', value: campana.efectivas_con_lead ?? campana.efectivo_con_lead ?? 0 },
          { icon: 'mdi-account-plus', color: '#3f94e8', label: 'Efectivas s/Lead', value: campana.efectivas_sin_lead ?? campana.efectivo_sin_lead ?? 0 },
          { icon: 'mdi-account-cancel', color: '#de8d04', label: 'No efectivas', value: campana.no_efectivas ?? campana.no_efectivo ?? 0 },
        ];
      }
      // WhatsApp
      if (campana.canal === 1) {
        if (campana.plantilla_envio == 'promocionar_productos_servicios') {
          return [
            { icon: 'mdi-check-all', color: '#19bf56', label: 'Entregadas', value: campana.entregadas + campana.leidas },
            { icon: 'mdi-check', color: '#db3030', label: 'No Entregadas', value: campana.enviadas },
            { icon: 'mdi-cancel', color: '#de8d04', label: 'No Existe', value: campana.fallidas },
            { icon: 'mdi-thumb-up', color: '#22C55E', label: 'Interés positivo', value: campana.interes_positivo ?? 0 },
            { icon: 'mdi-thumb-down', color: '#d95323', label: 'Interés negativo', value: campana.interes_negativo ?? 0 },
            { icon: 'mdi-help-circle-outline', color: '#454a52', label: 'Sin respuesta', value: campana.sin_respuesta ?? 0 },
          ];
        } else {
          return [
            { icon: 'mdi-check-all', color: '#19bf56', label: 'Entregadas', value: campana.entregadas + campana.leidas },
            { icon: 'mdi-check', color: '#db3030', label: 'No Entregadas', value: campana.enviadas },
            { icon: 'mdi-cancel', color: '#de8d04', label: 'No Existe', value: campana.fallidas },
          ];
        }

      }
      // Email
      if (campana.canal === 3) {
        return [
          { icon: 'mdi-check-circle', color: '#19bf56', label: 'Entregadas', value: campana.entregadas ?? 0 },
          { icon: 'mdi-cancel', color: '#de8d04', label: 'No Recibidas', value: campana.no_entregadas ?? 0 },
          { icon: 'mdi-email-check', color: '#3f94e8', label: 'Con respuesta', value: campana.con_respuesta ?? 0 },
          { icon: 'mdi-help-circle-outline', color: '#454a52', label: 'Sin respuesta', value: campana.sin_respuesta ?? 0 },
        ];
      }
      // Default: solo interés positivo/negativo/sin respuesta
      return [
        { icon: 'mdi-lightbulb-on-10', color: '#004D40', label: 'Interés Positivo', value: campana.interes_positivo ?? 0 },
        { icon: 'mdi-cancel', color: '#D50000', label: 'Interés Negativo', value: campana.interes_negativo ?? 0 },
        { icon: 'mdi-check-all', color: '#00B0FF', label: 'Sin respuesta', value: campana.sin_respuesta ?? 0 },
      ];
    },

    canalNombre(id) {
      if (id === 1) return 'WhatsApp';
      if (id === 2) return 'Telefónico';
      if (id === 3) return 'Email';
      return '—';
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
            labels: ['Entregadas', 'No Recibidas'],
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

    onImagenCampanaChange(e) {
      const file = e.target.files[0];
      if (file) {
        // Validar tamaño (puedes ajustar el límite para videos si lo deseas)
        if (file.size > 14 * 1024 * 1024) { // 14MB para videos, ajusta si quieres
          this.mensajeAlertLogin = 'El archivo debe ser menor a 14MB.';
          this.alerta = true;
          this.selectedImagenCampaña = null;
          this.previewImagenCampana = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s";
          return;
        }
        this.selectedImagenCampaña = file;

        // Si es imagen, previsualiza normalmente
        if (file.type.startsWith('image/')) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            this.previewImagenCampana = ev.target.result;
          };
          reader.readAsDataURL(file);
        }
        // Si es video, genera preview del primer frame
        else if (file.type.startsWith('video/')) {
          const video = document.createElement('video');
          video.preload = 'metadata';
          video.muted = true;
          video.src = URL.createObjectURL(file);

          video.onloadeddata = () => {
            // Captura el primer frame
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            this.previewImagenCampana = canvas.toDataURL('image/png');
            URL.revokeObjectURL(video.src);
          };
          video.onerror = () => {
            this.previewImagenCampana = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSckB0rNNsHn82Ve8LCWttG4OYHuRMg7bMvSQ&s";
            URL.revokeObjectURL(video.src);
          };
        }
      }
    },

    onImagenCampanaEditarChange(e) {
      const file = e.target.files[0];
      if (file) {
        if (file.size > 14 * 1024 * 1024) { // 14MB para videos
          this.mensajeAlertLogin = 'El archivo debe ser menor a 14MB.';
          this.alerta = true;
          this.selectedImagenCampanaEditar = null;
          this.previewImagenCampanaEditar = null;
          return;
        }
        this.selectedImagenCampanaEditar = file;

        if (file.type.startsWith('image/')) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            this.previewImagenCampanaEditar = ev.target.result;
          };
          reader.readAsDataURL(file);
        } else if (file.type.startsWith('video/')) {
          const video = document.createElement('video');
          video.preload = 'metadata';
          video.muted = true;
          video.src = URL.createObjectURL(file);

          video.onloadeddata = () => {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            this.previewImagenCampanaEditar = canvas.toDataURL('image/png');
            URL.revokeObjectURL(video.src);
          };
          video.onerror = () => {
            this.previewImagenCampanaEditar = null;
            URL.revokeObjectURL(video.src);
          };
        }
      }
    },

    esVideo(val) {
      if (!val) return false;
      // Si es un File, revisa el tipo
      if (typeof val === 'object' && val.type) return val.type.startsWith('video/');
      // Si es string (url o nombre), revisa la extensión
      return /\.(mp4|webm|ogg|mov|avi|mkv)(\?|$)/i.test(val);
    },

    itemTipoLabel(item) {
      if (item.tipo === 'creacion') return 'Campaña creada';
      if (item.tipo === 'modificacion') return 'Campaña modificada';
      if (item.tipo === 'respuesta') return 'Respuesta registrada';
      if (item.tipo === 'envio') return 'Envío realizado';
      return item.tipo || 'Evento';
    },
    itemColor(item) {
      if (item.tipo === 'creacion') return '#22C55E';
      if (item.tipo === 'modificacion') return '#e39005';
      if (item.tipo === 'respuesta') return '#1976d2';
      if (item.tipo === 'envio') return '#6c4ee6';
      return '#888';
    },
    itemIcon(item) {
      if (item.tipo === 'creacion') return 'mdi-plus-circle';
      if (item.tipo === 'modificacion') return 'mdi-pencil';
      if (item.tipo === 'respuesta') return 'mdi-message-reply-text';
      if (item.tipo === 'envio') return 'mdi-send-check';
      return 'mdi-alert-circle-outline';
    },

    abrirDialogHistorialGeneral() {
      this.dialogHistorialGeneral = true;
      this.buscadorHistorialGeneral = '';
      this.canalFiltro = 0;
      this.historialGeneral = [];

      // Cargar campañas y respuestas
      axios.post(this.baseURL + '/api/informesCampanias', {
        idUsuario: this.idUsuario
      })
        .then(async response => {
          const campanias = response.data.data || [];
          let historial = [];

          // Para cada campaña, agrega evento de creación y carga respuestas
          for (const camp of campanias) {
            // Evento de creación de campaña
            historial.push({
              tipo: 'creacion',
              fecha: camp.fecha_creacion || camp.fecha,
              descripcion: `Se creó la campaña "${camp.nombre_campaña}"`,
              nombre_campaña: camp.nombre_campaña,
              canal: camp.canal,
              color: '#1976d2',
              icon: 'mdi-calendar-plus',
              ciudad: camp.ciudades,
            });

            // Evento de modificación si aplica
            if (
              camp.fecha_modificacion &&
              new Date(camp.fecha_modificacion) > new Date(camp.fecha_creacion || camp.fecha)
            ) {
              historial.push({
                tipo: 'modificacion',
                fecha: camp.fecha_modificacion,
                descripcion: `Se editó la campaña "${camp.nombre_campaña}"`,
                nombre_campaña: camp.nombre_campaña,
                canal: camp.canal,
                color: '#e39005',
                icon: 'mdi-pencil',
                ciudad: camp.ciudades,
              });
            }

            // Cargar respuestas de la campaña
            try {
              const resp = await axios.post(this.baseURL + '/api/CampaniasEnviadasDetalle', {
                idCampania: camp.id
              });
              const respuestas = resp.data.data || [];
              respuestas.forEach(r => {
                let icon = 'mdi-help-circle-outline';
                let color = '#454a52';
                if (r.interes === 1) { // Positivo
                  icon = 'mdi-thumb-up';
                  color = '#22C55E';
                } else if (r.interes === 2) { // Negativo
                  icon = 'mdi-thumb-down';
                  color = '#d95323';
                }
                historial.push({
                  tipo: 'respuesta',
                  fecha: r.fecha_envio || r.fecha,
                  descripcion: `Respuesta de ${r.nombre_contacto || '—'} (${r.nombre_ciudad || '—'})`,
                  nombre_campaña: camp.nombre_campaña,
                  canal: camp.canal,
                  color,
                  icon,
                  ciudad: r.nombre_ciudad,
                  interes: this.interesLabel(r.interes),
                });
              });
            } catch (e) {
              // Si falla la carga de respuestas, solo muestra la campaña
            }
          }

          // Ordena por fecha descendente
          this.historialGeneral = historial.sort((a, b) => new Date(b.fecha) - new Date(a.fecha));
        })
        .catch(error => {
          console.error('Error al cargar historial general:', error);
          this.historialGeneral = [];
        });
    },

    limpiarCamposHistorial() {
      this.canalFiltro = null;
      this.buscadorHistorialGeneral = '';
    },

    abrirImagenAmpliada(url) {
      this.imagenAmpliadaUrl = url;
      this.dialogImagenAmpliada = true;
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
        // Si tienes el archivo original, puedes obtener el tamaño real
        let format = '';
        let size = '';
        if (url.startsWith('blob:')) {
          format = 'Desconocido';
          size = 'Desconocido';
        } else {
          const ext = url.split('.').pop().split('?')[0].toUpperCase();
          format = ext.length <= 5 ? ext : 'Desconocido';
          size = 'Desconocido';
        }
        this.infoImagenPreview = {
          width: img.naturalWidth,
          height: img.naturalHeight,
          format,
          size
        };
      };
      img.src = url;
    },

    limpiarFiltroSectoresYCiudades() {
      this.searchProsp = '';
    },

    async toggleEstadoCampana(campana) {
      this.isRefreshing = true;
      try {
        // Prepara todos los datos requeridos para editar
        await axios.post(this.baseURL + '/api/CrearCampania', {
          nombre: campana.nombre_campaña,
          detalle: campana.detalle_campaña,
          guion: campana.guion || '',
          idusu: this.idUsuario,
          idCampania: campana.id,
          tipo: 1, // 1 = Editar
          canal: campana.canal,
          activo: campana.activo === 1 ? 0 : 1, // Cambia el estado
          url_media: campana.url_media || '',

        });
        campana.activo = campana.activo === 1 ? 0 : 1; // Actualiza localmente
        this.mensajeAlertLogin = campana.activo === 1
          ? '¡Campaña habilitada!'
          : '¡Campaña deshabilitada!';
        this.alerta = true;
      } catch (e) {
        this.mensajeAlertLogin = 'Error al cambiar el estado de la campaña.';
        this.alerta = true;
      }
      this.isRefreshing = false;
    },

    setFiltrosPorDefecto() {
      this.filtroPlantilla = null;
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

    reenviarCampana(campana) {
      // Guarda la info relevante en localStorage
      if (campana.activo === 0) {
        this.mensajeAlertLogin = 'No puedes reenviar una campaña deshabilitada.';
        this.alerta = true;
        return;
      }
      localStorage.setItem('campanaReenviar', JSON.stringify({
        id: campana.id,
        nombre: campana.nombre_campaña,
        detalle: campana.detalle_campaña,
        guion: campana.guion,
        url_media: campana.url_media,
        tipo: campana.tipo,
        canal: campana.canal,
        plantilla_envio: campana.plantilla_envio,
        filtrosEnvio: campana.filtrosEnvio,
        numeros_manual: campana.numerosManuales,
      }));
      localStorage.setItem('reenviarUnaCampaña', 'true');
      this.$router.push('/campana');
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

    formatFechaCorta(fecha) {
      if (!fecha) return '—';
      const date = new Date(fecha);
      if (isNaN(date)) return '—';
      const day = String(date.getUTCDate()).padStart(2, '0');
      const month = String(date.getUTCMonth() + 1).padStart(2, '0');
      const year = date.getUTCFullYear();
      let hours = date.getUTCHours();
      const minutes = String(date.getUTCMinutes()).padStart(2, '0');
      const ampm = hours >= 12 ? 'PM' : 'AM';
      hours = hours % 12;
      hours = hours ? hours : 12; // 0 -> 12
      const strHours = String(hours).padStart(2, '0');
      return `${day}/${month}/${year} ${strHours}:${minutes} ${ampm}`;
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


  }
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

.page-title {
  /* alto contraste sobre fondo blanco */
  color: rgba(0, 0, 0, 0.87);
  letter-spacing: -0.25px;
  line-height: 1.2;
}

/* Igualamos el “input” de Rango de fechas a la altura de los fields */
.input-btn {
  height: 44px;
  /* coincide con density="comfortable" */
  border-radius: 12px !important;
  padding-inline: 16px !important;
}

/* Borde suave como en el diseño */
.soft-divider {
  opacity: .3;
}

/* Responsive: en móvil los controles ocupan todo el ancho */
@media (max-width: 600px) {
  .filter-chip {
    min-width: 100%;
  }
}

.cards-container {
  width: 100%;
}

/* Card y layout */
.campaign-card {
  transition: box-shadow .2s ease;
  height: 100%;
  /* para que todas sean iguales en la fila */
  width: 100%;
}

.campaign-card:hover {
  box-shadow: 0 10px 28px rgba(0, 0, 0, .08);
}

.thumb {
  background: #f5f6f7;
  flex: 0 0 auto;
}

.label {
  color: rgba(0, 0, 0);
  margin-right: 6px;
  font-size: 0.9rem;
}

.lh-tight {
  line-height: 1.15;
}

.filter-chip {
  border-radius: 12px;
  background: #fff;
}

.min-160 {
  min-width: 160px;
}

@media (max-width: 600px) {
  .thumb {
    width: 96px !important;
    height: 128px !important;
  }
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

.refresh-btn {
  color: #00277d !important;
  /* Azul oscuro similar al mock */
}

.v-btn--outlined.btn-details {
  border-color: #00277d;
  /* Borde del mismo color del texto */
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

.v-data-table td[data-test="td-total"],
.v-data-table td[data-test="td-total"] .th-content,
.v-data-table td:last-child .th-content {
  color: #0a1c3a !important;
  font-weight: 700 !important;
  font-size: 0.98rem !important;
  letter-spacing: 0.1px !important;
}

.th-content {
  align-items: center;
  gap: 6px;
  font-weight: 700;
  color: #0a1c3a;
  font-size: 0.98rem;
  letter-spacing: 0.1px;
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

.row-rechazado {
  background-color: rgba(220, 38, 38, 0.08) !important;
  /* rojo con mucha opacidad */
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
