<template>
    <v-app>
        <AppHeader :nombre-comercial="nombreComercial" :imagen-comercial="imagenComercial"
            :correo-usuario="correoUsuario" :comercial-id="comercialId" :base-u-r-l="baseURL" :idCargo="idCargo"
            v-model:drawer="drawer" @imagen-actualizada="actualizarImagen" @cerrar-sesion="cerrarSesion" />

        <v-main style="height: 100vh !important; max-height: 100vh !important; overflow-y: auto !important;">

            <v-container fluid class="pa-4 px-4 px-md-6" style="min-height: 100%; height: auto;">
                <!-- Top Controls -->
                <div class="d-flex flex-column flex-md-row justify-space-between align-md-center gap-4 mb-4">
                    <!-- Left: Logo & Title -->
                    <div class="d-flex align-center gap-3" style="min-width: 250px;">
                        <div class="d-flex align-center justify-center rounded-lg elevation-0 mr-4"
                            style="width: 52px; height: 52px; border: 2px solid #E0F2F1;">
                            <v-icon color="#009B90" size="28">mdi-monitor-dashboard</v-icon>
                        </div>
                        <div>
                            <h2 class="text-h5 font-weight-bold text-blue-grey-darken-4 mb-0" style="line-height: 1.2;">
                                CIO</h2>
                            <div class="text-caption font-weight-bold text-uppercase"
                                style="color: #009B90; letter-spacing: 1px;">Centro de Interacción Omnicanal
                            </div>
                        </div>
                    </div>

                    <!-- Center: Search Bar & Clear Filters -->
                    <div class="d-none d-md-flex justify-center align-center flex-grow-1 px-8 gap-3"
                        style="max-width: 750px;">
                        <v-text-field v-model="filtroGlobal" placeholder="Buscar solicitud, cliente o ID..."
                            variant="outlined" density="compact" hide-details bg-color="white" rounded="pill"
                            class="flex-grow-1">
                            <template v-slot:prepend-inner>
                                <v-icon color="grey-darken-1" class="ml-1">mdi-magnify</v-icon>
                            </template>
                            <template v-slot:append-inner>
                                <v-icon color="grey-darken-1" class="mr-2" @click="dialogFiltros = true"
                                    style="cursor: pointer">mdi-filter-variant</v-icon>
                            </template>
                        </v-text-field>

                        <!-- Clear Filters Button -->
                        <v-badge v-if="contadorFiltrosActivos > 0" :content="contadorFiltrosActivos" color="error"
                            overlap>
                            <v-btn icon variant="flat" size="small" @click="limpiarTodosFiltros"
                                class="clear-filters-btn ml-2" elevation="0">
                                <v-icon size="20">mdi-broom</v-icon>
                            </v-btn>
                        </v-badge>
                    </div>

                    <div class="d-flex flex-wrap gap-4 align-center">
                        <!--
                        <v-btn variant="text" color="grey-darken-3" class="text-capitalize font-weight-medium"
                            prepend-icon="mdi-download-outline" @click="exportarDatos">
                            Exportar
                        </v-btn>
                        <v-btn variant="text" color="grey-darken-3" class="text-capitalize font-weight-medium"
                            prepend-icon="mdi-refresh" @click="recargarTickets">
                            Recargar
                        </v-btn>
                        -->

                        <v-divider vertical class="mx-2" style="height: 32px;"></v-divider>

                        <v-btn color="#0D1B2A" class="text-capitalize text-white px-6" prepend-icon="mdi-plus"
                            elevation="0" height="48" rounded="pill"
                            @click="crearPQR = true; estadoCrearPQR = estadosPQRCrear[0]">
                            <span class="font-weight-bold">Nueva Solicitud</span>
                        </v-btn>
                    </div>
                </div>

                <!-- Filters Bar (Tabs) -->
                <div class="d-flex flex-column gap-4 mb-3">
                    <div class="d-flex align-center overflow-x-auto pb-2">
                        <v-card class="d-flex align-center bg-white pa-1 rounded-pill elevation-2 border-0"
                            style="min-width: max-content;">
                            <v-btn variant="flat" class="text-capitalize rounded-pill px-6"
                                :color="(!canalSeleccionado || canalSeleccionado === 'todos') ? 'white' : 'transparent'"
                                :class="{ 'text-grey-darken-4 border': !canalSeleccionado || canalSeleccionado === 'todos', 'text-grey-darken-1': canalSeleccionado && canalSeleccionado !== 'todos' }"
                                @click="canalSeleccionado = 'todos'; filtrarxCanal()" height="44">
                                <v-icon start size="20"
                                    :color="(!canalSeleccionado || canalSeleccionado === 'todos') ? 'grey-darken-1' : 'grey-darken-1'">mdi-view-grid-outline</v-icon>
                                Todos
                                <v-chip size="small" class="ml-2 font-weight-bold rounded-pill"
                                    :color="(!canalSeleccionado || canalSeleccionado === 'todos') ? '#0D1B2A' : 'grey-lighten-3'"
                                    :class="{ 'text-white': !canalSeleccionado || canalSeleccionado === 'todos', 'text-grey-darken-1': canalSeleccionado && canalSeleccionado !== 'todos' }"
                                    variant="flat">
                                    {{ tickets.length }}
                                </v-chip>
                            </v-btn>

                            <v-divider vertical class="mx-2 my-2" inset></v-divider>

                            <v-btn v-for="canal in canales.filter(c => c.id !== 'todos')" :key="canal.id" variant="flat"
                                class="text-capitalize rounded-pill px-5 mx-1"
                                :color="canalSeleccionado === canal.id ? 'teal-lighten-5' : 'transparent'"
                                :class="{ 'text-teal-darken-3 font-weight-bold': canalSeleccionado === canal.id, 'text-grey-darken-1': canalSeleccionado !== canal.id }"
                                @click="canalSeleccionado = canal.id; filtrarxCanal()" height="44">
                                <v-icon start size="22" :icon="canal.icono"
                                    :color="getCanalColorModern(canal.id)"></v-icon>
                                {{ canal.nombre }}
                            </v-btn>
                        </v-card>
                    </div>
                </div>

                <!-- Table Section -->
                <v-card class="rounded-xl border elevation-2 d-flex flex-column" style="overflow-x: auto;">
                    <v-data-table v-model:page="page" :headers="headers" :items="filteredTickets"
                        class="custom-table-modern" :items-per-page="itemsPerPage" hide-default-footer hover
                        style="min-width: 1200px;" @click:row="(event, row) => verTicket(row)">
                        <!-- Custom Header Slot -->
                        <template v-slot:headers="{ columns, isSorted, getSortIcon, toggleSort }">
                            <tr class="sidebar-gradient">
                                <template v-for="column in columns" :key="column.key">
                                    <th class="text-white text-uppercase font-weight-bold text-caption py-4 px-6"
                                        style="background: transparent !important;"
                                        :class="{ 'text-center': ['canal', 'fecha_ingreso', 'ultima_respuesta', 'estado', 'prioridad', 'activo_con'].includes(column.key) }">
                                        {{ column.title }}
                                    </th>
                                </template>
                            </tr>
                        </template>

                        <template #item="{ item, columns, props: rowProps }">
                            <v-tooltip location="top" open-delay="200" max-width="420">
                                <template #activator="{ props: tooltipProps }">
                                    <tr v-bind="{ ...rowProps, ...tooltipProps }"
                                        @click="verTicket({ item: item.raw || item })">
                                        <td v-for="column in columns" :key="column.key"
                                            :class="{ 'text-center': ['canal', 'fecha_ingreso', 'ultima_respuesta', 'estado', 'prioridad', 'activo_con'].includes(column.key) }">

                                            <!-- PQR -->
                                            <span v-if="column.key === 'pqr'"
                                                class="font-weight-bold text-grey-darken-2">#{{ (item.raw || item).pqr
                                                }}</span>

                                            <!-- Categoria -->
                                            <div v-else-if="column.key === 'categoria_pqr'"
                                                class="text-center text-caption text-grey-darken-1">
                                                {{ (item.raw || item).categoria_pqr }}
                                            </div>

                                            <!-- Subcategoria -->
                                            <div v-else-if="column.key === 'subcategoria_pqr'"
                                                class="text-center text-caption text-grey-darken-1">
                                                {{ (item.raw || item).subcategoria_pqr }}
                                            </div>

                                            <!-- Canal -->
                                            <div v-else-if="column.key === 'canal'" class="d-flex justify-center">
                                                <v-icon :icon="getCanalIcono((item.raw || item).canal)"
                                                    :color="getCanalColorModern((item.raw || item).canal)"
                                                    size="24"></v-icon>
                                            </div>

                                            <!-- Fecha Ingreso -->
                                            <div v-else-if="column.key === 'fecha_ingreso'"
                                                class="text-center text-caption text-grey-darken-1">
                                                {{ formatFechaCorta((item.raw || item).fecha_ingreso) }}
                                            </div>

                                            <!-- Ultima Respuesta -->
                                            <div v-else-if="column.key === 'ultima_respuesta'"
                                                class="text-center text-caption text-grey-darken-1">
                                                {{ (item.raw || item).ultima_respuesta ? formatFechaCorta((item.raw ||
                                                    item).ultima_respuesta) : '-' }}
                                            </div>

                                            <!-- Cliente -->
                                            <div v-else-if="column.key === 'cliente'" class="d-flex align-center gap-2">
                                                <v-avatar size="24" color="grey-lighten-3"
                                                    class="text-caption font-weight-bold text-grey-darken-2">
                                                    {{ ((item.raw || item).nombre_cliente || (item.raw || item).usuario
                                                        || '?').charAt(0).toUpperCase() }}
                                                </v-avatar>
                                                <span class="font-weight-medium text-grey-darken-2">{{ (item.raw ||
                                                    item).nombre_cliente || (item.raw || item).usuario || 'Sin nombre'
                                                }}</span>
                                            </div>

                                            <!-- Agente -->
                                            <span v-else-if="column.key === 'agente'" class="text-grey-darken-1">{{
                                                (item.raw || item).agente || 'Sin asignar' }}</span>

                                            <!-- Estado -->
                                            <div v-else-if="column.key === 'estado'" class="text-center">
                                                <v-chip size="small" class="font-weight-bold"
                                                    :color="getEstadoColorModern((item.raw || item).estado).bg"
                                                    :style="`color: ${getEstadoColorModern((item.raw || item).estado).text} !important; border: 1px solid ${getEstadoColorModern((item.raw || item).estado).border}`"
                                                    variant="flat">
                                                    {{ (item.raw || item).estado == 'Suspendido' ? 'Escalado' :
                                                        (item.raw || item).estado }}
                                                </v-chip>
                                            </div>

                                            <!-- Prioridad -->
                                            <div v-else-if="column.key === 'prioridad'" class="text-center">
                                                <v-chip size="small" class="font-weight-bold"
                                                    :color="getPrioridadColorModern((item.raw || item).prioridad).bg"
                                                    :style="`color: ${getPrioridadColorModern((item.raw || item).prioridad).text} !important; border: 1px solid ${getPrioridadColorModern((item.raw || item).prioridad).border}`"
                                                    variant="flat">
                                                    <span v-if="(item.raw || item).prioridad === 'Alta'"
                                                        class="d-inline-block rounded-circle mr-1 bg-red"
                                                        style="width: 6px; height: 6px;"></span>
                                                    {{ (item.raw || item).prioridad }}
                                                </v-chip>
                                            </div>

                                            <!-- Activo con -->
                                            <div v-else-if="column.key === 'activo_con'" class="d-flex justify-center">
                                                <div class="bg-grey-lighten-4 pa-1 rounded-circle btn-grow-card">
                                                    <v-icon :icon="getActivoConIcono((item.raw || item).activo_con)"
                                                        color="grey-darken-1" size="20"></v-icon>
                                                </div>
                                            </div>

                                            <!-- Default -->
                                            <span v-else>
                                                {{ (item.raw || item)[column.key] }}
                                            </span>

                                        </td>
                                    </tr>
                                </template>
                                <div style="white-space: pre-line;">
                                    {{ (item.raw || item).descripcion || (item.raw || item).mensaje || 'Sin mensaje' }}
                                </div>
                            </v-tooltip>
                        </template>
                    </v-data-table>

                    <!-- Custom Footer -->
                    <div
                        class="bg-grey-lighten-5 border-t pa-4 d-flex flex-column flex-sm-row align-center justify-space-between gap-4 text-caption text-grey-darken-1">
                        <div>
                            Mostrando <span class="font-weight-bold text-grey-darken-3">{{ filteredTickets.length > 0 ?
                                ((page - 1) *
                                    itemsPerPage) + 1 : 0
                            }}-{{
                                    Math.min(page * itemsPerPage, filteredTickets.length) }}</span> de <span
                                class="font-weight-bold text-grey-darken-3">{{ filteredTickets.length }}</span>
                            resultados
                        </div>

                        <div class="d-flex align-center gap-6">
                            <div class="d-flex align-center gap-2">
                                <span>Filas por pág:</span>
                                <select v-model="itemsPerPage"
                                    class="border rounded px-2 py-1 bg-white text-caption font-weight-medium focus:border-teal-500"
                                    style="outline: none;">
                                    <option :value="10">10</option>
                                    <option :value="20">20</option>
                                    <option :value="50">50</option>
                                </select>
                            </div>

                            <!-- Pagination Controls (Simplified for visual match) -->
                            <div class="d-flex align-center gap-1">
                                <v-btn icon variant="text" density="compact" size="small" :disabled="page === 1"
                                    @click="page = 1"><v-icon>mdi-chevron-double-left</v-icon></v-btn>
                                <v-btn icon variant="text" density="compact" size="small" :disabled="page === 1"
                                    @click="page--"><v-icon>mdi-chevron-left</v-icon></v-btn>
                                <v-btn icon variant="text" density="compact" size="small"
                                    :disabled="page >= Math.ceil(filteredTickets.length / itemsPerPage)"
                                    @click="page++"><v-icon>mdi-chevron-right</v-icon></v-btn>
                                <v-btn icon variant="text" density="compact" size="small"
                                    :disabled="page >= Math.ceil(filteredTickets.length / itemsPerPage)"
                                    @click="page = Math.ceil(filteredTickets.length / itemsPerPage)"><v-icon>mdi-chevron-double-right</v-icon></v-btn>
                            </div>
                        </div>
                    </div>
                </v-card>
            </v-container>

            <v-dialog v-model="alerta" persistent max-width="600" transition="dialog-bottom-transition">
                <v-card class="alert-card">
                    <v-card-title class="alert-title">
                        <div class="d-flex align-center" style="gap:10px; width:100%;">
                            <v-icon size="22" color="#fff">mdi-bell-ring</v-icon>
                            <div style="flex:1;">
                                <div class="alert-heading">Notificación</div>
                            </div>
                            <div>
                                <v-btn icon small color="white" @click="alerta = false" :disabled="ifCargando">
                                    <v-icon size="18">mdi-close</v-icon>
                                </v-btn>
                            </div>
                        </div>
                    </v-card-title>

                    <v-card-text class="alert-body">
                        <div class="d-flex align-center" style="gap: 16px;">
                            <div style="flex:0 0 auto;">
                                <v-progress-circular v-if="ifCargando" color="white" indeterminate :size="44"
                                    :width="5"></v-progress-circular>
                            </div>
                            <div style="flex:1; color: #072045; font-weight: 500; white-space: pre-wrap;">
                                {{ mensajeAlerta }}
                            </div>
                        </div>
                    </v-card-text>

                    <v-card-actions class="alert-actions">
                        <v-spacer />
                        <v-btn class="btn-apply" small @click="alerta = false" :disabled="ifCargando">Cerrar</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <v-dialog v-model="alertaInteres" persistent max-width="800" transition="dialog-bottom-transition">
                <v-card class="alert-card">
                    <v-card-title class="alert-title">
                        <div class="d-flex align-center" style="gap:10px; width:100%;">
                            <v-icon size="22" color="#fff">mdi-alert</v-icon>
                            <div style="flex:1;">
                                <div class="alert-heading">Alerta</div>
                            </div>
                            <div>
                                <v-btn icon small color="white" variant="text" @click="alertaInteres = false" :disabled="ifCargando">
                                    <v-icon size="18">mdi-close</v-icon>
                                </v-btn>
                            </div>
                        </div>
                    </v-card-title>

                    <v-card-text class="alert-body">
                        <div class="d-flex flex-column" style="gap: 16px;">
                            <div style="color: #072045; font-weight: 500; white-space: pre-wrap;">
                                {{ mensajeAlertInteres }}
                            </div>

                            <v-row dense>
                                <v-col cols="12" md="6">
                                    <v-select v-model="selectedEstadoChat" :items="estadosPQRChat" item-title="nombre"
                                        item-value="id" label="Estado" outlined dense return-object
                                        clearable></v-select>
                                </v-col>

                                <v-col cols="12" md="6">
                                    <v-select v-model="selectedPrioridadChat" :items="prioridadesPQR"
                                        item-title="nombre" item-value="id" label="Prioridad" outlined dense
                                        return-object clearable></v-select>
                                </v-col>

                                <v-col cols="12" v-if="selectedEstadoChat && selectedEstadoChat.id == 4">
                                    <v-autocomplete 
                                        v-model="usuarioEscalarChat" 
                                        :items="usuariosPQREscalar" 
                                        item-title="nombre" 
                                        item-value="id" 
                                        return-object
                                        label="Escalar a un Usuario" 
                                        variant="outlined" 
                                        density="compact" 
                                        clearable
                                    >
                                        <template v-slot:prepend-inner>
                                            <v-icon color="#223551">mdi-account-arrow-right</v-icon>
                                        </template>
                                    </v-autocomplete>
                                </v-col>

                                <v-col cols="12">
                                    <v-textarea 
                                        v-model="observacionChat" 
                                        label="Observaciones de gestión" 
                                        variant="outlined" 
                                        rows="3"
                                        placeholder="Ingrese detalles sobre la gestión realizada..."
                                    ></v-textarea>
                                </v-col>
                            </v-row>
                        </div>

                    </v-card-text>

                    <v-card-actions class="alert-actions mt-n4">
                        <v-spacer />
                        <v-btn class="btn-apply2" small @click="agregarHistorialGestion()"
                            :disabled="!selectedEstadoChat || !selectedPrioridadChat">Guardar</v-btn>
                        <v-btn class="btn-apply" small
                            @click="alertaInteres = false; mensajesAlmacenados = []">Cerrar</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <v-dialog v-model="informacionServicio" fullscreen transition="scale-transition"
                @update:modelValue="onInformacionServicioToggle">
                <v-card class="alert-card">
                    <!-- Header (styled like alerts) -->
                    <v-card-title class="py-2 px-4 alert-title" style="display:flex; align-items:center; gap:8px;">
                        <div class="d-flex align-center">
                            <v-icon size="small" class="mr-2">mdi-folder-question</v-icon>
                            <span class="text-subtitle-1" style="color: #fff;">Información PQR: {{ idPQR }}</span>
                        </div>
                        <v-spacer />
                        <v-btn icon size="30" color="white" variant="text" class="btn-grow" @click="cerrarInfoPQR()">
                            <v-icon size="20">mdi-close</v-icon>
                        </v-btn>
                    </v-card-title>

                    <v-card-text class="pt-1 pb-4 px-4 alert-body">
                        <v-row dense>
                            <!-- Historial -->
                            <v-col cols="12" md="4">
                                <div id="contenido-exportar">
                                    <v-sheet rounded="lg" elevation="1" class="pa-3 overflow-y-auto gap-2"
                                        style="height: 90vh; padding-right: 10px; background: #fafbfc;">
                                        <div class="subheader-dark d-flex align-center mb-2"
                                            style="border-radius:8px; padding:8px 12px;">
                                            <div class="d-flex align-center">
                                                <v-icon size="small" class="mr-2"
                                                    color="white">mdi-calendar-clock-outline</v-icon>
                                                <span class="text-subtitle-1"
                                                    style="color:#fff; font-weight:700;">Histórico</span>
                                            </div>
                                            <v-spacer />
                                            <!-- boton exportar pdf -->
                                            <v-btn class="btn-grow mr-2" size="small" color="#223551"
                                                @click="exportarPDF">
                                                <v-icon size="18">mdi-file-pdf-box</v-icon>
                                                <v-progress-circular v-if="ifCargando2" color="white" indeterminate
                                                    :size="18" :width="2" class="ml-2 mr-4"></v-progress-circular>
                                                Exportar
                                            </v-btn>

                                            <!-- Menu de filtros para el historico -->
                                            <v-menu v-model="menuHistorico" offset-y close-on-click="false" persistent>
                                                <template #activator="{ props }">
                                                    <v-btn v-bind="props" class="btn-grow" size="small" color="#223551"
                                                        style="color:white; margin-right:8px;">
                                                        <v-icon size="18">mdi-filter-variant</v-icon>
                                                        Filtrar
                                                    </v-btn>
                                                </template>

                                                <!-- Contenedor del contenido del menu; usamos un id para adjuntar los menús de los selects aquí -->
                                                <!-- Evitar que eventos de puntero se propaguen hacia el documento y cierren el v-menu padre -->
                                                <v-card id="menu-historico-content"
                                                    style="min-width: 300px; max-width: 420px; overflow: visible;"
                                                    @click.stop @mousedown.stop @pointerdown.stop @touchstart.stop>
                                                    <v-card-text>
                                                        <v-row dense>
                                                            <v-col cols="12">
                                                                <v-select label="Fecha" :items="selectHistoricoFecha"
                                                                    item-title="nombre" item-value="id"
                                                                    v-model="selectedHistoricoFecha" clearable
                                                                    variant="outlined" dense return-object
                                                                    :menu-props="{ attach: '#menu-historico-content', closeOnContentClick: false }"></v-select>
                                                            </v-col>

                                                            <v-col cols="12">
                                                                <v-select label="Usuario"
                                                                    :items="selectHistoricoUsuario" item-title="nombre"
                                                                    item-value="id" v-model="selectedHistoricoUsuario"
                                                                    clearable variant="outlined" dense return-object
                                                                    :menu-props="{ attach: '#menu-historico-content', closeOnContentClick: false }"></v-select>
                                                            </v-col>

                                                            <v-col cols="12">
                                                                <v-select label="Estado" :items="selectHistoricoEstado"
                                                                    item-title="nombre" item-value="id"
                                                                    v-model="selectedHistoricoEstado" clearable
                                                                    variant="outlined" dense return-object
                                                                    :menu-props="{ attach: '#menu-historico-content', closeOnContentClick: false }"></v-select>
                                                            </v-col>
                                                        </v-row>
                                                    </v-card-text>
                                                    <v-divider />
                                                    <v-card-actions>
                                                        <v-btn text color="black"
                                                            @click="limpiarCamposHistorico()">Borrar</v-btn>
                                                        <v-spacer />
                                                        <v-btn color="primary" class="btn-apply"
                                                            @click="filtrarHistorico()">Aplicar</v-btn>
                                                    </v-card-actions>
                                                </v-card>
                                            </v-menu>

                                            <v-btn class="btn-grow" size="small" :disabled="dsGestionManual"
                                                @click="iframeChat = !iframeChat; ifDetallesPQR = !ifDetallesPQR; validarUsuariosDisponibles(); !ifDetallesPQR ? chatLoading = true : null; !ifDetallesPQR ? estadoPQRGrabar = 'En Proceso' : null;"
                                                style="background: #223551; color: #fff;">
                                                <v-icon size="18">mdi-tools</v-icon>
                                                Gestión Manual
                                            </v-btn>
                                        </div>
                                        <div v-for="(item, index) in historico" :key="index" class="mb-4">
                                            <v-card class="pa-4 btn-grow-card-historial" elevation="1"
                                                style="border: 1px solid #ececec; border-radius: 16px; background: #fff;">
                                                <div class="d-flex align-center mb-2">
                                                    <span class="fecha-chip"> <v-icon size="small" class="mr-2">mdi
                                                            mdi-calendar-clock-outline</v-icon> {{ item.fecha }}</span>
                                                </div>
                                                <div class="font-weight-bold mb-1" style="color: #1a1a1a;"
                                                    v-if="item.mensajes_chat === 0">
                                                    <v-avatar size="36" class="mr-2">
                                                        <v-img
                                                            :src="`https://cdn-icons-png.flaticon.com/512/3541/3541871.png`"
                                                            cover />
                                                    </v-avatar>{{ item.usuario }}
                                                </div>
                                                <v-chip
                                                    :color="item.estado === 'Nuevo' ? 'green' : item.estado === 'En Proceso' ? 'blue' : item.estado === 'Suspendido' ? 'orange' : item.estado === 'Resuelto' ? 'red' : 'grey'"
                                                    class="mb-2" size="small" label>
                                                    {{ item.estado == 'Suspendido' ? 'Escalado' : item.estado }}
                                                </v-chip>
                                                <div class="mb-1" style="color: #444;" v-if="item.mensajes_chat === 0">
                                                    {{
                                                        item.observaciones }}</div>
                                                <div class="mt-2" v-if="item.mensajes_chat === 1">
                                                    <template v-if="parseWhatsApp(item.observaciones)">
                                                        <div>
                                                            <template
                                                                v-if="parseWhatsApp(item.observaciones).outgoing === 1">
                                                                <b style="color:#0A1C3A"><v-icon size="small">{{
                                                                    getIconByChannel(item.canal) }}</v-icon> {{
                                                                            item.usuario
                                                                        }}
                                                                    dijo:</b>
                                                            </template>
                                                            <template
                                                                v-else-if="parseWhatsApp(item.observaciones).outgoing === 0">
                                                                <b style="color:purple"><v-icon size="small">{{
                                                                    getIconByChannel(item.canal) }}</v-icon> Cliente
                                                                    dijo:</b>
                                                            </template>
                                                            <template v-else>
                                                                <b>Mensaje:</b>
                                                            </template>
                                                        </div>
                                                        <div style="margin-top:2px;">
                                                            <div v-if="parseWhatsApp(item.observaciones).tipo === 'text'"
                                                                style="white-space: pre-line;">
                                                                <span v-if="!expandedMessages[i]">
                                                                    {{
                                                                        truncateText(removeHeader(parseWhatsApp(item.observaciones).mensaje),
                                                                            180)
                                                                    }}
                                                                    <template
                                                                        v-if="shouldShowExpand(parseWhatsApp(item.observaciones).mensaje, 180)">
                                                                        <v-icon size="18" color="#223551"
                                                                            style="cursor:pointer; vertical-align:middle;"
                                                                            @click="expandedMessages = { ...expandedMessages, [i]: true }"
                                                                            title="Ver más">mdi-eye</v-icon> <strong
                                                                            @click="expandedMessages = { ...expandedMessages, [i]: true }">Ver
                                                                            más</strong>
                                                                    </template>
                                                                </span>
                                                                <span v-else>
                                                                    {{
                                                                        removeHeader(parseWhatsApp(item.observaciones).mensaje)
                                                                    }}
                                                                    <v-icon size="18" color="#223551"
                                                                        style="cursor:pointer; vertical-align:middle;"
                                                                        @click="expandedMessages = { ...expandedMessages, [i]: false }"
                                                                        title="Ver menos">mdi-eye-off</v-icon> <strong
                                                                        @click="expandedMessages = { ...expandedMessages, [i]: false }">Ver
                                                                        menos</strong>
                                                                </span>
                                                            </div>
                                                            <img v-else-if="parseWhatsApp(item.observaciones).tipo === 'image'"
                                                                :src="parseWhatsApp(item.observaciones).mensaje"
                                                                alt="Imagen"
                                                                style="max-width:220px; max-height:220px; border-radius:8px; box-shadow:0 2px 8px #888; margin-top:6px; display:block;" />
                                                            <audio
                                                                v-else-if="parseWhatsApp(item.observaciones).tipo === 'audio'"
                                                                controls
                                                                style="margin-top:6px; max-width:220px; display:block;">
                                                                <source
                                                                    :src="parseWhatsApp(item.observaciones).mensaje">
                                                            </audio>
                                                            <video
                                                                v-else-if="parseWhatsApp(item.observaciones).tipo === 'video'"
                                                                controls
                                                                style="margin-top:6px; max-width:220px; display:block;">
                                                                <source
                                                                    :src="parseWhatsApp(item.observaciones).mensaje">
                                                            </video>
                                                            <a v-else-if="parseWhatsApp(item.observaciones).tipo === 'document'"
                                                                :href="parseWhatsApp(item.observaciones).mensaje"
                                                                target="_blank"
                                                                style="color:#223551; text-decoration:underline; display:block; margin-top:6px;">{{
                                                                    getFileName2(parseWhatsApp(item.observaciones).mensaje)
                                                                }}</a>
                                                            <span v-else>{{ parseWhatsApp(item.observaciones).mensaje
                                                            }}</span>
                                                        </div>
                                                    </template>
                                                    <template v-else>
                                                        {{ item.observaciones }}
                                                    </template>
                                                </div>
                                                <div class="mb-2" style="font-size: 13px; color: #888;"
                                                    v-if="item.mensajes_chat === 0">
                                                    <span v-if="item.archivos.length">
                                                        <!-- necesitamos mostrar para cada archivo, un icono de un documento, con su nombre al lado y que sea seleccionable como hipervinculo-->
                                                        <div v-for="(archivo, idx) in item.archivos" :key="idx">
                                                            <v-icon size="small" class="mr-1"
                                                                color="#223551">mdi-file</v-icon>
                                                            <a :href="archivo" target="_blank"
                                                                style="color: #223551; text-decoration: underline;">
                                                                {{ getFileName(archivo) }}
                                                            </a>
                                                        </div>
                                                    </span>
                                                    <span v-else>Sin archivos</span>
                                                </div>
                                            </v-card>
                                        </div>
                                        <div v-if="!historico.length" class="text-medium-emphasis text-caption">
                                            Aún no hay registros.
                                        </div>
                                    </v-sheet>
                                </div>
                            </v-col>

                            <!-- Formulario (Derecha) -->
                            <v-col cols="12" md="8">
                                <v-sheet rounded="lg" elevation="1" class="pa-3 mb-4"
                                    style="height: 90vh; background: #fafbfc;">

                                    <v-row class="align-center justify-space-between">
                                        <!-- COLUMNA IZQUIERDA: Chips -->
                                        <v-col cols="12" md="9">
                                            <transition-group name="chips" tag="div" class="estado-chips mr-2"
                                                v-if="!ifDetallesPQR">

                                                <v-chip key="label" v-if="chipsVisible" class="estado-chip"
                                                    color="black">
                                                    Estado Grabación:
                                                </v-chip>

                                                <v-chip key="enproceso"
                                                    v-if="chipsVisible && (!estadoPQRGrabar || estadoPQRGrabar === 'En Proceso')"
                                                    class="estado-chip2"
                                                    :class="{ 'chip-active-enproceso-grabar': estadoPQRGrabar === 'En Proceso' }"
                                                    @click="setEstadoPQRGrabar('En Proceso')" outlined>
                                                    <v-icon size="18" class="mr-1"
                                                        v-if="estadoPQRGrabar === 'En Proceso'">mdi-pencil</v-icon>
                                                    En proceso
                                                </v-chip>

                                                <v-chip key="nuevo"
                                                    v-if="chipsVisible && (!estadoPQRGrabar || estadoPQRGrabar === 'Escalar')"
                                                    class="estado-chip2"
                                                    :class="{ 'chip-active-escalar-grabar': estadoPQRGrabar === 'Escalar' }"
                                                    @click="setEstadoPQRGrabar('Escalar')" outlined>
                                                    <v-icon size="18" class="mr-1"
                                                        v-if="estadoPQRGrabar === 'Escalar'">mdi-pencil</v-icon>
                                                    Escalar
                                                </v-chip>

                                                <v-chip key="resuelto"
                                                    v-if="chipsVisible && (!estadoPQRGrabar || estadoPQRGrabar === 'Resuelto')"
                                                    class="estado-chip2"
                                                    :class="{ 'chip-active-resuelto-grabar': estadoPQRGrabar === 'Resuelto' }"
                                                    @click="setEstadoPQRGrabar('Resuelto')" outlined>
                                                    <v-icon size="18" class="mr-1"
                                                        v-if="estadoPQRGrabar === 'Resuelto'">mdi-pencil</v-icon>
                                                    Resuelto
                                                </v-chip>

                                            </transition-group>
                                        </v-col>

                                        <!-- COLUMNA DERECHA: Iconos sociales -->
                                        <v-col cols="12" md="3" class="d-flex justify-end align-center">

                                            <!-- WhatsApp -->
                                            <v-btn :disabled="disablediconoWhastapp" icon variant="text"
                                                @click="onWhatsapp">
                                                <v-icon size="28" color="green">mdi-whatsapp</v-icon>
                                            </v-btn>

                                            <!-- Messenger -->
                                            <v-btn :disabled="disablediconoMessenger" icon variant="text"
                                                @click="onMessenger">
                                                <v-icon size="28" color="blue">mdi-facebook-messenger</v-icon>
                                            </v-btn>

                                            <!-- Instagram -->
                                            <v-btn :disabled="disablediconoInstagram" icon variant="text"
                                                @click="onInstagram">
                                                <v-icon size="28" color="purple">mdi-instagram</v-icon>
                                            </v-btn>

                                        </v-col>
                                    </v-row>


                                    <transition name="slide-y-reverse-transition">
                                        <div class="chat-wrapper"
                                            style="position:relative; width:100%; display:flex; justify-content:center;">
                                            <!-- Render the iframe when iframeChat is true so @load can fire even if a loader is visible -->
                                            <iframe id="iframeChatID" v-if="iframeChat" :src="urlChat"
                                                transition="scroll-y-reverse-transition" :style="getChatStyle()"
                                                frameborder="0" class="chat-iframe mt-2" @load="onIframeLoaded">
                                            </iframe>

                                            <!-- Overlay loader: visible while chatLoading -->
                                            <div v-if="chatLoading" class="chat-loader-overlay">
                                                <div class="chat-loader-content">
                                                    <v-progress-circular indeterminate size="56" width="6"
                                                        color="#223551"></v-progress-circular>
                                                    <div style="color:#444; font-weight:600; margin-top:8px;">
                                                        Cargando chat...</div>
                                                </div>
                                            </div>
                                        </div>
                                    </transition>

                                    <div v-if="ifDetallesPQR"
                                        style="height: 100%; overflow-y: auto; overflow-x: hidden;">
                                        <!-- Detalles del PQR -->
                                        <div class="subheader-dark subheader-center mb-2"
                                            style="border-radius:8px; padding:8px 12px;">
                                            <div class="d-flex align-center">
                                                <v-icon size="small" class="mr-2"
                                                    color="white">mdi-information-outline</v-icon>
                                                <span class="text-subtitle-1"
                                                    style="color:#fff; font-weight:700;">Detalles del PQR</span>
                                            </div>
                                        </div>
                                        <!-- subtitulo indicando que el ticket está resuelto -->
                                        <div v-if="estadoItemSeleccionado === 'Resuelto'"
                                            class="d-flex text-subtitle-1 font-weight-bold mb-2 justify-center">
                                            <span style="font-size: 0.7rem; color: red; text-align: center;">Este ticket
                                                está
                                                marcado como <strong>Resuelto</strong>. No se pueden realizar más
                                                cambios.
                                            </span>
                                        </div>
                                        <v-row class="mb-n6">
                                            <v-col cols="12">
                                                <v-textarea readonly label="Descripción" v-model="descripcionServicio"
                                                    variant="outlined" class="mt-2 mb-2" no-resize rows="4"
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-clipboard</v-icon>
                                                    </template>
                                                </v-textarea>
                                            </v-col>
                                            <v-col cols="12">
                                                <v-select label="Documentos relacionados por el cliente"
                                                    :items="documentosCliente" v-model="documentoSeleccionadoCliente"
                                                    item-title="nombre" item-value="nombre" clearable variant="outlined"
                                                    @update:modelValue="abrirDocumentoCliente()" class="mt-n8"
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-file</v-icon>
                                                    </template>
                                                </v-select>
                                            </v-col>
                                        </v-row>
                                        <v-divider class="my-4" />
                                        <!-- Gestión Manual -->
                                        <div class="subheader-dark subheader-center mb-2"
                                            style="border-radius:8px; padding:8px 12px;">
                                            <div class="d-flex align-center justify-center" style="width:100%;">
                                                <v-icon size="small" class="mr-2" color="white">mdi-tools</v-icon>
                                                <span class="text-subtitle-1"
                                                    style="color:#fff; font-weight:700;">Gestión Manual</span>
                                            </div>
                                        </div>
                                        <!-- subtitulo pequeño de informacion -->
                                        <div class="d-flex text-subtitle-1 font-weight-bold mb-2 justify-center">
                                            <span style="font-size: 0.7rem; color: #555; text-align: center;">Utiliza
                                                estos
                                                campos
                                                para gestionar una observación si no has interactuado con el cliente
                                                mediante el
                                                chat.</span>
                                        </div>
                                        <v-row>
                                            <v-col cols="12" md="6">
                                                <v-select return-object item-title="nombre" item-value="id"
                                                    v-model="estadoServicio" :items="estadosPQR" variant="outlined"
                                                    clearable label="Estado" class="mt-2 mb-2"
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-list-status</v-icon>
                                                    </template>
                                                </v-select>
                                            </v-col>
                                            <v-col cols="12" md="6">
                                                <v-select return-object item-title="nombre" item-value="id"
                                                    v-model="prioridadPQR" :items="prioridadesPQR" variant="outlined"
                                                    clearable label="Prioridad" class="mt-2 mb-2"
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-priority-high</v-icon>
                                                    </template>
                                                </v-select>
                                            </v-col>
                                            <v-col cols="12"
                                                v-if="estadoServicio ? estadoServicio.id == 4 ? true : false : false">
                                                <v-autocomplete return-object item-title="nombre" item-value="id"
                                                    v-model="usuarioEscalar" :items="usuariosPQREscalar"
                                                    variant="outlined" clearable label="Escalar a un Usuario"
                                                    class="mt-n8 mb-2"
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-account</v-icon>
                                                    </template>
                                                </v-autocomplete>
                                            </v-col>
                                            <v-col cols="12"
                                                v-if="estadoServicio ? estadoServicio.id != 4 ? true : false : true">
                                                <v-autocomplete return-object item-title="nombre" item-value="id"
                                                    v-model="usuarioAsignado" :items="usuariosPQRAsignar"
                                                    variant="outlined" clearable label="Asignar Usuario"
                                                    class="mt-n8 mb-2"
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-account</v-icon>
                                                    </template>
                                                </v-autocomplete>
                                            </v-col>
                                            <v-col cols="12">
                                                <v-textarea label="Respuesta del asesor" v-model="respuestaAsesor"
                                                    variant="outlined" clearable class="mt-n8 mb-2" rows="4" no-resize
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-text-box-check</v-icon>
                                                    </template>
                                                </v-textarea>
                                            </v-col>
                                            <v-col cols="12">
                                                <v-file-input multiple clearable label="Adjuntar archivos"
                                                    prepend-icon="" v-model="archivosRespuestaPQR" variant="outlined"
                                                    show-size class="mt-n8 mb-2"
                                                    :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                    <template v-slot:prepend-inner>
                                                        <v-icon color="#223551">mdi-paperclip</v-icon>
                                                    </template>
                                                </v-file-input>
                                            </v-col>
                                        </v-row>
                                        <div class="d-flex align-center justify-end mt-n6 gap-2"
                                            v-if="estadoItemSeleccionado !== 'Resuelto'">
                                            <v-btn color="primary" class="btn-grow" @click="guardarRespuestaPQR()"
                                                :disabled="estadoItemSeleccionado === 'Resuelto'">
                                                Guardar
                                            </v-btn>
                                        </div>
                                    </div>
                                </v-sheet>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-dialog>

            <v-dialog v-model="crearPQR" max-width="600" style="z-index: 1100;">
                <v-card class="rounded-xl elevation-3">
                    <!-- Header Moderno -->
                    <v-card-title class="px-6 py-4 bg-white d-flex align-center justify-space-between border-b">
                        <div>
                            <div class="text-h5 font-weight-bold text-blue-grey-darken-4">
                                Nueva Solicitud PQR
                            </div>
                            <div class="text-caption text-grey-darken-1 mt-1">
                                Registre los detalles del caso.
                            </div>
                        </div>
                        <v-btn icon variant="text" color="grey" @click="cerrarCrearPQR()">
                            <v-icon>mdi-close</v-icon>
                        </v-btn>
                    </v-card-title>

                    <v-card-text class="pa-4 bg-grey-lighten-5">
                        <v-row dense>
                            <!-- Columna Izquierda -->
                            <v-col cols="12" md="6">
                                <label class="input-label">CLIENTE / EMPRESA</label>
                                <v-autocomplete v-model="clienteCrearPQR" :items="clientesPQR" item-title="nombre"
                                    item-value="id" return-object variant="outlined" density="compact"
                                    placeholder="Buscar cliente..." hide-details="auto" class="mb-3 rounded-lg bg-white"
                                    color="primary" :rules="[rules.required]">
                                    <template v-slot:prepend-inner>
                                        <v-icon color="primary" size="20">mdi-account-outline</v-icon>
                                    </template>
                                </v-autocomplete>

                                <label class="input-label">ASIGNAR USUARIO</label>
                                <v-autocomplete v-model="usuarioAsignadoCrear" :items="usuariosPQR" item-title="nombre"
                                    item-value="id" return-object variant="outlined" density="compact"
                                    placeholder="Seleccionar usuario..." hide-details="auto"
                                    class="mb-3 rounded-lg bg-white" color="primary" :rules="[rules.required]">
                                    <template v-slot:prepend-inner>
                                        <v-icon color="grey" size="20">mdi-account-plus-outline</v-icon>
                                    </template>
                                </v-autocomplete>

                                <label class="input-label">CATEGORÍA</label>
                                <v-autocomplete v-model="categoriaCrearPQR" :items="listaCategoriasPQR"
                                    item-title="nombre" item-value="id" return-object variant="outlined"
                                    density="compact" placeholder="Seleccionar..." hide-details="auto"
                                    class="mb-3 rounded-lg bg-white" color="primary">
                                    <template v-slot:prepend-inner>
                                        <v-icon color="purple" size="20">mdi-shape</v-icon>
                                    </template>
                                </v-autocomplete>
                            </v-col>

                            <!-- Columna Derecha -->
                            <v-col cols="12" md="6">
                                <label class="input-label">ESTADO</label>
                                <v-select v-model="estadoCrearPQR" :items="estadosPQRCrear" item-title="nombre"
                                    item-value="id" return-object variant="outlined" density="compact"
                                    hide-details="auto" class="mb-3 rounded-lg bg-white" color="primary"
                                    :rules="[rules.required]">
                                    <template v-slot:prepend-inner>
                                        <v-icon color="green" size="20">mdi-check-circle-outline</v-icon>
                                    </template>
                                    <template v-slot:selection="{ item }">
                                        <span class="text-green-darken-1 font-weight-bold">{{ item.title }}</span>
                                    </template>
                                </v-select>

                                <label class="input-label">PRIORIDAD</label>
                                <v-select v-model="prioridadPQR" :items="prioridadesPQR" item-title="nombre"
                                    item-value="id" return-object variant="outlined" density="compact"
                                    placeholder="Seleccionar..." hide-details="auto" class="mb-3 rounded-lg bg-white"
                                    color="primary" :rules="[rules.required]">
                                    <template v-slot:prepend-inner>
                                        <v-icon color="orange" size="20">mdi-lightning-bolt-outline</v-icon>
                                    </template>
                                </v-select>

                                <label class="input-label">SUBCATEGORÍA</label>
                                <v-autocomplete v-model="subcategoriaCrearPQR" :items="subcategoriasFiltradas"
                                    item-title="nombre" item-value="id" return-object :disabled="!categoriaCrearPQR"
                                    variant="outlined" density="compact" placeholder="Seleccionar..."
                                    hide-details="auto" class="mb-3 rounded-lg bg-white" color="primary">
                                    <template v-slot:prepend-inner>
                                        <v-icon color="purple-lighten-2" size="20">mdi-shape-outline</v-icon>
                                    </template>
                                </v-autocomplete>
                            </v-col>

                            <!-- Descripción (Full Width) -->
                            <v-col cols="12">
                                <label class="input-label">DESCRIPCIÓN DEL CASO</label>
                                <v-textarea v-model="descripcionCrearPQR" auto-grow variant="outlined" density="compact"
                                    placeholder="Detalle la solicitud..." rows="2" hide-details="auto"
                                    class="mb-3 rounded-lg bg-white" color="primary" :rules="[rules.required]">
                                    <template v-slot:prepend-inner>
                                        <v-icon color="grey" size="20" class="mt-1">mdi-text-short</v-icon>
                                    </template>
                                </v-textarea>
                            </v-col>

                            <!-- Respuesta (Full Width) -->
                            <v-col cols="12">
                                <label class="input-label">INDICACIONES DEL ASESOR</label>
                                <v-textarea v-model="respuestaCrearPQR" auto-grow variant="outlined" density="compact"
                                    placeholder="Ingrese observaciones, pasos técnicos o notas de gestión..." rows="2"
                                    hide-details="auto" class="mb-3 rounded-lg bg-white" color="primary" clearable>
                                    <template v-slot:prepend-inner>
                                        <v-icon color="grey" size="20"
                                            class="mt-1">mdi-file-document-edit-outline</v-icon>
                                    </template>
                                </v-textarea>
                            </v-col>

                            <!-- Archivo (Full Width) -->
                            <v-col cols="12">
                                <label class="input-label">ADJUNTAR ARCHIVO</label>
                                <v-file-input v-model="archivoCrearPQR" multiple clearable variant="outlined"
                                    density="compact" label="Seleccione o arrastre y suelte el archivo" prepend-icon=""
                                    prepend-inner-icon="mdi-paperclip" hide-details="auto" class="rounded-lg bg-white"
                                    color="primary"></v-file-input>
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions class="pa-4 bg-white">
                        <v-spacer></v-spacer>
                        <v-btn variant="text" color="grey-darken-1" class="text-capitalize mr-2"
                            @click="cerrarCrearPQR()">
                            Cancelar
                        </v-btn>
                        <v-btn :disabled="!isFormValid" :color="isFormValid ? '#223551' : undefined"
                            :class="['text-capitalize px-6 rounded-lg font-weight-bold', isFormValid ? 'text-white' : 'text-grey']"
                            variant="flat" elevation="0" height="44" @click="guardarPQR()">
                            Crear Solicitud
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>


            <v-dialog v-model="dialogPreguntasF" max-width="70%" height="100%" persistent>
                <v-card class="pa-2 rounded-xl" style="background-color: #F0F4F8;">
                    <v-card-title class="text-h6 text-primary">
                        Preguntas Frecuentes
                        <v-btn color="#223551" @click="dialogPreguntaNueva = true" style="float: right;"><v-icon
                                class="mr-2">mdi-plus</v-icon>
                            Agregar una pregunta</v-btn>
                    </v-card-title>
                    <v-card-subtitle class="text-subtitle-1 mt-2" style="color: #0A1C3A">
                        Configura las preguntas y respuestas que tu bot podrá usar para responder automaticamente a tus
                        clientes.
                    </v-card-subtitle>
                    <v-card-text>
                        <v-row>
                            <v-col>
                                <v-select v-model="selectedCategoriaFiltro" :items="selectRol" item-title="nombre"
                                    item-value="id" return-object label="Categoría" color="blue" class="mb-4" clearable
                                    prepend-inner-icon="mdi-menu" density="compact"></v-select>
                            </v-col>

                            <v-col>
                                <v-text-field v-model="filtroPreguntasF" label="Buscar pregunta"
                                    prepend-inner-icon="mdi-magnify" color="blue" clearable density="compact" />
                            </v-col>

                            <v-col>
                                <v-btn color="#223551" @click="" style="float: right;">
                                    <v-icon icon="mdi-file-excel" class="mr-2"></v-icon>
                                    Exportar
                                </v-btn>
                            </v-col>
                        </v-row>

                        <v-row class="mt-n10">
                            <v-col>
                                <v-data-table :headers="headersPreguntasF" :items="preguntasF"
                                    :search="filtroPreguntasF"
                                    class="elevation-1 data-table-campanas fancy-headers fancy-rows-campanas"
                                    items-per-page-text="Preguntas por página" items-per-page="10"
                                    :items-per-page-options="[10, 20, 30]" style="height: 100%;"
                                    page-text="Preguntas de la ({0}) a la ({1}) de ({2})">

                                    <!--DATA  HEADERS-->
                                    <template #header.pregunta="{ column }">
                                        <div class="th-content">
                                            <v-icon size="16" class="mr-2"
                                                color="#ffffff">mdi-comment-question-outline</v-icon>
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
                                            <v-icon size="16" class="mr-2"
                                                color="#ffffff">mdi-shield-account-outline</v-icon>
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
                                            <v-icon size="16" class="mr-2"
                                                color="#ffffff">mdi-comment-check-outline</v-icon>
                                            <span>{{ column.title }}</span>
                                        </div>
                                    </template>

                                    <template #header.usuario="{ column }">
                                        <div class="th-content">
                                            <v-icon size="16" class="mr-2" color="#ffffff">mdi
                                                mdi-account-search</v-icon>
                                            <span>{{ column.title }}</span>
                                        </div>
                                    </template>
                                    <template v-slot:item.categoria="{ item }">
                                        <div size="small"> {{ getCategoríaNombre(item.categoria) }}
                                        </div>
                                    </template>
                                    <template v-slot:item.estado="{ item }">
                                        <v-chip
                                            :color="item.estado === 1 ? 'green' : item.estado === 0 ? 'red' : 'blue'"
                                            size="small"> {{ getEstadoNombre(item.estado) }}
                                        </v-chip>
                                    </template>
                                    <template v-slot:item.prioridad="{ item }">
                                        <v-chip
                                            :color="item.prioridad === 'Alta' ? 'red' : item.prioridad === 'Media' ? 'orange' : 'green'"
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
                                            <v-chip v-if="item.rolactivo === 0" color="red lighten-4" text-color="red"
                                                size="x-small" class="mr-1" style="font-weight: bold;">
                                                Rol inactivo
                                            </v-chip>
                                            {{ getCategoríaNombre(item.idrol) }}
                                        </span>
                                    </template>
                                    <template v-slot:item.opciones="{ item }">
                                        <v-tooltip text="Editar Pregunta Frecuente" location="top">
                                            <template #activator="{ props }">
                                                <div class="justify-center d-flex">
                                                    <v-btn v-bind="props" size="35" icon color="primary"
                                                        @click="editarItemPregunta(item)" class="btn-grow-card">
                                                        <v-icon size="15">mdi-pencil</v-icon>

                                                    </v-btn>
                                                </div>
                                            </template>
                                        </v-tooltip>

                                    </template>

                                </v-data-table>
                            </v-col>
                        </v-row>

                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn variant="flat" color="#223551" @click="dialogPreguntasF = false">Cerrar</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>


            <v-dialog v-model="dialogPreguntaNueva" max-width="600" persistent>
                <div class="pa-4 rounded-xl" style="overflow-y: auto;">
                    <v-card-title class="py-2 px-4"
                        style="background:#223551; color:#fff; display:flex; align-items:center">

                        <div v-if="editandoPreguntaFrecuente" class="d-flex align-center">
                            <v-icon class="mr-2">mdi mdi-frequently-asked-questions</v-icon>
                            <span class="text-subtitle-1">Configurar Preguntas Frecuentes</span>
                        </div>

                        <div v-if="!editandoPreguntaFrecuente" class="d-flex align-center">
                            <v-icon class="mr-2">mdi mdi-chat-question</v-icon>
                            <span class="text-subtitle-1">Crear Nueva Pregunta</span>
                        </div>
                        <v-spacer />
                        <v-btn icon size="30" color="white" class="btn-grow"
                            @click="dialogPreguntaNueva = false; limpiarCamposNuevaPregunta()">
                            <v-icon size="20">mdi-close</v-icon>
                        </v-btn>

                    </v-card-title>
                    <v-card class="pa-2 rounded-b-xl">
                        <v-alert v-if="rolInactivo" class="mx-0 mb-4 mt-2 modern-alert" type="error" prominent
                            icon="mdi mdi-robot-off" style="font-size: 0.95rem;">
                            <span style="font-weight: 500;">La pregunta se encuentra inhabilitada porque el rol
                                seleccionado
                                está inactivo.</span>
                        </v-alert>
                        <v-card-text>
                            <v-textarea v-model="nuevaPregunta" label="Pregunta Frecuente" variant="outlined"
                                :disabled="idrolactivoPregunta === 0" required />
                            <v-select v-model="rolNuevaPregunta" :items="selectRol" item-title="nombre"
                                :disabled="idrolactivoPregunta === 0" item-value="id" return-object
                                label="Seleccionar Un Rol" variant="outlined" required />
                            <v-textarea v-model="respuestaBotNuevaPregunta" label="Respuesta del Bot" variant="outlined"
                                :disabled="idrolactivoPregunta === 0" required />
                            <v-switch v-if="editandoPreguntaFrecuente" v-model="estadoNuevaPregunta"
                                label="Activar Pregunta" color="blue" :disabled="idrolactivoPregunta === 0"
                                class="mb-n8" />
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn v-if="!editandoPreguntaFrecuente" variant="flat" color="#0A1C3A"
                                @click="guardarNuevaPreguntaF()" class="btn-grow-card">Guardar</v-btn>
                            <v-btn v-if="editandoPreguntaFrecuente" variant="flat" color="#0A1C3A"
                                @click="editarPreguntaF()" :disabled="idrolactivoPregunta === 0"
                                class="btn-grow-card">Actualizar</v-btn>
                            <v-btn variant="flat" color="#223551" class="btn-grow-card"
                                @click="dialogPreguntaNueva = false; limpiarCamposNuevaPregunta()">Cancelar</v-btn>
                        </v-card-actions>
                    </v-card>
                </div>
            </v-dialog>

            <!-- Minimalist Filters Dialog -->
            <v-dialog v-model="dialogFiltros" max-width="620px" persistent transition="dialog-transition">
                <v-card class="rounded-xl elevation-2">
                    <!-- Simple Header -->
                    <v-card-title class="d-flex justify-space-between align-center pa-5 bg-white">
                        <div class="d-flex align-center gap-3">
                            <v-icon color="#006CA1" size="28">mdi-filter-variant</v-icon>
                            <span class="text-h6 font-weight-bold text-grey-darken-3">Filtrar Solicitudes</span>
                        </div>
                        <v-btn icon variant="text" size="small" class="filter-close-btn" @click="dialogFiltros = false">
                            <v-icon>mdi-close</v-icon>
                        </v-btn>
                    </v-card-title>

                    <v-divider></v-divider>

                    <v-card-text class="pa-5">
                        <!-- Status Section -->
                        <div class="mb-4">
                            <div class="d-flex justify-space-between align-center mb-3">
                                <div class="d-flex align-center gap-2">
                                    <v-icon color="#006CA1" size="18">mdi-checkbox-marked-circle-outline</v-icon>
                                    <span class="text-caption font-weight-bold text-grey-darken-2">ESTADO</span>
                                </div>
                                <v-btn variant="text" size="small" density="compact" color="#009B90"
                                    class="text-none font-weight-medium filter-reset-btn"
                                    @click="estadoSeleccionado = null; filtrarPorEstado()">
                                    <v-icon start size="16">mdi-refresh</v-icon>
                                    Restablecer
                                </v-btn>
                            </div>

                            <div class="d-flex gap-2">
                                <v-btn v-for="estado in ['Nuevo', 'En proceso', 'Resuelto']" :key="estado"
                                    class="flex-grow-1 text-capitalize filter-status-btn"
                                    :variant="estadoSeleccionado === estado ? 'flat' : 'outlined'"
                                    :color="estadoSeleccionado === estado ? '#006CA1' : 'grey-lighten-1'"
                                    :class="{ 'elevation-2': estadoSeleccionado === estado }" rounded="lg" size="small"
                                    @click="estadoSeleccionado = estado; filtrarPorEstado()">
                                    <v-icon :start="estadoSeleccionado === estado" size="18">
                                        {{ estado === 'Nuevo' ? 'mdi-new-box' : estado === 'En proceso' ?
                                            'mdi-clock-outline' :
                                            'mdi-check-circle' }}
                                    </v-icon>
                                    <span
                                        :class="estadoSeleccionado === estado ? 'text-white font-weight-medium' : 'text-grey-darken-2'">
                                        {{ estado }}
                                    </span>
                                </v-btn>
                            </div>
                        </div>

                        <!-- Inputs Grid with Icons -->
                        <v-row dense>
                            <!-- No. PQR -->
                            <v-col cols="12" md="6">
                                <div class="d-flex align-center gap-2 mb-2">
                                    <v-icon color="#006CA1" size="16">mdi-ticket-outline</v-icon>
                                    <span class="text-caption font-weight-bold text-grey-darken-2">NÚMERO DE
                                        TICKET</span>
                                </div>
                                <v-autocomplete v-model="selectedPQRFiltro" :items="selectPQRFiltro" item-title="nombre"
                                    item-value="id" return-object placeholder="Ej: 1023" clearable hide-details
                                    variant="outlined" density="compact" rounded="lg" class="filter-input-field"
                                    @update:model-value="filtrarTickets">
                                    <template v-slot:prepend-inner>
                                        <v-icon size="18">mdi-pound</v-icon>
                                    </template>
                                </v-autocomplete>
                            </v-col>

                            <!-- Prioridad -->
                            <v-col cols="12" md="6">
                                <div class="d-flex align-center gap-2 mb-2">
                                    <v-icon color="#FF6B35" size="16">mdi-flag</v-icon>
                                    <span class="text-caption font-weight-bold text-grey-darken-2">NIVEL DE
                                        PRIORIDAD</span>
                                </div>
                                <v-select v-model="selectedPrioridadFiltro" :items="selectPrioridadFiltro"
                                    item-title="nombre" item-value="id" return-object placeholder="Todas" clearable
                                    hide-details variant="outlined" density="compact" rounded="lg"
                                    class="filter-input-field" @update:model-value="filtrarTickets">
                                    <template v-slot:prepend-inner>
                                        <v-icon size="18">mdi-star-circle</v-icon>
                                    </template>
                                </v-select>
                            </v-col>

                            <!-- Fecha Desde -->
                            <v-col cols="12" md="6" class="mt-2">
                                <div class="d-flex align-center gap-2 mb-2">
                                    <v-icon color="#9C27B0" size="16">mdi-calendar-start</v-icon>
                                    <span class="text-caption font-weight-bold text-grey-darken-2">FECHA DESDE</span>
                                </div>
                                <v-text-field type="date" v-model="fechaDesde" placeholder="Seleccionar" clearable
                                    hide-details variant="outlined" density="compact" rounded="lg"
                                    :disabled="!!selectedFechaIngresoFiltro || !!selectedUltimaRespuestaFiltro"
                                    class="filter-input-field" @update:model-value="filtrarTickets">
                                    <template v-slot:prepend-inner>
                                        <v-icon size="18">mdi-calendar-arrow-right</v-icon>
                                    </template>
                                </v-text-field>
                            </v-col>

                            <!-- Fecha Hasta -->
                            <v-col cols="12" md="6" class="mt-2">
                                <div class="d-flex align-center gap-2 mb-2">
                                    <v-icon color="#F57C00" size="16">mdi-calendar-end</v-icon>
                                    <span class="text-caption font-weight-bold text-grey-darken-2">FECHA HASTA</span>
                                </div>
                                <v-text-field type="date" v-model="fechaHasta" placeholder="Seleccionar" clearable
                                    hide-details variant="outlined" density="compact" rounded="lg"
                                    :disabled="!!selectedFechaIngresoFiltro || !!selectedUltimaRespuestaFiltro"
                                    class="filter-input-field" @update:model-value="filtrarTickets">
                                    <template v-slot:prepend-inner>
                                        <v-icon size="18">mdi-calendar-arrow-left</v-icon>
                                    </template>
                                </v-text-field>
                            </v-col>

                            <!-- Cliente -->
                            <v-col cols="12" md="6" class="mt-2">
                                <div class="d-flex align-center gap-2 mb-2">
                                    <v-icon color="#2E7D32" size="16">mdi-account-circle</v-icon>
                                    <span class="text-caption font-weight-bold text-grey-darken-2">CLIENTE</span>
                                </div>
                                <v-autocomplete v-model="selectedUsuarioFiltro" :items="selectUsuarioFiltro"
                                    item-title="nombre" item-value="id" return-object placeholder="Buscar..." clearable
                                    hide-details variant="outlined" density="compact" rounded="lg"
                                    class="filter-input-field" @update:model-value="filtrarTickets">
                                    <template v-slot:prepend-inner>
                                        <v-icon size="18">mdi-account-search</v-icon>
                                    </template>
                                </v-autocomplete>
                            </v-col>

                            <!-- Agente -->
                            <v-col cols="12" md="6" class="mt-2">
                                <div class="d-flex align-center gap-2 mb-2">
                                    <v-icon color="#1565C0" size="16">mdi-account-tie</v-icon>
                                    <span class="text-caption font-weight-bold text-grey-darken-2">AGENTE
                                        ASIGNADO</span>
                                </div>
                                <v-autocomplete v-model="selectedAgenteFiltro" :items="selectAgenteFiltro"
                                    item-title="nombre" item-value="id" return-object placeholder="Todos" clearable
                                    hide-details variant="outlined" density="compact" rounded="lg"
                                    class="filter-input-field" @update:model-value="filtrarTickets">
                                    <template v-slot:prepend-inner>
                                        <v-icon size="18">mdi-briefcase-account</v-icon>
                                    </template>
                                </v-autocomplete>
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-divider></v-divider>

                    <!-- Simple Footer Actions -->
                    <v-card-actions class="pa-4">
                        <v-btn variant="text" color="grey-darken-1"
                            class="font-weight-medium filter-action-btn-secondary" @click="limpiarCamposFiltros()">
                            <v-icon start size="18">mdi-broom</v-icon>
                            Limpiar
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn variant="text" color="grey-darken-2" class="font-weight-medium"
                            @click="dialogFiltros = false">
                            Cerrar
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>



        </v-main>

    </v-app>
</template>

<script>
import axios from 'axios';
import CryptoJS from "crypto-js";
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';
import AppHeader from '../components/AppHeader.vue';

// ✅ Optimización: Función debounce simple (sin dependencias externas)
function debounce(fn, delay) {
    let timeoutId;
    return function (...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn.apply(this, args), delay);
    };
}

export default {
    components: {
        AppHeader
    },
    data: () => ({

        drawer: true,
        baseURL: '',
        nombreComercial: localStorage.getItem('nombreLogin') + ' ' + localStorage.getItem('apellidoLogin') || 'Comercial',
        comercialId: localStorage.getItem('idUsuario') || '0',
        idCargo: localStorage.getItem('idCargo') || '0',
        correoUsuario: localStorage.getItem('correoUsuario') || 'No disponible',

        ifCargando: false,
        ifCargando2: false,

        tickets: [],
        page: 1,
        itemsPerPage: 10,
        isFiltered: false,
        headers: [
            { title: 'PQR', key: 'pqr' },
            { title: 'categoria', key: 'categoria_pqr' },
            { title: 'subcategoria', key: 'subcategoria_pqr' },
            { title: 'Canal', key: 'canal' },
            { title: 'Fecha Ingreso', key: 'fecha_ingreso' },
            { title: 'Última Respuesta', key: 'ultima_respuesta' },
            { title: 'Cliente', key: 'cliente' },
            { title: 'Agente', key: 'agente' },
            { title: 'Estado', key: 'estado' },
            { title: 'Prioridad', key: 'prioridad' },
            { title: 'Activo con', key: 'activo_con' },
        ],

        // Filtros de canales
        canales: [
            { id: 'todos', nombre: 'Todos', count: 0, icono: 'mdi-message-text', colorSeleccionado: '#223551' },
            { id: 'web', nombre: 'Web', count: 0, icono: 'mdi-web', colorSeleccionado: '#FFA500' },
            { id: 'whatsapp', nombre: 'WhatsApp', count: 0, icono: 'mdi-whatsapp', colorSeleccionado: '#25D366' },
            { id: 'messenger', nombre: 'Messenger', count: 0, icono: 'mdi-facebook-messenger', colorSeleccionado: '#223551' },
            { id: 'instagram', nombre: 'Instagram', count: 0, icono: 'mdi-instagram', colorSeleccionado: '#C13584' },
        ],
        canalSeleccionado: 'todos',
        canalTicketSeleccionado: null,

        // Histórico filtros (panel izquierdo del dialogo de PQR)
        menuHistorico: false,
        selectedHistoricoFecha: null,
        selectedHistoricoUsuario: null,
        selectedHistoricoEstado: null,
        selectHistoricoFecha: [],
        selectHistoricoUsuario: [],
        selectHistoricoEstado: [],
        historicoOriginal: null,

        // Filtros adicionales
        activoConOpciones: [
            { id: 'todos', nombre: 'Todos' },
            { id: 'nuevo', nombre: 'Nuevo' },
            { id: 'en_proceso', nombre: 'En proceso' },
            { id: 'resuelto', nombre: 'Resuelto' }
        ],
        activoConSeleccionado: 'todos',
        prioridadSeleccionada: 'todos',
        fechaDesde: null,
        fechaHasta: null,


        preguntasF: [],
        headersPreguntasF: [
            { title: 'Pregunta', key: 'pregunta' },
            { title: 'Rol', key: 'idrol' },
            { title: 'Respuesta', key: 'respuesta' },
            { title: 'Usuario', key: 'usuario' },
            { title: 'Estado', key: 'estado' },
            { title: 'Última Modificación', key: 'fecha' },
            { title: 'Opciones', key: 'opciones' }
        ],


        selectRol: [],

        selectedCategoriaFiltro: null,
        filtroGlobal: null,

        urlChat: null,
        iframeChat: true,
        chatLoading: false,
        dsGestionManual: true,

        ifDetallesPQR: false,

        alerta: false,
        mensajeAlerta: null,
        baseURL: '',
        informacionServicio: null,
        descripcionServicio: null,
        documentosCliente: [],
        documentoSeleccionadoCliente: null,
        respuestaAsesor: null,
        archivosRespuestaPQR: null,
        archivoCrearPQR: null,
        estadoServicio: null,
        estadosPQR: [
            { id: '2', nombre: 'En Proceso' },
            { id: '4', nombre: 'Escalar' },
            { id: '3', nombre: 'Resuelto' },

        ],
        estadosPQRChat: [
            { id: '2', nombre: 'En Proceso' },
            { id: '4', nombre: 'Escalar' },
            { id: '3', nombre: 'Resuelto' },
        ],
        estadosPQRCrear: [
            { id: '1', nombre: 'Nuevo' },
            { id: '2', nombre: 'En Proceso' }
        ],
        prioridadesPQR: [
            { id: '1', nombre: 'Alta' },
            { id: '2', nombre: 'Media' },
            { id: '3', nombre: 'Baja' }
        ],
        usuariosPQR: [],
        usuariosPQRAsignar: [],
        usuariosPQREscalar: [],
        prioridadPQR: null,
        idPQR: '0',
        historico: [],

        dialogPreguntasF: false,
        dialogPreguntaNueva: false,
        filtroPreguntasF: null,
        nuevaPregunta: null,
        rolNuevaPregunta: null,
        respuestaBotNuevaPregunta: null,
        estadoNuevaPregunta: true,

        dialogFiltros: false,
        selectedPQRFiltro: null,
        selectedDescripcionFiltro: null,
        selectedEstadoFiltro: null,
        selectedPrioridadFiltro: null,
        selectedUsuarioFiltro: null,
        selectedFechaIngresoFiltro: null,
        selectedUltimaRespuestaFiltro: null,
        selectedAgenteFiltro: null,
        selectAgenteFiltro: [],
        selectPQRFiltro: [],
        selectDescripcionFiltro: [],
        selectEstadoFiltro: [],
        selectEstadoPreguntasFrecuentes: [
            { id: '1', nombre: 'Activo' },
            { id: '0', nombre: 'Inactivo' }
        ],
        selectPrioridadFiltro: [],
        selectUsuarioFiltro: [],

        celularCliente: null,

        crearPQR: false,
        descripcionCrearPQR: null,
        respuestaCrearPQR: null,
        estadoCrearPQR: null,
        usuarioAsignado: null,
        usuarioEscalar: null,
        usuarioAsignadoCrear: null,

        nombreClienteSeleccionado: null,
        asignadoActual: null,
        escaladoActual: null,

        arrayArchivos: [],
        idRespuestaPQR: null,
        clientesPQR: [],
        clienteCrearPQR: null,
        imagenComercial: '',

        editandoPreguntaFrecuente: false,
        idPreguntaEditando: null,
        idrolactivoPregunta: null,

        estadoItemSeleccionado: null,
        categoriaCrearPQR: null,
        subcategoriaCrearPQR: null,
        listaCategoriasPQR: [],
        listaSubCategoriasPQR: [],
        rolInactivo: null,

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

        estadoSeleccionado: null,
        menuActivo: null,

        mensajesAlmacenados: [],
        selectedPrioridadChat: null,
        selectedEstadoChat: null,
        usuarioEscalarChat: null,
        observacionChat: null,

        alertaInteres: false,
        mensajeAlertInteres: null,
        expandedMessages: {},

        estadoPQRGrabar: null,
        // controla la animación/visibilidad de los chips cuando se abre el diálogo
        chipsVisible: false,
        // duración (ms) de la animación de entrada de los chips. Ajustable.
        // Cambiado a 1200ms para que la entrada dure ~1.2s antes de permitir el cierre/ocultado.
        chipsEntryDuration: 1200,
        // indicador temporal para bloquear acciones mientras la entrada se anima
        chipsEntryAnimating: false,
        // temporizador usado para retrasar la aplicación del estado seleccionado
        chipsSetStateTimer: null,

        disablediconoWhastapp: true,
        disablediconoMessenger: false,
        disablediconoInstagram: false,
        recipientMessenger: '',
        recipientInstagram: '',
        idClienteChat: null,
        canalChat: null,
        icons: {
            whatsapp: 'mdi-whatsapp',
            messenger: 'mdi-facebook-messenger',
            instagram: 'mdi-instagram',
        },
    }),

    created() {
        window.addEventListener("message", (e) => this.recibirMensaje(e));
    },
    destroyed() {
        window.removeEventListener("message", (e) => this.recibirMensaje(e));
    },

    mounted() {
        this.baseURL = import.meta.env.VITE_API_BASE_URL;
        this.cargarFiltros();
        this.obtenerClientes();
        this.setMenuActivoPorRuta();
        this.cargarRolesIA();
        this.llamadoUsuarios();
        this.cargarCategoriasPQR();
        this.cargarSubCategoriasPQR();

        // Cargar imagen del comercial
        const savedImage = localStorage.getItem('imagenComercial');
        if (savedImage) {
            this.imagenComercial = savedImage;
        } else {
            this.imagenComercial = `${this.baseURL}images/${this.comercialId}.jpeg?t=${Date.now()}`;
        }

        // ✅ Optimización: Crear versión debounced del filtro (300ms delay)
        this.filtrarTicketsDebounced = debounce(this.filtrarTicketsImpl, 300);
    },

    watch: {
        alertaInteres(val) {
            if (val) {
                this.validarUsuariosDisponibles();
                this.observacionChat = null;
                this.usuarioEscalarChat = null;
                this.selectedEstadoChat = null;
                this.selectedPrioridadChat = null;
            }
        },
        categoriaCrearPQR(newVal) {
            // Si cambia la categoría, limpiar la subcategoría seleccionada
            this.subcategoriaCrearPQR = null;
        },

        // Ensure animations run when the dialog property changes (some Vuetify builds
        // may not emit update:modelValue). This watcher guarantees the handler runs.
        informacionServicio(newVal) {
            if (typeof this.onInformacionServicioToggle === 'function') {
                this.onInformacionServicioToggle(newVal);
            } else {
                // fallback: if dialog opened, show chips
                if (newVal) this.chipsVisible = true;
            }
        }
    },

    computed: {

        filteredTickets() {
            let items = this.tickets;

            // Apply global search if exists
            if (this.filtroGlobal) {
                const search = this.filtroGlobal.toLowerCase();
                items = items.filter(item => {
                    // Check all properties or specific ones
                    return Object.values(item).some(val =>
                        String(val || '').toLowerCase().includes(search)
                    );
                });
            }

            return items;
        },

        isFormValid() {
            return !!(
                this.clienteCrearPQR &&
                this.usuarioAsignadoCrear &&
                this.estadoCrearPQR &&
                this.prioridadPQR &&
                (this.descripcionCrearPQR && this.descripcionCrearPQR.trim().length > 0)
            );
        },

        /**
         * Filtra las subcategorías basándose en la categoría seleccionada.
         * Retorna un array vacío si no hay categoría seleccionada.
         */
        subcategoriasFiltradas() {
            if (!this.categoriaCrearPQR) return [];
            // Filtra la lista completa de subcategorías comparando el ID de la categoría padre
            return this.listaSubCategoriasPQR.filter(sub => sub.id_categoriapqr === this.categoriaCrearPQR.id);
        },

        // ✅ Optimizado: Validación de conflictos de fecha en un solo computed
        fechaConfig() {
            const hasRango = !!(this.fechaDesde || this.fechaHasta);
            const hasIngreso = !!this.selectedFechaIngresoFiltro;
            const hasRespuesta = !!this.selectedUltimaRespuestaFiltro;

            return {
                rangoActivo: hasRango,
                ingresoActivo: hasIngreso,
                respuestaActivo: hasRespuesta,
                // Deshabilitar campos según prioridad
                deshabilitarRango: hasIngreso || hasRespuesta,
                deshabilitarIngreso: hasRango || hasRespuesta,
                deshabilitarRespuesta: hasRango || hasIngreso
            };
        },

        // ✅ Optimizado: Contar filtros usando array.filter para mejor performance
        contadorFiltrosActivos() {
            const filtros = [
                this.estadoSeleccionado,
                this.selectedPQRFiltro,
                this.selectedPrioridadFiltro,
                this.fechaDesde,
                this.fechaHasta,
                this.selectedUsuarioFiltro,
                this.selectedAgenteFiltro,
                this.selectedFechaIngresoFiltro,
                this.selectedUltimaRespuestaFiltro
            ];
            return filtros.filter(Boolean).length;
        },

        // ✅ Nuevo: Tickets filtrados como computed (mejor performance)
        hasActiveFechaFiltro() {
            return this.fechaDesde || this.fechaHasta ||
                this.selectedFechaIngresoFiltro ||
                this.selectedUltimaRespuestaFiltro;
        },

        // ✅ Nuevo: Detectar si hay algún filtro activo
        hasAnyFilter() {
            return !!(this.estadoSeleccionado || this.selectedPQRFiltro ||
                this.selectedPrioridadFiltro || this.selectedUsuarioFiltro ||
                this.selectedAgenteFiltro || this.canalSeleccionado !== 'todos' ||
                this.hasActiveFechaFiltro);
        }
    },

    methods: {

        getIconByChannel(canal) {
            console.log('Canal recibido:', canal);
            return this.icons[canal?.toLowerCase()] || 'mdi-chat';
        },

        exportarPDF() {
            this.ifCargando2 = true;
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
            // También asegurar que los descendientes dentro del contenedor que tengan
            // height/max-height o overflow fijos se expandan para que html2canvas capture todo.
            const descendantOriginals = [];
            try {
                const descendants = elemento.querySelectorAll('*');
                for (const desc of descendants) {
                    // Guardar solo estilos inline actuales para restaurar luego
                    descendantOriginals.push({
                        node: desc,
                        height: desc.style.height,
                        maxHeight: desc.style.maxHeight,
                        overflow: desc.style.overflow,
                        overflowY: desc.style.overflowY,
                    });
                    // Forzar expansión
                    desc.style.height = 'auto';
                    desc.style.maxHeight = 'none';
                    desc.style.overflow = 'visible';
                    desc.style.overflowY = 'visible';
                }
            } catch (err) {
                // Si algo falla iterando descendants, continuar sin bloquear el proceso
                console.warn('No se pudo expandir descendientes antes de exportar PDF', err);
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
                        const imgDataFull = canvas.toDataURL('image/png');
                        const pdf = new jsPDF('p', 'mm', 'a4');
                        const pdfWidth = pdf.internal.pageSize.getWidth();
                        const pdfHeight = pdf.internal.pageSize.getHeight();

                        const canvasWidth = canvas.width;
                        const canvasHeight = canvas.height;

                        // Calcular la altura en pixeles del canvas que cabe en una página PDF
                        const pageCanvasHeight = Math.floor((pdfHeight * canvasWidth) / pdfWidth);

                        let renderedHeight = 0;
                        let pageIndex = 0;

                        while (renderedHeight < canvasHeight) {
                            // Crear canvas temporal para la porción de página
                            const pageCanvas = document.createElement('canvas');
                            pageCanvas.width = canvasWidth;
                            const remaining = canvasHeight - renderedHeight;
                            pageCanvas.height = Math.min(pageCanvasHeight, remaining);

                            const ctx = pageCanvas.getContext('2d');
                            // Dibujar la porción correspondiente del canvas original
                            ctx.drawImage(canvas, 0, renderedHeight, canvasWidth, pageCanvas.height, 0, 0, canvasWidth, pageCanvas.height);

                            const pageData = pageCanvas.toDataURL('image/png');

                            // Convertir la altura de esta porción a milímetros para el PDF
                            const imgHeightMM = (pageCanvas.height * pdfWidth) / canvasWidth;

                            if (pageIndex > 0) pdf.addPage();
                            pdf.addImage(pageData, 'PNG', 0, 0, pdfWidth, imgHeightMM);

                            renderedHeight += pageCanvas.height;
                            pageIndex++;
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
                        // Restaurar estilos de los descendientes que modificamos
                        try {
                            for (const { node: dnode, height, maxHeight, overflow, overflowY } of descendantOriginals) {
                                dnode.style.height = height;
                                dnode.style.maxHeight = maxHeight;
                                dnode.style.overflow = overflow;
                                dnode.style.overflowY = overflowY;
                            }
                        } catch (err) {
                            console.warn('Error restaurando estilos de descendientes tras exportar PDF', err);
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

                        this.ifCargando2 = false;
                    });
            });
        },

        // Helper para normalizar/extraer la parte fecha de varios formatos
        parseDateOnly(input) {
            if (!input) return null;
            try {
                let s = String(input).trim();
                // Si tiene hora, tomar la primera parte
                if (s.indexOf(' ') > -1) s = s.split(' ')[0];
                // Normalizar separadores
                s = s.replace(/\//g, '-');

                // Detectar formatos comunes
                // yyyy-mm-dd
                const isoMatch = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})$/);
                if (isoMatch) {
                    const yy = isoMatch[1];
                    const mm = String(isoMatch[2]).padStart(2, '0');
                    const dd = String(isoMatch[3]).padStart(2, '0');
                    return `${yy}-${mm}-${dd}`;
                }

                // dd-mm-yyyy or dd-mm-yy
                const dmyMatch = s.match(/^(\d{1,2})-(\d{1,2})-(\d{2,4})$/);
                if (dmyMatch) {
                    const dd = String(dmyMatch[1]).padStart(2, '0');
                    const mm = String(dmyMatch[2]).padStart(2, '0');
                    let yy = String(dmyMatch[3]);
                    if (yy.length === 2) {
                        yy = '20' + yy;
                    }
                    // validar
                    const d = new Date(`${yy}-${mm}-${dd}`);
                    if (isNaN(d)) return null;
                    return `${yy}-${mm}-${dd}`;
                }

                // fallback: try Date parse
                const d = new Date(s);
                if (isNaN(d)) return null;
                const yy = d.getFullYear();
                const mm = String(d.getMonth() + 1).padStart(2, '0');
                const dd = String(d.getDate()).padStart(2, '0');
                return `${yy}-${mm}-${dd}`;
            } catch (e) {
                return null;
            }
        },

        filtrarxCanal() {
            // Asegurar que existe una copia original para restaurar más tarde
            if (!this.ticketsOriginal) {
                this.ticketsOriginal = Array.isArray(this.tickets) ? [...this.tickets] : [];
            }

            // Delegamos la combinación de filtros a filtrarTickets para que canal se combine
            // con cualquier otro filtro activo (fecha, agente, prioridad, etc.).
            // canalSeleccionado ya debe estar establecido por el botón que llama a este método.
            this.filtrarTickets();
        },

        // --- Animaciones y control de chips ---
        // Se llama cuando el dialog v-model "informacionServicio" cambia de valor
        onInformacionServicioToggle(val) {
            // cerrar primero
            if (!val) {
                // cancel any pending set-state timer
                if (this.chipsSetStateTimer) {
                    clearTimeout(this.chipsSetStateTimer);
                    this.chipsSetStateTimer = null;
                }
                this.chipsVisible = false;
                this.estadoPQRGrabar = null;
                this.chipsEntryAnimating = false;
                return;
            }

            // abrir: forzamos reinicio de la animación
            this.chipsVisible = false;
            this.estadoPQRGrabar = null;
            // mark as animating and after chipsEntryDuration clear it
            this.chipsEntryAnimating = true;
            this.$nextTick(() => {
                // pequeño delay antes de iniciar la entrada para separar animaciones
                setTimeout(() => {
                    this.chipsVisible = true;
                    // una vez iniciada la entrada, esperar chipsEntryDuration para desactivar la señal
                    if (this.chipsEntryDuration && this.chipsEntryDuration > 0) {
                        setTimeout(() => {
                            this.chipsEntryAnimating = false;
                        }, this.chipsEntryDuration);
                    } else {
                        this.chipsEntryAnimating = false;
                    }
                }, 120);
            });
        },

        // Alterna el estado seleccionado; si se pulsa el mismo estado, deselecciona
        // y vuelve a mostrar todos los chips (con animación)
        setEstadoPQRGrabar(state) {
            // If we are currently animating the entry, delay applying the state so
            // the entry animation finishes and the leave animation is visually distinct.
            if (this.chipsEntryAnimating) {
                // clear any previous timer
                if (this.chipsSetStateTimer) clearTimeout(this.chipsSetStateTimer);
                this.chipsSetStateTimer = setTimeout(() => {
                    this.chipsSetStateTimer = null;
                    this.aplicarEstadoPQRGrabar(state);
                }, this.chipsEntryDuration + 550); // small buffer after entry (longer to ensure entry finished)
                return;
            }
            this.aplicarEstadoPQRGrabar(state);
        },

        aplicarEstadoPQRGrabar(state) {
            if (this.estadoPQRGrabar === state) {
                // deseleccionar -> reiniciar animación para mostrar todos
                this.chipsVisible = false;
                this.estadoPQRGrabar = null;
                this.$nextTick(() => setTimeout(() => (this.chipsVisible = true), 120));
                return;
            }

            this.estadoPQRGrabar = state;
            
            if (state === 'Escalar') {
                // Para 'Escalar', usamos el diálogo de alertaInteres (mismo que cerrar chat)
                this.alertaInteres = true;
                this.mensajeAlertInteres = 'Escalar caso';
                
                // Pre-seleccionar estado
                this.selectedEstadoChat = this.estadosPQRChat.find(e => e.nombre === 'Escalar');
                
                // Intentar pre-seleccionar prioridad del ticket actual
                const currentTicket = this.tickets.find(t => t.pqr === this.idPQR);
                if (currentTicket) {
                    this.selectedPrioridadChat = this.prioridadesPQR.find(p => p.nombre === currentTicket.prioridad);
                }
                
                // Aseguramos que el panel manual esté cerrado si se abre este diálogo
                this.ifDetallesPQR = false;

            } else if (state === 'En Proceso' || state === 'Resuelto') {
                this.iframeChat = false;
                this.ifDetallesPQR = true;
                this.validarUsuariosDisponibles();
                
                // Mapear el estado seleccionado al objeto estadoServicio
                let estadoId = null;
                if (state === 'En Proceso') estadoId = '2';
                else if (state === 'Resuelto') estadoId = '3';
                
                if (estadoId) {
                    this.estadoServicio = this.estadosPQR.find(e => e.id == estadoId);
                }
            }
        },

        filtrarPorEstado() {

            // Validar si se ha filtrado, si es asi, filtrar por estado la base actual
            if (this.isFiltered) {
                this.tickets = this.tickets.filter(ticket => {
                    return ticket.estado && ticket.estado.toLowerCase() === this.estadoSeleccionado.toLowerCase();
                });
                this.dialogFiltros = false;
                return;
            }

            if (!this.ticketsOriginal) {
                this.ticketsOriginal = [...this.tickets];
            }
            if (!this.estadoSeleccionado) {
                this.tickets = [...this.ticketsOriginal];
            } else {
                this.tickets = this.ticketsOriginal.filter(ticket => {
                    return ticket.estado && ticket.estado.toLowerCase() === this.estadoSeleccionado.toLowerCase();
                });
            }

            this.dialogFiltros = false;

            this.canales.forEach(canal => {
                canal.count = this.tickets.filter(ticket => {
                    if (canal.id === 'todos') return true;
                    return ticket.canal && ticket.canal.toLowerCase() === canal.id.toLowerCase();
                }).length;
            });
        },

        llamadoUsuarios() {
            axios
                .post(this.baseURL + "api/cargausus", {
                    idusu: 0,
                    tipo: 2, // 2 para cargar los usuarios del rol servicio al cliente
                })
                .then((response) => {
                    this.usuariosPQR = response.data.data.map((c) => ({
                        id: c.u_id,
                        nombre: `${c.u_nom} ${c.u_ape}`,
                    }));
                    this.usuariosPQREscalar = response.data.data.map((c) => ({
                        id: c.u_id,
                        nombre: `${c.u_nom} ${c.u_ape}`,
                    }));
                    this.usuariosPQRAsignar = response.data.data.map((c) => ({
                        id: c.u_id,
                        nombre: `${c.u_nom} ${c.u_ape}`,
                    }));
                })
                .catch((error) => {
                    console.error("Error al cargar Usuarios:", error);
                });
        },

        obtenerClientes() {
            let arregloTemp = [];

            axios.post(this.baseURL + 'api/cargarpp', {
                'idusu': 0
            }
            )
                .then(response => {
                    console.log('Respuesta cargarpp:', response.data.data);
                    arregloTemp = response.data.data.filter(cliente => cliente.pc_id);

                    this.clientesPQR = arregloTemp.map(cliente => ({
                        id: cliente.pc_id,
                        nombre: cliente.pc_nombre + ' ' + cliente.pc_apellido + ' - ' + cliente.p_razon_social
                    }));
                })
                .catch(error => {
                    console.error('Error al cargar empresas:', error)
                })
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
        getFileName2(url) {
            if (!url) return '';
            try {
                return decodeURIComponent(url.split('/').pop().split('?')[0]);
            } catch (e) {
                return url;
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

        cargarCategoriasPQR() {
            axios.post(this.baseURL + 'api/cargarcategoriasPQR')
                .then(response => {
                    console.log('Respuesta cargarCategoriasPQR:', response.data.data);
                    this.listaCategoriasPQR = response.data.data;
                })
                .catch(error => {
                    console.error('Error al cargar categorias:', error)
                })
        },

        cargarSubCategoriasPQR() {
            axios.post(this.baseURL + 'api/cargarsubcategoriasPQR')
                .then(response => {
                    console.log('Respuesta cargarsubcategoriasPQR:', response.data.data);
                    this.listaSubCategoriasPQR = response.data.data;
                })
                .catch(error => {
                    console.error('Error al cargar subcategorias:', error)
                })
        },

        guardarPQR() {


            // Validación de campos obligatorios
            if (!this.estadoCrearPQR || !this.prioridadPQR || !this.descripcionCrearPQR || !this.clienteCrearPQR) {
                this.mensajeAlerta = 'Por favor, complete todos los campos obligatorios.';
                this.alerta = true;
                return;
            }

            let formData = new FormData();
            let formData2 = new FormData();
            let formData3 = new FormData();
            let urlsCombinadas = '';
            formData.append('estado', this.estadoCrearPQR.id);
            formData.append('asignado', this.usuarioAsignadoCrear ? this.usuarioAsignadoCrear.id : 0);
            formData.append('prioridad', this.prioridadPQR.id);
            formData.append('idCategoriapqr', this.categoriaCrearPQR ? this.categoriaCrearPQR.id : '');
            formData.append('idSubcategoriapqr', this.subcategoriaCrearPQR ? this.subcategoriaCrearPQR.id : '');
            formData.append('descripcion', this.descripcionCrearPQR);
            formData.append('respuesta', this.respuestaCrearPQR ? this.respuestaCrearPQR : '');
            formData.append('idcli', this.clienteCrearPQR.id);
            formData.append('idusu', this.comercialId);

            this.mensajeAlerta = 'Guardando PQR...';
            this.alerta = true;
            this.ifCargando = true;

            axios.post(this.baseURL + 'api/savePqr', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {

                if (this.archivoCrearPQR && this.archivoCrearPQR.length > 0) {
                    formData2.append('id', response.data.data[0].idPqrRespuesta);
                    this.idRespuestaPQR = response.data.data[0].idPqrRespuesta;
                    this.archivoCrearPQR.forEach(file => {
                        formData2.append('files[]', file);
                    });

                    axios.post(this.baseURL + 'api/savePqrFiles', formData2, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }).then(response => {
                        console.log('Archivos guardados:', response.data.archivos);
                        this.arrayArchivos = response.data.archivos;

                        this.arrayArchivos.map(archivo => {
                            console.log('Archivo con url:', archivo);
                            urlsCombinadas += archivo.url + '----';
                        });

                        urlsCombinadas = urlsCombinadas.slice(0, -4); // Eliminar los últimos cuatro guiones
                        formData3.append('urls', urlsCombinadas);
                        formData3.append('idRespuesta', this.idRespuestaPQR);
                        console.log('URLs combinadas:', urlsCombinadas);

                        axios.post(this.baseURL + 'api/updatePqrFilesUrl', formData3, {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            }
                        }).then(response => {
                            this.mensajeAlerta = 'PQR registrado correctamente.';
                            this.ifCargando = false;
                            this.alerta = true;
                            this.crearPQR = false;
                            // Limpiar campos
                            this.clienteCrearPQR = null;
                            this.descripcionCrearPQR = null;
                            this.respuestaCrearPQR = null;
                            this.estadoCrearPQR = null;
                            this.prioridadPQR = null;
                            this.categoriaCrearPQR = null;
                            this.subcategoriaCrearPQR = null;
                            this.archivoCrearPQR = null;
                            setTimeout(() => {
                                this.alerta = false;
                                this.recargarTickets();
                            }, 1500);
                            this.arrayArchivos = [];
                            this.idRespuestaPQR = null;
                        }).catch(error => {
                            console.error('Error al guardar los archivos:', error);
                        });
                    }).catch(error => {
                        console.error('Error al guardar la respuesta:', error);
                        this.mensajeAlerta = 'Error al guardar la respuesta.';
                        this.ifCargando = false;
                        this.alerta = true;
                    });

                } else {
                    this.mensajeAlerta = 'PQR registrado correctamente.';
                    this.ifCargando = false;
                    this.alerta = true;
                    this.crearPQR = false;
                    // Limpiar campos
                    this.clienteCrearPQR = null;
                    this.descripcionCrearPQR = null;
                    this.respuestaCrearPQR = null;
                    this.estadoCrearPQR = null;
                    this.prioridadPQR = null;
                    this.categoriaCrearPQR = null;
                    this.subcategoriaCrearPQR = null;
                    this.archivoCrearPQR = null;
                    setTimeout(() => {
                        this.alerta = false;
                        this.recargarTickets();
                    }, 1500);
                }

            }).catch(error => {
                this.ifCargando = false;
                this.mensajeAlerta = 'Error al registrar el PQR.';
                this.alerta = true;
                console.error('Error al registrar el PQR:', error);
            });
            this.crearPQR = false;

        },

        guardarRespuestaPQR() {

            if (!this.respuestaAsesor) {
                this.mensajeAlerta = 'Por favor, digite la respuesta del asesor';
                this.alerta = true;
                return;
            }

            if (!this.estadoServicio) {
                this.mensajeAlerta = 'Por favor, seleccione el estado del servicio';
                this.alerta = true;
                return;
            }

            if (!this.prioridadPQR) {
                this.mensajeAlerta = 'Por favor, seleccione el estado del servicio';
                this.alerta = true;
                return;
            }

            let formData = new FormData();
            let formData2 = new FormData();
            let formData3 = new FormData();

            let urlsCombinadas = '';

            formData.append('res', this.respuestaAsesor);
            formData.append('est', this.estadoServicio.id);
            formData.append('id', this.idPQR);
            formData.append('prio', this.prioridadPQR.id);
            formData.append('idusu', localStorage.getItem('idUsuario'));
            formData.append('asignado', this.usuarioAsignado ? this.usuarioAsignado.id : 0);
            formData.append('escalado', this.usuarioEscalar ? this.usuarioEscalar.id : 0);

            console.log('Datos a enviar:', {
                res: this.respuestaAsesor,
                est: this.estadoServicio.id,
                id: this.idPQR,
                files: this.archivosRespuestaPQR,
                prio: this.prioridadPQR.id,
                idusu: localStorage.getItem('idUsuario'),
                asignado: this.usuarioAsignado ? this.usuarioAsignado.id : 0,
                escalado: this.usuarioEscalar ? this.usuarioEscalar.id : 0
            });

            this.mensajeAlerta = 'Guardando respuesta...';
            this.alerta = true;
            this.ifCargando = true;

            axios.post(this.baseURL + 'api/savePqrRespuesta', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                console.log('Respuesta guardada:', response.data);

                formData2.append('id', response.data.data[0].idRespuestaPQR);
                this.idRespuestaPQR = response.data.data[0].idRespuestaPQR;

                if (this.archivosRespuestaPQR) {

                    this.archivosRespuestaPQR.forEach(file => {
                        formData2.append('files[]', file);
                    });

                    axios.post(this.baseURL + 'api/savePqrFiles', formData2, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }).then(response => {
                        console.log('Archivos guardados:', response.data.archivos);
                        this.arrayArchivos = response.data.archivos;

                        this.arrayArchivos.map(archivo => {
                            console.log('Archivo con url:', archivo);
                            urlsCombinadas += archivo.url + '----';
                        });

                        urlsCombinadas = urlsCombinadas.slice(0, -4); // Eliminar los últimos cuatro guiones
                        formData3.append('urls', urlsCombinadas);
                        formData3.append('idRespuesta', this.idRespuestaPQR);
                        console.log('URLs combinadas:', urlsCombinadas);

                        axios.post(this.baseURL + 'api/updatePqrFilesUrl', formData3, {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            }
                        }).then(response => {
                            this.mensajeAlerta = 'La respuesta se ha registrado correctamente.';
                            this.alerta = true;
                            this.ifCargando = false;
                            this.arrayArchivos = [];
                            this.idRespuestaPQR = null;

                            setTimeout(() => {
                                this.recargarTickets();
                            }, 1000);
                            this.cerrarInfoPQR();
                        }).catch(error => {
                            console.error('Error al guardar los archivos:', error);
                        });

                    }).catch(error => {
                        console.error('Error al guardar los archivos:', error);
                    });

                } else {

                    this.mensajeAlerta = 'La respuesta se ha registrado correctamente.';
                    this.alerta = true;
                    this.ifCargando = false;
                    this.arrayArchivos = [];
                    this.idRespuestaPQR = null;
                    this.cerrarInfoPQR();

                    setTimeout(() => {
                        this.recargarTickets();
                    }, 1000);

                }

            }).catch(error => {
                console.error('Error al registrar la respuesta:', error);
            });

            this.informacionServicio = false;
        },

        // ✅ Optimización: Wrapper público con debounce
        filtrarTickets() {
            // Si se llama directamente, usar la versión debounced si existe
            if (this.filtrarTicketsDebounced) {
                this.filtrarTicketsDebounced();
            } else {
                // Fallback para llamadas antes de mounted
                this.filtrarTicketsImpl();
            }
        },

        // ✅ Optimización: Implementación real del filtrado (debounced)
        filtrarTicketsImpl() {
            // Asegurar copia original
            if (!this.ticketsOriginal) {
                this.ticketsOriginal = Array.isArray(this.tickets) ? [...this.tickets] : [];
            }

            // Detectar si hay algún filtro activo
            const hasFilters = !!(
                this.selectedPQRFiltro ||
                this.selectedDescripcionFiltro ||
                this.selectedEstadoFiltro ||
                this.selectedPrioridadFiltro ||
                this.selectedUsuarioFiltro ||
                this.selectedAgenteFiltro ||
                (this.canalSeleccionado && this.canalSeleccionado !== 'todos') ||
                this.selectedFechaIngresoFiltro ||
                this.selectedUltimaRespuestaFiltro ||
                this.fechaDesde ||
                this.fechaHasta
            );

            // ✅ Optimizado: Simplificar lógica de restauración
            if (!hasFilters) {
                if (this.estadoSeleccionado) {
                    this.filtrarPorEstado();
                    return;
                }
                this.tickets = Array.isArray(this.ticketsOriginal) ? [...this.ticketsOriginal] : [];
                this.dialogFiltros = false;
                this.actualizarContadoresCanales();
                return;
            }

            // Prioridad de filtros de fecha (implementada):
            // A) Si existe fechaDesde o fechaHasta => usar rango (ignore selectedFechaIngresoFiltro y selectedUltimaRespuestaFiltro)
            // B) Si existe selectedFechaIngresoFiltro => filtrar por fecha_ingreso (exacta, sin hora)
            // C) Si existe selectedUltimaRespuestaFiltro => filtrar por ultima_respuesta (comparando la parte fecha)

            // Filtrar sobre ticketsOriginal para evitar encadenar filtros sobre el resultado previo
            this.tickets = (this.ticketsOriginal || []).filter(ticket => {
                const matchPqr = !this.selectedPQRFiltro || String(ticket.pqr) === String(this.selectedPQRFiltro.id);
                const matchDescripcion = !this.selectedDescripcionFiltro || String(ticket.descripcion) === String(this.selectedDescripcionFiltro.id);
                const matchEstado = !this.selectedEstadoFiltro || String(ticket.estado) === String(this.selectedEstadoFiltro.nombre) || String(ticket.estado) === String(this.selectedEstadoFiltro.id);
                const matchPrioridad = !this.selectedPrioridadFiltro || String(ticket.prioridad) === String(this.selectedPrioridadFiltro.nombre) || String(ticket.prioridad) === String(this.selectedPrioridadFiltro.id);
                const matchUsuario = !this.selectedUsuarioFiltro || String(ticket.idCliente) === String(this.selectedUsuarioFiltro.id) || String(ticket.co_id) === String(this.selectedUsuarioFiltro.id);
                // Agente: soporta comparar por id o nombre del agente (dependiendo de cómo se llenó el select)
                const matchAgente = !this.selectedAgenteFiltro || String(ticket.agente) === String(this.selectedAgenteFiltro.id) || String(ticket.agente) === String(this.selectedAgenteFiltro.nombre);
                // Canal: si canalSeleccionado está establecido y no es 'todos', filtrar por canal
                const matchCanal = !this.canalSeleccionado || this.canalSeleccionado === 'todos' || (ticket.canal && ticket.canal.toLowerCase() === String(this.canalSeleccionado).toLowerCase());

                // Fecha ingreso: soporta tres modos (usar helper parseDateOnly)
                const ticketFechaStr = this.parseDateOnly(ticket.fecha_ingreso);
                // Normalizar ultima_respuesta (tomar la parte fecha y parsearla)
                const ticketUltimaRespFecha = ticket.ultima_respuesta ? this.parseDateOnly((ticket.ultima_respuesta.split && ticket.ultima_respuesta.split(' ')[0]) || ticket.ultima_respuesta) : null;

                // Fecha ingreso exacta (normalizada)
                const selFechaStr = this.selectedFechaIngresoFiltro ? this.parseDateOnly(this.selectedFechaIngresoFiltro) : null;
                let matchFechaIngreso = true;

                // If fechaDesde/fechaHasta are set, use range and ignore selectedFechaIngresoFiltro and selectedUltimaRespuestaFiltro
                if (this.fechaDesde || this.fechaHasta) {
                    matchFechaIngreso = true; // default true if no ticket date
                    if (ticketFechaStr) {
                        const fromStr = this.fechaDesde ? this.parseDateOnly(this.fechaDesde) : null;
                        const toStr = this.fechaHasta ? this.parseDateOnly(this.fechaHasta) : null;
                        const ticketDate = new Date(ticketFechaStr + 'T00:00:00');
                        let afterFrom = true;
                        let beforeTo = true;
                        if (fromStr) {
                            const fromDate = new Date(fromStr + 'T00:00:00');
                            afterFrom = ticketDate >= fromDate;
                        }
                        if (toStr) {
                            const toDate = new Date(toStr + 'T00:00:00');
                            beforeTo = ticketDate <= toDate;
                        }
                        matchFechaIngreso = afterFrom && beforeTo;
                    } else {
                        matchFechaIngreso = false;
                    }
                } else if (this.selectedFechaIngresoFiltro) {
                    // exact match by date (no time)
                    matchFechaIngreso = ticketFechaStr && selFechaStr && ticketFechaStr === selFechaStr;
                }

                // Última respuesta filter - only applied when NOT using fechaDesde/fechaHasta and when selectedUltimaRespuestaFiltro is set
                let matchUltimaRespuesta = true;
                if (!this.fechaDesde && !this.fechaHasta && this.selectedUltimaRespuestaFiltro) {
                    const selUltResp = parseDateOnly(this.selectedUltimaRespuestaFiltro);
                    matchUltimaRespuesta = !!(ticketUltimaRespFecha && selUltResp && ticketUltimaRespFecha === selUltResp);
                }

                return matchPqr && matchDescripcion && matchEstado && matchPrioridad && matchUsuario && matchAgente && matchCanal && matchFechaIngreso && matchUltimaRespuesta;
            });

            // si tiene estadoSeleccionado, aplicar filtro adicional
            if (this.estadoSeleccionado) {
                this.tickets = this.tickets.filter(ticket => {
                    return ticket.estado && ticket.estado.toLowerCase() === this.estadoSeleccionado.toLowerCase();
                });
            }

            this.isFiltered = true;
            this.dialogFiltros = false;

            // ✅ Optimizado: Usar método reutilizable
            this.actualizarContadoresCanales();

            // Si hay filtros en historico abiertos y estamos mostrando el dialogo de información,
            // actualizar el historico mostrado en caso de haber aplicado filtros globales que afecten al PQR actual.
            // (no eliminar historicoOriginal aquí; filtrarHistorico maneja su propia copia)
            // No limpiar inmediatamente los campos para que el usuario pueda ver qué filtros aplicó;
            // si se desea limpiar, llamar a limpiarCamposFiltros() desde la UI cuando corresponda.
        },

        async cargarFiltros() {
            try {
                await this.obtenerPQR();

                this.selectPQRFiltro = this.tickets.map(ticket => ({
                    id: ticket.pqr,
                    nombre: ticket.pqr
                }));

                this.selectDescripcionFiltro = this.tickets.map(ticket => ({
                    id: ticket.descripcion,
                    nombre: ticket.descripcion
                }));

                this.selectEstadoFiltro = [
                    { id: 1, nombre: 'Nuevo' },
                    { id: 2, nombre: 'En Proceso' },
                    { id: 3, nombre: 'Cerrado' }
                ];

                this.selectPrioridadFiltro = [
                    { id: 1, nombre: 'Alta' },
                    { id: 2, nombre: 'Media' },
                    { id: 3, nombre: 'Baja' }
                ];

                // llenar una unica vez cada cliente para el select de filtro
                const clientes = this.tickets.map(ticket => ({
                    id: ticket.idCliente,
                    nombre: ticket.nombre_cliente
                }));
                this.selectUsuarioFiltro = [...new Map(clientes.map(cliente => [cliente.id, cliente])).values()];

                // llenar una unica vez cada agente para el select de filtro ignorando los null o vacios
                const agentes = this.tickets
                    .filter(ticket => ticket.agente && ticket.agente.trim() !== '')
                    .map(ticket => ({
                        id: ticket.agente,
                        nombre: ticket.agente
                    }));
                this.selectAgenteFiltro = [...new Map(agentes.map(agente => [agente.id, agente])).values()];
            } catch (error) {
                console.error("Error cargando filtros:", error);
            }
        },



        editarItemPregunta(item) {
            // Guarda el id de la pregunta seleccionada
            this.idPreguntaEditando = item.idPregunta || item.id || item.idpregunta;
            this.idrolactivoPregunta = item.rolactivo;
            console.log("ID de la pregunta a editar:", this.idPreguntaEditando);
            console.log("Rol activo de la pregunta a editar:", this.idrolactivoPregunta);

            // Llena los campos del formulario con los datos de la pregunta seleccionada
            this.nuevaPregunta = item.pregunta;
            this.rolNuevaPregunta = this.selectRol.find(c => c.id == item.idrol);
            this.respuestaBotNuevaPregunta = item.respuesta;
            this.estadoNuevaPregunta = item.estado == 1 || item.estado == '1';

            // Activa modo edición
            this.editandoPreguntaFrecuente = true;
            this.dialogPreguntaNueva = true;
            if (this.idrolactivoPregunta == 0) {
                this.rolInactivo = true;
            }
        },

        limpiarCamposNuevaPregunta() {
            this.nuevaPregunta = '';
            this.rolNuevaPregunta = null;
            this.respuestaBotNuevaPregunta = '';
            this.estadoNuevaPregunta = true;
            this.editandoPreguntaFrecuente = false;
            this.idPreguntaEditando = null;
            this.idrolActivoPregunta = null;
            this.rolInactivo = false;
        },

        limpiarCamposFiltros() {
            this.estadoSeleccionado = null;
            this.selectedPQRFiltro = null;
            this.selectedDescripcionFiltro = null;
            this.selectedEstadoFiltro = null;
            this.selectedPrioridadFiltro = null;
            this.selectedUsuarioFiltro = null;
            this.selectedFechaIngresoFiltro = null;
            this.selectedUltimaRespuestaFiltro = null;
            this.fechaDesde = null;
            this.fechaHasta = null;
            this.selectedAgenteFiltro = null;
            this.canalSeleccionado = 'todos';

            this.filtrarTickets();
            this.isFiltered = false;
            this.dialogFiltros = false;
        },

        // Limpiar todos los filtros desde el botón de escobita
        limpiarTodosFiltros() {
            this.estadoSeleccionado = null;
            this.selectedPQRFiltro = null;
            this.selectedDescripcionFiltro = null;
            this.selectedEstadoFiltro = null;
            this.selectedPrioridadFiltro = null;
            this.selectedUsuarioFiltro = null;
            this.selectedFechaIngresoFiltro = null;
            this.selectedUltimaRespuestaFiltro = null;
            this.fechaDesde = null;
            this.fechaHasta = null;
            this.selectedAgenteFiltro = null;
            this.canalSeleccionado = 'todos';

            this.filtrarTickets();
            this.isFiltered = false;
        },

        obtenerHistorico(idPQR) {

            return axios.post(this.baseURL + 'api/pqrhist', { idpqr: idPQR })
                .then(response => {

                    const datos = response.data.data;

                    this.historico = datos.map(item => ({
                        fecha: item.pqd_fecres || 'Sin fecha',
                        usuario: item.com_nom || 'Desconocido',
                        estado: item.es_nom || 'Sin estado',
                        observaciones: item.pqd_res || 'Sin observaciones',
                        archivos: item.url_archivos ? item.url_archivos.split('----') : [],  // suponiendo que es una cadena separada por guiones
                        mensajes_chat: item.mensajes_chat || 0,
                        canal: item.canal || ''
                    }));

                    // Guardar copia original para poder restaurar después
                    this.historicoOriginal = Array.isArray(this.historico) ? [...this.historico] : [];

                    // Preparar opciones para los selects del menu de historico (fechas/usuarios/estados)
                    const fechas = this.historico
                        .map(h => ({ id: this.parseDateOnly(h.fecha) || h.fecha, nombre: this.parseDateOnly(h.fecha) || h.fecha }))
                        .filter(f => f.id)
                        .reduce((acc, cur) => {
                            if (!acc.find(a => a.id === cur.id)) acc.push(cur);
                            return acc;
                        }, []);

                    const usuarios = this.historico
                        .map(h => ({ id: h.usuario, nombre: h.usuario }))
                        .filter(u => u.id && String(u.id).trim() !== '')
                        .reduce((acc, cur) => {
                            if (!acc.find(a => a.id === cur.id)) acc.push(cur);
                            return acc;
                        }, []);

                    const estados = this.historico
                        .map(h => ({ id: h.estado, nombre: h.estado }))
                        .filter(e => e.id && String(e.id).trim() !== '')
                        .reduce((acc, cur) => {
                            if (!acc.find(a => a.id === cur.id)) acc.push(cur);
                            return acc;
                        }, []);

                    this.selectHistoricoFecha = fechas;
                    this.selectHistoricoUsuario = usuarios;
                    this.selectHistoricoEstado = estados;
                })
                .catch(error => {
                    console.error('Error al cargar histórico:', error);
                });
        },

        filtrarHistorico() {
            // Asegurar copia original
            if (!this.historicoOriginal) {
                this.historicoOriginal = Array.isArray(this.historico) ? [...this.historico] : [];
            }

            const hasFilters = !!(this.selectedHistoricoFecha || this.selectedHistoricoUsuario || this.selectedHistoricoEstado);

            if (!hasFilters) {
                // Restaurar
                this.historico = Array.isArray(this.historicoOriginal) ? [...this.historicoOriginal] : [];
                this.menuHistorico = false;
                return;
            }

            this.historico = (this.historicoOriginal || []).filter(h => {
                let matchFecha = true;
                let matchUsuario = true;
                let matchEstado = true;

                if (this.selectedHistoricoFecha) {
                    const sel = this.parseDateOnly(this.selectedHistoricoFecha.id || this.selectedHistoricoFecha) || (this.selectedHistoricoFecha.id || this.selectedHistoricoFecha);
                    const hf = this.parseDateOnly(h.fecha) || h.fecha;
                    matchFecha = !!(hf && sel && hf === sel);
                }

                if (this.selectedHistoricoUsuario) {
                    const selU = String(this.selectedHistoricoUsuario.id || this.selectedHistoricoUsuario).trim().toLowerCase();
                    const hu = String(h.usuario || '').trim().toLowerCase();
                    matchUsuario = !!(hu && selU && hu === selU);
                }

                if (this.selectedHistoricoEstado) {
                    const selE = String(this.selectedHistoricoEstado.id || this.selectedHistoricoEstado).trim().toLowerCase();
                    const he = String(h.estado || '').trim().toLowerCase();
                    matchEstado = !!(he && selE && he === selE);
                }

                return matchFecha && matchUsuario && matchEstado;
            });

            this.menuHistorico = false;
        },

        limpiarCamposHistorico() {
            this.selectedHistoricoFecha = null;
            this.selectedHistoricoUsuario = null;
            this.selectedHistoricoEstado = null;
            this.historico = Array.isArray(this.historicoOriginal) ? [...this.historicoOriginal] : this.historico;
            this.menuHistorico = false;
        },

        cerrarCrearPQR() {

            this.crearPQR = false;
            this.descripcionCrearPQR = null;
            this.respuestaCrearPQR = null;
            this.estadoCrearPQR = null;
            this.categoriaCrearPQR = null;
            this.subcategoriaCrearPQR = null;

        },


        cerrarInfoPQR() {

            this.estadoServicio = null;
            this.usuarioAsignado = null;
            this.usuarioEscalar = null;
            this.prioridadPQR = null;
            this.categoriaCrearPQR = null;
            this.subcategoriaCrearPQR = null;
            this.respuestaAsesor = null;
            this.informacionServicio = false;
            this.archivos = [];
            this.historico = [];
            this.archivosRespuestaPQR = null;
            this.documentoSeleccionadoCliente = null;
            this.respuestaAsesor = null;
            this.idPQR = '0';
            this.iframeChat = true;
            this.ifDetallesPQR = false;

            this.usuariosPQRAsignar = this.usuariosPQR;
            this.usuariosPQREscalar = this.usuariosPQR;
        },

        async recargarTickets() {
            this.canalSeleccionado = 'todos';
            this.limpiarCamposFiltros();
            this.filtrarTickets();
            this.alerta = true;
            this.ifCargando = true;
            this.mensajeAlerta = 'Recargando tickets...';

            try {
                await this.obtenerPQR();
            } catch (error) {
                console.error("Error recargando tickets:", error);
            } finally {
                this.ifCargando = false;
                this.alerta = false;
                this.mensajeAlerta = '';
            }
        },

        obtenerPQR() {

            return axios.post(this.baseURL + 'api/cargarpqrs', {
                'idusu': localStorage.getItem('idUsuario'),
            })
                .then(response => {

                    const resultados = response.data.data;

                    console.log("Datos recibidos de la API:", resultados);
                    this.tickets = resultados.map((item, index) => ({
                        pqr: item.pq_id,
                        mensaje: item.pq_des,
                        categoria_pqr: item.categoria_pqr,
                        subcategoria_pqr: item.subcategoria_pqr,
                        canal: item.pq_canal,
                        fecha_ingreso: item.pq_fecing,
                        ultima_respuesta: item.pqd_fecres || 'Sin respuesta',
                        cliente: item.co_nom,
                        agente: item.pq_agente != '' ? item.pq_agente : 'Sin Asignar',
                        estado: item.es_nom,
                        prioridad: item.pr_nom,
                        activo_con: item.pq_activo_con,
                        usuario: item.com_nom || 'Sin usuario',
                        nombre_cliente: item.co_nom,
                        opciones: 'Ver',
                        celularCliente: item.co_cel,
                        idCliente: item.co_id,
                        idAsignado: item.asignado_a,
                        idEscalado: item.escalado_a,
                        idInstagram: item.co_instagram || '',
                        idMessenger: item.co_messenger || '',
                    }));

                    console.log('Tickets obtenidos:', this.tickets);

                    // Extraer categorias y subcategorias unicas
                    const categorias = [...new Set(this.tickets.map(t => t.categoria_pqr).filter(Boolean))];
                    this.listaCategorias = categorias.sort();

                    const subcategorias = [...new Set(this.tickets.map(t => t.subcategoria_pqr).filter(Boolean))];
                    this.listaSubcategorias = subcategorias.sort();

                    // Guardar copia original completa (sin filtros) para futuras operaciones de filtrado
                    this.ticketsOriginal = Array.isArray(this.tickets) ? [...this.tickets] : [];

                    // Actualizar contadores por canal con lógica consistente (normalizar texto y validar nulos)
                    this.canales.forEach(canal => {
                        const canalId = String(canal.id || '').toLowerCase();
                        if (canalId === 'todos') {
                            canal.count = this.tickets.length;
                        } else {
                            canal.count = this.tickets.filter(ticket => {
                                const ticketCanal = ticket && ticket.canal ? String(ticket.canal).trim().toLowerCase() : '';
                                return ticketCanal && ticketCanal === canalId;
                            }).length;
                        }
                    });
                })
                .catch(error => {
                    console.error('Error al obtener los tickets:', error);
                });
        },


        async verTicket(item) {
            setTimeout(() => {
                this.dsGestionManual = false;
            }, 2000);
            console.log('Ver ticket seleccionado:', item.item);
            this.canalTicketSeleccionado = item.item.canal;
            this.estadoItemSeleccionado = item.item.estado;
            this.idPQR = item.item.pqr;
            this.descripcionServicio = item.item.descripcion;
            this.informacionServicio = true;
            try {
                await this.obtenerHistorico(this.idPQR);
            } catch (error) {
                console.error("Error obteniendo histórico:", error);
            }
            this.celularCliente = item.item.celularCliente;
            this.nombreClienteSeleccionado = item.item.nombre_cliente;
            this.asignadoActual = item.item.idAsignado;
            this.escaladoActual = item.item.idEscalado;
            this.recipientInstagram = item.item.idInstagram;
            this.recipientMessenger = item.item.idMessenger;
            this.idClienteChat = item.item.idCliente;

            this.activarChat();
        },

        validarUsuariosDisponibles() {
            this.dsGestionManual = true;
            // validar si el id de asignadoActual y escaladoActual existen en la lista de usuarios disponibles para asignar o escalar y quitarlos de la lista si es así
            this.usuariosPQRAsignar = this.usuariosPQR.filter(usuario => usuario.id != this.asignadoActual && usuario.id != this.escaladoActual);
            this.usuariosPQREscalar = this.usuariosPQR.filter(usuario => usuario.id != this.escaladoActual && usuario.id != this.asignadoActual);

            setTimeout(() => {
                this.dsGestionManual = false;
            }, 2000);
        },

        async activarChat() {
            this.disablediconoInstagram = true;
            this.disablediconoMessenger = true;
            this.disablediconoWhastapp = true;
            var celular = '';
            if (this.canalTicketSeleccionado == 'instagram') {
                celular = this.recipientInstagram;
                this.disablediconoInstagram = false;
                this.canalChat = 'instagram';
            } else if (this.canalTicketSeleccionado == 'messenger') {
                celular = this.recipientMessenger;
                this.disablediconoMessenger = false;
                this.canalChat = 'messenger';
            } else {
                celular = this.celularCliente;
                this.disablediconoWhastapp = false;
                this.canalChat = 'whatsapp';
            }

            /* 1: Conversa Activa dentro de las 24 Horas - 0: No hay Conversa Activa dentro de las 24 Horas */
            const response = await axios.post(this.baseURL + 'api/activo24horas', {
                idcli: this.idClienteChat,
                canal: this.canalTicketSeleccionado,
            })
                .then(response => {
                    const resultados = response.data.data;
                    console.log('Conversa Activa:', resultados[0].conversa_activa);
                    if (resultados[0].conversa_activa == 1) {
                        if (this.canalTicketSeleccionado == 'instagram') {
                            this.disablediconoInstagram = false;
                            this.canalChat = 'instagram';
                        } else if (this.canalTicketSeleccionado == 'messenger') {
                            this.disablediconoMessenger = false;
                            this.canalChat = 'messenger';
                        } else {
                            this.disablediconoWhastapp = false;
                            this.canalChat = 'whatsapp';
                        }
                    } else {
                        this.disablediconoInstagram = true;
                        this.disablediconoMessenger = true;
                        this.disablediconoWhastapp = false;
                    }
                })
                .catch(error => {
                    console.error('Error al obtener los tickets:', error);
                });

            console.log('Canal seleccionado para el chat:', this.canalTicketSeleccionado);
            console.log('Celular seleccionado para el chat:', celular);
            // Construir la URL del chat
            this.urlChat = `/chat-web?` + new URLSearchParams({
                ncliente: this.nombreClienteSeleccionado,
                ccliente: celular,
                idusuario: localStorage.getItem('idUsuario'),
                nusuario: this.nombreComercial,
                cusuario: localStorage.getItem('celularLogin'),
                rusuario: '5',
                idpqr: '0',
                perfilm: '0',
                isRecording: '1',
                canal: this.canalTicketSeleccionado || 'web',
                modulo: 'PQR',
            }).toString();

            console.log('Activando chat con URL:', this.urlChat);

            // Mostrar animación de carga como "máscara" visual.
            // Usamos un delay fijo y corto (visual trick). Máximo 3s acordado.
            const delay = 500; // ms (1.2s). Si deseas lo subimos hasta 3000ms.

            this.chatLoading = true;
            this.iframeChat = false; // ocultar iframe mientras carga

            // Después del delay, mostrar iframe y asignar src
            setTimeout(() => {
                this.iframeChat = true;
                // asignar src en el siguiente tick para forzar recarga
                this.$nextTick(() => {
                    const el = document.getElementById('iframeChatID');
                    if (el) {
                        el.src = this.urlChat;
                    }
                });

                this.estadoPQRGrabar = 'En Proceso';
            }, delay);

        },

        onIframeLoaded() {
            // Cuando el iframe termina de cargar, ocultar el loader
            this.chatLoading = false;
            // A veces el iframe envía mensajes postMessage para indicar que está listo; eso puede manejarse en recibirMensaje
            console.log('Iframe chat cargado');
        },

        recibirMensaje(event) {
            if (event.data.action === 'cerrarIframe') {
                this.iframeChat = false;
            } else if (event.data.action === 'mensajesAlmacenados') {
                console.log('Mensajes almacenados recibidos:', event.data.data);
                this.mensajesAlmacenados = JSON.parse(event.data.data);
                console.log('Mensajes almacenados actualizados:', this.mensajesAlmacenados);
                this.agregarHistorialGestion();
            }
        },

        async agregarHistorialGestion() {
            // Eliminamos la restricción de mensajes obligatorios para permitir escalamiento manual
            /*
            if (this.mensajesAlmacenados.length == 0) {
                this.alert = true;
                this.mensajeAlerta = 'No hay mensajes para guardar.';
                return;
            }
            */

            if (this.selectedEstadoChat == null || this.selectedPrioridadChat == null) {
                this.alertaInteres = true;
                this.mensajeAlertInteres = 'Por favor, selecciona una prioridad y un estado para guardar la gestión del PQR.';
                return;
            }

            // Validar escalamiento si el estado es Escalar (id 4)
            if (this.selectedEstadoChat.id == 4 && !this.usuarioEscalarChat) {
                this.alerta = true;
                this.mensajeAlerta = 'Por favor, selecciona un usuario para escalar el caso.';
                return;
            }

            // Filtrar mensajes si existen
            if (this.mensajesAlmacenados && this.mensajesAlmacenados.length > 0) {
                this.mensajesAlmacenados = this.mensajesAlmacenados.filter((msg, index, self) =>
                    index === self.findIndex((m) => m.id === msg.id)
                );
            }

            try {
                // 1. Guardar historial de mensajes (Solo si hay mensajes)
                if (this.mensajesAlmacenados && this.mensajesAlmacenados.length > 0) {
                    const response = await axios.post(this.baseURL + 'api/agregarHistorialGestionWhatsappPQR', {
                        idPQR: this.idPQR,
                        mensajes: this.mensajesAlmacenados,
                        idUsuario: localStorage.getItem('idUsuario'),
                        idEstado: this.selectedEstadoChat.id,
                        idPrioridad: this.selectedPrioridadChat.id,
                        canal: this.canalChat,
                    });
                    console.log('Historial de gestión agregado:', response.data);
                }

                // 2. Guardar respuesta/estado/escalamiento (Siempre)
                // Usamos el mismo endpoint que la gestión manual para asegurar consistencia
                let formData = new FormData();
                const respuesta = this.observacionChat || 'Gestión finalizada desde chat';
                
                formData.append('res', respuesta);
                formData.append('est', this.selectedEstadoChat.id);
                formData.append('id', this.idPQR);
                formData.append('prio', this.selectedPrioridadChat.id);
                formData.append('idusu', localStorage.getItem('idUsuario'));
                formData.append('asignado', this.asignadoActual || 0);
                
                const idEscalado = (this.selectedEstadoChat.id == 4 && this.usuarioEscalarChat) 
                    ? this.usuarioEscalarChat.id 
                    : 0;
                formData.append('escalado', idEscalado);

                await axios.post(this.baseURL + 'api/savePqrRespuesta', formData);

                // Limpieza
                this.mensajesAlmacenados = [];
                this.selectedEstadoChat = null;
                this.selectedPrioridadChat = null;
                this.usuarioEscalarChat = null;
                this.observacionChat = null;
                this.estadoPQRGrabar = null; // Reset chip selection if any

                this.alertaInteres = false;
                this.mensajeAlertInteres = null;
                this.mensajeAlerta = 'La gestión se registró correctamente.';
                this.alerta = true;

                this.obtenerHistorico(this.idPQR);
                this.recargarTickets(); // Actualizar lista principal
                
            } catch (error) {
                console.error('Error al agregar historial de gestión:', error);
            }
        },

        getChatStyle() {
            // Estilos minimalistas para el iframe del chat: sin sombras, bordes suaves,
            // ancho responsivo para encajar dentro del panel derecho.
            return {
                borderRadius: '10px',
                boxShadow: 'none',
                height: '83vh',
                width: '100%',
                border: '1px solid rgba(0,0,0,0.06)',
                backgroundColor: '#ffffff',
                display: 'block'
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

        exportarDatos() {
            axios.post(this.baseURL + 'api/exportarDatosPQR', {}, { responseType: 'blob' })
                .then(response => {
                    const blob = new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = 'datos_pqr.xlsx';
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    this.alerta = true;
                    this.mensajeAlerta = 'Datos exportados a datos_pqr.xlsx';
                })
                .catch(error => {
                    console.error('Error al exportar datos PQR:', error);
                    this.alerta = true;
                    this.mensajeAlerta = 'Error al exportar datos PQR.';
                });
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

        irReserva() {
            this.$router.push('/reserva');
        },

        estadoColor(id) {
            const n = Number(id);
            if (n === 0) return '#1976d2';
            if (n === 1) return '#2e7d32'; // Azul En proceso
            if (n === 2) return 'gray'; // gris
            return '';
        },

        actualizarImagen(url) {
            this.imagenComercial = url;
        },

        setMenuActivoPorRuta() {
            const path = (this.$route.path || '').toLowerCase();
            if (path.includes('/vercampanas')) this.menuActivo = '/vercampanas';
            else if (path.includes('/campana')) this.menuActivo = '/campana';
            else if (path.includes('/contactos')) this.menuActivo = '/contactos';
            else if (path.includes('/prospeccion-telefonica')) this.menuActivo = '/prospeccion-telefonica';
            else if (path.includes('/seguimiento-llamadas')) this.menuActivo = '/seguimiento-llamadas';
            else if (path.includes('/informes-cio')) this.menuActivo = '/informes-cio';
            else if (path.includes('/informes-campanas')) this.menuActivo = '/informes-campanas';
            else if (path.includes('/comercial')) this.menuActivo = '/comercial';
            else if (path.includes('/pendiente-general')) this.menuActivo = '/pendiente-general';
            else if (path.includes('/pedidos')) this.menuActivo = '/pedidos'
            else if (path.includes('/pqr')) this.menuActivo = '/pqr'

            // ...agrega más si tienes otras rutas...
            else this.menuActivo = '';
        },

        cargarRolesIA() {
            axios.post(this.baseURL + 'api/cargarRolesIA', {
                'idrol': 0,
            })
                .then(response => {
                    this.selectRol = response.data.data;
                    console.log("ROLES IA: ", this.selectRol)
                })
                .catch(error => {
                    console.log(error);
                });
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

        getEstadoNombre(id) {
            const estado = this.selectEstadoPreguntasFrecuentes.find(e => e.id === id || e.id == id);
            return estado ? estado.nombre : id;
        },

        getCategoríaNombre(id) {
            const estado = this.selectRol.find(e => e.id === id || e.id == id);
            return estado ? estado.nombre : id;
        },

        getCanalColorModern(canal) {
            const colors = {
                'web': '#FF9800',
                'whatsapp': '#25D366',
                'messenger': '#006AFF',
                'instagram': '#E1306C'
            };
            return colors[canal?.toLowerCase()] || '#64748B';
        },

        getEstadoColorModern(estado) {
            const map = {
                'Nuevo': { bg: '#D1FAE5', text: '#047857', border: '#A7F3D0' },
                'En Proceso': { bg: '#DBEAFE', text: '#1D4ED8', border: '#BFDBFE' },
                'Suspendido': { bg: '#FEF3C7', text: '#B45309', border: '#FDE68A' },
                'Escalado': { bg: '#FEF3C7', text: '#B45309', border: '#FDE68A' },
                'Resuelto': { bg: '#F1F5F9', text: '#334155', border: '#E2E8F0' },
                'Cerrado': { bg: '#F1F5F9', text: '#334155', border: '#E2E8F0' }
            };
            return map[estado] || { bg: '#F1F5F9', text: '#334155', border: '#E2E8F0' };
        },

        getPrioridadColorModern(prioridad) {
            const map = {
                'Alta': { bg: '#FEF2F2', text: '#B91C1C', border: '#FECACA' },
                'Media': { bg: '#FFF7ED', text: '#C2410C', border: '#FED7AA' },
                'Baja': { bg: '#ECFDF5', text: '#047857', border: '#A7F3D0' }
            };
            return map[prioridad] || { bg: '#F1F5F9', text: '#334155', border: '#E2E8F0' };
        },

        // Métodos helper para canales
        getCanalIcono(canal) {
            const iconos = {
                'web': 'mdi-web',
                'whatsapp': 'mdi-whatsapp',
                'messenger': 'mdi-facebook-messenger',
                'instagram': 'mdi-instagram',
                'todos': 'mdi-message-text'
            };
            return iconos[canal?.toLowerCase()] || 'mdi-message-text';
        },

        getCanalColor(canal) {
            const colores = {
                'web': '#FFA500', // Orange predeterminado para web
                'whatsapp': '#25D366', // Verde predeterminado de WhatsApp
                'messenger': '#223551', // Azul predeterminado de Messenger
                'instagram': '#C13584', // color similar para Instagram
                'todos': '#223551' // blue para todos
            };
            return colores[canal?.toLowerCase()] || '#223551';
        },

        getActivoConIcono(activoCon) {
            if (activoCon?.toLowerCase() == 'bot') {
                return 'mdi-robot';
            }
            return 'mdi-face-agent';
        },

        // ✅ Nuevo método helper: Actualizar contadores de canales (reutilizable)
        actualizarContadoresCanales() {
            this.canales.forEach(canal => {
                canal.count = this.tickets.filter(ticket => {
                    if (canal.id === 'todos') return true;
                    return ticket.canal && ticket.canal.toLowerCase() === canal.id.toLowerCase();
                }).length;
            });
        },
    }
}
</script>

<style scoped>
:root {
    --color-teal: #4DB6AC;
    --color-teal-dark: #00897B;
    --color-teal-light: #80CBC4;
    --color-teal-bg: #E0F2F1;
    --color-accent: #FFB74D;
    --color-text-main: #0A1C3A;
}

.text-primary-bold {
    color: #0A1C3A;
    font-weight: bold;
}

.text-primary {
    color: #0A1C3A;
}

.sidebar-gradient {
    background: linear-gradient(90deg, #223551 0%, #2C466B 100%);
}

.bg-light-gray {
    background-color: #F8FAFC;
}

.max-w-1920 {
    max-width: 1920px;
}

.rounded-lg {
    border-radius: 12px;
}

.texto-limitado {
    max-width: 350px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.btn-grow-card-historial {
    transition: transform 0.2s ease-in-out;
}

.btn-grow:hover {
    transform: scale(1.15);
    z-index: 2;
}

.btn-grow-card:hover {
    transform: scale(1.05);
    z-index: 1.5;
}

.btn-grow-card-historial:hover {
    transform: scale(1.02);
    z-index: 1.2;
    background: var(--color-teal-light, #cffffa);
}

.custom-table-modern {
    border-radius: 0 0 12px 12px;
}

.custom-table-modern :deep(th) {
    font-size: 0.75rem !important;
    letter-spacing: 0.05em !important;
}

.custom-table-modern :deep(td) {
    font-size: 0.875rem !important;
    color: #334155 !important;
    height: 64px !important;
}

.custom-table-modern :deep(tbody tr:hover) {
    background-color: #F8FAFC !important;
}

/* Custom Scrollbar for Table */
.custom-scroll-table :deep(.v-table__wrapper)::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

.custom-scroll-table :deep(.v-table__wrapper)::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 4px;
}

.custom-scroll-table :deep(.v-table__wrapper)::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 4px;
    border: 2px solid #f1f5f9;
}

.custom-scroll-table :deep(.v-table__wrapper)::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* ✅ Optimizado: Estilos consolidados para chat y alertas */
.chat-iframe,
.chat-loader {
    width: 95%;
}

.alert-title,
.subheader-dark {
    background: linear-gradient(90deg, #223551 0%, #2C466B 100%);
    color: #ffffff;
    padding: 12px 16px;
    display: flex;
    align-items: center;
}

/* Loader centered block for chat initialization */
.chat-loader {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 95%;
    height: 82vh;
    border-radius: 10px;
    background: linear-gradient(180deg, #ffffff, #f7fbff);
    border: 1px solid rgba(0, 0, 0, 0.03);
}

/* Overlay that sits above the iframe while it's loading */
.chat-loader-overlay {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 95%;
    height: 82vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 10px;
    z-index: 30;
    box-shadow: 0 6px 18px rgba(3, 33, 71, 0.06);
}

.chat-loader-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.fecha-chip {
    background: var(--color-teal-light, #80CBC4);
    color: var(--color-text-main, #0A1C3A);
    font-weight: bold;
    font-size: 14px;
    padding: 4px 12px;
    border-radius: 8px;
    margin-bottom: 8px;
    display: inline-block;
}

.chip-color-background {
    background: var(--color-accent, #FFB74D);
    color: var(--color-text-main, #0A1C3A);
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 8px;
    margin-bottom: 8px;
    display: inline-block;
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

.v-input__prepend .v-icon {
    color: #223551;
}

.menu-item-activo {
    background: #fff !important;
    color: #223551 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 12px 0 #2235511a;
    transition: background 0.2s, color 0.2s;
    padding-top: 5px;
    padding-bottom: 5px;
}

.menu-item-activo .v-list-item-title,
.menu-item-activo .v-icon {
    color: #223551 !important;
}

/* Estilo para el header de la v-data-table */
.v-data-table thead th {
    background-color: #223551 !important;
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

.modern-alert {
    background: #fff0f3 !important;
    color: #b71c1c !important;
    border-radius: 10px !important;
    box-shadow: 0 2px 8px #b71c1c22;
}

.row-rol-inactivo {
    background: linear-gradient(90deg, #ffeaea 60%, #fff 100%);
    /* Fondo rojo muy suave */
    opacity: 0.95;
    border-left: 4px solid #ffb3b3;
    /* Borde rojo suave a la izquierda */
}

/* Estilos personalizados para la nueva tabla de PQR */
.custom-table {
    background: var(--color-teal-bg, #E0F2F1);
    border-radius: 12px;
}

.custom-table :deep(thead th) {
    background-color: var(--color-teal, #4DB6AC) !important;
    color: white !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
    text-align: center !important;
    padding: 12px 8px !important;
}

.custom-table :deep(tbody tr) {
    transition: background-color 0.2s;
}

.custom-table :deep(tbody tr:hover) {
    background-color: var(--color-teal-light, #80CBC4) !important;
}

.custom-table :deep(tbody td) {
    text-align: center !important;
    padding: 10px 8px !important;
    font-size: 0.85rem;
}

/* Estilos para los botones de canal */
.canal-btn {
    transition: all 0.2s ease-in-out;
}

.canal-btn:hover {
    transform: scale(1.05);
}

/* Avatar de canal con fondo oscuro */
.canal-avatar {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s;
}

.canal-avatar:hover {
    transform: scale(1.1);
}

/* Espaciado para los chips */
.gap-2 {
    gap: 8px;
}

/* Redesigned filters dialog styles */
.filters-card {
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 30px rgba(6, 30, 60, 0.12);
}

.filters-title {
    background: linear-gradient(90deg, #223551 0%, #2C466B 100%);
    color: white;
    padding: 14px 16px;
    align-items: center;
}

.filters-body {
    padding: 18px 20px 8px 20px;
}

.section-label {
    font-weight: 600;
    color: #0A1C3A;
    display: block;
    margin-bottom: 8px;
}

.estado-chips {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.chips-enter-active,
.chips-leave-active {
    /* entrada más lenta: duración alineada con chipsEntryDuration (1.2s) */
    transition: transform 700ms cubic-bezier(.2, .9, .2, 1), opacity 1000ms ease;
}

/* ✅ Optimizado: Transiciones de chips consolidadas */
.chips-enter-from,
.chips-leave-to {
    transform: translateX(40px);
    opacity: 0;
}

.chips-enter-to,
.chips-leave-from {
    transform: translateX(0);
    opacity: 1;
}

/* ✅ Optimizado: Estilos base de chips consolidados */
.estado-chip,
.estado-chip2 {
    border-radius: 20px;
    background: transparent;
    text-transform: none;
}

.estado-chip {
    color: #0A1C3A;
}

.estado-chip2 {
    color: #000000;
}

.estado-chip .v-icon {
    margin-right: 4px;
}

/* ✅ Optimizado: Chips activos con base común */
.chip-active-nuevo,
.chip-active-enproceso,
.chip-active-resuelto,
.chip-active-enproceso-grabar,
.chip-active-resuelto-grabar,
.chip-active-escalar-grabar {
    color: white;
}

.chip-active-nuevo {
    background: #00897B;
    box-shadow: 0 4px 12px rgba(0, 108, 161, 0.18);
}

.chip-active-enproceso {
    background: #223551;
    box-shadow: 0 4px 12px rgba(255, 165, 0, 0.18);
}

.chip-active-resuelto {
    background: #F44336;
    box-shadow: 0 4px 12px rgba(244, 67, 54, 0.18);
}

.chip-active-enproceso-grabar {
    background: #0044ff;
    box-shadow: 0 4px 12px rgba(0, 75, 115, 0.18);
}

.chip-active-resuelto-grabar {
    background: #b71c1c;
    box-shadow: 0 4px 12px rgba(170, 46, 37, 0.18);
}

.chip-active-escalar-grabar {
    background: #be5a07;
    box-shadow: 0 4px 12px rgba(139, 0, 0, 0.18);
}

.input-smooth :deep(.v-input__control) {
    border-radius: 8px;
}

.input-smooth :deep(.v-field) {
    background: #ffffff;
    border-radius: 8px;
}

.actions-row {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.02), rgba(0, 0, 0, 0.01));
}

@media (max-width: 720px) {
    .filters-card {
        margin: 0 8px;
    }

    .filters-body {
        padding-left: 12px;
        padding-right: 12px;
    }
}

/* Estilos para alerta vistosa */
.alert-card {
    border-radius: 12px;
    overflow: hidden;
    background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%);
    box-shadow: 0 12px 34px rgba(3, 33, 71, 0.14);
}

.alert-title {
    background: linear-gradient(90deg, #223551 0%, #2C466B 100%);
    color: #ffffff;
    padding: 12px 16px;
    display: flex;
    align-items: center;
}

.alert-heading {
    font-weight: 700;
    font-size: 1rem;
    color: white;
}

.alert-body {
    padding: 18px 20px;
    background: transparent;
}

/* Navigation Drawer Transitions */
.alert-actions {
    padding: 12px 16px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.6), rgba(250, 250, 250, 0.9));
    display: flex;
    align-items: center;
}

.alert-card .v-progress-circular {
    box-shadow: 0 4px 12px rgba(0, 108, 161, 0.12);
}

.btn-apply {
    color: white !important;
    background: linear-gradient(90deg, #223551, #2C466B) !important;
    box-shadow: 0 6px 18px rgba(0, 120, 255, 0.18);
    border-radius: 20px;
}

.btn-apply2 {
    color: white !important;
    background: linear-gradient(90deg, #00A08F, #00897B) !important;
    box-shadow: 0 6px 18px rgba(77, 182, 172, 0.18);
    border-radius: 20px;
}

/* Sub-headers used inside the fullscreen dialog (darker blue to contrast with main dialog header) */
.subheader-dark {
    background: linear-gradient(90deg, #223551 0%, #2C466B 100%);
    color: #ffffff !important;
    box-shadow: 0 6px 18px rgba(0, 64, 96, 0.12);
}

.subheader-dark .v-icon {
    color: #ffffff !important;
}

.subheader-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Estilos para la tabla personalizada */
.custom-table :deep(thead tr th) {
    background-color: #F5F7FA !important;
    color: #223551 !important;
    font-weight: bold;
    border-bottom: 2px solid #223551 !important;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 5px;
    border: 2px solid #f1f5f9;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}



.input-label {
    font-size: 0.75rem;
    font-weight: 700;
    color: #616161;
    /* grey-darken-1 */
    margin-bottom: 4px;
    display: block;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
</style>
<style>
/* Estilos de Scrollbar GLOBAL (movidos aquí para que funcionen en toda la página) */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 5px;
    border: 2px solid #f1f5f9;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* TUS ESTILOS DE LAYOUT ANTERIORES */
html {
    overflow-y: auto !important;
}

.v-application,
.v-application__wrap {
    min-height: 100vh !important;
    height: auto !important;
    overflow: visible !important;
}

.v-main {
    height: auto !important;
    overflow: visible !important;
    flex: 1 0 auto;
}

/* Minimalist Filter Modal Styles */
.filter-close-btn {
    transition: all 0.25s ease;
}

.filter-close-btn:hover {
    transform: rotate(90deg);
    background-color: rgba(0, 0, 0, 0.05) !important;
}

.filter-reset-btn {
    transition: all 0.2s ease;
}

.filter-reset-btn:hover {
    background-color: rgba(0, 155, 144, 0.08) !important;
}

.filter-status-btn {
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    font-weight: 500;
}

.filter-status-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0, 108, 161, 0.15) !important;
}

.filter-status-btn:active {
    transform: translateY(0);
}

.filter-input-field {
    transition: all 0.2s ease;
}

.filter-input-field:hover {
    box-shadow: 0 1px 4px rgba(0, 108, 161, 0.1);
}

.filter-input-field .v-field--focused {
    box-shadow: 0 2px 8px rgba(0, 108, 161, 0.15);
}

.filter-action-btn-secondary {
    transition: all 0.2s ease;
}

.filter-action-btn-secondary:hover {
    background-color: rgba(0, 0, 0, 0.04) !important;
}

/* Subtle icon scale on hover */
.filter-input-field:hover .v-icon {
    transform: scale(1.05);
}

/* Clear Filters Button */
.clear-filters-btn {
    transition: all 0.25s ease;
    background-color: #FFFFFF !important;
    border: 1.5px solid #E0E0E0 !important;
    border-radius: 8px !important;
    min-width: 36px !important;
    height: 36px !important;
}

.clear-filters-btn .v-icon {
    color: #616161 !important;
}

.clear-filters-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(245, 124, 0, 0.2) !important;
    background-color: #FFF3E0 !important;
    border-color: #F57C00 !important;
}

.clear-filters-btn:hover .v-icon {
    color: #F57C00 !important;
    transform: scale(1.1);
}

.clear-filters-btn:active {
    transform: translateY(0);
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
</style>