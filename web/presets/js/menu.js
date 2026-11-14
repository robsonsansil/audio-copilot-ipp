/*
==========================================================
 Audio Copilot IPP
 Biblioteca Oficial de Presets

 menu.js
==========================================================
*/

function carregarMenu(lista = PRESETS) {

    const menu = document.getElementById("sidebar");

    if (!menu) return;

    menu.innerHTML = "";

    const titulo = document.createElement("h2");
    titulo.textContent = "📁 Biblioteca";
    menu.appendChild(titulo);

    const categorias = {};

    lista.forEach(preset => {

        if (!categorias[preset.categoria]) {
            categorias[preset.categoria] = [];
        }

        categorias[preset.categoria].push(preset);

    });

    Object.keys(categorias).forEach(categoria => {

        const grupo = document.createElement("div");
        grupo.className = "menu-group";

        const tituloCategoria = document.createElement("h3");
        tituloCategoria.className = "menu-category";
        tituloCategoria.textContent = obterIconeCategoria(categoria) + " " + categoria;

        grupo.appendChild(tituloCategoria);

        categorias[categoria].forEach(preset => {

            const botao = document.createElement("button");

            botao.className = "menu-item";
            botao.textContent = preset.nome;

            botao.onclick = () => {

                selecionarItem(botao);

                abrirPreset(preset.id);

            };

            grupo.appendChild(botao);

        });

        menu.appendChild(grupo);

    });

}

/* ====================================================== */

function selecionarItem(itemSelecionado) {

    document
        .querySelectorAll(".menu-item")
        .forEach(item => item.classList.remove("active"));

    itemSelecionado.classList.add("active");

}

/* ====================================================== */

function obterIconeCategoria(categoria) {

    return CATEGORIAS[categoria] || "📁";

}