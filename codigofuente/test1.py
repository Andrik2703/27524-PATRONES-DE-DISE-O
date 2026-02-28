import qrcode

datos_complejos = {
    "nombre": "Andrik",
    "empresa": "Tech Solutions",
    "cargo": "Desarrollador Senior",
    "email": "andrik@empresa.com",
    "telefono": "+34 123 456 789",
    "web": "www.andrik.dev"
}

texto_completo = "\n".join([f"{k}: {v}" for k, v in datos_complejos.items()])
img = qrcode.make(texto_completo)
img.save("datos_complejos.png")