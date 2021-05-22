var key = document.querySelectorAll('#llave');
var bf = new Blowfish(key);

// Encrypt and encode to base64
var encrypted = bf.base64Encode(bf.encrypt("secret message"));
console.log(encrypted);

// Decrypt
var encrypted = bf.base64Decode(encrypted);
var decrypted = bf.decrypt(encrypted);