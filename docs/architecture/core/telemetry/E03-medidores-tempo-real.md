# Sprint E03 – Medidores em Tempo Real

## Objetivo

Definir a arquitetura responsável pela aquisição, processamento e distribuição das informações de áudio em tempo real provenientes da Soundcraft Ui24R.

Esta camada será a principal fonte de dados do Audio Copilot durante toda a operação do evento.

Todos os módulos do sistema dependerão da Telemetria para visualizar níveis de áudio, detectar eventos, alimentar a Inteligência Artificial e manter o estado atualizado da mesa de som.

---

# Visão Geral

A Telemetria representa os "olhos e ouvidos" do Audio Copilot.

Seu papel é transformar os dados brutos recebidos da Ui24R em informações estruturadas, confiáveis e prontas para serem utilizadas pelos demais componentes do sistema.

Esta camada não possui interface gráfica.

Sua responsabilidade é exclusivamente processar e disponibilizar dados em tempo real.

---

# Arquitetura Geral

O fluxo básico da Telemetria será:

```text
Soundcraft Ui24R
        │
        ▼
 Ui24R Client
        │
        ▼
Telemetry Manager
        │
        ├────────► State Manager
        │
        ├────────► Dashboard
        │
        ├────────► Console de Operação
        │
        ├────────► Painel da IA
        │
        ├────────► Mobile
        │
        └────────► Histórico
```

Todo o sistema passa a consumir informações desta camada.

Nenhum módulo deverá acessar diretamente a Ui24R.

---

# Responsabilidades

A Telemetria será responsável por:

- receber dados da Ui24R;
- monitorar continuamente todos os canais;
- acompanhar níveis de entrada e saída;
- calcular indicadores de áudio;
- detectar eventos relevantes;
- publicar alterações para o restante do sistema;
- manter o estado sincronizado.

---

# O que é monitorado

A camada de Telemetria deverá acompanhar continuamente informações como:

## Entradas

- nível instantâneo;
- pico (Peak);
- sinal presente;
- clipping;
- mute;
- phantom power;
- gate;
- compressor;
- equalização;
- ganho;
- panorama;
- fader.

---

## Saídas

- PA Esquerdo;
- PA Direito;
- Monitores;
- Stream;
- Gravação;
- Auxiliares.

---

## Sistema

Também serão monitorados diversos componentes da mesa.

Exemplos:

- conexão com a Ui24R;
- latência;
- sincronização;
- snapshots;
- cenas ativas;
- processamento interno.

---

# Separação de Responsabilidades

Esta camada apenas processa informações.

Ela não toma decisões.

Ela não altera configurações da mesa.

Ela não executa comandos.

Sua única responsabilidade é fornecer dados confiáveis para os demais módulos.

---

# Consumidores da Telemetria

Diversos componentes utilizarão as informações produzidas pela Telemetria.

## Dashboard Operacional

Utiliza os níveis de áudio para apresentar uma visão geral do evento.

---

## Console de Operação

Utiliza a Telemetria para exibir:

- medidores;
- estados dos canais;
- níveis;
- indicadores de sinal.

---

## Painel da IA

Recebe continuamente os eventos produzidos pela Telemetria.

Com essas informações a IA poderá:

- identificar riscos;
- detectar problemas;
- sugerir ajustes;
- aprender padrões de operação.

---

## Histórico

Todas as alterações detectadas poderão ser registradas para auditoria e análise posterior.

---

## Aplicativo Mobile

Recebe uma versão resumida dos dados da Telemetria.

O objetivo é fornecer apenas as informações relevantes para acompanhamento remoto.

---

# Eventos Produzidos

A Telemetria será responsável por publicar eventos para o Event Bus.

Exemplos:

- ChannelLevelChanged
- ChannelPeakDetected
- ChannelClipDetected
- ChannelSilenceDetected
- OutputLevelChanged
- MeterUpdated
- StatisticsUpdated
- Ui24rConnectionLost
- Ui24rConnectionRestored

Esses eventos serão consumidos pelos demais módulos do sistema.

---

# Frequência de Atualização

Os medidores deverão ser atualizados continuamente, respeitando um intervalo suficientemente curto para transmitir sensação de tempo real, sem comprometer o desempenho da aplicação.

A frequência efetiva de atualização será definida durante a implementação do Telemetry Manager.

---

# Integração com o State Manager

Após processar os dados recebidos da Ui24R, a Telemetria atualizará o State Manager.

As interfaces da aplicação nunca consultarão diretamente a mesa de som.

Todo acesso ocorrerá através do estado compartilhado do sistema.

Fluxo:

Ui24R → Telemetry Manager → State Manager → Interface

---

# Benefícios da Arquitetura

Esta separação oferece diversas vantagens:

- desacoplamento entre hardware e interface;
- reutilização dos dados por vários módulos;
- maior facilidade para testes;
- melhor desempenho;
- arquitetura orientada a eventos;
- escalabilidade para futuras integrações.

---

# Componentes da Sprint

Esta Sprint será dividida em módulos especializados.

Cada documento detalhará um componente específico da Telemetria.

Documentos previstos:

- E03-medidores-tempo-real.md
- E03-telemetry-manager.md
- E03-audio-levels.md
- E03-peak-detector.md
- E03-clip-detector.md
- E03-silence-detector.md
- E03-meter-cache.md
- E03-statistics.md

---

# Objetivos da Sprint

Ao final desta Sprint, o Audio Copilot deverá possuir uma arquitetura de Telemetria capaz de:

- receber informações da Ui24R em tempo real;
- processar continuamente todos os canais;
- disponibilizar dados para todas as interfaces;
- publicar eventos para o sistema;
- manter o estado sincronizado;
- servir como base para o funcionamento da Inteligência Artificial.

---

# Situação da Sprint

**Status:** ✅ Concluída