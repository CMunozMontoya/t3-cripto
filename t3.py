import blowfish
from os import urandom
from yattag import Doc

doc, tag, text = Doc().tagtext()
archivo = open("codigo.html","w")


#cifrar----------------
cipher = blowfish.Cipher(b"abcd1234")
block = bytes(8)
print(block)
mensaje_cifrado = cipher.encrypt_block(block)
#texto_plano = cipher.decrypt_block(ciphertext)


texto_oculto = "<div class='blowfish' id='mensaje_cifrado'>" + str(mensaje_cifrado) + "</div>"

#escribir html----------
#TEST
archivo.write("<!DOCTYPE html>\n<html>\n<body>\n\n")
archivo.write("<p>Este sitio contiene un mensaje secreto</p>")
archivo.write(texto_oculto)
archivo.write("\n</body>\n</html>")

archivo.close()
