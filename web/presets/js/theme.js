/*
==========================================================
 Audio Copilot IPP
 Biblioteca Oficial de Presets

 theme.js
==========================================================
*/

const TEMA_CLARO = "light";
const TEMA_ESCURO = "dark";

/* ====================================================== */

function iniciarTema() {

    const botao = document.getElementById("theme-toggle");

    if (!botao) return;

    const temaSalvo = localStorage.getItem("tema");

    if (temaSalvo === TEMA_ESCURO) {

        document.body.classList.add("dark");

    }

    atualizarBotaoTema();

    botao.addEventListener("click", alternarTema);

}

/* ====================================================== */

function alternarTema() {

    document.body.classList.toggle("dark");

    const temaAtual = document.body.classList.contains("dark")
        ? TEMA_ESCURO
        : TEMA_CLARO;

    localStorage.setItem("tema", temaAtual);

    atualizarBotaoTema();

}

/* ====================================================== */

function atualizarBotaoTema() {

    const botao = document.getElementById("theme-toggle");

    if (!botao) return;

    if (document.body.classList.contains("dark")) {

        botao.textContent = "☀️";
        botao.title = "Tema claro";

    } else {

        botao.textContent = "🌙";
        botao.title = "Tema escuro";

    }

}