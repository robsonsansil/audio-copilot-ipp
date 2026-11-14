# Sprint E01 – Fluxo de Eventos

## Objetivo

Definir o modelo de comunicação baseado em eventos utilizado pelo Audio Copilot.

Toda interação entre a Soundcraft Ui24R, o operador, a Inteligência Artificial e os módulos internos ocorrerá através de eventos.

Essa arquitetura garante desacoplamento entre os componentes, sincronização em tempo real e rastreabilidade completa de todas as alterações realizadas durante um evento.

---

# Filosofia

O Audio Copilot é um sistema orientado a eventos (**Event-Driven Architecture**).

Nenhum módulo altera diretamente outro módulo.

Sempre que alguma ação ocorre, um evento é publicado.

Os módulos interessados recebem esse evento e executam suas respectivas ações.

Esse modelo reduz dependências entre componentes e facilita a evolução do sistema.

---

# Fluxo Geral

```
                Operador
                    │
                    ▼
              Interface (UI)
                    │
                    ▼
             State Manager
                    │
                    ▼
             Event Manager
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
Ui24R Client     IA Manager   History Manager
      │             │             │
      └─────────────┼─────────────┘
                    ▼
             Atualização Global
```

Todos os módulos compartilham o mesmo fluxo de comunicação.

---

# Ciclo de Vida de um Evento

Todo evento percorre as seguintes etapas.

1. Um módulo executa uma ação.
2. O evento é publicado.
3. O Event Manager recebe o evento.
4. O State Manager atualiza o estado global.
5. Os módulos interessados são notificados.
6. As interfaces são atualizadas automaticamente.

Esse fluxo ocorre em poucos milissegundos.

---

# Exemplo

O operador altera o volume do Canal 05.

```
Operador

↓

Console de Operação

↓

VolumeAlterado

↓

Event Manager

↓

State Manager

↓

Ui24R

↓

Dashboard

↓

Painel IA

↓

Mobile

↓

Histórico
```

Todos os componentes passam a visualizar imediatamente o novo valor.

---

# Origem dos Eventos

Os eventos podem ser gerados por diferentes módulos.

## Operador

Exemplos:

- alterar volume;
- aplicar mute;
- carregar snapshot;
- alterar participante;
- trocar instrumento.

---

## Soundcraft Ui24R

Exemplos:

- alteração realizada diretamente na mesa;
- mudança de ganho;
- alteração de compressor;
- mudança de cena;
- alteração de efeito.

---

## Inteligência Artificial

Exemplos:

- nova recomendação;
- sugestão aplicada;
- alerta preventivo;
- aprendizado registrado.

---

## Sistema

Exemplos:

- conexão estabelecida;
- perda de comunicação;
- sincronização concluída;
- início do evento;
- encerramento do evento.

---

# Categorias de Eventos

Os eventos serão organizados por categoria.

## Eventos do Sistema

Exemplos:

- SystemStarted
- SystemStopped
- SystemConnected
- SystemDisconnected
- ConfigurationLoaded

---

## Eventos do Evento

Exemplos:

- EventCreated
- EventStarted
- EventPaused
- EventFinished

---

## Eventos dos Canais

Exemplos:

- ChannelEnabled
- ChannelDisabled
- ChannelMuted
- ChannelUnmuted
- ChannelVolumeChanged
- ChannelGainChanged
- ChannelNameChanged

---

## Eventos de Processamento

Exemplos:

- EQChanged
- CompressorChanged
- GateChanged
- FXChanged
- HPFChanged
- LPFChanged

---

## Eventos dos Participantes

Exemplos:

- ParticipantAssigned
- ParticipantRemoved
- ParticipantUpdated

---

## Eventos dos Equipamentos

Exemplos:

- InstrumentAssigned
- InstrumentRemoved
- MicrophoneAssigned
- PresetApplied

---

## Eventos da IA

Exemplos:

- IARecommendationCreated
- IARecommendationAccepted
- IARecommendationRejected
- IALearningCompleted
- IAAlertGenerated

---

## Eventos da Preparação

Exemplos:

- PreparationStarted
- ResourceTestStarted
- ResourceTestCompleted
- PreparationCompleted

---

## Eventos da Operação

Exemplos:

- OperationStarted
- OperationFinished
- SnapshotLoaded
- SnapshotSaved

---

## Eventos do Histórico

Exemplos:

- HistoryEntryCreated
- UndoExecuted
- RedoExecuted

---

# Estrutura de um Evento

Todo evento deverá seguir uma estrutura padronizada.

Exemplo:

```json
{
  "id": "evt-000154",
  "timestamp": "2027-03-15T09:42:31",
  "category": "Channel",
  "type": "ChannelVolumeChanged",
  "source": "Operator",
  "channel": 5,
  "oldValue": -12,
  "newValue": -10,
  "user": "Robson"
}
```

Essa padronização facilita auditoria e integração entre módulos.

---

# Publicação dos Eventos

Sempre que uma alteração ocorrer, o módulo responsável publicará um evento.

Exemplo:

```
Console

↓

ChannelMuted
```

O Console não atualiza diretamente os demais módulos.

Apenas publica o evento.

---

# Assinatura de Eventos

Cada módulo informa quais eventos deseja receber.

Exemplo:

```
Dashboard

↓

Recebe

- ChannelMuted
- VolumeChanged
- IARecommendationCreated
```

```
Mobile

↓

Recebe

- IAAlertGenerated
- ChannelMuted
- ChannelVolumeChanged
```

```
Histórico

↓

Recebe TODOS
```

---

# Eventos da IA

A Inteligência Artificial também utiliza eventos.

Exemplo:

```
ClippingDetectado

↓

IARecommendationCreated

↓

Operador

↓

IARecommendationAccepted

↓

VolumeAlterado
```

Todo o processo permanece registrado.

---

# Eventos de Auditoria

Toda alteração importante gera automaticamente um registro.

Exemplo:

```
09:42

Robson

Mute Canal 05
```

```
09:44

IA

Sugestão criada

Reduzir 2 dB
```

```
09:45

Operador

Sugestão aceita
```

Esses eventos alimentam o Histórico de Alterações.

---

# Atualização das Interfaces

Quando um evento altera o estado da aplicação, todas as interfaces conectadas são atualizadas automaticamente.

Exemplo:

```
Volume Canal 05

↓

Dashboard

↓

Console

↓

Mobile

↓

Painel IA
```

Não existe sincronização manual.

---

# Benefícios

A arquitetura baseada em eventos oferece:

- comunicação desacoplada;
- atualização em tempo real;
- sincronização automática;
- facilidade para testes;
- facilidade para registrar histórico;
- suporte a auditoria;
- melhor escalabilidade;
- integração simples com novos módulos.

---

# Eventos Futuros

A arquitetura permite incorporar novos eventos sem alterar os módulos existentes.

Exemplos:

- detecção automática de microfonia;
- integração com equipamentos externos;
- controle de iluminação;
- transmissão ao vivo;
- gravação multipista;
- monitoramento remoto.

Novos módulos apenas passam a publicar ou consumir eventos.

---

# Relação com o State Manager

O Event Manager e o State Manager trabalham em conjunto.

O Event Manager é responsável por distribuir os eventos.

O State Manager é responsável por armazenar o estado atualizado da aplicação.

Essa separação evita que regras de negócio fiquem espalhadas pelo sistema.

---

# Integração com as Próximas Sprints

O fluxo de eventos será utilizado diretamente por:

- E02 – Dashboard Operacional;
- E03 – Medidores em Tempo Real;
- E04 – Painel da Liturgia;
- E05 – IA Operacional;
- E06 – Histórico de Alterações;
- E07 – Destaque Visual das Alterações da IA;
- E08 – Modo Ensaio;
- E09 – Modo Culto;
- E10 – Modo Técnico.

Todos esses módulos deverão publicar e consumir eventos seguindo o padrão definido neste documento.

---

# Objetivos da Sprint

Ao final desta sprint, o projeto deverá possuir:

- arquitetura de comunicação baseada em eventos;
- categorias padronizadas de eventos;
- fluxo de publicação e assinatura documentado;
- estrutura única para todos os eventos;
- integração entre operador, Ui24R, IA e interfaces;
- base preparada para sincronização em tempo real.

---

# Situação da Sprint

**Status:** ✅ Concluída