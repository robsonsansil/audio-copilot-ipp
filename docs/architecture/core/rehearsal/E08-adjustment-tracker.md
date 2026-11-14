# Sprint E08 – Adjustment Tracker

## Objetivo

Definir o componente responsável por registrar, organizar e acompanhar todas as alterações realizadas durante uma sessão de ensaio.

O **Adjustment Tracker** é responsável por documentar cada modificação efetuada pelo operador, permitindo reconstruir toda a evolução da mixagem ao longo do ensaio.

Enquanto o **Observation Engine** observa os eventos e o **Learning Capture** prepara os dados para aprendizado, o Adjustment Tracker mantém o histórico detalhado de todos os ajustes realizados na mesa.

---

# Visão Geral

Durante um ensaio são realizados centenas de pequenos ajustes.

Exemplos:

- aumentar ganho;
- reduzir o volume;
- alterar equalização;
- modificar compressor;
- ajustar monitores;
- carregar snapshots;
- trocar efeitos.

Essas alterações representam o processo de construção da mixagem.

O Adjustment Tracker registra toda essa evolução.

---

# Filosofia

O Adjustment Tracker foi desenvolvido seguindo cinco princípios.

## Precisão

Cada alteração deve ser registrada exatamente como ocorreu.

---

## Cronologia

Os ajustes devem permanecer na ordem em que aconteceram.

---

## Contexto

Toda alteração deve possuir informações suficientes para ser compreendida futuramente.

---

## Rastreabilidade

Sempre deve ser possível identificar quem realizou uma alteração e quando ela ocorreu.

---

## Transparência

Nenhuma modificação importante deve ocorrer sem registro.

---

# Arquitetura

```text
Operador

↓

Mesa Ui24R

↓

Observation Engine

↓

Adjustment Tracker

↓

History Manager

↓

Rehearsal Report
```

---

# Responsabilidades

O Adjustment Tracker será responsável por:

- registrar alterações;
- organizar cronologicamente os ajustes;
- identificar responsáveis;
- agrupar alterações relacionadas;
- disponibilizar histórico para consultas;
- fornecer dados para relatórios e aprendizado.

---

# Fluxo Geral

```text
Alteração

↓

Capturar

↓

Registrar

↓

Adicionar Contexto

↓

Armazenar

↓

Disponibilizar
```

---

# Ajustes Monitorados

O componente poderá registrar alterações em:

- Gain;
- Fader;
- Equalizador;
- Compressor;
- Gate;
- Panorama;
- Delay;
- Reverb;
- Auxiliares;
- Mute;
- Solo;
- Phantom Power;
- Polaridade;
- DCA;
- Grupos;
- Snapshots.

---

# Exemplo

```text
20:14

Canal 08

↓

Gain

22 dB

↓

25 dB

↓

Operador

Robson
```

---

Outro exemplo:

```text
20:27

Monitor 2

↓

Aux Send

-2 dB
```

---

# Estrutura do Registro

Cada ajuste poderá armazenar:

- identificador;
- data;
- horário;
- canal;
- parâmetro alterado;
- valor anterior;
- novo valor;
- operador responsável;
- etapa da liturgia;
- observações.

---

# Registro Cronológico

Todas as alterações permanecem organizadas na sequência em que ocorreram.

Exemplo:

```text
20:10

Gain

↓

20:11

EQ

↓

20:13

Compressor

↓

20:15

Snapshot
```

Isso permite reconstruir toda a evolução da sessão.

---

# Agrupamento

Alterações consecutivas poderão ser agrupadas.

Exemplo:

```text
Canal 05

↓

Gain

↓

EQ

↓

Compressor
```

↓

Um único bloco de ajuste.

Essa estratégia facilita a leitura do histórico.

---

# Ajustes por Canal

O sistema poderá listar todas as alterações realizadas em um canal específico.

Exemplo:

```text
Canal 08

↓

15 alterações

↓

Resumo
```

---

# Ajustes por Operador

Também será possível visualizar ajustes realizados por um operador específico.

Exemplo:

```text
Robson

↓

42 alterações
```

---

# Ajustes por Participante

O histórico poderá ser organizado por músico ou participante.

Exemplo:

```text
Vocal Azul

↓

12 alterações

↓

Durante o Louvor
```

---

# Ajustes por Música

As alterações poderão ser associadas às músicas ensaiadas.

Exemplo:

```text
Música

Sola Scriptura

↓

8 ajustes
```

---

# Ajustes por Snapshot

Também será possível visualizar todas as alterações realizadas antes de um snapshot.

Exemplo:

```text
Snapshot Louvor

↓

24 ajustes
```

---

# Associação Temporal

O componente manterá relação entre eventos próximos.

Exemplo:

```text
Clipping

↓

Operador reduz Gain

↓

Clipping desaparece
```

Essa sequência será útil para análises futuras.

---

# Integração com o Learning Capture

Os registros poderão ser utilizados para identificar padrões de operação.

Exemplo:

```text
Sempre reduz

2 dB

↓

Registrar preferência
```

---

# Integração com o History Manager

Todos os ajustes também serão armazenados no histórico permanente do sistema.

---

# Integração com o Scene Comparison

Os registros facilitarão a identificação das diferenças entre snapshots.

Exemplo:

```text
Snapshot A

↓

Snapshot B

↓

Mostrar quais ajustes produziram a diferença
```

---

# Integração com o Dashboard

O Dashboard poderá apresentar indicadores como:

- número de ajustes;
- canais mais alterados;
- parâmetros mais modificados;
- operador mais ativo.

---

# Integração com o Replay

Durante um Replay será possível acompanhar exatamente quando cada ajuste ocorreu.

Exemplo:

```text
20:15

↓

Gain +2 dB

↓

20:16

EQ -3 dB

↓

20:18

Snapshot
```

---

# Pesquisa

Os registros poderão ser filtrados por:

- canal;
- operador;
- parâmetro;
- música;
- participante;
- data;
- tipo de ajuste.

---

# Benefícios

O Adjustment Tracker proporciona:

- histórico completo das alterações;
- rastreabilidade da operação;
- facilidade para auditoria;
- suporte ao aprendizado da IA;
- documentação automática dos ensaios;
- reconstrução detalhada da evolução da mixagem.

---

# Separação de Responsabilidades

O Adjustment Tracker não:

- observa eventos diretamente;
- aprende padrões;
- gera recomendações;
- altera parâmetros da mesa;
- compara snapshots.

Sua responsabilidade é registrar e organizar todas as alterações realizadas durante o ensaio.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- agrupamento inteligente de ajustes;
- classificação automática por impacto;
- identificação de alterações redundantes;
- sugestões de reversão;
- análise estatística de parâmetros mais ajustados;
- comparação entre operadores;
- integração com gravações de áudio;
- exportação completa do histórico de ajustes.

---

# Relação com Outros Componentes

O Adjustment Tracker trabalha diretamente com:

- Rehearsal Manager;
- Session;
- Observation Engine;
- Learning Capture;
- Scene Comparison;
- Performance Analysis;
- History Manager;
- Replay;
- Learning Engine;
- Dashboard Operacional;
- Console Operacional.

Ele representa o registro operacional detalhado do Audio Copilot, documentando cada alteração realizada durante o ensaio e fornecendo uma base sólida para auditoria, comparação, aprendizado da Inteligência Artificial e evolução contínua da operação da mesa de som.

---

# Situação da Sprint

**Status:** ✅ Concluída