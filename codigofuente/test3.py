import qrcode

vcard = """BEGIN:VCARD
VERSION:3.0
N:Andrik;Apellido
FN:Andrik Nombre Completo
ORG:Empresa Tecnológica
TITLE:Ingeniero de Software
TEL;TYPE=work,voice:+34 123 456 789
TEL;TYPE=cell:+34 987 654 321
EMAIL:andrik@empresa.com
URL:www.andrik.dev
NOTE:Desarrollador Python experto
END:VCARD"""

img = qrcode.make(vcard)
img.save("contacto_vcard.png")