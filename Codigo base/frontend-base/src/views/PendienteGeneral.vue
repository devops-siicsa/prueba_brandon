<template>
  <v-app>
    <AppHeader :imagenComercial="imagenComercial" />
    <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">
      <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
        <v-row class="mx-auto my-auto">
        </v-row>
        <v-card
          elevation="6"
          class="shadow-lg"
          style="border-radius: 10px; box-shadow: 0 6px 24px rgba(0,0,0,0.1); padding: 0 0 32px 0; margin-bottom: 18px; border: 1px solid #e0e0e0;"
        >
        <v-card-title class="text-h5 calendar-header-bar">
          <v-icon class="mr-2" size="28">mdi-calendar-month</v-icon>
          <span class="calendar-title">Agenda de Tareas Pendientes</span>
          <v-spacer></v-spacer>
          <!-- Filtro de razón social -->
          <v-autocomplete
            v-model="filtroRazonSocial"
            :items="razonesSociales"
            label="Razón social"
            density="compact"
            variant="solo" bg-color="rgba(255,255,255, 0.9)" base-color="rgba(255,255,255, 0.9)" color="white"
            clearable rounded="lg" hide-details style="max-width: 320px;"
          />
          <!-- Filtro de id de actividad -->
          <v-autocomplete
            v-model="filtroIdActividad"
            :items="idsActividades"
            label="Id Actividad"
            density="compact"
            variant="solo" bg-color="rgba(255,255,255, 0.9)" base-color="rgba(255,255,255, 0.9)" color="white"
            clearable rounded="lg" hide-details style="max-width: 320px;"
          />
          <v-btn-toggle v-model="calendarView" mandatory class="mr-4" color="primary" style="background: #e3f2fd; border-radius: 8px;">
            <v-btn value="today" class="font-weight-bold" prepend-icon="mdi-calendar-today" size="small">Hoy</v-btn>
            <v-btn value="week" class="font-weight-bold"prepend-icon="mdi-calendar-week" size="small">Semana</v-btn>
            <v-btn value="range" class="font-weight-bold"prepend-icon="mdi-calendar-range" size="small">Mes</v-btn>
          </v-btn-toggle>
          <template v-if="calendarView === 'range'">
            <v-menu v-model="menuRangoFechas" :close-on-content-click="false" offset-y>
              <template #activator="{ props }">
                <!--<v-btn v-bind="props" variant="outlined" size="small" color="white">
                  Seleccionar rango
                </v-btn>-->
              </template>
              <v-card>
                <v-card-text>
                  <v-date-picker v-model="rangoFechas" range color="primary"></v-date-picker>
                  <v-btn color="primary" @click="menuRangoFechas = false" class="mt-2">Aceptar</v-btn>
                </v-card-text>
              </v-card>
            </v-menu>
          </template>
          <v-btn icon  variant="text" size="small" @click="goToPrevMonth"><v-icon>mdi-chevron-left</v-icon></v-btn>
          <span class="calendar-month-label">{{ calendarMonthLabel }}</span>
          <v-btn icon @click="goToNextMonth" variant="text" size="small"><v-icon>mdi-chevron-right</v-icon></v-btn>
        </v-card-title>
        <div class="calendar-grid">
          <div class="calendar-weekdays">
            <div v-for="day in weekDays" :key="day" class="calendar-weekday">{{ day }}</div>
          </div>
          <div class="calendar-days" :key="calendarView + '-' + calendarMonth + '-' + calendarYear">
            <div v-for="day in calendarDays" :key="day.date || day.empty" :class="['calendar-day-cell', day.isPast ? 'calendar-day-past' : '', (!day.empty && (!day.items || day.items.length === 0)) ? 'calendar-day-empty' : '']">
              <div v-if="!day.empty" class="calendar-day-header">
                <span class="calendar-day-number" :class="{ 'calendar-today': day.isToday }">{{ day.day }}</span>
                <span class="calendar-day-date-label">{{ day.label }}</span>
              </div>
              <div v-if="!day.empty" class="calendar-day-cards">
                <template v-for="(item, i) in day.items.slice(0,2)" :key="i">
                  <v-tooltip location="right">
                    <template #activator="{ props }">
                      <v-card
                        @click="irPendientes(item)"
                        class="mb-2 px-3 py-2 calendar-task-card btn-grow-card-items"
                        variant="elevated"
                        :class="{
                        }"
                        style="border-radius: 12px; cursor: pointer;"
                        v-bind="props"
                      >
                        <!-- Encabezado con nombre y código -->
                        <div class="d-flex align-center mb-1">
                          <v-avatar color="primary" size="22" class="mr-2">
                            <span style="font-size:0.70rem; color:white;">{{ item.idpcact  || 'N/A' }}</span>
                          </v-avatar>
                          <div class="font-weight-bold" style="font-size: 1.05rem;">
                            {{ item.name }}
                          </div>
                        </div>
                        <!-- Estado y número de tarea -->
                        <div class="d-flex align-center mb-1">
                          <v-chip color="blue-grey" size="small" class="mr-2" label>
                            Estado: {{ estados.find(e => e.id === item.estadoId)?.nombreAct || 'Sin etapa' }}
                          </v-chip>
                          <v-chip color="primary" size="small" class="ml-1" label style="font-weight:600;">
                            Tarea #{{ item.numeroTarea }}
                          </v-chip>
                        </div>
                        <div class="text-caption text-grey-darken-1 mb-1">{{ item.description }}</div>
                        <div v-if="item.date" class="text-caption mt-1 d-flex align-center justify-space-between">
                          <div class="d-flex align-center">
                            <v-icon size="16" class="mr-1" color="#1976D2">{{ getIconForItem(item) }}</v-icon>
                            <span>{{ item.date }}</span>
                          </div>
                          <v-chip v-if="item.isUltima && !item.isPrimera" color="primary" size="small" label style="font-weight:600; margin-left:4px;">
                            Última tarea
                          </v-chip>
                        </div>
                      </v-card>
                    </template>
                    <span>
                      <strong>Contacto:</strong> {{ item.contacto || 'N/A' }}<br>
                      <strong>Teléfono:</strong> {{ item.telefono || 'N/A' }}<br>
                      <strong>Celular:</strong> {{ item.celular || 'N/A' }}<br>
                      <strong>Observación:</strong> {{ item.segobs || 'Sin observación' }}
                    </span>
                  </v-tooltip>
                </template>
                <v-btn v-if="day.items.length > 2" size="x-small" color="primary" style="align-self: flex-end; margin-top: 2px;" @click="showDayDialog(day)">
                  Ver todas ({{ day.items.length }})
                </v-btn>
                <div v-if="day.items.length === 0" class="calendar-no-items">No hay tareas</div>

              <v-dialog v-model="dialogDayItems" max-width="540px" persistent class="dialog-day-items">
                <v-card-title class="text-h6"
                style="background-color: #006CA1; color: white; display: flex; align-items: center;">

                <div class="d-flex align-center">
                  <v-icon class="mr-2">mdi-calendar-month</v-icon>
                  Tareas del {{ selectedDayLabel }}
                </div>

                <v-spacer></v-spacer>
                <v-btn icon="mdi-close" size="small" color="white" @click="dialogDayItems = false" class="btn-grow" />
              </v-card-title>

                <v-card style="border-radius: 4px; box-shadow: 0 2px 12px rgba(0,0,0,0.05);">
                  <v-card-text style="background:#f4f8fb; padding: 18px 18px 8px 18px;">
                    <div v-if="selectedDayItems.length === 0" class="calendar-no-items" style="margin: 32px 0;">No hay tareas</div>
                    <div v-for="(item, i) in selectedDayItems" :key="i" class="mb-3">
                      <v-tooltip location="right">
                        <template #activator="{ props }">
                          <v-card @click="irPendientes(item)" class="px-3 py-2 calendar-task-card-all btn-grow-card-items" variant="elevated"
                            :class="{
                              'ultima-tarea-card': item.isUltimaDia && !item.isPrimeraDia
                            }"
                            style="border-radius: 12px; cursor: pointer;"
                            v-bind="props">
                            <!-- Encabezado con nombre y código -->
                            <div class="d-flex align-center mb-1">
                          <v-avatar color="primary" size="22" class="mr-2">
                            <span style="font-size:0.60rem; color:white;">{{ item.idpcact  || 'N/A' }}</span>
                          </v-avatar>
                          <div class="font-weight-bold" style="font-size: 1.05rem;">
                            {{ item.name }}
                          </div>
                        </div>
                            <!-- Estado y número de tarea -->
                            <div class="d-flex align-center mb-1">
                              <v-chip color="blue-grey" size="small" class="mr-2" label>
                                Estado: {{ estados.find(e => e.id === item.estadoId)?.nombreAct || 'Sin etapa' }}
                              </v-chip>
                              <v-chip color="primary" size="small" class="ml-1" label style="font-weight:600;">
                                Tarea #{{ item.numeroTarea }}
                              </v-chip>
                            </div>
                            <div class="text-caption text-grey-darken-1 mb-1">{{ item.description }}</div>
                            <div v-if="item.date" class="text-caption mt-1 d-flex align-center justify-space-between">
                              <div class="d-flex align-center">
                                <v-icon size="16" class="mr-1" color="#1976D2">{{ getIconForItem(item) }}</v-icon>
                                <span>{{ item.date }}</span>
                              </div>
                              <v-chip v-if="item.isUltimaDia && !item.isPrimeraDia" color="primary" size="small" label style="font-weight:600; margin-left:4px;">
                                Última tarea
                              </v-chip>
                            </div>
                          </v-card>
                        </template>
                        <span>
                          <strong>Contacto:</strong> {{ item.contacto || 'N/A' }}<br>
                          <strong>Teléfono:</strong> {{ item.telefono || 'N/A' }}<br>
                          <strong>Celular:</strong> {{ item.celular || 'N/A' }}<br>
                          <strong>Observación:</strong> {{ item.segobs || 'Sin observación' }}
                        </span>
                      </v-tooltip>
                    </div>
                  </v-card-text>
                  <v-card-actions style="background:#f4f8fb; border-radius:0 0 16px 16px;">
                    <v-spacer></v-spacer>
                    <v-btn class="btn-grow-card" color="primary" variant="text" style="font-weight:600;" @click="dialogDayItems = false">CERRAR</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              </div>
            </div>
          </div>
        </div>
        </v-card>

        <v-dialog v-model="dialogNuevaActividad" max-width="600px" height="100vh" persistent>
          <v-card>

            <v-card-title class="text-h6">Registrar Actividad</v-card-title>

            <v-card-text>

              <!-- Cambios Angelo -->
              <v-row class="mt-n4">
                <v-col>
                  <v-autocomplete label="Cliente" prepend-inner-icon="mdi-domain" v-model="selectedClienteActividad"
                    :items="selectClientesActividad" return-object item-title="nombre" item-value="id"
                    variant="outlined" :readonly="roClienteActividad"></v-autocomplete>
                </v-col>
              </v-row>
              <!-- Cambios Angelo -->

              <v-row class="mt-n4">
                <v-col>
                  Actividad:
                </v-col>
              </v-row>

              <v-row class="mt-n2">
                <v-col>
                  <v-checkbox label="Llamada realizada" prepend-icon="mdi-phone" v-model="cbLlamadaRealizada"
                    color="red" density="compact"></v-checkbox>
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
                    v-model="selectedServicioActividad" :items="selectServiciosActividad" return-object
                    item-title="nombre" item-value="id" variant="outlined"></v-select>
                </v-col>
              </v-row>

              <v-row class="mt-n6" v-if="ifValorProyecto">
                <v-col>
                  <v-text-field label="Valor del Proyecto" clearable prepend-inner-icon="mdi-currency-usd"
                    variant="outlined" v-model="selectedValorProyecto" type="number"></v-text-field>
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

              <v-row class="mt-n6" v-if="ifObservaciones">
                <v-col>
                  <v-btn color="green" text @click="dialogHistorico = true" density="compact"
                    style="float: right;">Histórico</v-btn>
                </v-col>
              </v-row>

              <v-row class="mt-n2" v-if="ifObservaciones">
                <v-col>
                  <v-textarea prepend-inner-icon="mdi-eye" label="Observaciones" rows="4" variant="outlined"
                    density="compact" v-model="selectedObservacionesActividad" clearable></v-textarea>
                </v-col>
              </v-row>

              <v-row class="mt-n2">
                <v-col>
                  <v-select label="Estado actual del cliente" prepend-inner-icon="mdi-list-status"
                    v-model="selectedEstadoActividad" :items="selectEstadosActividad" return-object item-title="nombre"
                    item-value="id" variant="outlined" :readonly="roEstadoActividad"></v-select>
                </v-col>
              </v-row>

              <v-row class="mt-n2" v-if="ifComentariosAdicionales">
                <v-col>
                  <v-textarea prepend-inner-icon="mdi-text-box-outline" label="Comentarios adicionales" rows="4"
                    variant="outlined" density="compact" v-model="selectedComentariosActividad" clearable></v-textarea>
                </v-col>
              </v-row>

              <v-row class="mt-n2">
                <v-col>
                  <v-text-field type="date" clearable label="Próximo seguimiento" prepend-inner-icon="mdi-calendar"
                    v-model="proximoSeguimientoActividad" variant="outlined"></v-text-field>
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
                  <v-checkbox class="mt-n4" label="Cotizar" prepend-icon="mdi-network-pos" v-model="cbCotizar"
                    color="green" density="compact"></v-checkbox>
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

        <v-dialog v-model="dialogCambioClave" persistent max-width="400px">
          <v-card-title class="text-h6" style="background-color: #006CA1; color: white;">
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

        <v-dialog v-model="alerta" persistent>
          <v-card :style="getAlertStyle()">
            <v-progress-circular v-if="ifCargando" color="blue" indeterminate :size="50" :width="5"
              class="mx-auto"></v-progress-circular>
            <v-card-tittle v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-tittle>
            <v-btn class="mt-4 mx-auto" @click="cerrarDIV()" :readonly="ifCargando"
              style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
          </v-card>
        </v-dialog>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppHeader from '../components/AppHeader.vue';
import axios from 'axios';
import CryptoJS from "crypto-js";
export default {
  components: {
    AppHeader
  },
  data() {
    return {
      estados: [
        { id: 1, nombreAct: 'Llamar', items: [] },
        { id: 2, nombreAct: 'Enviar Correo', items: [] },
        { id: 3, nombreAct: 'Visita Presencial', items: [] },
        { id: 4, nombreAct: 'Visita Virtual', items: [] },
        { id: 5, nombreAct: 'Cotizar', items: [] },
        { id: 99, nombreAct: 'Sin etapa', items: [] },
      ],
      baseURL: '',
      idCargo: null,
      dialogNuevaActividad: false,
      selectedClienteActividad: null,
      selectClientesActividad: [],
      calendarYear: new Date().getFullYear(),
      calendarMonth: new Date().getMonth(),
      weekDays: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'],
      dialogDayItems: false,
      selectedDayItems: [],
      selectedDayLabel: '',
      calendarView: 'Range', 
      menuRangoFechas: false,
      rangoFechas: [],
      drawer: false,
      filtroRazonSocial: null,
      razonesSociales: [],
      filtroIdActividad: null,
      idsActividades: [],
      menuAbierto: false, // Estado del menú de usuario
      comercialId: 0,

      menuActivo: null,
    };
  },
  computed: {
    calendarMonthLabel() {
      const date = new Date(this.calendarYear, this.calendarMonth);
      return date.toLocaleString('es-CO', { month: 'long', year: 'numeric' });
    },

    calendarDays() {
  const year = this.calendarYear;
  const month = this.calendarMonth;
  const firstDay = new Date(year, month, 1);
  const lastDay = new Date(year, month + 1, 0);
  const today = new Date();
  const days = [];
  let dayOfWeek = firstDay.getDay();
  dayOfWeek = dayOfWeek === 0 ? 6 : dayOfWeek - 1;
  for (let i = 0; i < dayOfWeek; i++) {
    days.push({ empty: true });
  }
  for (let d = 1; d <= lastDay.getDate(); d++) {
    const dateObj = new Date(year, month, d);
    const dateStr = dateObj.toISOString().slice(0, 10);
    let items = [];
    this.estados.forEach(column => {
      column.items.forEach(item => {
        if (item.date && item.date === dateStr) {
          items.push({ ...item, estadoId: column.id });
        }
      });
    });
    // Filtrar por razón social y/o id actividad
    if (this.filtroRazonSocial) {
      items = items.filter(i => i.razon_social === this.filtroRazonSocial);
    }
    if (this.filtroIdActividad) {
      items = items.filter(i => i.idpcact == this.filtroIdActividad);
    }
    days.push({
      date: dateStr,
      day: d,
      label: dateObj.toLocaleDateString('es-CO', { weekday: 'short' }),
      items,
      isToday: dateObj.toDateString() === today.toDateString(),
      isPast: dateObj < new Date(today.getFullYear(), today.getMonth(), today.getDate()),
    });
  }

  // VISTA HOY: SOLO UNA FILA DE 7 COLUMNAS
  if (this.calendarView === 'today') {
    let weekDay = today.getDay();
    weekDay = weekDay === 0 ? 6 : weekDay - 1;
    const result = Array(7).fill({ empty: true });
    const dateStr = today.toISOString().slice(0, 10);
    const dayObj = days.find(d => d.date === dateStr);
    if (dayObj) result[weekDay] = dayObj;
    return result;
  }

  // VISTA SEMANA: SIEMPRE 7 COLUMNAS
  if (this.calendarView === 'week') {
    const currentDate = new Date();
    let dayOfWeek = currentDate.getDay();
    dayOfWeek = dayOfWeek === 0 ? 6 : dayOfWeek - 1;
    const startOfWeek = new Date(currentDate);
    startOfWeek.setDate(currentDate.getDate() - dayOfWeek);
    const result = [];
    for (let i = 0; i < 7; i++) {
      const d = new Date(startOfWeek);
      d.setDate(startOfWeek.getDate() + i);
      const dateStr = d.toISOString().slice(0, 10);
      const dayObj = days.find(day => day.date === dateStr);
      result.push(dayObj || { empty: true });
    }
    return result;
  }

  // VISTA RANGO: puede tener más de 7 elementos
  if (this.calendarView === 'range' && this.rangoFechas.length === 2) {
    const [start, end] = this.rangoFechas;
    return days.filter(d => {
      if (!d.date) return false;
      return d.date >= start && d.date <= end;
    });
  }

  // VISTA MES: puede tener más de 7 elementos
  return days;
},
},

  mounted() {
    this.baseURL = import.meta.env.VITE_API_BASE_URL;
    this.idCargo = localStorage.getItem('idCargo');
    this.cargarDatos();
    this.cargarClientesActividad();
    this.cargarServiciosActividad();
    this.cargarEstadosActividad();
    this.comercialId = localStorage.getItem('idUsuario');
    this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?${Date.now()}`;

    // Cambios Angelo
    this.nombreComercial = localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin');
    this.idproccom = localStorage.getItem('idproccom');

    setTimeout(() => {
      //this.cargarActividades();
      console.log('ID de Oportunidad:', this.idproccom);
    }, 1000);

  },

  watch: {

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

    calendarView(newValue) {
        if (newValue === 'today' || newValue === 'week') {
          const today = new Date();
          this.calendarMonth = today.getMonth();
          this.calendarYear = today.getFullYear();
        }
      },

  },

  methods: {
    goToPrevMonth() {
      const today = new Date();
      const currentYear = today.getFullYear();
      const currentMonth = today.getMonth();
      // Solo permite retroceder si no estamos en el mes/año actual
      if (
        this.calendarYear > currentYear ||
        (this.calendarYear === currentYear && this.calendarMonth > currentMonth)
      ) {
        if (this.calendarMonth === 0) {
          this.calendarMonth = 11;
          this.calendarYear--;
        } else {
          this.calendarMonth--;
        }
      }
    },
    goToNextMonth() {
      // Solo permite avanzar si la vista es 'range' o 'mes'
      if (this.calendarView === 'today' || this.calendarView === 'week') {
        return;
      }
      if (this.calendarMonth === 11) {
        this.calendarMonth = 0;
        this.calendarYear++;
      } else {
        this.calendarMonth++;
      }
  },
    // Watcher para calendarView: si cambia a 'today' o 'week', regresar al mes y año actual
    getIconForItem(item) {
      switch (item.estadoId) {
        case 1: return 'mdi-phone';
        case 2: return 'mdi-gmail';
        case 3: return 'mdi-calendar-cursor-outline';
        case 4: return 'mdi-monitor-account';
        case 5: return 'mdi-laptop';
        case 6: return 'mdi-point-of-sale';
        default: return 'mdi-calendar';
      }
    },
    irPendientes(item) {
      // Unificar estructura de datos con Comercial.vue
      console.log("item:", item);

      localStorage.setItem('idproccom', item.idproccom ?? item.idproc);
      localStorage.setItem('idempresa', item.idcli ?? item.idprosp);
      localStorage.setItem('idprospecto', item.idcli ?? item.idprosp);
      localStorage.setItem('razon_soc', item.nombre ?? item.razon_social);
      localStorage.setItem('idestado', item.idestado ?? item.idest ?? item.estado ?? null);
      localStorage.setItem('servicio', item.producto);
      localStorage.setItem('valorpro', item.valor);
      localStorage.setItem('telefonoCliente', item.telefono);
      localStorage.setItem('contactoCliente', item.contacto);
      localStorage.setItem('celularCliente', item.celular);
      localStorage.setItem('direccionCliente', item.direccion);
      localStorage.setItem('departamentoCliente', item.departamento);
      localStorage.setItem('ciudadCliente', item.ciudad);
      localStorage.setItem('idprospecto', item.idprospecto ?? item.idprosp);
      localStorage.setItem('valorproy', item.valorproy ?? item.valor);
      localStorage.setItem('rutacot', item.rutacot ?? '');
      localStorage.setItem('rutarut', item.rutarut ?? '');
      
      this.$router.push('/pendiente');
    },

    irPedidos_legacy() {
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

    abrirFormularioActividad(item) {

      this.dialogNuevaActividad = true;
      this.selectedClienteActividad.id = item.idproc;
      console.log('ID del item seleccionado:', item.idproc);

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

      let cbCotizacion = this.cbCotizacion;

      const isValid1 = this.selectClientesActividad && this.idActividad !== null && this.selectedObservacionesActividad && this.selectedEstadoActividad && this.proximoSeguimientoActividad && this.idSeguimiento !== null;

      const isValid2 = this.selectClientesActividad && this.idActividad !== null && this.selectedEstadoActividad && this.proximoSeguimientoActividad && this.idSeguimiento !== null && this.selectServiciosActividad && this.selectedValorProyecto && this.archivoRUT !== null && this.selectedComentariosActividad;

      if (cbCotizacion) {

        if (!isValid2) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos. 1';
          this.alerta = true;
          return;
        }
      } else {
        if (!isValid1) {
          this.mensajeAlertLogin = 'Por favor, complete todos los campos requeridos. 2';
          this.alerta = true;
          return;
        }

      }

      // Cambios Angelo
      let formData = new FormData();
      formData.append('procom', this.idOportunidad);
      formData.append('cli', this.selectedClienteActividad.id);
      formData.append('act', this.idActividad);
      formData.append('obs', this.selectedObservacionesActividad);
      formData.append('estado', this.selectedEstadoActividad.id);
      formData.append('fpseg', this.proximoSeguimientoActividad);
      formData.append('idseg', this.idSeguimiento);
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

    cargarDatos() {
      const id = localStorage.getItem('idUsuario');
      axios.post(this.baseURL + 'api/cargarlispend', {
        idusu: id,
      })
        .then(response => {
          const datos = response.data?.data;
          console.log('Datos cargados:', datos);
          if (!Array.isArray(datos)) {
            console.error('⚠️ La respuesta del servidor no contiene un arreglo válido:', response.data);
            return;
          }
          this.estados.forEach(estado => {
            estado.items = [];
          });
          datos.forEach(item => {
            const etapa = item.nomseg || 'Sin etapa';
            const estadoEncontrado = this.estados.find(e => e.nombreAct === etapa);
            let normalizedDate = null;
            if (item.fecproxseg) {
              const d = new Date(item.fecproxseg);
              if (!isNaN(d)) {
                normalizedDate = d.toISOString().slice(0, 10);
              } else if (typeof item.fecproxseg === 'string' && item.fecproxseg.length >= 10) {
                normalizedDate = item.fecproxseg.slice(0, 10);
              }
            }
            const nuevoItem = {
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
              idprospecto: item.idprosp,
              valorproy: item.valorproy,
              rutacot: item.rutacot,
              rutarut: item.rutarut,
              // Para compatibilidad con la vista anterior
              name: item.razon_social,
              razon_social: item.razon_social,
              description: item.nomserv,
              date: normalizedDate,
              obsev: item.obsev,
              segobs: item.segobs,
              idpcact: item.idpcact,
            };
            if (estadoEncontrado) {
              estadoEncontrado.items.push(nuevoItem);
            } else {
              const sinEtapa = this.estados.find(e => e.nombreAct === 'Sin etapa');
              if (sinEtapa) {
                sinEtapa.items.push(nuevoItem);
              }
            }
          });
          // Recolectar razones sociales e ids de actividad
          datos.forEach(item => {
            const razonSocial = item.razon_social;
            const idActividad = item.idpcact;

            if (!this.razonesSociales.includes(razonSocial)) {
              this.razonesSociales.push(razonSocial);
            }
            if (idActividad && !this.idsActividades.includes(idActividad)) {
              this.idsActividades.push(idActividad);
            }
          });
          // Asignar número de tarea por razón social y fecha
          const allItems = this.estados.flatMap(e => e.items);
          const grupos = {};
          allItems.forEach(item => {
            const key = item.razon_social || item.name || 'SinRazonSocial';
            if (!grupos[key]) grupos[key] = [];
            grupos[key].push(item);
          });
          Object.values(grupos).forEach(grupo => {
            grupo.sort((a, b) => new Date(a.date) - new Date(b.date));
            grupo.forEach((t, idx) => {
              t.numeroTarea = idx + 1;
              t.isPrimera = idx === 0;
              t.isUltima = false;
            });
            if (grupo.length > 0) {
              grupo[grupo.length - 1].isUltima = true;
            }
          });
        })
        .catch(error => {
          console.error('Error al cargar datos:', error);
        });
    },

    // Cambios Angelo
    cargarActividades() {
      const data = {
        idproccom: this.idproccom,
      };

      axios.post(this.baseURL + 'api/cargarprosppend', data)
        .then(response => {
          console.log('Actividades cargadas:', response.data.data);

          const datos = response.data?.data;

          this.estados.forEach(estado => {
            estado.items = [];
          });

          datos.forEach(item => {
            const etapa = item.nomseg || 'Sin etapa';

            const estadoEncontrado = this.estados.find(e => e.nombreAct === etapa);

            // Normalizar fecproxseg a YYYY-MM-DD
            let normalizedDate = null;
            if (item.fecproxseg) {
              const d = new Date(item.fecproxseg);
              if (!isNaN(d)) {
                normalizedDate = d.toISOString().slice(0, 10);
              } else if (typeof item.fecproxseg === 'string' && item.fecproxseg.length >= 10) {
                normalizedDate = item.fecproxseg.slice(0, 10);
              }
            }
            const nuevoItem = {
                name: item.razon_social,
                description: item.nomserv,
                date: normalizedDate,
                idproc: item.idproc,
                obsev: item.obsev,
                obseg: item.obseg,
                idpcact: item.idpcact,
              };

            if (estadoEncontrado) {
              estadoEncontrado.items.push(nuevoItem);
            } else {
              // Si no coincide con ningún estado, lo pone en "Sin etapa"
              const sinEtapa = this.estados.find(e => e.nombreAct === 'Sin etapa');
              if (sinEtapa) {
                sinEtapa.items.push(nuevoItem);
              }
            }
          });
        })
        .catch(error => {
          console.error('Error al cargar actividades:', error);
        });
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
          width: '20%'
        };
      }
    },

    cerrarDIV() {
      this.alerta = false;
    },

    showDayDialog(day) {
        // Marcar primera y última tarea solo para las tareas del día
        const items = day.items.slice();
        items.sort((a, b) => new Date(a.date) - new Date(b.date));
        items.forEach((t, idx) => {
          t.isPrimeraDia = idx === 0;
          t.isUltimaDia = idx === items.length - 1;
        });
        this.selectedDayItems = items;
        this.selectedDayLabel = `${day.day} ${day.label}`;
        this.dialogDayItems = true;
      },


  agruparPorEmpresa(items) {
    const grupos = {};
    items.forEach(item => {
      const key = item.idcli || item.idprospecto || item.idempresa || 'SinID';
      if (!grupos[key]) grupos[key] = [];
      grupos[key].push(item);
    });
    // Ordena cada grupo por fecha ascendente
    Object.values(grupos).forEach(grupo => {
      grupo.sort((a, b) => new Date(a.date) - new Date(b.date));
    });
    return grupos;
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


  }
};
</script>

<style scoped>
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

.calendar-header-bar {
  background-color: #005c8a;
  color: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  padding: 18px 32px 18px 24px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.calendar-title {
  font-size: 1.25rem;
  font-weight: 600;
  letter-spacing: 1px;
}
.calendar-month-label {
  font-size: 1.1rem;
  font-weight: 500;
  margin: 0 12px;
  color: #fff;
}
.calendar-grid {
  background: #f4f8fb;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 12px;
  align-items: stretch;
}
.calendar-day-cell {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  min-height: 120px;
  height: 100%;
  padding: 8px 6px 10px 6px;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: background 0.2s;
}
.calendar-day-past {
  background: #f3f3f313;
}
.calendar-day-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}
.calendar-day-number {
  font-size: 1.1rem;
  font-weight: 700;
  color: #1976D2;
  background: #e3f2fd;
  border-radius: 8px;
  padding: 2px 8px;
}
.calendar-today {
  background: #1976D2;
  color: #fff;
}
.calendar-day-date-label {
  font-size: 0.95rem;
  color: #888;
  font-weight: 500;
}
.calendar-day-cards {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.calendar-task-card {
  border: 2px solid #1976d20a;
  background: #e3f2fd63;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.calendar-task-card-all {
  background: #f8fafc;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.calendar-task-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}

.calendar-task-card-all:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}
.calendar-no-items {
  color: #b0b0b0;
  font-size: 0.98rem;
  margin-top: 8px;
  text-align: center;
}

.calendar-day-empty {
  min-height: 88px !important;
  height: 100% !important;
  max-height: 100% !important;
  padding: 4px 2px !important;
  font-size: 0.85rem;
}

.v-overlay__scrim {
  background: rgba(255,255,255,0.12) !important;
}

/* Estilos para cards de primera y última tarea */
.primera-tarea-card {
  border: 2px solid #43a04810;
  background: #e8f5e97b;
  box-shadow: 0 4px 16px rgba(67, 160, 71, 0.08);
}
.ultima-tarea-card {
  border: 2px solid #1976d214;
  background: #e3f2fd9a;
  box-shadow: 0 4px 16px rgba(25, 118, 210, 0.08);
}
</style>

<style>
/* Solo afecta el dialogo de tareas del calendario en este archivo */
.dialog-day-items .v-overlay__scrim {
  background: rgba(33, 33, 33, 0.137) !important;
}

.ultima-tarea-card {
  border: 2px solid #1976d22f;
  background: #e3f2fd;
  box-shadow: 0 4px 16px rgba(25, 118, 210, 0.08);
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



