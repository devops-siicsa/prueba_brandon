
*****ROLES Y PERMISOS
Esta es la definición **detallada y minuciosa** de los permisos organizada por **Rol** y desglosada por **Pantalla**, tal como lo solicitaste.

He integrado la lógica de **Multi-tenancy (Multi-entidad)**:

  * **Roles Internos (Tu Empresa):** `Scope = GLOBAL` (Ven todo).
  * **Roles Externos (Cliente):** `Scope = TENANT` (Filtrado automáticamente por el ID de su empresa).

-----

### 1\. Rol: SUPER ADMINISTRADOR (Interno / Dueño)

**Alcance (Scope):** Global (Todo el sistema, todos los clientes).
**Descripción:** Control total sobre la configuración del software, catálogos y auditoría.

  * **Pantalla: Login**

      * `auth:login` (Acceso habilitado).
      * `auth:2fa_bypass` (Opcional: Si se rompe el 2FA, puede entrar con código de recuperación).

  * [cite\_start]**Pantalla: Menú Principal** [cite: 3]

      * `menu:view_sys_config` (Ve el botón "Configuración del Sistema").
      * `menu:view_client_config` (Ve el botón "Configuración Cliente").

  * [cite\_start]**Pantalla: Panel de Control (Configuración del Sistema)** [cite: 6]

      * **Sección Empresa/Usuarios:**
          * `sys_company:manage`: Crear/Editar tus propias empresas y sedes.
          * `sys_users:manage_all`: Crear/Editar usuarios internos y asignar roles.
      * **Sección Catálogos (Procesadores, RAM, SO, etc.):**
          * `catalogs:create`: Crear nuevas marcas, tipos de RAM, Modelos de CPU.
          * [cite\_start]`catalogs:edit`: Corregir nombres o activar/desactivar opciones[cite: 10].
      * **Sección Auditoría:**
          * [cite\_start]`audit:view_full`: Ver el log completo de todo el sistema (quién borró qué, cuándo)[cite: 7].

  * [cite\_start]**Pantalla: Panel de Control (Configuración Cliente)** [cite: 14]

      * `clients:create`: Dar de alta un nuevo Cliente (NIT, Razón Social).
      * `clients:edit`: Modificar datos de facturación o dirección de cualquier cliente.
      * `clients:manage_contacts`: Crear/Editar los usuarios (contactos) de los clientes.

  * [cite\_start]**Pantalla Principal (Dashboard)** [cite: 16]

      * `dashboard:view_all`: Ve las tarjetas de **TODOS** los clientes y las empresas propias.

  * [cite\_start]**Pantalla Inventario (Listado)** [cite: 19]

      * `inventory:view_global`: Puede buscar equipos en cualquier cliente.
      * `inventory:create`: Botón "+" habilitado para cualquier empresa.
      * `inventory:export`: Descargar reportes en Excel/PDF.

  * [cite\_start]**Pantalla Equipo (Ficha Técnica)** [cite: 20]

      * **Modo Edición:** Habilitado para todos los campos.
      * `equipment:edit_sensitive`: Puede editar campos bloqueados para otros (ej: seriales, fechas de compra).
      * `history:view_hidden`: Ve incluso los logs de sistema interno.

-----

### 2\. Rol: ADMINISTRADOR (Interno / Coordinador de Operaciones)

**Alcance (Scope):** Global (Ve todos los clientes).
**Diferencia:** Es operativo. No puede tocar la "Configuración del Sistema" (catálogos base) ni borrar logs.

  * **Pantalla: Menú Principal**

      * `menu:view_client_config` (Sí, gestiona clientes).
      * `menu:view_sys_config` (BLOQUEADO o Solo Lectura).

  * **Pantalla: Panel de Control (Configuración del Sistema)**

      * **Sección Catálogos:** `catalogs:view` (Solo ve las opciones, no puede crear nuevas marcas de procesadores. Si necesita una, la pide al Super Admin).
      * **Sección Auditoría:** BLOQUEADO.

  * **Pantalla: Panel de Control (Configuración Cliente)**

      * `clients:create`: Puede ingresar nuevos clientes.
      * `clients:edit`: Puede actualizar direcciones y sedes de clientes.
      * `clients:manage_contacts`: Puede crear usuarios para los clientes.

  * **Pantalla Principal (Dashboard)**

      * `dashboard:view_all`: Ve todas las empresas.

  * **Pantalla Inventario & Equipo**

      * `inventory:create`: Sí.
      * `equipment:edit_all`: Puede editar Hardware, Software, Asignaciones.
      * `maintenance:log`: Registrar mantenimientos.

-----

### 3\. Rol: SOPORTE TÉCNICO (Interno)

**Alcance (Scope):** Global (Da soporte a todos los clientes).
**Descripción:** Su trabajo es mantener actualizada la hoja de vida de los equipos. No gestiona clientes ni contratos.

  * **Pantalla: Menú Principal**

      * Ocultos los botones de "Configuración del Sistema" y "Configuración Cliente".

  * **Pantalla Principal (Dashboard)**

      * `dashboard:view_all`: Ve todos los clientes para poder entrar a trabajar.

  * **Pantalla Inventario**

      * `inventory:create`: Sí (Puede ingresar equipos nuevos que llegan).
      * `inventory:view_global`: Busca equipos por serial en cualquier cliente.

  * **Pantalla Equipo (Ficha Técnica)**

      * [cite\_start]`equipment:edit_hardware`: Sí (Cambiar RAM, Disco)[cite: 23].
      * [cite\_start]`equipment:edit_software`: Sí (Instalar Office, Antivirus)[cite: 25].
      * `equipment:edit_user`: Sí (Reasignar equipo a otro usuario).
      * [cite\_start]`maintenance:create`: **CRÍTICO.** Botón "Aplicar Mantenimiento Preventivo" habilitado[cite: 25].
      * [cite\_start]`history:comment`: Puede agregar observaciones manuales al historial[cite: 28].
      * [cite\_start]`attachments:upload`: Subir fotos y actas[cite: 27].

-----

### 4\. Rol: ADMINISTRADOR CLIENTE (Externo)

**Alcance (Scope):** **Limitado (Tenant)**. Solo ve su propia empresa (NIT vinculado a su usuario).
**Descripción:** El gerente de sistemas del cliente. Quiere ver SU inventario y gestionar SUS sedes.

  * **Pantalla: Menú Principal**

      * `menu:view_sys_config`: BLOQUEADO (No ve catálogos globales).
      * `menu:view_client_config`: HABILITADO (Pero filtrado, solo ve "Mi Empresa").

  * **Pantalla: Panel de Control (Configuración Cliente)**

      * `clients:view_self`: Solo ve su ficha de empresa.
      * [cite\_start]`clients:edit_self_sedes`: Puede crear/editar sus propias sedes (ej: abrieron una oficina nueva)[cite: 9].
      * `clients:manage_self_contacts`: Puede crear usuarios "Soporte Cliente" para su equipo.

  * **Pantalla Principal (Dashboard)**

      * `dashboard:view_self`: Solo ve 1 Card (Su empresa). Al hacer login, podría redirigirse automáticamente al Inventario para ahorrar un clic.

  * **Pantalla Inventario**

      * `inventory:view_self`: Ve todos SUS equipos.
      * `inventory:create`: Sí (Puede ingresar sus propios equipos).

  * **Pantalla Equipo**

      * `equipment:edit_all`: Sí, gestiona su propio inventario.
      * `history:view`: Ve el historial de cambios.

-----

### 5\. Rol: SOPORTE CLIENTE / CONSULTA (Externo)

**Alcance (Scope):** **Limitado (Tenant)**.
**Descripción:** Auxiliar del cliente o auditor. Solo entra a ver qué tienen o a reportar algo básico.

  * **Pantalla: Menú Principal**

      * Sin acceso a configuraciones.

  * **Pantalla Principal**

      * Solo ve su empresa.

  * **Pantalla Inventario**

      * `inventory:view_self`: Ve la lista.
      * `inventory:create`: **BLOQUEADO** (No puede crear equipos, solo ver los existentes).

  * **Pantalla Equipo**

      * **Modo Vista:** Activo por defecto.
      * **Botón Lápiz (Editar):** **OCULTO**. No puede modificar Hardware ni Software.
      * `history:view`: Puede ver la hoja de vida.
      * `attachments:download`: Puede descargar actas, pero no borrarlas.

----
Aquí tienes la definición detallada y minuciosa para los roles de **Auditoría**, desglosada por pantalla y respetando la lógica de negocio y seguridad (Read-Only) que requiere un perfil de este tipo.

La clave de estos roles es el **Acceso de Lectura Profunda**: pueden ver cosas que otros no (como logs detallados o datos sensibles), pero **no pueden modificar absolutamente nada**.

---

### 6. Rol: AUDITOR INTERNO (SIICSA)
**Alcance (Scope):** **Global**.
**Descripción:** Auditor contratado por TU empresa (SIICSA) o un revisor fiscal interno. Su objetivo es garantizar la calidad de los datos, verificar procesos de los técnicos y asegurar que no haya corrupción de información en todo el sistema.

* **Pantalla: Login**
    * `auth:login`: Acceso estándar.
    * `auth:2fa_required`: **Obligatorio**. Los auditores manejan información sensible, deben tener seguridad alta.

* **Pantalla: Menú Principal**
    * `menu:view_sys_config`: **HABILITADO**. Necesita entrar para revisar los logs globales.
    * `menu:view_client_config`: **HABILITADO**. Necesita auditar la creación de clientes.

* **Pantalla: Panel de Control (Configuración del Sistema)**
    * **Sección Empresa/Usuarios:**
        * `sys_company:view`: Ve la configuración de SIICSA. **(Sin botón Editar)**.
        * `sys_users:view_all`: Ve la lista de usuarios y sus roles asignados para validar permisos. **(Sin botón Crear/Editar)**.
    * **Sección Catálogos (Procesadores, RAM, etc.):**
        * `catalogs:view_hidden`: Ve todos los ítems, incluso los "Inactivos/Ocultos", para validar por qué se desactivaron.
        * `catalogs:edit`: **BLOQUEADO**.
    * **Sección Auditoría (CRÍTICO):**
        * `audit:view_full`: Acceso total al Log de Auditoría del Sistema.
        * `audit:export`: Puede descargar los logs en CSV/Excel para análisis forense.
        * `audit:delete`: **BLOQUEADO ESTRICTAMENTE**.

* **Pantalla: Panel de Control (Configuración Cliente)**
    * `clients:view_list`: Ve la lista completa de todos los clientes.
    * `clients:view_details`: Entra al detalle (NIT, Dirección, Contactos) para validar veracidad.
    * `clients:edit`: **BLOQUEADO**.

* **Pantalla Principal (Dashboard)**
    * `dashboard:view_all`: Ve las tarjetas de todos los clientes.
    * `dashboard:view_stats`: Si implementas gráficas (ej: "Equipos por Cliente"), el auditor debe verlas.

* **Pantalla Inventario (Listado)**
    * `inventory:view_global`: Búsqueda global habilitada.
    * `inventory:export_bulk`: **HABILITADO**. Puede descargar el inventario masivo de todos los clientes para cruzar información.

* **Pantalla Equipo (Ficha Técnica)**
    * **Modo Vista:** Siempre activo. El botón "Lápiz" (Editar) no existe para este rol.
    * `equipment:view_sensitive`: Ve campos sensibles como Costo de Compra, Facturas, Vencimientos.
    * `history:view_full`: Ve el historial completo, incluyendo quién creó el equipo y todas las modificaciones de hardware.
    * `attachments:view_all`: Puede abrir y descargar todos los adjuntos (Facturas, Fotos de seriales).
    * `attachments:delete`: **BLOQUEADO**.

---

### 7. Rol: AUDITOR EXTERNO (CLIENTE)
**Alcance (Scope):** **Limitado (Tenant)**.
**Descripción:** Auditor contratado por el CLIENTE (ej: Revisor Fiscal de "Coca-Cola" que entra a tu software a ver SOLO los activos de "Coca-Cola"). No le interesa (y no debe ver) las otras empresas.

* **Pantalla: Login**
    * `auth:login`: Acceso estándar.

* **Pantalla: Menú Principal**
    * `menu:view_sys_config`: **BLOQUEADO**. No tiene por qué ver tus catálogos internos ni logs de otros clientes.
    * `menu:view_client_config`: **HABILITADO** (Filtrado solo a su empresa).

* **Pantalla: Panel de Control (Configuración Cliente)**
    * `clients:view_self`: Ve los datos de la empresa que está auditando (Razón Social, Sedes).
    * `clients:view_contacts`: Ve quiénes son los usuarios autorizados de esa empresa.
    * `clients:edit`: **BLOQUEADO**. No puede cambiar direcciones ni teléfonos.

* **Pantalla Principal (Dashboard)**
    * `dashboard:view_self`: Solo ve la tarjeta de su empresa.

* **Pantalla Inventario (Listado)**
    * `inventory:view_self`: Ve el listado completo de equipos de su empresa.
    * `inventory:create`: **BLOQUEADO**.
    * `inventory:export`: **HABILITADO**. Necesita sacar la data a Excel para hacer su trabajo de auditoría física (ir puesto por puesto).

* **Pantalla Equipo (Ficha Técnica)**
    * **Modo Vista:** Siempre activo. Sin opción de editar.
    * **Pestañas:**
        * **Usuario Equipo:** `view_only`. Valida quién tiene el equipo.
        * **Equipo/Hardware:** `view_only`. Valida que el hardware coincida con lo comprado.
        * **Software:** `view_only`. Valida licencias (Auditoría de legalidad de software).
        * **Adjuntos:** `attachments:view`. Ve fotos y facturas.
        * **Historial:** `history:view_tenant`. Ve los cambios realizados a ese equipo (ej: "¿Cuándo le cambiaron el disco duro?").