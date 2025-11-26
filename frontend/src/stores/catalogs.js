import { defineStore } from 'pinia'

export const useCatalogsStore = defineStore('catalogs', {
    state: () => ({
        departamentos: [],
        ciudades: [],
        tiposEquipo: [],
        estadosEquipo: [],
        fabricantes: [],
        // ... otros catálogos
        loading: false
    }),

    actions: {
        async fetchCatalogs() {
            if (this.departamentos.length > 0) return // Ya cargados

            this.loading = true
            try {
                // TODO: Llamadas a API
                // const [deptos, tipos] = await Promise.all([...])
                console.log('Cargando catálogos...')
            } catch (error) {
                console.error('Error loading catalogs', error)
            } finally {
                this.loading = false
            }
        }
    }
})
