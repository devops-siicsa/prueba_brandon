import hashlib
import os
import mimetypes
import uuid
import traceback
import time
import threading
import asyncio
import requests
import subprocess
import pusher
import httpx
import pandas as pd
import re
import base64
import pytz
import pdfplumber
import io
import pytesseract
import shutil
import openai
from urllib.parse import urlparse
import json

from flask import Flask, send_from_directory, request, jsonify, url_for, current_app, send_file
from flask_cors import CORS
from configuracionbd import get_db_connection
from werkzeug.utils import secure_filename
from pytz import timezone
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from message_helper import (sendCustomTexto, sendCustomImage, sendCustomAudio, sendCustomDocumentos, sendCustomLista, sendCustomButtons, send_message_pni, sendTexto_PG_IG,
                            sendCustomThreeButtons, build_whatsapp_template_payload, sendCustomActionUrl, sendCustomVideo, send_message, sendCustomButtons1, send_notificacion_app)
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions, ContentSettings
from dateutil.relativedelta import relativedelta
from pdf2image import convert_from_path
from openai import AsyncOpenAI

# Configuración de Azure Blob Storage
# Tu cadena de conexión de Azure
connect_str = os.getenv("CONNECT_STR").strip()
container_name = os.getenv("CONTAINER_NAME").strip()  # Nombre del contenedor
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


app = Flask(__name__, static_folder="frontend/dist", static_url_path="/")
CORS(app)  # Habilita CORS en toda la app

load_dotenv()


ffmpegNube = 1  # 1 para app services, 0 para local

if ffmpegNube == 1:
    # Forzar el uso de FFmpeg en el app services para convertir audio o video
    ffmpeg_path = "/home/site/wwwroot/ffmpeg/bin/ffmpeg"

else:
    # Forzar el uso de FFmpeg localmente para convertir audio o video
    os.environ["PATH"] += os.pathsep + os.path.abspath("ffmpeg/bin/")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Crear la carpeta files y uploads en caso que no existe
if not os.path.exists("files"):
    os.makedirs("files")
if not os.path.exists("uploads"):
    os.makedirs("uploads")


# Configurar API Key de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')
client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))


# Ruta principal (sirve index.html)
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")


# Ruta para archivos estáticos (CSS, JS, imágenes)
"""@app.route("/<path:path>") 
def serve_vue_routes(path): 
    try: 
        return send_from_directory(app.static_folder, path) 
    except: 
        return send_from_directory(app.static_folder, "index.html")  # Redirige rutas desconocidas a Vue """

# Ruta para servir archivos estáticos y permitir SPA


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue_app(path):
    file_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/api/consql", methods=["GET", "POST"])
def consql():
    try:
        query = "SELECT * FROM usuario"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        # Imprime el stack completo en los logs de Azure
        traceback.print_exc()
        return jsonify({'status': 'error', 'data': str(e)}), 500


@app.route('/api/proxy-image')
def proxy_image():
    """Proxy simple para imágenes remotas.
    Uso: /api/proxy-image?url=<url>
    Nota: restringimos hosts para evitar que este endpoint se use como proxy abierto.
    """
    try:
        url = request.args.get('url')
        if not url:
            return jsonify({'status': 'error', 'message': 'url required'}), 400

        parsed = urlparse(url)
        hostname = parsed.hostname or ''
        # Lista blanca de hosts permitidos (agregar si es necesario)
        allowed_hosts = ['blob.core.windows.net', 'localhost', '127.0.0.1']
        if not any(h for h in allowed_hosts if h in hostname):
            return jsonify({'status': 'error', 'message': 'host not allowed'}), 403

        # Obtener la imagen
        resp = requests.get(url, stream=True, timeout=15)
        if resp.status_code != 200:
            return jsonify({'status': 'error', 'message': f'remote status {resp.status_code}'}), 502

        content = resp.content
        content_type = resp.headers.get('Content-Type') or mimetypes.guess_type(url)[0] or 'application/octet-stream'

        # Devolver la imagen con cabeceras CORS (la app ya tiene CORS habilitado pero por seguridad dejamos Origin abierto para assets)
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Cache-Control': 'public, max-age=300'
        }
        return send_file(io.BytesIO(content), mimetype=content_type, as_attachment=False, download_name=None), 200, headers

    except Exception as e:
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 500


pusher_client = pusher.Pusher(
    app_id=os.getenv("PUSHER_APP_ID"),        # Reemplaza con tu app_id
    key=os.getenv("PUSHER_KEY"),          # Reemplaza con tu key
    secret=os.getenv("PUSHER_SECRET"),    # Reemplaza con tu secret
    # Reemplaza con tu cluster (ej. 'mt1')
    cluster=os.getenv("PUSHER_CLUSTER"),
    ssl=True
)


# ========================================================================================================
# RUTAS DE LA API
# ========================================================================================================
# Ruta de login
# Esta ruta recibe el usuario y la clave, y retorna los datos del usuario si es correcto
@app.route("/api/login", methods=["GET", "POST"])
def login():
    try:
        ipadd = request.remote_addr
        data = request.get_json()
        usuario = data.get('usuario', '')
        clave = data.get('clave', '')
        # Codificar la clave a MD5
        clave = hashlib.md5(clave.encode()).hexdigest()

        query = "EXEC procLogin ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (usuario, clave, ipadd))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        # Imprime el stack completo en los logs de Azure
        traceback.print_exc()
        return jsonify({'status': 'error', 'data': str(e)}), 500


# Para logueo dedicada de la app movil
@app.route("/api/loginApp", methods=["GET", "POST"])
def loginApp():
    try:
        ipadd = request.remote_addr
        data = request.get_json()
        usuario = data.get('usuario', '')
        clave = data.get('clave', '')
        token = data.get('token', '')
        # Codificar la clave a MD5
        clave = hashlib.md5(clave.encode()).hexdigest()

        query = "EXEC procLoginApp ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (usuario, clave, ipadd, token))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        # Imprime el stack completo en los logs de Azure
        traceback.print_exc()
        return jsonify({'status': 'error', 'data': str(e)}), 500


# Crear nueva oportunidad
# Esta ruta recibe los datos de la oportunidad y lo crea en la base de datos, retorna el id de la oportunidad creada y el id del cliente asociado
@app.route("/api/newproccom", methods=["GET", "POST"])
def newproccom():
    try:
        data = request.get_json()
        idcliente = int(data.get('idcliente', 0))
        idservicio = int(data.get('idservicio', 0))
        valor_proy = int(data.get('valor_proy', 0))
        observacion = data.get('observacion', '')
        idmedio = int(data.get('idmedio', 0))
        idcom = int(data.get('idcom', 0))
        idcampania = int(data.get('idcampania', 0))

        query = "EXEC procCrearOportunidad ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idcliente, idservicio, valor_proy,
                       observacion, idmedio, idcom, idcampania))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


# Crear registro actividad del proceso comercial. [ Se recibe un formdata ]
# Esta ruta recibe los datos de la actividad del proceso comercial y lo crea en la base de datos
@app.route("/api/newproccomact", methods=["GET", "POST"])
def newproccomact():
    try:
        """data = request.get_json()
        idprocom = int(data.get('procom', 0))
        idcli = int(data.get('cli', 0))
        idactividad = int(data.get('act', 0))
        observaciones = data.get('obs', '')
        estado = int(data.get('estado', 0))
        rut = data.get('rut', '')
        fecha_prox_seguimiento = data.get('fpseg', '')
        idseguimiento = int(data.get('idseg', 0))
        idserv = int(data.get('idserv', 0))"""

        idprocom = request.form.get('procom')
        idactividad = request.form.get('act')
        observaciones = request.form.get('obs')
        estado = request.form.get('estado')
        fecha_prox_seguimiento = request.form.get('fpseg')
        idseguimiento = request.form.get('idseg')
        idcom = request.form.get('idcom')
        cosproy = request.form.get('cosproy')
        idserv = request.form.get('idserv')
        rutarut = request.form.get('rutarut', '')  # Inicializar variable rut
        # Inicializar variable cotiza
        rutacot = request.form.get('rutacot', '')
        obs_seg = request.form.get('obs_seg')  # Observaciones de seguimiento

        # Registrar la actividad del proceso comercial en la base de datos
        query = "EXEC procRegistrarProcesoActividad ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idprocom, idactividad, observaciones, estado,
                       fecha_prox_seguimiento, idseguimiento, idcom, rutarut, rutacot, cosproy, idserv, obs_seg))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


# Crear registro actividad del proceso comercial. [ Se recibe un formdata ]
# Esta ruta recibe los datos de la actividad del proceso comercial y lo crea en la base de datos
@app.route("/api/cargaproccomact", methods=["GET", "POST"])
def cargaproccomact():
    try:
        data = request.get_json()
        idprocom = int(data.get('idproccom', 0))

        # Registrar la actividad del proceso comercial en la base de datos
        query = "EXEC procBuscarProcesoActividad ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idprocom))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


# Crear un nuevo prospecto
# Esta ruta recibe los datos del prospecto y lo crea en la base de datos
@app.route("/api/newprospecto", methods=["GET", "POST"])
def newprospecto():
    try:
        data = request.get_json()
        nit = data.get('nit', '')
        razon_social = data.get('razon_social', '')
        tipo_identif = int(data.get('tipo_identif', 0))
        tipo_emp = int(data.get('tipo_emp', 0))
        sector = int(data.get('sector', 0))
        direccion = data.get('direccion', '')
        dpto = int(data.get('dpto', 0))
        ciudad = int(data.get('ciudad', 0))
        web = data.get('web', '')
        correo = data.get('correo', '')
        telefono1 = data.get('telefono1', '')
        telefono2 = data.get('telefono2', '')
        comercial = int(data.get('comercial', 0))
        idserv = int(data.get('servicio', 0))
        # Nuevo campo activo, por defecto 1
        activo = int(data.get('activo', 1))
        mercadeo = int(data.get('mercadeo', 0))
        # Imprimir datos recibidos para depuración
        print(f"Datos recibidos: {data}")

        query = "EXEC procCrearProspecto ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (nit, razon_social, tipo_identif, tipo_emp, sector,
                       direccion, dpto, ciudad, web, correo, telefono1, telefono2, comercial, idserv, activo, mercadeo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500

# Editar un nuevo prospecto
# Esta ruta recibe los datos del prospecto y lo edita en la base de datos


@app.route("/api/editprospecto", methods=["GET", "POST"])
def editprospecto():
    try:
        data = request.get_json()
        nit = data.get('nit', '')
        razon_social = data.get('razon_social', '')
        tipo_identif = int(data.get('tipo_identif', 0))
        tipo_emp = int(data.get('tipo_emp', 0))
        sector = int(data.get('sector', 0))
        direccion = data.get('direccion', '')
        dpto = int(data.get('dpto', 0))
        ciudad = int(data.get('ciudad', 0))
        web = data.get('web', '')
        correo = data.get('correo', '')
        telefono1 = data.get('telefono1', '')
        telefono2 = data.get('telefono2', '')
        comercial = int(data.get('comercial', 0))
        id = int(data.get('id', 0))
        # Nuevo campo activo, por defecto 1
        activo = int(data.get('activo', 1))
        # Imprimir datos recibidos para depuración
        print(f"Datos recibidos: {data}")

        query = "EXEC procEditarProspecto ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (nit, razon_social, tipo_identif, tipo_emp, sector,
                       direccion, dpto, ciudad, web, correo, telefono1, telefono2, comercial, id, activo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500

# Crear un nuevo contacto prospecto
# Esta ruta recibe los datos del contacto prospecto y lo crea en la base de datos


@app.route("/api/newprospectocontacto", methods=["GET", "POST"])
def newprospectocontacto():
    try:
        data = request.get_json()
        nombre = data.get('nombre', '')
        apellido = data.get('apellido', '')
        cargo = int(data.get('cargo', 0))
        correo = data.get('correo', '')
        celular = data.get('celular', '')
        extension = data.get('extension', '')
        idemp = int(data.get('idemp', 0))

        query = "EXEC procCrearProspectoContacto ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (nombre, apellido, cargo,
                       correo, celular, extension, idemp))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500

# Editar un contacto prospecto
# Esta ruta recibe los datos del contacto prospecto y lo edita en la base de datos


@app.route("/api/editprospectocontacto", methods=["GET", "POST"])
def editprospectocontacto():
    try:
        data = request.get_json()
        nombre = data.get('nombre', '')
        apellido = data.get('apellido', '')
        cargo = int(data.get('cargo', 0))
        correo = data.get('correo', '')
        celular = data.get('celular', '')
        extension = data.get('extension', '')
        id = int(data.get('id', 0))

        query = "EXEC procEditarProspectoContacto ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (nombre, apellido, cargo,
                       correo, celular, extension, id))

        cursor.commit()  # Confirmar los cambios en la base de datos

        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        return {'status': 'success', 'data': id}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


# Esta ruta recibe e inserta los comentarios al activar o desactivar un prospecto

@app.route("/api/comentariosActivoProspecto", methods=["GET", "POST"])
def comentariosActivoProspecto():
    try:
        data = request.get_json()
        idUsu = int(data.get('idUsu', 0))
        comentarios = data.get('comentarios', '')
        idProspecto = int(data.get('idProspecto', 0))
        activo = int(data.get('activo', 0))

        query = "EXEC procComentariosActivoProspecto ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idUsu, comentarios, idProspecto, activo))

        cursor.commit()  # Confirmar los cambios en la base de datos

        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        return {'status': 'success', 'data': idUsu}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500

# Esta ruta carga el historial de activaciones y desactivaciones de un prospecto


@app.route("/api/historialActivoProspecto", methods=["GET", "POST"])
def historialActivoProspecto():
    try:
        data = request.get_json()
        idUsu = int(data.get('idUsu', 0))
        idProspecto = int(data.get('idProspecto', 0))

        query = "EXEC procHistorialActivoProspecto ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idUsu, idProspecto))

        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


# cargarTipoIdentificacion
# Esta ruta retorna los tipos de identificación disponibles
@app.route("/api/cargarti", methods=["GET", "POST"])
def cargarti():
    try:
        query = "SELECT id, nombre FROM tipo_identificacion ORDER BY nombre"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargarTipoEmpresa
# Esta ruta retorna los tipos de empresa disponibles


@app.route("/api/cargarte", methods=["GET", "POST"])
def cargarte():
    try:
        query = "SELECT id, nombre FROM tipo_persona ORDER BY nombre"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargarSector
# Esta ruta retorna los sectores disponibles


@app.route("/api/cargarse", methods=["GET", "POST"])
def cargarse():
    try:
        query = "SELECT id, nombre FROM sector ORDER BY nombre"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargarDepartamento
# Esta ruta retorna los departamentos disponibles


@app.route("/api/cargarde", methods=["GET", "POST"])
def cargarde():
    try:
        query = "SELECT id, nombre FROM departamento"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargarCiudad con iddpto
# Esta ruta recibe un id de departamento y retorna las ciudades asociadas a ese departamento


@app.route("/api/cargarci", methods=["GET", "POST"])
def cargarci():
    try:
        data = request.get_json()
        iddpto = int(data.get('iddpto', 0))
        query = "EXEC procBuscarCiudad ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (iddpto))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status22': 'error', 'message': str(e)}), 500

    return {'status': 'success', 'data': datos}, 200

# cargarProspectoEmpresa
# Esta ruta retorna los prospectos de empresa disponibles


@app.route("/api/cargarpp", methods=["GET", "POST"])
def cargarpp():
    try:
        data = request.get_json()
        idprosp = data.get('idusu', 0)

        query = "EXEC procProspectosComercial ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, idprosp)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargar Estados
# Esta ruta retorna los estados comerciales disponibles


# Cargar campañas
# Esta ruta retorna las campañas para prospeccion telefonica
@app.route("/api/cargarcamptel", methods=["GET", "POST"])
def cargarcamptel():
    try:
        data = request.get_json()
        idusu = data.get('idusu', 0)
        tipo = data.get('tipo', 0)

        query = "EXEC procCargarCampanasTelefónicas ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idusu, tipo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# cargar Estados
# Esta ruta retorna los estados comerciales disponibles


@app.route("/api/cargares", methods=["GET", "POST"])
def cargares():
    try:
        query = "SELECT id, nombre FROM estado_comercial ORDER BY id ASC"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargar Servicios
# Esta ruta retorna los servicios disponibles


@app.route("/api/cargarsv", methods=["GET", "POST"])
def cargarsv():
    try:
        query = "SELECT id, nombre FROM producto_comercial"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# cargar tipos de motivos
# Esta ruta retorna los motivos disponibles para las prospecciones telefónicas
@app.route("/api/cargarmotivos", methods=["GET", "POST"])
def cargarmotivos():
    try:
        query = "EXEC procMotivosProspeccion"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# cargar Categoría Cargos
# Esta ruta retorna los categorias de cargos disponibles
@app.route("/api/cargarcc", methods=["GET", "POST"])
def cargarcc():
    try:
        query = "SELECT id, nombre FROM categoria_cargo_cliente ORDER BY nombre"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# cargar Cargos con idcargo
# Esta ruta recibe un id de categoria cargo y retorna los cargos asociadas a esa categoria de cargo
@app.route("/api/cargarca", methods=["GET", "POST"])
def cargarca():
    try:
        data = request.get_json()
        idcat = int(data.get('idcat', 0))
        query = "EXEC procBuscarCargo ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idcat))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status22': 'error', 'message': str(e)}), 500


# Mostrar el comercial asignado a esa empresa
@app.route("/api/empcomer", methods=["GET", "POST"])
def empcomer():
    try:
        data = request.get_json()
        idemp = int(data.get('idemp', 0))
        idcom = int(data.get('idcom', 0))
        query = "EXEC procEmpresaComercial ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idemp, idcom))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargar Lista de Estados Iniciales. Tambien si ha hecho filtros en la pantalla inicial
# Esta ruta retorna todos los datos para la carga inicial de comercial


@app.route("/api/cargarlisest", methods=["GET", "POST"])
def cargarlisest():
    try:
        data = request.get_json(silent=True)
        fecini = ''
        fecfin = ''
        idprosp = 0
        idserv = 0
        idmedio = 0
        idusu = 0
        if data:
            data = request.get_json()
            fecini = data.get('fecini', '')
            fecfin = data.get('fecfin', '')
            idprosp = int(data.get('idprosp', 0))
            idmedio = int(data.get('idmedio', 0))
            idserv = int(data.get('idserv', 0))
            # Agregar idusu para filtrar por usuario si es necesario
            idusu = int(data.get('idusu', 0))

        query = "EXEC procCargaInicialComercial ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(
            query, (fecini, fecfin, idprosp, idmedio, idserv, idusu))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargarlispend", methods=["GET", "POST"])
def cargarlispend():
    try:
        data = request.get_json()
        idusu = int(data.get('idusu', 0))

        query = "EXEC procCargaPendientesComercial ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idusu))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargarProcSinAct", methods=["GET", "POST"])
def cargarProcSinAct():
    try:
        data = request.get_json(silent=True)
        idusu = 0
        if data:
            data = request.get_json()
            idusu = int(data.get('idusu', 0))

        query = "EXEC procCargaProcesosSinActividad ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idusu,))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargarlispropest", methods=["GET", "POST"])
def cargarlispropest():
    try:
        data = request.get_json()
        fecini = data.get('fecini', '')
        fecfin = data.get('fecfin', '')
        idprosp = int(data.get('idprosp', 0))
        idserv = int(data.get('idserv', 0))
        idusu = int(data.get('idusu', 0))
        idest = int(data.get('idest', 0))
        idmedio = int(data.get('idmedio', 0))

        query = "EXEC procCargaProspEsta ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (fecini, fecfin, idprosp,
                       idserv, idusu, idest, idmedio))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargarprosppend", methods=["GET", "POST"])
def cargarprosppend():
    try:
        data = request.get_json()
        idproccom = int(data.get('idproccom', 0))

        query = "EXEC procCargaPendientesComercialProsp ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idproccom))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargarProspectos", methods=["GET", "POST"])
def cargarProspectos():
    try:
        query = "EXEC procCargaProspectos"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)  # Pasar el parámetro iddpto como una tupla

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Proceso para cargar los contactos y usarlos en el chat


@app.route("/api/contactos", methods=["GET", "POST"])
def contactos():
    try:
        query = "EXEC procCargaProspectosContacto"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)  # Pasar el parámetro iddpto como una tupla

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/validarnitraz", methods=["GET", "POST"])
def validarnitraz():
    try:
        data = request.get_json()
        nit = data.get('nit', '')
        raz = data.get('raz', '')

        query = "EXEC procValidarNitRaz ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (nit, raz))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/histprocom", methods=["GET", "POST"])
def histprocom():
    try:
        data = request.get_json()
        idproccom = data.get('idproccom', 0)
        idusu = data.get('idusu', 0)

        query = "EXEC procBuscarHistorico ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idusu, idproccom))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargaproscon", methods=["GET", "POST"])
def cargaproscon():
    try:
        data = request.get_json()
        idprosp = data.get('idprosp', 0)

        query = "EXEC procInfoProspectoContacto ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, idprosp)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargarPQR
# Esta ruta retorna los pqrs existentes


@app.route("/api/cargarpqrs", methods=["GET", "POST"])
def cargarpqrs():
    try:
        data = request.get_json()
        idusu = int(data.get('idusu', 0))

        query = "EXEC procCargarPQR ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idusu,))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargar historico de pqr
# Esta ruta retorna si el histórtico de un idpqr


@app.route("/api/pqrhist", methods=["GET", "POST"])
def pqrhist():
    try:
        data = request.get_json()
        id = int(data.get('idpqr', 0))
        query = "EXEC procCargarPQRHistorico ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# cargarUsuarios
# Esta ruta retorna los usuarios que hacen uso del aplicativo

@app.route("/api/cargausus", methods=["GET", "POST"])
def cargausus():
    try:
        data = request.get_json()
        idusu = data.get('idusu', 0)
        tipo = data.get('tipo', 0)  # Tipo de usuario, si es necesario
        query = "EXEC procCargaUsuarios ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idusu, tipo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# cargar proyectos
# Esta ruta retorna los proyectos que pertenecen al comercial


@app.route("/api/cargarproyectos", methods=["GET", "POST"])
def cargarproyectos():
    try:
        data = request.get_json()
        idComercial = data.get('idComercial', 0)
        query = "EXEC procCargaProyectos ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idComercial))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Procesar valor de proyecto


@app.route("/api/saveValorProyecto", methods=["GET", "POST"])
def saveValorProyecto():
    try:
        data = request.get_json()
        id = int(data.get('id', 0))
        valor_proyecto = int(data.get('valor_proyecto', 0))
        query = "EXEC procProcesarValorProyecto ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (id, valor_proyecto))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# crearUsuario
# Esta ruta crea usuario para el manejo dle sistema

@app.route("/api/newusu", methods=["GET", "POST"])
def newusu():
    try:
        data = request.get_json()
        ced = data.get('ced', '')
        nom = data.get('nom', '')
        ape = data.get('ape', '')
        cue = data.get('cue', '')
        ema = data.get('ema', '')
        cel = data.get('cel', '')
        act = int(data.get('act', 0))
        sta = int(data.get('sta', 0))
        met = int(data.get('met', 0))
        perfil = int(data.get('perfil', 0))
        admin = int(data.get('admin', 0))
        clave = data.get('clave', '')

        query = "EXEC procCrearUsuario ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (ced, nom, ape, cue, ema,
                       cel, act, sta, met, perfil, admin, clave))
        cursor.commit()  # Confirmar los cambios en la base de datos

        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        return {'status': 'success', 'data': 0}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# editarUsuario
# Esta ruta edita usuario según el id de usuario


@app.route("/api/editusu", methods=["GET", "POST"])
def editusu():
    try:
        data = request.get_json()
        idu = int(data.get('idu', 0))
        ced = data.get('ced', '')
        nom = data.get('nom', '')
        ape = data.get('ape', '')
        cue = data.get('cue', '')
        ema = data.get('ema', '')
        cel = data.get('cel', '')
        act = int(data.get('act', 0))
        sta = int(data.get('sta', 0))
        met = int(data.get('met', 0))
        perfil = int(data.get('perfil', 0))
        admin = int(data.get('admin', 0))
        clave = data.get('clave', '')

        query = "EXEC procEditarUsuario ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idu, ced, nom, ape,
                       cue, ema, cel, act, sta, met, perfil, admin, clave))
        cursor.commit()  # Confirmar los cambios en la base de datos

        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        return {'status': 'success', 'data': 0}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# validar celular prospecto_contacto
# Esta ruta retorna si el número de celular ya está asignado a otro usuario o no
# devuelve variable res, donde 0 es el celular se puede usar, 1 es el celular ya está asignado a otro


@app.route("/api/validarcel", methods=["GET", "POST"])
def validarcel():
    try:
        data = request.get_json()
        id = int(data.get('id', 0))
        cel = data.get('cel', '')
        query = "EXEC procValidarCelular ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (cel, id))
        resultados = cursor.fetchall()  # Obtener los resultados

        # Convertir los resultados en una lista de diccionarios (opcional)
        columnas = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columnas, row)) for row in resultados]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# validar y editar contraseña usuario
# Esta ruta retorna un mensaje de respuesta según la validación de la contraseña del usuario

@app.route("/api/cambiarclave", methods=["GET", "POST"])
def cambiarclave():
    try:
        data = request.get_json()
        id = int(data.get('idusu', 0))
        claveActual = data.get('claveActual', '')
        nuevaClave = data.get('nuevaClave', '')
        query = "EXEC procCambiarClave ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (id, claveActual, nuevaClave))
        resultados = cursor.fetchall()  # Obtener los resultados

        # Convertir los resultados en una lista de diccionarios (opcional)
        columnas = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columnas, row)) for row in resultados]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# validar telefonos a enviar a una campaña para saber si ya se les ha enviado una previamente dentro de un lapso de 24 horas


@app.route("/api/validar_numeros_campania", methods=["GET", "POST"])
def validar_numeros_campania():
    try:
        data = request.get_json()
        telefonos = data.get('telefonos', [])

        if not telefonos:
            return jsonify({'status': 'error', 'message': 'No se enviaron números'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        # 1️⃣ Crear tabla temporal
        cursor.execute("CREATE TABLE #tempTelefonos (numero NVARCHAR(20));")

        # 2️⃣ Insertar todos los números de una vez
        cursor.fast_executemany = True
        datos = [(str(t),) for t in telefonos]
        cursor.executemany("INSERT INTO #tempTelefonos (numero) VALUES (?);", datos)

        # 3️⃣ Ejecutar el procedimiento (sola instrucción → sí devuelve resultados)
        cursor.execute("EXEC procValidarNumerosCampania;")

        # 4️⃣ Leer los resultados
        resultados = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]
        resultados_dict = [dict(zip(columnas, fila)) for fila in resultados]

        conn.close()
        return jsonify({'status': 'success', 'data': resultados_dict}), 200

    except Exception as e:
        print(f"Error en validar_numeros_campania: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
# Validacion sin post
def validar_numeros_campania2(numero):
    try:

        # por cada posicion del array de teléfonos, se ejecuta el procedimiento almacenado
        resultados_finales = []
        query = "EXEC procValidarNumerosCampania2 ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (numero,))
        resultados = cursor.fetchall()  # Obtener los resultados

        # Convertir los resultados en una lista de diccionarios (opcional)
        columnas = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columnas, row)) for row in resultados]
        resultados_finales.extend(resultados_dict)
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión
        
        res = resultados_finales[0]['novalido']

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return res
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga filtros destinatarios
@app.route("/api/cargaFiltros", methods=["GET", "POST"])
def cargaFiltros():
    try:

        query = "EXEC procCargaFiltros"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga sector
@app.route("/api/cargaSector", methods=["GET", "POST"])
def cargaSector():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))

        query = "EXEC procCargaSector ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Procesar sector, ya sea editar o crear


@app.route("/api/saveSector", methods=["GET", "POST"])
def saveSector():
    try:
        data = request.get_json(silent=True)
        id = 0
        nombre = ''
        tipo = 0  # 0: Editar, 1: Nuevo

        if data:
            data = request.get_json()
            id = int(data.get('id', 0))
            nombre = data.get('nombre', '')
            tipo = int(data.get('tipo', 0))

        query = "EXEC procProcesarSector ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id, nombre, tipo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga productos
@app.route("/api/cargaProducto", methods=["GET", "POST"])
def cargaProducto():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))

        query = "EXEC procCargaProducto ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga sub productos
@app.route("/api/cargarSubProductos", methods=["GET", "POST"])
def cargarSubProductos():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('id', 0))

        query = "EXEC procCargaSubProducto ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar producto, ya sea editar o crear
@app.route("/api/saveProducto", methods=["GET", "POST"])
def saveProducto():
    try:
        data = request.get_json(silent=True)
        id = 0
        nombre = ''
        tipo = 0  # 0: Editar, 1: Nuevo
        descripcion = ''

        if data:
            data = request.get_json()
            id = int(data.get('id', 0))
            nombre = data.get('nombre', '')
            tipo = int(data.get('tipo', 0))
            descripcion = data.get('descripcion', '')

        query = "EXEC procProcesarProducto ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id, nombre, tipo, descripcion))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar la ficha tecnica del producto
@app.route("/api/uploadFichaTecnica", methods=["GET", "POST"])
def uploadFichaTecnica():
    try:
        from dateutil.relativedelta import relativedelta
        container_client = blob_service_client.get_container_client(
            container_name)
        try:
            container_client.create_container()
        except Exception:
            pass  # Si ya existe, no hace nada

        if "ficha_tecnica" not in request.files:
            return jsonify({"error": "No file part"}), 400

        id = request.form.get('id')
        file = request.files.get('ficha_tecnica', None)
        carpeta = "fichas_tecnicas"

        # Procesar file si existe y tiene nombre
        if file and file.filename:
            try:
                fileName = f"{carpeta}/{id}-{file.filename}"
                blob_client = container_client.get_blob_client(fileName)
                blob_client.upload_blob(file, overwrite=True)
                sas_token_rut = generate_blob_sas(
                    account_name=blob_service_client.account_name,
                    container_name=container_name,
                    blob_name=fileName,
                    account_key=blob_service_client.credential.account_key,
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + relativedelta(years=10)
                )
                urlFile = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{fileName}?{sas_token_rut}"
            except Exception as e:
                print(f"❌ Error al subir fileRUT: {e}")

        query = "EXEC procUpdateUrlFichaTecnica ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id, urlFile))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar el archivo de intenciones
@app.route("/api/uploadIntencionesIA", methods=["GET", "POST"])
def uploadIntencionesIA():
    try:
        from dateutil.relativedelta import relativedelta
        container_client = blob_service_client.get_container_client(
            container_name)
        try:
            container_client.create_container()
        except Exception:
            pass  # Si ya existe, no hace nada

        if "file_intencion" not in request.files:
            return jsonify({"error": "No file part"}), 400

        id = request.form.get('id')
        file = request.files.get('file_intencion', None)
        carpeta = "pqr/intenciones_ia"

        # Procesar file si existe y tiene nombre
        if file and file.filename:
            try:
                fileName = f"{carpeta}/{id}-{file.filename}"
                blob_client = container_client.get_blob_client(fileName)
                blob_client.upload_blob(file, overwrite=True)
                sas_token_rut = generate_blob_sas(
                    account_name=blob_service_client.account_name,
                    container_name=container_name,
                    blob_name=fileName,
                    account_key=blob_service_client.credential.account_key,
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + relativedelta(years=10)
                )
                urlFile = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{fileName}?{sas_token_rut}"
            except Exception as e:
                print(f"❌ Error al subir fileRUT: {e}")

        query = "EXEC procUpdateUrlIntencionIA ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id, urlFile))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga estado comercial
@app.route("/api/cargaEstadoComercial", methods=["GET", "POST"])
def cargaEstadoComercial():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))

        query = "EXEC procCargaEstadoComercial ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar estado comercial, ya sea editar o crear
@app.route("/api/saveEstadoComercial", methods=["GET", "POST"])
def saveEstadoComercial():
    try:
        data = request.get_json(silent=True)
        id = 0
        nombre = ''
        tipo = 0  # 0: Editar, 1: Nuevo

        if data:
            data = request.get_json()
            id = int(data.get('id', 0))
            nombre = data.get('nombre', '')
            tipo = int(data.get('tipo', 0))

        query = "EXEC procProcesarEstadoComercial ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id, nombre, tipo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga prioridades
@app.route("/api/cargaPrioridad", methods=["GET", "POST"])
def cargaPrioridad():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))

        query = "EXEC procCargaPrioridades ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar prioridades, ya sea editar o crear
@app.route("/api/savePrioridad", methods=["GET", "POST"])
def savePrioridad():
    try:
        data = request.get_json(silent=True)
        id = 0
        nombre = ''
        tipo = 0  # 0: Editar, 1: Nuevo

        if data:
            data = request.get_json()
            id = int(data.get('id', 0))
            nombre = data.get('nombre', '')
            tipo = int(data.get('tipo', 0))

        query = "EXEC procProcesarPrioridades ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id, nombre, tipo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga Ubicaciones
@app.route("/api/cargaUbi", methods=["GET", "POST"])
def cargaUbi():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))

        query = "EXEC procCargaUbicaciones ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga ciudades
@app.route("/api/cargaCiudades", methods=["GET", "POST"])
def cargaCiudades():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))
            depto = int(data.get('depto', 0))

        query = "EXEC procCargaCiudades ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id, depto)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar ubicaciones, ya sea editar o crear
@app.route("/api/saveUbicacion", methods=["GET", "POST"])
def saveUbicacion():
    try:
        data = request.get_json(silent=True)

        if data:
            data = request.get_json()
            tipo = int(data.get('tipo', 0))
            tipoEdit = int(data.get('tipoEdit', 0))
            tipoCreate = int(data.get('tipoCreate', 0))
            idDeptoEdit = int(data.get('idDeptoEdit', 0))
            idDepto = int(data.get('idDepto', 0))
            idCiudad = int(data.get('idCiudad', 0))
            nombreDeptoEdit = data.get('nombreDeptoEdit', '')
            nombreCiudadEdit = data.get('nombreCiudadEdit', '')
            nombreDepto = data.get('nombreDepto', '')
            nombreCiudad = data.get('nombreCiudad', '')

        query = "EXEC procProcesarUbicacion ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (tipo, tipoEdit, tipoCreate, idDeptoEdit, idDepto, idCiudad,
                       nombreDeptoEdit, nombreCiudadEdit, nombreDepto, nombreCiudad))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga Cargos
@app.route("/api/cargaCargos", methods=["GET", "POST"])
def cargaCargos():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))

        query = "EXEC procCargaCargos ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga cargo x categoria
@app.route("/api/cargaCargosxCat", methods=["GET", "POST"])
def cargaCargosxCat():
    try:
        data = request.get_json(silent=True)
        id = 0
        if data:
            data = request.get_json()
            id = int(data.get('idusu', 0))
            cat = int(data.get('cat', 0))

        query = "EXEC procCargaCargosxCat ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, id, cat)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Carga los perfiles para la configuracion de usuarios
@app.route("/api/cargaPerfiles", methods=["GET", "POST"])
def cargaPerfiles():
    try:

        query = "EXEC procCargaPerfiles"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar cargos, ya sea editar o crear
@app.route("/api/saveCargo", methods=["GET", "POST"])
def saveCargo():
    try:
        data = request.get_json(silent=True)

        if data:
            data = request.get_json()
            tipo = int(data.get('tipo', 0))
            tipoEdit = int(data.get('tipoEdit', 0))
            tipoCreate = int(data.get('tipoCreate', 0))
            idCat = int(data.get('idCat', 0))
            idCargo = int(data.get('idCargo', 0))
            nombreCatEdit = data.get('nombreCatEdit', '')
            nombreCargoEdit = data.get('nombreCargoEdit', '')
            nombreCat = data.get('nombreCat', '')
            nombreCargo = data.get('nombreCargo', '')

        query = "EXEC procProcesarCargo ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (tipo, tipoEdit, tipoCreate, idCat, idCargo,
                       nombreCatEdit, nombreCargoEdit, nombreCat, nombreCargo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Procesar cargos, ya sea editar o crear


@app.route("/api/savePqrRespuesta", methods=["GET", "POST"])
def savePqrRespuesta():
    try:
        id = request.form.get('id')
        res = request.form.get('res')
        est = request.form.get('est')
        prio = request.form.get('prio')
        idusu = request.form.get('idusu')
        asignado = request.form.get('asignado')
        escalado = request.form.get('escalado')

        query = "EXEC procCrearPqrRespuesta ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id, res, est, prio, idusu, asignado, escalado))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# --- Endpoint para subir archivos de pqr ---
@app.route("/api/savePqrFiles", methods=["POST"])
def savePqrFiles():

    # Procesar todos los archivos enviados como 'files' en el FormData

    try:
        from dateutil.relativedelta import relativedelta
        container_client = blob_service_client.get_container_client(
            container_name)
        try:
            container_client.create_container()
        except Exception:
            pass  # Si ya existe, no hace nada

        archivos = request.files.getlist(
            'files') or request.files.getlist('files[]')
        id = request.form.get('id')
        if not archivos or len(archivos) == 0:
            return jsonify({"error": "No se recibieron archivos en 'files'"}), 400
        if not id:
            return jsonify({"error": "No se recibió el id en formdata"}), 400

        carpeta = "pqr/respuestas"

        archivos_subidos = []
        for archivo in archivos:
            if archivo.filename == '':
                continue
            # Anteponer el id al nombre del archivo
            nuevo_nombre = f"{carpeta}/{id}-{archivo.filename}"
            try:
                blob_client = container_client.get_blob_client(nuevo_nombre)
                blob_client.upload_blob(archivo, overwrite=True)
                sas_token = generate_blob_sas(
                    account_name=blob_service_client.account_name,
                    container_name=container_name,
                    blob_name=nuevo_nombre,
                    account_key=blob_service_client.credential.account_key,
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + relativedelta(years=10)
                )
                url_segura = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{nuevo_nombre}?{sas_token}"
                archivos_subidos.append({
                    "filename": nuevo_nombre,
                    "url": url_segura
                })
            except Exception as e:
                print(f"❌ Error al subir el archivo {nuevo_nombre}: {e}")

        if not archivos_subidos:
            return jsonify({"error": "No se pudo subir ningún archivo"}), 500

        return jsonify({
            "message": "Archivos subidos correctamente",
            "archivos": archivos_subidos
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/savePqr", methods=["GET", "POST"])
def savePqr():
    try:
        idcli = request.form.get('idcli')
        estado = request.form.get('estado')
        asignado = request.form.get('asignado', 0)
        prioridad = request.form.get('prioridad')
        descripcion = request.form.get('descripcion')
        respuesta = request.form.get('respuesta')
        idusuario = request.form.get('idusu')
        idEscalado = request.form.get('idEscalado', None)
        idSubcategoriapqr = request.form.get('idSubcategoriapqr', None)
        idCategoriapqr = request.form.get('idCategoriapqr', None)

        query = "EXEC procCrearPqr ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            query,( idcli, estado, prioridad, descripcion, respuesta, idusuario, asignado, idEscalado, idSubcategoriapqr, idCategoriapqr)
        )

        # Convertir resultados en diccionarios
        columns = [column[0] for column in cursor.description]
        resultados_dict = [
            dict(zip(columns, row)) for row in cursor.fetchall()
        ]

        cursor.close()
        conn.close()

        return {'status': 'success', 'data': resultados_dict}, 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# --- Endpoint para actualizar las urls de la respuesta de pqr ---
@app.route("/api/updatePqrFilesUrl", methods=["POST"])
def updatePqrFilesUrl():

    try:
        idRespuesta = request.form.get('idRespuesta')
        urls = request.form.get('urls')

        query = "EXEC procUpdatePqrResArchivos ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idRespuesta, urls))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/exportarDatosPQR", methods=["GET", "POST"])
def exportarDatosPQR():
    try:
        query = "EXEC procInformeGeneralPqr"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()
        conn.close()

        # Crear el archivo Excel en memoria (sin guardarlo en disco)
        df = pd.DataFrame(resultados_dict)

        from io import BytesIO
        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        # Retornar el archivo como adjunto
        return send_file(
            output,
            as_attachment=True,
            download_name="datos_pqr.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar Pedidos
@app.route("/api/cargarPedidos", methods=["GET", "POST"])
def cargarPedidos():
    try:

        query = "EXEC procCargarPedidos"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procesar pedidos, ya sea editar o crear
@app.route("/api/guardarPedido", methods=["GET", "POST"])
def guardarPedido():
    try:
        data = request.get_json(silent=True)

        if data:
            data = request.get_json()
            empresaId = int(data.get('empresaId', 0))
            contactoId = int(data.get('contactoId', 0))
            servicioId = int(data.get('servicioId', 0))
            cantidad = int(data.get('cantidad', 0))
            detalle = data.get('detalle', '')
            comercialId = int(data.get('comercialId', ''))
            idpedido = 0

        query = "EXEC procProcesoPedido ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (empresaId, contactoId, servicioId,
                       cantidad, detalle, comercialId, idpedido))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar los datos de las campañas para su respectivo informe
@app.route("/api/informesCampanias", methods=["GET", "POST"])
def informesCampanias():
    try:
        query = "EXEC procInformeCampanias"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)  # Pasar el parámetro iddpto como una tupla

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

import time

@app.route("/api/registros", methods=["GET", "POST"])
def get_registros():
    start = time.time()
    query = "EXEC procInformeCampanias"
    conn = get_db_connection()  # Obtener conexión a la base de datos
    cursor = conn.cursor()  # Crear un cursor para ejecutar el query
    cursor.execute(query)  # Pasar el parámetro iddpto como una tupla

    # Convertir los resultados en una lista de diccionarios (opcional)
    columns = [column[0] for column in cursor.description]
    resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión

    end = time.time()
    print(f"Tiempo de consulta SQL: {end - start:.3f}s")
    return jsonify(resultados_dict)


# Cargar datos para reenviar una campaña
@app.route("/api/reenvioCampaña", methods=["GET", "POST"])
def reenvioCampaña():
    try:
        data = request.get_json()
        id_campania = data.get('id_campania', '')

        query = "EXEC procReenvioCampaña ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id_campania,))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar los datos de las campañas enviadas de una campaña en especifico
@app.route("/api/CampaniasEnviadasDetalle", methods=["GET", "POST"])
def CampaniasEnviadasDetalle():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            id = int(data.get('idCampania', 0))
        query = "EXEC procCampaniasEnviadasDetalle ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (id))  # Pasar el parámetro iddpto como una tupla

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procedimiento para crear o editar campañas
@app.route("/api/CrearCampania", methods=["GET", "POST"])
def CrearCampania():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            nombre = data.get('nombre', '')
            detalle = data.get('detalle', '')
            guion = data.get('guion', '')
            idusu = int(data.get('idusu', 0))
            idCampania = int(data.get('idCampania', 0))
            tipo = int(data.get('tipo', 0))  # 0: Nuevo, 1: Editar
            canal = int(data.get('canal', 0))
            activo = int(data.get('activo', 1))
            age = data.get('age', [])

        query = "EXEC procCrearCampania ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar los parámetros como una tupla
        cursor.execute(
            query, (nombre, detalle, guion, idusu, idCampania, tipo, canal, activo, age))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procedimiento para crear o editar campañas
@app.route("/api/infoCampania", methods=["GET", "POST"])
def infoCampania():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            idCampania = int(data.get('idCampania', 0))

        query = "EXEC procInfoCampania ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar los parámetros como una tupla
        cursor.execute(query, (idCampania,))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procedimiento para crear historial de gestion de chat whatsapp
@app.route("/api/agregarHistorialGestionWhatsapp", methods=["GET", "POST"])
def agregarHistorialGestionWhatsapp():
    try:
        data = request.get_json()
        idCampania = int(data.get('idCampania', 0))
        idEstado = int(data.get('idEstado', 0))
        interes = int(data.get('interes', 0))
        idprospecto_contacto = int(data.get('idprospecto_contacto', 0))
        idUsuario = int(data.get('idUsuario', 0))
        mensajes = data.get('mensajes', [])

        resultados_dict = []
        query = "EXEC procAgregarHistorialGestionWhatsapp ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()
        cursor = conn.cursor()

        for mensaje in mensajes:
            # Extraer los atributos requeridos
            mensaje_texto = mensaje.get('mensaje', '')
            hora_mensaje = mensaje.get('horaMensaje', '')
            tipo = mensaje.get('tipo', '')
            outgoing = mensaje.get('outgoing', 0)
            # Construir el JSON para el procedimiento
            mensaje_json = {
                'mensaje': mensaje_texto,
                'horaMensaje': hora_mensaje,
                'tipo': tipo,
                'outgoing': outgoing
            }
            import json
            mensaje_json_str = json.dumps(mensaje_json, ensure_ascii=False)
            # Ejecutar el procedimiento para cada mensaje
            cursor.execute(query, (
                idCampania,
                idEstado,
                interes,
                idprospecto_contacto,
                idUsuario,
                mensaje_json_str
            ))
            columns = [column[0] for column in cursor.description]
            resultados_dict.extend([dict(zip(columns, row))
                                   for row in cursor.fetchall()])

        cursor.close()
        conn.close()
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Procedimiento para crear historial de gestion de chat whatsapp en PQR


@app.route("/api/agregarHistorialGestionWhatsappPQR", methods=["GET", "POST"])
def agregarHistorialGestionWhatsappPQR():
    try:
        data = request.get_json()
        idPQR = int(data.get('idPQR', 0))
        mensajes = data.get('mensajes', [])
        idUsuario = int(data.get('idUsuario', 0))
        idEstado = int(data.get('idEstado', 0))
        idPrioridad = int(data.get('idPrioridad', 0))
        canal = data.get('canal', '')

        resultados_dict = []
        query = "EXEC procAgregarHistorialGestionWhatsappPQR ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()
        cursor = conn.cursor()

        for mensaje in mensajes:
            # Extraer los atributos requeridos
            mensaje_texto = mensaje.get('mensaje', '')
            hora_mensaje = mensaje.get('horaMensaje', '')
            tipo = mensaje.get('tipo', '')
            outgoing = mensaje.get('outgoing', 0)
            # Construir el JSON para el procedimiento
            mensaje_json = {
                'mensaje': mensaje_texto,
                'horaMensaje': hora_mensaje,
                'tipo': tipo,
                'outgoing': outgoing,
                'canal': canal,
            }
            import json
            mensaje_json_str = json.dumps(mensaje_json, ensure_ascii=False)
            # Ejecutar el procedimiento para cada mensaje
            cursor.execute(query, (
                idPQR,
                idEstado,
                idPrioridad,
                idUsuario,
                mensaje_json_str,
                canal
            ))
            columns = [column[0] for column in cursor.description]
            resultados_dict.extend([dict(zip(columns, row))
                                   for row in cursor.fetchall()])

        cursor.close()
        conn.close()
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Procedimiento para crear historial de campañas
@app.route("/api/EnviarHistorialCampania", methods=["GET", "POST"])
def EnviarHistorialCampania():
    try:
        idCampania = request.form.get('idCampania', 0)
        respuesta = request.form.get('respuesta', '')
        idEstado = request.form.get('idEstado', 0)
        interes = request.form.get('interes', 0)
        idprospecto_contacto = request.form.get('idprospecto_contacto', 0)
        idUsuario = request.form.get('idUsuario', 0)

        query = "EXEC procEnviarHistorialCampania ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idCampania, respuesta, idEstado, interes,
                       idprospecto_contacto, idUsuario))  # Pasar los parámetros como una tupla

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# --- Endpoint para subir archivos de campañas ---


@app.route("/api/saveCampaniasFiles", methods=["POST"])
def saveCampaniasFiles():

    # Procesar todos los archivos enviados como 'files' en el FormData

    try:
        from dateutil.relativedelta import relativedelta
        container_client = blob_service_client.get_container_client(
            container_name)
        try:
            container_client.create_container()
        except Exception:
            pass  # Si ya existe, no hace nada

        archivos = request.files.getlist(
            'files') or request.files.getlist('files[]')
        id = request.form.get('id')
        if not archivos or len(archivos) == 0:
            return jsonify({"error": "No se recibieron archivos en 'files'"}), 400
        if not id:
            return jsonify({"error": "No se recibió el id en formdata"}), 400

        carpeta = "mercadeo/respuestas"

        archivos_subidos = []
        for archivo in archivos:
            if archivo.filename == '':
                continue
            # Anteponer el id al nombre del archivo
            nuevo_nombre = f"{carpeta}/{id}-{archivo.filename}"
            try:
                blob_client = container_client.get_blob_client(nuevo_nombre)
                blob_client.upload_blob(archivo, overwrite=True)
                sas_token = generate_blob_sas(
                    account_name=blob_service_client.account_name,
                    container_name=container_name,
                    blob_name=nuevo_nombre,
                    account_key=blob_service_client.credential.account_key,
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + relativedelta(years=10)
                )
                url_segura = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{nuevo_nombre}?{sas_token}"
                archivos_subidos.append({
                    "filename": nuevo_nombre,
                    "url": url_segura
                })
            except Exception as e:
                print(f"❌ Error al subir el archivo {nuevo_nombre}: {e}")

        if not archivos_subidos:
            return jsonify({"error": "No se pudo subir ningún archivo"}), 500

        return jsonify({
            "message": "Archivos subidos correctamente",
            "archivos": archivos_subidos
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- Endpoint para subir archivos de campañas ---
@app.route("/api/saveCampaniasMedia", methods=["POST"])
def saveCampaniasMedia():

    # Procesar todos los archivos enviados como 'files' en el FormData

    try:
        from dateutil.relativedelta import relativedelta
        container_client = blob_service_client.get_container_client(
            container_name)
        try:
            container_client.create_container()
        except Exception:
            pass  # Si ya existe, no hace nada

        archivos = request.files.getlist(
            'files') or request.files.getlist('files[]')
        id = request.form.get('id')
        if not archivos or len(archivos) == 0:
            return jsonify({"error": "No se recibieron archivos en 'files'"}), 400
        if not id:
            return jsonify({"error": "No se recibió el id en formdata"}), 400

        carpeta = "mercadeo/media"

        archivos_subidos = []
        for archivo in archivos:
            if archivo.filename == '':
                continue
            # Anteponer el id al nombre del archivo
            nuevo_nombre = f"{carpeta}/{id}-{archivo.filename}"
            try:
                blob_client = container_client.get_blob_client(nuevo_nombre)
                blob_client.upload_blob(archivo, overwrite=True)
                sas_token = generate_blob_sas(
                    account_name=blob_service_client.account_name,
                    container_name=container_name,
                    blob_name=nuevo_nombre,
                    account_key=blob_service_client.credential.account_key,
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + relativedelta(years=10)
                )
                url_segura = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{nuevo_nombre}?{sas_token}"
                archivos_subidos.append({
                    "filename": nuevo_nombre,
                    "url": url_segura
                })

                try:
                    query = "EXEC procUpdateCampaniasUrlMedia ?, ?"
                    conn = get_db_connection()  # Obtener conexión a la base de datos
                    cursor = conn.cursor()  # Crear un cursor para ejecutar el query
                    # Pasar el parámetro iddpto como una tupla
                    cursor.execute(query, (id, url_segura))

                    # Convertir los resultados en una lista de diccionarios (opcional)
                    columns = [column[0] for column in cursor.description]
                    resultados_dict = [dict(zip(columns, row))
                                       for row in cursor.fetchall()]
                    cursor.close()  # Cerrar el cursor
                    conn.close()  # Cerrar la conexión

                    # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
                    return {'status': 'success', 'data': resultados_dict}, 200
                except Exception as e:
                    print(f"Error: {e}")
                    return jsonify({'status': 'error', 'message': str(e)}), 500

            except Exception as e:
                print(f"❌ Error al subir el archivo {nuevo_nombre}: {e}")

            if not archivos_subidos:
                return jsonify({"error": "No se pudo subir ningún archivo"}), 500

        return jsonify({
            "message": "Archivos subidos correctamente",
            "archivos": archivos_subidos
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/uploadfileblobMediaCampania33", methods=['POST'])
def uploadfileblobMediaCampania33():
    carpeta = "mercadeo/media"
    file = request.files["files"]
    id = request.form.get('id')

    if not file or not file.filename:
        return jsonify({"message": "No se envió ningún archivo"}), 400

    # Asegura contenedor (idempotente)
    try:
        container_client = blob_service_client.get_container_client(
            container_name)
        # si existe, lanzará excepción que ignoramos abajo
        container_client.create_container()
    except Exception:
        pass

    unique_name = f"{carpeta}/{id}-{file.filename}"

    # Content-Type correcto
    content_type, _ = mimetypes.guess_type(file.filename)
    content_type = content_type or "application/octet-stream"

    if content_type == "video/mp4":
        input_file = file.filename

        # Si quieres guardar en otra carpeta:
        output_file = os.path.join('files/', file.filename)

        subprocess.run([
            "ffmpeg",
            "-y",  # sobrescribir si ya existe
            "-i", input_file,                 # archivo de entrada
            "-c:v", "libx264",                # video con códec H.264
            "-profile:v", "baseline",         # perfil compatible
            "-level", "3.0",                  # nivel
            "-pix_fmt", "yuv420p",            # formato de píxel
            "-movflags", "+faststart",        # mueve el moov atom al inicio
            "-c:a", "aac",                    # audio AAC
            "-b:a", "128k",                   # bitrate audio
            "-ar", "48000",                   # frecuencia de muestreo audio
            # escala máx 1280 de ancho, alto proporcional
            "-vf", "scale='min(1280,iw)':-2",
            output_file
        ])

    blob_client = container_client.get_blob_client(unique_name)

    try:
        if content_type != "video/mp4":

            # Sube desde stream para no cargar todo en memoria
            blob_client.upload_blob(
                file.stream,
                overwrite=True,
                content_settings=ContentSettings(content_type=content_type)
            )
        else:
            with open(output_file, "rb") as file_stream:
                blob_client.upload_blob(
                    file_stream,  # <-- esto es tu stream
                    overwrite=True,
                    content_settings=ContentSettings(content_type="video/mp4")
                )

        account_name = blob_service_client.account_name
        blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{unique_name}"

        # --- Opción alternativa: SAS larga (ej. 10 años) ---
        sas_token_long = generate_blob_sas(
            account_name=account_name,
            container_name=container_name,
            blob_name=unique_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + relativedelta(years=10)
        )
        sas_url_10y = f"{blob_url}?{sas_token_long}"

        try:
            query = "EXEC procUpdateCampaniasUrlMedia ?, ?"
            conn = get_db_connection()  # Obtener conexión a la base de datos
            cursor = conn.cursor()  # Crear un cursor para ejecutar el query
            # Pasar el parámetro iddpto como una tupla
            cursor.execute(query, (id, sas_url_10y))

            # Convertir los resultados en una lista de diccionarios (opcional)
            columns = [column[0] for column in cursor.description]
            resultados_dict = [dict(zip(columns, row))
                               for row in cursor.fetchall()]
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión

            # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
            return {'status': 'success', 'data': resultados_dict}, 200
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 500

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({
            "message": "Error al subir archivo",
            "error": str(e)
        }), 500


@app.route("/api/uploadfileblobMediaCampania", methods=['POST'])
def uploadfileblobMediaCampania():
    carpeta = "mercadeo/media"
    up = request.files.get("files")
    camp_id = request.form.get("id")

    if not up or not up.filename:
        return jsonify({"message": "No se envió ningún archivo"}), 400

    # Asegura contenedor (idempotente)
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
    except Exception:
        pass

    # ------- 1) Guardar archivo temporalmente en disco -------
    os.makedirs("files", exist_ok=True)
    original_name = secure_filename(up.filename)
    # Añade ID para evitar colisiones
    disk_in = os.path.join("files", f"in-{uuid.uuid4().hex}-{original_name}")
    up.save(disk_in)  # <-- ahora sí existe en disco

    # Detecta content-type (mejor usa el que manda el navegador si viene)
    content_type = up.mimetype or mimetypes.guess_type(
        original_name)[0] or "application/octet-stream"

    # Blob name definitivo (con id de campaña)
    unique_name = f"{carpeta}/{camp_id}-{original_name}"

    try:
        # ------- 2) Si es video/mp4, re-encode para WhatsApp (+faststart) -------
        if content_type.lower() == "video/mp4":
            disk_out = os.path.join(
                "files", f"out-{uuid.uuid4().hex}-{original_name}")
            # OJO: en Windows NO pongas comillas dentro del -vf; pásalo como un arg normal
            ffmpeg_bin = shutil.which("ffmpeg")
            """proc = subprocess.run([
                ffmpeg_bin, "-hide_banner", "-nostdin", "-y",
                "-i", disk_in,
                "-c:v", "libx264",
                "-profile:v", "baseline",
                "-level", "3.0",
                "-pix_fmt", "yuv420p",
                "-movflags", "+faststart",
                "-c:a", "aac", "-b:a", "128k", "-ar", "48000",
                "-vf", "scale=1280:-2:force_original_aspect_ratio=decrease",  # 👈 sin comas
                disk_out
            ], capture_output=True, text=True)"""

            cmd = [
                ffmpeg_bin, "-hide_banner", "-nostdin", "-y",
                "-i", disk_in,
                "-c", "copy",
                "-movflags", "+faststart",
                disk_out
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True)

            if proc.returncode != 0:
                os.remove(disk_in)
                print("❌ Error en ffmpeg")
                print("CMD:", " ".join(proc.args))
                print("STDERR:", proc.stderr)
                return jsonify({
                    "message": "Error en ffmpeg",
                    "stderr": proc.stderr
                }), 500

            # Subir el archivo convertido
            blob_client = container_client.get_blob_client(unique_name)
            with open(disk_out, "rb") as f:
                blob_client.upload_blob(
                    f,
                    overwrite=True,
                    content_settings=ContentSettings(
                        content_type="video/mp4",
                        content_disposition="inline",
                        cache_control="public, max-age=31536000"
                    )
                )
            # Limpieza
            try:
                os.remove(disk_out)
            except Exception:
                pass

        else:
            # ------- 3) No es video: subir directo desde disco -------
            blob_client = container_client.get_blob_client(unique_name)
            with open(disk_in, "rb") as f:
                blob_client.upload_blob(
                    f,
                    overwrite=True,
                    content_settings=ContentSettings(content_type=content_type)
                )

        # ------- 4) Generar URL y SAS (si lo necesitas) -------
        account_name = blob_service_client.account_name
        blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{unique_name}"

        # SAS largo (mejor usa expiración más corta en prod)
        sas_token = generate_blob_sas(
            account_name=account_name,
            container_name=container_name,
            blob_name=unique_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + relativedelta(years=10),
            protocol="https",
            version="2023-11-03",  # evita versiones "futuras"
        )
        sas_url = f"{blob_url}?{sas_token}"

        # ------- 5) Persistir en DB (tal como tenías) -------
        try:
            query = "EXEC procUpdateCampaniasUrlMedia ?, ?"
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, (camp_id, sas_url))
            columns = [c[0] for c in cursor.description]
            resultados = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return {'status': 'success', 'data': resultados, 'url': sas_url}, 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    except Exception as e:
        return jsonify({"message": "Error al subir archivo", "error": str(e)}), 500

    finally:
        # ------- 6) Limpieza del input local -------
        try:
            os.remove(disk_in)
            os.remove(disk_out)
        except Exception:
            pass

    carpeta = "mercadeo/media"
    up = request.files.get("files")
    camp_id = request.form.get("id")

    if not up or not up.filename:
        return jsonify({"message": "No se envió ningún archivo"}), 400

    # Asegura contenedor (idempotente)
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
    except Exception:
        pass

    # ------- 1) Guardar archivo temporalmente en disco -------
    os.makedirs("files", exist_ok=True)
    original_name = secure_filename(up.filename)
    # Añade ID para evitar colisiones
    disk_in = os.path.join("files", f"in-{uuid.uuid4().hex}-{original_name}")
    up.save(disk_in)  # <-- ahora sí existe en disco

    # Detecta content-type (mejor usa el que manda el navegador si viene)
    content_type = up.mimetype or mimetypes.guess_type(
        original_name)[0] or "application/octet-stream"

    # Blob name definitivo (con id de campaña)
    unique_name = f"{carpeta}/{camp_id}-{original_name}"

    try:
        # ------- 2) Si es video/mp4, re-encode para WhatsApp (+faststart) -------
        if content_type.lower() == "video/mp4":
            disk_out = os.path.join(
                "files", f"out-{uuid.uuid4().hex}-{original_name}")
            # OJO: en Windows NO pongas comillas dentro del -vf; pásalo como un arg normal
            ffmpeg_bin = shutil.which("ffmpeg")
            """proc = subprocess.run([
                ffmpeg_bin, "-hide_banner", "-nostdin", "-y",
                "-i", disk_in,
                "-c:v", "libx264",
                "-profile:v", "baseline",
                "-level", "3.0",
                "-pix_fmt", "yuv420p",
                "-movflags", "+faststart",
                "-c:a", "aac", "-b:a", "128k", "-ar", "48000",
                "-vf", "scale=1280:-2:force_original_aspect_ratio=decrease",  # 👈 sin comas
                disk_out
            ], capture_output=True, text=True)"""

            cmd = [
                ffmpeg_bin, "-hide_banner", "-nostdin", "-y",
                "-i", disk_in,
                "-c", "copy",
                "-movflags", "+faststart",
                disk_out
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True)

            if proc.returncode != 0:
                os.remove(disk_in)
                print("❌ Error en ffmpeg")
                print("CMD:", " ".join(proc.args))
                print("STDERR:", proc.stderr)
                return jsonify({
                    "message": "Error en ffmpeg",
                    "stderr": proc.stderr
                }), 500

            # Subir el archivo convertido
            blob_client = container_client.get_blob_client(unique_name)
            with open(disk_out, "rb") as f:
                blob_client.upload_blob(
                    f,
                    overwrite=True,
                    content_settings=ContentSettings(
                        content_type="video/mp4",
                        content_disposition="inline",
                        cache_control="public, max-age=31536000"
                    )
                )
            # Limpieza
            try:
                os.remove(disk_out)
            except Exception:
                pass

        else:
            # ------- 3) No es video: subir directo desde disco -------
            blob_client = container_client.get_blob_client(unique_name)
            with open(disk_in, "rb") as f:
                blob_client.upload_blob(
                    f,
                    overwrite=True,
                    content_settings=ContentSettings(content_type=content_type)
                )

        # ------- 4) Generar URL y SAS (si lo necesitas) -------
        account_name = blob_service_client.account_name
        blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{unique_name}"

        # SAS largo (mejor usa expiración más corta en prod)
        sas_token = generate_blob_sas(
            account_name=account_name,
            container_name=container_name,
            blob_name=unique_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + relativedelta(years=10),
            protocol="https",
            version="2023-11-03",  # evita versiones "futuras"
        )
        sas_url = f"{blob_url}?{sas_token}"

        # ------- 5) Persistir en DB (tal como tenías) -------
        try:
            query = "EXEC procUpdateCampaniasUrlMedia ?, ?"
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, (camp_id, sas_url))
            columns = [c[0] for c in cursor.description]
            resultados = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return {'status': 'success', 'data': resultados, 'url': sas_url}, 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    except Exception as e:
        return jsonify({"message": "Error al subir archivo", "error": str(e)}), 500

    finally:
        # ------- 6) Limpieza del input local -------
        try:
            os.remove(disk_in)
            os.remove(disk_out)
        except Exception:
            pass

# --- Endpoint para actualizar las urls de la respuesta de campañas ---


@app.route("/api/updateCampaniasFilesUrl", methods=["POST"])
def updateCampaniasFilesUrl():

    try:
        idRespuesta = request.form.get('idRespuesta')
        urls = request.form.get('urls')

        query = "EXEC procUpdateCampaniasResArchivos ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idRespuesta, urls))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


"""
Carga los mensajes que se han enviado por whatsapp al cliente
Envía todos los campos de la tabla messages para que se pueda mostrar en la pantalla de mensajes
Esta ruta recibe clicel, tipo e id y retorna los mensajes asociados a ese cliente
"""


@app.route('/api/messages_old', methods=['GET', 'POST'])
def messages_old():
    data = request.get_json()
    clicel = data['clicel']
    tipo = data['tipo']
    id = int(data['id'])
    try:
        query = "EXEC procBuscarSubConsulta ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (clicel, tipo, id))
        # cursor.commit()

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/messages', methods=['GET', 'POST'])
def messages():
    data = request.get_json()
    clicel = data['clicel']
    recipient = data['recipient']  # celular del cliente
    try:
        query = "EXEC procBuscarSubConsultaMercadeo ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (clicel, recipient))
        # cursor.commit()

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/wh_buscarchatactivo', methods=['GET', 'POST'])
def wh_buscarchatactivo():
    data = request.get_json()
    clicel = data['clicel']
    try:
        query = "EXEC procWh_buscarchatactivo ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (clicel,))
        # cursor.commit()

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Mensaje enviado desde el chat del glpi, para poder enviarlo por whatsapp
@app.route('/api/chat_from_backend_consec', methods=['GET', 'POST'])
async def chat_from_backend_consec():
    a = 1
    try:
        # Obtener los datos JSON de la solicitud
        data = request.get_json()
        clicel = data['clicel']  # celular de cliente
        # mensaje para el cliente por parte de nuestro asesor
        men = data['men']
        # opción seleccionada para el envio del mensaje (1: mensaje normal, 2: saluda desde el icono del chat, 3: despedida desde el icono del chat)
        opc = int(data['opc'])
        clinom = data['clinom']  # nombre del cliente
        idusu = int(data['idusu'])  # idusuario
        asenom = data['asenom']  # nombre del asesor que chatea
        asecel = data['asecel']  # celular del asesor que chatea
        # estado si el cliente esta en espera o no
        espera = int(data.get('espera', 0))
        # id del mensaje que se reenvia
        resp_men = int(data.get('idMensaje', 0))
        consec = int(data.get('id', 0))  # consecutivo del pqr o mercadeo
        # perfil del moduo que envia pqr o mercadeo
        area = data.get('perf', '')
        rolUsuario = int(data.get('rolUsuario', 0))
        canal = data.get('canal', '')
        #   OJO: AGREGARLO AL procChatGLPI, REVISAR EN DONDE MAS SE LLAMA ESE PROCEDIMIENTO EN EL GLPI-SIICSA Y EN LA APP DE ANDROID

        query = "EXEC procChatGLPI ?, ?, ?, ?, ?, ?, ?, ?"
        conn2 = get_db_connection()  # Obtener conexión a la base de datos
        cursor2 = conn2.cursor()  # Crear un cursor para ejecutar el query
        cursor2.execute(query, (clicel, men, opc, clinom,
                        idusu, asenom, asecel, espera))
        resultados = cursor2.fetchall()  # Obtener los resultados
        conn2.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columnas = [column[0] for column in cursor2.description]
        resultados_dict = [dict(zip(columnas, row)) for row in resultados]

        idemp = 0
        nomemp = ''
        for dato in resultados_dict:
            idemp = dato['idemp']
            nomemp = dato['nomemp']

        cursor2.close()  # Cerrar el cursor
        conn2.close()  # Cerrar la conexión

        men = f"*{asenom} Dice:*\n{men}"

        if opc == 2:  # Saludo desde el icono del chat (icono: mano alzada)
            men = f"*{asenom} Dice:*\n😀 Hola *{clinom}*. Buen día. Cómo te encuentras?"
        elif opc == 3:  # Despedida desde el icono del chat (icono: puerta)
            men = f"*{asenom} Dice:*\nHasta Pronto 😊. Que tengas un Excelente Día! 👍🏻"
        elif opc == 4:  # Redirige al Bot (icono: piñon)
            men = f"En este momento seras Dirigido a Nuestra Area de Soporte 👨🏻‍💻👨🏻‍💻\n\n*Por favor, Describeme tu problema o requerimiento técnico:*"
        elif opc == 5:  # Pausa desde el icono del chat (icono: pausa)
            men = f"*{asenom} Dice:*\nGracias, seguimos con el proceso de tu caso"
            if espera == 1:
                men = f"*{asenom} Dice:*\nGracias por la espera, estoy atendiendo tu caso"

        # celular de la empresa para el bot de soporte
        recipient = os.getenv("PHONE_NUMBER_ID")
        if rolUsuario == 5:
            # celular de la empresa para el bot de mercadeo
            recipient = os.getenv("PHONE_NUMBER_ID")
            
        if canal == 'messenger':
            recipient = os.getenv("PHONE_NUMBER_ID_PG")
        if canal == 'instagram':
            recipient = os.getenv("PHONE_NUMBER_ID_IG")

        try:
            message_data = sendCustomTexto(clicel, men)

            if opc == 2:  # envía plantilla de bienvenida
                # enviar template
                body_params = [clinom]
                message_data = build_whatsapp_template_payload(
                    to=clicel,
                    template_name='siicsa_saludo_dato',
                    body_params=body_params,
                    header_text='Comercial Siicsa'
                )

            try:
                if canal == 'messenger' or canal == 'instagram':
                    message_data = await sendTexto_PG_IG(clicel, men)
                    wam_id = message_data["message_id"]
                else:        
                    dato = await send_message_pni(message_data, recipient)
                    wam_id = dato['response']['messages'][0]['id']
            except Exception as e:
                print({"error en send_message_pni": str(e)})

            if opc == 3:
                save_res_bot_consec(clicel, wam_id, men, '', '', '', '', '', '', '', '', '',
                                    '', '', '', '', '', '', 1, 0, 0, 0, consec, area, resp_men, '', recipient, canal)
            elif opc == 4:
                save_res_bot_consec(clicel, wam_id, men, 'servicio_det', clinom, '', idemp, nomemp, 'usu',
                                    'si', '', '', '', '', '', '', '', '', 1, 0, 0, 0, consec, area, resp_men, '', recipient, canal)
            else:
                save_res_bot_consec(clicel, wam_id, men, 'asesor en proceso', clinom, '', idemp, nomemp,
                                    '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, consec, area, resp_men, '', recipient, canal)

            # Muestra todos los datos de la tabla messages en un json
            mess = cargar_message(wam_id)
            data = mess[0]
            pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {'message': data, 'change': 1})

        except Exception as e:
            print({"error en festivo": str(e)})

        # Procesar los datos (puedes añadir lógica adicional aquí)
        return jsonify({'status': 'success', 'data': data}), 200
    except Exception as e:
        return jsonify({"error_glpichat_from_backend_consec": str(e)}), 500


def save_res_bot_consec(wa_id, wam_id, body, option, nombre, cedula, idemp, nomemp, tipologin, logueo, dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8, outgoing, tempo, vip, especial, consecutivo, area, resp_men, resp_men_body, recipient, canal):
    query = "EXEC procCrearMessage2 ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
    conn = get_db_connection()  # Obtener conexión a la base de datos
    cursor = conn.cursor()  # Crear un cursor para ejecutar el query
    cursor.execute(query, (wa_id, wam_id, body, option, nombre, cedula, idemp, nomemp, tipologin, logueo, dato1, dato2, dato3,
                   dato4, dato5, dato6, dato7, dato8, outgoing, tempo, vip, especial, consecutivo, area, resp_men, resp_men_body, recipient, canal))
    conn.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)
    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión


def cargar_message(wamid):
    query = "EXEC procBuscarWamId ?"

    conn = get_db_connection()  # Obtener conexión a la base de datos
    cursor = conn.cursor()  # Crear un cursor para ejecutar el query
    cursor.execute(query, wamid)
    resultados = cursor.fetchall()  # Obtener los resultados
    conn.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)

    # Convertir los resultados en una lista de diccionarios (opcional)
    # columnas = [column[0] for column in cursor.description]
    # resultados_dict = [dict(zip(columnas, row)) for row in resultados]

    datos = []
    for row in resultados:
        datos.append({'id': row[0], 'wa_id': row[1], 'wam_id': row[2], 'type': row[3], 'outgoing': row[4], 'body': row[5], 'status': row[6], 'caption': row[7], 'data': row[8], 'created_at': str(row[9]), 'updated_at': str(row[10]), 'option_button': row[11], 'option_fecha': row[12], 'option_nombre': row[13], 'option_cedula': row[14], 'option_fecha2': row[15], 'option_fecha3': row[16], 'option_pedido': row[17], 'option_cantidad': row[18], 'dato_uno': row[19],
                     'dato_dos': row[20], 'dato_tres': row[21], 'dato_cuatro': row[22], 'dato_cinco': row[23], 'dato_seis': row[24], 'dato_siete': row[25], 'option_idemp': row[26], 'option_nomemp': row[27], 'dato_ocho': row[28], 'tipo_login': row[29], 'logueo': row[30], 'correo': row[31], 'tempo': row[32], 'vip': row[33], 'especial': row[34], 'consecutivo': row[35], 'area': row[36], 'resp_men': row[37], 'resp_men_body': row[38], 'recipient': row[39]})

    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión
    return datos  # Retornar los resultados como JSON


# Carpeta para almacenar imágenes
UPLOAD_FOLDER = '/home/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/api/subir-imagen', methods=['POST'])
def subir_imagen():
    if 'imagen' not in request.files:
        return jsonify({'error': 'No se encontró el archivo'}), 400

    file = request.files['imagen']
    nombre_archivo = request.form.get('nombre_archivo')

    if not file or not nombre_archivo:
        return jsonify({'error': 'Faltan datos'}), 400

    nombre_archivo = secure_filename(nombre_archivo)
    ruta_guardado = os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo)

    try:
        if os.path.exists(ruta_guardado):
            os.remove(ruta_guardado)
        file.save(ruta_guardado)
        print(f"✅ Imagen guardada en: {ruta_guardado}")
        return jsonify({'mensaje': 'Imagen subida correctamente'}), 200
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return jsonify({'error': 'No se pudo guardar la imagen'}), 500


@app.route('/api/cargarMetaUsu', methods=['GET', 'POST'])
def cargarMetaUsu():
    data = request.get_json()
    id = int(data['id'])
    try:
        query = "EXEC procBuscarMetaUsu ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (id))
        # cursor.commit()

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/api/cargaActividades", methods=["GET", "POST"])
def cargaActividades():
    try:
        query = "EXEC procCargaActividades"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargaSeguimiento", methods=["GET", "POST"])
def cargaSeguimiento():
    try:
        data = request.get_json()
        cotiz = int(data['cotiz'])
        query = "EXEC procCargaSeguimiento ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, cotiz)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Cargar la lista de las campañas


@app.route("/api/cargarCampanas", methods=["GET", "POST"])
def cargarCampanas():
    try:

        query = "EXEC procCargarCampanas"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar el historial de una campaña enviada
@app.route("/api/cargarHistorialCampana", methods=["GET", "POST"])
def cargarHistorialCampana():
    try:
        data = request.get_json()
        idCampania = int(data['idCampania'])
        query = "EXEC procCargarHistorialCampania ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idCampania,))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar Lista de Empresas
@app.route("/api/cargarEm", methods=["GET", "POST"])
def cargarEm():
    try:
        query = "EXEC procCargaEmpresas"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Cargar Lista de Categoria de cargo


@app.route("/api/cargarCatCargo", methods=["GET", "POST"])
def cargarCatCargo():
    try:

        query = "EXEC procCargaCatCargos "
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Cargar Lista de cargos


@app.route("/api/cargarCargo", methods=["GET", "POST"])
def cargarCargo():
    try:

        query = "EXEC procCargaCargos ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, 0)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Cargar Lista de Departamentos


@app.route("/api/cargarDep", methods=["GET", "POST"])
def cargarDep():
    try:

        query = "EXEC procCargaDptos"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Cargar Lista de Departamentos


@app.route("/api/cargarCiudad", methods=["GET", "POST"])
def cargarCiudad():
    try:

        query = "EXEC procCargaCiudades2"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Cargar lista de filtros


@app.route("/api/cargardatosfiltcamp", methods=["GET", "POST"])
def cargardatosfiltcamp():
    try:
        idsector = request.form.get('idsector')
        idempresa = request.form.get('idempresa')
        idcatcargo = request.form.get('idcatcargo')
        idcargo = request.form.get('idcargo')
        iddpto = request.form.get('iddpto')
        idciudad = request.form.get('idciudad')

        query = "EXEC procFiltroCampaniaEnvio ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idsector, idempresa,
                       idcatcargo, idcargo, iddpto, idciudad))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Guardar una gestión de campaña telefónica
@app.route("/api/guardarGestionTelefonica", methods=["GET", "POST"])
def guardarGestionTelefonica():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            idComercial = int(data.get('id_comercial', 0))
            idProducto = int(data.get('id_producto', 0))
            idSubProducto = int(data.get('id_subproducto', 0))
            observaciones = data.get('observaciones', '')
            idCampania = int(data.get('id_campania', 0))
            idContacto = int(data.get('id_contacto', 0))
            idUsuario = int(data.get('id_usuario', 0))
            efectividad = int(data.get('efectividad', 0))
            crearLead = int(data.get('crear_lead', 0))
            motivoNoLead = int(data.get('motivo_no_lead', 0))
            motivoNoEfectivo = int(data.get('motivo_no_efectivo', 0))
            observacionesNoEfectivo = data.get('observaciones_no_efectivo', '')
            id_empresa = int(data.get('id_empresa', 0))
            fecha_reagenda = data.get('fecha_reagenda', '')
            estado = int(data.get('estado', 0))
            id_campenv = int(data.get('id_campenv', 0))
            # formatear fecha reagenda a formato datetime para base de datos cuando el valor es igual al formato similar al "2025-09-15T10:00"
            if fecha_reagenda and re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$', fecha_reagenda):
                fecha_reagenda = datetime.strptime(
                    fecha_reagenda, '%Y-%m-%dT%H:%M')
            else:
                fecha_reagenda = ''

        query = "EXEC procGuardarGestionTelefonica ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idComercial, idProducto, idSubProducto, observaciones,
                       idCampania, idContacto, idUsuario, efectividad, crearLead, motivoNoLead, motivoNoEfectivo, observacionesNoEfectivo, id_empresa, fecha_reagenda, estado, id_campenv))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Editar una gestión de campaña telefónica
@app.route("/api/editarGestionTelefonica", methods=["GET", "POST"])
def editarGestionTelefonica():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            id_historial = int(data.get('id_historial', 0))
            fecha_original = data.get('fecha_original', '')
            texto_original = data.get('texto_original', '')
            texto_editado = data.get('texto_editado', '')
            id_usu = int(data.get('id_usu', 0))
            id_tipo_log = int(data.get('id_tipo_log', 0))

            # formatear fecha original a formato datetime para base de datos cuando el valor es igual al formato similar al "15/09/2025 15:09"
            if fecha_original and re.match(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$', fecha_original):
                fecha_original = datetime.strptime(
                    fecha_original, '%d/%m/%Y %H:%M')
            else:
                fecha_original = ''

        query = "EXEC procEditarGestionTelefonica ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id_historial, fecha_original,
                       texto_original, texto_editado, id_usu, id_tipo_log))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar los seguimientos de las campañas telefónicas
@app.route("/api/cargarSeguimientosCampanasT", methods=["GET", "POST"])
def cargarSeguimientosCampanasT():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            idUsuario = int(data.get('id_usuario', 0))

        query = "EXEC procCargarSeguimientosCampanasT ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idUsuario))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar el historial de ediciones de una gestión telefónica
@app.route("/api/historialEdiciones", methods=["GET", "POST"])
def historialEdiciones():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            id_historial = int(data.get('id_historial', 0))

        query = "EXEC procCargarHistorialEdiciones ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id_historial))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar los llamadas relizadas por el usuario a modo de informe
@app.route("/api/llamadasRealizadas", methods=["GET", "POST"])
def llamadasRealizadas():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            idUsuario = int(data.get('id_usuario', 0))
            filtro = int(data.get('filtro', 0))

        query = "EXEC procCargarLlamadasRealizadas ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idUsuario, filtro))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar el historial de una prospeccion telefónica
@app.route("/api/cargarhistorialgestion", methods=["GET", "POST"])
def cargarhistorialgestion():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            id_campaña = int(data.get('id_campaña', 0))
            id_contacto = int(data.get('id_contacto', 0))
            id_empresa = int(data.get('id_empresa', 0))

        query = "EXEC procCargarHistorialGestionT ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id_campaña, id_contacto, id_empresa))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Cargar el historial de una prospeccion telefónica desde comercial


@app.route("/api/cargarhistorialgestion2", methods=["GET", "POST"])
def cargarhistorialgestion2():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            idproccom = int(data.get('idproccom', 0))

        query = "EXEC procCargarHistorialGestionT2 ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idproccom))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar el historial de una prospeccion telefónica
@app.route("/api/cargarhistoriallead", methods=["GET", "POST"])
def cargarhistoriallead():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            id_usuario = int(data.get('id_usuario', 0))
            agrupar = int(data.get('agrupar', 0))

        query = "EXEC procCargarHistorialLead ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id_usuario, agrupar))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Cargar el historial global de prospeccion telefónica
@app.route("/api/historialGlobalLlamadas", methods=["GET", "POST"])
def historialGlobalLlamadas():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            id_usuario = int(data.get('id_usuario', 0))
            agrupar = int(data.get('agrupar', 0))

        query = "EXEC procCargarHistorialGlobalLlamadas ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (id_usuario, agrupar))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Reporte de campanñas telefónicas enviadas por usuario


@app.route("/api/reporteCampaniasEnviadas", methods=["GET", "POST"])
def reporteCampaniasEnviadas():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            idusu = int(data.get('idusu', 0))

        query = "EXEC procReporteCampaniasEnviadas ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar el parámetro iddpto como una tupla
        cursor.execute(query, (idusu))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# ENVIO DE CAMPAÑAS DESDE LA WEB

@app.route('/api/envia_campania', methods=['GET', 'POST'])
def envia_campania():
    try:
        campid = request.form['campid']  # 👈 Recibir nombre campaña
        campnom = request.form['campnom']  # 👈 Recibir nombre campaña
        template = request.form['template']  # 👈 Recibir nombre campaña
        idusu = request.form['idusu']  # 👈 Recibir nombre campaña
        urlArchivo = request.form['archivo']  # 👈 Recibir nombre campaña

        solo_manual = request.form.get('soloManual', 'false') == 'true'
        numeros_manual = request.form.get('numerosManual', '')
        telefonos = []

        filtros_envio_json = request.form.get('filtrosEnvio', '{}')

        filtros_envio = json.loads(filtros_envio_json)

        if solo_manual:
            # Solo usar los números manuales
            if numeros_manual:
                telefonos = [n.strip() for n in re.split(
                    r'[,;\s]+', numeros_manual) if n.strip()]
        else:
            filtroSector = str(filtros_envio.get('1', 0))
            filtroEmpresa = str(filtros_envio.get('2', 0))
            filtroCatCargo = str(filtros_envio.get('3', 0))
            filtroCargo = str(filtros_envio.get('4', 0))
            filtroDpto = str(filtros_envio.get('5', 0))
            filtroCiudad = str(filtros_envio.get('6', 0))

            telefonos = campania_filtros_envio(
                filtroSector, filtroEmpresa, filtroCatCargo, filtroCargo, filtroDpto, filtroCiudad)
            if numeros_manual:
                numeros_extra = [n.strip() for n in re.split(
                    r'[,;\s]+', numeros_manual) if n.strip()]
                telefonos.extend(numeros_extra)

        # Lanzar el proceso en segundo plano
        if template == 'boletin_informativo':
            threading.Thread(target=envia_boletin_form, args=(urlArchivo, telefonos, campid, idusu, campnom,
                             numeros_manual, json.dumps(filtros_envio, ensure_ascii=False), template), daemon=True).start()
        elif template == 'video_informativo_mp4':
            threading.Thread(target=run_async_coroutine_in_thread, args=(video_informativo_mp4, urlArchivo, telefonos, campid,
                             idusu, campnom, numeros_manual, json.dumps(filtros_envio, ensure_ascii=False), template), daemon=True).start()
        elif template == 'promocionar_productos_servicios':
            threading.Thread(target=promocionar_productos_servicios, args=(urlArchivo, telefonos, campid, idusu,
                             campnom, numeros_manual, json.dumps(filtros_envio, ensure_ascii=False), template), daemon=True).start()

        return jsonify({'status': 'success', 'data': "Mensajes enviados correctamente !!\nMuy pronto te avisaremos el estado de la campaña por este medio. La url del archivo es: "}), 200

    except Exception as e:
        return jsonify({'status': 'error envia_campania', 'data': str(e)}), 200


def campania_filtros_envio(idsector, idempresa, idcatcargo, idcargo, filtroDpto, filtroCiudad):
    query = "EXEC procFiltroCampaniaEnvio ?, ?, ?, ?, ?, ?"
    conn = get_db_connection()  # Obtener conexión a la base de datos
    cursor = conn.cursor()  # Crear un cursor para ejecutar el query
    cursor.execute(query, (idsector, idempresa, idcatcargo,
                   idcargo, filtroDpto, filtroCiudad))
    resultados = cursor.fetchall()  # Obtener los resultados
    conn.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)

    datos = []
    for row in resultados:
        datos.append(row[0])

    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión
    return datos  # Retornar los resultados

# Se encarga de llevar control en los hilos que se vayan generando para el envio de mensajes


def run_async_coroutine_in_thread(coro_func, *args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro_func(*args))
    loop.close()


"""def envia_boletin_form(urlArchivo, telefonos, campid, idusu, campnom):
    time.sleep(10)  # Esperar 5 minutos (300 segundos)

    with app.app_context():
        try:

            # URL de acceso al archivo
            url_imagen = urlArchivo
            time.sleep(0.5)

            i = 0
            recipient_mercadeo = os.getenv("PHONE_NUMBER_ID")
            # Procesar campaña
            resultados = {}
            for numero in telefonos:
                i += 1
                res = envia_boletin_form_template(numero, url_imagen)
                resultados[numero] = res
                wam_id = res["messages"][0]["id"]
                try:
                    query = "EXEC procCrearMessage ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
                    conn = get_db_connection()  # Obtener conexión a la base de datos
                    cursor = conn.cursor()  # Crear un cursor para ejecutar el query
                    cursor.execute(query, (numero, wam_id, url_imagen, '', '', '', '', '',
                                   '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, recipient_mercadeo))
                    conn.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)
                    cursor.close()  # Cerrar el cursor
                    conn.close()  # Cerrar la conexión
                except Exception as e:
                    print(f"❌ Error al ejecutar procCrearMessage: {e}")
                time.sleep(2)  # Esperar 2 segundos entre cada mensaje

                if i % 50 == 0:
                    time.sleep(30)  # Esperar 30 segundos cada 50 mensajes

            # Configura Pusher con las credenciales que obtuviste de tu cuenta Pusher
            # pusher_client_mercadero = pusher.Pusher(
            #    app_id='1984968',        # Reemplaza con tu app_id
            #    key='f0b7888bd36a4d955af0',          # Reemplaza con tu key
            #    secret='c9f85e0de46e7d6c8e86',    # Reemplaza con tu secret
            #    cluster='us2',  # Reemplaza con tu cluster (ej. 'mt1')
            #    ssl=True
            # )
            # pusher_client_mercadero.trigger('webhooks', 'telemercadeo', {'message': resultados, 'change': 1})

            return jsonify({'status': 'success', 'data': resultados}), 200
        except Exception as e:
            return jsonify({'error envia_boletin_form': str(e)}), 500
"""


def envia_boletin_form(urlArchivo, telefonos, campid, idusu, campnom, numeros_manual, filtros_envio, template):
    # time.sleep(300)  # Esperar 5 minutos (300 segundos)
    time.sleep(10)  # Esperar 5 minutos (300 segundos)
    with app.app_context():
        try:
            # url_imagen = url_for('static', filename=f'{carpeta}/{filename}', _external=True)
            # URL de acceso al archivo
            url_imagen = urlArchivo
            recipientmerc = os.getenv("PHONE_NUMBER_ID")
            resultados = ''
            status = 'success'
            rechazado = 0
            valido = 0

            i = True
            j = 0
            for numero in telefonos:
                valido = validar_numeros_campania2(numero)
                if valido == 0:                    
                    rechazado = 0
                    if len(str(numero)) > 0:
                        j += 1
                        try:
                            res = envia_boletin_form_template(numero, url_imagen)
                            wam_id = res["messages"][0]["id"]
                        except Exception as e:
                            wam_id = 'Rechazado'
                            resultados += f"numero. "
                            rechazado = 1
                        finally:
                            save_res_bot_campania(numero, wam_id, url_imagen, 'campania', '', '', '', '', '',
                                                '', '', '', '', '', campid, '0', '', '', 1, 0, 0, 0, 0, '', 0, '', recipientmerc, numeros_manual, filtros_envio, template, rechazado, 'image')
                        time.sleep(2)  # Esperar 2 segundos entre cada mensaje

                        if j % 50 == 0:
                            time.sleep(30)  # Esperar 30 segundos cada 50 mensajes


            if resultados == '':
                resultados = f"La carga de mensajes de la campaña {campnom} se envió correctamente."
            else:
                status = 'error'
                resultados = "Los siguientes números 📞 no se pudieron enviar. Por favor rectifíquelos y envíalos nuevamente: \n" + \
                    str(resultados)

            # Configura Pusher con las credenciales que obtuviste de tu cuenta Pusher

            # Está así porque el evento se llama así en la app de laravel
            pusher_client.trigger('webhooks', 'App\\Events\\Comercial', {
                                  'message': resultados, 'change': 1})

            return jsonify({'status': status, 'data': resultados}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'data': str(e)}), 500


def envia_boletin_form_template(numero, url_imagen):
    HEADERS = {
        'Authorization': f"Bearer {os.getenv('ACCESS_TOKEN')}",
        'Content-Type': 'application/json'
    }
    url = f"https://graph.facebook.com/v23.0/{os.getenv('PHONE_NUMBER_ID')}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "template",
        "template": {
            "name": "boletin_informativo",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": url_imagen
                            }
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()


"""async def video_informativo_mp4(urlArchivo, telefonos, campid, idusu):
    # time.sleep(10)  # Esperar 5 minutos (300 segundos)
    await asyncio.sleep(10)
    with app.app_context():
        # Configura Pusher con las credenciales que obtuviste de tu cuenta Pusher
        # pusher_client_mercadero = pusher.Pusher(
        #    app_id='1984968',        # Reemplaza con tu app_id
        #    key='f0b7888bd36a4d955af0',          # Reemplaza con tu key
        #    secret='c9f85e0de46e7d6c8e86',    # Reemplaza con tu secret
        #    cluster='us2',  # Reemplaza con tu cluster (ej. 'mt1')
        #    ssl=True
        # )
        try:
            # URL de acceso al archivo
            video_url = urlArchivo
            # URL de acceso al archivo
            # video_url = f"{os.getenv('URL')}/{carpeta}/{filename}"
            # media_id = await subir_video_a_meta_url(video_url)
            i = 0

            if True:
                recipient_mercadeo = os.getenv("PHONE_NUMBER_ID")
                # Procesar campaña
                resultados = {}
                for numero in telefonos:
                    i += 1
                    res = await enviar_template_video_idmedia(numero, video_url)
                    resultados[numero] = res
                    wam_id = res["messages"][0]["id"]
                    try:
                        query = "EXEC procCrearMessage ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
                        conn = get_db_connection()  # Obtener conexión a la base de datos
                        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
                        cursor.execute(query, (numero, wam_id, video_url, '', '', '', '', '', '',
                                       '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, recipient_mercadeo))
                        conn.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)
                        cursor.close()  # Cerrar el cursor
                        conn.close()  # Cerrar la conexión
                    except Exception as e:
                        print(f"❌ Error al ejecutar procCrearMessage: {e}")
                    # Esperar 2 segundos entre cada mensaje
                    await asyncio.sleep(2)

                    if i % 50 == 0:
                        # Esperar 30 segundos cada 50 mensajes
                        asyncio.sleep(30)

                # pusher_client_mercadero.trigger('webhooks', 'telemercadeo', {'message': resultados, 'change': 1})
                return jsonify({'status': 'success', 'data': resultados}), 200
            else:
                resultados = "❌ No se pudo subir el video a META." + \
                    str(media_id)
                # print(resultados)
                # pusher_client_mercadero.trigger('webhooks', 'telemercadeo', {'message': resultados, 'change': 1})
                return jsonify({'status': 'success', 'data': resultados}), 200

        except Exception as e:
            return jsonify({'status': 'error video_informativo_mp4', 'data': str(e)}), 200
"""


async def video_informativo_mp4(urlArchivo, telefonos, campid, idusu, campnom, numeros_manual, filtros_envio, template):
    await asyncio.sleep(10)
    with app.app_context():
        try:
            video_url = urlArchivo
            recipientmerc = os.getenv("PHONE_NUMBER_ID")
            resultados = ''
            status = 'success'
            rechazado = 0
            valido = 0

            i = True
            j = 0
            for numero in telefonos:
                valido = validar_numeros_campania2(numero)
                if valido == 0:
                    rechazado = 0
                    if len(str(numero)) > 0:
                        j += 1
                        try:
                            res = await enviar_template_video_idmedia(numero, video_url)
                            wam_id = res["messages"][0]["id"]
                        except Exception as e:
                            wam_id = 'Rechazado'
                            resultados += f"numero. "
                            rechazado = 1
                        finally:
                            save_res_bot_campania(numero, wam_id, video_url, 'campania', '', '', '', '', '',
                                                '', '', '', '', '', campid, '0', '', '', 1, 0, 0, 0, 0, '', 0, '', recipientmerc, numeros_manual, filtros_envio, template, rechazado, 'video')
                        time.sleep(2)  # Esperar 2 segundos entre cada mensaje

                        if j % 50 == 0:
                            time.sleep(30)  # Esperar 30 segundos cada 50 mensajes

            if resultados == '':
                resultados = f"La carga de mensajes de la campaña {campnom} se envió correctamente."
            else:
                status = 'error'
                resultados = "Los siguientes números 📞 no se pudieron enviar. Por favor rectifíquelos y envíalos nuevamente: \n" + \
                    str(resultados)

            # Configura Pusher con las credenciales que obtuviste de tu cuenta Pusher

            # Está así porque el evento se llama así en la app de laravel
            pusher_client.trigger('webhooks', 'App\\Events\\Comercial', {
                                  'message': resultados, 'change': 1})

            return jsonify({'status': status, 'data': resultados}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'data': str(e)}), 500


async def enviar_template_video_idmedia(numero, media_id):
    HEADERS = {
        'Authorization': f"Bearer {os.getenv('ACCESS_TOKEN')}",
        'Content-Type': 'application/json'
    }
    url = f"https://graph.facebook.com/v23.0/{os.getenv('PHONE_NUMBER_ID')}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "template",
        "template": {
            "name": "video_informativo_mp4",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "video",
                            "video": {
                                "link": media_id
                            }
                        }
                    ]
                }
            ]
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=HEADERS, json=payload)
    return response.json()


def video_informativo(url_youtube, telefonos, campid, idusu):
    time.sleep(300)  # Esperar 5 minutos (300 segundos)
    try:
        # Procesar campaña
        resultados = {}
        i = 0
        for numero in telefonos:
            i += 1
            res = video_informativo_template(numero, url_youtube)
            resultados[numero] = res
            time.sleep(2)  # Esperar 2 segundos entre cada mensaje

            if i % 50 == 0:
                time.sleep(30)  # Esperar 30 segundos cada 50 mensajes

        return jsonify({'status': 'success', 'data': resultados}), 200
    except Exception as e:
        return jsonify({"error_envia_boletin": str(e)}), 500


def video_informativo_template(numero, url_youtube):
    HEADERS = {
        'Authorization': f'Bearer EAAV0YdrwkzMBO9qW0NBbxzi5lgzCl3s1ZAGymRobVM9txc5ZBG4ZBjMZBFVKlSY8PILuj56Dqnund5r9uL5LGN0ZAE11ID6NFSPsRpMyv3sX2JHQ0KMQgbaVblPFnmMPyCUMwiHMGTIQ1TZAWaz8wCEHj4OqyYuGPkHdfiiLkr4ETUekKQVVbtnA1ZCvlU6rybaiAZDZD',
        'Content-Type': 'application/json'
    }
    url = f'https://graph.facebook.com/v21.0/611457702059438/messages'
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "template",
        "template": {
            "name": "video_informativo",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": url_youtube
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()


def promocionar_productos_servicios(urlArchivo, telefonos, campid, idusu, campnom, numeros_manual, filtros_envio, template):
    # time.sleep(300)  # Esperar 5 minutos (300 segundos)
    time.sleep(10)  # Esperar 5 minutos (300 segundos)
    with app.app_context():
        try:
            # url_imagen = url_for('static', filename=f'{carpeta}/{filename}', _external=True)
            # URL de acceso al archivo
            url_imagen = urlArchivo
            recipientmerc = os.getenv("PHONE_NUMBER_ID")
            resultados = ''
            status = 'success'
            rechazado = 0
            valido = 0

            i = True
            j = 0
            for numero in telefonos:
                valido = validar_numeros_campania2(numero)
                if valido == 0:
                    rechazado = 0
                    if len(str(numero)) > 0:
                        j += 1
                        try:
                            res = promocionar_productos_servicios_template(
                                numero, url_imagen, recipientmerc)
                            wam_id = res["messages"][0]["id"]
                        except Exception as e:
                            wam_id = 'Rechazado'
                            resultados += f"numero. "
                            rechazado = 1
                        finally:
                            save_res_bot_campania(numero, wam_id, url_imagen, 'campania', '', '', '', '', '',
                                                '', '', '', '', '', campid, '0', '', '', 1, 0, 0, 0, 0, '', 0, '', recipientmerc, numeros_manual, filtros_envio, template, rechazado, 'image')
                        time.sleep(2)  # Esperar 2 segundos entre cada mensaje

                        if j % 50 == 0:
                            time.sleep(30)  # Esperar 30 segundos cada 50 mensajes

            if resultados == '':
                resultados = f"La carga de mensajes de la campaña {campnom} se envió correctamente."
            else:
                status = 'error'
                resultados = "Los siguientes números 📞 no se pudieron enviar. Por favor rectifíquelos y envíalos nuevamente: \n" + \
                    str(resultados)

            # Configura Pusher con las credenciales que obtuviste de tu cuenta Pusher

            # Está así porque el evento se llama así en la app de laravel
            pusher_client.trigger('webhooks', 'App\\Events\\Comercial', {
                                  'message': resultados, 'change': 1})

            return jsonify({'status': status, 'data': resultados}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'data': str(e)}), 500


def promocionar_productos_servicios_template(numero, url_imagen, recipentmerc):
    HEADERS = {
        'Authorization': f"Bearer {os.getenv('ACCESS_TOKEN')}",
        'Content-Type': 'application/json'
    }
    url = f"https://graph.facebook.com/v23.0/{recipentmerc}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "template",
        "template": {
            "name": "promocionar_productos_servicios",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": url_imagen
                            }
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()

# se sube video a meta por medio de url


async def subir_video_a_meta_url(video_url):
    url = 'https://graph.facebook.com/v21.0/406446499215000/media'
    headers = {
        'Authorization': 'Bearer EAAV0YdrwkzMBO9qW0NBbxzi5lgzCl3s1ZAGymRobVM9txc5ZBG4ZBjMZBFVKlSY8PILuj56Dqnund5r9uL5LGN0ZAE11ID6NFSPsRpMyv3sX2JHQ0KMQgbaVblPFnmMPyCUMwiHMGTIQ1TZAWaz8wCEHj4OqyYuGPkHdfiiLkr4ETUekKQVVbtnA1ZCvlU6rybaiAZDZD'
    }
    data = {'messaging_product': 'whatsapp', 'type': 'video'}

    # Descargar el archivo
    response = requests.get(video_url, stream=True)

    if response.status_code == 200:
        # Se pasa el archivo como un archivo binario al parámetro 'file'
        files = {
            'file': (video_url, response.raw, 'video/mp4')
        }

        # Realizar la solicitud POST para subir el video
        upload_response = requests.post(
            url, headers=headers, data=data, files=files)

        # print("Respuesta subida:", upload_response.text)

        try:
            result = upload_response.json()
            # print("Respuesta subida:", result)
            return result.get('id')
        except Exception as e:
            # print("❌ Error al parsear la respuesta de subida:", e)
            # print("Respuesta sin procesar:", upload_response.text)
            return None
    else:
        print("❌ Error al descargar el video.")
        return None


def save_res_bot_campania(wa_id, wam_id, body, option, nombre, cedula, idemp, nomemp, tipologin, logueo, dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8, outgoing, tempo, vip, especial, consecutivo, area, resp_men, resp_men_body, recipient, nummanual, filtro, plantilla, rechazado, tipo_media):
    try:
        query = "EXEC procEnvioCampania ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query

        # print(f"waid: {wa_id}, wam_id: {wam_id}, body: {body}, option: {option}, nombre: {nombre}, cedula: {cedula}, idemp: {idemp}, nomemp: {nomemp}, tipologin: {tipologin}, logueo: {logueo}, dato1: {dato1}, dato2: {dato2}, dato3: {dato3}, dato4: {dato4}, dato5: {dato5}, dato6: {dato6}, dato7: {dato7}, dato8: {dato8}, outgoing: {outgoing}, tempo: {tempo}, vip: {vip}, especial: {especial}, consecutivo: {consecutivo}, area: {area}, resp_men: {resp_men}, resp_men_body: {resp_men_body}, recipient: {recipient}, nummanual: {nummanual}, filtro: {filtro}, plantilla: {plantilla}, rechazado: {rechazado}")

        cursor.execute(query, (wa_id, wam_id, body, option, nombre, cedula, idemp, nomemp, tipologin, logueo, dato1, dato2, dato3,
                               dato4, dato5, dato6, dato7, dato8, outgoing, tempo, vip, especial, consecutivo, area, resp_men, resp_men_body, recipient, nummanual, filtro, plantilla, rechazado, tipo_media))
        conn.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión
    except Exception as e:
        print(f"❌ Error al ejecutar procEnvioCampania: {e}")


@app.route('/api/send_media_app', methods=['GET', 'POST'])
async def send_media_app():
    print('entra')
    data = request.get_json()
    clicel = data.get('clicel', '')
    nomarc = data.get('nomarc', '')
    usuid = data.get('usuid', 0)
    usunom = data.get('usunom', 0)
    consec = int(data.get('consec', 0))
    area = data.get('perf', '')
    recipient = os.getenv("PHONE_NUMBER_ID")
    url = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + str(nomarc)
    time.sleep(0.5)

    # Obtener la extensión
    # Obtener la extensión, si pone 0 es el nombre del archvio sin extension
    extension = os.path.splitext(nomarc)[1]
    nomarcmp3 = os.path.splitext(nomarc)[0] + '.mp3'
    extension = extension.replace(".", "")  # Eliminar el punto
    if extension == 'aac' or extension == 'amr' or extension == 'mp3' or extension == 'm4a' or extension == 'ogg' or extension == 'wav':
        try:
            convertir_a_mp3(nomarc, nomarcmp3)  # Convertir el archivo a MP3
            body = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + \
                str(nomarcmp3)
            message_data = sendCustomAudio(clicel, body)
            # dato = await send_message(message_data)
            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            print({"Mensaje enviado correctamente": dato})
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'audio', consec, area, recipient)
            os.remove('files/' + nomarc)
            os.remove('files/' + nomarcmp3)
        except Exception as e:
            print({"error en audio": str(e)})
    elif extension == 'jpg' or extension == 'jpeg' or extension == 'png':
        try:
            body = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + str(nomarc)
            message_data = sendCustomImage(clicel, url, '')
            # dato = await send_message(message_data)
            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'image', consec, area, recipient)
        except Exception as e:
            print({"error en imagen": str(e)})
    elif extension == '3gp' or extension == 'mp4':
        try:
            body = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + str(nomarc)
            media_id = get_media_video_id(nomarc)
            message_data = sendCustomVideo(clicel, media_id)
            # dato = await send_message(message_data)
            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'video', consec, area, recipient)

        except Exception as e:
            print({"error en video": str(e)})
    else:
        try:
            body = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + str(nomarc)
            message_data = sendCustomDocumentos(clicel, '', url, nomarc)
            # dato = await send_message(message_data)
            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'document', consec, area, recipient)
        except Exception as e:
            print({"error en documentos": str(e)})

    return "Evento recibido", 200


def save_res_bot_media_consec_app(wa_id, wam_id, body, option, nombre, cedula, idemp, nomemp, tipologin, logueo, dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8, outgoing, tempo, vip, especial, tipo, consec, area, recipient):
    query = "EXEC procCrearMessageMedia2 ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
    conn = get_db_connection()  # Obtener conexión a la base de datos
    cursor = conn.cursor()  # Crear un cursor para ejecutar el query
    cursor.execute(query, (wa_id, wam_id, body, option, nombre, cedula, idemp, nomemp, tipologin, logueo, dato1, dato2,
                   dato3, dato4, dato5, dato6, dato7, dato8, outgoing, tempo, vip, especial, tipo, consec, area, recipient))
    conn.commit()  # Confirmar cambios (si el procedimiento realiza modificaciones)
    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión

# convertir un aduio a mp3 por medio de ffmpeg


def convertir_a_mp3(archivo_entrada, archivo_salida, bitrate="192k"):
    """Convierte un archivo de audio a MP3 usando FFmpeg con opciones."""
    try:
        url = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + \
            str(archivo_entrada)
        folder_path = 'files/'  # Ruta donde deseas guardar el archivo
        # Asegúrate de que la carpeta 'files' exista
        os.makedirs(folder_path, exist_ok=True)
        # Ruta completa del archivo de la nube
        file_path = os.path.join(folder_path, archivo_entrada)

        try:
            response = requests.get(url)  # Descargar el archivo desde la URL
            response.raise_for_status()  # Lanza un error si el código de respuesta no es 200

            # Guardar el archivo
            with open(file_path, 'wb') as file:
                file.write(response.content)

            print(f"✅ Archivo descargado y guardado en {file_path}")

            if ffmpegNube == 1:
                # Ejecuta el comando FFmpeg con opciones. Para el servidor de azure
                subprocess.run([ffmpeg_path, '-y', '-i', file_path, '-b:a',
                               bitrate, os.path.join(folder_path, archivo_salida)])
            else:
                # Ejecuta el comando FFmpeg con opciones. Es mi entorno local del pc
                subprocess.run(['ffmpeg', '-y', '-i', file_path, '-b:a',
                               bitrate, os.path.join(folder_path, archivo_salida)])

            print(f"Archivo convertido a MP3: {archivo_salida}")

            # Se envia el archivo al glpi ya convertido en mp3
            urlenviofile = "https://glpi-siicsa.azurewebsites.net/wh_recibirfilewhbe.php"
            # Abre el archivo en modo binario
            file_path = os.path.join(folder_path, archivo_salida)
            with open(file_path, 'rb') as f:
                # Preparar el archivo para ser enviado
                files = {'attachment': (file_path, f)}
                response = requests.post(urlenviofile, files=files)

            if response.status_code == 200:
                print("Archivo enviado correctamente.")
                print("Respuesta del servidor:", response.text)
            else:
                print(
                    f"Error al enviar el archivo. Código de estado: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Error al descargar el archivo: {e}")

    except FileNotFoundError:
        print("Error: FFmpeg no se encontró en el sistema. Asegúrate de que esté instalado y en la variable PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir el archivo: {e}")

# Función para obtener el Media ID del archivo de video


def get_media_video_id(nomarc):
    folder_path = 'files/'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, nomarc)

    # descargar archvio desde la nube
    url = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + str(nomarc)
    # Realizar la solicitud GET para obtener el archivo
    response = requests.get(url)
    if response.status_code == 200:
        # Guardar el archivo en la ruta especificada
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Archivo descargado y guardado en: {file_path}")
    else:
        print(
            f"Error al descargar el archivo. Código de estado: {response.status_code}")

    media_api_url = f"https://graph.facebook.com/{os.getenv('VERSION')}/{os.getenv('PHONE_NUMBER_ID')}/media"
    media_headers = {
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"
    }

    # Abrir el archivo de video
    with open(file_path, 'rb') as video_file:
        # Datos del archivo que se va a subir
        files = {
            # Abre el archivo y establece su tipo MIME
            'file': (file_path, video_file, 'video/mp4'),
            # Parámetro para indicar que es un mensaje de WhatsApp
            'messaging_product': (None, 'whatsapp')
        }

        try:
            # Subir el archivo
            media_response = requests.post(
                media_api_url, headers=media_headers, files=files)
        except Exception as e:
            print({"error en documentos": str(e)})

    # Ver la respuesta
    if media_response.status_code == 200:
        # media_id = response.json()['id']
        media_data = media_response.json()
        return media_data['id']
    else:
        print(f"Error al subir el archivo: {media_response.status_code}")
        print(f"Detalles del error: {media_response.json()}")
        raise Exception(
            f"Error al subir el archivo de audio: {media_response.json()}")


# --- Endpoint para subir archivo ---
@app.route("/api/uploadFilesActividad", methods=["POST"])
def upload_file():

    fileRUT = request.files.get('fileRUT', None)
    fileCOT = request.files.get('fileCOT', None)

    filenameRUT = ''
    urlRUT = ''
    carpetaRUT = "archivosRUT"
    filenameCOT = ''
    urlCOT = ''
    carpetCOT = "archivosCOT"

    from datetime import datetime
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    try:
        # Asegura contenedor (idempotente)
        container_client = blob_service_client.get_container_client(
            container_name)
        try:
            container_client.create_container()
        except Exception:
            pass  # Si ya existe, no hace nada

        # Procesar fileRUT si existe y tiene nombre
        if fileRUT and fileRUT.filename:
            try:
                filenameRUT = f"{carpetaRUT}/{fecha_actual}-{fileRUT.filename}"
                blob_client = container_client.get_blob_client(filenameRUT)
                blob_client.upload_blob(fileRUT, overwrite=True)
                sas_token_rut = generate_blob_sas(
                    account_name=blob_service_client.account_name,
                    container_name=container_name,
                    blob_name=filenameRUT,
                    account_key=blob_service_client.credential.account_key,
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + relativedelta(years=10)
                )
                urlRUT = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{filenameRUT}?{sas_token_rut}"
            except Exception as e:
                print(f"❌ Error al subir fileRUT: {e}")

        # Procesar fileCOT si existe y tiene nombre
        if fileCOT and fileCOT.filename:
            try:
                filenameCOT = f"{carpetCOT}/{fecha_actual}-{fileCOT.filename}"
                blob_client = container_client.get_blob_client(filenameCOT)
                blob_client.upload_blob(fileCOT, overwrite=True)
                sas_token_cot = generate_blob_sas(
                    account_name=blob_service_client.account_name,
                    container_name=container_name,
                    blob_name=filenameCOT,
                    account_key=blob_service_client.credential.account_key,
                    permission=BlobSasPermissions(read=True),
                    expiry=datetime.utcnow() + relativedelta(years=10)
                )
                urlCOT = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{filenameCOT}?{sas_token_cot}"
            except Exception as e:
                print(f"❌ Error al subir fileCOT: {e}")

        return jsonify({
            "message": "Archivos subidos correctamente",
            "filenameRUT": filenameRUT,
            "urlRUT": urlRUT,
            "filenameCOT": filenameCOT,
            "urlCOT": urlCOT
        }), 200

    except Exception as e:
        print(f"❌ Error general en uploadFilesActividad: {e}")
        return jsonify({
            "message": "Archivos subidos correctamente",
            "filenameRUT": filenameRUT,
            "urlRUT": urlRUT,
            "filenameCOT": filenameCOT,
            "urlCOT": urlCOT
        }), 200


# ==========================================================
#   CREADO POR LEANDRO 20250828 - INICIO
# ==========================================================
@app.route('/api/messages_app', methods=['GET', 'POST'])
def messages_app():
    data = request.get_json()
    clicel = data['clicel']
    recipient = data['recipient']  # celular del cliente

    if 'limit' in data:
        limit = data['limit']
        offset = data['offset']
        limit = limit + offset

    try:
        if 'limit' in data:
            query = "EXEC procBuscarSubConsultaMercadeoApp ?, ?, ?, ?"
            conn = get_db_connection()  # Obtener conexión a la base de datos
            cursor = conn.cursor()  # Crear un cursor para ejecutar el query
            cursor.execute(query, (clicel, recipient, offset, limit))
        # cursor.commit()
        else:
            query = "EXEC procBuscarSubConsultaMercadeo ?, ?"
            conn = get_db_connection()  # Obtener conexión a la base de datos
            cursor = conn.cursor()  # Crear un cursor para ejecutar el query
            cursor.execute(query, (clicel, recipient))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Send_media con blob storage
@app.route('/api/send_media_app2', methods=['GET', 'POST'])
async def send_media_app2():
    print('entra')

    clicel = request.form.get('clicel')
    usuid = request.form.get('usuid')
    usunom = request.form.get('usunom')
    consec = request.form.get('consec')
    area = request.form.get('perf')
    recipient = '611457702059438'

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    mime = file.mimetype  # Obtener el tipo MIME del archivo
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # guardar archivo
    nomarc = file.filename
    filepath = os.path.join('files', file.filename)
    file.save(filepath)

    # Obtener la extensión
    # Obtener la extensión, si pone 0 es el nombre del archvio sin extension
    extension = os.path.splitext(nomarc)[1]
    extension = extension.replace(".", "")  # Eliminar el punto
    if extension == 'aac' or extension == 'amr' or extension == 'mp3' or extension == 'm4a' or extension == 'ogg' or extension == 'wav' or extension == 'm4a':
        try:
            nomarcmp3 = os.path.splitext(nomarc)[0] + '.mp3'
            # Convierte el archivo a mp3 y devuelve la URL del archivo
            body = convertir_audio_mp3_blob(nomarc, nomarcmp3)
            message_data = sendCustomAudio(clicel, body)

            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            print({"Mensaje enviado correctamente": dato})
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'audio', consec, area, recipient)

            mess = cargar_message(wam_id)
            data = mess[0]
            pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {
                                  'message': data, 'change': 1})

            # Elimina el archivo entrante
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)
            # Elimina el archivo mp3 local
            filepath = os.path.join('files', nomarcmp3)
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)
        except Exception as e:
            print({"error en audio": str(e)})
    elif extension == 'jpg' or extension == 'jpeg' or extension == 'png':
        try:
            # Se envia el archivo al blob storage y retorna la URL del archivo
            body = uploadfileblob(filepath, 'media')
            message_data = sendCustomImage(clicel, body, '')
            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'image', consec, area, recipient)

            mess = cargar_message(wam_id)
            data = mess[0]
            pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {
                                  'message': data, 'change': 1})

            # Elimina el archivo entrante
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)

        except Exception as e:
            print({"error en imagen": str(e)})
    elif extension == '3gp' or extension == 'mp4':
        try:
            # Se envia el archivo al blob storage y retorna la URL del archivo
            body = uploadfileblob(filepath, 'media')
            media_id = get_media_video_id_blob(filepath)
            message_data = sendCustomVideo(clicel, media_id)
            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'video', consec, area, recipient)

            mess = cargar_message(wam_id)
            data = mess[0]
            pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {
                                  'message': data, 'change': 1})

            # Elimina el archivo entrante
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)

            mess = cargar_message(wam_id)
            data = mess[0]
            pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {
                                  'message': data, 'change': 1})

            # Elimina el archivo entrante
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)

            mess = cargar_message(wam_id)
            data = mess[0]
            pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {
                                  'message': data, 'change': 1})

            # Elimina el archivo entrante
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)

        except Exception as e:
            print({"error en video": str(e)})
    else:
        try:
            # Se envia el archivo al blob storage y retorna la URL del archivo
            body = uploadfileblob(filepath, 'media')
            message_data = sendCustomDocumentos(clicel, '', body, nomarc)
            # dato = await send_message(message_data)
            dato = await send_message_pni(message_data, recipient)
            wam_id = dato['response']['messages'][0]['id']
            save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'document', consec, area, recipient)

            mess = cargar_message(wam_id)
            data = mess[0]
            pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {
                                  'message': data, 'change': 1})

            # Elimina el archivo entrante
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)

        except Exception as e:
            print({"error en documentos": str(e)})

    return "Evento recibido", 200


# subir archivo al blob storage y retorna la url del archivo
@app.route("/api/uploadfileblobWeb", methods=['POST'])
def uploadfileblobWeb():
    carpeta = "media"
    file = request.files["file"]

    if not file or not file.filename:
        return jsonify({"message": "No se envió ningún archivo"}), 400

    # Asegura contenedor (idempotente)
    try:
        container_client = blob_service_client.get_container_client(
            container_name)
        # si existe, lanzará excepción que ignoramos abajo
        container_client.create_container()
    except Exception:
        pass

    # Nombre único: yyyy/mm/dd/UUID_nombre-seguro.ext
    original_name = secure_filename(file.filename)
    now = datetime.now()
    today_prefix = now.strftime("%Y%m%d%H%M%S") + \
        f"{int(now.microsecond / 1000):03d}"
    unique_name = f"{carpeta}/{uuid.uuid4()}_{today_prefix}"

    # Content-Type correcto
    content_type, _ = mimetypes.guess_type(original_name)
    content_type = content_type or "application/octet-stream"

    blob_client = container_client.get_blob_client(unique_name)

    try:
        # Sube desde stream para no cargar todo en memoria
        blob_client.upload_blob(
            file.stream,
            overwrite=True,
            content_settings=ContentSettings(content_type=content_type)
        )

        account_name = blob_service_client.account_name
        blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{unique_name}"

        # --- Opción recomendada: SAS corta (ej. 24h) para descarga ---
        sas_token_short = generate_blob_sas(
            account_name=account_name,
            container_name=container_name,
            blob_name=unique_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=24)
        )
        sas_url_24h = f"{blob_url}?{sas_token_short}"

        # --- Opción alternativa: SAS larga (ej. 10 años) ---
        sas_token_long = generate_blob_sas(
            account_name=account_name,
            container_name=container_name,
            blob_name=unique_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + relativedelta(years=10)
        )
        sas_url_10y = f"{blob_url}?{sas_token_long}"

        return sas_url_10y

        """return jsonify({
            "message": "Archivo subido correctamente",
            "filename_original": original_name,
            "blob_name": unique_name,
            "content_type": content_type,
            "blob_url": blob_url,          # URL permanente sin credenciales (requiere SAS para leer si el contenedor es privado)
            "download_url_24h": sas_url_24h,
            "download_url_10y": sas_url_10y
        }), 200"""

    except Exception as e:
        print("❌ Error:", str(e))
        """return jsonify({
            "message": "Error al subir archivo",
            "error": str(e)
        }), 500"""


# Sube archivo al blob en una carpeta especifica
# @app.route("/api/uploadfileblob", methods=['POST', 'GET'])
def uploadfileblob(ruta, carpeta):
    # ruta = 'files/grabacion_1756303985529.mp3'
    # carpeta = "media"
    # Asegura contenedor (idempotente)
    try:
        container_client = blob_service_client.get_container_client(
            container_name)
        # si existe, lanzará excepción que ignoramos abajo
        container_client.create_container()
    except Exception:
        pass

    # Nombre único
    original_name = secure_filename(os.path.basename(ruta))
    now = datetime.now()
    today_prefix = now.strftime("%Y%m%d%H%M%S") + \
        f"{int(now.microsecond / 1000):03d}"
    unique_name = f"{carpeta}/{uuid.uuid4()}_{today_prefix}.{original_name.split('.')[-1]}"
    print(unique_name)
    # Content-Type correcto
    content_type, _ = mimetypes.guess_type(original_name)
    content_type = content_type or "application/octet-stream"

    blob_client = container_client.get_blob_client(unique_name)

    try:
        # Subida desde archivo local
        with open(ruta, "rb") as data:
            blob_client.upload_blob(
                data,
                overwrite=True,
                content_settings=ContentSettings(content_type=content_type)
            )

        account_name = blob_service_client.account_name
        blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{unique_name}"

        # --- Opción recomendada: SAS corta (ej. 24h) para descarga ---
        sas_token_short = generate_blob_sas(
            account_name=account_name,
            container_name=container_name,
            blob_name=unique_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=24)
        )
        sas_url_24h = f"{blob_url}?{sas_token_short}"

        # --- Opción alternativa: SAS larga (ej. 10 años) ---
        sas_token_long = generate_blob_sas(
            account_name=account_name,
            container_name=container_name,
            blob_name=unique_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + relativedelta(years=10)
        )
        sas_url_10y = f"{blob_url}?{sas_token_long}"

        return sas_url_10y

        """return jsonify({
            "message": "Archivo subido correctamente",
            "filename_original": original_name,
            "blob_name": unique_name,
            "content_type": content_type,
            "blob_url": blob_url,          # URL permanente sin credenciales (requiere SAS para leer si el contenedor es privado)
            "download_url_24h": sas_url_24h,
            "download_url_10y": sas_url_10y
        }), 200"""

    except Exception as e:
        print("❌ Error:", str(e))
        """return jsonify({
            "message": "Error al subir archivo",
            "error": str(e)
        }), 500"""


@app.route("/api/send_media_audio", methods=['GET', 'POST'])
async def send_media_audio():
    clicel = request.form.get('clicel')
    usuid = request.form.get('usuid')
    usunom = request.form.get('usunom')
    consec = request.form.get('consec')
    area = request.form.get('perf')
    extension = request.form.get('ext')
    mime = request.form.get('mime')
    recipient = os.getenv("PHONE_NUMBER_ID")
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    mime = file.mimetype  # Obtener el tipo MIME del archivo
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # guardar archivo
    nomarc = file.filename
    filepath = os.path.join('files', file.filename)
    file.save(filepath)

    # return jsonify({"status": "success", "filename": file.filename})
    # Obtener la extensión
    # Obtener la extensión, si pone 0 es el nombre del archvio sin extension
    extension = os.path.splitext(nomarc)[1]
    extension = extension.replace(".", "")  # Eliminar el punto

    try:
        nomarcmp3 = os.path.splitext(nomarc)[0] + '.mp3'
        body = convertir_audio_mp3_blob(
            nomarc, nomarcmp3)  # Convertir el archivo a MP3
        # body = "https://glpi-siicsa.azurewebsites.net/WHWEB/" + str(nomarcmp3)
        message_data = sendCustomAudio(clicel, body)

        try:
            dato = await send_message_pni(message_data, recipient)
            print({"Mensaje enviado correctamente": dato})
        except Exception as e:
            print({"error al enviar mensaje de audio": str(e)})
        wam_id = dato['response']['messages'][0]['id']
        print({"Mensaje enviado correctamente": dato})
        save_res_bot_media_consec_app(clicel, wam_id, body, 'asesor en proceso', '', '', '', '',
                                      '', '', '', '', '', '', '', '', '', '', 1, 0, 0, 0, 'audio', consec, area, recipient)

        mess = cargar_message(wam_id)
        data = mess[0]
        pusher_client.trigger('webhooks', 'App\\Events\\Webhook', {
                              'message': data, 'change': 1})
        # Elimina el archivo entrante
        if os.path.exists(filepath) and os.path.isfile(filepath):
            os.remove(filepath)
        # Elimina el archivo mp3 local
        filepath = os.path.join('files', nomarcmp3)
        if os.path.exists(filepath) and os.path.isfile(filepath):
            os.remove(filepath)
    except Exception as e:
        print({"error en audio": str(e)})
        return "Error al procesar el audio", 500

    return "Audio enviado correctamente", 200

    # convertir un aduio a mp3 por medio de ffmpeg


def convertir_audio_mp3(archivo_entrada, archivo_salida, bitrate="192k"):
    """Convierte un archivo de audio a MP3 usando FFmpeg con opciones."""
    try:
        folder_path = 'files/'  # Ruta donde deseas guardar el archivo
        # Asegúrate de que la carpeta 'files' exista
        os.makedirs(folder_path, exist_ok=True)
        # Ruta completa del archivo de la nube
        file_path = os.path.join(folder_path, archivo_entrada)

        try:
            if ffmpegNube == 1:
                # Ejecuta el comando FFmpeg con opciones. Para el servidor de azure
                subprocess.run([ffmpeg_path, '-y', '-i', file_path, '-b:a',
                               bitrate, os.path.join(folder_path, archivo_salida)])
            else:
                # Ejecuta el comando FFmpeg con opciones. Es mi entorno local del pc
                subprocess.run(['ffmpeg', '-y', '-i', file_path, '-b:a',
                               bitrate, os.path.join(folder_path, archivo_salida)])

            print(f"Archivo convertido a MP3: {archivo_salida}")

            # Se envia el archivo al glpi ya convertido en mp3
            urlenviofile = "https://glpi-siicsa.azurewebsites.net/wh_recibirfilewhbe.php"
            # Abre el archivo en modo binario
            file_path = os.path.join(folder_path, archivo_salida)
            with open(file_path, 'rb') as f:
                # Preparar el archivo para ser enviado
                files = {'attachment': (file_path, f)}
                response = requests.post(urlenviofile, files=files)

            if response.status_code == 200:
                print("Archivo enviado correctamente.")
                print("Respuesta del servidor:", response.text)
            else:
                print(
                    f"Error al enviar el archivo. Código de estado: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Error al descargar el archivo: {e}")

    except FileNotFoundError:
        print("Error: FFmpeg no se encontró en el sistema. Asegúrate de que esté instalado y en la variable PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir el archivo: {e}")


def convertir_audio_mp3_blob(archivo_entrada, archivo_salida, bitrate="192k"):
    """Convierte un archivo de audio a MP3 usando FFmpeg con opciones."""
    try:
        folder_path = 'files/'  # Ruta donde deseas guardar el archivo
        # Asegúrate de que la carpeta 'files' exista
        os.makedirs(folder_path, exist_ok=True)
        # Ruta completa del archivo de la nube
        file_path = os.path.join(folder_path, archivo_entrada)

        try:
            if ffmpegNube == 1:
                # Ejecuta el comando FFmpeg con opciones. Para el servidor de azure
                subprocess.run([ffmpeg_path, '-y', '-i', file_path, '-b:a',
                               bitrate, os.path.join(folder_path, archivo_salida)])
            else:
                # Ejecuta el comando FFmpeg con opciones. Es mi entorno local del pc
                subprocess.run(['ffmpeg', '-y', '-i', file_path, '-b:a',
                               bitrate, os.path.join(folder_path, archivo_salida)])

            print(f"Archivo convertido a MP3: {archivo_salida}")

            # Se envia el archivo al blob ya convertido en mp3
            file_path = os.path.join(folder_path, archivo_salida)
            respuesta = uploadfileblob(file_path, 'media')

            return respuesta

        except requests.exceptions.RequestException as e:
            print(f"❌ Error al convertir archivo: {e}")
            return f"❌ Error al convertir archivo: {e}"

    except FileNotFoundError:
        print("Error: FFmpeg no se encontró en el sistema. Asegúrate de que esté instalado y en la variable PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir el archivo: {e}")


def get_media_video_id_blob(file_path):
    media_api_url = f"https://graph.facebook.com/{os.getenv('VERSION')}/{os.getenv('PHONE_NUMBER_ID')}/media"
    media_headers = {"Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"}

    # Abrir el archivo de video
    with open(file_path, 'rb') as video_file:
        # Datos del archivo que se va a subir
        files = {
            # Abre el archivo y establece su tipo MIME
            'file': (file_path, video_file, 'video/mp4'),
            # Parámetro para indicar que es un mensaje de WhatsApp
            'messaging_product': (None, 'whatsapp')
        }

        try:
            # Subir el archivo
            media_response = requests.post(
                media_api_url, headers=media_headers, files=files)
        except Exception as e:
            print({"error en documentos": str(e)})

    # Ver la respuesta
    if media_response.status_code == 200:
        # media_id = response.json()['id']
        media_data = media_response.json()
        return media_data['id']
    else:
        print(f"Error al subir el archivo: {media_response.status_code}")
        print(f"Detalles del error: {media_response.json()}")
        raise Exception(
            f"Error al subir el archivo de audio: {media_response.json()}")

# cargar Roles de las Preguntas Frecuentes IA
# Esta ruta retorna los Roles de las Preguntas Frecuentes de PQR


@app.route("/api/cargarRolesIA", methods=["GET", "POST"])
def cargarRolesIA():
    print("Cargando roles IA...")
    try:
        data = request.get_json()
        idrol = data.get('idrol')

        query = "EXEC procIaCargarRol ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idrol))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        # Imprime el stack completo en los logs de Azure
        traceback.print_exc()
        return jsonify({'status': 'error', 'data': str(e)}), 500

# crear Roles de las Preguntas Frecuentes
# Esta ruta crea Roles para las Preguntas Frecuentes de PQR


@app.route("/api/crearRol", methods=["GET", "POST"])
def crearRol():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            nombre = data.get('nombre', '')
            contenido = data.get('contenido', '')
            idusu = data.get('idusu', '')

        query = "EXEC procIaCrearRol ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar los parámetros como una tupla
        cursor.execute(
            query, (nombre, contenido, idusu))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Validación: si existe == 0 se editó bien, si no, ya existe el nombre
        existe_result = resultados_dict[0].get(
            'existe', 0) if resultados_dict else 1
        if existe_result == 0:
            return {'status': 'success', 'data': resultados_dict}, 200
        else:
            return jsonify({'status': 'warning', 'message': 'Ya existe un rol con ese nombre.'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Editar un rol IA


@app.route("/api/editarRolIA", methods=["GET", "POST"])
def editarRolIA():
    try:
        data = request.get_json()
        idrol = data.get('idrol', '')
        nombre = data.get('nombre', '')
        contenido = data.get('contenido', '')
        activo = data.get('activo', '')
        # Imprimir datos recibidos para depuración
        print(f"Datos recibidos: {data}")

        query = "EXEC procIaEditarRol ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idrol, nombre, contenido, activo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Validación: si existe == 0 se editó bien, si no, ya existe el nombre
        existe_result = resultados_dict[0].get(
            'existe', 0) if resultados_dict else 1
        if existe_result == 0:
            return {'status': 'success', 'data': resultados_dict}, 200
        else:
            return jsonify({'status': 'warning', 'message': 'Ya existe un rol con ese nombre.'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


@app.route("/api/cargarPreguntasFrecuentes", methods=["GET", "POST"])
def cargarPreguntasFrecuentes():
    try:
        data = request.get_json()
        idpregunta = data.get('idpregunta')

        query = "EXEC procIaCargarPregunta ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idpregunta))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        # Imprime el stack completo en los logs de Azure
        traceback.print_exc()
        return jsonify({'status': 'error', 'data': str(e)}), 500

# Editar una pregunta frecuente


@app.route("/api/editarPreguntaFrecuente", methods=["GET", "POST"])
def editarPreguntaFrecuente():
    try:
        data = request.get_json()
        idPregunta = data.get('idPregunta', '')
        pregunta = data.get('pregunta', '')
        respuesta = data.get('respuesta', '')
        estado = int(data.get('estado', 0))
        idconte = int(data.get('idconte', 0))
        # Imprimir datos recibidos para depuración
        print(f"Datos recibidos: {data}")

        query = "EXEC procIaEditarPregunta ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idPregunta, pregunta, respuesta,
                       estado, idconte))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Validación: si existe == 0 se editó bien, si no, ya existe el nombre
        existe_result = resultados_dict[0].get(
            'existe', 0) if resultados_dict else 1
        if existe_result == 0:
            return {'status': 'success', 'data': resultados_dict}, 200
        else:
            return jsonify({'status': 'warning', 'message': 'Ya existe una pregunta con ese nombre.'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500

# Procedimiento para crear o editar campañas


@app.route("/api/CrearPreguntaFrecuente", methods=["GET", "POST"])
def CrearPreguntaFrecuente():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            pregunta = data.get('pregunta', '')
            respuesta = data.get('respuesta', '')
            usuario = int(data.get('usuario', ''))
            estado = int(data.get('estado', 0))
            idconte = int(data.get('idconte', 0))

        query = "EXEC procIaCrearPregunta ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar los parámetros como una tupla
        cursor.execute(
            query, (pregunta, respuesta, usuario, estado, idconte))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Validación: si id > 0 se creó bien, si no, ya existe el nombre
        id_result = resultados_dict[0].get('id', 0) if resultados_dict else 0
        if id_result > 0:
            return {'status': 'success', 'data': resultados_dict}, 200
        else:
            return jsonify({'status': 'warning', 'message': 'Ya existe una pregunta con ese nombre.'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargarIntencionIA", methods=["GET", "POST"])
def cargarIntencionIA():
    try:
        data = request.get_json()
        idintencion = data.get('idintencion')

        query = "EXEC procIaCargarIntencion ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idintencion))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        # Imprime el stack completo en los logs de Azure
        traceback.print_exc()
        return jsonify({'status': 'error', 'data': str(e)}), 500


@app.route("/api/crearIntencionIA", methods=["GET", "POST"])
def crearIntencionIA():
    try:
        data = request.get_json(silent=True)
        if data:
            data = request.get_json()
            intencion = data.get('intencion', '')
            url = data.get('url', '')
            idconte = int(data.get('idrol', 0))
            contenidopdf = data.get('contenidopdf', '')
            idusu = int(data.get('usu', 0))

        query = "EXEC procIaCrearIntencion ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        # Pasar los parámetros como una tupla
        cursor.execute(
            query, (intencion, url, idconte, contenidopdf, idusu))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Validación: si existe == 0 se editó bien, si no, ya existe el nombre
        existe_result = resultados_dict[0].get(
            'existe', 0) if resultados_dict else 1
        if existe_result == 0:
            return {'status': 'success', 'data': resultados_dict}, 200
        else:
            return jsonify({'status': 'warning', 'message': 'Ya existe un rol con ese nombre.'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/editarIntencion", methods=["GET", "POST"])
def editarIntencion():
    try:
        data = request.get_json()
        idIntencion = int(data.get('idIntencion', ''))
        intencion = data.get('intencion', '')
        url = data.get('url', '')
        idconte = int(data.get('idrol', 0))
        contenido = data.get('contenido', '')
        activo = int(data.get('activo', 0))
        # Imprimir datos recibidos para depuración
        print(f"Datos recibidos: {data}")

        query = "EXEC procIaEditarIntencion ?, ?, ?, ?, ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idIntencion, intencion,
                       url, contenido, idconte, activo))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Validación: si existe == 0 se editó bien, si no, ya existe el nombre
        existe_result = resultados_dict[0].get(
            'existe', 0) if resultados_dict else 1
        if existe_result == 0:
            return {'status': 'success', 'data': resultados_dict}, 200
        else:
            return jsonify({'status': 'warning', 'message': 'Ya existe un rol con ese nombre.'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


@app.route("/api/extraerTextoPdf", methods=["GET", "POST"])
async def extraerTextoPdf():
    texto = ''
    ruta_pdf = ''
    umbral_minimo = 100

    file = request.files.get("file")

    if not file or not file.filename:
        return jsonify({"message": "No se envió ningún archivo"}), 400

    # nomarc = secure_filename(file.filename)
    ruta_pdf = os.path.join('files', file.filename)
    file.save(ruta_pdf)
    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            pagina_texto = pagina.extract_text()
            if pagina_texto:
                texto += pagina_texto + '\n'

    if len(texto.strip()) < umbral_minimo:
        print("Texto insuficiente detectado, aplicando OCR...")
        texto = ''
        # paginas_imagen = convert_from_path(ruta_pdf, poppler_path=r'D:\poppler\Library\bin')
        paginas_imagen = convert_from_path(
            ruta_pdf, dpi=300, poppler_path=r'D:\poppler\Library\bin')
        for pagina_imagen in paginas_imagen:
            texto += pytesseract.image_to_string(
                pagina_imagen, lang='spa') + '\n'

    texto = await formatearTextoConIA(texto)

    return {'status': 'success', 'texto': texto}, 200


async def formatearTextoConIA(message: str):
    rol = f"""
        Rol: Restaurador de texto de PDF/OCR (solo texto plano)

        Objetivo: Recibir un texto crudo extraído de un PDF (potencialmente con tablas mal pegadas, cortes de línea, encabezados/pies de página repetidos, guiones de final de línea, caracteres raros y frases incompletas) y devolver un texto plano claro, coherente y legible para usuarios finales.

        Instrucciones estrictas:
        No inventes información. Si falta contenido o hay dudas, marca con [?] o [...] sin agregar datos nuevos.
        Corrige errores comunes de OCR (l—>l, 0↔O, |↔l, comas/puntos en números) solo cuando sea obvio por contexto.
        Une palabras cortadas por guion al final de línea (ej.: “infor- mación” → “información”).
        Reconstruye párrafos: elimina saltos de línea innecesarios dentro de una misma oración y conserva un salto de línea vacío entre párrafos.
        Elimina ruido: números de página, encabezados/pies repetidos, marcas de agua, líneas de separación decorativas y numeraciones huérfanas.
        Listas: detecta listas y formátalas con guiones - o numeración 1., cada ítem en su propia línea.
        Tablas: conviértelas a texto plano alineado por filas. Encabezado claro, luego filas con separadores simples como | (sin ASCII art complejo). Si una celda está incompleta, marca [?].
        Títulos y secciones: detecta jerarquía (TÍTULO, subtítulos) y represéntala en texto plano con mayúsculas y/o prefijos como ## (solo texto, sin Markdown avanzado).
        Unidades, fechas y cantidades: conserva con fidelidad y formato consistente (p. ej., 1.234,56 o 1,234.56; no cambies arbitrariamente).
        Quita duplicados consecutivos y espacios múltiples; normaliza comillas y guiones.
        Mantén el idioma original del contenido (español colombiano); no traduzcas.
        No incluyas metadatos, explicaciones del proceso ni notas fuera del contenido final. Salida = solo el texto depurado.
        En caso que el texto no lo puedas interpretar o llegue vacío, por favor devolver "No se pudo interpretar el contenido del archivo." sin comillas.

        Formato de salida (obligatorio):
        Texto plano únicamente.
        Estructurado por secciones y párrafos.
        Listas con - o 1.
        Tablas en filas Columna1 | Columna2 | Columna3 (una fila por línea).
        Sin cabeceras técnicas, sin código, sin backticks.

        Entrada del usuario:
        {message}

        Salida deseada:
        Mismo contenido, pero limpio, coherente y fácil de leer, siguiendo las reglas anteriores.

        Criterios de calidad:
        Claridad > literalidad cuando existan evidentes artefactos de OCR.
        Cero alucinaciones.
        Marcado explícito de incertidumbre con [?] o [...].

        Ejemplo breve (ilustrativo):
        Entrada:
        “PÁG 3 — Informe
        Produc- ción 2024
        Tabla:
        Mes Ene Feb Mar
        Val or 1.2O0 1,350 1.4OO
        — — —
        Conf… (ver imagen)

        Fin”

        Salida:
        “INFORME

        Producción 2024

        Mes | Valor
        Ene | 1200
        Feb | 1,350
        Mar | 1400

        Nota: contenido faltante en sección “Conf[...]” [?]”"""

    conversation = []
    conversation.append({"role": "system", "content": rol})

    # Enviar mensaje a OpenAI
    try:
        response = await client.chat.completions.create(model="gpt-4o-mini", messages=conversation)
        bot_response = response.choices[0].message.content.strip().encode(
            'utf-8').decode('utf-8')  # Obtiene la respuesta del modelo
        bot_response = bot_response.strip()
        print("Respuesta IA formateo texto:", bot_response)

        # Mostrar resultados
        return bot_response

    except Exception as e:
        return 'Error'


@app.route("/api/cargarfiltrosDestinatarios", methods=["GET", "POST"])
def cargarfiltrosDestinatarios():
    try:

        query = "EXEC procFiltrosDestinatarios"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/switchRolIA", methods=["GET", "POST"])
def switchRolIA():
    try:
        data = request.get_json()
        id = int(data.get('id', 0))

        query = "EXEC procSwicthRol ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (id,))

        cursor.commit()  # Confirmar los cambios en la base de datos

        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        return {'status': 'success', 'data': id}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'data': e}), 500


# Cargar Procesar archivo de números manuales
@app.route("/api/procesarArchivoNumeros", methods=["GET", "POST"])
def procesarArchivoNumeros():
    try:
        # Recibe el archivo desde el form-data
        if 'archivo' not in request.files:
            return jsonify({'status': 'error', 'message': 'No se envió el archivo'}), 400
        archivo = request.files['archivo']
        filename = archivo.filename
        extension = filename.split('.')[-1].lower()

        numeros = []
        if extension == 'txt':
            # Procesar archivo txt
            contenido = archivo.read().decode('utf-8')
            lineas = contenido.splitlines()
            for linea in lineas:
                num = linea.strip()
                if num:  # Solo si la línea no está vacía
                    numeros.append(num)
        elif extension in ['xls', 'xlsx']:
            import io
            import pandas as pd
            archivo_bytes = archivo.read()
            excel = pd.read_excel(io.BytesIO(archivo_bytes))
            # Se asume que la segunda columna es la de los números
            if excel.shape[1] < 2:
                return jsonify({'status': 'error', 'message': 'El archivo Excel no tiene la cantidad de columnas esperada'}), 400
            columna_numeros = excel.iloc[:, 1]
            for num in columna_numeros:
                if pd.notnull(num):
                    numeros.append(str(num).strip())
        else:
            return jsonify({'status': 'error', 'message': 'Tipo de archivo no soportado. Solo se permiten .txt o .xls/.xlsx'}), 400

        # Formatear la respuesta como una cadena separada por comas y espacio
        numeros_str = ', '.join(numeros)
        return jsonify({'status': 'success', 'data': numeros_str}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# ==========================================================
#   CREADO POR LEANDRO 20250828 - FINAL
# ==========================================================

@app.route("/api/cargarareascomerciales", methods=["GET", "POST"])
def cargarareascomerciales():
    try:

        query = "EXEC procCargarAreasComerciales"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route("/api/cargarcomerciales", methods=["GET", "POST"])
def cargarcomerciales():
    try:
        data = request.get_json()
        idac = data.get('idac', 0)
        
        query = "EXEC procCargarComercialesArea ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idac,))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
# Procedimiento para saber si esa red social en particular ha pasao las 24 horas de actividad   
@app.route("/api/activo24horas", methods=["GET", "POST"])
def activo24horas():
    try:
        data = request.get_json()
        idcli = int(data.get('idcli', 0))
        canal = data.get('canal', '')

        query = "EXEC proc24Horas ?, ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (idcli, canal))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Obtener métricas de Business Intelligence para PQR
@app.route("/api/metricaspqr", methods=["GET", "POST"])
def metricaspqr():
    try:
        data = request.get_json()
        if data is None:
            data = {}

        try:
            idusu = int(data.get('idusu', 0))
        except (ValueError, TypeError):
            idusu = 0

        fecha_inicio = data.get('fechaInicio', None)
        fecha_fin = data.get('fechaFin', None)

        # Si no se envían fechas, usar últimos 30 días
        if not fecha_inicio or not fecha_fin:
            fecha_fin = datetime.now().strftime('%Y-%m-%d')
            fecha_inicio = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        # Obtener todos los PQRs del usuario
        query = "EXEC procCargarPQR ?"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (idusu,))
        
        if cursor.description:
            columns = [column[0] for column in cursor.description]
            pqrs = [dict(zip(columns, row)) for row in cursor.fetchall()]
        else:
            pqrs = []
        
        # Filtrar por rango de fechas
        pqrs_filtrados = []
        for pqr in pqrs:
            fecha_ingreso = pqr.get('fecha_ingreso', '')
            if fecha_ingreso:
                try:
                    # Convertir fecha_ingreso a datetime para comparar
                    if isinstance(fecha_ingreso, str):
                        fecha_pqr = datetime.strptime(fecha_ingreso.split(' ')[0], '%Y-%m-%d')
                    else:
                        fecha_pqr = fecha_ingreso
                    
                    fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
                    fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')
                    
                    if fecha_inicio_dt <= fecha_pqr <= fecha_fin_dt:
                        pqrs_filtrados.append(pqr)
                except:
                    pqrs_filtrados.append(pqr)
        
        # Calcular métricas
        total = len(pqrs_filtrados)
        
        # Contar por estado
        estados = {}
        for pqr in pqrs_filtrados:
            estado = pqr.get('estado', 'Sin Estado')
            estados[estado] = estados.get(estado, 0) + 1
        
        # Contar por canal
        canales = {}
        for pqr in pqrs_filtrados:
            canal = pqr.get('canal', 'Sin Canal')
            canales[canal] = canales.get(canal, 0) + 1
        
        # Contar por prioridad
        prioridades = {}
        for pqr in pqrs_filtrados:
            prioridad = pqr.get('prioridad', 'Sin Prioridad')
            prioridades[prioridad] = prioridades.get(prioridad, 0) + 1
        
        # Contar por categoría
        categorias = {}
        for pqr in pqrs_filtrados:
            categoria = pqr.get('categoria_pqr', 'Sin Categoría')
            categorias[categoria] = categorias.get(categoria, 0) + 1
        
        # Contar por agente
        agentes = {}
        for pqr in pqrs_filtrados:
            agente = pqr.get('agente', 'Sin Asignar')
            if agente and agente != 'Sin Asignar':
                agentes[agente] = agentes.get(agente, 0) + 1
        
        # Tendencia por día
        tendencia_dias = {}
        for pqr in pqrs_filtrados:
            fecha_ingreso = pqr.get('fecha_ingreso', '')
            if fecha_ingreso:
                try:
                    if isinstance(fecha_ingreso, str):
                        fecha = fecha_ingreso.split(' ')[0]
                    else:
                        fecha = fecha_ingreso.strftime('%Y-%m-%d')
                    tendencia_dias[fecha] = tendencia_dias.get(fecha, 0) + 1
                except:
                    pass
        
        cursor.close()
        conn.close()

        resultado = {
            'total': total,
            'estados': estados,
            'canales': canales,
            'prioridades': prioridades,
            'categorias': categorias,
            'agentes': agentes,
            'tendencia_dias': tendencia_dias,
            'pqrs': pqrs_filtrados
        }

        return {'status': 'success', 'data': resultado}, 200
    except Exception as e:
        print(f"Error en metricaspqr: {e}")
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route("/api/cargarcategoriasPQR", methods=["GET", "POST"])
def cargarcategoriasPQR():
    try:
        query = "EXEC procCargarPQR_Categoria"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route("/api/cargarsubcategoriasPQR", methods=["GET", "POST"])
def cargarsubcategoriasPQR():
    try:
        query = "EXEC procCargarPQR_SubCategoria"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query)

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route("/api/cargarNotificaciones", methods=["GET", "POST"])
def cargarNotificaciones():
    try:
        data = request.get_json()
        id_usuario = data.get('idusu')
        
        query = "EXEC procObtenerNotificaciones ?"
        conn = get_db_connection()  # Obtener conexión a la base de datos
        cursor = conn.cursor()  # Crear un cursor para ejecutar el query
        cursor.execute(query, (id_usuario,))

        # Convertir los resultados en una lista de diccionarios (opcional)
        columns = [column[0] for column in cursor.description]
        resultados_dict = [dict(zip(columns, row))
                           for row in cursor.fetchall()]
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        # Cuando usas ensure_ascii=False, se respetan los caracteres especiales y se codifican tal como están
        return {'status': 'success', 'data': resultados_dict}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route("/api/crear_notificacion", methods=["GET", "POST"])
def crear_notificacion():
    try:
        data = request.get_json()
        id_usuario = data.get('id_usuario')
        titulo = data.get('titulo')
        mensaje = data.get('mensaje')
        tipo = data.get('tipo', 'info')
        link = data.get('link', None)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC procCrearNotificacion ?, ?, ?, ?, ?", 
                       (id_usuario, titulo, mensaje, tipo, link))
        conn.commit()
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión
    
        return {'status': 'success', 'message': 'Notificación creada'}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route("/api/actualizar_notificacion", methods=["GET", "POST"])
def actualizar_notificacion():
    try:
        data = request.get_json()
        id_notif = data.get('id') or data.get('id_notificacion')

        # Caso: Marcar como leída
        if data.get('leida') is True:
            query = "UPDATE Notificaciones SET leida = 1 WHERE id = ?"
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, (id_notif,))
            conn.commit()
            cursor.close()
            conn.close()
            return {'status': 'success', 'message': 'Notificación marcada como leída'}, 200

        # Caso: Marcar todas como leídas
        if data.get('marcar_todas') is True:
            id_usuario = data.get('id_usuario')
            query = "UPDATE Notificaciones SET leida = 1 WHERE id_usuario = ?"
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, (id_usuario,))
            conn.commit()
            cursor.close()
            conn.close()
            return {'status': 'success', 'message': 'Todas las notificaciones marcadas como leídas'}, 200

        # Caso: Actualización completa (usando SP)
        id_usuario = data.get('id_usuario')
        titulo = data.get('titulo')
        mensaje = data.get('mensaje')
        tipo = data.get('tipo', 'info')
        link = data.get('link', None)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC procActualizarNotificacion ?, ?, ?, ?, ?, ?", 
                       (id_notif, id_usuario, titulo, mensaje, tipo, link))
        conn.commit()
        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión
    
        return {'status': 'success', 'message': 'Notificación actualizada'}, 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# Iniciar la aplicación Flask
if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=5000)
