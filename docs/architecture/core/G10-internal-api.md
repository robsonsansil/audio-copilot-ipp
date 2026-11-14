# Sprint G10 – Internal API

## Objetivo

Definir a arquitetura da **Internal API**, componente responsável pela comunicação entre todos os módulos do Audio Copilot.

A Internal API estabelece um padrão único para troca de informações entre os componentes internos do sistema, garantindo baixo acoplamento, alta coesão e facilidade de manutenção.

Seu objetivo é permitir que cada módulo funcione de forma independente, comunicando-se apenas através de interfaces bem definidas.

---

# Visão Geral

O Audio Copilot é composto por diversos módulos independentes.

Exemplos:

- Event Manager;
- Program Manager;
- Liturgy Manager;
- Scene Manager;
- Rule Engine;
- Alert Engine;
- Operation State;
- Recording System;
- IA Operacional;
- Integração com Ui24R;
- Interface do Operador.

Nenhum módulo deve acessar diretamente os dados internos de outro componente.

Toda comunicação deverá ocorrer através da Internal API.

---

# Papel dentro do Audio Copilot

A Internal API possui as seguintes responsabilidades:

- padronizar a comunicação entre módulos;
- disponibilizar serviços internos;
- desacoplar componentes;
- controlar chamadas entre módulos;
- validar mensagens;
- registrar comunicações;
- facilitar futuras expansões do sistema.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Internal API
│
├── API Controller
├── Service Registry
├── Request Dispatcher
├── Event Bus
├── Message Validator
├── API Repository
└── API Logger
```

Cada módulo possui responsabilidades específicas.

---

# API Controller

Coordena todas as chamadas realizadas entre os módulos.

É responsável por:

- receber solicitações;
- encaminhar chamadas;
- validar respostas;
- controlar erros;
- retornar resultados.

Nenhum módulo comunica-se diretamente com outro.

---

# Service Registry

Mantém o catálogo de todos os serviços disponíveis.

Exemplo:

```text
Event Manager

↓

createEvent()

↓

openEvent()

↓

closeEvent()
```

Cada componente publica apenas os serviços que deseja disponibilizar.

---

# Request Dispatcher

Responsável pelo roteamento das chamadas internas.

Fluxo:

```text
Solicitação

↓

Dispatcher

↓

Módulo Destino

↓

Resposta

↓

Solicitante
```

---

# Event Bus

Permite comunicação baseada em eventos.

Ao invés de chamadas diretas, alguns módulos apenas publicam eventos.

Exemplo:

```text
Cena Aplicada

↓

Event Bus

↓

Console

↓

IA

↓

Logs

↓

Dashboard
```

Todos os módulos interessados recebem automaticamente a notificação.

---

# Message Validator

Valida todas as mensagens antes da entrega.

São verificados:

- estrutura;
- parâmetros obrigatórios;
- tipos de dados;
- permissões;
- versão da mensagem.

Mensagens inválidas serão rejeitadas.

---

# API Repository

Responsável pelo armazenamento da documentação dos serviços internos.

Cada serviço deverá possuir:

- nome;
- descrição;
- parâmetros;
- retorno;
- versão;
- módulo responsável.

---

# API Logger

Registra todas as comunicações realizadas.

São armazenadas informações como:

- data;
- horário;
- módulo origem;
- módulo destino;
- operação executada;
- tempo de resposta;
- resultado.

Esses registros auxiliam diagnósticos e auditorias.

---

# Comunicação entre Componentes

Exemplo de fluxo interno.

```text
Console de Operação

↓

Internal API

↓

Scene Manager

↓

Operation State

↓

Alert Engine

↓

Console atualizado
```

Nenhum componente acessa diretamente outro módulo.

---

# Serviços Internos

Cada componente poderá disponibilizar serviços.

Exemplo:

```text
Event Manager

- createEvent()
- updateEvent()
- startEvent()
- finishEvent()

Program Manager

- loadProgram()
- nextStep()
- previousStep()

Scene Manager

- applyScene()
- compareScene()
- saveScene()

Recording System

- startRecording()
- stopRecording()
- createMarker()
```

Todos seguem um padrão único de comunicação.

---

# Estrutura de uma Requisição

Cada requisição deverá conter:

```text
Requisição

ID

Origem

Destino

Serviço

Parâmetros

Data

Hora

Versão
```

---

# Estrutura da Resposta

Cada resposta deverá possuir:

```text
Resposta

Status

Código

Mensagem

Dados

Tempo de execução
```

---

# Fluxo de Funcionamento

```text
Módulo Solicitante

↓

Internal API

↓

Validação

↓

Dispatcher

↓

Serviço

↓

Resposta

↓

Retorno ao Solicitante
```

---

# Comunicação Assíncrona

Além das chamadas diretas, o sistema permitirá comunicação por eventos.

Exemplo:

```text
Gravação Iniciada

↓

Event Bus

↓

IA

↓

Logs

↓

Tela Principal

↓

Dashboard Mobile
```

Essa abordagem reduz o acoplamento entre os módulos.

---

# Integração com Outros Componentes

A Internal API é utilizada por todos os módulos do Audio Copilot.

Entre eles:

- Event Manager;
- Program Manager;
- Liturgy Manager;
- Scene Manager;
- Rule Engine;
- Alert Engine;
- Operation State;
- Recording System;
- IA Operacional;
- Ui24R Integration;
- Console de Operação;
- Dashboard Mobile;
- Sistema de Relatórios.

Ela representa o principal mecanismo de comunicação interna da aplicação.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- toda comunicação entre módulos deverá ocorrer através da Internal API;
- mensagens deverão ser validadas antes do processamento;
- chamadas deverão ser registradas para auditoria;
- componentes não poderão acessar diretamente estruturas internas de outros módulos;
- serviços deverão possuir versionamento;
- falhas de comunicação deverão ser tratadas de forma controlada.

---

# Requisitos Funcionais

A Internal API deverá permitir:

- registrar serviços;
- localizar serviços;
- executar chamadas internas;
- publicar eventos;
- receber eventos;
- validar mensagens;
- registrar comunicações;
- consultar histórico de chamadas.

---

# Requisitos Não Funcionais

O componente deverá:

- possuir baixa latência;
- suportar alto volume de chamadas simultâneas;
- garantir integridade das mensagens;
- permitir evolução dos serviços sem quebrar compatibilidade;
- facilitar testes unitários e integração entre módulos.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- descoberta automática de serviços;
- versionamento avançado da API;
- monitoramento em tempo real das chamadas;
- métricas de desempenho por serviço;
- cache interno para consultas frequentes;
- suporte a arquitetura distribuída;
- comunicação entre múltiplas instâncias do Audio Copilot;
- integração com APIs externas através do mesmo barramento de serviços;
- documentação automática dos serviços internos.

---

# Situação da Sprint

**Status:** ✅ Concluída