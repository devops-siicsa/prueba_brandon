import { openDB } from 'idb'
import axios from 'axios'

const DB_NAME = 'inventory_db'
const STORE_NAME = 'offline_queue'

async function getDB() {
    return openDB(DB_NAME, 2, {
        upgrade(db) {
            if (!db.objectStoreNames.contains('drafts')) {
                db.createObjectStore('drafts')
            }
            if (!db.objectStoreNames.contains(STORE_NAME)) {
                db.createObjectStore(STORE_NAME, { keyPath: 'id', autoIncrement: true })
            }
        },
    })
}

export const syncService = {
    async addToQueue(data) {
        const db = await getDB()
        const item = {
            ...data,
            timestamp: Date.now(),
            retryCount: 0
        }
        return db.add(STORE_NAME, item)
    },

    async getQueue() {
        const db = await getDB()
        return db.getAll(STORE_NAME)
    },

    async removeFromQueue(id) {
        const db = await getDB()
        return db.delete(STORE_NAME, id)
    },

    async processQueue() {
        const queue = await this.getQueue()
        if (queue.length === 0) return 0

        let processedCount = 0
        for (const item of queue) {
            try {
                // Remove internal fields before sending
                const { id, timestamp, retryCount, ...payload } = item

                await axios.post('/api/inventory/equipos', payload, { withCredentials: true })

                await this.removeFromQueue(id)
                processedCount++
            } catch (error) {
                console.error(`Failed to sync item ${item.id}`, error)
                // Optional: Update retry count or handle permanent failures
            }
        }
        return processedCount
    }
}
