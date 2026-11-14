# Sprint G02 – Program Manager

## Objetivo

Definir a arquitetura do **Program Manager**, componente responsável pelo gerenciamento da **Programação Técnica** dos eventos do Audio Copilot.

A Programação Técnica representa a sequência operacional planejada para um evento, descrevendo cada etapa que será executada durante sua realização.

O Program Manager é responsável por organizar, controlar e disponibilizar essa programação para todos os demais módulos do sistema.

---

# Visão Geral

Todo evento possui uma programação.

Essa programação descreve, em ordem cronológica, tudo o que deverá acontecer durante a operação.

Exemplos:

- Abertura;
- Louvor Congregacional;
- Oração Inicial;
- Avisos;
- Pregação;
- Santa Ceia;
- Encerramento.

Cada etapa poderá possuir regras próprias, recursos específicos, cenas associadas e ações automáticas.

---

# Papel dentro do Audio Copilot

O Program Manager possui as seguintes responsabilidades:

- criar programações;
- editar programações;
- organizar a sequência das etapas;
- controlar o andamento da programação;
- informar a etapa atual;
- disponibilizar a programação para todo o sistema;
- registrar alterações realizadas durante o evento.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Program Manager
│
├── Program Registry
├── Program Controller
├── Program Timeline
├── Program Validator
├── Program Repository
└── Program History
```

Cada módulo possui responsabilidades específicas.

---

# Program Registry

Responsável pelo cadastro das Programações Técnicas.

Cada programação poderá ser utilizada em diferentes eventos.

Exemplos:

- Culto Domingo Manhã
- Culto Domingo Noite
- Ensaio da Banda
- Escola Dominical
- Conferência

---

# Program Controller

Controla toda a execução da programação.

Suas responsabilidades incluem:

- iniciar programação;
- avançar etapa;
- retornar etapa;
- alterar ordem;
- pausar;
- finalizar.

Também mantém sincronização com os demais componentes.

---

# Program Timeline

Mantém a sequência cronológica das etapas.

Exemplo:

```text
01 - Abertura

↓

02 - Louvor Congregacional

↓

03 - Oração Inicial

↓

04 - Avisos

↓

05 - Pregação

↓

06 - Santa Ceia

↓

07 - Encerramento
```

A Timeline representa a ordem lógica da programação.

---

# Program Validator

Valida a consistência da programação.

São verificadas informações como:

- existência de etapas;
- ordem das etapas;
- recursos associados;
- cenas vinculadas;
- liturgia correspondente.

Caso haja inconsistências, a programação não poderá ser utilizada.

---

# Program Repository

Responsável pelo armazenamento permanente das programações.

São persistidos:

- estrutura;
- etapas;
- recursos;
- cenas;
- configurações.

---

# Program History

Registra todas as alterações realizadas na programação.

Exemplos:

- inclusão de etapa;
- exclusão;
- alteração de ordem;
- mudança de horário;
- alteração de cena.

Esse histórico poderá ser utilizado em auditorias.

---

# Estrutura da Programação

Cada programação deverá possuir:

```text
Programação

ID

Nome

Descrição

Categoria

Tempo previsto

Quantidade de etapas

Versão
```

---

# Estrutura das Etapas

Cada etapa deverá conter:

```text
Etapa

ID

Nome

Descrição

Ordem

Duração prevista

Cena associada

Liturgia relacionada

Recursos utilizados

Observações
```

---

# Fluxo de Funcionamento

```text
Criar Programação

↓

Cadastrar Etapas

↓

Definir Ordem

↓

Associar Recursos

↓

Associar Cenas

↓

Validar

↓

Salvar

↓

Utilizar no Evento
```

---

# Execução da Programação

Durante o evento o Program Manager controla automaticamente o avanço da programação.

Fluxo:

```text
Etapa Atual

↓

Concluída

↓

Próxima Etapa

↓

Atualização da Tela Principal

↓

Atualização do Console

↓

Atualização da IA
```

Todos os módulos permanecem sincronizados.

---

# Integração com Outros Componentes

O Program Manager fornece informações para:

- Event Manager;
- Liturgy Manager;
- Scene Manager;
- Rule Engine;
- Alert Engine;
- Operation State;
- Recording System;
- IA Operacional;
- Tela Principal;
- Console de Operação.

Também recebe informações do Event Manager.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- toda programação deverá possuir pelo menos uma etapa;
- a ordem das etapas deverá ser única;
- cada etapa poderá possuir uma cena associada;
- alterações durante a execução deverão ser registradas;
- somente uma etapa poderá estar ativa por vez;
- toda programação pertence a uma categoria de evento.

---

# Requisitos Funcionais

O Program Manager deverá permitir:

- criar programações;
- editar programações;
- excluir programações;
- duplicar programações;
- cadastrar etapas;
- alterar ordem das etapas;
- iniciar execução;
- avançar etapa;
- retornar etapa;
- finalizar programação.

---

# Requisitos Não Funcionais

O componente deverá:

- responder imediatamente às alterações;
- manter sincronização com todos os módulos;
- permitir reutilização de programações;
- suportar eventos longos;
- preservar o histórico de alterações.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- programação baseada em horário;
- atualização automática da etapa por tempo;
- programação condicional;
- múltiplas trilhas de execução;
- dependência entre etapas;
- importação e exportação de programações;
- biblioteca de modelos de programação;
- sugestões automáticas geradas pela IA;
- sincronização com ProPresenter e softwares de apresentação.

---

# Situação da Sprint

**Status:** ✅ Concluída