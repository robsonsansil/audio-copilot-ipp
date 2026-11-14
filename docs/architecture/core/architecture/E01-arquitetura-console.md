# Sprint E01 – Arquitetura do Console Inteligente

## Objetivo

Definir a arquitetura técnica do Console Inteligente do Audio Copilot, estabelecendo como os módulos internos se comunicam, como ocorre a integração com a Soundcraft Ui24R e como as informações são compartilhadas entre a interface, a Inteligência Artificial e os demais componentes do sistema.

Esta sprint não implementa funcionalidades visíveis ao usuário.

Seu propósito é criar a fundação técnica que sustentará toda a operação do Audio Copilot.

---

# Visão Geral

O Console Inteligente é o núcleo operacional do sistema.

Embora o operador interaja com telas como Dashboard, Console de Operação, Painel da IA e Aplicativo Mobile, nenhuma dessas interfaces se comunica diretamente com a Ui24R.

Toda comunicação passa por um núcleo central responsável por manter o estado da aplicação e coordenar os módulos internos.

Essa arquitetura reduz o acoplamento entre componentes, facilita a manutenção e permite a evolução do sistema de forma organizada.

---

# Arquitetura Geral

A arquitetura é organizada em camadas.

```
                  Soundcraft Ui24R
                         │
                         │
              Comunicação em Tempo Real
                         │
                         ▼
                Ui24R Communication Layer
                         │
                         ▼
                Event Manager (Eventos)
                         │
                         ▼
                State Manager (Estado)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Dashboard        Console Operação      IA
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                   Aplicativo Mobile
```

Cada camada possui uma responsabilidade específica.

Nenhuma interface acessa diretamente a mesa de som.

---

# Filosofia da Arquitetura

Todo o sistema é orientado por eventos.

Isso significa que nenhuma alteração ocorre diretamente.

Toda ação realizada pelo operador, pela IA ou pela Ui24R gera um evento que será processado pelo sistema.

Exemplos:

- alteração de volume;
- aplicação de mute;
- carregamento de snapshot;
- associação de participante;
- aplicação de preset;
- recomendação da IA.

Essa abordagem garante rastreabilidade completa das operações.

---

# Camadas do Sistema

## Interface (UI)

Responsável apenas pela interação com o usuário.

Inclui:

- Dashboard Principal;
- Configuração do Evento;
- Preparação do Evento;
- Console de Operação;
- Painel da IA;
- Aplicativo Mobile.

As interfaces nunca implementam regras de negócio.

Sua função é apenas apresentar informações e solicitar ações ao sistema.

---

## State Manager

O State Manager representa o estado global da aplicação.

Todas as informações operacionais ficam centralizadas neste módulo.

Exemplos de informações armazenadas:

- canais;
- participantes;
- equipamentos;
- presets;
- snapshots;
- programação técnica;
- estado da IA;
- alertas;
- histórico.

Sempre que uma informação for alterada, o State Manager notificará automaticamente todas as interfaces conectadas.

---

## Event Manager

Responsável por controlar todos os eventos do sistema.

Cada ação gera um evento.

Exemplos:

- ChannelMuted;
- ChannelUnmuted;
- GainChanged;
- EQChanged;
- SnapshotLoaded;
- ParticipantAssigned;
- InstrumentAssigned;
- IARecommendationCreated;
- IARecommendationAccepted;
- IARecommendationIgnored.

O Event Manager distribui esses eventos aos módulos interessados.

---

## Serviços

Os serviços implementam as regras de negócio do sistema.

Exemplos:

- gerenciamento de presets;
- gerenciamento de snapshots;
- monitoramento;
- histórico;
- notificações;
- permissões;
- integração com IA.

Os serviços nunca dependem da interface gráfica.

---

## Comunicação com a Ui24R

Toda comunicação com a mesa será realizada através de um módulo dedicado.

Este módulo será responsável por:

- estabelecer conexão;
- enviar comandos;
- receber alterações;
- monitorar o estado da mesa;
- tratar falhas de comunicação.

A comunicação será totalmente isolada do restante da aplicação.

---

# Estrutura Modular

O Console Inteligente será dividido em módulos independentes.

```
core/

├── state/
├── events/
├── ui24r/
├── ai/
├── presets/
├── snapshots/
├── monitoring/
├── history/
├── notifications/
├── permissions/
└── services/
```

Cada módulo possui uma única responsabilidade.

Essa organização facilita manutenção, testes e evolução do sistema.

---

# Fluxo de Dados

## Alterações provenientes da Ui24R

```
Ui24R

↓

Ui24R Client

↓

Event Manager

↓

State Manager

↓

Interfaces
```

Sempre que a mesa sofrer alguma alteração, todas as telas serão atualizadas automaticamente.

---

## Alterações realizadas pelo Operador

```
Operador

↓

Interface

↓

State Manager

↓

Event Manager

↓

Ui24R Client

↓

Ui24R
```

O operador nunca envia comandos diretamente para a mesa.

Toda ação passa pelo núcleo do sistema.

---

## Recomendações da IA

```
IA

↓

Recomendação

↓

State Manager

↓

Operador

↓

Aceitar ou Ignorar

↓

Ui24R
```

Na primeira versão do Audio Copilot, toda recomendação dependerá da aprovação do operador.

---

# Estado Global

O Console Inteligente trabalha com um único estado compartilhado.

Esse estado contém todas as informações do evento.

Exemplos:

Evento

- nome;
- data;
- operador;
- template.

Canais

- ganho;
- volume;
- mute;
- EQ;
- compressor;
- gate;
- efeitos.

Participantes

- nome;
- função;
- equipamento.

Equipamentos

- instrumento;
- microfone;
- DI;
- retorno.

IA

- recomendações;
- histórico;
- nível de confiança.

Sistema

- conexão;
- gravação;
- snapshots;
- sincronização.

---

# Histórico de Alterações

Toda alteração realizada durante o evento será registrada automaticamente.

Exemplo:

```
10:32

Robson

Mute Canal 05
```

```
10:35

IA

Sugestão:
Reduzir 2 dB
Canal 04
```

```
10:36

Snapshot

Culto Domingo Manhã
Carregado
```

Esse histórico servirá para auditoria, aprendizado da IA e geração de relatórios.

---

# Atualização em Tempo Real

Todas as interfaces compartilham o mesmo estado.

Quando uma alteração ocorre:

- Dashboard é atualizado;
- Console de Operação é atualizado;
- Painel da IA é atualizado;
- Mobile é atualizado;
- Relatórios recebem a alteração.

O operador visualiza sempre as mesmas informações, independentemente da tela utilizada.

---

# Permissões

O Console Inteligente deverá suportar diferentes níveis de acesso.

Perfis previstos:

- Administrador;
- Operador;
- Operador Auxiliar;
- Somente Leitura;
- Inteligência Artificial.

Cada perfil possui permissões específicas.

---

# Princípios Arquiteturais

A arquitetura do Console segue os seguintes princípios:

- modularidade;
- baixo acoplamento;
- alta coesão;
- orientação a eventos;
- estado único da aplicação;
- atualização em tempo real;
- escalabilidade;
- facilidade de manutenção;
- facilidade de testes;
- independência entre interface e regras de negócio.

---

# Benefícios

Essa arquitetura proporciona:

- comunicação centralizada;
- sincronização automática entre telas;
- maior confiabilidade;
- facilidade para futuras integrações;
- rastreabilidade completa das operações;
- melhor organização do código;
- evolução contínua do sistema sem impacto nas interfaces.

---

# Estrutura Inicial do Projeto

```
src/

core/
├── state/
├── events/
├── ui24r/
├── ai/
├── history/
├── monitoring/
├── notifications/
├── permissions/
├── presets/
├── snapshots/
└── services/

ui/
├── dashboard/
├── configuration/
├── preparation/
├── console/
├── ai/
├── mobile/
└── shared/

models/

config/

database/
```

Essa estrutura poderá evoluir conforme novas funcionalidades forem incorporadas ao projeto.

---

# Integração com as Próximas Sprints

A arquitetura definida nesta sprint servirá de base para:

- E02 – Dashboard Operacional;
- E03 – Medidores em Tempo Real;
- E04 – Painel da Liturgia;
- E05 – IA Operacional;
- E06 – Histórico de Alterações;
- E07 – Destaque Visual das Alterações da IA;
- E08 – Modo Ensaio;
- E09 – Modo Culto;
- E10 – Modo Técnico.

Todas essas funcionalidades deverão respeitar os princípios estabelecidos neste documento.

---

# Objetivos da Sprint

Ao final desta sprint, o projeto deverá possuir:

- arquitetura modular definida;
- separação clara entre interface e lógica de negócio;
- fluxo de comunicação documentado;
- organização inicial dos módulos internos;
- modelo de comunicação entre Ui24R, operador e IA;
- base técnica preparada para a implementação do Console Inteligente.

---

# Situação da Sprint

**Status:** ✅ Concluída