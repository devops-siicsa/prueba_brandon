<template>
    <v-app>
        <v-row>

            <v-col>

                <v-card style="border-radius: 0px; height: 100vh;" class="d-flex flex-column">

                    <!-- Cabecera de contacto tipo WhatsApp -->
                    <v-row class="align-center pt-3 pl-3 pr-3 pb-n3 fixed-chat-header"
                        style="background: #006CA1; border-radius: 14px 14px 0 0; min-height: 64px; max-height: 72px; height: 64px;">
                        <v-col cols="auto" class="d-flex align-center ml-1">
                            <div class="d-flex align-center" style="gap:8px;">
                                <v-avatar size="44" color="#1976D2" class="mr-2 shadow recording-avatar">
                                    <template v-if="animacionCarga">
                                        <div class="avatar-recording" title="Grabando" role="status" aria-label="Grabando">
                                            <span class="mic-badge">
                                                <v-icon size="12">mdi-microphone</v-icon>
                                            </span>
                                            <div class="recording-dots-row">
                                                <span class="recording-dot"></span>
                                                <span class="recording-dot"></span>
                                                <span class="recording-dot"></span>
                                            </div>
                                        </div>
                                    </template>
                                    <template v-else>
                                        <span style="color: #fff; font-size: 1.15rem; font-weight: 700;">
                                            {{ nombreVisible ? nombreVisible.charAt(0).toUpperCase() : '?' }}
                                        </span>
                                    </template>
                                </v-avatar>
                            </div>

                            <div class="d-flex flex-column justify-center" style="gap: 2px;">
                                <span class="contact-title-name"
                                    style="font-size: 1.08rem; font-weight: 700; color: #fff; line-height: 1.1;">{{
                                        nombreVisible }}</span>
                                <span class="contact-title-phone"
                                    style="font-size: 0.93rem; font-weight: 600; color: #e3f2fd; line-height: 1;">{{
                                        celularCliente }}</span>
                            </div>
                        </v-col>
                        <v-spacer />
                        <v-col cols="auto" class="d-flex flex-column align-center justify-end mr-1" style="gap: 0px;">
                            <div class="d-flex align-center justify-center" style="gap: 12px;">
                                <div v-if="ifSoporte && (canal == 'web' || canal == 'whatsapp')" class="d-flex flex-column align-center">
                                    <v-btn @click="soporteChat()" class="btn-grow" color="#1976D2" title="Soporte"
                                        style="border-radius: 50px; min-width: 32px; height: 32px; padding: 0;">
                                        <v-icon color="#e3f2fd" size="18">mdi-cog</v-icon>
                                    </v-btn>
                                    <span style="font-size: 0.75rem; color: #e3f2fd; margin-top: 2px;">Soporte</span>
                                </div>
                                <div v-if="ifDespedida" class="d-flex flex-column align-center">
                                    <v-btn color="#1976D2" @click="despedidaChat()" class="btn-grow" title="Despedida"
                                        style="border-radius: 50px; min-width: 32px; height: 32px; padding: 0;">
                                        <v-icon color="#e3f2fd" size="18">mdi-exit-run</v-icon>
                                    </v-btn>
                                    <span style="font-size: 0.75rem; color: #e3f2fd; margin-top: 2px;">Despedida</span>
                                </div>
                                <div v-if="ifPausa && (canal == 'web' || canal == 'whatsapp')" class="d-flex flex-column align-center">
                                    <v-btn :color="isPaused ? '#0252a8' : '#1976D2'" @click="pausarChat()"
                                        class="btn-grow" :title="mensajeIconoPausa" :disabled="dsPausa"
                                        style="border-radius: 50px; min-width: 32px; height: 32px; padding: 0;">
                                        <v-icon :color="'#e3f2fd'" size="18">{{ isPaused ? 'mdi-play' : 'mdi-pause'
                                            }}</v-icon>
                                    </v-btn>
                                    <span style="font-size: 0.75rem; color: #e3f2fd; margin-top: 2px;">{{ isPaused ?
                                        'Activar' : 'Pausa' }}</span>
                                </div>
                                <div v-if="ifSaludo && (canal == 'web' || canal == 'whatsapp')" class="d-flex flex-column align-center">
                                    <v-btn color="#1976D2" @click="saludarChat()" title="Saludo Inicial"
                                        style="border-radius: 50px; min-width: 32px; height: 32px; padding: 0;">
                                        <v-icon color="#e3f2fd" size="18">mdi-human-greeting</v-icon>
                                    </v-btn>
                                    <span style="font-size: 0.75rem; color: #e3f2fd; margin-top: 2px;">Saludo</span>
                                </div>
                                <div class="d-flex flex-column align-center" v-if="(canal == 'web' || canal == 'whatsapp') && modulo != 'PQR'">
                                    <v-btn
                                        style="border-radius: 18px; background: #e3f2fd; min-width: 18px; height: 32px;"
                                        variant="tonal" @click="cerrarIframe()" title="Cerrar chat">
                                        <v-icon color="#1976D2" size="22">mdi-close</v-icon>
                                    </v-btn>
                                    <span style="font-size: 0.75rem; color: #e3f2fd; margin-top: 2px;">Cerrar</span>
                                </div>
                            </div>
                        </v-col>
                    </v-row>

                    <!-- Fila de acciones con fondo suave -->
                    <!-- <v-row class="align-center fixed-chat-buttons" style="background: #0277b0;">
                    <v-col v-if="colSoporte"></v-col>
                    <v-col v-if="ifSoporte" class="d-flex justify-center mt-n3">
                        <v-btn @click="soporteChat()" class="btn-grow" variant="tonal" title="Soporte" style="border-radius: 50px;">
                        <v-icon color="#fff">mdi-cog</v-icon>
                        </v-btn>
                    </v-col>
                    <v-col v-if="ifDespedida" class="d-flex justify-center mt-n3">
                        <v-btn color="#2196f3" @click="despedidaChat()" class="btn-grow" variant="tonal" title="Despedida" style="border-radius: 50px;">
                        <v-icon color="#fff">mdi-exit-run</v-icon>
                        </v-btn>
                    </v-col>
                    <v-col v-if="ifPausa" class="d-flex justify-center mt-n3">
                        <v-btn :color="colorIconoPausa" @click="pausarChat()" class="btn-grow" variant="tonal" :title="mensajeIconoPausa" :disabled="dsPausa" style="border-radius: 50px;">
                        <v-icon color="#fff">mdi-pause</v-icon>
                        </v-btn>
                    </v-col>
                    <v-col v-if="ifSaludo" class="d-flex justify-center mt-n3">
                        <v-btn color="#2196f3" @click="saludarChat()" variant="tonal" title="Saludo Inicial" style="border-radius: 50px;">
                        <v-icon color="#fff">mdi-human-greeting</v-icon>
                        </v-btn>
                    </v-col>
                    </v-row> -->


                    <v-card-text class="flex-grow-1 chat-box scroll-custom"
                        style="background-color: #eaedf2; background-size: auto; background-repeat: repeat; overflow-y: auto;">

                        <br>

                        <v-card v-for="mensaje in mensajesChatBot" class="mb-5 ;"
                            :color="mensaje.rol === 0 ? 'white' : '#c3d7eb'"
                            :style="mensaje.rol === 0 ? 'width: fit-content; max-width: 100%; color: black; box-shadow: rgba(0, 0, 0, 0.56) -5px 5px 5px -3px; border-radius: 16px 16px 16px 16px; ' : 'width: fit-content; max-width: 100%; box-shadow: rgba(0, 0, 0, 0.56) 5px 5px 5px -3px; border-radius: 16px 16px 16px 16px; '"
                            :class="mensaje.rol === 0 ? 'mr-auto' : 'ml-auto '">
                            <v-card :color="mensaje.rol === 0 ? 'grey-lighten-2' : 'grey-lighten-2'"
                                style="font-size: 12px; border-radius: 4px 16px 16px 16px;"
                                v-if="modoChat == 1 && mensaje.resp_men != null && mensaje.resp_men != 0">
                                <v-row>

                                    <v-col class="ml-8 mt-2 mb-2">

                                        <v-card-title v-if="modoChat == 1" style="font-size: 12px; font-weight: bold;"
                                            class="ml-n4">{{ mensaje.rol ===
                                                0 ? nombreVisible : 'SIICSA'
                                            }}</v-card-title>

                                        <v-text v-html="mensaje.resp_men_body" style="white-space: pre-wrap;"></v-text>

                                    </v-col>

                                </v-row>

                            </v-card>

                            <v-card-text>

                                <v-row>

                                    <v-col>

                                        <v-row class="mb-n8">
                                            <v-col class="d-flex align-center mb-4" style="gap: 8px;">
                                                <template v-if="mensaje.rol === 0">
                                                    <v-avatar size="34" color="#1976D2">
                                                        <span
                                                            style="color: #fff; font-size: 1.15rem; font-weight: 700;">
                                                            {{ nombreVisible ? nombreVisible.charAt(0).toUpperCase() :
                                                                '?' }}
                                                        </span>
                                                    </v-avatar>
                                                    <span v-if="modoChat == 1"
                                                        style="font-size: 12px; font-weight: bold; white-space: nowrap;">{{
                                                            nombreVisible }}</span>
                                                    <span v-if="modoChat == 2"
                                                        style="font-size: 12px; font-weight: bold; white-space: nowrap;">Ana</span>
                                                </template>
                                                <template v-else-if="mensaje.rol === 1">
                                                    <v-avatar size="38" class="ml-2 mr-2 shadow"
                                                        style="border: 1px solid #e0e0e0;">
                                                        <v-img
                                                            :src="`${baseURL}images/${comercialId}.jpeg?${Date.now()}`" />
                                                    </v-avatar>
                                                    <span v-if="modoChat == 1"
                                                        style="font-size: 12px; font-weight: bold; white-space: nowrap;">SIICSA</span>
                                                    <span v-if="modoChat == 2"
                                                        style="font-size: 12px; font-weight: bold; white-space: nowrap;">SIICSA</span>
                                                </template>
                                            </v-col>

                                            <v-col v-if="modoChat == 1 && rolUsuario == 5">
                                                <v-icon class="mt-1" color="black" style="float: right;"
                                                    @click="responderMensajeD(mensaje.mensaje, mensaje.id)">
                                                    mdi-menu-down
                                                </v-icon>
                                            </v-col>
                                        </v-row>

                                        <v-card-text style="font-size: 12px;" v-if="modoChat == 1">
                                            <v-icon v-if="mensaje.documento === 1">
                                                mdi-file-document
                                            </v-icon>
                                            <v-text v-html="mensaje.mensaje"
                                                style="white-space: pre-wrap; word-break: break-word; max-width: 100%; display: block;"
                                                v-if="mensaje.tipo == 'text' || mensaje.tipo == 'button'"></v-text>
                                            <a v-else-if="mensaje.tipo == 'image'" :href="mensaje.mensaje"
                                                target="_blank" style="color: black;">
                                                <v-img :src="mensaje.mensaje" style="max-width: 100%;"></v-img>
                                            </a>
                                            <audio v-else-if="mensaje.tipo == 'audio'" controls
                                                :src="mensaje.mensaje"></audio>
                                            <video v-else-if="mensaje.tipo == 'video'" controls
                                                :src="mensaje.mensaje"></video>
                                            <a v-else-if="mensaje.tipo == 'document'" :href="mensaje.mensaje"
                                                target="_blank" style="color:#006CA1;">{{
                                                    mensaje.mensaje }}</a>
                                        </v-card-text>

                                        <v-card-text v-if="modoChat == 2">
                                            <v-text v-html="mensaje.mensaje"
                                                style="white-space: pre-wrap; word-break: break-word; max-width: 100%; display: block;">
                                            </v-text>
                                        </v-card-text>

                                        <v-card-text v-for="boton in interaccionesBot" v-if="mensaje.interaccion == 1"
                                            style="font-size: 12px;">
                                            <v-btn :color="boton.color" :append-icon="boton.icon" variant="elevated"
                                                readonly @click="cambioRol(boton.function_id)"
                                                style="box-shadow: rgba(0, 0, 0, 0.56) 0px 0px 5px 2px;">{{
                                                    boton.label }} </v-btn>
                                        </v-card-text>

                                        <v-row style="float: right; font-size: 11px;">
                                            {{ mensaje.horaMensaje }}

                                            <v-icon class="ml-1 mr-2 pb-1" v-if="mensaje.estado === 'sent'"
                                                color="grey">
                                                mdi-check
                                            </v-icon>

                                            <v-icon class="ml-1 mr-2 pb-1" v-if="mensaje.estado === 'delivered'"
                                                color="grey">
                                                mdi-check-all
                                            </v-icon>

                                            <v-icon class="ml-1 mr-2 pb-1" v-if="mensaje.estado === 'read'"
                                                color="blue">
                                                mdi-check-all
                                            </v-icon>
                                        </v-row>

                                    </v-col>

                                </v-row>

                            </v-card-text>

                        </v-card>

                        <!-- moved recording animation to header next to avatar -->

                    </v-card-text>

                    <v-footer
                        style="background-color: #eaedf2; position: sticky; left: 0; bottom: 0; width: 100%; text-align: center; border-top: 2px solid #006CA1; display: flex; flex-grow: 0;">
                        <v-container fluid>

                            <v-row align="center" no-gutters class="ml-n4 mr-n8 " v-if="responderMensaje">
                                <v-col style="flex-grow: 1; max-width: calc(100% - 100px);">
                                    <v-textarea rows="2" v-model="mensajeAResponder" variant="outlined"
                                        style="width: 100%;" hide-details no-resize disabled="true"
                                        bg-color="blue-grey-lighten-3"></v-textarea>
                                </v-col>
                            </v-row>

                            <v-row align="center" no-gutters class="ml-n4 mr-n8">
                                <v-col style="flex-grow: 1; max-width: calc(100% - 100px);">
                                    <v-textarea ref="chatInput" :label="labelMensaje" rows="1" clearable
                                        v-model="mensajeChatBot" variant="outlined" style="width: 100%;" hide-details
                                        @keydown.enter.exact.prevent="validarEnvioMensaje()" auto-grow
                                        append-inner-icon="mdi-paperclip"
                                        @click:append-inner="abrirInput"></v-textarea>
                                        <!-- :disabled="dsMensajeChat" volverlo a poner a este textarea -->
                                    <input type="file" ref="fileInput" style="display: none;" @change="submitFile2()" />
                                </v-col>

                                <v-col cols="auto">
                                    <v-btn color="#006CA1" dark variant="text" style="border-radius: 50px;"
                                        icon="mdi-emoticon-happy-outline" @click="emojiMenu = !emojiMenu">
                                    </v-btn>
                                </v-col>

                                <v-col cols="auto">
                                    <v-btn color="#006CA1" dark variant="text" style="border-radius: 50px;"
                                        icon="mdi-send" @click="validarEnvioMensaje()">
                                    </v-btn>
                                </v-col>
                            </v-row>

                            <v-row v-if="modoChat == 1" class="d-flex align-center justify-start"
                                :style="userChatActivo.includes('BOT')
                                    ? 'background: linear-gradient(90deg, #c7e8ff 100%, #c8e6fa 0%); border-radius: 10px; min-height: 38px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); opacity: 70%'
                                    : 'background: linear-gradient(90deg, #1976D2 100%, #0A1C3A 0%); border-radius: 10px; min-height: 38px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); opacity: 70%'">
                                <v-icon :color="userChatActivo.includes('BOT') ? '#1976D2' : '#e3f2fd'" size="22"
                                    class="ml-3 mr-2">
                                    {{ userChatActivo.includes('BOT') ? 'mdi-robot' : 'mdi-chat-processing' }}
                                </v-icon>
                                <span
                                    :style="userChatActivo.includes('BOT')
                                        ? 'font-size: 1.02rem; font-weight: 600; color: #1976D2; letter-spacing: 0.5px;'
                                        : 'font-size: 1.02rem; font-weight: 600; color: #e3f2fd; letter-spacing: 0.5px;'">
                                    {{ userChatActivo }}
                                </span>
                            </v-row>

                        </v-container>
                    </v-footer>

                </v-card>

            </v-col>

        </v-row>

        <div style="position: fixed; bottom: 100px; right: 50px;">
            <EmojiPicker :native="true" :hide-group-names="true" theme="light" @select="onSelectEmoji"
                v-if="emojiMenu" />
        </div>

        <v-dialog v-model="crearServicio" persistent>
            <v-card :style="getAlertStyle()">
                <v-card-tittle v-text="mensajeCrearServicio" style="color: black; text-align: center;"></v-card-tittle>
                <v-btn class="mt-4 mx-auto" @click="crearServicio = false"
                    style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
            </v-card>
        </v-dialog>

        <div v-if="confirmChat" :style="getAlertStyle()" style="z-index: 9999;" persistent align="center"
            justify="center">
            <p :class="{ 'mx-5': true }"><v-card-tittle v-text="mensajeConfirmChat"></v-card-tittle></p>
            <v-btn class="mt-4" @click="confirmar()"
                style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255);">Si</v-btn>
            <v-btn class="mt-4" @click="cancelar()"
                style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255);">No</v-btn>
        </div>

    </v-app>
</template>

<script>
import { marked } from 'marked';
import { nextTick } from 'vue';
import EmojiPicker from 'vue3-emoji-picker'
import Echo from 'laravel-echo';
import Pusher from 'pusher-js';
import moment from 'moment';
import 'vue3-emoji-picker/css'
import { id } from 'vuetify/locale';
import axios from 'axios';


window.Pusher = Pusher;
export default {

    components: {
        EmojiPicker
    },

    props: {
        ncliente: String,
        ccliente: String,
        idusuario: String,
        nusuario: String,
        cusuario: String,
        rusuario: String,
        idpqr: String,
        perfilm: String,
    },

    data: () => ({

        urlBackend: "https://glpi-siicsa-whbe.azurewebsites.net",

        idMensajeAux: 0,
        colSoporte: false,

        userChatActivo: 'Chat Activo con: BOT',
        imagenModelo: 'https://cdn-icons-png.freepik.com/256/10111/10111027.png',
        modoChat: 1,

        crearServicio: false,
        mensajeCrearServicio: '',
        confirmChat: false,
        mensajeConfirmChat: '',

        nombreCliente: '',
        celularCliente: '',
        idUsuario: '',
        nombreUsuario: '',
        celularUsuario: '',
        rolUsuario: '',
        idPQR: '',
        isRecording: '',
        canal: 'web',
        modulo: '',
        perfilM: '',

        ifSoporte: false,
        ifDespedida: false,
        ifPausa: false,
        ifSaludo: true,
        isPaused: false,
        dsPausa: false,

        dsMensajeChat: true,
        mensajeChatBot: '',
        mensajesChatBot: [],
        interaccionesBot: [],

        emojiMenu: false,

        animacionCarga: false,

        rol_sql: [],
        rol_conversa: [],

        textoPDF: '',
        arregloExcel: [],
        tituloGraficoExcel: '',
        tituloEjeXExcel: '',
        tituloEjeYExcel: '',
        graficoExcel: 0,
        errorArchivo: false,

        labelMensaje: 'Escribe aqui tu mensaje...',

        responderMensaje: false,
        mensajeAResponder: '',
        nombreVisible: '',
        onlineStatus: true, // Cambia a false para probar desconectado

        baseURL: import.meta.env.VITE_API_BASE_URL,
        comercialId: localStorage.getItem('idUsuario'),
        recipient: import.meta.env.VITE_RECIPIENT,
        pusher_key: import.meta.env.VITE_PUSHER_KEY,
        pusher_cluster: import.meta.env.VITE_PUSHER_CLUSTER,

        webhookListener: null,

        estaAlmacenado: false,
        mensajesAlmacenados: [],
    }),

    created() {

        this.nombreCliente = this.$route.query.ncliente;
        this.celularCliente = this.$route.query.ccliente;
        this.idUsuario = this.$route.query.idusuario;
        this.nombreUsuario = this.$route.query.nusuario;
        this.celularUsuario = this.$route.query.cusuario;
        this.rolUsuario = this.$route.query.rusuario;
        this.idPQR = this.$route.query.idpqr;
        this.isRecording = this.$route.query.isRecording;
        this.canal = this.$route.query.canal;
        this.modulo = this.$route.query.modulo;


        console.log(this.$route.query.ncliente);
        console.log(this.$route.query.ccliente);
        console.log(this.$route.query.idusuario);
        console.log(this.$route.query.nusuario);
        console.log(this.$route.query.cusuario);
        console.log(this.$route.query.rusuario);
        console.log(this.$route.query.idpqr);
        console.log(this.$route.query.perfilm);
        console.log('IsRecording: ' + this.$route.query.isRecording);
        console.log(this.$route.query.canal);
        console.log(this.$route.query.modulo);

        if (this.isRecording == '1') {
            this.mensajesAlmacenados = [];
            this.estaAlmacenado = true;
            console.log('Empezar nueva conversacion, mensajesAlmacenados vacio: ', this.mensajesAlmacenados);
        }

        // Activar animacion de grabando si isRecording == '1'
        this.animacionCarga = (this.isRecording == '1');

        // Watch para cambios posteriores en isRecording (si cambia en runtime)
        this.$watch('isRecording', (newVal) => {
            this.animacionCarga = (newVal == '1');
        });

        this.nombreVisible = this.nombreCliente;

        if (this.$route.query.perfilm == '1') {
            this.perfilM = 'CRM-Publicidad';
        } else if (this.$route.query.perfilm == '2') {
            this.perfilM = 'pqrsf';
        } else if (this.$route.query.perfilm == '0') {
            this.perfilM = '';
        }

        setTimeout(() => {

            if (this.rolUsuario == 2 || this.rolUsuario == 1) {

                this.rol_sql.push({
                    role: "system", content: "Hoy es el dia " + new Date().toISOString().slice(0, 10) + ", eres un asistente de chatbot correspondiente a una mesa de soporte tecnológico que solo responde como un experto en sentencias SQL SERVER en base a lo que pide el usuario, intenta solamente dejar las sentencias en tu respuesta, no les agregues nigún caracter especial fuera de los necesarios para la consulta, no usar las funciones scalar que contengan @, no usar LIMIT dentro de las sentencias, por último recuerda mantener un orden correcto de sentencias para no cometer errores en la consulta (FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY). Si solo te estan saludando, responderas unicamente con esta consulta: SELECT GETDATE(). Tienes conocimiento de la tabla llamada 'servicio', Está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de la columna. 'id' de tipo INT (id del servicio). 'detalle' de tipo VARCHAR(descripción del servicio). 'idemp' de tipo INT(id de la tabla 'empresa' a la cual pertenece el servicio). 'idcli' de tipo INT(id de la tabla 'cliente' al cual le pertenece el servicio). 'idsed' de tipo INT(id de la tabla 'sede' de la empresa a la que corresponde el servicio). 'fecha_ingreso' de tipo DATETIME(fecha en la que se ingresó el servicio por primera vez). 'asignado_a' de tipo INT(id de la tabla 'usuario' que atenderá este servicio). 'idprio' de tipo TINYINT(id de la tabla 'prioridad' a la cual se categoriza el servicio). 'idcat' de tipo TINYINT(id de la tabla 'categoria' a la cual pertenece el servicio). 'fecha_atencion' de tipo SMALLDATETIME(fecha asignada para darle solucion al servicio). 'idaten' de tipo TINYINT(id del tipo de atencion del servicio, 1 = Presencial, 2 = Virtual).  'idestado' de tipo TINYINT(id del estado del servicio, 1 = Nuevo, 2 = En proceso, 3 = Resuleto, 4 = Suspendido, 5 = Anulado, 6 = Cerrado por el Cliente, 7 = Cerrado por Siicsa, 8 = Cerrado por Gestor). 'observaciones' de tipo VARCHAR(observaciones del gestor con respecto al servicio). 'observacionesusu' de tipo VARCHAR(observaciones del usuario con respecto al servicio). 'correo' de tipo TINYINT(indicativo de si el servicio fue creado por correo). 'puesto_por' de tipo VARCHAR(si el servicio fue diligenciado por la pagina web o desde el chatbot, las opciones son 'Web' o 'Bot'). Tienes conocimiento de la tabla llamada 'usuario', esta tabla es utilizada unicamente cuando se hacen preguntas que involucren a un técnico o a un gestor o un agente, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del usuario). 'cedula' de tipo VARCHAR (numero de identificación del usuario). 'nombre' de tipo VARCHAR (nombre del usuario). 'apellido' de tipo VARCHAR (apellido del usuario). 'correo' de tipo VARCHAR (correo del usuario). 'celular' de tipo VARCHAR (celular del usuario). 'celular' de tipo VARCHAR (numero de celular del usuario). 'activo' de tipo TINYINT (1 si el usuario está activo, 0 si por el contrario está inhabilitado). 'fecha_sistema' de tipo SMALLDATETIME (fecha en la que se creo el usuario). 'standby' de tipo INT (1 si el usuario está en disponibilidad o 0 si no lo está). 'fecha_inicio' de tipo DATE (fecha en la que el usuario comenzó a estar en disponibilidad). 'periodo' de tipo INT (1 = Anual, 2 = Semestral). Tambien tienes conocimiento de la tabla llamada 'cliente', esta tabla se utiliza cuando se hacen preguntas relacionadas a los usuarios pertenecientes a las diferentes empresas que tienen servicios con nosotros, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del cliente). 'celular' de tipo VARCHAR (celular del cliente). 'nombre' de tipo VARCHAR (nombre del cliente). 'correo' de tipo VARCHAR (correo del cliente). 'idsed' de tipo INT (id de la tabla sede a la que pertenece segun la empresa a la que esté afiliado). 'fecha_sistema' de tipo SMALLDATETIME (fecha en la que se creó el cliente). 'estado' de tipo TINYINT (Si está activo o no el cliente, representado 1 como activo y 0 como inactivo). 'apellido' de tipo VARCHAR (apellido del cliente). Tambien tienes conocimiento de la tabla llamada 'empresa', esta tabla se utiliza cuando se hacen preguntas relacionadas a las empresas (o tambien llamados clientes) que están asociadas con nosotros, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la empresa). 'razon_social' de tipo VARCHAR (nombre de la empresa). 'contactoppal' de tipo VARCHAR (nombre de la persona seleccionada como contacto directo de la empresa). 'contactotel' de tipo VARCHAR (celular de la persona seleccionada como contacto directo de la empresa). 'tipopers' de tipo INT (tipo de persona, 1 = Jurídica, 2 = Natural). 'tipoidentif' de tipo INT (tipo de identificacion, 1 = Cédula de Ciudadanía, 2 = Cédula de Extranjería, 3 = NIT, 4 = Pasaporte). 'activo' de tipo TINYINT (1 si la empresa está activa, 0 si por el contrario está inhabilitada). 'fecha_sistema' de tipo SMALLDATETIME (fecha en la que se creo la empresa). 'nit' de tipo VARCHAR (NIT de la empresa). 'festivo' de tipo INT (1 si trabaja los dias festivos, 0 si por el contrario no trabaja en dias festivos). Tambien tienes conocimiento de la tabla llamada 'obs_cliente', esta tabla se utiliza cuando se hacen preguntas relacionadas a las observaciones que hacen los usuarios con respecto a los tickets o tambien llamado servicios que solicitaron, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la observacion). 'idserv' de tipo INT (id de la tabla 'servicio' a la cual pertenertenece esta observacion). 'fecha' de tipo SMALLDATETIME (fecha en la que se creo la observacion). 'detalle' de tipo VARCHAR(descripción de la observacion). Tambien tienes conocimiento de la tabla llamada 'obs_gestor', esta tabla se utiliza cuando se hacen preguntas relacionadas a las observaciones que hace el gestor con respecto a los tickets o tambien llamado servicios que se ha solicitado a la mesa de soporte, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la observacion). 'idserv' de tipo INT (id de la tabla 'servicio' a la cual pertenertenece esta observacion). 'fecha' de tipo SMALLDATETIME (fecha en la que se creo la observacion). 'detalle' de tipo VARCHAR(descripción de la observacion). 'idage' de tipo INT (id de la tabla 'usuario' que pertenece al agente de soporte asignado durante esta observacion). 'estado_momento' de tipo INT (estado en el que se encontraba el ticket al momento de realizar la observacion). Tambien tienes conocimiento de la tabla llamada 'pqr', esta tabla se utiliza cuando se hacen preguntas relacionadas a los pqr que hemos recibido por parte de nuestros usuarios, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del pqr). 'descripcion' de tipo VARCHAR (descripción del pqr). 'idcli' de tipo INT(id de la tabla 'cliente' al cual le pertenece el pqr). 'fecha' de tipo SMALLDATETIME (fecha en la que se creo el pqr). 'estado' de tipo INT (estado en el que se encuentra el pqr, 0 = Nuevo, 1 = Resuelto). 'respuesta' de tipo VARCHAR (Respuesta que el gestor le dió al pqr). Tambien tienes conocimiento de la tabla llamada 'sede', esta tabla se utiliza cuando se hacen preguntas relacionadas a la sede desde la cual fue solicitado un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la sede). 'nombre' de tipo VARCHAR (nombre de la sede). 'direccion' de tipo VARCHAR (direccion de la sede). 'ciudad' de tipo VARCHAR (nombre de la sede). 'telefono' de tipo VARCHAR (telefono de la sede). 'idemp' de tipo INT (id de la tabla 'empresa' a la cual pertenece la sede). Tambien tienes conocimiento de la tabla llamada 'estado', esta tabla se utiliza cuando se hacen preguntas relacionadas a los estados de un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del estado). 'nombre' de tipo VARCHAR (nombre del estado). Tambien tienes conocimiento de la tabla llamada 'prioridad', esta tabla se utiliza cuando se hacen preguntas relacionadas al nivel de prioridad actual de un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la prioridad). 'nombre' de tipo VARCHAR (nombre de la prioridad). Tambien tienes conocimiento de la tabla llamada 'tipo_atencion', esta tabla se utiliza cuando se hacen preguntas relacionadas al tipo de atencion quese le está dando a un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del tipo de atencin). 'nombre' de tipo VARCHAR (nombre del tipo de atencion). Tambien tienes conocimiento de la tabla llamada 'tipo_persona', esta tabla se utiliza cuando se hacen preguntas relacionadas al tipo de persona registrada como contacto directo de una empresa registrada, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del tipo de persona). 'nombre' de tipo VARCHAR (nombre del tipo de persona). Tambien tienes conocimiento de la tabla llamada 'tipo_identificacion', esta tabla se utiliza cuando se hacen preguntas relacionadas al tipo de identificacion de la persona registrada como contacto directo de una empresa registrada, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del tipo de identificacion). 'nombre' de tipo VARCHAR (nombre del tipo de identificacion). Tambien tienes conocimiento de la tabla llamada 'categoria', esta tabla se utiliza cuando se hacen preguntas relacionadas a la categoria a la que pertenece el ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la categoria). 'nombre' de tipo VARCHAR (nombre de la categoria). Tambien tienes conocimiento de la tabla llamada 'servico_detalle', esta tabla se utiliza cuando se hacen preguntas relacionadas al historial de atencion de un ticket o servicio, es basicamente el proceso que hizo el técnico encargado del ticket para darle respuesta, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la categoria). 'fecha_registro' de tipo SMALLDATETIME (Fecha en que se creo la observación). 'fecha_inicio' de tipo SMALLDATETIME (Fecha en que se inicio la observación). 'fecha_fin' de tipo SMALLDATETIME (Fecha en que finalizó la observación). 'idserv' de tipo INT (id del a tabla 'servicio' a la cual pertenece la observación). 'idage' de tipo INT (id del a tabla 'usuario' que pertenece al técnico encargado del servicio). 'idesta' de tipo INT (id del a tabla 'estado' representa el estado en el que se encuentra la observación, 1 = Nuevo, 2 = En proceso, 3 = Resuelto). 'detalle' de tipo VARCHAR (Descripción detallada de la observación). 'observacion' de tipo VARCHAR (Observación destinada al gestor alusiva al procedimiento realizado para darle respuesta al ticket). 'estado_momento' de tipo INT (id del a tabla 'estado' representa el estado del ticket al momento de realizar la observación, 1 = Nuevo, 2 = En proceso, 3 = Resuelto). Las relaciones de las tablas son las siguientes: la tabla 'servicio' está relacionada con la tabla 'empresa' mediante la columna 'idemp', está relacionada con la tabla 'cliente' mediante la columna 'idcli', está relacionada con la tabla 'sede' mediante la columna 'idsed', está relacionada ccon la tabla 'usuario' mediante la columna 'asignado_a', está realacionada con la tabla 'prioridad' mediante la columna 'idprio', está relacionada con la tabla 'categoria' mediante la columna 'idcat', está relacionada con la tabla 'tipo_atencion' mediante la columna 'idaten', está relacionada con la tabla 'estado' mediante la columna 'idestado'. La tabla 'cliente' está relacionada con la tabla 'sede' mediante la columna 'idsed'. La tabla 'empresa' está relacionada con la tabla 'tipo_persona' mediante la columna 'tipopers' está relacionada con la tabla 'tipo_identificacion' mediante la columna 'tipoidentif'. La tabla 'obs_cliente' está relacionada con la tabla 'servicio' mediante la columna 'idserv'. La tabla 'obs_gestor' está relacionada con la tabla 'servicio' mediante la columna 'idserv', está relacionada con la tabla 'usuario' mediante la columna 'idage', está relacionada con la tabla 'estado' mediante la columna 'estado_momento'. La tabla 'pqr' está relacionada con la tabla 'cliente' mediante la columna 'idcli'. La tabla 'sede' está relacionada con la tabla 'empresa' mediante la columna 'idemp'. La tabla 'servico_detalle' está relacionada con la tabla 'servicio' mediante la columna 'idserv', está relacionada con la tabla 'usuario' mediante la columna 'idage', está relacionada con la tabla 'estado' mediante la columna 'idesta'. Si te hacen esta pregunta o una similar a esta: 'Quien es Juan Camilo Gallardo', donde se incluya el nombre completo de una persona, tu respuesta siempre debe ser esta consulta: SELECT 'Cliente' AS Tipo, c.nombre AS Nombre, c.apellido AS Apellido, c.correo AS Correo, c.celular AS Celular FROM cliente c WHERE LOWER(REPLACE(CONCAT(c.nombre COLLATE Latin1_General_CI_AI, ' ', c.apellido COLLATE Latin1_General_CI_AI), ' ', '')) = LOWER(REPLACE('Inserta el nombre solicitado aquí' COLLATE Latin1_General_CI_AI, ' ', '')) UNION SELECT 'Usuario' AS Tipo, u.nombre AS Nombre, u.apellido AS Apellido, u.correo AS Correo, u.celular AS Celular FROM usuario u WHERE LOWER(REPLACE(CONCAT(u.nombre COLLATE Latin1_General_CI_AI, ' ', u.apellido COLLATE Latin1_General_CI_AI), ' ', '')) = LOWER(REPLACE('Inserta el nombre solicitado aquí' COLLATE Latin1_General_CI_AI, ' ', '')), pero si por otra parte ves que solo está escrito el nombre, haras esta consulta: SELECT 'Cliente' AS Tipo, c.nombre AS Nombre, c.apellido AS Apellido, c.correo AS Correo, c.celular AS Celular FROM cliente c WHERE LOWER(REPLACE(c.nombre COLLATE Latin1_General_CI_AI, ' ', '')) = LOWER(REPLACE('Inserta el nombre solicitado aquí' COLLATE Latin1_General_CI_AI, ' ', '')) UNION SELECT 'Usuario' AS Tipo, u.nombre AS Nombre, u.apellido AS Apellido, u.correo AS Correo, u.celular AS Celular FROM usuario u WHERE LOWER(REPLACE(u.nombre COLLATE Latin1_General_CI_AI, ' ', '')) = LOWER(REPLACE('Inserta el nombre solicitado aquí' COLLATE Latin1_General_CI_AI, ' ', '')), como ultima opcion si solo te dan un apellido, haras la siguiente consulta: SELECT 'Cliente' AS Tipo, c.nombre AS Nombre, c.apellido AS Apellido, c.correo AS Correo, c.celular AS Celular FROM cliente c WHERE LOWER(REPLACE(c.apellido COLLATE Latin1_General_CI_AI, ' ', '')) = LOWER(REPLACE('Inserta el nombre solicitado aquí' COLLATE Latin1_General_CI_AI, ' ', '')) UNION SELECT 'Usuario' AS Tipo, u.nombre AS Nombre, u.apellido AS Apellido, u.correo AS Correo, u.celular AS Celular FROM usuario u WHERE LOWER(REPLACE(u.apellido COLLATE Latin1_General_CI_AI, ' ', '')) = LOWER(REPLACE('Inserta el nombre solicitado aquí' COLLATE Latin1_General_CI_AI, ' ', '')), recuerda siempre inserta el nombre, apellido o nombre completo que ingresa el usuario dentro de cada tipo de consulta. Recuerda siempre poner alias en los selects que hagas para mejor manejo de la informacion devuelta por la consulta. Si el usuario te solicita un dato que se responde con una consulta sql que combine varias tablas y por ejemplo se trate del nombre completo del usuario 'X' entonces debes asignarle un alias que contenga un guion bajo y el nombre del a tabla a la que pertenece ese dato al final para poder reconocerlo, ejemplo: 'AS nombreCompleto_usuario'. Adicionalmente debes tener muy en cuenta los tipos de dato de cada columna de cada tabla suministrada para poder hacer las conversiones necesarias en base a la pregunta del usuario. Recuerda todas las fechas convertirlas adecuadamente segun la pregunta del usuario y el tipo de dato que maneja la columna que debes manipular (si fecha_sistema de la tabla servicio es DATETIME, le haces un CAST(AS DATE) si el usuario pregunta solo con la fecha, mas no con la hora). Si debes usar los nombres de los usuarios o clientes para una consulta, no las modifiques ni le cambies mayusculas o tildes, usalas tal cual el usuario lo indica o si debes usarlo según el historial de mensajes. Recuerda usar expresiones admitidas y correctas para sql server para no generar un error de base de datos y no poder contestar al usuario con su pregunta. Pueden existir casos donde el usuario esté pidiendo generar un documento PDF, tu sigue con normalidad generando una consulta para sql server que se puede generar en base a la peticion del usuario. Pueden existir otros casos donde el usuario esté pidiendo generar un grafico para ese documento PDF, tu sigue con normalidad generando una consulta para sql server que se puede generar en base a la peticion del usuario."
                });

                this.rol_conversa.push({
                    role: "system", content: "Eres un asistente de chatbot que responde al nombre de Ana y correspondes a una mesa de soporte tecnológico. Vas a charlar con" + this.nombreUsuario + ", tendras que leer la pregunta inicial hecha por dicha persona y luego un json convertido a string. Ambos estan separados por un ';', la primera parte siempre será la pregunta de la persona y la segunda parte es la información util para responder su pregunta, intenta siempre agregar emojis con contexto de tu respuesta para hacer la conversa mas dinamica con el usuario que pregunta. Debes tener en cuenta la consulta que se utilizó para suministrar información en el JSON y saber contestar adecuadamente segun el contexto de la pregunta y el JSON convertido a string. Si " + this.nombreUsuario + " simplemente esta saludando, no importa que el json venga con un error de sql, tu saluda como un asistente cordial y utiliza su nombre para que se sienta mas familiarizado contigo, luego pregunta en que puedes colaborarle. Si el usuario te pide un documento PDF, debes contestar unicamente con la informacion del json de manera organizada y omite cualquier clase de comentario hacia el usuario, por ejemplo omite los comentarios al principo como los de 'Aqui tienes la información solicitada', o los comentarios al final como 'Eso seria todo, necesitas ayuda con algo mas?'. Si el usuario te pide un documento Excel, debes contestar unicamente con la información suministrada por el json en formato lista de listas, por ejemplo: 'Grafico: 0-[['Id Ticket', 'Detalle', 'Estado'], [256, 'Prueba 1', 'En Proceso'], [528, 'Prueba 2', 'Resuelto']]' y omite los comentarios al principo como los de 'Aqui tienes la información solicitada', o los comentarios al final como 'Eso seria todo, necesitas ayuda con algo mas?'. Si junto al excel te piden gráficos, adicional a tu respuesta estructurada debes adicionar separado por lineas lo siguiente: Titulo del gráfico, titulo de los datos del eje x y titulo de los datos del eje y, por tanto tu respuesta final seria por ejemplo asi: Grafico: 1-[['Id Ticket', 'Detalle', 'Estado'], [256, 'Prueba 1', 'En Proceso'], [528, 'Prueba 2', 'Resuelto']]-Título del gráfico: Resumen de Servicios por Categoría-Título de los datos del eje x: Categorías-Título de los datos del eje y: Cantidad. Aunque la informacion suministrada en el json no parezca contener un titulo adecuado, recuerda siempre relacionar esa informacion con la pregunta del usuario para poder responder su pregunta y no des respuestas negativas sabiendo que el json si contiene información, solo responde al usuario de manera cordial. Si la información suministrada te habla de estados pero solo te muestra numeros, debes decirl el nombre del estado segun lo siguiente, 1 = Nuevo, 2 = En proceso, 3 = Resuelto, 4 = Suspendido, 5 = Anulado, 6 = Cerrado por el Cliente, 7 = Cerrado por Siicsa, 8 = Cerrado por Gestor. Si la información suministrada te habla de tipo de persona pero solo te muestra numeros, debes decirle el nombre de tipo de persona segun lo siguiente, 1 = Natural, 2 = Juridica. Si te hablan de tipo de atención pero solo ves numeros, debes contestar segun lo siguiente, 1 = Presencial, 2 = Virtual. Si te hablan de periodo pero el json solo contiene numeros deberas contestar segun lo siguiente, 1 = Anual, 2 = Semestral. Si te hablan de tipo de identificacion pero solo te dan numeros  en el json deberas contestar segun lo siguiente, 1 = Cédula de Ciudadanía, 2 = Cédula de Extranjería, 3 = NIT, 4 = Pasaporte. Si te hablan de categoria pero solo te entregan numeros deberas responder segun lo siguiente, 1 = Punto Venta, 2 = Mantenimiento, 3 = Antivirus, 4 = Servidores, 5 = implementacion, 6 = Impresoras, 7 = Varios, 38 = Office 365, 39 = Auditoria. Si te hablan de prioridad pero solo te entregan numeros deberas contestar segun lo siguiente, 2 = Alta, 3 = Media, 4 = Baja. Si la pregunta es acerca de la cantidad de servicios pero la información en el json viene vacia, dile que no hay servicios según la pregunta del usuario. Cuando te den nombres de usuarios, clientes, agentes o empresas, deja el nombre tal cual como viene escrito en el json, no le cambies mayusculas ni tildes si las trae. Recuerda ser muy cordial con tu respuesta y preguntar siempre después de contestar si el usuario requiere ayuda con alguna otra pregunta. Recuerda no desviarte del tema, en caso de que la información devuelva un error de bases de datos, debes responder simplemente con que no se pudo obtener esa información y que intente mas tarde o algo asi parecido, en caso de que la pregunta no tenga nada que ver con la mesa de soporte debes responder que no puedes ayudarlo y que por favor solo se traten temas relacionados. No puedes responder absolutamente nada que tenga que ver con las consultas sql ejecutadas para traer la información necesaria para responder la pregunta del usuario, cualquier pregunta relacionada al respecto dile que no puedes ayudarlo con esa información porque es privada y dile si necesita ayuda con otra pregunta."
                });

            } else {

                this.rol_sql.push({
                    role: "system", content: "Hoy es el dia " + new Date().toISOString().slice(0, 10) + ", eres un asistente de chatbot correspondiente a una mesa de soporte tecnológico que solo responde como un experto en sentencias SQL SERVER en base a lo que pide el usuario, intenta solamente dejar las sentencias en tu respuesta, no les agregues nigún caracter especial fuera de los necesarios para la consulta, no usar las funciones scalar que contengan @, no usar LIMIT dentro de las sentencias, por último recuerda mantener un orden correcto de sentencias para no cometer errores en la consulta (FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY). Si solo te estan saludando, responderas unicamente con esta consulta: SELECT GETDATE(). Tienes conocimiento de la tabla llamada 'servicio', Está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de la columna. 'id' de tipo INT (id del servicio). 'detalle' de tipo VARCHAR(descripción del servicio). 'idemp' de tipo INT(id de la tabla 'empresa' a la cual pertenece el servicio). 'idcli' de tipo INT(id de la tabla 'cliente' al cual le pertenece el servicio). 'idsed' de tipo INT(id de la tabla 'sede' de la empresa a la que corresponde el servicio). 'fecha_ingreso' de tipo DATETIME(fecha en la que se ingresó el servicio por primera vez). 'asignado_a' de tipo INT(id de la tabla 'usuario' que atenderá este servicio). 'idprio' de tipo TINYINT(id de la tabla 'prioridad' a la cual se categoriza el servicio). 'idcat' de tipo TINYINT(id de la tabla 'categoria' a la cual pertenece el servicio). 'fecha_atencion' de tipo SMALLDATETIME(fecha asignada para darle solucion al servicio). 'idaten' de tipo TINYINT(id del tipo de atencion del servicio, 1 = Presencial, 2 = Virtual).  'idestado' de tipo TINYINT(id del estado del servicio, 1 = Nuevo, 2 = En proceso, 3 = Resuelto, 4 = Suspendido, 5 = Anulado, 6 = Cerrado por el Cliente, 7 = Cerrado por Siicsa, 8 = Cerrado por Gestor). 'observaciones' de tipo VARCHAR(observaciones del gestor con respecto al servicio). 'observacionesusu' de tipo VARCHAR(observaciones del usuario con respecto al servicio). 'correo' de tipo TINYINT(indicativo de si el servicio fue creado por correo). 'puesto_por' de tipo VARCHAR(si el servicio fue diligenciado por la pagina web o desde el chatbot, las opciones son 'Web' o 'Bot'). Tienes conocimiento de la tabla llamada 'usuario', esta tabla es utilizada unicamente cuando se hacen preguntas que involucren a un técnico o a un gestor o un agente, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del usuario). 'cedula' de tipo VARCHAR (numero de identificación del usuario). 'nombre' de tipo VARCHAR (nombre del usuario). 'apellido' de tipo VARCHAR (apellido del usuario). 'correo' de tipo VARCHAR (correo del usuario). 'celular' de tipo VARCHAR (celular del usuario). 'celular' de tipo VARCHAR (numero de celular del usuario). 'activo' de tipo TINYINT (1 si el usuario está activo, 0 si por el contrario está inhabilitado). 'fecha_sistema' de tipo SMALLDATETIME (fecha en la que se creo el usuario). 'standby' de tipo INT (1 si el usuario está en disponibilidad o 0 si no lo está). 'fecha_inicio' de tipo DATE (fecha en la que el usuario comenzó a estar en disponibilidad). 'periodo' de tipo INT (1 = Anual, 2 = Semestral). Tambien tienes conocimiento de la tabla llamada 'cliente', esta tabla se utiliza cuando se hacen preguntas relacionadas a los usuarios pertenecientes a las diferentes empresas que tienen servicios con nosotros, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del cliente). 'celular' de tipo VARCHAR (celular del cliente). 'nombre' de tipo VARCHAR (nombre del cliente). 'correo' de tipo VARCHAR (correo del cliente). 'idsed' de tipo INT (id de la tabla sede a la que pertenece segun la empresa a la que esté afiliado). 'fecha_sistema' de tipo SMALLDATETIME (fecha en la que se creó el cliente). 'estado' de tipo TINYINT (Si está activo o no el cliente, representado 1 como activo y 0 como inactivo). 'apellido' de tipo VARCHAR (apellido del cliente). Tambien tienes conocimiento de la tabla llamada 'empresa', esta tabla se utiliza cuando se hacen preguntas relacionadas a las empresas (o tambien llamados clientes) que están asociadas con nosotros, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la empresa). 'razon_social' de tipo VARCHAR (nombre de la empresa). 'contactoppal' de tipo VARCHAR (nombre de la persona seleccionada como contacto directo de la empresa). 'contactotel' de tipo VARCHAR (celular de la persona seleccionada como contacto directo de la empresa). 'tipopers' de tipo INT (tipo de persona, 1 = Jurídica, 2 = Natural). 'tipoidentif' de tipo INT (tipo de identificacion, 1 = Cédula de Ciudadanía, 2 = Cédula de Extranjería, 3 = NIT, 4 = Pasaporte). 'activo' de tipo TINYINT (1 si la empresa está activa, 0 si por el contrario está inhabilitada). 'fecha_sistema' de tipo SMALLDATETIME (fecha en la que se creo la empresa). 'nit' de tipo VARCHAR (NIT de la empresa). 'festivo' de tipo INT (1 si trabaja los dias festivos, 0 si por el contrario no trabaja en dias festivos). Tambien tienes conocimiento de la tabla llamada 'obs_cliente', esta tabla se utiliza cuando se hacen preguntas relacionadas a las observaciones que hacen los usuarios con respecto a los tickets o tambien llamado servicios que solicitaron, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la observacion). 'idserv' de tipo INT (id de la tabla 'servicio' a la cual pertenertenece esta observacion). 'fecha' de tipo SMALLDATETIME (fecha en la que se creo la observacion). 'detalle' de tipo VARCHAR(descripción de la observacion). Tambien tienes conocimiento de la tabla llamada 'obs_gestor', esta tabla se utiliza cuando se hacen preguntas relacionadas a las observaciones que hace el gestor con respecto a los tickets o tambien llamado servicios que se ha solicitado a la mesa de soporte, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la observacion). 'idserv' de tipo INT (id de la tabla 'servicio' a la cual pertenertenece esta observacion). 'fecha' de tipo SMALLDATETIME (fecha en la que se creo la observacion). 'detalle' de tipo VARCHAR(descripción de la observacion). 'idage' de tipo INT (id de la tabla 'usuario' que pertenece al agente de soporte asignado durante esta observacion). 'estado_momento' de tipo INT (estado en el que se encontraba el ticket al momento de realizar la observacion). Tambien tienes conocimiento de la tabla llamada 'sede', esta tabla se utiliza cuando se hacen preguntas relacionadas a la sede desde la cual fue solicitado un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la sede). 'nombre' de tipo VARCHAR (nombre de la sede). 'direccion' de tipo VARCHAR (direccion de la sede). 'ciudad' de tipo VARCHAR (nombre de la sede). 'telefono' de tipo VARCHAR (telefono de la sede). 'idemp' de tipo INT (id de la tabla 'empresa' a la cual pertenece la sede). Tambien tienes conocimiento de la tabla llamada 'estado', esta tabla se utiliza cuando se hacen preguntas relacionadas a los estados de un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del estado). 'nombre' de tipo VARCHAR (nombre del estado). Tambien tienes conocimiento de la tabla llamada 'prioridad', esta tabla se utiliza cuando se hacen preguntas relacionadas al nivel de prioridad actual de un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la prioridad). 'nombre' de tipo VARCHAR (nombre de la prioridad). Tambien tienes conocimiento de la tabla llamada 'tipo_atencion', esta tabla se utiliza cuando se hacen preguntas relacionadas al tipo de atencion quese le está dando a un ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id del tipo de atencin). 'nombre' de tipo VARCHAR (nombre del tipo de atencion). Tambien tienes conocimiento de la tabla llamada 'categoria', esta tabla se utiliza cuando se hacen preguntas relacionadas a la categoria a la que pertenece el ticket o servicio, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la categoria). 'nombre' de tipo VARCHAR (nombre de la categoria). Tambien tienes conocimiento de la tabla llamada 'servico_detalle', esta tabla se utiliza cuando se hacen preguntas relacionadas al historial de atencion de un ticket o servicio, es basicamente el proceso que hizo el técnico encargado del ticket para darle respuesta, está compuesta por la siguientes columnas, siendo las palabras encerradas entre comillas simples los nombres de cada columna, seguido del tipo de dato sql y entre paréntesis una breve descripción de columna. 'id' de tipo INT (id de la categoria). 'fecha_registro' de tipo SMALLDATETIME (Fecha en que se creo la observación). 'fecha_inicio' de tipo SMALLDATETIME (Fecha en que se inicio la observación). 'fecha_fin' de tipo SMALLDATETIME (Fecha en que finalizó la observación). 'idserv' de tipo INT (id del a tabla 'servicio' a la cual pertenece la observación). 'idage' de tipo INT (id del a tabla 'usuario' que pertenece al técnico encargado del servicio). 'idesta' de tipo INT (id del a tabla 'estado' representa el estado en el que se encuentra la observación, 1 = Nuevo, 2 = En proceso, 3 = Resuelto). 'detalle' de tipo VARCHAR (Descripción detallada de la observación). 'observacion' de tipo VARCHAR (Observación destinada al gestor alusiva al procedimiento realizado para darle respuesta al ticket). 'estado_momento' de tipo INT (id del a tabla 'estado' representa el estado del ticket al momento de realizar la observación, 1 = Nuevo, 2 = En proceso, 3 = Resuelto). Las relaciones de las tablas son las siguientes: la tabla 'servicio' está relacionada con la tabla 'empresa' mediante la columna 'idemp', está relacionada con la tabla 'cliente' mediante la columna 'idcli', está relacionada con la tabla 'sede' mediante la columna 'idsed', está relacionada ccon la tabla 'usuario' mediante la columna 'asignado_a', está realacionada con la tabla 'prioridad' mediante la columna 'idprio', está relacionada con la tabla 'categoria' mediante la columna 'idcat', está relacionada con la tabla 'tipo_atencion' mediante la columna 'idaten', está relacionada con la tabla 'estado' mediante la columna 'idestado'. La tabla 'cliente' está relacionada con la tabla 'sede' mediante la columna 'idsed'. La tabla 'obs_cliente' está relacionada con la tabla 'servicio' mediante la columna 'idserv'. La tabla 'obs_gestor' está relacionada con la tabla 'servicio' mediante la columna 'idserv', está relacionada con la tabla 'usuario' mediante la columna 'idage', está relacionada con la tabla 'estado' mediante la columna 'estado_momento'. La tabla 'servico_detalle' está relacionada con la tabla 'servicio' mediante la columna 'idserv', está relacionada con la tabla 'usuario' mediante la columna 'idage', está relacionada con la tabla 'estado' mediante la columna 'idesta'. Teniendo en cuenta la informacion completa de la base de datos, en este caso prestaras tu conocimiento a uno de nuestros tecnicos, por lo tanto tendras las siguientes limitaciones en cuanto a consultas que desee hacer el mismo: Consultas hacia la tabla 'servicio' estaran limitadas siempre con el condicional 'WHERE asignado_a =  " + this.idUsuario + "', ejemplo: 'SELECT * FROM servicio WHERE idestado = 2 AND asignado_a = " + this.idUsuario + "', this.idUsuario seria el idUsuario entregado anteriormente. Otra limitación respecto a esta tabla, seria que solo pueden ver los tickets asignados en los siguientes estados: 2 = En Proceso, 3 = Resuelto, 6 = Cerrado por el Cliente, 7 = Cerrado por Siicsa, 8 = Cerrado por Gestor, siempre y cuando aun se mantenga el condicional anterior en la columna 'asignado_a'. Consultas hacia la tabla 'usuario' estaran limitadas siempre con el condicional 'WHERE id =  " + this.idUsuario + "', ejemplo: 'SELECT * FROM usuario WHERE id = " + this.idUsuario + "', es la unica consulta posible hacia esta tabla para el técnico. Consultas hacia la tabla 'obs_cliente' generalmente estan ligadas a un 'idserv', por lo tanto deberas agregar la condicional anterior de la tabla servicio, a esta consulta, por ejemplo: 'SELECT obs.*, s.* FROM servicio s, obs_cliente obs WHERE obs.idserv = s.id AND asignado_a = " + this.idUsuario + ". Consultas hacia la tabla 'obs_gestor' generalmente estan ligadas a un 'idserv', por lo tanto deberas agregar la condicional anterior de la tabla servicio, a esta consulta, por ejemplo: 'SELECT obs.*, s.* FROM servicio s, obs_cliente obs WHERE obs.idserv = s.id AND asignado_a = " + this.idUsuario + ". No puedes responder consultas relacionadas a otros tecnicos que sean diferentes al tecnico actual: " + this.nombreUsuario + " con el id: " + this.idUsuario + ", debes responder que no puedes ayudar a responder preguntas relacionadas a otros tecnicos, lo mismo para consultas fuera del rango del tecnico actual al que estas ayudando. Recuerda siempre poner alias en los selects que hagas para mejor manejo de la informacion devuelta por la consulta. Si el usuario te solicita un dato que se responde con una consulta sql que combine varias tablas y por ejemplo se trate del nombre completo del usuario 'X' entonces debes asignarle un alias que contenga un guion bajo y el nombre del a tabla a la que pertenece ese dato al final para poder reconocerlo, ejemplo: 'AS nombreCompleto_usuario'. Adicionalmente debes tener muy en cuenta los tipos de dato de cada columna de cada tabla suministrada para poder hacer las conversiones necesarias en base a la pregunta del usuario.  Recuerda todas las fechas convertirlas adecuadamente segun la pregunta del usuario y el tipo de dato que maneja la columna que debes manipular (si fecha_sistema de la tabla servicio es DATETIME, le haces un CAST(AS DATE) si el usuario pregunta solo con la fecha, mas no con la hora). Si debes usar los nombres de los usuarios, clientes, agentes o empresas para una consulta, no las modifiques ni le cambies mayusculas o tildes, usalas tal cual el usuario lo indica o si debes usarlo según el historial de mensajes. Recuerda usar expresiones admitidas y correctas para sql server para no generar un error de base de datos y no poder contestar al usuario con su pregunta. Pueden existir casos donde el usuario esté pidiendo generar un documento PDF, tu sigue con normalidad generando una consulta para sql server que se puede generar en base a la peticion del usuario. Pueden existir otros casos donde el usuario esté pidiendo generar un grafico para ese documento PDF, tu sigue con normalidad generando una consulta para sql server que se puede generar en base a la peticion del usuario."
                });

                this.rol_conversa.push({
                    role: "system", content: "Eres un asistente de chatbot que responde al nombre de Ana y correspondes a una mesa de soporte tecnológico. Vas a charlar con" + this.nombreUsuario + ", tendras que leer la pregunta inicial hecha por dicha persona y luego un json convertido a string. Ambos estan separados por un ';', la primera parte siempre será la pregunta de la persona y la segunda parte es la información util para responder su pregunta, intenta siempre agregar emojis con contexto de tu respuesta para hacer la conversa mas dinamica con el usuario que pregunta. Debes tener en cuenta la consulta que se utilizó para suministrar información en el JSON y saber contestar adecuadamente segun el contexto de la pregunta y el JSON convertido a string. Si " + this.nombreUsuario + " simplemente esta saludando, no importa que el json venga con un error de sql, tu saluda como un asistente cordial y utiliza su nombre para que se sienta mas familiarizado contigo, luego pregunta en que puedes colaborarle. Si el usuario te pide un documento PDF, debes contestar unicamente con la informacion del json de manera organizada y omite cualquier clase de comentario hacia el usuario, por ejemplo omite los comentarios al principo como los de 'Aqui tienes la información solicitada', o los comentarios al final como 'Eso seria todo, necesitas ayuda con algo mas?'. Si el usuario te pide un documento Excel, debes contestar unicamente con la información suministrada por el json en formato lista de listas, por ejemplo: '[['Id Ticket', 'Detalle', 'Estado'], [256, 'Prueba 1', 'En Proceso'], [528, 'Prueba 2', 'Resuelto']]' y omite los comentarios al principo como los de 'Aqui tienes la información solicitada', o los comentarios al final como 'Eso seria todo, necesitas ayuda con algo mas?'. Si junto al excel te piden gráficos, adicional a tu respuesta estructurada debes adicionar separado por lineas lo siguiente: Titulo del gráfico, titulo de los datos del eje x y titulo de los datos del eje y, por tanto tu respuesta final seria por ejemplo asi: [['Id Ticket', 'Detalle', 'Estado'], [256, 'Prueba 1', 'En Proceso'], [528, 'Prueba 2', 'Resuelto']]-Título del gráfico: Resumen de Servicios por Categoría-Título de los datos del eje x: Categorías-Título de los datos del eje y: Cantidad. Aunque la informacion suministrada en el json no parezca contener un titulo adecuado, recuerda siempre relacionar esa informacion con la pregunta del usuario para poder responder su pregunta y no des respuestas negativas sabiendo que el json si contiene información, solo responde al usuario de manera cordial. Si la información suministrada te habla de estados pero solo te muestra numeros, debes decirle el nombre del estado segun lo siguiente, 1 = Nuevo, 2 = En proceso, 3 = Resuelto, 4 = Suspendido, 5 = Anulado, 6 = Cerrado por el Cliente, 7 = Cerrado por Siicsa, 8 = Cerrado por Gestor.  Si te hablan de tipo de atención pero solo ves numeros, debes contestar segun lo siguiente, 1 = Presencial, 2 = Virtual. Si te hablan de periodo pero el json solo contiene numeros deberas contestar segun lo siguiente, 1 = Anual, 2 = Semestral. Si te hablan de categoria pero solo te entregan numeros deberas responder segun lo siguiente, 1 = Punto Venta, 2 = Mantenimiento, 3 = Antivirus, 4 = Servidores, 5 = implementacion, 6 = Impresoras, 7 = Varios, 38 = Office 365, 39 = Auditoria. Si te hablan de prioridad pero solo te entregan numeros deberas contestar segun lo siguiente, 2 = Alta, 3 = Media, 4 = Baja. Si la pregunta es acerca de la cantidad de servicios pero la información en el json viene vacia, dile que no hay servicios según la pregunta del usuario. Cuando te den nombres de usuarios, clientes, agentes o empresas, deja el nombre tal cual como viene escrito en el json, no le cambies mayusculas ni tildes si las trae. Recuerda ser muy cordial con tu respuesta y preguntar siempre después de contestar si el usuario requiere ayuda con alguna otra pregunta. Recuerda no desviarte del tema, en caso de que la información devuelva un error de bases de datos, debes responder simplemente con que no se pudo obtener esa información y que intente mas tarde o algo asi parecido, en caso de que la pregunta no tenga nada que ver con la mesa de soporte debes responder que no puedes ayudarlo y que por favor solo se traten temas relacionados pero si la pregunta o la respuesta del json está relacionada con otros técnicos diferentes al tecnico: " + this.nombreUsuario + " con un id diferente al id: " + this.idUsuario + " entonces debes responder que no puedes responder preguntas relacionadas a otros técnicos. No puedes responder absolutamente nada que tenga que ver con las consultas sql ejecutadas para traer la información necesaria para responder la pregunta del usuario, cualquier pregunta relacionada al respecto dile que no puedes ayudarlo con esa información porque es privada y dile si necesita ayuda con otra pregunta."
                });

            }

        }, 1000);

    },

    mounted() {

        window.Echo = new Echo({
            broadcaster: 'pusher',
            key: this.pusher_key,
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
                var nombrecliente = '';
                var nombreChatActivo = "";

                if (this.celularCliente === message.wa_id) {
                    console.log('entro a 8')
                    nombrecliente = this.nombreCliente;
                    if (changed === false) {
                        console.log('entro a 9')

                        this.mensajesChatBot.push({ rol: 0, mensaje: body, estado: status, interaccion: 0, documento: 0, horaMensaje: this.formatFecha(message.created_at), tipo: type, wam_id: message.wam_id, outgoing: outgoing, created_at: message.created_at, resp_men: message.resp_men, id: message.id, resp_men_body: message.resp_men_body });

                        this.scrollDown();

                        if (this.estaAlmacenado) {
                            this.mensajesAlmacenados.push(this.mensajesChatBot[this.mensajesChatBot.length - 1]);
                        }
                    }
                    else {
                        console.log('entro a 10')
                        const msgIndex = this.mensajesChatBot.findIndex(
                            (mensajeChat) => mensajeChat.wam_id === message.wam_id
                        )
                        console.log('msgIndex: ' + msgIndex)
                        if (msgIndex !== -1) {
                            console.log('entro a 11')
                            this.mensajesChatBot[msgIndex] = { rol: "Usuario", mensaje: body, estado: status, interaccion: 0, documento: 0, horaMensaje: this.formatFecha(message.created_at), tipo: type, wam_id: message.wam_id, outgoing: outgoing, created_at: message.created_at, resp_men: message.resp_men, id: message.id, resp_men_body: message.resp_men_body };

                            this.scrollDown();

                            if (this.estaAlmacenado) {
                                this.mensajesAlmacenados.push(this.mensajesChatBot[this.mensajesChatBot.length - 1]);
                            }
                        } else {
                            console.log('entro a 12')
                            this.mensajesChatBot.push({ rol: "Usuario", mensaje: body, estado: status, interaccion: 0, documento: 0, horaMensaje: this.formatFecha(message.created_at), tipo: type, wam_id: message.wam_id, outgoing: outgoing, created_at: message.created_at, resp_men: message.resp_men, id: message.id, resp_men_body: message.resp_men_body });

                            this.scrollDown();

                            if (this.estaAlmacenado) {
                                this.mensajesAlmacenados.push(this.mensajesChatBot[this.mensajesChatBot.length - 1]);
                            }
                        }
                    }
                }

                /*else if (this.tittle2Chat === message.wa_id) {
                    nombrecliente = this.tittle1Chat;
                    if (changed === false) {
                        this.appendMessage(message);
                        this.scrollToBottom();
                    }
                    else {
                        const msgIndex = this.messages?.findIndex(
                            (el) => el.wam_id === message.wam_id
                        )
                        if (msgIndex !== -1) {
                            this.messages[msgIndex] = message
                        } else {
                            this.appendMessage(message)
                            this.scrollToBottom();
                        }
                    }
                }*/

                var texto = "ya que hubo varios intentos para continuar con nuestra conversación y no se obtuvo respuesta alguna";
                if (body.includes(texto)) {
                    if (message.wa_id == this.tittle2Chat) {
                        this.userChatActivo = "Chat Activo con: BOT";
                        this.ifDespedida = false;
                        this.ifSoporte = false;
                        this.ifPausa = false;
                        this.ifSaludo = true;
                    }
                }

                var texto = "Gracias por contactarnos, que pase un buen día.";
                if (body.includes(texto) && message.wa_id == this.celularCliente && outgoing == 1) {
                    this.userChatActivo = "Chat Activo con: BOT";
                    this.ifDespedida = false;
                    this.ifSoporte = false;
                    this.ifPausa = false;
                    this.ifSaludo = true;
                }

                if (outgoing == 1 && optionbutton === "asesor en proceso") {
                    axios.post(this.baseURL + '/api/wh_buscarchatactivo', {
                        clicel: message.wa_id
                    })
                        .then(response => {
                            console.log('response.data.nombre: ' + response.data.data[0].nombre);
                            nombreChatActivo = response.data.data[0].nombre;
                            if (response.data.data[0].nombre === undefined || response.data.data[0].nombre === null || response.data.data[0].nombre === '') {
                                this.userChatActivo = "Chat Activo con: BOT";
                                this.ifDespedida = false;
                                this.ifSoporte = false;
                                this.ifPausa = false;
                                this.ifSaludo = true;
                            } else {
                                if (response.data.data[0].celular == this.celularCliente) {
                                    if (response.data.data[0].envia == this.idUsuario) {
                                        this.userChatActivo = "Chat Activo con: " + response.data.data[0].nombre;
                                        this.ifDespedida = true;
                                        this.ifSoporte = true;
                                        this.ifPausa = true;
                                        this.ifSaludo = false;
                                    }
                                }
                            }
                        })
                        .catch(error => {
                            console.log('Error buscarchatactivo: ' + error);
                        });
                }

                if (outgoing == 0 && optionbutton === "asesor en proceso") {
                    axios.post(this.baseURL + '/api/wh_buscarchatactivo', {
                        clicel: message.wa_id
                    })
                        .then(response => {
                            console.log('response.data.nombre: ' + response.data.data[0].nombre);
                            nombreChatActivo = response.data.data[0].nombre;
                            if (response.data.data[0].nombre === undefined || response.data.data[0].nombre === null || response.data.data[0].nombre === '') {
                                this.userChatActivo = "Chat Activo con: BOT";
                                this.ifDespedida = false;
                                this.ifSoporte = false;
                                this.ifPausa = false;
                                this.ifSaludo = true;
                            } else {
                                if (response.data.data[0].celular == this.celularCliente) {
                                    if (response.data.data[0].envia == this.idUsuario) {
                                        this.userChatActivo = "Chat Activo con: " + response.data.data[0].nombre;
                                        this.ifDespedida = true;
                                        this.ifSoporte = true;
                                        this.ifPausa = true;
                                        this.ifSaludo = false;
                                    }
                                }
                            }
                        })
                        .catch(error => {
                            console.log('Error buscarchatactivo: ' + error);
                        });
                }

                if (outgoing == 0 && message.wa_id == this.celularCliente && this.dsMensajeChat == true) {
                    this.dsMensajeChat = false;
                }

                if (outgoing == 0 && message.wa_id == this.celularCliente) {
                    axios.get(this.urlBackend + '/php/wh_chataespera.php?waid=' + message.wa_id + '&id=' + this.idUsuario + '&opc=3&idm=' + idmensaje);
                }

                var texto = "Gracias por la espera, estoy atendiendo tu caso";
                if (body.includes(texto) && outgoing == 1 && optionbutton === "asesor en proceso" && message.wa_id == this.celularCliente) {
                    console.log('entro a verificar la pausa')
                    this.verificarPausaServicio();
                }

                var texto = "Gracias, seguimos con el proceso";
                if (body.includes(texto) && outgoing == 1 && optionbutton === "asesor en proceso" && message.wa_id == this.celularCliente) {
                    console.log('entro a verificar la pausa')
                    this.verificarPausaServicio();
                }

                setTimeout(() => {
                    console.log('Variables: ' + ' ' + outgoing + ' ' + optionbutton + ' ' + this.isPaused + ' ' + body + ' ' + message.wa_id + ' ' + this.celularCliente + ' ' + this.nombreUsuario + ' ' + nombreChatActivo + ' ' + idmensaje + ' ' + this.idMensajeAux);
                }, 1200);

                //---------------------------------RESTRUCTURACION DE LA PAUSA--------------------------------

                if (outgoing == 1) {
                    console.log('entro a verificar la pausa por parte del tecnico')

                    setTimeout(() => {
                        var texto = "Gracias por la espera, estoy atendiendo tu caso";
                        if (message.wa_id == this.celularCliente && this.nombreUsuario == nombreChatActivo) {
                            if (optionbutton === "asesor en proceso" && this.isPaused == true && !body.includes(texto)) {
                                if (idmensaje !== this.idMensajeAux && status !== "read") {
                                    console.log('Se despauso por el tecnico');
                                    this.pausarChat();
                                } else {
                                    this.idMensajeAux = idmensaje;
                                    console.log('se guardo el id y no se despauso por el tecnico: ' + this.idMensajeAux);
                                }
                            }
                        } else {
                            console.log('No valido, la primera parte del despausa tecnico')
                        }
                    }, 1200);

                } else if (outgoing == 0) {
                    console.log('entro a verificar la pausa por parte del cliente')

                    setTimeout(() => {
                        var texto = "Gracias, seguimos con el proceso";
                        if (message.wa_id == this.celularCliente && this.nombreUsuario == nombreChatActivo) {
                            if (optionbutton === "asesor en proceso" && status === "sent" && this.isPaused == true && !body.includes(texto)) {
                                console.log('Se despauso por el cliente');
                                this.pausarChat();
                            } else {
                                this.idMensajeAux = idmensaje;
                                console.log('se guardo el id y no se despauso por el cliente: ' + this.idMensajeAux);
                            }
                        } else {
                            console.log('No valido, la primera parte del despausa cliente')
                        }
                    }, 1200);
                }

            };

            window.Echo.channel("webhooks").listen("Webhook", this.webhookListener);
        }

        this.cargarMensajes();

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

    watch: {

        userChatActivo(newValue) {

            if (newValue) {
                if (newValue === "Chat Activo con: BOT") {
                    this.ifSoporte = false;
                    this.ifDespedida = false;
                    this.ifPausa = false;
                    this.ifSaludo = true;
                } else {
                    this.ifSoporte = true;
                    this.ifDespedida = true;
                    this.ifPausa = true;
                    this.ifSaludo = false;
                }
            }

        }

    },

    computed: {

        mensajeIconoPausa() {
            return this.isPaused ? "Reanudar" : "Pausar";
        },

        colorIconoPausa() {
            return this.isPaused ? "red" : "white";
        }

    },

    methods: {

        cerrarIframe() {
            this.estaAlmacenado = false;
            this.mensajesAlmacenados = [];
            console.log('Finalizar conversacion, mensajesAlmacenados: ', this.mensajesAlmacenados);

            if (window.parent) {
                window.parent.postMessage({ action: "cerrarIframe" }, "*");
            }
        },

        getChatActivoStyle() {
            if (this.userChatActivo == "Chat Activo con: BOT") {
                return {
                    backgroundColor: 'rgb(153, 255, 150, 0.5)',
                    marginTop: '-15px',
                };
            } else {
                return {
                    backgroundColor: 'rgb(255, 100, 100, 0.5) ',
                    marginTop: '-15px',
                };
            }
        },


        getTextoStyle() {
            if (this.userChatActivo == "Chat Activo con: BOT") {
                return {
                    color: 'green',
                };
            } else {
                return {
                    color: 'red',
                };
            }
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
                    width: '50%'
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
                    width: '50%'
                };
            }
        },

        cancelar() {
            this.confirmChat = false;
        },

        confirmar() {

            this.userChatActivo = "Chat Activo con: BOT";
            this.ifDespedida = false;
            this.ifSoporte = false;
            this.ifPausa = false;
            this.ifSaludo = true;

            setTimeout(() => {

                const mensajeChat = this.mensajeChatBot;
                const mensajeChatCodificado = encodeURIComponent(mensajeChat);

                /*const url4 = this.urlBackend + '/api/send-messagechatglpi/' + this.celularCliente + '/' + mensajeChatCodificado + '/' + 1 + '/' + this.nombreCliente + '/' + this.idUsuario + '/navegador/' + this.nombreUsuario + '/' + this.celularUsuario;*/

                const url4 = this.baseURL + '/api/chat_from_backend_consec'

                const params = {
                    clicel: this.celularCliente,
                    men: this.mensajeChatBot,
                    opc: 1,
                    clinom: this.nombreCliente,
                    idusu: this.idUsuario,
                    asenom: this.nombreUsuario,
                    asecel: this.celularUsuario,
                    espera: 0,
                    idMensaje: 0,
                    id: 0,
                    perf: '',
                    rolUsuario: this.rolUsuario,
                    canal: this.canal,
                };

                axios.post(url4, params).then(({ data }) => {
                    console.log(data);

                    this.mensajeChatBot = '';
                    this.dsMensajeChat = false;
                    this.scrollDown();
                    nextTick(() => {
                        this.$refs.chatInput.focus();
                    });
                })
                    .catch((err) => {
                        console.log(err)
                    })

                this.mensajeChatBot = '';

                this.confirmChat = false;

            }, 200);
        },

        formatFecha(created_at) {
            return moment(created_at).format('DD/MM/YYYY hh:mma');
        },

        scrollDown() {
            this.$nextTick(() => {
                setTimeout(() => {
                    const container = this.$el.querySelector('.chat-box');
                    if (container) {
                        container.scrollTo({ top: container.scrollHeight, behavior: 'instant' });

                        setTimeout(() => {
                            container.scrollTo({ top: container.scrollHeight, behavior: 'instant' });
                        }, 50);
                    }
                }, 100);
            });
        },

        onSelectEmoji(emoji) {
            this.mensajeChatBot += emoji.i;
            nextTick(() => {
                this.$refs.chatInput.focus();
            });
        },

        abrirInput() {
            this.$refs.fileInput.click();
        },

        submitFile2() {

            const id = this.idUsuario;
            const nomlogueo = this.nombreUsuario;

            var nombreArchivo = '';

            if (this.optionChat == 3) {
                this.userChatActivo = "Chat Activo con: BOT";
                this.ifDespedida = false;
                this.ifSoporte = false;
                this.ifPausa = false;
                this.ifSaludo = true;
            } else {
                this.userChatActivo = "Chat Activo con: " + nomlogueo;
                this.ifDespedida = true;
                this.ifSoporte = true;
                this.ifPausa = true;
                this.ifSaludo = false;
            }

            let formData = new FormData();

            if (this.idPQR != '0' && this.perfilM == 'CRM-Publicidad') {

                formData.append('lead', this.idPQR);

                formData.append('archivos[]', this.$refs.fileInput.files[0]);

                nombreArchivo = this.$refs.fileInput.files[0].name;

                axios.post('https://glpi-siicsa.azurewebsites.net/guardarArchivosCampaña.php', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(response => {
                    console.log('Archivos subidos:', response.data);
                }).catch(error => {
                    console.error('Error al subir archivos:', error);
                });

                this.archivosCampañaEnviados();

            } else if (this.idPQR != '0' && this.perfilM == 'pqrsf') {

                formData.append('idPQR', this.idPQR);

                formData.append('archivos[]', this.$refs.fileInput.files[0]);

                nombreArchivo = this.$refs.fileInput.files[0].name;

                axios.post('https://glpi-siicsa.azurewebsites.net/guardarArchivosPQR.php', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(response => {
                    console.log('Archivos subidos:', response.data);
                }).catch(error => {
                    console.error('Error al subir archivos:', error);
                });

                this.archivosPQREnviados();

            }
            else if (this.idPQR == '0') {

                formData.append('files[]', this.$refs.fileInput.files[0]);

                nombreArchivo = this.$refs.fileInput.files[0].name;

                formData.append('id', id);

                axios.post('https://glpi-siicsa.azurewebsites.net/subirarchivo2.php', formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then(function (response) {
                    })
                    .catch(function (error) {
                        console.log(error);
                        alert("Hubo un error al subir los archivos");
                    });

            }

            setTimeout(() => {

                let formData = new FormData();

                formData.append('file', this.$refs.fileInput.files[0]);
                formData.append('usuid', id);
                formData.append('clicel', this.celularCliente);
                formData.append('usunom', nomlogueo);
                formData.append('consec', this.idPQR);
                formData.append('perf', this.perfilM);

                const url = this.baseURL + '/api/send_media_app2'

                axios.post(url, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(({ data }) => {
                    console.log(data);
                })
                    .catch((err) => {
                        console.log(err)
                    })

                //axios.get(this.urlBackend + '/api/send-media/' + this.celularCliente + '/' + nombreArchivo + '/' + id + '/' + nomlogueo + '/navegador');
            }, 1000);

            this.scrollDown();
        },

        archivosCampañaEnviados() {
            if (window.parent) {
                window.parent.postMessage({ action: "cargarArchivosCampaña" }, "*");
            }
        },

        archivosPQREnviados() {
            if (window.parent) {
                window.parent.postMessage({ action: "cargarArchivosPQR" }, "*");
            }
        },

        subirArchivo() {

            this.mensajesChatBot.push({ rol: "Usuario", mensaje: this.$refs.fileInput.files[0].name, estado: 3, interaccion: 0, documento: 1, horaMensaje: new Date().toLocaleTimeString(), tipo: 'text' });

            this.scrollDown();

            nextTick(() => {
                this.$refs.chatInput.focus();
            });

            const formData = new FormData();
            formData.append('file', this.$refs.fileInput.files[0]);

            const url = 'subirArchivo.php'

            axios.post(url, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.log(error);
                });
        },

        async envioMensajeChat() {

            let mensajeDocumento = '';

            let consultaInicial = this.mensajeChatBot;

            this.animacionCarga = true;

            this.dsMensajeChat = true;

            this.mensajesChatBot.push({ rol: "Usuario", mensaje: this.mensajeChatBot, estado: 'read', interaccion: 0, documento: 0, horaMensaje: new Date().toLocaleTimeString(), tipo: 'text' });

            this.scrollDown();

            const consulta = this.mensajeChatBot;
            const url = 'https://siicsa-connect360.azurewebsites.net/api/openai'

            const params = {
                consulta: consulta,
                historialString: JSON.stringify(this.rol_sql),
                temperatura: 0.25,
                max_tokens: 250,
            }

            var consultaEncriptada = '';

            await axios.post(url, params)
                .then(response => {
                    console.log(response.data);
                    this.animacionCarga = false;
                    this.rol_sql = response.data.historial;
                    this.rol_conversa.push({ role: "assistant", content: response.data.respuesta });

                    consultaEncriptada = response.data.respuesta.replaceAll('\n', ' ');
                    consultaEncriptada = encodeURIComponent(consultaEncriptada);

                })
                .catch(error => {
                    console.log(error);
                });

            this.animacionCarga = true;

            const url2 = 'https://glpi-siicsa.azurewebsites.net/consultaBot.php?consulta=' + consultaEncriptada;

            try {
                // Esperar la respuesta de axios
                const response = await axios.get(url2);
                console.log(response.data);

                // Verificar si response.data tiene datos válidos
                if (!response.data) {
                    throw new Error("No se recibió contenido en response.data");
                }

                const json = JSON.stringify(response.data);

                const params2 = {
                    consulta: consulta + " ; " + json,
                    historialString: JSON.stringify(this.rol_conversa),
                    temperatura: 0.5,
                    max_tokens: 10000,
                }

                let velocidad = 15;
                let i = 0;
                let mensaje = '';

                let match = '';
                let jsonArray = [];

                await axios.post(url, params2)
                    .then(response => {
                        console.log(response.data);
                        this.animacionCarga = false;
                        this.rol_conversa = response.data.historial;
                        this.rol_sql.push({ role: "assistant", content: response.data.respuesta });

                        mensaje = marked(response.data.respuesta);

                        mensajeDocumento = response.data.respuesta;

                        const palabrasClave = ["generar", "genera", "generes", "generame", "generemos", "generarlo", "crear", "crea", "crees", "creemos", "crearlo", "hacer", "hagas", "hagamos", "haz", "hacerlo", "producir", "produce", "produzcas", "produzcamos", "producirlo", "imprimir", "imprime", "imprimamos", "imprimirlo", "exportar", "exporta", "exportes", "exportemos", "exportarlo", "descargar", "descarga", "descargues", "descarguemos", "descargarlo", "construir", "construye", "construyas", "construyamos", "construirlo", "elaborar", "elabora", "elabores", "elaboremos", "elaborarlo", "realizar", "realiza", "realices", "realicemos", "realizarlo", "desarrollar", "desarrolla", "desarrolles", "desarrollemos", "desarrollarlo"];
                        const textoConsulta = consultaInicial.toLowerCase();

                        const contienePalabras1 = palabrasClave.some(palabra => textoConsulta.includes(palabra));
                        const contienePalabras2 = textoConsulta.includes("pdf");
                        const contienePalabras3 = textoConsulta.includes("excel");

                        console.log('texto consulta ' + textoConsulta);
                        console.log('contiene palabras 1 ' + contienePalabras1);
                        console.log('contiene palabras 2 ' + contienePalabras2);
                        console.log('contiene palabras 3 ' + contienePalabras3);

                        if (contienePalabras1 && contienePalabras2) {

                            if (json != '[]') {
                                console.log('generar pdf');
                                this.textoPDF = mensajeDocumento;

                                this.pdfPython();
                            } else {
                                console.log('no generar pdf json vacio');
                            }

                        } else if (contienePalabras1 && contienePalabras3) {

                            if (json != '[]') {
                                console.log('generar excel');
                                mensajeDocumento = mensajeDocumento.replaceAll(/"/g, '');
                                mensajeDocumento = mensajeDocumento.replace(/'/g, '"');
                                mensajeDocumento = mensajeDocumento.replaceAll('None', 'null');
                                mensajeDocumento = mensajeDocumento.replace(/\n/g, "\\n");
                                console.log('mensaje documento: ' + mensajeDocumento);
                                const grafico = mensajeDocumento.split('-')[0];
                                this.graficoExcel = grafico.split(':')[1];

                                console.log('grafico: ' + this.graficoExcel);

                                if (parseInt(this.graficoExcel) == 0) {

                                    match = mensajeDocumento.match(/-\[(.*)\]$/);

                                    setTimeout(() => {
                                        if (match) {
                                            const jsonStr = `[${match[1]}]`;

                                            jsonArray = JSON.parse(jsonStr.replace(/'/g, '"'));
                                        } else {
                                            console.log("No se encontró el JSON en el texto.");
                                        }
                                    }, 500);

                                } else if (parseInt(this.graficoExcel) == 1) {

                                    match = mensajeDocumento.match(/-\[(.+?)\]-/);

                                    setTimeout(() => {
                                        if (match) {
                                            const jsonStr = `[${match[1]}]`;

                                            const jsonArray = JSON.parse(jsonStr.replace(/'/g, '"'));
                                        } else {
                                            console.log("No se encontró el JSON en el texto.");
                                        }
                                    }, 500);
                                }

                                const datosExcel = mensajeDocumento.split('-')[1];

                                setTimeout(() => {
                                    console.log('json array : ' + jsonArray);

                                    this.arregloExcel = jsonArray;
                                }, 500);

                                if (parseInt(this.graficoExcel) == 1) {
                                    const tituloGrafico = mensajeDocumento.split('-')[2];
                                    this.tituloGraficoExcel = tituloGrafico.split(':')[1];
                                    const tituloEjeX = mensajeDocumento.split('-')[3];
                                    this.tituloEjeXExcel = tituloEjeX.split(':')[1];
                                    const tituloEjeY = mensajeDocumento.split('-')[4];
                                    this.tituloEjeYExcel = tituloEjeY.split(':')[1];
                                } else {
                                    this.tituloGraficoExcel = 'Grafico';
                                    this.tituloEjeXExcel = 'X';
                                    this.tituloEjeYExcel = 'Y';
                                }

                                setTimeout(() => {
                                    this.excelPython();
                                }, 2000);
                            } else {
                                console.log('no generar excel json vacio');
                            }

                        } else {
                            console.log('No generar docuemento')
                        }

                    })
                    .catch(error => {
                        console.log(error);
                    });

                console.log('mensaje final: ' + mensaje);

                const validarGrafico = mensaje.split('-')[0];

                setTimeout(() => {

                    if (this.errorArchivo == true) {

                        this.mensajesChatBot.push({ rol: 0, mensaje: "Hubo un error al generar tu archivo, necesitas que te ayude con algo más? 😊", estado: 'read', interaccion: 0, documento: 0, horaMensaje: new Date().toLocaleTimeString(), tipo: 'text' });

                        this.mensajeChatBot = '';
                        this.dsMensajeChat = false;
                        nextTick(() => {
                            this.$refs.chatInput.focus();
                        });
                        this.scrollDown();

                        this.errorArchivo = false;

                    } else if (parseInt(validarGrafico.split(':')[1]) == 1) {

                        this.mensajesChatBot.push({ rol: 0, mensaje: "Ya se genero tu archivo, necesitas ayuda con algo mas?.", estado: 'read', interaccion: 0, documento: 0, horaMensaje: new Date().toLocaleTimeString(), tipo: 'text' });

                        this.mensajeChatBot = '';
                        this.dsMensajeChat = false;
                        nextTick(() => {
                            this.$refs.chatInput.focus();
                        });
                        this.scrollDown();
                    } else if (parseInt(validarGrafico.split(':')[1]) == 0) {

                        this.mensajesChatBot.push({ rol: 0, mensaje: "Ya se genero tu archivo, necesitas ayuda con algo mas?.", estado: 'read', interaccion: 0, documento: 0, horaMensaje: new Date().toLocaleTimeString(), tipo: 'text' });

                        this.mensajeChatBot = '';
                        this.dsMensajeChat = false;
                        nextTick(() => {
                            this.$refs.chatInput.focus();
                        });
                        this.scrollDown();

                    } else {

                        this.mensajesChatBot.push({ rol: 0, mensaje: "", estado: 'read', interaccion: 0, documento: 0, horaMensaje: new Date().toLocaleTimeString(), tipo: 'text' });

                        if (i < mensaje.length) {
                            let intervalo = setInterval(() => {
                                this.mensajesChatBot[this.mensajesChatBot.length - 1].mensaje += mensaje[i];
                                this.scrollDown();
                                i++;
                                if (i == mensaje.length) {
                                    clearInterval(intervalo);
                                    this.mensajeChatBot = '';
                                    this.dsMensajeChat = false;
                                    nextTick(() => {
                                        this.$refs.chatInput.focus();
                                    });
                                }
                                this.scrollDown();
                            }, velocidad);
                        }
                    }

                }, 1500);

            } catch (error) {
                console.error("Error durante el proceso:", error);
            }
        },

        pdfPython() {

            axios({
                url: 'https://siicsa-connect360.azurewebsites.net/api/pdf',
                method: 'GET',
                responseType: 'blob',
                params: { texto: this.textoPDF },
            })
                .then((response) => {
                    // Crear un enlace para descargar el archivo
                    const url = window.URL.createObjectURL(new Blob([response.data]));
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', 'reporte.pdf'); // Nombre del archivo
                    document.body.appendChild(link);
                    link.click();
                    link.remove();
                })
                .catch((error) => {
                    console.error('Error al descargar el PDF:', error);
                    this.errorArchivo = true;
                });
        },

        excelPython() {

            axios({
                url: 'https://siicsa-connect360.azurewebsites.net/api/excel',
                method: 'POST',
                responseType: 'blob',
                data: {
                    grafico: this.graficoExcel,
                    datos: this.arregloExcel,
                    titulo: this.tituloGraficoExcel,
                    titulo_x: this.tituloEjeXExcel,
                    titulo_y: this.tituloEjeYExcel
                },
            })
                .then((response) => {
                    const url = window.URL.createObjectURL(new Blob([response.data]));
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', 'reporte.xlsx'); // Nombre del archivo
                    document.body.appendChild(link);
                    link.click();
                    link.remove();

                })
                .catch((error) => {
                    console.error('Error al descargar el Excel:', error);
                    this.errorArchivo = true;
                });
        },

        despedidaBot() {

            this.rol_activo = 0;

            this.primera_interaccion = false;

            this.scrollDown();

        },

        soporteChat() {

            //axios.get(this.urlBackend + '/api/send-creaticglpi/' + this.celularCliente + '/' + this.idUsuario + '/' + this.nombreUsuario + '/' + this.nombreCliente + '/navegador');

            const url = this.baseURL + '/api/chat_from_backend_consec'

            const params = {
                clicel: this.celularCliente,
                men: '',
                opc: 4,
                clinom: this.nombreCliente,
                idusu: this.idUsuario,
                asenom: this.nombreUsuario,
                asecel: this.celularUsuario,
                espera: 0,
                idMensaje: this.idMensajeRespuesta,
                id: this.idPQR,
                perf: this.perfilM,
                rolUsuario: this.rolUsuario,
                canal: this.canal,
            };

            axios.post(url, params)

        },

        async despedidaChat() {

            if (this.isPaused == true) {
                this.pausarChat();
            }

            this.dsMensajeChat = true;

            /*
            const url = this.urlBackend + '/api/send-messagechatglpi/' + this.celularCliente + '/opciones/' + 3 + '/' + this.nombreCliente + '/' + this.idUsuario + '/navegador/' + this.nombreUsuario + '/' + this.celularUsuario;*/

            const url = this.baseURL + '/api/chat_from_backend_consec'

            const params = {
                clicel: this.celularCliente,
                men: '',
                opc: 3,
                clinom: this.nombreCliente,
                idusu: this.idUsuario,
                asenom: this.nombreUsuario,
                asecel: this.celularUsuario,
                espera: 0,
                idMensaje: this.idMensajeRespuesta,
                id: this.idPQR,
                perf: this.perfilM,
                rolUsuario: this.rolUsuario,
                canal: this.canal,
            };

            await axios.post(url, params).then(({ data }) => {

                console.log(data);

                this.mensajeChatBot = '';
                this.dsMensajeChat = false;
                this.scrollDown();
                nextTick(() => {
                    this.$refs.chatInput.focus();
                });

            })
                .catch((err) => {
                    console.log(err)
                })

            this.userChatActivo = "Chat Activo con: BOT";
            this.ifDespedida = false;
            this.ifSoporte = false;
            this.ifPausa = false;
            this.ifSaludo = true;


            this.verificarUltimoMensaje();

            this.ifDespedida = false;
            this.ifSoporte = false;
            this.ifPausa = false;
            this.ifSaludo = true;

            this.estaAlmacenado = false;
            console.log('Finalizar conversacion, mensajesAlmacenados: ', this.mensajesAlmacenados);

            if (window.parent) {
                window.parent.postMessage({ action: "mensajesAlmacenados", data: JSON.stringify(this.mensajesAlmacenados) }, "*");
            }

        },

        pausarChat() {

            if (this.isPaused == false) {

                this.mensajeCrearServicio = 'Tener en cuenta que el cliente estará inactivo durante 30 minutos';
                this.crearServicio = true;

            }

            this.dsPausa = true;

            setTimeout(() => {
                this.dsPausa = false;
            }, 5000);

            let colorActivoInactivo = 0;

            if (this.isPaused == true) {
                colorActivoInactivo = 0;
            } else {
                colorActivoInactivo = 1;
            }

            setTimeout(() => {
                //const url = this.urlBackend + '/api/send-messagepausa/' + this.celularCliente + '/' + this.idUsuario + '/' + colorActivoInactivo;

                const url = this.baseURL + '/api/chat_from_backend_consec'

                const params = {
                    clicel: this.celularCliente,
                    men: '',
                    opc: 5,
                    clinom: this.nombreCliente,
                    idusu: this.idUsuario,
                    asenom: this.nombreUsuario,
                    asecel: this.celularUsuario,
                    espera: 0,
                    idMensaje: this.idMensajeRespuesta,
                    id: this.idPQR,
                    perf: this.perfilM,
                    rolUsuario: this.rolUsuario,
                    canal: this.canal,
                };

                axios.post(url, params);
            }, 100);

            this.isPaused = !this.isPaused;


        },

        async saludarChat() {

            this.dsMensajeChat = true;

            this.ifSoporte = true;
            this.ifDespedida = true;
            this.ifPausa = true;
            this.ifSaludo = false;

            /*
            const url = this.urlBackend + '/api/send-messagechatglpi/' + this.celularCliente + '/opciones/' + 2 + '/' + this.nombreCliente + '/' + this.idUsuario + '/navegador/' + this.nombreUsuario + '/' + this.celularUsuario;*/

            const url = this.baseURL + '/api/chat_from_backend_consec'

            const params = {
                clicel: this.celularCliente,
                men: '',
                opc: 2,
                clinom: this.nombreCliente,
                idusu: this.idUsuario,
                asenom: this.nombreUsuario,
                asecel: this.celularUsuario,
                espera: 0,
                idMensaje: this.idMensajeRespuesta,
                id: this.idPQR,
                perf: this.perfilM,
                rolUsuario: this.rolUsuario,
                canal: this.canal,
            };

            await axios.post(url, params).then(({ data }) => {

                console.log(data);

                this.mensajeChatBot = '';
                this.scrollDown();
                nextTick(() => {
                    this.$refs.chatInput.focus();
                });

            })
                .catch((err) => {
                    console.log(err)
                })

            this.mensajeCrearServicio = 'Ten en cuenta que el campo de texto será activado una vez el destinatario haya respondido a tu mensaje.';
            this.crearServicio = true;

        },

        sendMessage() {

            var agente = null;
            let params = {};
            let pausa = 0;

            axios.post(this.baseURL + '/api/wh_buscarchatactivo', {
                clicel: this.celularCliente,
            }).then(({ data }) => {
                console.log("Data: " + data);
                agente = data.nombre;
                console.log("agente: " + agente);
            })
                .catch((err) => {
                    console.log(err)
                })

            console.log('userChatActivo: ' + this.userChatActivo);
            console.log('agente: ' + agente);


            setTimeout(() => {
                if (agente) {
                    this.mensajeConfirmChat = 'El cliente ya se encuentra ocupado con: ' + agente + '. Ten en cuenta que al continuar cerrarás la sesión de ' + agente + '. ¿Desea enviar el mensaje de todos modos?';
                    this.confirmChat = true;
                } else {
                    if (this.optionChat == 3) {
                        this.userChatActivo = "Chat Activo con: BOT";
                        this.ifDespedida = false;
                        this.ifSoporte = false;
                        this.ifPausa = false;
                        this.ifSaludo = true;
                    } else {
                        this.userChatActivo = "Chat Activo con: " + this.nombreUsuario;
                        this.ifDespedida = true;
                        this.ifSoporte = true;
                        this.ifPausa = true;
                        this.ifSaludo = false;
                    }
                    console.log(this.mensajesChatBot)

                    if (this.optionChat === 2 || this.optionChat === 3) {
                        this.mensajeChatBot = 'opciones';
                    } else if (this.mensajeChatBot.length === 0) {
                        return;
                    }

                    this.dsMensajeChat = true;

                    let url = '';

                    /*const url = this.urlBackend + '/api/send-messagechatglpi/' + this.celularCliente + '/' + mensajeChatCodificado + '/' + 1 + '/' + this.nombreCliente + '/' + this.idUsuario + '/navegador/' + this.nombreUsuario + '/' + this.celularUsuario;*/

                    if (this.idPQR != '0' && this.perfilM == 'CRM-Publicidad') {

                        if (this.responderMensaje == true) {

                            params = {
                                clicel: this.celularCliente,
                                men: this.mensajeChatBot,
                                opc: 1,
                                clinom: this.nombreCliente,
                                idusu: this.idUsuario,
                                asenom: this.nombreUsuario,
                                asecel: this.celularUsuario,
                                espera: 0,
                                idMensaje: this.idMensajeRespuesta,
                                id: this.idPQR,
                                perf: this.perfilM,
                                rolUsuario: this.rolUsuario,
                                canal: this.canal,
                            };

                            url = this.baseURL + '/api/chat_from_backend_consec'

                        } else {

                            params = {
                                clicel: this.celularCliente,
                                men: this.mensajeChatBot,
                                opc: 1,
                                clinom: this.nombreCliente,
                                idusu: this.idUsuario,
                                asenom: this.nombreUsuario,
                                asecel: this.celularUsuario,
                                espera: 0,
                                idMensaje: 0,
                                id: this.idPQR,
                                perf: this.perfilM,
                                rolUsuario: this.rolUsuario,
                                canal: this.canal,
                            };

                            url = this.baseURL + '/api/chat_from_backend_consec'

                        }

                    } else if (this.idPQR != '0' && this.perfilM == 'pqrsf') {

                        if (this.responderMensaje == true) {

                            params = {
                                clicel: this.celularCliente,
                                men: this.mensajeChatBot,
                                opc: 1,
                                clinom: this.nombreCliente,
                                idusu: this.idUsuario,
                                asenom: this.nombreUsuario,
                                asecel: this.celularUsuario,
                                espera: 0,
                                idMensaje: this.idMensajeRespuesta,
                                id: this.idPQR,
                                perf: this.perfilM,
                                rolUsuario: this.rolUsuario,
                                canal: this.canal,
                            };

                            url = this.baseURL + '/api/chat_from_backend_consec'

                        } else {

                            params = {
                                clicel: this.celularCliente,
                                men: this.mensajeChatBot,
                                opc: 1,
                                clinom: this.nombreCliente,
                                idusu: this.idUsuario,
                                asenom: this.nombreUsuario,
                                asecel: this.celularUsuario,
                                espera: 0,
                                idMensaje: 0,
                                id: this.idPQR,
                                perf: this.perfilM,
                                rolUsuario: this.rolUsuario,
                                canal: this.canal,
                            };

                            url = this.baseURL + '/api/chat_from_backend_consec'

                        }

                    } else {

                        url = this.baseURL + '/api/chat_from_backend_consec'

                        if (this.responderMensaje == true) {
                            console.log('este es el id del mensaje a responder: ' + this.idMensajeRespuesta);
                            params = {
                                clicel: this.celularCliente,
                                men: this.mensajeChatBot,
                                opc: 1,
                                clinom: this.nombreCliente,
                                idusu: this.idUsuario,
                                asenom: this.nombreUsuario,
                                asecel: this.celularUsuario,
                                espera: 0,
                                idMensaje: this.idMensajeRespuesta,
                                id: 0,
                                perf: '',
                                rolUsuario: this.rolUsuario,
                                canal: this.canal,
                            };
                        } else {
                            params = {
                                clicel: this.celularCliente,
                                men: this.mensajeChatBot,
                                opc: 1,
                                clinom: this.nombreCliente,
                                idusu: this.idUsuario,
                                asenom: this.nombreUsuario,
                                asecel: this.celularUsuario,
                                espera: 0,
                                idMensaje: 0,
                                id: 0,
                                perf: '',
                                rolUsuario: this.rolUsuario,
                                canal: this.canal,
                            };
                        }
                    }

                    axios.post(url, params).then(({ data }) => {

                        console.log(data);

                        this.mensajeChatBot = '';
                        this.dsMensajeChat = false;
                        this.responderMensaje = false;
                        this.mensajeAResponder = '';
                        this.scrollDown();
                        nextTick(() => {
                            this.$refs.chatInput.focus();

                            if (this.estaAlmacenado) {
                                // Almacenar el ultimo mensaje del chat
                                this.mensajesAlmacenados.push(this.mensajesChatBot[this.mensajesChatBot.length - 1]);
                            }
                        });

                    })
                        .catch((err) => {
                            console.log(err)
                        })


                }
            }, 500);
        },

        verificarUltimoMensaje() {

            const ultimoMensajeCliente = this.mensajesChatBot[this.mensajesChatBot.length - 1];
            if (ultimoMensajeCliente.outgoing == 0 && this.dsMensajeChat == true) {
                this.dsMensajeChat == false;
            }

            let ultimoMensaje = null; // Inicializar como nulo para verificar si se encontró un mensaje
            for (let i = this.mensajesChatBot.length - 1; i >= 0; i--) {
                const mensaje = this.mensajesChatBot[i];
                if (mensaje.outgoing == 0) {
                    ultimoMensaje = mensaje;
                    break; // Detener el bucle una vez que se encuentra el mensaje saliente
                }
            }

            if (ultimoMensaje) {
                /*console.log('Contenido de la última fecha ingresada: ' + ultimoMensaje.created_at);
                console.log('Contenido de quien mandó el mensaje: ' + ultimoMensaje.outgoing);
                console.log('Contenido de quien mandó el mensaje: ' + ultimoMensaje.mensaje);

                const fechaActual = Date.now();
                const fechaMensaje = new Date(ultimoMensaje.created_at).getTime();

                if (ultimoMensaje.outgoing == 0 && fechaActual - fechaMensaje >= 82800000) {
                    console.log('Han pasado 23 horas o más');
                    this.dsMensajeChat = true;
                    this.ifSaludo = true;
                    this.ifDespedida = false;
                    this.ifPausa = false;
                    this.ifSoporte = false;
                } else {
                    console.log('No han pasado 23 horas o más');
                    this.dsMensajeChat = false;
                    this.ifSaludo = true;
                    this.ifDespedida = false;
                    this.ifPausa = false;
                    this.ifSoporte = false;
                }*/

            } else {
                // No se encontró ningún mensaje saliente con outgoing === 0
                console.log('No se encontró ningún mensaje saliente con outgoing === 0');
                this.dsMensajeChat = true;
                this.ifSaludo = true;
                this.ifDespedida = false;
                this.ifPausa = false;
                this.ifSoporte = false;
            }

            this.scrollDown();

        },

        verificarPausaServicio() {

            const url = 'https://glpi-siicsa.azurewebsites.net/consultaPausaServicio.php?celularCliente=' + this.celularCliente;

            axios.get(url)
                .then(({ data }) => {

                    let pausa = data[0].pausa;
                    console.log("ESTE ES EL ESTADO DEL SERVICIO (PAUSA): " + this.pausa);

                    if (pausa == 1) {
                        console.log('this pausa es igual a 1, entro al cambio de isPaused');
                        if (this.isPaused == false) {
                            this.isPaused = !this.isPaused;
                        } else {
                            this.isPaused = this.isPaused;
                        }
                    } else {
                        console.log('this pausa es igual a 0, entro al cambio de isPaused');
                        if (this.isPaused == true) {
                            this.isPaused = !this.isPaused;
                        } else {
                            this.isPaused = this.isPaused;
                        }
                    }

                }).catch(function (error) {
                    console.log(error);
                })
        },

        cargarMensajes() {

            if (this.idPQR != '0') {

                var datos = {
                    clicel: this.celularCliente,
                    tipo: this.perfilM,
                    id: this.idPQR
                };

                this.ifChat2 = true;

                axios.post(this.baseURL + 'api/messages', {
                    'clicel': this.celularCliente,
                    'recipient': this.recipient
                })
                    .then(({ data }) => {
                        let arrayMensajes = [];
                        arrayMensajes.push(data.data);
                        for (let i = 0; i < arrayMensajes[0].length; i++) {

                            this.mensajesChatBot.push({ rol: arrayMensajes[0][i].outgoing == 1 ? 1 : 0, mensaje: arrayMensajes[0][i].body, estado: arrayMensajes[0][i].status, interaccion: 0, documento: 0, horaMensaje: this.formatFecha(arrayMensajes[0][i].created_at), tipo: arrayMensajes[0][i].type, wam_id: arrayMensajes[0][i].wam_id, outgoing: arrayMensajes[0][i].outgoing, created_at: arrayMensajes[0][i].created_at, id: arrayMensajes[0][i].id, resp_men: arrayMensajes[0][i].resp_men, id: arrayMensajes[0][i].id, resp_men_body: arrayMensajes[0][i].resp_men_body });

                        }

                        this.scrollDown();

                        this.verificarUltimoMensaje();

                        axios.post(this.baseURL + '/api/wh_buscarchatactivo', {
                            clicel: this.celularCliente
                        })
                            .then(response => {
                                console.log('response.data.nombre: ' + response.data.data[0].nombre);
                                if (response.data.data[0].nombre === undefined || response.data.data[0].nombre === null || response.data.data[0].nombre === '') {
                                    this.userChatActivo = "Chat Activo con: BOT";

                                    this.ifDespedida = false;
                                    this.ifSoporte = false;
                                    this.ifPausa = false;
                                    this.ifSaludo = true;
                                } else {
                                    if (response.data.data[0].celular == this.celularCliente) {
                                        if (response.data.data[0].envia == this.idUsuario) {
                                            this.userChatActivo = "Chat Activo con: " + response.data.data[0].nombre;
                                            this.ifDespedida = true;
                                            this.ifSoporte = true;
                                            this.ifPausa = true;
                                            this.ifSaludo = false;
                                        } else {
                                            this.userChatActivo = "Chat Activo con: " + response.data.data[0].nombre;
                                            this.ifDespedida = true;
                                            this.ifSoporte = true;
                                            this.ifPausa = true;
                                            this.ifSaludo = false;
                                        }
                                    }
                                }
                            })
                            .catch(error => {
                                console.log('Error buscarchatactivo: ' + error);
                            });

                        this.verificarPausaServicio();
                    })
                    .catch(error => {
                        console.log(error);
                    });

            } else if (this.idPQR == '0') {
                var rcp = this.recipient;
                if (this.canal == 'instagram' || this.canal == 'messenger') {
                    rcp = this.celularCliente
                } else {
                    rcp = this.recipient
                }
                axios.post(this.baseURL + 'api/messages', {
                    'clicel': this.celularCliente,
                    'recipient': rcp
                })
                    .then(response => {
                        console.log(response.data.data);
                        let arrayMensajes = [];
                        arrayMensajes.push(response.data.data);

                        for (let i = 0; i < arrayMensajes[0].length; i++) {

                            this.mensajesChatBot.push({ rol: arrayMensajes[0][i].outgoing == 1 ? 1 : 0, mensaje: arrayMensajes[0][i].body, estado: arrayMensajes[0][i].status, interaccion: 0, documento: 0, horaMensaje: this.formatFecha(arrayMensajes[0][i].created_at), tipo: arrayMensajes[0][i].type, wam_id: arrayMensajes[0][i].wam_id, outgoing: arrayMensajes[0][i].outgoing, created_at: arrayMensajes[0][i].created_at, id: arrayMensajes[0][i].id, resp_men: arrayMensajes[0][i].resp_men, id: arrayMensajes[0][i].id, resp_men_body: arrayMensajes[0][i].resp_men_body });

                        }

                        this.scrollDown();

                        this.verificarUltimoMensaje();

                        axios.post(this.baseURL + '/api/wh_buscarchatactivo', {
                            clicel: this.celularCliente
                        })
                            .then(response => {
                                console.log('response.data.nombre: ' + response.data.data[0].nombre);
                                if (response.data.data[0].nombre === undefined || response.data.data[0].nombre === null || response.data.data[0].nombre === '') {
                                    this.userChatActivo = "Chat Activo con: BOT";
                                    this.ifDespedida = false;
                                    this.ifSoporte = false;
                                    this.ifPausa = false;
                                    this.ifSaludo = true;
                                } else {
                                    if (response.data.data[0].celular == this.celularCliente) {
                                        if (response.data.data[0].envia == this.idUsuario) {
                                            this.userChatActivo = "Chat Activo con: " + response.data.data[0].nombre;
                                            this.ifDespedida = true;
                                            this.ifSoporte = true;
                                            this.ifPausa = true;
                                            this.ifSaludo = false;
                                        } else {
                                            this.userChatActivo = "Chat Activo con: " + response.data.data[0].nombre;
                                            this.ifDespedida = true;
                                            this.ifSoporte = true;
                                            this.ifPausa = true;
                                            this.ifSaludo = false;
                                        }
                                    }
                                }
                            })
                            .catch(error => {
                                console.log('Error buscarchatactivo: ' + error);
                            });

                        this.verificarPausaServicio();
                    })
                    .catch(error => {
                        console.log(error);
                    });

            }

        },

        validarEnvioMensaje() {

            if (this.modoChat == 1) {
                this.sendMessage();
            } else if (this.modoChat == 2) {
                this.envioMensajeChat();
            }

        },

        cambioModoChat() {

            if (this.modoChat == 1) {

                this.modoChat = 2;
                this.imagenModelo = 'https://glpi-siicsa.azurewebsites.net/img/Bot.png'
                this.userChatActivo = "";
                this.dsMensajeChat = false;
                this.mensajesChatBot = [];
                this.ifDespedida = false;
                this.ifSoporte = false;
                this.ifPausa = false;
                this.ifSaludo = false;
                this.colSoporte = true;

            } else if (this.modoChat == 2) {

                this.dsMensajeChat = true;
                this.colSoporte = false;
                this.mensajesChatBot = [];
                this.modoChat = 1;
                this.rol_sql.length = 1;
                this.rol_conversa.length = 1;
                this.imagenModelo = 'https://glpi-siicsa.azurewebsites.net/img/Ana.png'
                this.cargarMensajes();
            }
        },

        responderMensajeD(mensaje, id) {
            this.responderMensaje = !this.responderMensaje;
            this.mensajeAResponder = mensaje;

            if (this.responderMensaje == true) {
                this.dsMensajeChat = false;
                this.labelMensaje = 'Respondiendo a ☝️';
                this.idMensajeRespuesta = id;
                this.scrollDown();
            } else {
                this.verificarUltimoMensaje();
                this.labelMensaje = 'Escribe aqui tu mensaje...';
                this.scrollDown();
            }
        },
    }

}

</script>

<style>
/* Recording animation styles (burgundy/red dots) */
.avatar-recording {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: center;
    justify-content: center;
}

.mic-badge {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #b0002e; /* burgundy */
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
.mic-badge v-icon,
.mic-badge .v-icon {
    color: #fff;
    font-size: 11px;
    line-height: 1;
}

.recording-dots-row { display: flex; gap: 4px; align-items: center; justify-content: center; }
.recording-dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #b0002e; /* burgundy/red */
    opacity: 0.25;
    display: inline-block;
    transform: translateY(0);
    animation: recording-bounce 900ms infinite ease-in-out;
}
.recording-dot:nth-child(2) { animation-delay: 0.12s; }
.recording-dot:nth-child(3) { animation-delay: 0.24s; }

@keyframes recording-bounce {
    0% { transform: translateY(0); opacity: 0.25; }
    50% { transform: translateY(-3px); opacity: 1; }
    100% { transform: translateY(0); opacity: 0.25; }
}

.recording-avatar { min-width: 44px; min-height: 44px; display: flex; align-items: center; justify-content: center; }

/* Modern contact title styles */
.contact-title-block {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 2px;
}

.contact-title-name {
    font-size: 1.15rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: 0.5px;
    line-height: 1.2;
    text-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.contact-title-phone {
    font-size: 1.05rem;
    font-weight: 600;
    color: #dfdfdf;
    letter-spacing: 0.3px;
    line-height: 1.1;
    border-radius: 0px;
    margin-top: 1px;
}

/* Estado de conexión en cabecera */
.chat-status-online {
    color: #43a047 !important;
    font-weight: 600;
}

.chat-status-offline {
    color: #757575 !important;
    font-weight: 600;
}

html,
body {
    overflow: hidden !important;
}

.container {
    align-items: center;
    display: flex;
    justify-content: center;
    gap: 0.1rem;

    animation: 2s zoom infinite ease-out;
    position: relative;

    left: 15px;
    float: left;
    width: 60px;
    height: 0px;

    background: #006CA1;
    border-radius: 9999px;
    padding: 1rem;

}

.container::before,
.container::after {
    content: '';
    position: absolute;
    border-radius: 9999px;
    background: #006CA1;
    bottom: 0;
    left: 0;
}

.container::before {
    height: 1rem;
    width: 1rem;
    transform: translate(-0.125rem, 0.125rem);
}

.container::after {
    height: 0.5rem;
    width: 0.5rem;
    transform: translate(-0.5rem, 0.5rem);
}

.dot {
    border-radius: 9999px;
    height: 0.4rem;
    width: 0.4rem;

    background: rgb(255, 255, 255);
    animation: wave 1s infinite;
}

.dot:nth-child(1) {
    animation-delay: 0.3333s;
}

.dot:nth-child(2) {
    animation-delay: 0.6666s;
}

.dot:nth-child(3) {
    animation-delay: 0.9999s;
}

.v-avatar.shadow {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.fixed-chat-header {
    min-height: 90px !important;
    max-height: 120px !important;
    height: 90px !important;
    transition: none !important;
}

.fixed-chat-buttons {
    min-height: 70px !important;
    max-height: 80px !important;
    height: 70px !important;
    transition: none !important;
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

@keyframes zoom {
    50% {
        transform: scale(1.1);
    }
}

@keyframes wave {
    0% {
        transform: translateY(0px);
        background: rgba(148 163 184 / 0);
    }

    50% {
        transform: translateY(-0.5rem);
        background: rgba(255, 255, 255, 0.8);
    }

    100% {
        transform: translateY(0px);
        background: rgba(148 163 184 / 0);
    }
}

.anachat:hover {
    cursor: pointer;
}

.chat-box::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background-image: url('https://i.pinimg.com/564x/ab/63/ce/ab63ce446c82f192be2475a7b6cbf510.jpg');
    background-size: auto;
    background-repeat: repeat;
    opacity: 0.05;
}

.chat-box>* {
    position: relative;
    z-index: 1;
}

.scroll-custom::-webkit-scrollbar {
    width: 10px;
    border-radius: 8px;
    background: #e3eafc00;
}

.scroll-custom::-webkit-scrollbar-thumb {
    background: #9c9c9c98;
    border-radius: 8px;
}

.scroll-custom::-webkit-scrollbar-thumb:hover {
    background: #9c9c9cee;
}

.scroll-custom::-webkit-scrollbar-track {
    background: #f5f7fa00;
    border-radius: 8px;
}
</style>