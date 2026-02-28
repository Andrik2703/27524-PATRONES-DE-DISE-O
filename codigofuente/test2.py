import qrcode

# Formato WiFi: WIFI:T:WPA;S:nombre_red;P:contraseña;;
wifi_config = "WIFI:T:WPA;S:MiRedWifi;P:MiClaveSegura123;;"
img = qrcode.make(wifi_config)
img.save("wifi_config.png")