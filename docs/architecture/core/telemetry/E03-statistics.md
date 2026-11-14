# Sprint E03 – Statistics

## Objetivo

Definir o componente responsável por consolidar estatísticas da operação de áudio durante ensaios e eventos.

Enquanto os demais componentes da Telemetria trabalham com informações em tempo real, o Statistics é responsável por transformar esses dados em indicadores históricos, métricas operacionais e informações que auxiliam tanto o operador quanto a Inteligência Artificial na análise do comportamento do sistema.

Este componente não realiza monitoramento em tempo real da interface.

Seu objetivo é produzir conhecimento a partir dos dados coletados.

---

# Visão Geral

Durante um evento, milhares de informações são processadas pela Telemetria.

Grande parte desses dados possui valor apenas naquele instante.

O Statistics tem a responsabilidade de transformar esse fluxo contínuo em indicadores úteis para análise posterior.

Exemplos:

- tempo total de utilização de um canal;
- quantidade de clipping;
- maior nível registrado;
- média de utilização;
- tempo sem sinal;
- quantidade de alterações realizadas.

Essas informações servirão para auditoria, relatórios e aprendizado da IA.

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
Eventos de Telemetria
        │
        ▼
Statistics
        │
        ├────────► Histórico
        ├────────► Painel da IA
        ├────────► Relatórios
        └────────► Dashboard
```

O Statistics trabalha sobre eventos já processados.

Ele nunca consulta diretamente a Ui24R.

---

# Responsabilidades

O Statistics será responsável por:

- consolidar métricas do evento;
- calcular médias e máximos;
- registrar contadores;
- produzir indicadores operacionais;
- disponibilizar informações para relatórios;
- fornecer dados históricos para a IA.

---

# Estatísticas por Canal

Para cada canal poderão ser registradas informações como:

- tempo total ativo;
- tempo em mute;
- tempo sem sinal;
- maior Peak registrado;
- nível médio;
- quantidade de clipping;
- quantidade de picos;
- número de alterações realizadas;
- quantidade de ativações e desativações.

Exemplo:

```text
Canal 05

Vocal Alessandra

Tempo ativo:
1h18min

Peak máximo:
-2,1 dB

Clipping:
0

Mute:
2 vezes

Sem sinal:
18 segundos
```

---

# Estatísticas das Saídas

Também poderão ser registradas métricas das saídas.

Exemplos:

- maior nível do PA;
- maior nível dos monitores;
- nível médio da transmissão;
- utilização dos auxiliares;
- tempo total de operação.

---

# Estatísticas do Evento

Ao final de cada evento poderão ser calculados indicadores gerais.

Exemplos:

- duração do evento;
- quantidade de canais utilizados;
- quantidade de participantes;
- número de ajustes realizados;
- quantidade de recomendações da IA;
- alterações aprovadas;
- alterações recusadas.

---

# Estatísticas da Inteligência Artificial

O Statistics também acompanhará o desempenho da IA.

Exemplos:

- recomendações emitidas;
- recomendações aceitas;
- recomendações ignoradas;
- recomendações rejeitadas;
- tempo médio de resposta da IA.

Essas informações serão importantes para avaliar a evolução do sistema.

---

# Estatísticas de Operação

Durante o evento poderão ser registradas métricas como:

- quantidade de mudanças de ganho;
- alterações de equalização;
- mudanças de compressor;
- alterações de fader;
- utilização de snapshots;
- alterações de cena.

Esses dados permitem compreender o comportamento da operação.

---

# Integração com o Histórico

O Statistics utiliza os eventos registrados pelo Histórico para consolidar suas métricas.

Fluxo:

```text
Evento

↓

Histórico

↓

Statistics

↓

Relatórios
```

---

# Integração com a Inteligência Artificial

A IA utilizará essas estatísticas para aprender padrões de operação.

Exemplo:

```text
Durante os últimos 20 cultos:

O canal do Pastor nunca apresentou clipping.

↓

A IA passa a considerar esse comportamento como padrão.
```

Outro exemplo:

```text
O Violão Martin normalmente necessita de +3 dB de ganho.

↓

A IA poderá sugerir esse ajuste em futuros eventos.
```

Com o tempo, essas estatísticas contribuirão para recomendações cada vez mais precisas.

---

# Atualização

Nem todas as estatísticas precisam ser atualizadas em tempo real.

Cada indicador poderá possuir sua própria frequência de consolidação.

Exemplos:

- durante o evento;
- ao término da música;
- ao final do culto;
- no encerramento do evento.

Essa estratégia reduz o processamento desnecessário.

---

# Relatórios

As estatísticas poderão alimentar diversos relatórios.

Exemplos:

- relatório do evento;
- relatório técnico;
- relatório da IA;
- relatório por participante;
- relatório por canal;
- histórico de operação.

---

# Benefícios

A utilização do Statistics oferece diversas vantagens:

- compreensão do comportamento da operação;
- geração de relatórios automáticos;
- suporte à auditoria técnica;
- identificação de padrões recorrentes;
- auxílio ao treinamento da IA;
- base para indicadores de desempenho.

---

# Separação de Responsabilidades

O Statistics possui uma única responsabilidade.

Ele não:

- monitora níveis em tempo real;
- detecta clipping;
- detecta silêncio;
- controla a interface;
- envia comandos para a Ui24R.

Sua função é exclusivamente consolidar e disponibilizar estatísticas da operação.

---

# Evoluções Futuras

Nas próximas versões, o Statistics poderá incorporar funcionalidades como:

- comparação entre eventos;
- indicadores de estabilidade da operação;
- ranking dos canais mais utilizados;
- métricas por operador de áudio;
- análise de tendências ao longo do tempo;
- gráficos históricos;
- indicadores de desempenho da equipe de sonorização;
- geração automática de insights para a Inteligência Artificial.

---

# Situação da Sprint

**Status:** ✅ Concluída