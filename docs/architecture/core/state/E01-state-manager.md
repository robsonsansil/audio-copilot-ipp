# Sprint E01 – State Manager

## Objetivo

Definir a arquitetura do **State Manager**, responsável por manter o estado global do Audio Copilot.

O State Manager é o núcleo central da aplicação.

Todos os módulos do sistema compartilham o mesmo estado, garantindo sincronização em tempo real, consistência das informações e atualização automática das interfaces.

Esta sprint estabelece como os dados serão organizados, atualizados e distribuídos entre os diversos componentes do sistema.

---

# Visão Geral

O State Manager é a única fonte oficial de informações do Audio Copilot.

Nenhuma tela, módulo ou serviço mantém cópias independentes dos dados.

Toda leitura e toda alteração passam obrigatoriamente pelo State Manager.

Essa abordagem elimina inconsistências entre telas e garante que todos os componentes trabalhem sempre com o mesmo conjunto de informações.

---

# Filosofia

O Audio Copilot utiliza o conceito de **Single Source of Truth (SSOT)**.

Isso significa que existe apenas um estado global compartilhado por toda a aplicação.

Qualquer alteração realizada:

- pelo operador;
- pela Ui24R;
- pela Inteligência Artificial;
- pelo sistema;

é refletida imediatamente nesse estado global.

As interfaces apenas exibem esse estado.

---

# Papel do State Manager

O State Manager é responsável por:

- armazenar todas as informações da aplicação;
- manter o estado consistente;
- atualizar automaticamente as interfaces;
- fornecer dados aos módulos internos;
- registrar alterações;
- disponibilizar informações para a IA;
- sincronizar Desktop e Mobile.

Ele não executa regras de negócio.

Seu papel é armazenar e distribuir informações.

---

# Arquitetura

```
                 Operador
                     │
                     ▼
              Interface (UI)
                     │
                     ▼
              Event Manager
                     │
                     ▼
               State Manager
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Dashboard      IA Manager      Mobile
      │              │              │
      └──────────────┼──────────────┘
                     ▼
                  Ui24R
```

Todas as interfaces observam o State Manager.

Sempre que um dado muda, apenas os componentes afetados são atualizados.

---

# Estrutura Geral do Estado

O estado global é dividido em módulos.

```
Application State

├── System
├── Event
├── Channels
├── Participants
├── Equipment
├── Presets
├── Program
├── Preparation
├── IA
├── Monitoring
├── History
├── Alerts
├── Settings
└── User
```

Cada módulo representa uma área específica do sistema.

---

# Estado do Sistema

Contém informações gerais da aplicação.

Exemplos:

- versão;
- conexão com Ui24R;
- status da gravação;
- sincronização;
- horário;
- modo de operação.

---

# Estado do Evento

Armazena todas as informações do evento atual.

Exemplos:

- nome;
- template;
- data;
- horário;
- operador;
- igreja;
- status do evento.

---

# Estado dos Canais

Cada canal da Ui24R possui um objeto próprio.

Exemplo:

```
Canal 05

- habilitado
- nome
- participante
- equipamento
- preset
- ganho
- volume
- mute
- pan
- compressor
- gate
- equalizador
- efeitos
- medidor
- status
```

Essa estrutura representa completamente o canal durante toda a operação.

---

# Estado dos Participantes

Cada participante possui informações independentes.

Exemplo:

```
Robson

- função
- instrumento
- microfone
- canal
- preset utilizado
- status do teste
```

Essas informações são compartilhadas entre Configuração, Preparação e Operação.

---

# Estado dos Equipamentos

Armazena os equipamentos utilizados no evento.

Exemplos:

- Cajón;
- Violão Martin;
- Baixo;
- Guitarra;
- Microfone Vermelho;
- Microfone Azul;
- DI Box;
- Microfone do Púlpito.

Cada equipamento possui seu histórico de utilização.

---

# Estado da Programação Técnica

Representa o cronograma do evento.

Exemplo:

```
Culto Domingo Manhã

↓

Louvor

↓

Oração

↓

Avisos

↓

Pregação

↓

Ceia

↓

Encerramento
```

A tela principal utiliza essas informações para acompanhar o andamento do culto.

---

# Estado da Preparação

Controla o checklist realizado antes do evento.

Exemplo:

```
Canal 01

Testado

✔

Canal 02

Pendente

⏳
```

A atualização ocorre automaticamente conforme os testes são concluídos.

---

# Estado da IA

Contém todas as informações relacionadas à Inteligência Artificial.

Exemplos:

- recomendações;
- sugestões pendentes;
- nível de confiança;
- histórico de aprendizado;
- justificativas;
- modo de operação.

A IA consulta continuamente o estado global para tomar decisões.

---

# Estado do Monitoramento

Representa as informações em tempo real recebidas da Ui24R.

Exemplos:

- nível de entrada;
- nível de saída;
- clipping;
- silêncio;
- ruído;
- feedback;
- pico.

Essas informações alimentam o Painel da IA e os alertas.

---

# Estado dos Alertas

Armazena todos os alertas ativos.

Exemplo:

```
Mic Vermelho

↓

Sem sinal
```

```
Canal 08

↓

Clipping
```

```
Retorno

↓

Possível feedback
```

Os alertas são compartilhados por todas as interfaces.

---

# Estado do Histórico

Cada alteração realizada gera um registro.

Exemplo:

```
10:31

Robson

Mute Canal 05
```

```
10:35

IA

Reduziu 2 dB
```

Esse histórico nunca altera os dados atuais.

Ele apenas registra acontecimentos.

---

# Atualização do Estado

Sempre que um evento é recebido:

```
Evento

↓

State Manager

↓

Atualiza Estado

↓

Notifica Interfaces
```

Essa atualização ocorre automaticamente.

---

# Atualização Parcial

O sistema evita atualizar toda a aplicação.

Exemplo:

```
Volume Canal 05

↓

Atualiza

Canal 05

↓

Dashboard

↓

Console

↓

Mobile
```

Os demais componentes permanecem inalterados.

Isso melhora significativamente o desempenho.

---

# Imutabilidade

As alterações deverão seguir o princípio da imutabilidade.

Ao invés de modificar diretamente um objeto existente, será criada uma nova versão do estado.

Benefícios:

- maior previsibilidade;
- facilidade de depuração;
- suporte a Undo e Redo;
- melhor integração com testes.

---

# Sincronização

Todas as interfaces utilizam exatamente o mesmo estado.

Desktop

↓

Console

↓

Painel IA

↓

Mobile

↓

Relatórios

Não existem estados independentes.

---

# Persistência

Parte do estado poderá ser armazenada permanentemente.

Exemplos:

- configurações;
- templates;
- presets;
- snapshots;
- participantes;
- histórico;
- preferências.

Outras informações existirão apenas durante o evento.

Exemplos:

- medidores;
- níveis de sinal;
- alertas temporários;
- testes em andamento.

---

# Benefícios

A utilização de um State Manager centralizado proporciona:

- sincronização automática;
- consistência entre telas;
- facilidade para testes;
- atualização em tempo real;
- redução de código duplicado;
- melhor desempenho;
- facilidade para integração com IA;
- suporte futuro a múltiplos operadores.

---

# Integração com os Módulos

O State Manager fornece informações para:

- Dashboard Principal;
- Configuração do Evento;
- Preparação do Evento;
- Console de Operação;
- Painel da IA;
- Aplicativo Mobile;
- Histórico;
- Relatórios;
- Sistema de Notificações.

Todos esses módulos consultam o mesmo estado global.

---

# Evolução Futura

A arquitetura do State Manager foi projetada para suportar futuras expansões do Audio Copilot, incluindo:

- múltiplas mesas de som;
- múltiplos operadores simultâneos;
- operação remota;
- sincronização em nuvem;
- colaboração em tempo real;
- integração com sistemas de iluminação;
- integração com sistemas de transmissão;
- monitoramento distribuído.

Essas funcionalidades poderão ser incorporadas sem alterações significativas na arquitetura central.

---

# Objetivos da Sprint

Ao final desta sprint, o projeto deverá possuir:

- definição completa do estado global da aplicação;
- organização modular das informações;
- estratégia de atualização em tempo real;
- sincronização entre todas as interfaces;
- suporte ao histórico e auditoria;
- base arquitetural para as próximas fases do projeto.

---

# Situação da Sprint

**Status:** ✅ Concluída