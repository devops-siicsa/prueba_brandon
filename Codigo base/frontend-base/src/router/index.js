import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Mercadeo from '../views/Mercadeo.vue'
import Comercial from '../views/Comercial.vue'
import Pendiente from '../views/Pendiente.vue'
import PendienteGeneral from '@/views/PendienteGeneral.vue'
import Configuracion from '@/views/Configuracion.vue'
import Pqr from '@/views/Pqr.vue'
import Pedidos from '@/views/Pedidos.vue'
import ChatWeb from '@/views/ChatWeb.vue'
import Campaña from '@/views/Campana.vue'
import informesCampañas from '../views/informesCampañas.vue'
import InformesCio from '../views/InformesCio.vue'
import VerCampañas from '@/views/VerCampanas.vue'
import Contactos from '@/views/Contactos.vue'
import ClientesSinActividad from '@/views/ClientesSinActividad.vue'
import Gerencial from '@/views/Gerencial.vue'
import ProspeccionT from '@/views/ProspeccionT.vue'
import seguimientoLlamadas from '@/views/seguimientoLlamadas.vue'
import Empresas from '@/views/Empresas.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/mercadeo', component: Mercadeo, meta: { requiereAuth: true, cargos: ['2'] } },
  { path: '/comercial', component: Comercial, meta: { requiereAuth: true, cargos: ['3'] } },
  { path: '/pendiente', component: Pendiente, meta: { requiereAuth: true, cargos: ['3'] } },
  { path: '/pendiente-general', component: PendienteGeneral, meta: { requiereAuth: true, cargos: ['3'] } },
  { path: '/configuracion', component: Configuracion, meta: { requiereAuth: true, cargos: ['1'] } },
  { path: '/pqr', component: Pqr, meta: { requiereAuth: true, cargos: ['5'] } },
  { path: '/informes-cio', component: InformesCio, meta: { requiereAuth: true, cargos: ['5'] } },
  { path: '/pedidos', component: Pedidos, meta: { requiereAuth: true, cargos: ['3'] } },
  { path: '/chat-web', component: ChatWeb, meta: { requiereAuth: true } },
  { path: '/campana', component: Campaña, meta: { requiereAuth: true, cargos: ['2'] } },
  { path: '/informes-campanas', component: informesCampañas, meta: { requiereAuth: true, cargos: ['2'] } },
  { path: '/verCampanas', component: VerCampañas, meta: { requiereAuth: true, cargos: ['2'] } },
  { path: '/contactos', component: Contactos, meta: { requiereAuth: true, cargos: ['2'] } },
  { path: '/clientesSinActividad', component: ClientesSinActividad, meta: { requiereAuth: true, cargos: ['3'] } },
  { path: '/gerencial', component: Gerencial, meta: { requiereAuth: true, cargos: ['4'] } },
  { path: '/prospeccion-telefonica', component: ProspeccionT, meta: { requiereAuth: true, cargos: ['2'] } },
  { path: '/seguimiento-llamadas', component: seguimientoLlamadas, meta: { requiereAuth: true, cargos: ['2'] } },
  { path: '/empresas', component: Empresas, meta: { requiereAuth: true, cargos: ['2'] } },

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// ⛔ Navigation Guard
router.beforeEach((to, from, next) => {
  const logueado = localStorage.getItem('logueado') === 'true'
  const idCargo = localStorage.getItem('idCargo')

  if (to.meta.requiereAuth && !logueado) {
    return next('/')
  }

  if (to.meta.cargos && !to.meta.cargos.includes(idCargo)) {
    // Disparar evento inmediatamente antes de cancelar la navegación
    setTimeout(() => {
      window.dispatchEvent(new CustomEvent('access-denied', {
        detail: { mensaje: 'No tienes permisos para acceder a esta página' }
      }))
    }, 0)
    return next(from.fullPath || '/') // lo devuelve a la ruta anterior o al home si no hay
  }

  if (to.path === '/' && logueado) {
    switch (idCargo) {
      case '1': return next('/configuracion')
      case '2': return next('/contactos')
      case '3': return next('/comercial')
      case '4': return next('/gerencial')
      case '5': return next('/pqr')
      default: return next('/')
    }
  }

  next()
})

export default router