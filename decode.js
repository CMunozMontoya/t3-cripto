function desencriptar (){
	
	var key = document.querySelectorAll('#llave')[0].value;
	var mensaje = document.querySelectorAll('.blowfish')[0].id;

	//console.log(key);
	//console.log(mensaje);

	var mode = "ecb"

	var bf = new Blowfish(key,mode);

	var encrypted = bf.base64Decode(mensaje);
	var decrypted = bf.decrypt(encrypted);


	document.querySelectorAll('.blowfish')[0].innerHTML="mensaje: " + decrypted;

}
