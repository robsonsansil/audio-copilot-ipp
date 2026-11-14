# Sprint E06 – Change Log

## Objetivo

Definir o componente responsável por registrar todas as alterações realizadas nos parâmetros da mesa de som durante a operação.

O Change Log representa o histórico técnico do Audio Copilot. Seu objetivo é armazenar, de forma cronológica e detalhada, cada modificação realizada nos canais, barramentos, processamentos e configurações da mesa de som, independentemente da origem da alteração.

Enquanto o **History Manager** coordena todo o subsistema de histórico, o **Change Log** registra especificamente **o que foi alterado na mesa**.

---

# Visão Geral

Durante um culto, centenas ou até milhares de parâmetros podem ser modificados.

Entre eles:

- ganho (Gain);
- fader;
- mute;
- pan;
- phantom power;
- HPF;
- Gate;
- Compressor;
- Equalizador;
- Aux Sends;
- FX Sends;
- DCA;
- Matrix;
- Master.

Cada alteração representa uma informação importante para auditoria, aprendizado da IA e reprodução posterior do evento.

---

# Filosofia

O Change Log foi desenvolvido seguindo cinco princípios.

## Precisão

Toda alteração deve registrar exatamente o valor anterior e o novo valor.

---

## Cronologia

As alterações devem permanecer organizadas pela ordem em que ocorreram.

---

## Neutralidade

O Change Log apenas registra.

Ele nunca interpreta a alteração.

---

## Integridade

Nenhuma alteração confirmada deve ser perdida.

---

## Rastreabilidade

Cada modificação deve indicar sua origem.

---

# Arquitetura

```text
Ui24R

↓

State Manager

↓

Change Log

↓

History Manager

↓

Banco de Histórico

↓

Replay

↓

Learning Engine
```

---

# Responsabilidades

O Change Log será responsável por:

- registrar alterações dos parâmetros da mesa;
- armazenar valores anteriores e atuais;
- identificar a origem da alteração;
- manter ordem cronológica;
- fornecer histórico técnico para consultas;
- alimentar auditorias e replay.

---

# O que é considerado uma alteração?

Uma alteração ocorre sempre que algum parâmetro muda de valor.

Exemplos:

```text
Gain

18 dB

↓

20 dB
```

```text
Mute

OFF

↓

ON
```

```text
Fader

-10 dB

↓

-5 dB
```

---

# Alterações Registradas

O sistema poderá registrar alterações em:

## Entrada

- Gain
- Phantom
- Polaridade
- HPF

---

## Equalizador

- Frequência
- Ganho
- Q
- Bandas ativadas

---

## Gate

- Threshold
- Attack
- Hold
- Release
- Range

---

## Compressor

- Threshold
- Ratio
- Attack
- Release
- Makeup Gain

---

## Fader

- posição;
- mute;
- solo;
- pan.

---

## Auxiliares

- Aux Sends;
- FX Sends;
- Matrix Sends;
- DCA.

---

## Master

- nível;
- mute;
- processamento;
- configurações globais.

---

# Estrutura de um Registro

Cada alteração poderá conter as seguintes informações.

```text
ID

CHG-000548

Data

12/05/2028

Hora

09:42:18

Canal

08

Parâmetro

Gain

Valor Anterior

18 dB

Novo Valor

20 dB

Origem

Operador
```

---

# Origem da Alteração

Toda alteração possuirá uma origem identificada.

Exemplo:

```text
Operador
```

```text
Mesa Ui24R
```

```text
Sistema
```

```text
Automação
```

No futuro:

```text
IA
```

Caso existam alterações automáticas aprovadas pelo operador.

---

# Agrupamento

Alterações realizadas em sequência poderão ser agrupadas.

Exemplo:

```text
Canal 08

Gain

↓

EQ

↓

Compressor

↓

Fader
```

Ao invés de quatro registros independentes, o sistema poderá exibir:

```text
Canal 08

4 alterações realizadas.
```

Essa visualização melhora a leitura do histórico.

---

# Registro Cronológico

O Change Log mantém todas as alterações em ordem temporal.

```text
09:41:02

Gain

↓

09:41:08

EQ

↓

09:41:21

Compressor

↓

09:41:37

Fader
```

Essa sequência permite reconstruir exatamente a operação.

---

# Integração com o Replay

O Replay utiliza o Change Log para reproduzir as alterações da mesa.

Exemplo:

```text
09:41

Gain +2 dB

↓

09:42

Mute

↓

09:43

EQ

↓

09:44

Fader
```

Toda movimentação poderá ser reproduzida.

---

# Integração com o Learning Engine

O Learning Engine poderá identificar padrões.

Exemplo:

```text
Após iniciar a Pregação

↓

Operador reduz
o retorno em 2 dB.
```

Esse padrão poderá gerar futuras recomendações.

---

# Integração com Auditoria

O módulo de Auditoria poderá responder perguntas como:

```text
Quem alterou?

↓

Quando?

↓

Qual parâmetro?

↓

Qual era o valor anterior?

↓

Qual foi o novo valor?
```

---

# Integração com Relatórios

Ao término do evento, será possível gerar estatísticas.

Exemplo:

```text
Resumo

Alterações

312

Gain

24

EQ

58

Faders

143

Mute

87
```

---

# Consultas

O Change Log permitirá pesquisas por diversos critérios.

Exemplos:

```text
Todas as alterações do Canal 08.
```

```text
Alterações realizadas durante a Pregação.
```

```text
Mudanças feitas pelo operador.
```

```text
Alterações de Gain.
```

---

# Desempenho

O registro deverá ocorrer em tempo real.

A gravação do histórico nunca poderá causar atraso na operação da mesa.

Por isso, o componente deverá utilizar mecanismos assíncronos de gravação sempre que possível.

---

# Benefícios

O Change Log proporciona:

- rastreabilidade completa;
- histórico técnico detalhado;
- suporte à auditoria;
- base para replay;
- suporte ao aprendizado da IA;
- geração de estatísticas operacionais;
- facilidade na identificação de alterações indevidas.

---

# Separação de Responsabilidades

O Change Log não:

- interpreta alterações;
- gera recomendações;
- calcula estatísticas;
- aprende padrões;
- modifica parâmetros da mesa.

Sua única responsabilidade é registrar todas as alterações técnicas realizadas na operação da mesa de som.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- agrupamento inteligente de alterações;
- comparação entre snapshots;
- visualização gráfica da evolução dos parâmetros;
- filtros avançados por tipo de alteração;
- exportação para CSV, JSON e PDF;
- pesquisa por intervalo de tempo;
- integração com controle de versões de configurações.

---

# Relação com Outros Componentes

O Change Log trabalha diretamente com:

- History Manager;
- State Manager;
- Telemetry Manager;
- Replay;
- Audit;
- Learning Engine;
- Statistics;
- Dashboard Operacional;
- Console Operacional.

Ele representa o registro técnico detalhado da operação da mesa de som, preservando cada alteração realizada ao longo do evento e fornecendo a base para auditoria, reprodução, análise e evolução contínua do Audio Copilot.

---

# Situação da Sprint

**Status:** ✅ Concluída