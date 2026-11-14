/*
==========================================================
 Audio Copilot IPP
 Biblioteca Oficial de Presets

 markdown.js
==========================================================
*/

function abrirPreset(id) {

    const preset = DATABASE[id];

    if (!preset) {

        mostrarErro("Preset não encontrado.");

        return;

    }

    renderizarMarkdown(preset.markdown);

}



/*
==========================================================
 Renderização
==========================================================
*/

function renderizarMarkdown(markdown) {

    const viewer = document.getElementById("viewer");

    if (typeof marked !== "undefined") {

        viewer.innerHTML = marked.parse(markdown);

        return;

    }

    viewer.innerHTML = `<pre>${escapeHtml(markdown)}</pre>`;

}



/*
==========================================================
 Tela de erro
==========================================================
*/

function mostrarErro(mensagem) {

    document.getElementById("viewer").innerHTML = `

        <h2>Erro</h2>

        <p>${mensagem}</p>

    `;

}



/*
==========================================================
 Escape HTML
==========================================================
*/

function escapeHtml(texto) {

    return texto

        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");

}