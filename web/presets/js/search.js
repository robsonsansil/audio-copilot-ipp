/*
==========================================================
 Audio Copilot IPP
 Biblioteca Oficial de Presets

 search.js
==========================================================
*/

function iniciarBusca() {

    const campo = document.getElementById("search");

    if (!campo) return;

    campo.addEventListener("input", pesquisarPresets);

}

/* ====================================================== */

function pesquisarPresets() {

    const texto = document
        .getElementById("search")
        .value
        .trim()
        .toLowerCase();

    if (texto === "") {

        carregarMenu();

        return;

    }

    const resultado = PRESETS.filter(preset => {

        return (

            preset.nome.toLowerCase().includes(texto)

            ||

            preset.categoria.toLowerCase().includes(texto)

            ||

            preset.descricao.toLowerCase().includes(texto)

        );

    });

    carregarMenu(resultado);

}