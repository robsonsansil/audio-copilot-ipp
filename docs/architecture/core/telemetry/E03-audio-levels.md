# Sprint E03 – Audio Levels

## Objetivo

Definir o componente responsável pelo monitoramento e processamento dos níveis de áudio de todos os canais e saídas da Soundcraft Ui24R.

O Audio Levels será um dos principais módulos da camada de Telemetria, fornecendo informações em tempo real para a interface, para a Inteligência Artificial e para os demais componentes do sistema.

Seu objetivo é representar fielmente o comportamento do áudio, permitindo ao operador visualizar instantaneamente o nível de cada sinal.

---

# Visão Geral

O Audio Levels é responsável por acompanhar continuamente a intensidade do sinal de áudio presente em cada canal.

Ele transforma os valores recebidos da Ui24R em informações padronizadas que poderão ser utilizadas em toda a aplicação.

Esse componente não realiza qualquer alteração na mesa de som.

Sua função é exclusivamente observar, processar e disponibilizar os níveis de áudio.

---

# Arquitetura

Fluxo simplificado:

```text
Soundcraft Ui24R
        │
        ▼
Telemetry Manager
        │
        ▼
Audio Levels
        │
        ├────────► State Manager
        ├────────► Dashboard
        ├────────► Console de Operação
        ├────────► Painel da IA
        ├────────► Mobile
        └────────► Histórico
```

O Audio Levels recebe informações do Telemetry Manager e disponibiliza dados normalizados para toda a aplicação.

---

# Responsabilidades

O Audio Levels será responsável por:

- acompanhar continuamente os níveis de todos os canais;
- monitorar entradas e saídas;
- converter os valores recebidos da Ui24R;
- manter os níveis atualizados;
- identificar presença ou ausência de sinal;
- disponibilizar informações para os medidores da interface.

---

# Canais Monitorados

O componente deverá monitorar todos os canais disponíveis na mesa.

Exemplos:

- Voz Pastor
- Vocal 1
- Vocal 2
- Violão
- Baixo
- Cajón
- Playback
- Teclado
- Microfone Ambiente

Além das entradas, também serão monitoradas todas as saídas configuradas.

---

# Saídas Monitoradas

Exemplos:

- PA Esquerdo
- PA Direito
- Monitores
- Stream
- Gravação
- Auxiliares

Todos os medidores deverão permanecer sincronizados.

---

# Informações Disponibilizadas

Para cada canal deverão estar disponíveis informações como:

- nível instantâneo;
- nível apresentado ao operador;
- último valor recebido;
- presença de sinal;
- horário da última atualização.

Esses dados servirão de base para os demais componentes da Telemetria.

---

# Atualização Contínua

Durante todo o evento o Audio Levels executará continuamente o seguinte ciclo:

```text
Receber novo valor

↓

Atualizar nível interno

↓

Atualizar State Manager

↓

Atualizar Interface

↓

Publicar evento (quando necessário)

↓

Aguardar próximo ciclo
```

Esse processamento ocorre continuamente enquanto a Ui24R estiver conectada.

---

# Conversão dos Valores

A Ui24R poderá fornecer os níveis em um formato interno próprio.

O Audio Levels será responsável por converter esses valores para uma representação padronizada utilizada pelo Audio Copilot.

A forma exata dessa conversão será definida durante a implementação.

Essa separação permite que futuras integrações com outras mesas de som utilizem o mesmo modelo interno.

---

# Exibição dos Medidores

Os níveis processados serão utilizados por diferentes telas.

## Dashboard

Apresenta uma visão resumida dos níveis principais do sistema.

---

## Console de Operação

Apresenta medidores completos para todos os canais ativos.

---

## Painel da IA

Utiliza os níveis para analisar o comportamento do áudio e identificar possíveis anomalias.

---

## Mobile

Recebe apenas informações resumidas dos canais mais relevantes.

---

# Integração com Outros Componentes

O Audio Levels trabalha em conjunto com outros módulos da Telemetria.

Exemplos:

- Peak Detector
- Clip Detector
- Silence Detector
- Statistics

Cada componente possui uma responsabilidade específica.

O Audio Levels não executa essas análises.

---

# Eventos Produzidos

Sempre que ocorrer uma alteração significativa, o componente poderá publicar eventos como:

- ChannelLevelChanged
- OutputLevelChanged
- SignalDetected
- SignalLost
- MeterUpdated

Esses eventos serão distribuídos através do Event Bus.

---

# Desempenho

O processamento dos níveis deverá ser leve e contínuo.

O componente deverá:

- evitar processamento redundante;
- minimizar consumo de CPU;
- reduzir atualizações desnecessárias da interface;
- manter resposta em tempo real.

---

# Escalabilidade

O Audio Levels deverá ser independente da quantidade de canais existentes.

A mesma arquitetura deverá funcionar para:

- mesas menores;
- Soundcraft Ui24R;
- futuras integrações com outras mesas digitais.

Nenhuma regra deverá depender de uma quantidade fixa de canais.

---

# Benefícios

A separação deste componente oferece diversas vantagens:

- código mais organizado;
- responsabilidade única;
- reutilização em toda a aplicação;
- facilidade para testes;
- melhor desempenho;
- maior facilidade para futuras integrações.

---

# Relação com os Próximos Componentes

Os dados produzidos pelo Audio Levels servirão de base para:

- Peak Detector;
- Clip Detector;
- Silence Detector;
- Statistics.

Esses módulos utilizarão os níveis processados para realizar análises mais avançadas.

---

# Situação da Sprint

**Status:** ✅ Concluída