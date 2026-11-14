# Sprint G03 – Liturgy Manager

## Objetivo

Definir a arquitetura do **Liturgy Manager**, componente responsável pelo gerenciamento da **Liturgia** dos eventos do Audio Copilot.

A Liturgia representa a estrutura espiritual e ministerial do evento, descrevendo a sequência de momentos que compõem o culto ou reunião.

Enquanto a **Programação Técnica** organiza a operação da equipe de áudio, a **Liturgia** organiza aquilo que acontece no templo.

O Liturgy Manager permite que a equipe técnica acompanhe o andamento do culto sem precisar conhecer previamente toda a programação.

---

# Visão Geral

Toda programação poderá possuir uma liturgia associada.

Ela descreve os momentos do evento sob a perspectiva da condução do culto.

Exemplos:

- Abertura;
- Leitura Bíblica;
- Oração;
- Louvor Congregacional;
- Oferta;
- Avisos;
- Pregação;
- Santa Ceia;
- Batismo;
- Encerramento.

Cada momento poderá possuir:

- duração prevista;
- dirigente responsável;
- observações;
- recursos utilizados;
- cenas associadas.

---

# Papel dentro do Audio Copilot

O Liturgy Manager possui as seguintes responsabilidades:

- cadastrar liturgias;
- organizar os momentos da liturgia;
- controlar a execução da liturgia;
- sincronizar a liturgia com a Programação Técnica;
- disponibilizar informações para a IA;
- fornecer contexto para o operador.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Liturgy Manager
│
├── Liturgy Registry
├── Liturgy Controller
├── Liturgy Timeline
├── Liturgy Validator
├── Liturgy Repository
└── Liturgy History
```

Cada módulo possui responsabilidades específicas.

---

# Liturgy Registry

Responsável pelo cadastro das liturgias.

Uma liturgia poderá ser reutilizada em diversos eventos.

Exemplos:

- Culto Dominical Manhã;
- Culto Dominical Noite;
- Santa Ceia;
- Escola Dominical;
- Conferência Missionária.

---

# Liturgy Controller

Responsável pelo controle da execução da liturgia.

Permite:

- iniciar;
- avançar;
- retornar;
- pausar;
- finalizar;
- alterar a ordem dos momentos.

Todas as alterações são refletidas em tempo real para os demais módulos.

---

# Liturgy Timeline

Representa a sequência cronológica dos momentos da liturgia.

Exemplo:

```text
Abertura

↓

Leitura Bíblica

↓

Louvor Congregacional

↓

Oração

↓

Oferta

↓

Avisos

↓

Pregação

↓

Santa Ceia

↓

Encerramento
```

A Timeline serve como referência para o operador e para a IA.

---

# Liturgy Validator

Valida toda a estrutura da liturgia antes de sua utilização.

São verificadas:

- existência de momentos;
- ordem cronológica;
- consistência das informações;
- associação com a programação;
- duração prevista.

Caso sejam encontradas inconsistências, a liturgia não poderá ser utilizada.

---

# Liturgy Repository

Responsável pelo armazenamento permanente das liturgias.

São armazenados:

- estrutura;
- momentos;
- observações;
- recursos;
- relacionamentos.

---

# Liturgy History

Registra todas as alterações realizadas na liturgia.

Exemplos:

- inclusão de momento;
- exclusão;
- alteração da ordem;
- mudança de responsável;
- alteração de observações.

---

# Estrutura da Liturgia

Cada liturgia deverá possuir:

```text
Liturgia

ID

Nome

Descrição

Categoria

Quantidade de momentos

Versão
```

---

# Estrutura dos Momentos

Cada momento deverá conter:

```text
Momento

ID

Nome

Descrição

Ordem

Duração prevista

Dirigente

Recursos utilizados

Cena sugerida

Observações
```

---

# Sincronização com a Programação Técnica

Embora sejam componentes distintos, Programação Técnica e Liturgia trabalham em conjunto.

```text
Programação Técnica

↓

Etapa Atual

↓

Liturgia

↓

Momento Atual

↓

Tela Principal

↓

Console de Operação

↓

IA
```

Dessa forma, o operador acompanha simultaneamente a evolução técnica e litúrgica do evento.

---

# Fluxo de Funcionamento

```text
Criar Liturgia

↓

Cadastrar Momentos

↓

Definir Ordem

↓

Associar Recursos

↓

Validar

↓

Salvar

↓

Associar ao Evento

↓

Executar
```

---

# Integração com Outros Componentes

O Liturgy Manager fornece informações para:

- Event Manager;
- Program Manager;
- Scene Manager;
- Rule Engine;
- Alert Engine;
- Operation State;
- Recording System;
- IA Operacional;
- Tela Principal;
- Console de Operação.

Também recebe informações do Program Manager durante a execução do evento.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- toda liturgia deverá possuir pelo menos um momento;
- somente um momento poderá estar ativo por vez;
- a ordem deverá ser única;
- alterações realizadas durante o evento deverão ser registradas;
- uma liturgia poderá ser reutilizada em diversos eventos;
- a liturgia deverá permanecer sincronizada com a programação técnica.

---

# Requisitos Funcionais

O Liturgy Manager deverá permitir:

- criar liturgias;
- editar liturgias;
- excluir liturgias;
- duplicar liturgias;
- cadastrar momentos;
- alterar ordem dos momentos;
- iniciar execução;
- avançar momento;
- retornar momento;
- finalizar liturgia.

---

# Requisitos Não Funcionais

O componente deverá:

- manter sincronização em tempo real;
- responder rapidamente às alterações;
- suportar liturgias extensas;
- preservar o histórico de modificações;
- permitir reutilização em múltiplos eventos.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- modelos de liturgia;
- liturgias recorrentes;
- sincronização automática com a programação por horário;
- atualização automática do momento atual;
- integração com softwares de projeção;
- sugestões automáticas da IA;
- importação e exportação de liturgias;
- acompanhamento colaborativo por múltiplos operadores;
- integração com aplicativos utilizados pelo dirigente do culto.

---

# Situação da Sprint

**Status:** ✅ Concluída