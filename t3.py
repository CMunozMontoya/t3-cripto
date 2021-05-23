import blowfish
import base64
from os import urandom
from yattag import Doc

doc, tag, text = Doc().tagtext()
archivo = open("codigo.html","w")

#cifrar----------------
key = b"abcd1234" #Llave
texto = "holahola"
mensaje = bytes(texto, 'utf-8') #Mensaje
#print(mensaje)

cipher = blowfish.Cipher(key)
mensaje_cifrado = cipher.encrypt_block(mensaje)
#print(mensaje_cifrado)
#m = str(mensaje_cifrado)
#m = m[2:]

#texto_plano = cipher.decrypt_block(mensaje_cifrado)
#print(texto_plano)

data = base64.b64encode(mensaje_cifrado)
#print(data)

texto_oculto = "<div class='blowfish' id=" + str(data)[1:] + "></div>"

#escribir html----------
archivo.write("<!DOCTYPE html>\n<html>\n")
archivo.write("<head> <link rel='stylesheet' type='text/css' href='estilo.css' />")
archivo.write("<script type='text/javascript' src='Blowfish.js' ></script>")
archivo.write("<script type='text/javascript' src='decode.js' ></script>")
#archivo.write("<script type='text/javascript' src='decode.js' />")
archivo.write("</head><body>\n\n")
archivo.write("<p>Este sitio contiene un mensaje secreto</p>")
archivo.write(texto_oculto)
#archivo.write("<input type='text' id = 'llave'/>")
#archivo.write("<button type='button' onclick='desencriptar();'> desencriptar </button>")
archivo.write("\n</body>\n</html>")

archivo.close()
