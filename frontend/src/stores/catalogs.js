import { defineStore } from 'pinia'
import axios from 'axios'

export const useCatalogsStore = defineStore('catalogs', {
    state: () => ({
        departamentos: [],
        ciudades: [],
        tiposEquipo: [],
        estadosEquipo: [],
        fabricantes: [],
        // Hardware Catalogs
        marcasProcesador: [],
        tiposProcesador: [],
        generacionesProcesador: [],
        tiposRam: [],
        capacidadesRam: [],
        busesRam: [],
        tiposAlmacenamiento: [],
        capacidadesAlmacenamiento: [],
        protocolosAlmacenamiento: [],
        factoresFormaAlmacenamiento: [],
        // Software Catalogs
        sistemasOperativos: [],
        ofimaticas: [],
        antivirus: [],
        aplicativos: [], // New catalog for Apps

        loading: false,
        offlineReady: false
    }),

    actions: {
        async fetchCatalogs(keys = []) {
            this.loading = true

            // 1. Load from LocalStorage first (Cache-first strategy)
            keys.forEach(key => {
                const cached = localStorage.getItem(`catalog_${key}`)
                if (cached) {
                    try {
                        this[key] = JSON.parse(cached)
                    } catch (e) {
                        console.error(`Error parsing cached catalog ${key}`, e)
                    }
                }
            })

            // 2. Fetch from API (Network-second)
            try {
                const promises = []
                const endpoints = {
                    estadosEquipo: '/api/config/catalogs/estados_equipo',
                    tiposEquipo: '/api/config/catalogs/tipos_equipo',
                    fabricantes: '/api/config/catalogs/fabricantes',
                    marcasProcesador: '/api/config/catalogs/marcas_procesador',
                    tiposProcesador: '/api/config/catalogs/tipos_procesador',
                    generacionesProcesador: '/api/config/catalogs/generaciones_procesador',
                    tiposRam: '/api/config/tipos_ram',
                    capacidadesRam: '/api/config/capacidades_ram',
                    busesRam: '/api/config/velocidades_ram',
                    tiposAlmacenamiento: '/api/config/tipos_almacenamiento',
                    capacidadesAlmacenamiento: '/api/config/capacidades_almacenamiento',
                    protocolosAlmacenamiento: '/api/config/protocolos_almacenamiento',
                    factoresFormaAlmacenamiento: '/api/config/factores_forma_almacenamiento',
                    sistemasOperativos: '/api/config/catalogs/sistemas_operativos',
                    ofimaticas: '/api/config/catalogs/ofimaticas',
                    antivirus: '/api/config/catalogs/antivirus',
                    aplicativos: '/api/config/catalogs/aplicativos' // New endpoint
                }

                keys.forEach(key => {
                    if (endpoints[key]) {
                        promises.push(
                            axios.get(endpoints[key], { withCredentials: true })
                                .then(res => {
                                    this[key] = res.data
                                    localStorage.setItem(`catalog_${key}`, JSON.stringify(res.data))
                                })
                        )
                    }
                })

                await Promise.allSettled(promises)
            } catch (error) {
                console.error('Error updating catalogs from API', error)
                // We don't throw here, so the app keeps running with cached data
            } finally {
                this.loading = false
                // If we have data, we are ready for offline
                if (
                    this.estadosEquipo.length > 0 ||
                    this.tiposEquipo.length > 0 ||
                    this.fabricantes.length > 0 ||
                    this.sistemasOperativos.length > 0 ||
                    this.ofimaticas.length > 0 ||
                    this.antivirus.length > 0 ||
                    this.aplicativos.length > 0
                ) {
                    this.offlineReady = true
                }
            }
        },

        async createAplicativo(nombre, version) {
            try {
                // Optimistic update
                const tempId = Date.now()
                const newApp = { Id: tempId, Nombre: nombre, Version: version }
                this.aplicativos.push(newApp)

                // API Call
                // const res = await axios.post('/api/config/catalogs/aplicativos', { Nombre: nombre, Version: version })
                // Replace temp with real data
                // const index = this.aplicativos.findIndex(a => a.Id === tempId)
                // if (index !== -1) this.aplicativos[index] = res.data

                // For now, just save to local storage to simulate persistence
                localStorage.setItem('catalog_aplicativos', JSON.stringify(this.aplicativos))
                return newApp
            } catch (e) {
                console.error('Error creating app', e)
                throw e
            }
        }
    }
})
