import qrcode

menu_digital = """
=== MENÚ INTERACTIVO ===
🌐 Web: https://miweb.com
📱 App: https://app.miweb.com/download
📧 Contacto: mailto:info@miweb.com
📞 Teléfono: tel:+34123456789
📍 Ubicación: https://maps.google.com/?q=Madrid
🎁 Promo: https://miweb.com/descuento
"""

img = qrcode.make(menu_digital)
img.save("menu_interactivo.png")