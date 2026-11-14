/*
==========================================================
 Audio Copilot IPP
 Biblioteca Oficial de Presets

 script.js
 Inicialização da aplicação
==========================================================
*/

document.addEventListener("DOMContentLoaded", iniciarAplicacao);

function iniciarAplicacao() {

    console.log("========================================");
    console.log("Audio Copilot IPP");
    console.log("Biblioteca de Presets");
    console.log("Inicializando...");
    console.log("========================================");

    // Tema
    iniciarTema();

    // Menu lateral
    carregarMenu();

    // Busca
    iniciarBusca();

    console.log("Sistema iniciado.");

}