# Sprint G01 – Event Manager

## Objetivo

Definir a arquitetura do **Event Manager**, componente responsável pelo gerenciamento completo dos eventos do Audio Copilot.

O Event Manager é um dos principais componentes do Core do sistema. Todo o funcionamento do Audio Copilot é baseado em um evento ativo, que representa o contexto operacional atual.

Um evento pode representar:

- culto;
- ensaio;
- reunião de oração;
- escola dominical;
- conferência;
- casamento;
- congresso;
- manutenção;
- teste técnico;
- qualquer outra programação cadastrada.

É a partir do evento que todos os demais componentes obtêm suas informações.

---

# Visão Geral

Nenhum módulo do Audio Copilot funciona de forma isolada.

Antes do início de qualquer operação, deverá existir um evento ativo.

O Event Manager será responsável por:

- criar eventos;
- editar eventos;
- ativar eventos;
- finalizar eventos;
- armazenar histórico;
- disponibilizar o contexto operacional para todo o sistema.

Ele funciona como a porta de entrada de todas as operações.

---

# Papel dentro do Audio Copilot

O Event Manager possui as seguintes responsabilidades:

- gerenciamento do ciclo de vida dos eventos;
- controle do evento ativo;
- armazenamento do histórico;
- associação entre evento e seus componentes;
- disponibilização do contexto para os demais módulos.

Todo módulo do Audio Copilot depende direta ou indiretamente do Event Manager.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Event Manager
│
├── Event Registry
├── Event Controller
├── Event Context
├── Event Lifecycle
├── Event Validator
├── Event Repository
└── Event History
```

Cada módulo possui responsabilidades específicas.

---

# Event Registry

Responsável pelo cadastro dos eventos.

Cada evento possuirá um identificador único.

Exemplo:

```text
EVT-2028-000154
```

Também serão registrados:

- nome;
- categoria;
- descrição;
- local;
- data;
- horário;
- operador responsável.

---

# Event Controller

Coordena todas as operações relacionadas aos eventos.

Suas responsabilidades incluem:

- criar;
- editar;
- abrir;
- iniciar;
- pausar;
- finalizar;
- arquivar.

É o ponto central de controle do Event Manager.

---

# Event Context

Mantém o contexto operacional atualmente carregado.

Todos os módulos consultam esse contexto para saber:

- qual evento está ativo;
- qual programação está em execução;
- qual liturgia está carregada;
- quais recursos pertencem ao evento.

Sempre existirá apenas um Event Context ativo.

---

# Event Lifecycle

Controla o ciclo de vida completo do evento.

Estados previstos:

```text
Criado

↓

Configurado

↓

Preparado

↓

Em Execução

↓

Finalizado

↓

Arquivado
```

Cada alteração de estado será registrada automaticamente.

---

# Event Validator

Valida todas as informações necessárias antes do início do evento.

São verificadas, por exemplo:

- programação definida;
- liturgia carregada;
- operador informado;
- recursos configurados;
- cenas disponíveis;
- presets vinculados.

Caso alguma validação falhe, o evento não poderá ser iniciado.

---

# Event Repository

Responsável pela persistência dos eventos.

Armazena:

- informações gerais;
- configurações;
- relacionamentos;
- histórico;
- identificadores.

Nenhum dado será descartado automaticamente.

---

# Event History

Registra todas as alterações realizadas durante o ciclo de vida do evento.

Exemplos:

- criação;
- alteração de nome;
- alteração de horário;
- mudança de operador;
- início;
- pausa;
- retomada;
- encerramento.

Esse histórico será utilizado para auditorias e relatórios.

---

# Estrutura do Evento

Cada evento deverá conter, no mínimo, as seguintes informações.

```text
Evento

ID

Nome

Categoria

Descrição

Local

Data

Hora de início

Hora prevista de término

Operador responsável

Equipe

Status
```

---

# Categorias

Inicialmente o sistema deverá permitir:

- Culto
- Ensaio
- Escola Dominical
- Reunião de Oração
- Conferência
- Congresso
- Casamento
- Batismo
- Santa Ceia
- Evento Especial
- Teste Técnico
- Manutenção

Novas categorias poderão ser adicionadas futuramente.

---

# Estados

Cada evento poderá assumir apenas um estado.

```text
Criado

↓

Configurado

↓

Preparado

↓

Em Execução

↓

Finalizado

↓

Arquivado
```

Após finalizado, o evento passa para modo somente leitura.

---

# Informações Associadas

Cada evento poderá possuir diversos componentes relacionados.

```text
Evento
│
├── Programação Técnica
├── Liturgia
├── Recursos
├── Participantes
├── Operadores
├── Cenas
├── Presets
├── Gravações
├── Marcadores
├── Logs
├── Alertas
├── Relatórios
└── Histórico
```

O Event Manager centraliza todas essas associações.

---

# Fluxo de Funcionamento

```text
Criar Evento

↓

Configurar Evento

↓

Preparar Evento

↓

Validar Evento

↓

Iniciar Evento

↓

Executar

↓

Finalizar Evento

↓

Gerar Relatórios

↓

Arquivar
```

---

# Integração com Outros Componentes

O Event Manager fornece informações para:

- Program Manager;
- Liturgy Manager;
- Scene Manager;
- Rule Engine;
- Alert Engine;
- Operation State;
- Recording System;
- Replay Engine;
- IA Operacional;
- Relatórios.

Também recebe informações produzidas por esses componentes durante a execução do evento.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- existir apenas um evento ativo por estação de trabalho;
- impedir o início de um evento sem validação;
- preservar todo o histórico;
- impedir exclusão de eventos que possuam gravações ou relatórios, salvo autorização administrativa;
- registrar automaticamente todas as mudanças de estado;
- manter integridade entre o evento e seus componentes relacionados.

---

# Requisitos Funcionais

O Event Manager deverá permitir:

- criar eventos;
- editar eventos;
- excluir eventos;
- pesquisar eventos;
- listar eventos;
- ativar evento;
- finalizar evento;
- arquivar evento;
- consultar histórico;
- disponibilizar o evento ativo para todo o sistema.

---

# Requisitos Não Funcionais

O componente deverá:

- suportar milhares de eventos históricos;
- responder rapidamente às consultas;
- manter consistência entre todos os módulos;
- permitir expansão para múltiplas igrejas;
- garantir rastreabilidade completa das operações.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- eventos recorrentes;
- modelos de eventos (templates);
- calendário integrado;
- integração com Google Calendar e Outlook;
- sincronização automática com agenda da igreja;
- múltiplos operadores por função;
- aprovação eletrônica do evento;
- dashboard estatístico de eventos;
- integração com sistema de reservas de templos.

---

# Situação da Sprint

**Status:** ✅ Concluída