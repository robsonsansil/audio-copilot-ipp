# Sprint I03 — Reconexão da Interface

## Objetivo

Reconectar toda a interface Web da Biblioteca Oficial de Presets ao novo sistema de banco de dados gerado automaticamente (`database.js`), eliminando a dependência da leitura direta dos arquivos Markdown.

---

## Motivação

Até este momento, a interface carregava cada preset abrindo diretamente seu arquivo `.md`.

Esse modelo apresentava algumas limitações:

- dependência do caminho físico do arquivo;
- maior quantidade de requisições;
- dificuldades para futura publicação em GitHub Pages;
- necessidade de manter duas listas de presets (interface e gerador).

Com a criação do `gerar_database.py`, tornou-se possível transformar toda a biblioteca de Markdown em um único banco JavaScript.

Assim, a interface passou a consumir apenas um arquivo:

```
database.js
```

---

# Alterações realizadas

## 1. Menu lateral

O arquivo `menu.js` foi alterado para utilizar:

```javascript
Object.values(DATABASE)
```

em vez da constante:

```javascript
PRESETS
```

Cada botão agora é criado automaticamente utilizando os metadados presentes no banco gerado.

---

## 2. Abertura dos presets

O arquivo `markdown.js` foi simplificado.

Antes:

```javascript
fetch(...)
```

Agora:

```javascript
const preset = DATABASE[id];
renderizarMarkdown(preset.markdown);
```

Todo o conteúdo é carregado diretamente da memória.

---

## 3. Busca

O sistema de pesquisa passou a pesquisar em:

- título
- categoria
- conteúdo Markdown

diretamente dentro do `DATABASE`.

---

## 4. presets.js

O arquivo deixou de armazenar toda a lista de presets.

Agora possui apenas:

- informações da aplicação;
- categorias;
- ícones.

Toda a lista de presets é gerada automaticamente.

---

## 5. database.js

Passou a ser o único arquivo responsável pelos presets.

Cada entrada contém:

- id
- título
- categoria
- caminho original
- arquivo
- markdown completo

---

## 6. Gerador Python

O script

```
tools/gerar_database.py
```

passou a ser responsável por:

- localizar todos os arquivos `.md`;
- extrair os metadados;
- gerar automaticamente o `database.js`.

Sempre que um novo preset é criado basta executar:

```bash
py tools/gerar_database.py
```

Não é mais necessário editar JavaScript manualmente.

---

# Benefícios

- Biblioteca totalmente automática.
- Inclusão de novos presets sem alterar código.
- Busca mais rápida.
- Apenas um arquivo JavaScript é carregado.
- Menor quantidade de requisições.
- Compatível com GitHub Pages.
- Estrutura preparada para centenas de presets.

---

# Resultado

A Biblioteca Oficial de Presets passou a operar sobre um banco de dados JavaScript gerado automaticamente, tornando o sistema mais simples, rápido, escalável e preparado para futuras funcionalidades como favoritos, filtros, exportação, sincronização e integração com o Audio Copilot.