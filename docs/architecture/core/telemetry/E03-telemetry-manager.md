# Sprint E03 – Telemetry Manager

## Objetivo

Definir o componente responsável por centralizar toda a telemetria do Audio Copilot.

O Telemetry Manager será o núcleo da coleta e processamento das informações provenientes da Soundcraft Ui24R, transformando dados brutos em informações estruturadas que poderão ser consumidas por toda a aplicação.

Ele será o único componente autorizado a receber dados diretamente da mesa de som.

---

# Visão Geral

O Telemetry Manager é responsável por manter o Audio Copilot sincronizado com o estado atual da Ui24R.

Sua função é receber continuamente os dados enviados pela mesa, processá-los, detectar alterações e publicar eventos para o restante do sistema.

Ele atua como uma camada intermediária entre o hardware e a aplicação.

Fluxo simplificado:

```text
Soundcraft Ui24R
        │
        ▼
   Ui24R Client
        │
        ▼
Telemetry Manager
        │
        ▼
   State Manager
        │
        ▼
Dashboard
Console
IA
Mobile
Histórico
```

---

# Responsabilidades

O Telemetry Manager será responsável por:

- receber informações da Ui24R;
- validar os dados recebidos;
- manter o estado interno sincronizado;
- identificar alterações;
- calcular indicadores necessários;
- publicar eventos para o Event Bus;
- atualizar o State Manager.

---

# O que o Telemetry Manager NÃO faz

Para manter a arquitetura desacoplada, o Telemetry Manager não deverá:

- alterar configurações da mesa;
- enviar comandos para a Ui24R;
- executar decisões da IA;
- renderizar interfaces;
- armazenar histórico permanente.

Essas responsabilidades pertencem a outros módulos.

---

# Dados Monitorados

O Telemetry Manager deverá acompanhar continuamente informações como:

## Entradas

Para cada canal:

- nível de áudio;
- pico (Peak);
- mute;
- solo;
- ganho;
- phantom power;
- gate;
- compressor;
- equalizador;
- panorama;
- fader;
- nome do canal;
- cor do canal.

---

## Saídas

Monitorar continuamente:

- PA Esquerdo;
- PA Direito;
- Monitores;
- Stream;
- Gravação;
- Auxiliares.

---

## Sistema

Também serão monitorados:

- conexão com a Ui24R;
- snapshots;
- cenas;
- taxa de atualização;
- sincronização;
- latência.

---

# Ciclo de Funcionamento

O Telemetry Manager executará continuamente o seguinte ciclo:

```text
Receber dados

↓

Validar

↓

Comparar com estado anterior

↓

Detectar alterações

↓

Atualizar estado

↓

Publicar eventos

↓

Aguardar próximo ciclo
```

Esse processo ocorre durante toda a operação do evento.

---

# Detecção de Alterações

Nem todo dado recebido deverá gerar um evento.

Antes de publicar qualquer informação, o Telemetry Manager compara o estado atual com o estado anterior.

Somente alterações relevantes serão propagadas.

Exemplos:

- mudança de nível;
- alteração de mute;
- mudança de ganho;
- ativação do compressor;
- clipping detectado;
- perda de sinal.

Essa estratégia reduz processamento desnecessário.

---

# Integração com o State Manager

Após processar uma alteração, o Telemetry Manager atualiza o State Manager.

Fluxo:

```text
Ui24R

↓

Telemetry Manager

↓

State Manager

↓

Interfaces
```

Dessa forma, todas as telas permanecem sincronizadas.

---

# Integração com o Event Bus

Sempre que uma alteração relevante for detectada, o Telemetry Manager publicará um evento.

Exemplos:

- ChannelLevelChanged
- ChannelMuteChanged
- ChannelGainChanged
- ChannelPeakDetected
- ChannelClipDetected
- ChannelSignalLost
- OutputLevelChanged
- SnapshotChanged
- SceneChanged
- ConnectionLost
- ConnectionRestored

Outros módulos poderão consumir esses eventos sem depender diretamente da Ui24R.

---

# Atualização em Tempo Real

O Telemetry Manager deverá operar continuamente durante todo o evento.

O intervalo de atualização será suficientemente curto para proporcionar uma experiência de tempo real ao operador, mantendo o desempenho da aplicação.

A frequência exata será definida durante a implementação.

---

# Cache de Estado

O Telemetry Manager manterá uma cópia do último estado conhecido da mesa.

Esse cache permitirá:

- detectar alterações;
- reduzir processamento;
- evitar eventos duplicados;
- acelerar consultas internas.

O cache não substitui o State Manager.

Ele existe apenas para otimizar o processamento interno da Telemetria.

---

# Tratamento de Falhas

Caso a conexão com a Ui24R seja interrompida, o Telemetry Manager deverá:

- interromper a atualização dos medidores;
- publicar evento de perda de conexão;
- informar o State Manager;
- aguardar tentativa de reconexão.

Quando a comunicação for restabelecida:

- sincronizar novamente todos os estados;
- atualizar o cache interno;
- publicar evento de reconexão.

---

# Integração com a Inteligência Artificial

A IA não consulta diretamente a Ui24R.

Ela recebe apenas os eventos produzidos pelo Telemetry Manager.

Exemplo:

```text
Canal 04

↓

Clipping Detectado

↓

Evento publicado

↓

Painel da IA

↓

Sugestão ao operador
```

Isso mantém a IA desacoplada do hardware.

---

# Benefícios da Arquitetura

Centralizar toda a telemetria oferece diversas vantagens:

- única fonte de dados do sistema;
- desacoplamento entre hardware e software;
- facilidade para testes automatizados;
- redução de processamento duplicado;
- sincronização consistente;
- arquitetura orientada a eventos;
- escalabilidade para futuras mesas de som.

---

# Próximos Componentes

O Telemetry Manager servirá de base para os módulos especializados desta Sprint:

- Audio Levels
- Peak Detector
- Clip Detector
- Silence Detector
- Meter Cache
- Statistics

Cada um desses componentes será responsável por um aspecto específico da Telemetria, mantendo o código modular e de fácil manutenção.

---

# Situação da Sprint

**Status:** ✅ Concluída