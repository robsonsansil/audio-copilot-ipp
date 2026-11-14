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

    const resultado = Object.values(DATABASE).filter(preset => {

        return (

            (preset.titulo || "").toLowerCase().includes(texto)

            ||

            (preset.categoria || "").toLowerCase().includes(texto)

            ||

            (preset.markdown || "").toLowerCase().includes(texto)

        );

    });

    carregarMenu(resultado);

}