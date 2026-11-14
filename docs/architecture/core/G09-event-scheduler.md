# Sprint G09 – Event Scheduler

## Objetivo

Definir a arquitetura do **Event Scheduler**, componente responsável pelo agendamento e execução automática de ações dentro do Audio Copilot.

O Event Scheduler permite que determinadas tarefas sejam executadas automaticamente em momentos específicos do evento, reduzindo a necessidade de intervenção manual do operador.

Seu objetivo é garantir maior previsibilidade, sincronização e automação durante toda a operação.

---

# Visão Geral

Durante um culto ou ensaio, diversas ações ocorrem sempre na mesma sequência.

Exemplos:

- iniciar gravação alguns minutos antes do culto;
- aplicar automaticamente uma cena;
- iniciar um cronômetro;
- avançar uma etapa da programação;
- emitir um lembrete ao operador;
- iniciar monitoramento de determinado recurso;
- gerar um marcador na gravação.

O Event Scheduler é responsável por executar essas tarefas no momento correto.

---

# Papel dentro do Audio Copilot

O Event Scheduler possui as seguintes responsabilidades:

- agendar tarefas;
- executar tarefas automaticamente;
- controlar horários;
- controlar dependências;
- acompanhar tarefas pendentes;
- registrar execuções;
- sincronizar ações entre módulos.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Event Scheduler
│
├── Scheduler Controller
├── Task Registry
├── Scheduler Engine
├── Task Queue
├── Trigger Manager
├── Execution History
└── Scheduler Repository
```

Cada módulo possui responsabilidades específicas.

---

# Scheduler Controller

Coordena todo o funcionamento do agendador.

Permite:

- iniciar agendamentos;
- cancelar tarefas;
- reagendar eventos;
- pausar execuções;
- retomar processamento.

Também controla prioridades entre tarefas simultâneas.

---

# Task Registry

Responsável pelo cadastro das tarefas agendáveis.

Cada tarefa possuirá:

- identificador;
- nome;
- descrição;
- categoria;
- prioridade.

Exemplo:

```text
TASK-000148
```

---

# Scheduler Engine

É o núcleo do Event Scheduler.

Sua responsabilidade é verificar continuamente se existe alguma tarefa pronta para execução.

Sempre que uma condição for satisfeita, a tarefa correspondente será iniciada automaticamente.

---

# Task Queue

Mantém todas as tarefas pendentes.

As tarefas permanecem na fila até que:

- sejam executadas;
- sejam canceladas;
- expirem;
- sejam reagendadas.

---

# Trigger Manager

Responsável por identificar quando uma tarefa deve ser executada.

Os gatilhos podem ser baseados em:

- horário;
- duração;
- etapa da programação;
- momento da liturgia;
- alteração de estado;
- evento do sistema;
- decisão da IA.

---

# Execution History

Registra todas as execuções realizadas.

Cada registro conterá:

- data;
- horário;
- tarefa executada;
- origem;
- duração;
- resultado.

Esse histórico será utilizado em auditorias e aprendizado da IA.

---

# Scheduler Repository

Responsável pelo armazenamento permanente das tarefas cadastradas.

Também armazena:

- configurações;
- prioridades;
- dependências;
- histórico.

---

# Tipos de Agendamento

O sistema deverá suportar diferentes formas de agendamento.

## Por horário

Exemplo:

```text
08:55

↓

Iniciar gravação
```

---

## Por tempo relativo

Exemplo:

```text
5 minutos antes do início

↓

Aplicar Cena Inicial
```

---

## Por etapa

Exemplo:

```text
Programação

↓

Pregação

↓

Aplicar Cena "Pregação"
```

---

## Por liturgia

Exemplo:

```text
Momento

↓

Santa Ceia

↓

Iniciar gravação de destaque
```

---

## Por evento do sistema

Exemplo:

```text
Perda da conexão

↓

Gerar alerta
```

---

## Por decisão da IA

Exemplo:

```text
IA detectou necessidade

↓

Sugerir nova cena
```

---

# Fluxo de Funcionamento

```text
Criar Tarefa

↓

Definir Gatilho

↓

Agendar

↓

Aguardar Condição

↓

Executar

↓

Registrar Histórico
```

---

# Estrutura de uma Tarefa

Cada tarefa deverá possuir:

```text
Tarefa

ID

Nome

Descrição

Categoria

Prioridade

Gatilho

Ação

Status
```

---

# Estados da Tarefa

Cada tarefa poderá assumir um dos seguintes estados.

```text
Criada

↓

Agendada

↓

Aguardando

↓

Executando

↓

Concluída
```

Caso ocorra algum problema:

```text
Falhou
```

Ou ainda:

```text
Cancelada
```

---

# Prioridade das Tarefas

Quando houver múltiplas tarefas para execução simultânea, o Scheduler utilizará prioridades.

```text
Crítica

Alta

Normal

Baixa
```

Essa prioridade define apenas a ordem de execução.

---

# Integração com Outros Componentes

O Event Scheduler fornece informações para:

- Event Manager;
- Program Manager;
- Liturgy Manager;
- Scene Manager;
- Rule Engine;
- Alert Engine;
- Operation State;
- Recording System;
- IA Operacional;
- Console de Operação.

Também recebe informações provenientes desses componentes.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- tarefas somente poderão ser executadas quando suas condições forem satisfeitas;
- tarefas canceladas não poderão ser executadas;
- todas as execuções deverão ser registradas;
- tarefas críticas possuirão prioridade máxima;
- tarefas poderão depender da conclusão de outras tarefas;
- uma tarefa poderá ser executada apenas uma vez, salvo quando configurada como recorrente.

---

# Requisitos Funcionais

O Event Scheduler deverá permitir:

- criar tarefas;
- editar tarefas;
- excluir tarefas;
- agendar execuções;
- cancelar agendamentos;
- reagendar tarefas;
- consultar fila;
- acompanhar execuções;
- consultar histórico.

---

# Requisitos Não Funcionais

O componente deverá:

- operar em tempo real;
- possuir baixa latência;
- suportar centenas de tarefas simultâneas;
- garantir precisão na execução dos horários;
- permitir expansão para novos tipos de gatilho.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- tarefas recorrentes;
- calendário integrado;
- cronograma visual das execuções;
- dependências complexas entre tarefas;
- agendamento inteligente sugerido pela IA;
- sincronização com Google Calendar e Outlook;
- importação e exportação de cronogramas;
- notificações antecipadas ao operador;
- execução distribuída entre múltiplas estações do Audio Copilot.

---

# Situação da Sprint

**Status:** ✅ Concluída