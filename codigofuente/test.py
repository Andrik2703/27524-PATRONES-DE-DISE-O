import qrcode
from faker import Faker

#VARIABLE
fake = Faker()

for _ in range(10):
    name = fake.name()
    img = qrcode.make()
    img.save(name+".png")
    print(f"QR code for{name} generated and saved as {name}.png")
img = qrcode.make('Andrik WAS HERE')
type(img)  # qrcode.image.pil.PilImage
img.save("Andrik.png")
