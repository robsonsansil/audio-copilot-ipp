# Sprint D12 – Design System

## Objetivo

Definir o Design System oficial do Audio Copilot.

Este documento estabelece os padrões visuais, componentes de interface e regras de utilização que deverão ser utilizados em todo o sistema.

Seu objetivo é garantir consistência visual, facilidade de manutenção e escalabilidade durante toda a evolução do projeto.

---

# Filosofia

O Audio Copilot foi projetado para operar durante eventos ao vivo.

Por esse motivo, todas as decisões de design seguem cinco princípios fundamentais:

- simplicidade;
- rapidez;
- consistência;
- baixa carga cognitiva;
- foco na operação.

Cada elemento da interface deve ajudar o operador a tomar decisões rapidamente, evitando distrações desnecessárias.

---

# Identidade Visual

O sistema utiliza uma identidade visual moderna inspirada em consoles profissionais de áudio.

Características:

- interface escura;
- alto contraste;
- elementos minimalistas;
- indicadores visuais claros;
- uso moderado de animações.

---

# Paleta de Cores

## Cor Primária

Roxo Audio Copilot

Utilização:

- botões principais;
- destaques;
- seleção de menus;
- IA.

---

## Cor Secundária

Azul

Utilização:

- informações;
- links;
- elementos ativos.

---

## Verde

Utilização:

- sucesso;
- conectado;
- funcionando corretamente.

---

## Amarelo

Utilização:

- atenção;
- recomendações;
- avisos.

---

## Vermelho

Utilização:

- erro;
- clipping;
- falhas;
- alertas críticos.

---

## Tons Neutros

Cinzas escuros para:

- fundo;
- painéis;
- divisórias;
- cartões.

---

# Tipografia

Fonte principal:

Inter

Características:

- excelente legibilidade;
- moderna;
- otimizada para interfaces.

Hierarquia:

H1

Título principal

H2

Seções

H3

Subseções

Texto

14–16 px

Legendas

12 px

---

# Ícones

Biblioteca recomendada:

Lucide

Todos os ícones devem possuir:

- traço uniforme;
- mesmo tamanho;
- mesma espessura.

Jamais misturar estilos diferentes.

---

# Grid

Todas as telas seguem grid de 12 colunas.

Espaçamentos:

8 px

16 px

24 px

32 px

48 px

O sistema utiliza múltiplos de 8 px.

---

# Bordas

Raio padrão:

12 px

Botões principais:

16 px

Cards:

16 px

Campos:

12 px

---

# Sombras

Sombras discretas.

Nunca utilizar sombras pesadas.

A profundidade deve ser percebida apenas para separar cartões e painéis.

---

# Componentes

## Botões

Existem quatro categorias.

### Primário

Roxo

Ação principal.

Exemplo:

Salvar Configuração

---

### Secundário

Cinza

Ações comuns.

Exemplo:

Cancelar

---

### Perigo

Vermelho

Exemplo:

Excluir Evento

---

### IA

Gradiente Roxo

Exemplo:

Aplicar Sugestão

---

# Campos

Tipos:

- texto;
- seleção;
- pesquisa;
- data;
- hora.

Todos seguem o mesmo padrão visual.

---

# Cards

Os cards representam a principal unidade visual do sistema.

Exemplos:

- Saúde do Sistema;
- IA;
- Programação;
- Recursos;
- Console.

Todos possuem:

- cabeçalho;
- conteúdo;
- espaçamento interno;
- bordas arredondadas.

---

# Tabelas

Utilizadas em:

- Configuração do Evento;
- Console;
- Relatórios.

Regras:

- linhas bem espaçadas;
- poucas bordas;
- destaque apenas na linha selecionada.

---

# Indicadores

Sempre utilizar cores consistentes.

🟢 Funcionando

🟡 Atenção

🔴 Problema

Nunca depender apenas da cor.

Sempre incluir:

- texto;
- ícone.

---

# Navegação

Menu lateral fixo.

Cabeçalho superior.

Breadcrumb opcional.

As telas principais sempre possuem acesso rápido entre si.

Exemplo:

Dashboard

↓

Console

↓

Dashboard

---

# Responsividade

Desktop

Interface completa.

Tablet

Interface simplificada.

Mobile

Controle remoto da operação.

---

# Microinterações

Animações discretas.

Exemplos:

- fade;
- hover;
- loading;
- progresso.

Nunca utilizar animações que prejudiquem a operação.

---

# Estados dos Componentes

Cada componente possui estados padronizados.

Botões:

- normal;
- hover;
- pressionado;
- desabilitado.

Campos:

- vazio;
- preenchido;
- foco;
- erro.

Cards:

- normal;
- selecionado;
- alerta.

---

# Acessibilidade

O sistema deverá seguir boas práticas de acessibilidade.

Exemplos:

- contraste adequado;
- tamanho mínimo de fonte;
- navegação por teclado;
- ícones acompanhados de texto;
- áreas de clique amplas.

---

# Consistência

Todos os módulos devem utilizar os mesmos componentes.

Exemplos:

Dashboard

↓

Configuração

↓

Preparação

↓

Console

↓

IA

↓

Relatórios

Nenhuma tela poderá criar componentes diferentes sem atualização deste documento.

---

# Biblioteca de Componentes

Componentes oficiais:

- Botão;
- Card;
- Campo;
- Select;
- Data Picker;
- Toggle;
- Switch;
- Badge;
- Chip;
- Tooltip;
- Modal;
- Alert;
- Snackbar;
- Barra de Progresso;
- Indicador de Áudio;
- Medidor VU;
- Canal;
- Timeline da Programação;
- Cartão de Participante.

---

# Evolução

Este documento deverá acompanhar todas as futuras versões do Audio Copilot.

Sempre que um novo componente for criado, ele deverá ser documentado neste Design System antes de ser utilizado em produção.

---

# Objetivos

Este Design System garante:

- consistência visual;
- facilidade de manutenção;
- padronização;
- escalabilidade;
- experiência uniforme em todas as telas.

---

# Situação da Sprint

**Status:** ✅ Concluída