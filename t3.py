import blowfish
import base64
from os import urandom
from yattag import Doc

def rellenar (text):
	while len(text) < 8:
		text = text+"0"
	return text

doc, tag, text = Doc().tagtext()
archivo = open("codigo.html","w")

#datos----------------
#key = b"abcd1234" #Llave
#texto = "hola"

while True:
	texto = input("Ingrese mensaje a enviar (Maximo 8 caracteres): ")
	if len(texto) <= 8:
		break
	print("Mensaje demasiado largo.")

while True:
	llave = input("Ingrese mensaje a enviar (Maximo 8 caracteres): ")
	if len(llave) <= 8:
		break
	print("Llave demasiado larga")

texto = rellenar(texto)
print(texto)

mensaje = bytes(texto, 'utf-8') #Mensaje
key = bytes(llave, 'utf-8') #llave

cipher = blowfish.Cipher(key)
mensaje_cifrado = cipher.encrypt_block(mensaje)

#desencriptar --- DEBUG
#texto_plano = cipher.decrypt_block(mensaje_cifrado)
#print(texto_plano)

data = base64.b64encode(mensaje_cifrado) #pasar a base64 para enviado sencillo

texto_oculto = "<div class='blowfish' id=" + str(data)[1:] + "></div>"

#escribir html----------
archivo.write("<!DOCTYPE html>\n<html>\n")
archivo.write("<head> <link rel='stylesheet' type='text/css' href='estilo.css' />")
archivo.write("<script type='text/javascript' src='Blowfish.js' ></script>")
archivo.write("<script type='text/javascript' src='decode.js' ></script>")
archivo.write("</head><body>\n\n")
archivo.write("<p>Este sitio contiene un mensaje secreto</p>")
archivo.write(texto_oculto)
#archivo.write("<input type='text' id = 'llave'/>")
#archivo.write("<button type='button' onclick='desencriptar();'> desencriptar </button>")
archivo.write("\n</body>\n</html>")

archivo.close()
