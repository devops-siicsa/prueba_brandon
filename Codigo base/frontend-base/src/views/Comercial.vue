<template>
  <v-app>
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

            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/comercial' }" style="color: white;">
              <v-icon icon="mdi mdi-home-account" color="white" prepend-icon></v-icon>
              Comercial
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irContactos()" link v-if="idCargo == '2'">

          <v-list-item-content>

            <v-list-item-title style="color: white;">
              <v-icon icon="mdi-contacts" color="white" prepend-icon></v-icon>
              Contactos Mercadeo
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-item @click="irPendientesGeneral()" link v-if="idCargo == '3'">

          <v-list-item-content>

            <v-list-item-title :class="{ 'menu-item-activo': menuActivo === '/pendiente-general' }" style="color: white;">
              <v-icon icon="mdi-format-list-checks" color="white" prepend-icon></v-icon>
              Pendientes
            </v-list-item-title>
          </v-list-item-content>

        </v-list-item>

        <v-list-group value="Campañas" v-if="idCargo == '2'">
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" prepend-icon="mdi-bell-cog" title="Campañas" active></v-list-item>
          </template>

          <v-list-item @click="irCampañas()" link>

            <v-list-item-content>

              <v-list-item-title style="color: white;">
                <v-icon icon="mdi-bell" color="white" prepend-icon></v-icon>
                Ver Campañas
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irInformesCampañas()" link>

            <v-list-item-content>

              <v-list-item-title style="color: white;">
                <v-icon icon="mdi-chart-bell-curve-cumulative" color="white" prepend-icon></v-icon>
                Informes
              </v-list-item-title>
            </v-list-item-content>

          </v-list-item>

          <v-list-item @click="irGaleriaCampanas()" link>

            <v-list-item-content class="list-item-compact">

              <v-list-item-title style="color: white;">
                <v-icon icon="mdi mdi-view-gallery-outline" color="white" prepend-icon></v-icon>
                Ver Galería de Campañas
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

            <v-list-item-title  :class="{ 'menu-item-activo': menuActivo === '/pedidos' }" style="color: white;">
              <v-icon class="mr-2" size="small"  icon="mdi mdi-package-variant" color="white" prepend-icon></v-icon>
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

    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
        <v-row style="height: 100%;">
          <!-- Sidebar izquierda -->
          <v-col cols="3">
            <v-card style="overflow-y: auto; height: 85vh;" class="pa-4 scroll-custom">
              <div class="pa-3 mb-4 rounded" style="background-color: #1976D2; color: white;">
                <div class="text-h6 text-center">¡Bienvenido(a)!</div>
              </div>
              <div>
                <div class="text-center align-center justify-center">
                  <v-avatar size="150" class="mb-2">
                    <v-img :src="`${this.baseURL}images/${comercialId}.jpeg?${Date.now()}`" />
                  </v-avatar>
                  <div class="text-h6">{{ nombreComercial }}</div>
                </div>
                <div class="d-flex justify-space-between align-center mt-4">
                  <div class="text-subtitle-2">Meta mensual</div>
                  <div class="text-h5 font-weight-bold">${{ ctaMetaMensual.toLocaleString() }}</div>
                </div>
                <v-progress-linear :model-value="progress" height="25" color="blue" rounded class="my-2 progress-label">
                  <template v-slot:default>
                    <div class="label-text">{{ (porcMetaMensual * 100).toFixed(0) }}%</div>
                  </template>
                </v-progress-linear>

                <!-- Cambios Angelo -->
                <div class="d-flex justify-center mt-4">
              <div class="mt-3 mb-4">
                <template v-if="this.cantidadPendientes > 0">
                  <v-card elevation="3" class="pa-4" style="max-width: 350px; border-radius: 16px;">
                    <div class="d-flex align-center mb-2">
                      <v-icon color="#1976D2" size="32">mdi-calendar-month</v-icon>
                      <span class="ml-2 font-weight-bold" style="font-size: 1.1rem;">Pendientes</span>
                    </div>
                    <div class="mb-2" style="color: #666; font-size: 1.05rem;">
                      Tienes <span class="font-weight-bold">{{ this.cantidadPendientes }}</span> actividades pendientes por realizar.
                    </div>
                    <v-btn color="blue" block rounded @click="irPendientesGeneral()" prepend-icon="mdi-calendar-month" style="font-size: 0.82rem">
                      Ir a Pendientes
                    </v-btn>
                  </v-card>
                </template>
                <template v-else>
                  <v-card elevation="3" class="pa-4" style="max-width: 320px; border-radius: 16px;">
                    <div class="d-flex align-center mb-2">
                      <v-icon color="#43a047" size="32">mdi-thumb-up</v-icon>
                      <span class="ml-2 font-weight-bold" style="font-size: 1.1rem;">¡Sin pendientes!</span>
                    </div>
                    <div class="mb-2" style="color: #666;">
                      No se tienen actividades pendientes. ¡Buen trabajo!
                    </div>
                    <v-btn color="blue" block rounded @click="irPendientesGeneral()" prepend-icon="mdi-calendar-month">
                      Ir a Calendario
                    </v-btn>
                  </v-card>
                </template>
              </div>
                
              </div>
                <!-- Cambios Angelo -->
              </div>

              <div>
                <v-btn @click="dialogNuevaOportunidad = true"  class="mt-4 btn-grow-card" block rounded color="blue"
                  prepend-icon="mdi-plus-box" style="font-size: 0.82rem">
                  Nueva oportunidad
                </v-btn>
                <v-btn @click="abrirFormularioProspecto()" class="mt-2 btn-grow-card" block rounded color="blue"
                  prepend-icon="mdi-account" style="font-size: 0.82rem">
                  Nuevo Prospecto
                </v-btn>
                <v-btn class="mt-2 btn-grow-card" block rounded color="blue" prepend-icon="mdi-send" style="font-size: 0.82rem">
                  Enviar cotización
                </v-btn>
              </div>
            </v-card>
          </v-col>

          <!-- Panel derecho -->
          <v-col style="overflow-y: auto; height: 100%;">
            <div class="d-flex align-center mb-7" style="color: #666;">
              <span class="text-h6" style="margin-right: 24px;">Módulo Comercial</span>
              <div style="display: flex; gap: 12px;">
                <v-tooltip location="top" :open-delay="50" text="Actualizar lista">
                  <template #activator="{ props }">
                    <v-btn size="small" icon height="40px" width="40px" class="btn-grow" v-bind="props"
                      @click="ifRefrescarCargando = true; this.refrescar()" :readonly="ifRefrescarCargando" :loading="ifRefrescarCargando">
                      <v-icon color="#006CA1">mdi-refresh</v-icon>
                    </v-btn>
                  </template>
                </v-tooltip>
                <v-tooltip location="top" :open-delay="50" text="Activar Filtros">
                  <template #activator="{ props }">
                    <v-btn size="small" icon height="40px" width="40px" class="btn-grow" v-if="!mostrarSeguimientosMesPendientes"
                      @click="filtrosActivos = !filtrosActivos" v-bind="props">
                      <v-icon color="#006CA1">mdi mdi-filter-check</v-icon>
                    </v-btn>
                  </template>
                </v-tooltip>

                <v-tooltip location="top" :open-delay="50" text="Seguimientos pendientes del mes">
                    <template #activator="{ props }"> <!--V-if="!mostrarSoloSinActividad"-->
                      <v-btn size="small" icon height="40px" width="40px" class="btn-grow" v-if="false" 
                        v-bind="props" @click="mostrarSeguimientosMesPendientes = !mostrarSeguimientosMesPendientes; filtrosActivos = false">
                        <v-icon color="#006CA1">mdi-calendar-clock</v-icon>
                      </v-btn>
                    </template>
                  </v-tooltip>
              </div>
            </div>

            <v-row class="mb-4">

              <v-row class="mb-2 d-flex justify-center" style="margin-right: 0px;">
                <!-- Campos alineados a la derecha -->
                <div v-if="filtrosActivos" style="display: contents;">
                  <v-col cols="2">
                        <!-- Filtro normal -->
                        <v-text-field v-model="fechaInicio" label="Fecha Inicio" type="date" class="ml-n8 mr-n2 small-date-input"
                          prepend-inner-icon="mdi-calendar" density="compact" variant="outlined"  v-if="!mostrarSoloSinActividad"
                          @update:model-value="datosIniciales()" />
                        <!-- Filtro para actividades sin seguimiento -->
                        <v-text-field v-model="fechaInicioSinSeg" label="Fecha Inicio (Sin seguimiento)" type="date" class="ml-n8 mr-n2 small-date-input"
                            prepend-inner-icon="mdi-calendar" density="compact" variant="outlined"  v-if="mostrarSoloSinActividad"
                            @update:model-value="filtrarFechasSinSeguimiento()" />
                  </v-col>
                  <v-col cols="2"  >
                        <!-- Filtro normal -->
                        <v-text-field v-model="fechaFin" label="Fecha Fin" type="date" prepend-inner-icon="mdi-calendar"
                          class="mr-n7 small-date-input" density="compact" variant="outlined" :min="fechaInicio" v-if="!mostrarSoloSinActividad"
                          @update:model-value="datosIniciales()"/> 
                        <!-- Filtro para actividades sin seguimiento -->
                        <v-text-field v-model="fechaFinSinSeg" label="Fecha Fin (Sin seguimiento)" type="date" prepend-inner-icon="mdi-calendar"
                            class="mr-n7 small-date-input" density="compact" variant="outlined" :min="fechaInicioSinSeg" v-if="mostrarSoloSinActividad"
                            @update:model-value="filtrarFechasSinSeguimiento()"/> 
                  </v-col>
                  <!-- Filtros para actividades normales -->
                  <v-col cols="3" v-if="!mostrarSoloSinActividad">
                    <v-autocomplete v-model="empresaSeleccionada"
                      class="ml-2 mr-n2"
                      :items="empresas"
                      item-title="p_razon_social"
                      item-value="id"
                      label="Empresa"
                      density="compact"
                      variant="outlined"
                      clearable
                      return-object
                      @update:model-value="datosIniciales()" />
                  </v-col>
                  <v-col cols="2" v-if="!mostrarSoloSinActividad">
                    <v-autocomplete v-model="canal"
                      :items="canales"
                      item-title="nombre"
                      item-value="id"
                      label="Canal"
                      density="compact"
                      variant="outlined"
                      clearable
                      return-object
                      @update:model-value="datosIniciales()" />
                  </v-col>
                  <v-col cols="2" v-if="!mostrarSoloSinActividad">
                    <v-autocomplete v-model="productoSeleccionado"
                      :items="productos"
                      item-title="nombre"
                      item-value="id"
                      label="Producto"
                      density="compact"
                      variant="outlined"
                      clearable
                      return-object
                      @update:model-value="datosIniciales()" />
                  </v-col>
                  <!-- Filtros para actividades sin seguimiento -->
                  <v-col cols="3" v-if="mostrarSoloSinActividad">
                    <v-autocomplete v-model="empresaSeleccionadaSinSeg"
                      class="ml-2 mr-n2"
                      :items="empresasSinSeg"
                      item-title="p_razon_social"
                      item-value="id"
                      label="Empresa (Sin seguimiento)"
                      density="compact"
                      variant="outlined"
                      clearable
                      return-object
                      @update:model-value="filtrarActividadesSinSeguimiento()" />
                  </v-col>
                  <v-col cols="2" v-if="mostrarSoloSinActividad">
                    <v-autocomplete v-model="canalSinSeg"
                      :items="mediosSinSeg"
                      item-title="nombre"
                      item-value="id"
                      label="Canal (Sin seguimiento)"
                      density="compact"
                      variant="outlined"
                      clearable
                      return-object
                      @update:model-value="filtrarActividadesSinSeguimiento()" />
                  </v-col>
                  <v-col cols="2" v-if="mostrarSoloSinActividad">
                    <v-autocomplete v-model="productoSeleccionadoSinSeg"
                      :items="productosSinSeg"
                      item-title="nombre"
                      item-value="id"
                      label="Producto (Sin seguimiento)"
                      density="compact"
                      variant="outlined"
                      clearable
                      return-object
                      @update:model-value="filtrarActividadesSinSeguimiento()" />
                  </v-col>
                </div>
              </v-row>
            </v-row>
            <!-- Contenedor externo con scroll horizontal -->
            <div class="scroll-custom-v2"
              style="overflow-x: auto; white-space: nowrap; padding-bottom: 16px; margin-top: -40px;">
              
              <!-- Contenedor horizontal igual al de columnas -->
              <div style="display: flex; flex-wrap: nowrap; margin-bottom: 8px;">
                <!-- Espacio vacío para alinear totales desde la derecha -->
                <div v-for="(estado, index) in estados" :key="'total-' + index"
                  style="flex: 0 0 25%; max-width: 25%; padding: 0 8px; box-sizing: border-box;">
                  <div v-if="!mostrarSoloSinActividad && !mostrarSeguimientosMesPendientes && ['Cotizados', 'Ganado', 'Perdido'].includes(estado.nombre)"
                    class="text-center font-weight-bold">
                    Total ${{ estado.total.toLocaleString('es-CO') }}
                  </div>
                  <div v-else>&nbsp;</div> <!-- espacio en blanco para alinear -->
                </div>
              </div>
              
              <!-- Contenedor interno flex con columnas en línea -->
              <div style="display: flex; flex-wrap: nowrap;">
                
                <template v-if="mostrarSoloSinActividad === true">
                  <!-- SOLO mostrar actividades sin seguimiento en una sola columna -->
                  <div style="flex: 0 0 130%; max-width: 130%; padding: 0 8px; box-sizing: border-box;">
                    <div class="scroll-custom"
                      :style="`height: ${filtrosActivos ? '50vh' : '60vh'}; overflow-y: auto; padding-right: 8px;`">
                      <v-card-title class="text-subtitle-1" style="background:#9e2121; color:white; border-radius:8px;">
                        <v-icon icon="mdi-account-alert" color="white" prepend-icon></v-icon>
                        Clientes sin actividad +{{ limiteDeDiasSinActividad }} días
                        <span class="float-right">{{ actividadesSinSeguimiento.length }}</span>
                      </v-card-title>
                      <template v-for="item in actividadesSinSeguimientoFiltradas" :key="item.id">
                        <v-card class="mb-2 btn-grow-card-items" v-bind="props" @click="abrirActividades(item)">
                          <v-card-title class="text-subtitle-1 py-1">{{ item.nombre }}</v-card-title>
                          <v-card-subtitle class="py-1">
                            <strong>Producto:</strong> {{ item.producto }}
                          </v-card-subtitle>
                          <v-card-subtitle class="py-1">
                            <strong>Días sin actividad:</strong> {{ item.diasSinAct }}
                          </v-card-subtitle>
                           <v-card-subtitle class="py-1">
                             <strong>Medio:</strong>
                             <span>
                               {{ item.medio === 0 ? 'Bot' : item.medio === 1 ? 'Lead' : item.medio === 2 ? 'Comercial' : (item.medio_nombre || item.medio || 'Desconocido') }}
                             </span>
                           </v-card-subtitle>
                          <v-card-subtitle class="py-1">
                            <span><strong>Última actividad:</strong> {{ item.fechaUlt }}</span>
                            <span v-if="item.fecproxseg && !(item.fecproxseg.startsWith('1900'))"> | Próximo seguimiento: {{ item.fecproxseg }}</span>
                            <span v-else-if="item.fecproxseg && item.fecproxseg.startsWith('1900')"> | No hay próximo seguimiento</span>
                          </v-card-subtitle>
                        </v-card>
                      </template>
                    </div>
                  </div>
                </template>
                <template v-if="mostrarSeguimientosMesPendientes === true">
                <!-- Línea de tiempo curva y visualmente distribuida -->
                <div style="width: 100%; height: 74vh; padding: 0 8px; box-sizing: border-box; display: flex; flex-direction: column;">
                  <v-card-title class="text-h6 mb-2" style="background:#006CA1; color:white; border-radius:8px;">
                    <v-icon icon="mdi-calendar-clock" color="white" prepend-icon></v-icon>
                    Actividades pendientes del mes
                    <span class="float-right">{{ actividadesPendientesMes.length }}</span>
                  </v-card-title>
                  
                  <div  style="flex:1; overflow-x:auto; overflow-y:hidden; display:flex; align-items:center; position:relative;">
                    <!-- SVG curva -->
                     <div v-if="actividadesPendientesMes.length === 0" class="text-center py-4" style="color: #888; position:absolute; left:50%; top:100px; transform:translateX(-50%);">
                        No hay actividades pendientes para este mes.
                      </div>
                    <svg v-if="actividadesPendientesMes.length > 0" :width="Math.max(actividadesPendientesMes.length * 320, 1200)" height="220" style="position:absolute; left:0; top:40px; z-index:0;" viewBox="0 0 1200 220">
                      <path d="M40,180 Q300,20 600,180 T1160,180" stroke="#1976D2" stroke-width="5" fill="none" />
                      <!-- Puntos destacados -->
                      <circle cx="40" cy="180" r="12" fill="#43a047" />
                      <text x="40" y="210" font-size="16" fill="#1976D2" text-anchor="middle">Inicio</text>
                      <circle cx="600" cy="180" r="12" fill="#ffb300" />
                      <text x="600" y="210" font-size="16" fill="#1976D2" text-anchor="middle">Mitad</text>
                      <circle cx="1160" cy="180" r="12" fill="#e53935" />
                      <text x="1160" y="210" font-size="16" fill="#1976D2" text-anchor="middle">Fin</text>
                    </svg>
                    <!-- Cards distribuidas sobre la curva -->
                    <div style="position:relative; width:100%; height:220px; display:flex; align-items:flex-end; z-index:1;">
                      <div v-for="(actividad, idx) in actividadesPendientesMes" :key="actividad.id"
                        :style="getCardCurveStyle(idx, actividadesPendientesMes.length)"
                      >
                        <v-card elevation="6" class="pa-5 timeline-card-hover btn-" style="min-width: 280px; max-width:300px; height: 220px; display: flex; flex-direction: column; justify-content: space-between; cursor:pointer; border-radius:18px; box-shadow:0 6px 24px rgba(0,0,0,0.10); transition:box-shadow 0.2s; background: white; position:absolute;" @click="abrirActividades(actividad)">
                          <div class="d-flex align-center mb-2">
                            <v-avatar size="40" :color="actividad.estadoColor || '#1976D2'" class="mr-2">
                              <v-icon color="white">mdi-account</v-icon>
                            </v-avatar>
                            <span class="font-weight-bold" style="font-size: 1.18rem; color: #222;">{{ actividad.nombre }}</span>
                          </div>
                          <div style="font-size: 1.02rem; color: #666; margin-bottom:6px;">
                            <v-chip :color="actividad.estadoColor || '#1976D2'" text-color="white" class="mr-2" size="small">{{ actividad.estadoNombre }}</v-chip>
                            <strong>Producto:</strong> {{ actividad.producto }}
                          </div>
                          <div style="font-size: 1.01rem; color: #1976D2; margin-bottom:6px;">
                            <strong>Fecha pendiente:</strong> <span style="font-weight:bold;">{{ actividad.fecproxseg }}</span>
                          </div>
                          <div style="font-size: 1.01rem; color: #666; margin-bottom:6px;">
                            <strong>Contacto:</strong> {{ actividad.contacto }}
                          </div>
                          <span v-if="actividad.telefono"> | <strong>Tel:</strong> {{ actividad.telefono }}</span>
                          <div style="font-size: 1.01rem; color: #666; margin-bottom:6px;">
                            <strong>Valor:</strong> <span style="color:#43a047; font-weight:bold;">${{ actividad.valor ? actividad.valor.toLocaleString() : '0' }}</span>
                          </div>
                        </v-card>
                      </div>
                    
                    </div>
                  </div>
                    
                </div>
                </template>
                <template v-if="!mostrarSoloSinActividad && !mostrarSeguimientosMesPendientes">
                  <!-- Vista normal por estados -->
                  <template v-for="(estado, index) in estados" :key="index">
                    <div style="flex: 0 0 25%; max-width: 25%; padding: 0 8px; box-sizing: border-box;">
                      <div class="scroll-custom"
                        :style="`height: ${mostrarAdvertenciaSinActividad ? (filtrosActivos ? '46vh' : '56.5vh') : (filtrosActivos ? '56vh' : '65.5vh')}; overflow-y: auto; padding-right: 8px;`">
                        <v-card class="mb-2 btn-grow-card" :color="estado.color" dark
                          @click="cargaProspEst(estado.id, estado.nombre)"
                          style="position: sticky; top: 0; z-index: 1;">
                          <v-card-title class="text-subtitle-1">
                            <v-icon icon="mdi-eye" color="white" prepend-icon></v-icon> {{ estado.nombre }}
                            <span class="float-right">{{ estado.cantidad.toLocaleString('es-CO') }}</span>
                          </v-card-title>
                        </v-card>
                        <template v-for="item in estado.items.slice(0, 10)" :key="item.nombre">
                          <v-tooltip location="right" :open-delay="200">
                            <template #activator="{ props }">
                              <v-card class="mb-2 btn-grow-card" v-bind="props" @click="abrirActividades(item)" style="position:relative;">
                                <v-card-title class="text-subtitle-2 py-1" style="margin-bottom: -2px;">{{ item.nombre }}</v-card-title>
                                <div v-if="['En Proceso', 'Cotizados'].includes(estado.nombre) && item.fecproxseg && !(item.fecproxseg.startsWith('1900'))"
                                  style="margin-bottom: 2px;">
                                  <v-card-subtitle v-if="false" size="x-small" class="mt-1 mb-1 px-2 ml-2" style="color: #1976D2; font-size: 0.78rem; border-radius: 6px; box-shadow: none; font-weight: 500; align-items: center;">
                                    <v-icon left size="15" style="margin-right: 2px; color:#90caf9;">mdi-calendar-clock</v-icon>
                                    Prox.Seg: <span style="font-weight: bold; margin-left: 2px; color:#1976D2;">{{ item.fecproxseg }}</span>
                                  </v-card-subtitle>
                                </div>
                                <v-card-subtitle class="py-1">{{ item.producto }}</v-card-subtitle>
                                <v-card-subtitle class="py-1" style="display: flex; justify-content: space-between; align-items: center;">
                                  <span>{{ item.fecha }}</span>
                                  <span style="font-size: 13px; color: #1976D2;"> {{ item.medio == 0 ? "Bot" : item.medio == 1 ? "Lead" : "Comercial" }} </span>
                                </v-card-subtitle>
                                <v-card-text v-if="estado.nombre !== 'Prospecto' && estado.nombre !== 'En Proceso'" class="py-1">
                                  {{ item.valor ? `$${item.valor.toLocaleString()}` : '$0' }}
                                </v-card-text>
                              </v-card>
                            </template>
                            <span>
                              <strong>Nombre:</strong> {{ item.nombre }}<br>
                              <strong>Teléfono:</strong> {{ item.telefono }}<br>
                              <strong>Contacto:</strong> {{ item.contacto }}<br>
                              <strong>Celular:</strong> {{ item.celular }}<br>
                              <strong>Dirección:</strong> {{ item.direccion }}<br>
                              <strong>Departamento:</strong> {{ item.departamento }}<br>
                              <strong>Ciudad:</strong> {{ item.ciudad }}<br>
                            </span>
                          </v-tooltip>
                        </template>
                      </div>
                    </div>
                  </template>
                </template>
              </div>

              <div>
                
              </div>
            </div>

            <v-row>
              <v-alert v-if="!mostrarSeguimientosMesPendientes" class="mt-4" type="success" icon="mdi-cash-multiple">
                <div class="text-h6 d-flex justify-space-between" >
                  <span>ACUMULADO</span>
                  <span class="font-weight-bold">${{ ctaAcumulado.toLocaleString() }}</span>
                </div>
              </v-alert>
            </v-row>

            <v-row @click="mostrarSoloClientesSinActividad(), filtrosActivos = !filtrosActivos">
              <v-alert class="mt-4 btn-grow-card-items-active" type="error" icon="mdi-account-alert"
                v-if="mostrarAdvertenciaSinActividad && !mostrarSeguimientosMesPendientes">
                Clientes sin actividad +{{ limiteDeDiasSinActividad }} días: 
                  <template v-if="!mostrarSoloSinActividad">
                    <strong>{{ actividadesSinSeguimiento.length }}</strong>
                  </template>
                  <template v-if="mostrarSoloSinActividad">
                    <strong>{{ actividadesSinSeguimientoFiltradas.length }}</strong>
                  </template>
              </v-alert>
            </v-row>
          </v-col>
        </v-row>

      </v-container>
    </v-main>

    <!-- FORMULARIO PROSPECTO-->

    <v-dialog v-model="formularioContacto" width="600" persistent>
      <v-card>
        <v-card-title class="text-h6">Nuevo Contacto</v-card-title>
        <v-card-text>
          <v-row>
            <v-col>
              <v-text-field class="mx-5 mt-5" v-model="nombre" label="Nombre" type="text" variant="outlined" clearable
                autocomplete="off" />
              <v-text-field class="mx-5" v-model="apellido" label="Apellido" type="text" variant="outlined" clearable
                autocomplete="off" />
              <v-row>
                <v-col>
                  <v-autocomplete class="mx-5" v-model="categoria" :items="categorias" return-object item-title="nombre"
                    item-value="id" label="Categoria Cargo" variant="outlined" clearable autocomplete="off" />
                </v-col>
                <v-col>
                  <v-autocomplete class="mx-5" v-model="cargo" :items="cargos" return-object item-title="nombre"
                    item-value="id" label="Cargo" type="text" variant="outlined" clearable autocomplete="off" />
                </v-col>
              </v-row>
              <v-text-field class="mx-5" v-model="correoContacto" label="Correo" type="text" variant="outlined"
                clearable autocomplete="off" />
              <v-text-field class="mx-5" v-model="celular" label="Celular" type="number" variant="outlined" clearable
                autocomplete="off" />
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

    <v-dialog v-model="formularioProspecto" width="1100" persistent>
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
            <v-col style="border-left: 1px solid #ccc; padding-left: 20px;">
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
      <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
        <v-icon class="mr-2">mdi mdi-lightbulb-on </v-icon>
        Nueva Oportunidad
      </v-card-title>
      <v-card>



        <v-card-text>
          <v-row>
            <v-col>
              <v-autocomplete clearable label="Cliente" v-model="selectedClienteOportunidad"
                :items="selectClientesOportunidad" return-object item-title="p_razon_social" item-value="id"
                variant="outlined" autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-domain</v-icon>
                </template>
              </v-autocomplete>
            </v-col>
          </v-row>

          <v-row class="mt-n2">
            <v-col>
              <v-select clearable label="Relacionar Servicio" v-model="selectedServicioOportunidad"
                :items="selectServiciosOportunidad" return-object item-title="nombre" item-value="id" variant="outlined"
                autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-briefcase</v-icon>
                </template>
              </v-select>
            </v-col>
          </v-row>

          <v-row class="mt-n2" v-if=false>
            <v-col>
              <v-text-field label="Valor del Proyecto" clearable variant="outlined"
                v-model="selectedValorProyectoOportunidad" type="number" autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-currency-usd</v-icon>
                </template>
              </v-text-field>
            </v-col>
          </v-row>

          <v-row class="mt-n2">
            <v-col>
              <v-textarea label="Observaciones" rows="3" variant="outlined" class="mb-0" density="compact"
                v-model="selectedObservacionesOportunidad" clearable autocomplete="off">
                <template v-slot:prepend-inner>
                  <v-icon size="small" color="#006CA1" style="opacity: 100%;">mdi-eye</v-icon>
                </template>
              </v-textarea>
            </v-col>
          </v-row>
        </v-card-text>

        <v-row class="mt-n10 mx-2">
          <v-col>
            <v-btn color="blue" @click="registrarOportunidad()" class="ml-2 btn-grow-card"
              style="float: right;">Registrar
              Oportunidad</v-btn>
            <v-btn class="btn-grow-card" color="blue" text @click="dialogNuevaOportunidad = false"
              style="float: right;">Cerrar</v-btn>
          </v-col>
        </v-row>

      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogListProspEst" max-width="95%" height="100vh" persistent>
      <v-card-title class="text-h7"
        style="background-color: #006CA1; color: white; display: flex; align-items: center;">
        <div class="d-flex align-center">
          <v-icon class="mr-2" size="small">mdi mdi-view-list-outline </v-icon>
          <span>Listar Prospectos in Estado {{ estadoactual }}</span>
        </div>
        <v-spacer></v-spacer>
        <v-text-field v-model="searchProsp" @update:model-value="onSearchInput"
          placeholder="Buscar por razón social, NIT u observación…" prepend-inner-icon="mdi-magnify" density="compact"
          variant="solo" clearable class="header-search mr-6" hide-details style="max-width: 380px;" />
        <v-btn icon="mdi-close" size="small" color="white" @click="dialogListProspEst = false" class="btn-grow" />
      </v-card-title>
      <v-card class="pt-0">


        <!-- Tabla Prospectos / Seguimientos -->
        <v-data-table :headers="headersProspEst" :items="itemsListProspEstFiltered"
          :sort-by="[{ key: 'fecproxseg', order: 'desc' }]" :search="searchProsp"
          :filter-keys="['razon_social', 'nit', 'obsev']" :custom-filter="accentInsensitiveFilter"
          class="elevation-1 rounded-lg data-table fancy-headers fancy-rows" density="compact" virtual-scroll hover
          fixed-header height="78vh" :items-per-page="20" :items-per-page-options="[10, 20, 50]"
          items-per-page-text="Registros por página" page-text="({0}-{1}) de ({2})" no-data-text="No hay registros"
          @click:row="(_, row) => abrirNuevaActividad(row.item)" :item-class="() => 'btn-grow-card-items fancy-row'">

          <!--HEADERs-->
          <!-- Header con ícono por columna -->
          <template #header.nit="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-identifier</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.razon_social="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-domain</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.valorproy="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-cash-multiple</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.nomserv="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-briefcase-outline</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.fecproxseg="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-calendar-clock</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.nomseg="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-clipboard-text-outline</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.obsev="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-comment-text-outline</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.fecha_act="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-calendar</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <template #header.fecha_sistema="{ column }">
            <div class="th-content">
              <v-icon size="16">mdi-account</v-icon>
              <span>{{ column.title }}</span>
            </div>
          </template>

          <!--INYECCIÓN DE ESTILOS DE LAS FILAS-->
          <template #item="{ item, columns, props, index }">
            <tr v-bind="props" :key="item.id ?? index" :class="['btn-grow-card-items', 'fancy-row', toneClass(item)]">
              <td v-for="col in columns" :key="col.key">
                <span v-if="col.key === 'fecha_sistema'">
                  {{ formatFechaSistema(item.fecha_sistema) }}
                </span>
                <span v-else>
                  {{ item[col.key] ?? '—' }}
                </span>
              </td>
            </tr>
          </template>

          <!---------->
          <!--FILAS-->
          <!-- Costo formateado a COP -->
          <template #item.valorproy="{ item }">
            {{ formatCOP(item.valorproy) }}
          </template>

          <!-- Fechas en dd/mm/aaaa -->
          <template #item.fecproxseg="{ item }">
            {{ formatDMY(item.fecproxseg) }}
          </template>
          <template #item.fecha_act="{ item }">
            {{ formatDMY(item.fecha_act) }}
          </template>

          <!-- Observaciones: clamp + tooltip -->
          <template #item.obsev="{ item }">
            <v-tooltip :text="item.obsev" location="top" v-if="item.obsev">
              <template #activator="{ props }">
                <span v-bind="props" class="clamp-2">{{ item.obsev }}</span>
              </template>
            </v-tooltip>
            <span v-else>—</span>
          </template>

          <!-- Explicación de colores de filas en el footer de la tabla -->
          <template #footer.prepend>
          <v-row class="d-flex align-center" style="gap: 18px; margin-left: 8px;">
            <div class="d-flex align-center" style="gap: 8px;">
              <v-avatar size="18" color="#4550ec" class="mr-1" />
              <span style="font-size: 0.86rem; color: #131269;">Más de 7 días (azul)</span>
            </div>
            <div class="d-flex align-center" style="gap: 8px;">
              <v-avatar size="18" color="#fbc02d" class="mr-1" />
              <span style="font-size: 0.86rem; color: #544e01;">Entre 3 y 5 días (amarillo)</span>
            </div>
            <div class="d-flex align-center" style="gap: 8px;">
              <v-avatar size="18" color="#d32f2f" class="mr-1" />
              <span style="font-size: 0.86rem; color: #5c0101;">Hoy a 2 días (rojo)</span>
            </div>
            <div class="d-flex align-center" style="gap: 8px;">
              <v-avatar size="18" color="#bdbdbd" class="mr-1" />
              <span style="font-size: 0.86rem; color: #2f2f2f;">Sin seguimiento o vencido (gris)</span>
            </div>
          </v-row>
        </template>
        </v-data-table>


      </v-card>
    </v-dialog>

    <!----- Dialogo para listar los prospectos ----->

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

          <v-row v-for="(fila, filaIndex) in filasEmpresas" :key="filaIndex" class="mb-2" cols="12" md="3" lg="3">
            <v-col v-for="empresa in fila" :key="empresa.id" cols="12" md="6" lg="4">
              <v-card @click="cargarProspecto(empresa); estaEditando = true" class="empresa-card pa-4 mb-2 " elevation="3" >
              <v-row align="center" no-gutters>
                <v-col cols="auto">
                  <v-avatar color="#1976D2" size="44">
                    <v-icon color="white" size="32">mdi-office-building</v-icon>
                  </v-avatar>
                </v-col>
                <v-col>
                  <div class="empresa-title font-weight-bold ml-2" style="font-size: 1.15rem; color: #0A1C3A; white-space: normal; word-break: break-word;">
                    {{ empresa.p_razon_social }}
                  </div>
                  <div class="empresa-nit ml-2 text-caption" style="color: #1976D2; font-weight: 500; margin-top: 2px;">
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
                    <span style="white-space: normal; word-break: break-word;">{{ empresa.pc_nombre }} {{ empresa.pc_apellido }}</span>
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
    <!----- Dialogo para crear/editar los prospectos ----->
  </v-app>
</template>


<script>

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
    celular: '57',
    extension: '57',
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
    tel1: '57',
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
      { id: 0, nombre: 'Bot' },
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
    drawer: false,
    inicio: 1,

    ifCargando: false,
    ifRefrescarCargando: false,

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

    maxlength2: [v => !v || String(v).length < 13 || "Error. Máximo 10 dígitos"],

    headersProspEst: [
      { title: 'NIT', value: 'nit', sortable: true, width: 140 },
      { title: 'Razón Social', value: 'razon_social', sortable: true, minWidth: 220 },
      { title: 'Costo Proyecto', value: 'valorproy', sortable: true, align: 'end', width: 160 },
      { title: 'Servicio Interesado', value: 'nomserv', sortable: true, minWidth: 200 },
      { title: 'Fecha Prox. Seguim.', value: 'fecproxseg', sortable: true, width: 150 },
      { title: 'Tipo Seguimiento', value: 'nomseg', sortable: true, width: 170 },
      { title: 'Observaciones', value: 'obsev', sortable: false, minWidth: 280 },
      { title: 'Fecha Oportunidad', value: 'fecha_act', sortable: true, width: 140 },
      { title: 'Fecha Creación Prospecto', value: 'fecha_sistema', sortable: true, width: 140 },
    ],

    usarGrisVencido: false,

    searchInput: '',
    searchProsp: '',
    _searchTimer: null,
    _indexedItems: [],

    actividadesSinSeguimiento: [],
    limiteDeDiasSinActividad: 5,
    mostrarAdvertenciaSinActividad: false,
    estaEditando: true,


    rules: {
      required: v => String(v ?? '').trim().length > 0 || 'Requerido',

      // Teléfono: máximo 12 dígitos (ej: 57 + 10)
      phoneMax12: v => {
        const s = String(v ?? '')
        if (!s) return true                      // permite vacío si no usas 'required'
        const digits = s.replace(/\D/g, '')      // cuenta solo dígitos
        return digits.length <= 12 || 'Máximo 12 dígitos'
      },

      // Ejemplo genérico de "máximo 12 caracteres" (no solo dígitos)
      maxLen12: v => {
        const s = String(v ?? '')
        if (!s) return true
        return s.length <= 12 || 'Máximo 12 caracteres'
      },
    },
    mostrarSoloSinActividad: false,
    cantidadPendientes: 0,
    mostrarSeguimientosMesPendientes: false,

    fechaInicioSinSeg: '',
    fechaFinSinSeg: '',
    empresaSeleccionadaSinSeg: null,
    canalSinSeg: null,
    productoSeleccionadoSinSeg: null,
    actividadesSinSeguimientoFiltradas: [],
    empresasSinSeg: [],
    canalesSinSeg: [],
    productosSinSeg: [],
    mediosSinSeg: [],
    medioSinSeg: null,

    menuActivo: null,
    imagenComercial: null,
  }),

  mounted() {
    //axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL; // URL base de la API
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
    this.setMenuActivoPorRuta();

    const imagenGuardada = localStorage.getItem('imagenComercial');
    if (imagenGuardada) {
      this.imagenComercial = imagenGuardada;
    } else {
      this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg`;
    }

    const filtroRazonSocial = localStorage.getItem('filtroRazonSocialEmpresasComercial');
    if (filtroRazonSocial) {
      this.abrirDialogProspectos();
      // Espera a que las empresas estén cargada
      localStorage.removeItem('filtroRazonSocialEmpresasComercial');
      setTimeout(() => {
        // Busca el objeto empresa por nombre
        const empresa = this.listaEmpresasComercial.find(e =>
          e.p_razon_social && e.p_razon_social.toLowerCase().trim() === filtroRazonSocial.toLowerCase().trim()
        );
        if (empresa) {
          this.filtroRazonSocialEmpresasComercial = empresa;
          this.filtrarEmpresas();
        } else {
          this.filtroRazonSocialEmpresasComercial = null;
        }

      }, 1300); // 1.3 segundos
    }
    this.cargarCantidadPendientes();
    this.mostrarActividadesSinSeguimiento();

  },
  watch: {
    actividadesSinSeguimiento: {
      handler(newVal) {
        // Si estamos en modo sin seguimiento y no hay filtros activos, mostrar todos
        if (this.mostrarSoloSinActividad && !this.empresaSeleccionadaSinSeg && !this.canalSinSeg && !this.productoSeleccionadoSinSeg) {
          this.actividadesSinSeguimientoFiltradas = Array.isArray(newVal) ? [...newVal] : [];
          // Generar los arrays de filtros usando campos alternativos si los principales no existen
          this.empresasSinSeg = newVal
            .map(a => ({
              id: a.idEmpresa || a.idempresa || a.idcli || a.idprosp,
              p_razon_social: a.empresa || a.nombre || a.razon_social || a.p_razon_social || 'Sin nombre'
            }))
            .filter((v, i, a) => v.id && a.findIndex(t => t.id === v.id) === i);
          this.canalesSinSeg = newVal
            .map(a => ({
              id: a.idCanal || a.idcanal || a.idmedio,
              nombre: a.canal || a.nombre || a.nommedio || 'Sin canal'
            }))
            .filter((v, i, a) => v.id && a.findIndex(t => t.id === v.id) === i);
          this.productosSinSeg = newVal
            .map(a => ({
              id: a.idProducto || a.idproducto || a.idserv,
              nombre: a.producto || a.nomserv || a.nombre || 'Sin producto'
            }))
            .filter((v, i, a) => v.id && a.findIndex(t => t.id === v.id) === i);
           this.mediosSinSeg = newVal
             .map(a => {
               let id = typeof a.medio === 'number' ? a.medio : (a.idmedio ?? a.idCanal ?? a.idcanal);
               let nombre = (a.medio === 0 ? 'Bot' : a.medio === 1 ? 'Lead' : a.medio === 2 ? 'Comercial' : (a.medio_nombre || a.nommedio || a.medio || 'Desconocido'));
               return { id, nombre };
             })
             .filter((v, i, a) => v.id !== undefined && a.findIndex(t => t.id === v.id) === i);
           console.log('mediosSinSeg:', this.mediosSinSeg);
        }
      },
      deep: true
    },
    mostrarSoloSinActividad(val) {
      if (!val) {
        this.empresaSeleccionadaSinSeg = null;
        this.canalSinSeg = null;
        this.productoSeleccionadoSinSeg = null;
        this.actividadesSinSeguimientoFiltradas = [...this.actividadesSinSeguimiento];
      } else {
        // Inicializa los filtros y muestra todas las actividades
        this.empresaSeleccionadaSinSeg = null;
        this.canalSinSeg = null;
        this.productoSeleccionadoSinSeg = null;
        // Si hay actividades, inicializa la lista filtrada con todas
        this.actividadesSinSeguimientoFiltradas = Array.isArray(this.actividadesSinSeguimiento) ? [...this.actividadesSinSeguimiento] : [];
        // Generar los arrays de filtros usando campos alternativos si los principales no existen
        this.empresasSinSeg = this.actividadesSinSeguimiento
          .map(a => ({
            id: a.idEmpresa || a.idempresa || a.idcli || a.idprosp,
            p_razon_social: a.empresa || a.nombre || a.razon_social || a.p_razon_social || 'Sin nombre'
          }))
          .filter((v, i, a) => v.id && a.findIndex(t => t.id === v.id) === i);
        this.canalesSinSeg = this.actividadesSinSeguimiento
          .map(a => ({
            id: a.idCanal || a.idcanal || a.idmedio,
            nombre: a.canal || a.nombre || a.nommedio || 'Sin canal'
          }))
          .filter((v, i, a) => v.id && a.findIndex(t => t.id === v.id) === i);
        this.productosSinSeg = this.actividadesSinSeguimiento
          .map(a => ({
            id: a.idProducto || a.idproducto || a.idserv,
            nombre: a.producto || a.nomserv || a.nombre || 'Sin producto'
          }))
          .filter((v, i, a) => v.id && a.findIndex(t => t.id === v.id) === i);
         this.mediosSinSeg = this.actividadesSinSeguimiento
           .map(a => {
             let id = typeof a.medio === 'number' ? a.medio : (a.idmedio ?? a.idCanal ?? a.idcanal);
             let nombre = (a.medio === 0 ? 'Bot' : a.medio === 1 ? 'Lead' : a.medio === 2 ? 'Comercial' : (a.medio_nombre || a.nommedio || a.medio || 'Desconocido'));
             return { id, nombre };
           })
           .filter((v, i, a) => v.id !== undefined && a.findIndex(t => t.id === v.id) === i);
         console.log('mediosSinSeg:', this.mediosSinSeg);
         this.mediosSinSeg = this.actividadesSinSeguimiento
           .map(a => {
             let id = typeof a.medio === 'number' ? a.medio : (a.idmedio ?? a.idCanal ?? a.idcanal);
             let nombre = (a.medio === 0 ? 'Bot' : a.medio === 1 ? 'Lead' : a.medio === 2 ? 'Comercial' : (a.medio_nombre || a.nommedio || a.medio || 'Desconocido'));
             return { id, nombre };
           })
           .filter((v, i, a) => v.id !== undefined && a.findIndex(t => t.id === v.id) === i);
      }
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

    canal(newValue) {
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
      this.porcMetaMensual = 0;
      if (this.fechaInicio == null) {
        this.fechaFin = null;
        
      }
      else if (this.fechaFin && this.fechaFin < newValue) {
        this.fechaFin = this.fechaInicio;
        
      }
    },
    itemsListProspEst: {
      immediate: true,
      handler(list) {
        const norm = this._normalize
        this._indexedItems = (list || []).map(it => ({
          ...it,
          __search: norm([it.razon_social, it.nit, it.obsev].join(' ')),
        }))
      }
    },

    mostrarAdvertenciaSinActividad(val) {
      if (!val) {
        // Si se desactiva la advertencia, limpiar filtros y recargar pendientes
        this.fechaInicioSinSeg = '';
        this.fechaFinSinSeg = '';
        this.datosIniciales();
      } else {
 
      }
    },

    mostrarSoloSinActividad(val) {
      this.filtrarFechasSinSeguimiento();
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

    normalizedQuery() {
      return this._normalize(this.searchProsp)
    },


    itemsListProspEstFiltered() {
      const q = this.normalizedQuery
      let arr = this._indexedItems

      if (q) {
        arr = arr.filter(it => it.__search.includes(q))
      }

      return arr.slice().sort((a, b) => {
        const ta = this._ts(a.fecproxseg)
        const tb = this._ts(b.fecproxseg)
        return tb - ta
      })
    },

    actividadesPendientesMes() {
      // Filtra actividades con seguimiento pendiente desde hoy hasta fin de mes
      const hoy = new Date();
      const finMes = new Date(hoy.getFullYear(), hoy.getMonth() + 1, 0);
      let actividades = [];
      if (Array.isArray(this.estados)) {
        this.estados.forEach(estado => {
          if (estado.items && Array.isArray(estado.items)) {
            estado.items.forEach(item => {
              if (item.fecproxseg && !item.fecproxseg.startsWith('1900')) {
                const fechaSeg = new Date(item.fecproxseg);
                if (fechaSeg >= hoy && fechaSeg <= finMes) {
                  actividades.push({
                    ...item,
                    estadoNombre: estado.nombre,
                    estadoColor: estado.color || '#1976D2',
                  });
                }
              }
            });
          }
        });
      }
      // Ordenar por fecha de seguimiento
      return actividades.sort((a, b) => new Date(a.fecproxseg) - new Date(b.fecproxseg));
    },

    
  },

  methods: {
    filtrarActividadesSinSeguimiento() {
      let filtradas = Array.isArray(this.actividadesSinSeguimiento) ? [...this.actividadesSinSeguimiento] : [];
      if (this.empresaSeleccionadaSinSeg) {
        const idEmpresa = this.empresaSeleccionadaSinSeg.id;
        filtradas = filtradas.filter(a =>
          idEmpresa === a.idEmpresa ||
          idEmpresa === a.idempresa ||
          idEmpresa === a.idcli ||
          idEmpresa === a.idprosp
        );
      }
      if (this.canalSinSeg) {
        const idCanal = this.canalSinSeg.id;
          filtradas = filtradas.filter(a => {
            // Si el medio es numérico, comparar directamente
            if (typeof a.medio === 'number') return a.medio === idCanal;
            // Si el medio es string, comparar con idmedio, idCanal, idcanal
            return idCanal === a.idmedio || idCanal === a.idCanal || idCanal === a.idcanal;
          });
      }
      if (this.productoSeleccionadoSinSeg) {
        const idProducto = this.productoSeleccionadoSinSeg.id;
        filtradas = filtradas.filter(a =>
          idProducto === a.idProducto ||
          idProducto === a.idproducto ||
          idProducto === a.idserv
        );
      }
       if (this.medioSinSeg) {
         const idMedio = this.medioSinSeg.id;
         filtradas = filtradas.filter(a => {
           // Si el medio es numérico, comparar directamente
           if (typeof a.medio === 'number') return a.medio === idMedio;
           // Si el medio es string, comparar con idmedio, idCanal, idcanal
           return idMedio === a.idmedio || idMedio === a.idCanal || idMedio === a.idcanal;
         });
       }
      // Si no hay ningún filtro, mostrar todas
      if (!this.empresaSeleccionadaSinSeg && !this.canalSinSeg && !this.productoSeleccionadoSinSeg) {
        filtradas = Array.isArray(this.actividadesSinSeguimiento) ? [...this.actividadesSinSeguimiento] : [];
      }
      this.actividadesSinSeguimientoFiltradas = filtradas;
    },

    _updateDsGuardar(val = true) {
      this.dsGuardar = val;
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
          console.log("Carga Validación", response.data.data)
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

    irPendientes() {
      this.$router.push('/pendiente');
    },

    irClientesSinActividad() {
      this.$router.push('/clientesSinActividad');
    },

    cerrarDIV() {
      this.alerta = false;
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
      this.progress = 0;
      this.porcMetaMensual = 0;
      this.fechaInicio = null;
      this.fechaFin = null;
      this.datosIniciales();
      this.empresaSeleccionada = null;
      this.canal = null;
      this.productoSeleccionado = null;
      this.filtrosActivos = true;
      this.mostrarSoloSinActividad = false;
      this.mostrarSeguimientosMesPendientes = false;
      setTimeout(() => {
          this.ifRefrescarCargando = false;
        }, 280);
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
      let fecini = this.fechaInicio;
      let fecfin = this.fechaFin;

      // Si no hay fechas seleccionadas, usar el mes actual y mostrarlo en los inputs
      if (!this.fechaInicio || !this.fechaFin) {
        const hoy = new Date();
        const año = hoy.getFullYear();
        const mes = String(hoy.getMonth() + 1).padStart(2, '0');
        const primerDia = `${año}-${mes}-01`;
        // Último día del mes
        const ultimoDia = new Date(año, hoy.getMonth() + 1, 0).toISOString().substr(0, 10);
        fecini = primerDia;
        fecfin = ultimoDia;
        // Mostrar en los inputs
        this.fechaInicio = primerDia;
        this.fechaFin = ultimoDia;
      }
      this.estados.forEach(estado => {
        estado.cantidad = 0;
        estado.total = 0;
        estado.items = [];
      });
      // Actualizar los items de cada estado
      await axios.post(this.baseURL + 'api/cargarlisest', {
        'fecini': fecini,
        'fecfin': fecfin,
        'idprosp': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
        'idmedio': this.canal ? this.canal.id : 3,
        'idserv': this.productoSeleccionado ? this.productoSeleccionado.id : 0,
        'idusu': this.comercialId,
      })
        .then(response => {
          this.estados.forEach(estado => {
          estado.cantidad = 0;
          estado.total = 0;
          estado.items = [];
        });
          const data = response.data.data;
          data.forEach(item => {
            const estadoIndex = item.idest - 1;

            // Helper para obtener mes y año de una fecha
            const getMesAño = (fechaStr) => {
              if (!fechaStr) return { mes: -1, año: -1 };
              return { mes: fechaStr.split('-')[1], año: fechaStr.split('-')[0] };
            };

            let agregar = true;
            // Validar mes actual solo si no hay filtro de fechas
            if (!this.fechaInicio && !this.fechaFin) {
              agregar = false;
              const hoyRaw = new Date();
              const hoy = hoyRaw.toISOString().substring(0, 10);
              const mesActual = hoy.split('-')[1];
              const añoActual = hoy.split('-')[0];

              // 1. Validar fecha_act
              const { mes: mesFechaAct, año: añoFechaAct } = getMesAño(item.fecha_act.split(' ')[0]);
              if (mesFechaAct === mesActual && añoFechaAct === añoActual) {
                agregar = true;
              } else {
                // 2. Validar fecproxseg si fecha_act no cumple
                const { mes: mesFecProx, año: añoFecProx } = getMesAño(item.fecproxseg);
                if (mesFecProx === mesActual && añoFecProx === añoActual) {
                  agregar = true;
                }
              }
            }

            if (agregar && this.estados[estadoIndex]) {
              this.estados[estadoIndex].items.push({
                idproccom: item.idproc,
                idcli: item.idprosp,
                nombre: item.razon_social,
                producto: item.nomserv ? item.nomserv : 'Sin Producto',
                fecha: item.fecha_act,
                fecproxseg: item.fecproxseg,
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

              // Actualizar contadores y cantidades SOLO con los items que sí se muestran (mes actual/filtro)
              if (this.estados[estadoIndex]) {
                this.estados[estadoIndex].cantidad = this.estados[estadoIndex].items.length;
                // Actualizar contadores principales según el estado
                if (estadoIndex == 0) this.ctaProspecto = this.estados[0].cantidad;
                if (estadoIndex == 1) this.ctaEnProceso = this.estados[1].cantidad;
                if (estadoIndex == 2) this.ctaCotizados = this.estados[2].cantidad;
                if (estadoIndex == 3) this.ctaGanado = this.estados[3].cantidad;
                // Pendientes (tareas) solo si viene en el item
                if ('pendt' in item) this.tareas = item.pendt;
                // Meta mensual solo si viene en el item
                if ('meta' in item) this.ctaMetaMensual = item.meta;
              }
            }
          });
          console.log('items finales: ', this.estados)
        })
        .catch(error => {
          console.log(error);
        });

      // Calcular totales por estado
      for (const estado of this.estados) {
        estado.total = estado.items.reduce((sum, item) => sum + (item.valor || 0), 0);
      }

      const cotiztot = this.estados[this.estados.length - 3]?.total || 0;
      const ganadotot = this.estados[this.estados.length - 2]?.total || 0;
      this.ctaAcumulado = cotiztot + ganadotot;
      if (ganadotot == 0 && this.ctaMetaMensual == 0) {
        this.progress = 0;
      } else if (ganadotot == 0) {
        this.progress = 0;
      } else {
        this.porcMetaMensual = ((ganadotot / this.ctaMetaMensual));
        this.progress = this.porcMetaMensual * 100;
      }
      //this.recalcularSinSeguimiento();
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
        'fecini': fecini,
        'fecfin': fecfin,
        'idprosp': this.empresaSeleccionada ? this.empresaSeleccionada.id : 0,
        'idserv': this.productoSeleccionado ? this.productoSeleccionado.id : 0,
        'idest': idestado,
        'idmedio': this.canal ? this.canal.id : 3,
        'idusu': this.comercialId,
      })
        .then(response => {
          const data = response.data.data;
          const itemsFiltrados = [];

          // Validación de mes actual igual a datosIniciales
          const getMesAño = (fechaStr) => {
            if (!fechaStr) return { mes: -1, año: -1 };
            return { mes: fechaStr.split('-')[1], año: fechaStr.split('-')[0] };
          };
          let agregar;
          if (!this.fechaInicio && !this.fechaFin) {
            const hoyRaw = new Date();
            const hoy = hoyRaw.toISOString().substring(0, 10);
            const mesActual = hoy.split('-')[1];
            const añoActual = hoy.split('-')[0];
            for (const item of data) {
              agregar = false;
              const { mes: mesFechaAct, año: añoFechaAct } = getMesAño(item.fecha_act.split(' ')[0]);
              if (mesFechaAct === mesActual && añoFechaAct === añoActual) {
                agregar = true;
              } else {
                const { mes: mesFecProx, año: añoFecProx } = getMesAño(item.fecproxseg);
                if (mesFecProx === mesActual && añoFecProx === añoActual) {
                  agregar = true;
                }
              }
              if (agregar) itemsFiltrados.push(item);
            }
            this.itemsListProspEst = itemsFiltrados;
          } else {
            this.itemsListProspEst = data;
          }
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
      localStorage.setItem('idempresa', actividad.idprosp);
      localStorage.setItem('razon_soc', actividad.razon_social);
      localStorage.setItem('idestado', actividad.idest);

      localStorage.setItem('servicio', actividad.nomserv);
      localStorage.setItem('valorpro', actividad.valorproy);


      console.log("idprospecto guardado:", actividad.idcli);

      console.log("Actividad seleccionada:", actividad);
      console.log("servicio:", actividad.nomserv);
      console.log("servicio localStorage:", localStorage.getItem('servicio'));

      setTimeout(() => {
        this.$router.push('/pendiente');
      }, 1000);

    },

    // Cambios Angelo

    abrirActividades(actividad) {

      console.log("Actividad seleccionada:", actividad);

      console.log("ID de la actividad:", actividad.idproccom);

      localStorage.setItem('idproccom', actividad.idproccom);
      localStorage.setItem('idempresa', actividad.idcli);
      localStorage.setItem('idprospecto', actividad.idcli);
      localStorage.setItem('razon_soc', actividad.nombre);
      localStorage.setItem('idestado', actividad.idestado);
      localStorage.setItem('servicio', actividad.producto);
      localStorage.setItem('valorpro', actividad.valor);
      localStorage.setItem('telefonoCliente', actividad.telefono);
      localStorage.setItem('contactoCliente', actividad.contacto);
      localStorage.setItem('celularCliente', actividad.celular);
      localStorage.setItem('direccionCliente', actividad.direccion);
      localStorage.setItem('departamentoCliente', actividad.departamento);
      localStorage.setItem('ciudadCliente', actividad.ciudad);



      setTimeout(() => {
        this.$router.push('/pendiente');
      }, 1000);
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

    irGaleriaCampanas() {
      this.$router.push('/VerCampanas');
    },

    irContactos() {
      this.$router.push('/contactos');
    },

    cargarMetaUsu() {
      console.log("Cargando meta para el usuario:", this.idUsuario);
      var data = { id: this.idUsuario };

      axios.post(this.baseURL + 'api/cargarMetaUsu', data)
        .then(response => {
          this.ctaMetaMensual = response.data.data[0].meta;
        })
        .catch(error => {
          console.error('Error al cargar empresas:', error)
        })
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

    filterTel1() {
      if (this.tel1 < 57) {
        this.tel1 = 57;
      }
      if (this.tel1 && this.tel1.length > 12) {
        // Si tiene más de 10 dígitos, truncar el valor
        this.tel1 = this.tel1.slice(0, 12);
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

    filterNumberComercial() {
      if (this.celularComercial < 573) {
        this.celularComercial = 573;
      }

      if (this.celularComercial && this.celularComercial.length > 12) {
        // Si tiene más de 10 dígitos, truncar el valor
        this.celularComercial = this.celularComercial.slice(0, 12);
      }
    },

    // Ejemplos de helpers para usar en plantillas
    formatCOP(v) {
      if (v == null || v === '') return '—'
      const n = Number(v)
      if (Number.isNaN(n)) return String(v)
      return new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(n)
    },

    formatDMY(input) {
      if (!input) return '—'
      let d = new Date(input)
      if (isNaN(+d)) {
        const s = String(input).trim().replace(' ', 'T')
        const d2 = new Date(s)
        if (!isNaN(+d2)) d = d2
      }
      return isNaN(+d)
        ? String(input)
        : d.toLocaleDateString('es-CO', { day: '2-digit', month: '2-digit', year: 'numeric' })
    },

    parseDate(input) {
      if (!input) return null
      const s = String(input).trim()
      // intento 1: ISO friendly
      let d = new Date(s.replace(' ', 'T'))
      if (!isNaN(+d)) return d
      // intento 2: YYYY-MM-DD hh:mmAM/PM
      const m = s.match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{1,2}):(\d{2})(AM|PM)$/i)
      if (m) {
        let [, Y, Mo, D, h, mi, ampm] = m
        let hh = (parseInt(h, 10) % 12) + (ampm.toUpperCase() === 'PM' ? 12 : 0)
        d = new Date(`${Y}-${Mo}-${D}T${String(hh).padStart(2, '0')}:${mi}:00`)
        if (!isNaN(+d)) return d
      }
      return null
    },

    _isBogus1900(d) {
      return d && d.getFullYear() === 1900
    },

    recalcularSinSeguimiento() {
      // Siempre tomar actividades sin seguimiento de los últimos 30 días desde hoy, ignorando los filtros
      const hoy = new Date(); hoy.setHours(0, 0, 0, 0)
      const limite = Number(this.limiteDeDiasSinActividad) || 5
      const hace30dias = new Date(hoy); hace30dias.setDate(hoy.getDate() - 30)

      // Obtener los items originales (sin filtrar por fecha)
      let items = [];
      if (this.itemsSinFiltrar && Array.isArray(this.estadosOriginales)) {
        // Si tienes una copia original de los estados, úsala
        const estadosFiltrados = this.itemsSinFiltrar.filter(e => [2, 3].includes(e.id));
        items = estadosFiltrados.flatMap(e => e.items || []);
      } else {
        // Si no, usa los items actuales
        const estadosFiltrados = this.estados.filter(e => [2, 3].includes(e.id));
        items = estadosFiltrados.flatMap(e => e.items || []);
      }
      const resultado = [];

      const parse = (val) => {
        if (!val) return null
        const s = String(val).trim()
        let d = new Date(s.replace(' ', 'T'))
        if (!isNaN(+d)) { d.setHours(0, 0, 0, 0); return d }
        const m = s.match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{1,2}):(\d{2})(AM|PM)$/i)
        if (m) {
          let [, Y, Mo, D, h, mi, ampm] = m
          let hh = (parseInt(h, 10) % 12) + (ampm.toUpperCase() === 'PM' ? 12 : 0)
          d = new Date(`${Y}-${Mo}-${D}T${String(hh).padStart(2, '0')}:${mi}:00`)
          if (!isNaN(+d)) { d.setHours(0, 0, 0, 0); return d }
        }
        return null
      }
      const is1900 = (d) => d && d.getFullYear() === 1900
      const diffDays = (a, b) => Math.floor((a - b) / 86400000)

      for (const it of items) {
        const ultima = parse(it.fecha)
        let proxima = parse(it.fecproxseg)
        if (is1900(proxima)) proxima = null

        if (!ultima) continue

        // Solo actividades cuya última fecha esté dentro de los últimos 30 días desde hoy
        if (ultima < hace30dias || ultima > hoy) continue;

        const diasDesdeUltima = diffDays(hoy, ultima)
        if (diasDesdeUltima <= limite) continue

        if (proxima && proxima >= hoy) continue
        if (proxima && proxima < hoy) {
          const diasDesdeProxima = diffDays(hoy, proxima)
          if (diasDesdeProxima <= limite) continue
        }

        // Añade todos los campos del item y el campo extra diasSinAct
        resultado.push({
          ...it,
          fechaUlt: it.fecha,
          diasSinAct: diasDesdeUltima,
        })
      }

      this.actividadesSinSeguimiento = resultado
      console.log("actividadesSinSeguimiento", this.actividadesSinSeguimiento)
      this.mostrarAdvertenciaSinActividad = resultado.length > 0
    },

    async mostrarActividadesSinSeguimiento() {
      this.estados.forEach(estado => {
        estado.cantidad = 0;
        estado.total = 0;
        estado.items = [];
      });
      await axios.post(this.baseURL + 'api/cargarlisest', { //BUSCAR MÄS ADELANTE COMO SOLUCIONAR ESTO
        'idprosp': 0,
        'idmedio': 3,
        'idserv': 0,
        'idusu': this.comercialId,
      }).then(response => {
        this.itemsSinFiltrar = Array.isArray(response.data.data) ? response.data.data.slice() : [];
        console.log("Items sin Filtrar: ", this.itemsSinFiltrar);
      })
        .catch(error => {
          console.log(error);
        });
        // Usar todos los items sin filtrar, sin límite de fecha
          const hoy = new Date(); hoy.setHours(0, 0, 0, 0);
          const limite = Number(this.limiteDeDiasSinActividad) || 5;
          const estadosExcluidos = [4, 5, 6];
          const items = Array.isArray(this.itemsSinFiltrar) ? this.itemsSinFiltrar : [];
          const resultado = [];

          const parse = (val) => {
            if (!val) return null;
            const s = String(val).trim();
            let d = new Date(s.replace(' ', 'T'));
            if (!isNaN(+d)) { d.setHours(0, 0, 0, 0); return d; }
            const m = s.match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{1,2}):(\d{2})(AM|PM)$/i);
            if (m) {
              let [, Y, Mo, D, h, mi, ampm] = m;
              let hh = (parseInt(h, 10) % 12) + (ampm.toUpperCase() === 'PM' ? 12 : 0);
              d = new Date(`${Y}-${Mo}-${D}T${String(hh).padStart(2, '0')}:${mi}:00`);
              if (!isNaN(+d)) { d.setHours(0, 0, 0, 0); return d; }
            }
            return null;
          };
          const is1900 = (d) => d && d.getFullYear() === 1900;
          const diffDays = (a, b) => Math.floor((a - b) / 86400000);

          for (const it of items) {
            if (estadosExcluidos.includes(Number(it.idest))) continue;
            // Usar el campo correcto para la última actividad
            const ultima = parse(it.fecha_act || it.fecha);
            let proxima = parse(it.fecproxseg);
            if (is1900(proxima)) proxima = null;
            if (!ultima) continue;
            const diasDesdeUltima = diffDays(hoy, ultima);
            if (diasDesdeUltima <= limite) continue;
            if (proxima && proxima >= hoy) continue;
            if (proxima && proxima < hoy) {
              const diasDesdeProxima = diffDays(hoy, proxima);
              if (diasDesdeProxima <= limite) continue;
            }

            resultado.push({
              idproccom: it.idproc,
              idcli: it.idprosp,

              fecha: it.fecha_act,
              fecproxseg: it.fecproxseg,
              valor: it.valorproy,
              idestado: it.idest,
              telefono: it.telprosp,
              contacto: it.nomcontacto,
              celular: it.nomcelu,
              direccion: it.direccion,
              ciudad: it.nomciudad,
              departamento: it.nomdpto,
              medio: it.medio,
              nombre: it.nombre || it.razon_social || '', // Ajusta según tu backend
              producto: it.producto || it.nomserv || 'Sin Producto',
              ...it,
              fechaUlt: it.fecha_act || it.fecha,
              diasSinAct: diasDesdeUltima,
            });
          }
          this.actividadesSinSeguimiento = resultado;
          this.mostrarAdvertenciaSinActividad = resultado.length > 0;
    },

      /*
    recalcularSinSeguimiento() {
      // Siempre tomar actividades sin seguimiento de los últimos 30 días desde hoy, ignorando los filtros
      const hoy = new Date(); hoy.setHours(0, 0, 0, 0)
      const limite = Number(this.limiteDeDiasSinActividad) || 5
      const hace30dias = new Date(hoy); hace30dias.setDate(hoy.getDate() - 30)

      // Obtener los items originales (sin filtrar por fecha)
      let items = [];
      if (this.itemsSinFiltrar && Array.isArray(this.estadosOriginales)) {
        // Si tienes una copia original de los estados, úsala
        const estadosFiltrados = this.itemsSinFiltrar.filter(e => [2, 3].includes(e.id));
        items = estadosFiltrados.flatMap(e => e.items || []);
      } else {
        // Si no, usa los items actuales
        const estadosFiltrados = this.estados.filter(e => [2, 3].includes(e.id));
        items = estadosFiltrados.flatMap(e => e.items || []);
      }
      const resultado = [];

      const parse = (val) => {
        if (!val) return null
        const s = String(val).trim()
        let d = new Date(s.replace(' ', 'T'))
        if (!isNaN(+d)) { d.setHours(0, 0, 0, 0); return d }
        const m = s.match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{1,2}):(\d{2})(AM|PM)$/i)
        if (m) {
          let [, Y, Mo, D, h, mi, ampm] = m
          let hh = (parseInt(h, 10) % 12) + (ampm.toUpperCase() === 'PM' ? 12 : 0)
          d = new Date(`${Y}-${Mo}-${D}T${String(hh).padStart(2, '0')}:${mi}:00`)
          if (!isNaN(+d)) { d.setHours(0, 0, 0, 0); return d }
        }
        return null
      }
      const is1900 = (d) => d && d.getFullYear() === 1900
      const diffDays = (a, b) => Math.floor((a - b) / 86400000)

      for (const it of items) {
        const ultima = parse(it.fecha)
        let proxima = parse(it.fecproxseg)
        if (is1900(proxima)) proxima = null

        if (!ultima) continue

        // Solo actividades cuya última fecha esté dentro de los últimos 30 días desde hoy
        if (ultima < hace30dias || ultima > hoy) continue;

        const diasDesdeUltima = diffDays(hoy, ultima)
        if (diasDesdeUltima <= limite) continue

        if (proxima && proxima >= hoy) continue
        if (proxima && proxima < hoy) {
          const diasDesdeProxima = diffDays(hoy, proxima)
          if (diasDesdeProxima <= limite) continue
        }

        // Añade todos los campos del item y el campo extra diasSinAct
        resultado.push({
          ...it,
          fechaUlt: it.fecha,
          diasSinAct: diasDesdeUltima,
        })
      }

      this.actividadesSinSeguimiento = resultado
      console.log("actividadesSinSeguimiento", this.actividadesSinSeguimiento)
      this.mostrarAdvertenciaSinActividad = resultado.length > 0
    },
    */

    mostrarSoloClientesSinActividad() {
      this.mostrarSoloSinActividad = !this.mostrarSoloSinActividad;
    },

    daysUntil(dateLike) {
      const d = this.parseDate(dateLike)
      if (!d) return Infinity
      const today = new Date(); today.setHours(0, 0, 0, 0)
      return Math.ceil((d - today) / 86400000) // <=0 -> vencido
    },
    // asigna la clase para colorear la fila completa
    toneClass(item) {
      // si no hay fecha, no pintes
      const d = this.parseDate(item.fecproxseg)
      if (!d) return 'tone--neutral'

      const today = new Date(); today.setHours(0, 0, 0, 0)
      const days = Math.ceil((d - today) / 86400000)

      // vencido -> sin color o gris
      if (days < 0) return this.usarGrisVencido ? 'tone--past' : 'tone--neutral'

      if (days <= 2) return 'tone--urgent'   // rojo suave
      if (days <= 5) return 'tone--soon'     // amarillo suave
      if (days >= 6) return 'tone--safe'     // azul suave
      return 'tone--neutral'                 // 6 días
    },



    // Debounce del input (200ms)
    onSearchInput(val) {
      clearTimeout(this._searchTimer)
      this._searchTimer = setTimeout(() => {
        this.searchProsp = val
      }, 200)
    },

    _normalize(v) {
      return String(v ?? '')
        .toLowerCase()
        .normalize('NFD')
        .replace(/\p{Diacritic}/gu, '')
    },

    _ts(input) {
      if (!input) return -Infinity
      const s = String(input).trim()
      let d = new Date(s.replace(' ', 'T'))
      if (!isNaN(+d)) return d.getTime()
      const m = s.match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{1,2}):(\d{2})(AM|PM)$/i)
      if (m) {
        let [, Y, Mo, D, h, mi, ampm] = m
        let hh = (parseInt(h, 10) % 12) + (ampm.toUpperCase() === 'PM' ? 12 : 0)
        d = new Date(`${Y}-${Mo}-${D}T${String(hh).padStart(2, '0')}:${mi}:00`)
        if (!isNaN(+d)) return d.getTime()
      }
      return -Infinity
    },

    mensajeSegunComercial(comercial) {
      const esMismo = this._normalize(comercial) === this._normalize(this.nombreComercial)
      return esMismo
        ? 'Esta empresa ya se encuentra registrada'
        : `Esta empresa ya se encuentra asignada a: ${comercial}`
    },

    _isDigitsOnly(s) {
      const x = String(s ?? '').trim()
      // permite dígitos y separadores comunes (.,-_/ y espacios)
      return !!x && /^[\d\.\-\_\/\s]+$/.test(x)
    },
    _digitsCanon(s) {
      // solo dígitos y sin ceros a la izquierda
      const d = String(s ?? '').replace(/\D+/g, '')
      return d.replace(/^0+/, '') || '0'
    },
    _normalize(s) {  // deja tu versión mejorada para texto
      return String(s ?? '')
        .toLowerCase()
        .normalize('NFD')
        .replace(/\p{Diacritic}/gu, '')
        .replace(/\s+/g, ' ')
        .trim()
    },
    _equalsName(a, b) {
      const sa = String(a ?? '').trim()
      const sb = String(b ?? '').trim()

      // si ambos son "numéricos"
      if (this._isDigitsOnly(sa) && this._isDigitsOnly(sb)) {
        return this._digitsCanon(sa) === this._digitsCanon(sb)
      }
      // si no, comparación de texto insensible
      return this._normalize(sa) === this._normalize(sb)
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

    async cargarCantidadPendientes() {
    try {
      const idusu = this.idUsuario;
      const response = await axios.post(this.baseURL + 'api/cargarlispend', { idusu });
      const datos = response.data?.data || [];
      let count = 0;

      // Recorre el arreglo recibido y cuenta los pendientes con fecha futura
      datos.forEach(item => {
        if (item.fecproxseg) {
          const fecha = new Date(item.fecproxseg);
          if (!isNaN(fecha)) {
            count++;
          }
        }
      });

      this.cantidadPendientes = count; // Guarda el resultado en una variable reactiva
      console.log('Cantidad de pendientes:', count);
    } catch (error) {
      console.error('Error al cargar datos:', error);
      this.cantidadPendientes = 0;
    }
    },

    getCardCurveStyle(idx, total) {
    // Calcula la posición de la card sobre la curva SVG
    // La curva va de x=40 a x=1160, y=180, con punto medio en x=600
    const minX = 40, maxX = 1160, minY = 180, maxY = 40;
    if (total === 1) {
      return { left: `${minX - 140}px`, top: `${minY - 110}px` };
    }
    const t = idx / (total - 1);
    // Curva cuadrática: y = a(x-h)^2 + k
    // Usamos la ecuación de la SVG: Q300,20 600,180 T1160,180
    // Aproximamos la curva para distribuir las cards
    const x = minX + t * (maxX - minX);
    // Parámetros de la parábola
    const a = (maxY - minY) / Math.pow((maxX - minX) / 2, 2);
    const h = (minX + maxX) / 2;
    const k = maxY;
    const y = a * Math.pow(x - h, 2) + k;
    return {
      left: `${x - 140}px`,
      top: `${y - 110}px`,
    };
  },

  filtrarFechasSinSeguimiento() {
  const hoy = new Date(); hoy.setHours(0,0,0,0);
  const limite = Number(this.limiteDeDiasSinActividad) || 5;
  let actividades = Array.isArray(this.itemsSinFiltrar) ? this.itemsSinFiltrar.slice() : [];
  if (this.mostrarSoloSinActividad) {
    actividades = actividades.filter(item => {
      if (!this.esPendienteSinSeguimiento(item, hoy, limite)) return false;
      if (this.fechaInicioSinSeg && item.fecha_act < this.fechaInicioSinSeg) return false;
      if (this.fechaFinSinSeg && item.fecha_act > this.fechaFinSinSeg) return false;
      return true;
    });
  } else {
    this.fechaInicioSinSeg = '';
    this.fechaFinSinSeg = '';
    actividades = actividades.filter(item => this.esPendienteSinSeguimiento(item, hoy, limite));
  }
  this.actividadesSinSeguimiento = actividades.map(item => ({
    ...item,
    diasSinAct: this.calcularDiasSinActividad(item),
    fechaUlt: item.fecha_act,
    idproccom: item.idproc,
    idcli: item.idprosp,
    fecha: item.fecha_act,
    fecproxseg: item.fecproxseg,
    valor: item.valorproy,
    idestado: item.idest,
    telefono: item.telprosp,
    contacto: item.nomcontacto,
    celular: item.nomcelu,
    direccion: item.direccion,
    ciudad: item.nomciudad,
    departamento: item.nomdpto,
    medio: item.medio,
    nombre: item.nombre || item.razon_social || '',
    producto: item.producto || item.nomserv || 'Sin Producto',
  }));
  },

    calcularDiasSinActividad(item) {
    if (!item) return 0;
    // Usa el campo correcto y parsea robustamente
    const val = item.fecha_act || item.fecha;
    if (!val) return 0;
    // Intenta parsear con hora y sin hora
    let d = new Date(val.replace(' ', 'T'));
    if (isNaN(+d)) {
      // Si falla, intenta solo la fecha
      const soloFecha = val.split(' ')[0];
      d = new Date(soloFecha);
    }
    if (isNaN(+d)) return 0;
    d.setHours(0,0,0,0);
    const hoy = new Date();
    hoy.setHours(0,0,0,0);
    const diffMs = hoy - d;
    return Math.floor(diffMs / (1000 * 60 * 60 * 24));
  },

  esPendienteSinSeguimiento(item, hoy, limite) {
    if ([4,5,6].includes(Number(item.idest))) return false;
    const diasSinAct = this.calcularDiasSinActividad(item);
    if (diasSinAct <= limite) return false;
    // Si hay próxima actividad, verifica si está vencida y también supera el límite
    if (item.fecproxseg) {
      let proxima = new Date(item.fecproxseg.replace(' ', 'T'));
      if (isNaN(+proxima)) {
        const soloFecha = item.fecproxseg.split(' ')[0];
        proxima = new Date(soloFecha);
      }
      proxima.setHours(0,0,0,0);
      if (proxima >= hoy) return false;
      const diasDesdeProxima = Math.floor((hoy - proxima) / (1000 * 60 * 60 * 24));
      if (diasDesdeProxima <= limite) return false;
    }
    return true;
  },

    formatFechaSistema(fecha) {
      if (!fecha) return '—';
      const d = new Date(fecha);
      if (isNaN(d)) return fecha;
      // Devuelve en formato yyyy-mm-dd
      const yyyy = d.getFullYear();
      const mm = String(d.getMonth() + 1).padStart(2, '0');
      const dd = String(d.getDate()).padStart(2, '0');
      return `${yyyy}-${mm}-${dd}`;
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

      // ...agrega más si tienes otras rutas...
      else this.menuActivo = '';
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

.btn-grow-card-items {
  transition: transform 0.2s;
}

.btn-grow-card-items:hover {
  transform: scale(1.01);
  z-index: 1.1;
}

.btn-grow-card-items-active {
  transition: transform 0.2s;
}

.btn-grow-card-items-active:hover {
  background-color: #9e2121 !important;
  /* rojo más oscuro, ajusta el alpha si quieres más intensidad */
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

.scroll-custom::-webkit-scrollbar {
  width: 5px;
  border-radius: 8px;
  background: #e3eafc00;
}

.scroll-custom::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #e2e2e2 60%, #e6e6e6 100%);
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 123, 255, 0.2);
}

.scroll-custom::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #a1a1a1 60%, #e6e6e6 100%);
}

.scroll-custom::-webkit-scrollbar-track {
  background: #f5f7fa00;
  border-radius: 8px;
}

.scroll-custom-v2::-webkit-scrollbar {
  height: 8px;
  border-radius: 8px;
  background: #3e3e3f00;
}

.scroll-custom-v2::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #85848475 60%, #e6e6e685 100%);
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 123, 255, 0.2);
}

.scroll-custom-v2::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #a1a1a1 80%, #e6e6e685 100%);
}

.scroll-custom-v2::-webkit-scrollbar-track {
  border-radius: 8px;
}

.slide-x-enter-active,
.slide-x-leave-active {
  transition: all 0.4s cubic-bezier(.55, 0, .1, 1);
}

.slide-x-enter-from {
  opacity: 0;
  transform: translateX(-60px);
}

.slide-x-leave-to {
  opacity: 0;
  transform: translateX(60px);
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

.header-card {

  color: #fff;
  font-weight: bold;
  font-size: 1.04rem;
  padding: 14px 8px;
  text-align: center;
  letter-spacing: 0.5px;
  position: sticky;
  top: 0;
  z-index: 2;
}

.header-table {
  background: #006CA1;
  position: sticky;
  top: 0;
  z-index: 2;
}

.v-input__prepend .v-icon {
  color: #006CA1;
}


.data-table :deep(th) {
  font-weight: 700;
}

.data-table :deep(td),
.data-table :deep(th) {
  white-space: nowrap;
}

.clamp-2 {
  display: -webkit-box;
  -line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  max-width: 300px;
}

.fancy-headers :deep(.v-table__wrapper > table > thead > tr > th) {
  background-color: #0078b4 !important;
  color: #fff !important;
  font-weight: 700;
  /* bold */
  font-size: 0.85rem;
  /* un poco más grande */
  text-align: center;
  letter-spacing: .2px;
  border-bottom: 2px solid rgba(255, 255, 255, .15);
}

/* 2) Mantener iconos del header en blanco */
.fancy-headers :deep(.v-table__wrapper thead .v-icon) {
  color: #fff !important;
  opacity: .95;
}


/* 4) Alinear contenido (tu contenedor de ícono + texto) */
.th-content {
  display: inline-flex;
  align-items: center;
  text-align: center;
  gap: 8px;
}

/* Zebra + hover + cursor */
.fancy-rows :deep(tbody tr.fancy-row) {
  transition: transform .15s ease, background-color .15s ease, box-shadow .15s ease;
  cursor: pointer;
}

.fancy-rows :deep(tbody tr.fancy-row:nth-child(even)) {
  background-color: rgba(0, 0, 0, 0.005);
}

.fancy-rows :deep(tbody tr.fancy-row:hover) {
  background-color: rgba(0, 108, 161, .06);
  /* azul muy suave */
  transform: translateY(-1px);
  box-shadow: 0 1px 0 rgba(0, 0, 0, .04) inset;
}

/* Bordes sutiles entre filas y más respiración */
.fancy-rows :deep(tbody td) {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(0, 0, 0, .06);
}

/* Alinear números a la derecha (ej. costo) si quieres */
.fancy-rows :deep(tbody td.text-right) {
  text-align: right;
}

.fancy-rows :deep(tbody tr.tone--urgent > td) {
  background-color: rgba(211, 47, 47, 0.05) !important;
  /* #d32f2f @ 8% */
  color: #5c0101 !important;
  /* texto casi negro con tinte rojo */
}

.fancy-rows :deep(tbody tr.tone--urgent:hover > td) {
  background-color: rgba(211, 47, 47, 0.05) !important;
}

/* Próximo (3–5 días): amarillo suave */
.fancy-rows :deep(tbody tr.tone--soon > td) {
  background-color: rgba(251, 193, 45, 0.05) !important;
  /* #fbc02d @ 10% */
  color: #544e01 !important;
}

.fancy-rows :deep(tbody tr.tone--soon:hover > td) {
  background-color: rgba(251, 192, 45, 0.05) !important;
}

/* Seguro (>=7 días): azul como tu ejemplo */
.fancy-rows :deep(tbody tr.tone--safe > td) {
  background-color: rgba(69, 80, 236, 0.05) !important;
  /* #4550ec @ 6% */
  color: #131269 !important;
}

.fancy-rows :deep(tbody tr.tone--safe:hover > td) {
  background-color: rgba(69, 80, 236, 0.12) !important;
}

/* VENCIDO (gris suave) — solo si usarGrisVencido = true */
.fancy-rows :deep(.v-table__wrapper > table > tbody > tr.tone--past > td) {
  background-color: rgba(0, 0, 0, .04) !important;
  /* gris 4% */
  color: #2f2f2f !important;
  /* casi negro */
}

/* Neutro (sin color) */
.fancy-rows :deep(.v-table__wrapper > table > tbody > tr.tone--neutral > td) {
  background-color: transparent !important;
  color: inherit !important;
}

.header-search .v-field {
  background: rgba(255, 255, 255, .12);
}

.header-search .v-field__input,
.header-search .v-icon {
  color: #fff !important;
}

.header-search .v-field__input::placeholder {
  color: rgba(255, 255, 255, .75);
}

.header-search .v-field__outline,
.header-search .v-field__overlay {
  opacity: .18;
}

.empresa-card {
  border-radius: 16px;
  background: linear-gradient(135deg, #f5f7fa 80%, #e3f2fd 100%);
  transition: box-shadow 0.2s, transform 0.2s;
  cursor: pointer;
  min-width: 260px;
  max-width: 370px;
  width: 100%;
  box-sizing: border-box;
}
.empresa-card:hover {
  box-shadow: 0 8px 32px rgba(0, 123, 255, 0.12);
  transform: translateY(-2px) scale(1.01);
}
.empresa-title {
  letter-spacing: 0.5px;
  line-height: 1.1;
  max-width: 100%;
  overflow-wrap: break-word;
}
.empresa-nit {
  font-size: 0.98rem;
  word-break: break-word;
}
.empresa-label {
  font-size: 0.95rem;
}
.empresa-value {
  font-size: 1.05rem;
}

.contact-card-text {
  font-size: 0.9rem; /* tamaño normal para pantallas grandes */
}

@media (max-width: 1040px) {
  .contact-card-text {
    font-size: 0.8rem; /* tamaño reducido para pantallas pequeñas */
  }
}

@media (max-width: 1040px) {
  .empresas-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
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



