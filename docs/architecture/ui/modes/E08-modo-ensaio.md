# Sprint E08 – Modo Ensaio

## Objetivo

Definir o modo operacional utilizado durante os ensaios da igreja, permitindo que o Audio Copilot acompanhe toda a preparação do evento, registre ajustes realizados, observe o comportamento da equipe e aprenda continuamente para oferecer recomendações cada vez mais precisas nos cultos futuros.

O **Modo Ensaio** transforma o Audio Copilot em um assistente ativo durante a preparação da equipe de louvor, funcionando como uma plataforma de observação, aprendizado e documentação operacional.

Enquanto o **Modo Culto** prioriza estabilidade e mínima interferência, o Modo Ensaio incentiva experimentações, coleta de dados e refinamento das configurações.

---

# Visão Geral

O ensaio é o momento em que praticamente todas as decisões técnicas são tomadas.

Durante esse período são definidos:

- volumes;
- equalizações;
- compressões;
- retornos;
- panoramas;
- snapshots;
- ordem das músicas;
- participantes;
- transições da liturgia.

O Audio Copilot utilizará essas informações para construir uma base de conhecimento específica da igreja.

---

# Filosofia

O Modo Ensaio foi desenvolvido seguindo cinco princípios.

## Aprendizado Contínuo

Cada ensaio contribui para melhorar o conhecimento da IA.

---

## Liberdade de Experimentação

O operador pode testar configurações sem comprometer a estabilidade do sistema.

---

## Observação Inteligente

A IA acompanha todas as alterações realizadas.

---

## Registro Completo

Todas as mudanças ficam documentadas para futuras consultas.

---

## Evolução Gradual

O sistema aprende padrões ao longo do tempo, evitando conclusões precipitadas.

---

# Objetivos do Modo Ensaio

Durante o ensaio, o Audio Copilot deverá:

- registrar todos os ajustes realizados;
- aprender preferências da equipe;
- analisar padrões recorrentes;
- comparar configurações anteriores;
- gerar recomendações;
- produzir relatórios ao final da sessão.

---

# Arquitetura

```text
Operador

↓

Modo Ensaio

↓

Rehearsal Manager

↓

Observation Engine

↓

Learning Capture

↓

History Manager

↓

Recommendation Engine
```

---

# Fluxo Geral

```text
Iniciar Ensaio

↓

Registrar Sessão

↓

Monitorar Ajustes

↓

Observar Comportamentos

↓

Aprender Padrões

↓

Gerar Relatório

↓

Encerrar Sessão
```

---

# O que será observado

Durante o ensaio, praticamente toda alteração poderá ser registrada.

Exemplos:

- ganho;
- equalização;
- compressor;
- gate;
- panorama;
- envios auxiliares;
- mute;
- solo;
- DCA;
- snapshots.

---

# Aprendizado

O objetivo do modo ensaio não é apenas registrar informações.

Ele também permitirá que a IA aprenda.

Exemplo:

```text
Toda semana

↓

Vocal Azul

↓

+2 dB

↓

Registrar preferência
```

Outro exemplo:

```text
Sempre antes da pregação

↓

Reduzir Playback

↓

Registrar padrão
```

---

# Observação dos Operadores

O sistema poderá identificar diferenças entre operadores.

Exemplo:

```text
Robson

↓

Sempre reduz

150 Hz

↓

Registrar preferência
```

Enquanto:

```text
Gabriel

↓

Prefere

+2 dB em 3 kHz
```

Essas informações poderão ser utilizadas futuramente para recomendações personalizadas.

---

# Observação dos Participantes

O sistema poderá aprender características individuais.

Exemplos:

- vocalista canta mais forte;
- violonista utiliza pouca dinâmica;
- pregador possui voz grave;
- baixista utiliza compressor com frequência.

---

# Comparação entre Ensaios

A IA poderá comparar sessões anteriores.

Exemplo:

```text
Semana passada

↓

Gain

22 dB

↓

Hoje

↓

26 dB

↓

Mostrar diferença
```

---

# Comparação de Snapshots

O sistema poderá identificar alterações entre snapshots.

Exemplo:

```text
Snapshot A

↓

Snapshot B

↓

Mostrar diferenças
```

---

# Recomendações

Durante o ensaio, a IA poderá sugerir melhorias.

Exemplos:

- reduzir clipping;
- ajustar compressor;
- melhorar inteligibilidade da voz;
- reduzir risco de feedback;
- balancear retornos.

No Modo Ensaio essas sugestões poderão ser mais frequentes e detalhadas do que durante o culto.

---

# Experimentação

O Modo Ensaio permite testar diferentes configurações.

Exemplo:

```text
EQ A

↓

EQ B

↓

Comparar Resultado
```

Esses testes alimentam o aprendizado do sistema.

---

# Registro de Alterações

Todas as alterações poderão ser armazenadas.

Exemplo:

```text
20:42

Canal 08

↓

Gain

+3 dB

↓

Robson
```

---

# Métricas

Ao longo da sessão poderão ser coletadas métricas como:

- duração do ensaio;
- quantidade de ajustes;
- número de snapshots;
- canais mais modificados;
- recomendações aceitas;
- recomendações ignoradas;
- estabilidade da mixagem.

---

# Relatório Final

Ao término do ensaio será possível gerar um relatório contendo:

- resumo da sessão;
- participantes;
- músicas ensaiadas;
- principais ajustes;
- recomendações da IA;
- diferenças em relação ao último ensaio;
- pendências para o culto.

---

# Integração com a IA

O Modo Ensaio fornece informações para diversos componentes da Inteligência Artificial.

Entre eles:

- Context Manager;
- Learning Engine;
- Recommendation Engine;
- Decision Engine;
- Confidence Engine.

---

# Integração com o Histórico

Todas as ações poderão ser consultadas posteriormente.

Isso permitirá:

- auditorias;
- comparação entre ensaios;
- replay de alterações;
- treinamento de novos operadores.

---

# Integração com a Telemetria

Os medidores em tempo real também serão utilizados durante o ensaio.

Exemplos:

- clipping;
- headroom;
- ruído;
- silêncio;
- níveis RMS;
- níveis Peak.

Essas informações ajudam a IA a validar suas recomendações.

---

# Integração com a Liturgia

O sistema poderá relacionar ajustes com cada etapa do evento.

Exemplo:

```text
Louvor

↓

Configuração A

↓

Pregação

↓

Configuração B
```

Isso facilita a preparação dos snapshots.

---

# Diferenças em relação ao Modo Culto

| Modo Ensaio | Modo Culto |
|-------------|------------|
| Aprendizado ativo | Operação estável |
| Registro detalhado | Registro resumido |
| Sugestões frequentes | Sugestões apenas quando necessário |
| Experimentação permitida | Alterações minimizadas |
| Comparações constantes | Execução contínua |

---

# Benefícios

O Modo Ensaio proporciona:

- aprendizado contínuo da IA;
- documentação automática dos ensaios;
- redução do tempo de preparação;
- padronização da operação;
- evolução constante da mixagem;
- melhor preparação para o culto.

---

# Separação de Responsabilidades

O Modo Ensaio não:

- substitui o operador;
- altera automaticamente configurações;
- toma decisões sem autorização;
- interfere na execução do culto.

Sua responsabilidade é fornecer um ambiente seguro para observação, aprendizado e preparação da operação.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- comparação automática entre ensaios;
- avaliação da evolução da equipe;
- sugestões baseadas em histórico de meses ou anos;
- perfis individuais de músicos;
- análise automática da dinâmica da banda;
- geração de snapshots inteligentes;
- treinamento assistido para novos operadores;
- integração com gravações de áudio e vídeo.

---

# Relação com Outros Componentes

O Modo Ensaio trabalha diretamente com:

- Rehearsal Manager;
- Session;
- Observation Engine;
- Learning Capture;
- Scene Comparison;
- Adjustment Tracker;
- Performance Analysis;
- Rehearsal Report;
- History Manager;
- Learning Engine;
- Recommendation Engine;
- Dashboard Operacional;
- Console Operacional.

Ele representa o ambiente de aprendizado do Audio Copilot, transformando cada ensaio em uma fonte estruturada de conhecimento para que a Inteligência Artificial evolua continuamente e ofereça suporte cada vez mais preciso durante os cultos.

---

# Situação da Sprint

**Status:** ✅ Concluída