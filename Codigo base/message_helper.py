import aiohttp
import json
import os
import httpx
from dotenv import load_dotenv
from flask import current_app, jsonify

# Carga el archivo .env una vez al inicio del archivo
load_dotenv()

async def send_notificacion_app(data):
    headers = {"Content-type": "application/json"}
    async with aiohttp.ClientSession() as session:
        url = 'https://siicsa-connect360.azurewebsites.net/api/firebase'
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    response_data = await response.json()  # Convertir la respuesta en JSON
                    return {"status": "success", "response": response_data}
                    #return "ok"
                else:
                    return {"status": "error", "code": response.status, "details": await response.text()}
                    #return "error"
        except aiohttp.ClientConnectorError as e:
            return {"status": "error", "message": "Connection Error", "details": str(e)}
            #return "error coneccion: " + str(e)
            
async def sendTexto_PG_IG(recipient_id: str, text: str):
    url = f"{os.getenv('GRAPH_VERSION')}/{os.getenv('PAGE_ID')}/messages"
    payload = {
        "recipient": {"id": recipient_id},
        "message":   {"text": text},
        "messaging_type": "RESPONSE"  # ≤ 24h
    }
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post(url, params={"access_token": os.getenv('PAGE_TOKEN')}, json=payload)
        print("SEND:", r.status_code, r.text)
        r.raise_for_status()
        return r.json()
            
            
async def send_message_pni(data, recipient):
    dat = os.getenv('ACCESS_TOKEN')
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
    }

    async with aiohttp.ClientSession() as session:
        url = 'https://graph.facebook.com' + f"/{os.getenv('VERSION')}/{recipient}/messages"
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    response_data = await response.json()  # Convertir la respuesta en JSON
                    return {"status": "success", "response": response_data}
                    #return "ok"
                else:
                    return {"status": "error", "code": response.status, "details": await response.text()}
                    #return "error"
        except aiohttp.ClientConnectorError as e:
            return {"status": "error", "message": "Connection Error", "details": str(e)}
            #return "error coneccion: " + str(e)          
            
async def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {current_app.config['ACCESS_TOKEN']}",
    }

    async with aiohttp.ClientSession() as session:
        url = 'https://graph.facebook.com' + f"/{current_app.config['VERSION']}/{current_app.config['PHONE_NUMBER_ID']}/messages"
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    response_data = await response.json()  # Convertir la respuesta en JSON
                    return {"status": "success", "response": response_data}
                    #return "ok"
                else:
                    return {"status": "error", "code": response.status, "details": await response.text()}
                    #return "error"
        except aiohttp.ClientConnectorError as e:
            return {"status": "error", "message": "Connection Error", "details": str(e)}
            #return "error coneccion: " + str(e)


def sendCustomTexto(recipient, text):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {
            "preview_url": True,
            "body": text
        }
    })

def sendCustomImage(to, url, caption):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "image",
        "image": {
            "link": url,
            "caption": caption
        }
    })

def sendCustomAudio(to, link):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "audio",
        "audio": {
            "link": link
        }
    })

# no esta enviando video
def sendCustomVideo(to, id):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "video",
        "video": {
            "id": id
        }
    })

def sendCustomDocumentos(to, mensaje, url, filename):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "document",
        "document": {
            "link": url,
            "caption": mensaje,
            "filename": filename
        }
    })

def sendCustomActionUrl(to, header, body, footer, botontexto, botonurl):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "cta_url",

            # Header optional
            "header": {
                "type": "text",
                "text": header
            },

            # Body optional
            "body": {
                "text": body
            },

            # Footer optional
            "footer": {
                "text": footer
            },

            "action": {
                "name": "cta_url",
                "parameters": {
                    "display_text": botontexto,
                    "url": botonurl
                }
            }
        }
    })

def sendCustomLista(to, header, body, footer, title, rows, button):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
            "to": to,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": header
                },
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "sections": [
                        {
                            "title": title,
                            "rows": rows
                        }
                    ],
                "button": button,
            }
        }
    })

def sendCustomListaCopia(to, header, body, footer, title, sections):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
            "to": to,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": header
                },
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "sections": [
                        {
                            "title": title,
                            "rows": [
                                {
                                    "id": "1",
                                    "title": "Amarillo",
                                    "description": "Color claro y sobrio"
                                },
                                {
                                    "id": "2",
                                    "title": "Rojo",
                                    "description": "Color pasión"
                                },
                                {
                                    "id": "3",
                                    "title": "Negro",
                                    "description": "Color oscuro"
                                },
                            ]
                        }
                    ],
                "button": "Colores",
            }
        }
    })

def sendCustomButtons(to, header, body, footer, buttons):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "header": {
                "type": "text",
                "text": header
            },
            "body": {
                "text": body
            },
            "footer": {
                "text": footer
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1",
                            "title": buttons[0]
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "2",
                            "title": buttons[1]
                        }
                    }
                ]
            }
        }
    })
    
def sendCustomButtons1(to, header, body, footer, buttons):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "header": {
                "type": "text",
                "text": header
            },
            "body": {
                "text": body
            },
            "footer": {
                "text": footer
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1",
                            "title": buttons[0]
                        }
                    }
                ]
            }
        }
    })

def sendCustomThreeButtons(to, header, body, footer, buttons):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "header": {
                "type": "text",
                "text": header
            },
            "body": {
                "text": body
            },
            "footer": {
                "text": footer
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1",
                            "title": buttons[0]
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "2",
                            "title": buttons[1]
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "3",
                            "title": buttons[2]
                        }
                    }
                ]
            }
        }
    })

def sendTemplateTexto(to, plantilla, idioma, texto):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "template",
        "template": {
            "name": plantilla,
            "language": { "code": idioma },
            "components": [{
                "type": "body",
                "parameters": [
                    { "type": "text", "text": texto },
                ]
            }]
        }
    })
    
def build_whatsapp_template_payload22(to, template_name, body_params=None, header_text=None, image_url=None, document_url=None, document_name=None):
    payload = {
        'messaging_product': 'whatsapp',
        'to': to,
        'type': 'template',
        'template': {
            'name': template_name,
            'language': {
                'code': 'es'
            },
            'components': []
        }
    }

    # Detectar si se envía imagen o documento o texto en el header
    if image_url:
        # Header de tipo imagen
        header_component = {
            'type': 'header',
            'parameters': [{
                'type': 'image',
                'image': {
                    'link': image_url
                }
            }]
        }
        print("Enviando imagen en el header.")
        payload['template']['components'].append(header_component)

    elif document_url:
        # Header de tipo documento
        header_component = {
            'type': 'header',
            'parameters': [{
                'type': 'document',
                'document': {
                    'link': document_url,
                    'filename': document_name or 'documento.pdf'
                }
            }]
        }
        print("Enviando documento en el header.")
        payload['template']['components'].append(header_component)

    elif header_text:
        # Header de tipo texto
        header_component = {
            'type': 'header',
            'parameters': [{
                'type': 'text',
                'text': header_text
            }]
        }
        print("Enviando texto en el header.")
        payload['template']['components'].append(header_component)

    else:
        print("No se envió header.")
        
    # Agregar body si se proporciona y es lista
    if body_params and isinstance(body_params, list):
        body_parameters = [{'type': 'text', 'text': str(p)} for p in body_params]
        payload['template']['components'].append({
            'type': 'body',
            'parameters': body_parameters
        })

    return json.dumps(payload)


def build_whatsapp_template_payload(to, template_name, body_params=None, header_text=None, image_url=None, document_url=None, document_name=None):
    payload = {
        'messaging_product': 'whatsapp',
        'to': to,
        'type': 'template',
        'template': {
            'name': template_name,
            'language': {
                'code': 'es'
            },
            'components': []
        }
    }

    # Header de texto (si lo hay y NO hay documento)
    if header_text and not document_url and not image_url:
        payload['template']['components'].append({
            'type': 'header',
            'parameters': [{
                'type': 'text',
                'text': header_text
            }]
        })
        
    # Header con documento (si hay URL)
    if document_url:
        document_component = {
            'type': 'header',
            'parameters': [{
                'type': 'document',
                'document': {
                    'link': document_url,
                    'filename': document_name or 'documento.pdf'
                }
            }]
        }
        payload['template']['components'].append(document_component)
        
    elif image_url:
        # Header de tipo imagen
        header_component = {
            'type': 'header',
            'parameters': [{
                'type': 'image',
                'image': {
                    'link': image_url
                }
            }]
        }
        print("Enviando imagen en el header.")
        payload['template']['components'].append(header_component)
        

    # Agregar body si se proporciona y es lista
    if body_params and isinstance(body_params, list):
        body_parameters = [{'type': 'text', 'text': str(p)} for p in body_params]
        payload['template']['components'].append({
            'type': 'body',
            'parameters': body_parameters
        })

    return json.dumps(payload)

def construir_payload_whatsapp(
    numero_destino,
    nombre_plantilla,
    parametros_body=[],
    tipo_header=None,
    parametro_header=None,
    botones=None
):
    payload = {
        "messaging_product": "whatsapp",
        "to": numero_destino,
        "type": "template",
        "template": {
            "name": nombre_plantilla,
            "language": {"code": 'es'},
            "components": []
        }
    }

    # Parámetros del body
    if parametros_body:
        payload["template"]["components"].append({
            "type": "body",
            "parameters": [{"type": "text", "text": p} for p in parametros_body]
        })

    # Header (opcional)
    if tipo_header and parametro_header:
        if tipo_header == "image":
            header_param = {"type": "image", "image": {"link": parametro_header}}
        elif tipo_header == "video":
            header_param = {"type": "video", "video": {"link": parametro_header}}
        elif tipo_header == "document":
            header_param = {"type": "document", "document": {"link": parametro_header}}
        elif tipo_header == "text":
            header_param = {"type": "text", "text": parametro_header}
        else:
            raise ValueError("Tipo de header no soportado")

        payload["template"]["components"].append({
            "type": "header",
            "parameters": [header_param]
        })

    # Botones (opcional)
    if botones:
        payload["template"]["components"].append({
            "type": "button",
            "sub_type": "url",
            "index": 0,
            "parameters": [{"type": "text", "text": botones[0]}]
        })

    return json.dumps(payload)

