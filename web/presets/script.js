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
/* ==========================================================
   MENU RESPONSIVO
========================================================== */

const menuToggle = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

function abrirMenu() {

    sidebar.classList.add("open");
    overlay.classList.add("show");

}

function fecharMenu() {

    sidebar.classList.remove("open");
    overlay.classList.remove("show");

}

if (menuToggle) {

    menuToggle.addEventListener("click", () => {

        if (sidebar.classList.contains("open")) {

            fecharMenu();

        } else {

            abrirMenu();

        }

    });

}

if (overlay) {

    overlay.addEventListener("click", fecharMenu);

}

/* Fecha ao pressionar ESC */

document.addEventListener("keydown", (e) => {

    if (e.key === "Escape") {

        fecharMenu();

    }

});

/* Fecha automaticamente ao clicar em um item do menu */

document.addEventListener("click", (e) => {

    if (
        e.target.closest(".sidebar button") &&
        window.innerWidth <= 900
    ) {

        fecharMenu();

    }

});