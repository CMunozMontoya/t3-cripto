// ==UserScript==
// @name         Desencriptador
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Camilo Muñoz
// @match        *://*/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @require      https://raw.githubusercontent.com/CMunozMontoya/t3-cripto/8c8a8c8d05f8864bd5166005c7a8414e45cbeebe/decode.js
// @require      https://raw.githubusercontent.com/CMunozMontoya/t3-cripto/main/Blowfish.js
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    document.querySelectorAll('.blowfish')[0].innerHTML= "<input type='text' id = 'llave'/> <button type='button' onclick='desencriptar();'> desencriptar </button>";

    var key = document.querySelectorAll('#llave')[0].value;
    var mensaje = document.querySelectorAll('.blowfish')[0].id;

    //desencriptar(key,mensaje,"ecb");
})();
