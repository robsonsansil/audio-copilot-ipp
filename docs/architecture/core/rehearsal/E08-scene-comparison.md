# Sprint E08 – Scene Comparison

## Objetivo

Definir o componente responsável por comparar snapshots, cenas e configurações da mesa de som, identificando automaticamente todas as diferenças existentes entre duas ou mais versões.

O **Scene Comparison** permite que operadores e a Inteligência Artificial compreendam rapidamente o que mudou entre diferentes ensaios, cultos ou snapshots, facilitando a identificação de ajustes recorrentes, modificações inesperadas e oportunidades de padronização.

Enquanto o **Adjustment Tracker** registra cada alteração individual realizada durante a operação, o Scene Comparison analisa o resultado final dessas alterações comparando configurações completas.

---

# Visão Geral

Durante um ensaio é comum criar diversas versões de uma mesma cena.

Exemplo:

```text
Snapshot Inicial

↓

Louvor

↓

Pregação

↓

Culto Noturno

↓

Versão Final
```

Ao longo do tempo torna-se difícil lembrar exatamente o que mudou entre essas versões.

O Scene Comparison resolve esse problema realizando comparações automáticas entre snapshots.

---

# Filosofia

O Scene Comparison foi desenvolvido seguindo cinco princípios.

## Precisão

Toda diferença encontrada deve refletir exatamente a configuração da mesa.

---

## Clareza

As diferenças devem ser apresentadas de forma simples e objetiva.

---

## Contextualização

Cada alteração deve ser relacionada ao contexto em que ocorreu.

---

## Escalabilidade

O sistema deve suportar comparações entre qualquer quantidade de snapshots.

---

## Integração

Os resultados devem alimentar os demais módulos da Inteligência Artificial.

---

# Arquitetura

```text
Snapshots

↓

Scene Comparison

├── Snapshot A
├── Snapshot B
├── Diferenças
├── Classificação
└── Relatório

↓

Dashboard

↓

IA
```

---

# Responsabilidades

O Scene Comparison será responsável por:

- comparar snapshots;
- identificar diferenças;
- classificar alterações;
- gerar resumos das mudanças;
- alimentar o Learning Engine;
- fornecer informações para auditoria.

---

# Fluxo Geral

```text
Selecionar Snapshots

↓

Comparar

↓

Identificar Diferenças

↓

Classificar

↓

Gerar Resultado
```

---

# Comparação de Snapshots

O sistema poderá comparar qualquer combinação de snapshots.

Exemplo:

```text
Ensaio da Semana Passada

↓

Comparar

↓

Ensaio Atual
```

Ou:

```text
Snapshot Louvor

↓

Comparar

↓

Snapshot Pregação
```

---

# Comparação de Parâmetros

O Scene Comparison poderá analisar alterações em diversos parâmetros.

Exemplos:

- Gain;
- Fader;
- Equalizador;
- Compressor;
- Gate;
- Delay;
- Reverb;
- Auxiliares;
- Panorama;
- Polaridade;
- Phantom Power;
- Mute;
- DCA;
- Grupos.

---

# Exemplo

```text
Canal 08

Gain

22 dB

↓

25 dB
```

Resultado:

```text
+3 dB
```

---

Outro exemplo:

```text
EQ

250 Hz

↓

-2 dB

↓

+1 dB
```

Resultado:

```text
Alteração de 3 dB
```

---

# Comparação Global

O sistema poderá gerar um resumo completo.

Exemplo:

```text
Snapshots Comparados

↓

186 parâmetros iguais

↓

24 parâmetros alterados

↓

5 canais modificados
```

---

# Classificação das Alterações

Cada diferença poderá receber uma classificação.

Exemplo:

- alteração de ganho;
- alteração de equalização;
- alteração dinâmica;
- alteração de monitor;
- alteração de efeitos;
- alteração estrutural;
- alteração de roteamento.

---

# Identificação de Mudanças Relevantes

Nem toda diferença possui a mesma importância.

Exemplo:

```text
Gain

↓

+8 dB
```

Possui maior impacto que:

```text
Panorama

↓

2%
```

O sistema poderá destacar apenas alterações relevantes.

---

# Comparação Temporal

O componente poderá comparar versões produzidas em momentos diferentes.

Exemplo:

```text
Culto Domingo

↓

Semana 1

↓

Semana 2

↓

Semana 3
```

Permitindo visualizar a evolução das configurações.

---

# Comparação por Participante

Também será possível comparar configurações de um mesmo participante.

Exemplo:

```text
Pastor

↓

Janeiro

↓

Julho

↓

Outubro
```

A IA poderá identificar mudanças de padrão ao longo do tempo.

---

# Comparação por Música

Os snapshots utilizados em uma música poderão ser comparados.

Exemplo:

```text
Música

Sola Scriptura

↓

Ensaio

↓

Culto
```

Assim será possível verificar quais ajustes foram realizados entre a preparação e a execução.

---

# Comparação por Operador

O componente poderá comparar diferentes operadores.

Exemplo:

```text
Robson

↓

Snapshot A

↓

Gabriel

↓

Snapshot B
```

A IA poderá identificar estilos de operação distintos.

---

# Integração com o Learning Engine

As diferenças encontradas poderão alimentar o processo de aprendizado.

Exemplo:

```text
Toda semana

↓

Mesmo ajuste

↓

Registrar padrão
```

---

# Integração com o Recommendation Engine

O histórico de comparações poderá gerar recomendações.

Exemplo:

```text
Sempre aumenta

2 dB

↓

Sugerir automaticamente
```

---

# Integração com o History Manager

Cada comparação poderá ser armazenada.

Isso permitirá auditorias futuras e análise da evolução da mixagem.

---

# Integração com o Dashboard

O Dashboard poderá apresentar um resumo das diferenças.

Exemplo:

```text
Última comparação

↓

18 alterações

↓

3 críticas

↓

12 recomendadas
```

---

# Integração com o Rehearsal Report

O relatório do ensaio poderá incluir automaticamente um resumo das diferenças encontradas em relação ao ensaio anterior.

Exemplo:

- canais alterados;
- snapshots modificados;
- novas configurações;
- ajustes recorrentes.

---

# Visualização

As diferenças poderão ser exibidas em diversos formatos.

Exemplos:

- lista;
- tabela;
- timeline;
- comparação lado a lado;
- destaques por canal;
- gráfico de alterações.

---

# Benefícios

O Scene Comparison proporciona:

- identificação rápida das mudanças;
- comparação objetiva entre snapshots;
- padronização da operação;
- apoio ao aprendizado da IA;
- facilidade de auditoria;
- redução de erros durante a preparação.

---

# Separação de Responsabilidades

O Scene Comparison não:

- altera configurações;
- gera snapshots;
- registra eventos em tempo real;
- aprende padrões diretamente;
- toma decisões.

Sua responsabilidade é comparar configurações existentes e apresentar suas diferenças de forma estruturada.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- comparação entre múltiplos snapshots simultaneamente;
- comparação visual por canal;
- comparação de eventos completos;
- detecção automática de alterações críticas;
- sugestões de padronização;
- comparação entre diferentes igrejas;
- integração com Replay para visualizar quando cada alteração ocorreu;
- comparação utilizando métricas de áudio registradas durante o ensaio.

---

# Relação com Outros Componentes

O Scene Comparison trabalha diretamente com:

- Rehearsal Manager;
- Session;
- Adjustment Tracker;
- Observation Engine;
- Learning Capture;
- Learning Engine;
- Recommendation Engine;
- History Manager;
- Replay;
- Dashboard Operacional;
- Console Operacional.

Ele representa o mecanismo de comparação estrutural do Audio Copilot, permitindo analisar a evolução das configurações da mesa ao longo do tempo e fornecendo informações valiosas para padronização, auditoria e aprendizado contínuo da Inteligência Artificial.

---

# Situação da Sprint

**Status:** ✅ Concluída