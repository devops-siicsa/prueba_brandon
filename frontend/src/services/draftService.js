import { openDB } from 'idb'

const DB_NAME = 'inventory_db'
const STORE_NAME = 'drafts'

async function getDB() {
    return openDB(DB_NAME, 2, {
        upgrade(db) {
            if (!db.objectStoreNames.contains('drafts')) {
                db.createObjectStore('drafts')
            }
            if (!db.objectStoreNames.contains('offline_queue')) {
                db.createObjectStore('offline_queue', { keyPath: 'id', autoIncrement: true })
            }
        },
    })
}

export const draftService = {
    async saveDraft(key, data) {
        const db = await getDB()
        return db.put(STORE_NAME, data, key)
    },

    async getDraft(key) {
        const db = await getDB()
        return db.get(STORE_NAME, key)
    },

    async deleteDraft(key) {
        const db = await getDB()
        return db.delete(STORE_NAME, key)
    },

    async getDraftsByCompany(companyId) {
        const db = await getDB()
        const keys = await db.getAllKeys(STORE_NAME)
        const drafts = []

        for (const key of keys) {
            if (typeof key === 'string' && key.startsWith('draft_')) {
                const draft = await db.get(STORE_NAME, key)
                // Filter by companyId if provided and matches
                if (draft && draft.EmpresaId === parseInt(companyId)) {
                    drafts.push({ key, ...draft })
                }
            }
        }
        return drafts
    }
}
