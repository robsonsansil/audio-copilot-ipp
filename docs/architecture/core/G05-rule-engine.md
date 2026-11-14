# Sprint G05 – Rule Engine

## Objetivo

Definir a arquitetura do **Rule Engine**, componente responsável pelo gerenciamento e execução de todas as regras de negócio do Audio Copilot.

O Rule Engine é o cérebro lógico do sistema.

Seu objetivo é avaliar continuamente o estado da operação, interpretar eventos ocorridos durante a execução e decidir quais ações devem ser tomadas automaticamente ou sugeridas ao operador.

Todas as decisões automatizadas do Audio Copilot passam obrigatoriamente por este componente.

---

# Visão Geral

Durante um evento, diversas situações podem exigir uma resposta automática do sistema.

Exemplos:

- mudança de etapa da programação;
- avanço da liturgia;
- início de gravação;
- aplicação de uma cena;
- geração de alertas;
- recomendações da IA;
- alteração do estado da operação.

O Rule Engine recebe essas informações, avalia as regras configuradas e determina as ações apropriadas.

---

# Papel dentro do Audio Copilot

O Rule Engine possui as seguintes responsabilidades:

- gerenciar regras de negócio;
- avaliar condições em tempo real;
- executar ações automáticas;
- validar pré-condições;
- controlar dependências entre módulos;
- fornecer decisões para a IA;
- registrar todas as execuções das regras.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Rule Engine
│
├── Rule Registry
├── Rule Controller
├── Rule Evaluator
├── Rule Executor
├── Rule Repository
├── Rule History
└── Rule Validator
```

Cada módulo possui responsabilidades específicas.

---

# Rule Registry

Responsável pelo cadastro das regras.

Cada regra possuirá:

- identificador único;
- nome;
- descrição;
- categoria;
- prioridade;
- estado.

Exemplo:

```text
RL-000154
```

---

# Rule Controller

Coordena o ciclo de vida das regras.

Permite:

- criar;
- editar;
- habilitar;
- desabilitar;
- executar;
- testar;
- remover.

Também controla a ordem de execução quando várias regras forem acionadas simultaneamente.

---

# Rule Evaluator

Responsável por avaliar continuamente todas as condições do sistema.

Sempre que ocorrer um evento relevante, o avaliador verifica quais regras deverão ser executadas.

Exemplos de gatilhos:

- mudança da etapa da programação;
- alteração da liturgia;
- troca de cena;
- mudança do estado da mesa;
- alerta detectado;
- início ou término da gravação.

---

# Rule Executor

Executa as ações definidas pelas regras aprovadas pelo avaliador.

Uma ação poderá:

- atualizar o estado do sistema;
- aplicar uma cena;
- iniciar uma gravação;
- emitir um alerta;
- enviar uma recomendação para a IA;
- registrar um log;
- solicitar confirmação do operador.

---

# Rule Repository

Responsável pelo armazenamento permanente das regras.

São armazenados:

- condições;
- ações;
- prioridades;
- histórico de alterações;
- versões.

---

# Rule History

Registra todas as execuções realizadas.

Cada execução armazenará informações como:

- data;
- horário;
- regra executada;
- motivo da execução;
- resultado;
- duração.

Esse histórico será utilizado para auditorias e aprendizado da IA.

---

# Rule Validator

Valida cada regra antes de sua ativação.

São verificadas:

- consistência lógica;
- conflitos com outras regras;
- dependências;
- ações permitidas;
- integridade da configuração.

Regras inválidas não poderão ser ativadas.

---

# Estrutura de uma Regra

Cada regra deverá possuir:

```text
Regra

ID

Nome

Descrição

Categoria

Prioridade

Status

Versão
```

---

# Estrutura Lógica

Uma regra segue a estrutura:

```text
SE

↓

Condição

↓

ENTÃO

↓

Executar ação
```

Exemplo:

```text
SE

Momento Atual = Pregação

ENTÃO

Aplicar Cena "Pregação"
```

Outro exemplo:

```text
SE

Microfonia Detectada

ENTÃO

Gerar Alerta
```

---

# Prioridade das Regras

Cada regra possuirá uma prioridade.

```text
Crítica

Alta

Normal

Baixa
```

Quando várias regras forem acionadas simultaneamente, a prioridade definirá a ordem de execução.

---

# Fluxo de Funcionamento

```text
Evento

↓

Rule Evaluator

↓

Condição Atendida?

↓

Sim

↓

Rule Executor

↓

Executar Ação

↓

Registrar Histórico
```

---

# Categorias de Regras

Inicialmente o sistema suportará:

- Programação;
- Liturgia;
- Cenas;
- Operação;
- Alertas;
- IA;
- Gravação;
- Relatórios;
- Segurança;
- Manutenção.

Novas categorias poderão ser adicionadas futuramente.

---

# Integração com Outros Componentes

O Rule Engine fornece informações para:

- Event Manager;
- Program Manager;
- Liturgy Manager;
- Scene Manager;
- Alert Engine;
- Operation State;
- Recording System;
- IA Operacional;
- Ui24R Integration;
- Console de Operação.

Também recebe eventos provenientes desses componentes.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- todas as decisões automáticas deverão passar pelo Rule Engine;
- regras desabilitadas nunca serão executadas;
- regras deverão ser executadas respeitando a prioridade;
- conflitos deverão ser identificados automaticamente;
- todas as execuções deverão ser registradas;
- nenhuma regra poderá executar ações fora das permissões definidas.

---

# Requisitos Funcionais

O Rule Engine deverá permitir:

- criar regras;
- editar regras;
- excluir regras;
- habilitar e desabilitar regras;
- testar regras;
- executar regras;
- registrar histórico;
- consultar execuções;
- definir prioridades.

---

# Requisitos Não Funcionais

O componente deverá:

- responder em tempo real;
- suportar centenas de regras simultâneas;
- possuir baixo consumo de recursos;
- garantir consistência lógica;
- permitir expansão para novos tipos de regras.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- editor visual de regras;
- regras criadas sem programação (Low-Code);
- regras condicionais complexas;
- agrupamento de regras;
- herança de regras entre eventos;
- recomendações automáticas da IA para criação de regras;
- otimização automática baseada no histórico;
- simulação de regras antes da ativação;
- integração com motores de automação externos.

---

# Situação da Sprint

**Status:** ✅ Concluída