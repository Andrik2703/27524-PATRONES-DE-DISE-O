import qrcode
import json

datos_api = {
    "usuario": {
        "id": "A12345",
        "nombre": "Andrik",
        "rol": "admin"
    },
    "configuracion": {
        "tema": "oscuro",
        "idioma": "es",
        "notificaciones": True
    },
    "acceso": {
        "token": "abc123xyz789",
        "expiracion": "2024-12-31",
        "permisos": ["lectura", "escritura", "admin"]
    }
}

json_str = json.dumps(datos_api, indent=2)
img = qrcode.make(json_str)
img.save("datos_api.png")