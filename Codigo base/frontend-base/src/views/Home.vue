<template>

  <v-dialog v-model="alertLogin" persistent style="z-index: 10000;">
    <v-card :style="getAlertStyle()">
      <v-card-title v-text="mensajeAlertLogin" style="color: black; text-align: center;"></v-card-title>
      <v-btn class="mt-4 mx-auto" @click="cerrarDIV()"
        style="border-radius: 20px; color: black; background-color: rgb(188, 209, 255); margin: 0 auto; display: block;">Cerrar</v-btn>
    </v-card>
  </v-dialog>

  <v-app
    style="background-image: linear-gradient(rgba(34,53,81,0.65), rgba(34,53,81,0.65)), url('https://glpi-siicsa.azurewebsites.net/img/fondologin.jpg'); width: 100%; min-height: 100vh; object-fit: contain; background-size: cover; background-blend-mode: multiply;">
    <v-expand-x-transition>
          <v-card v-show="expand" width="400" class="mx-auto my-auto pa-0" style="border-radius: 32px; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.18); background: none; min-width: 320px; max-width: 95vw;">
            <div class="d-flex flex-column align-center justify-center" style="background-color: rgba(255,255,255,0.98); min-height: 480px; padding: 32px 32px;">
                <img src="../assets/LogosinFondo.png" alt="Logo" class="mb-4" style="width: 230px; height: 100px; border-radius: 0px;" />
              <h2 style="color: #1e3a8a; font-weight: 700; font-size: 1.8rem; margin-bottom: 0;">Bienvenido de Nuevo</h2>
              <span style="color: #1e3a8a; font-size: 1rem; margin-bottom: 18px;">Inicia sesión en tu cuenta</span>
              <v-defaults-provider :defaults="{ 'VIcon': { 'color': '#1e3a8a' } }">
                <v-card-text class="pa-0" style="width: 100%;">
                  <v-text-field style="width: 100%; margin-bottom: 18px;" v-model="user" :readonly="loading" :rules="[required]"
                    class="mx-auto" clearable label="Usuario" prepend-icon="mdi-account" autocomplete="off"
                    variant="solo-filled" color="#1e3a8a"></v-text-field>
                  <v-text-field style="width: 100%; margin-bottom: 18px;" v-model="password" :readonly="loading" :rules="[required]"
                    class="mx-auto" clearable label="Contraseña" prepend-icon="mdi-lock" :type="show ? 'text' : 'password'"
                    :append-inner-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append-inner="show = !show" @keydown.enter.exact.prevent="login()" autocomplete="off"
                    variant="solo-filled" color="#1e3a8a"></v-text-field>
                  <div class="d-flex justify-center align-center">
                    <v-btn color="#1e3a8a" :loading="loading" size="large" @click="login()" style="color: #fff; font-weight: 700; width: 100%; border-radius: 12px; margin-bottom: 12px;">
                      <v-icon color="#fff" class="mr-2">mdi mdi-login</v-icon>
                      Ingresar</v-btn>
                  </div>
                  <div class="mt-2" style="text-align: center;" v-if="false">
                    <span style="color: #1e3a8a;">¿No Recuerdas tu Contraseña? </span> <br>
                    <a style="color: #1e3a8a; text-decoration: underline; font-weight: 600; margin-left: 4px;" @click="dialogRecuperarClave = true">Recuperala Aquí</a>
                  </div>
                </v-card-text>
              </v-defaults-provider>
            </div>
          </v-card>
    </v-expand-x-transition>

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
          <div class="text-caption mt-n4 mb-4" style="color: red;" v-if="nuevaClave && !isValidPassword(nuevaClave)">La
            nueva
            clave debe tener al menos una mayúscula, un número, un caracter especial y mínimo 8 caracteres.</div>
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
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-app>

    <v-dialog v-model="dialogRecuperarClave" persistent max-width="600px">
        <v-card class="pa-0" style="border-radius: 18px; overflow: hidden; box-shadow: 0 4px 24px rgba(0,0,0,0.10);">
          <div style="background-color: #006CA1; color: white; padding: 18px 24px 12px 24px; display: flex; align-items: center; gap: 12px;">
            <v-icon size="32" style="color: white; border-radius: 50%; padding: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.10);">mdi mdi-lock-alert</v-icon>
            <span style="font-size: 1.25rem; font-weight: 600;">Recuperar Contraseña</span>
            <v-spacer></v-spacer>
          <v-btn icon="mdi-close" size="small" color="white" @click="dialogRecuperarClave = false; " class="btn-grow" />
          </div>
          <v-card-text class="pt-4 pb-2 px-5">
            <div class="mb-2" style="font-size: 1.05rem; color: #222; font-weight: 500;">Ingresa tu correo registrado y te enviaremos una contraseña temporal para que puedas acceder.</div>
            <v-text-field v-model="correoRecuperar" label="Correo electrónico" type="email" variant="outlined" required clearable
              prepend-inner-icon="mdi-email" autocomplete="email" style="margin-bottom: 12px;" :rules="[v => !!v || 'El correo es obligatorio']" />
            <div v-if="errorRecuperarClave" class="text-caption mb-2" style="color: #e53935; font-weight: 500; background: #fff3f3; border-radius: 6px; padding: 6px 10px;">
              <v-icon left size="16" color="#e53935" style="margin-right: 4px;">mdi-alert-circle</v-icon>
              {{ errorRecuperarClave }}
            </div>
          </v-card-text>
          <v-card-actions class="px-5 pb-4 pt-2" style="justify-content: flex-end;">
            <v-btn color="#006CA1" variant="flat" style="color: white; font-weight: 600; border-radius: 8px; min-width: 120px; font-size: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.08);" @click="enviarCorreoRecuperacion">
              <v-icon left size="18" style="margin-right: 6px;">mdi-send</v-icon>
              Enviar
            </v-btn>
          </v-card-actions>
        </v-card>
    </v-dialog>

 
</template>

<script>
import axios from 'axios';
import CryptoJS from "crypto-js";

export default {
  data: () => ({
    baseURL: '',
    isScreenSizeLarge: false,
    isScreenSizeSmall: false,
    isMobileView: false,

    form: false,
    loading: false,
    show: false,
    user: '',
    password: '',
    alertLogin: false,
    mensajeAlertLogin: '',
    expand: false,

    dialogCambioClave: false,
    claveActual: null,
    nuevaClave: null,
    confirmarClave: null,
    mostrarClaveActual: false,
    mostrarNuevaClave: false,
    mostrarConfirmarClave: false,

    listaUsuarios: [],
    dialogRecuperarClave: false,
    correoRecuperar: '',
    errorRecuperarClave: '',

  }),

  created() {
    this.checkScreenSize();
    window.addEventListener('resize', this.checkScreenSize);
    window.addEventListener('orientationchange', this.checkScreenSize);
  },
  destroyed() {
    window.removeEventListener('resize', this.checkScreenSize);
    window.removeEventListener('orientationchange', this.checkScreenSize);
  },

mounted() {
    this.baseURL = import.meta.env.VITE_API_BASE_URL; 
    this.obtenerUsuarios(); 
    setTimeout(() => {
      this.expand = true;
    }, 500);
  },


  methods: {
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
          width: '75%',
          zIndex: 10000
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
          width: '20%',
          zIndex: 10000
        };
      }
    },

    checkScreenSize() {
      this.isScreenSizeLarge = window.innerWidth >= 600;
      this.isScreenSizeSmall = window.innerWidth < 600;
      this.isMobileView = this.isScreenSizeSmall && !this.isScreenSizeLarge;

      if (this.isMobileView) {
        this.showGoBack = true;
        if (window.orientation === 90 || window.orientation === -90) {
          // La pantalla está en modo horizontal
          alert('Por favor, gire su dispositivo a modo vertical para ver la página correctamente.');
        }


      }

    },

    async enviarCorreoRecuperacion() {
      this.errorRecuperarClave = '';
      const correo = this.correoRecuperar.trim();
      if (!correo) {
        this.errorRecuperarClave = 'Por favor ingrese su correo.';
        return;
      }
      // Buscar usuario por correo
      const usuario = this.listaUsuarios.find(u => u.correo && u.correo.toLowerCase() === correo.toLowerCase());
      if (!usuario) {
        this.errorRecuperarClave = 'El correo no está registrado.';
        return;
        }
        // Generar contraseña temporal
        const tempPassword = Math.random().toString(36).slice(-8) + Math.floor(Math.random()*100);
        // Enviar correo (llamar API backend para enviar correo) MIRAR COMO SE HACE
        try {
          await axios.post(this.baseURL + 'api/enviarRecuperacion', {
            correo: correo,
            nombre: usuario.nom,
            tempPassword: tempPassword,
            });
            // Actualizar contraseña en backend
            await axios.post(this.baseURL + 'api/editusu', {
              idusu: usuario.id,
              clave: CryptoJS.MD5(tempPassword).toString(),
              });
                this.dialogRecuperarClave = false;
                this.mensajeAlertLogin = 'Se ha enviado un correo con una contraseña temporal.';
                this.alertLogin = true;
                this.correoRecuperar = '';
              } catch (err) {
                this.errorRecuperarClave = 'Error al enviar el correo. Intente más tarde.';
              }
            },
              


    cerrarDIV() {
      this.alertLogin = false;
    },

    required(v) {
      return !!v || 'Este campo es obligatorio'
    },

    async login() {
      const url = this.baseURL + '/api/login';
      const usuario = this.user;
      const clave = this.password.trim();

      if (usuario === '' || clave === '') {
        this.mensajeAlertLogin = 'Por favor, complete todos los campos';
        this.alertLogin = true;
        return;
      }

      try {
        const response = await axios.post(url, {
          'usuario': usuario,
          'clave': clave,
        })

        const data = response.data.data[0];
        console.log('Data:')
        console.log(data)

        const cedula = data.cedula

        if (cedula == clave) {
          this.alertLogin = true;
          this.mensajeAlertLogin = 'Bienvenido ' + data.nom + ' ' + data.ape + ', para ingresar por primera vez debe cambiar su contraseña.';

          setTimeout(() => {
            localStorage.setItem('idUsuario', data.id);
            this.dialogCambioClave = true;
          }, 500);
          return;
        }

        if (data.res == 1) {
          localStorage.setItem('idUsuario', data.id);
          localStorage.setItem('idCargo', data.idcar);
          localStorage.setItem('nombreLogin', data.nom);
          localStorage.setItem('apellidoLogin', data.ape);
          localStorage.setItem('celularLogin', data.cel);
          localStorage.setItem('cedulaLogin', data.cedula);
          localStorage.setItem('logueado', 'true')
          // Router push segun cargo
          const idCargo = localStorage.getItem('idCargo')
          switch (idCargo) {
            case '1':
              this.$router.push('/configuracion')
              break
            case '2':
              this.$router.push('/contactos')
              break
            case '3':
              this.$router.push('/comercial')
              break
            case '4':
              this.$router.push('/gerencial')
              break
            case '5':
              this.$router.push('/pqr')
              break
            default:
              this.$router.push('/')
          }
          //this.mensajeAlertLogin = 'Exitoso';
          //this.alertLogin = true;
          //return;
        } else {
          this.mensajeAlertLogin = 'Usuario o contraseña incorrectos';
          this.alertLogin = true;
          return;
        }
      } catch (err) {
        this.mensajeAlertLogin = 'Error de Sistema:\n' + err;
        this.alertLogin = true;
      }
    },

    logout() {
      localStorage.removeItem('idUsuario')
      localStorage.removeItem('idCargo')
      localStorage.removeItem('nombreLogin')
      localStorage.removeItem('apellidoLogin')
      localStorage.removeItem('celularLogin')
      localStorage.removeItem('logueado')
      this.$router.push('/')
    },

    cambiarClave() {
      const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

      if (this.nuevaClave !== this.confirmarClave) {
        this.alertLogin = true;
        this.mensajeAlertLogin = 'Las claves no coinciden.';
        return;
      } else if (!regex.test(this.nuevaClave)) {
        this.alertLogin = true;
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
              this.alertLogin = true;
              this.mensajeAlertLogin = 'La clave actual ingresada no coincide con el usuario.';
            } else if (response.data.data[0].respuesta == 'La clave ha sido editada correctamente.') {
              this.alertLogin = true;
              this.mensajeAlertLogin = 'La clave ha sido editada correctamente.';
              this.dialogCambioClave = false;
              this.claveActual = null;
              this.nuevaClave = null;
              this.confirmarClave = null;
            }
          })
          .catch(error => {
            console.error('Error al cambiar la clave:', error);
            this.alertLogin = true;
            this.mensajeAlertLogin = 'Error al cambiar la clave.';
          });
      }
    },

    isValidPassword(password) {
      const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;
      return regex.test(password);
    },

    obtenerUsuarios() {
      axios.post(this.baseURL + "api/cargausus", {
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

    async actualizarUsuario() {
      this.mensajeAlertLogin = "Actualizando usuario...";
      this.alerta = true;
      this.ifCargando = true;
      await axios
        .post(this.baseURL + "api/editusu", {
          clave: this.contraseñaUsu
            ? CryptoJS.MD5(this.cedulaUsu).toString()
            : "",
        })
        .then((response) => {
          console.log("Usuario actualizado:", response.data);
          this.ifCargando = false;
          this.alerta = true;
          this.mensajeAlertLogin = "Usuario actualizado correctamente";
        }) 
        .catch((error) => {
          console.log(error);
        });
    },

  },
}
</script>

<style>
.button-82-pushable {
  position: relative;
  border: none;
  background: transparent;
  padding: 0;
  cursor: pointer;
  outline-offset: 4px;
  transition: filter 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-82-shadow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  background: hsl(0deg 0% 0% / 0.25);
  will-change: transform;
  transform: translateY(2px);
  transition:
    transform 600ms cubic-bezier(.3, .7, .4, 1);
}

.button-82-edge {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  background: linear-gradient(to left,
      hsl(253, 100%, 16%) 0%,
      hsl(249, 100%, 32%) 8%,
      hsl(244, 100%, 32%) 92%,
      hsl(261, 100%, 16%) 100%);
}

.button-82-front {
  display: block;
  position: relative;
  padding: 12px 27px;
  border-radius: 12px;
  font-size: 1.1rem;
  color: white;
  background: hsl(219, 74%, 50%);
  will-change: transform;
  transform: translateY(-4px);
  transition:
    transform 600ms cubic-bezier(.3, .7, .4, 1);
}

@media (min-width: 768px) {
  .button-82-front {
    font-size: 1.25rem;
    padding: 12px 42px;
  }
}

.button-82-pushable:hover {
  filter: brightness(110%);
  -webkit-filter: brightness(110%);
}

.button-82-pushable:hover .button-82-front {
  transform: translateY(-6px);
  transition:
    transform 250ms cubic-bezier(.3, .7, .4, 1.5);
}

.button-82-pushable:active .button-82-front {
  transform: translateY(-2px);
  transition: transform 34ms;
}

.button-82-pushable:hover .button-82-shadow {
  transform: translateY(4px);
  transition:
    transform 250ms cubic-bezier(.3, .7, .4, 1.5);
}

.button-82-pushable:active .button-82-shadow {
  transform: translateY(1px);
  transition: transform 34ms;
}

.button-82-pushable:focus:not(:focus-visible) {
  outline: none;
}
</style>