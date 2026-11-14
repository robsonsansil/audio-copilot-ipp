# Sprint G07 – Operation State

## Objetivo

Definir a arquitetura do **Operation State**, componente responsável por manter o estado global da operação do Audio Copilot.

O Operation State funciona como a "fonte única da verdade" (Single Source of Truth) do sistema.

Seu objetivo é concentrar todas as informações referentes ao estado atual da operação, permitindo que todos os módulos consultem dados consistentes e sincronizados em tempo real.

---

# Visão Geral

Durante a execução de um evento, diversos componentes alteram continuamente o estado do sistema.

Exemplos:

- evento iniciado;
- programação em andamento;
- liturgia avançada;
- cena aplicada;
- gravação iniciada;
- alerta ativo;
- modo da IA alterado;
- operador assumiu controle manual.

O Operation State centraliza todas essas informações.

---

# Papel dentro do Audio Copilot

O Operation State possui as seguintes responsabilidades:

- armazenar o estado atual da operação;
- sincronizar informações entre módulos;
- disponibilizar contexto global;
- registrar mudanças de estado;
- notificar alterações;
- evitar inconsistências entre componentes.

Todos os módulos consultam o Operation State antes de executar qualquer operação.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Operation State
│
├── State Controller
├── State Store
├── State Synchronizer
├── State Validator
├── State History
└── State Observer
```

Cada módulo possui responsabilidades específicas.

---

# State Controller

Coordena todas as alterações realizadas no estado da operação.

É responsável por:

- atualizar estados;
- validar alterações;
- iniciar sincronizações;
- controlar transições;
- notificar componentes.

Nenhum módulo altera diretamente o estado global.

Toda alteração passa pelo State Controller.

---

# State Store

Armazena o estado atual do sistema.

Exemplo:

```text
Evento

↓

Programação

↓

Liturgia

↓

Cena Atual

↓

Modo da IA

↓

Gravação

↓

Alertas

↓

Estado Geral
```

O State Store representa sempre a situação atual do Audio Copilot.

---

# State Synchronizer

Responsável por manter todos os módulos sincronizados.

Sempre que ocorrer uma alteração de estado, todos os componentes interessados serão notificados automaticamente.

Exemplo:

```text
Nova Cena Aplicada

↓

State Synchronizer

↓

Console

↓

Tela Principal

↓

Painel da IA

↓

Logs

↓

Mobile
```

---

# State Validator

Valida todas as mudanças antes de atualizar o estado.

Exemplos:

- evento ativo;
- programação válida;
- transição permitida;
- recurso disponível;
- operação autorizada.

Mudanças inválidas serão rejeitadas.

---

# State History

Registra todas as alterações ocorridas durante a operação.

Exemplos:

- início do evento;
- mudança de cena;
- início da gravação;
- alerta crítico;
- operador assumiu controle;
- encerramento do culto.

Esse histórico será utilizado em auditorias e relatórios.

---

# State Observer

Permite que outros componentes acompanhem alterações do estado.

Exemplos de observadores:

- IA Operacional;
- Console de Operação;
- Tela Principal;
- Sistema de Alertas;
- Sistema de Logs;
- Aplicativo Mobile.

Sempre que houver uma alteração, os observadores serão notificados automaticamente.

---

# Estrutura do Estado

O Operation State deverá armazenar informações como:

```text
Estado Global

Evento

Programação

Liturgia

Etapa Atual

Cena Atual

Operador

Modo da IA

Estado da Mesa

Gravação

Alertas

Status Geral
```

---

# Estados Monitorados

O componente deverá acompanhar, entre outros:

- evento ativo;
- operador atual;
- programação em execução;
- momento da liturgia;
- cena aplicada;
- modo da IA;
- estado da gravação;
- alertas ativos;
- comunicação com a Ui24R;
- estado geral do sistema.

---

# Fluxo de Funcionamento

```text
Mudança Detectada

↓

State Controller

↓

Validação

↓

Atualizar State Store

↓

Registrar Histórico

↓

Notificar Observadores
```

---

# Sincronização Global

Todos os módulos trabalham utilizando o mesmo estado global.

```text
Event Manager
        │
Program Manager
        │
Liturgy Manager
        │
Scene Manager
        │
Rule Engine
        │
Alert Engine
        │
Recording System
        │
Operation State
        │
┌───────┼────────┐
│       │        │
IA   Console   Dashboard
```

Dessa forma, todas as interfaces permanecem sincronizadas.

---

# Integração com Outros Componentes

O Operation State fornece informações para:

- Event Manager;
- Program Manager;
- Liturgy Manager;
- Scene Manager;
- Rule Engine;
- Alert Engine;
- Recording System;
- IA Operacional;
- Console de Operação;
- Tela Principal;
- Dashboard Mobile;
- Sistema de Logs.

Também recebe atualizações provenientes desses componentes.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- existir apenas um estado global ativo;
- todas as alterações deverão passar pelo State Controller;
- mudanças deverão ser validadas antes da atualização;
- todos os componentes deverão consultar o Operation State como referência oficial;
- toda alteração deverá ser registrada no histórico;
- notificações deverão ocorrer imediatamente após a atualização do estado.

---

# Requisitos Funcionais

O Operation State deverá permitir:

- armazenar o estado global;
- atualizar informações;
- consultar estados;
- validar alterações;
- sincronizar módulos;
- registrar histórico;
- notificar observadores;
- restaurar estados quando necessário.

---

# Requisitos Não Funcionais

O componente deverá:

- responder em tempo real;
- garantir consistência dos dados;
- suportar múltiplas atualizações simultâneas;
- possuir baixo consumo de memória;
- permitir expansão para futuras integrações.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- snapshots automáticos do estado;
- restauração completa da operação;
- sincronização distribuída entre múltiplas estações;
- replicação em tempo real;
- visualização gráfica do estado do sistema;
- comparação entre estados históricos;
- exportação da linha do tempo da operação;
- integração com ferramentas externas de monitoramento;
- suporte a operação colaborativa entre múltiplos operadores.

---

# Situação da Sprint

**Status:** ✅ Concluída