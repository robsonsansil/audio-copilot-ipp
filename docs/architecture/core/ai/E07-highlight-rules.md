# Sprint E07 – Highlight Rules

## Objetivo

Definir o conjunto de regras responsáveis por determinar **quando**, **como** e **em quais condições** um destaque visual deverá ser apresentado ao operador pelo Audio Copilot.

O Highlight Rules estabelece os critérios utilizados pelo Highlight Engine para transformar recomendações da Inteligência Artificial em elementos visuais consistentes, previsíveis e contextualizados.

Enquanto o **Recommendation Engine** identifica situações relevantes e o **Highlight Engine** cria os destaques, o **Highlight Rules** define as políticas que governam esse comportamento.

---

# Visão Geral

Nem toda recomendação da IA deve gerar o mesmo tipo de destaque.

Algumas situações exigem atenção imediata.

Outras podem permanecer apenas como uma sugestão discreta.

O Highlight Rules define essas diferenças.

Exemplos:

- feedback → destaque crítico;
- clipping → destaque de alta prioridade;
- canal sem sinal → destaque médio;
- sugestão de melhoria → destaque discreto.

---

# Filosofia

O Highlight Rules foi desenvolvido seguindo cinco princípios.

## Consistência

Situações iguais devem produzir sempre o mesmo comportamento visual.

---

## Prioridade

Problemas críticos devem receber maior destaque.

---

## Contexto

As regras devem considerar o momento da operação.

---

## Simplicidade

Os destaques devem ser fáceis de interpretar.

---

## Escalabilidade

Novas regras poderão ser adicionadas sem alterar o funcionamento do sistema.

---

# Arquitetura

```text
Recommendation Engine

↓

Decision Engine

↓

Highlight Rules

↓

Highlight Engine

↓

Highlight Manager
```

---

# Responsabilidades

O Highlight Rules será responsável por:

- definir quando criar um destaque;
- determinar o tipo de destaque;
- definir cores;
- definir prioridade;
- definir animações;
- definir duração;
- impedir conflitos entre regras.

---

# Fluxo de Funcionamento

```text
Nova Recomendação

↓

Consultar Regras

↓

Encontrar Regra

↓

Aplicar Configuração

↓

Enviar ao Highlight Engine
```

---

# Estrutura de uma Regra

Cada regra poderá conter:

```text
Tipo

Clipping

Prioridade

Alta

Cor

Laranja

Animação

Pulsação

Persistência

Enquanto houver clipping
```

---

# Componentes de uma Regra

Cada regra poderá definir:

- condição de ativação;
- prioridade;
- elemento destacado;
- cor;
- animação;
- duração;
- condição de encerramento;
- comportamento em caso de conflito.

---

# Exemplo de Regra

```text
SE

Feedback detectado

ENTÃO

Destacar canal

Cor Vermelha

Pulsação rápida

Prioridade Crítica
```

---

# Outro Exemplo

```text
SE

Canal sem sinal

ENTÃO

Exibir ícone cinza

Sem animação

Prioridade Média
```

---

# Categorias de Regras

As regras poderão ser agrupadas em categorias.

## Áudio

Exemplos:

- clipping;
- feedback;
- saturação;
- ruído;
- ausência de sinal.

---

## Operação

Exemplos:

- canal mutado;
- ganho elevado;
- fader abaixo do esperado;
- auxiliar desbalanceado.

---

## Liturgia

Exemplos:

- participante prestes a entrar;
- transição de etapa;
- próximo microfone.

---

## Sistema

Exemplos:

- conexão perdida;
- snapshot carregado;
- sincronização concluída.

---

## Inteligência Artificial

Exemplos:

- recomendação disponível;
- sugestão aceita;
- sugestão rejeitada;
- confiança elevada.

---

# Prioridades

As regras definem quatro níveis de prioridade.

| Prioridade | Cor | Exemplo |
|------------|-----|----------|
| Crítica | Vermelho | Feedback |
| Alta | Laranja | Clipping |
| Média | Azul | Ajuste recomendado |
| Baixa | Cinza | Informação |

Essas prioridades são utilizadas pelo Highlight Manager para organizar a interface.

---

# Duração dos Destaques

Cada regra poderá definir sua duração.

Exemplo:

```text
Feedback

↓

Enquanto existir.
```

```text
Sugestão

↓

5 segundos.
```

```text
Confirmação

↓

2 segundos.
```

---

# Regras Temporárias

Alguns destaques aparecem apenas por alguns instantes.

Exemplo:

```text
Snapshot carregado

↓

Exibir confirmação

↓

2 segundos

↓

Remover
```

---

# Regras Persistentes

Outros permanecem ativos até que a condição desapareça.

Exemplo:

```text
Microfone sem sinal

↓

Permanece destacado

↓

Até o retorno do áudio
```

---

# Conflitos

Uma mesma interface poderá receber múltiplas recomendações simultaneamente.

Exemplo:

```text
Canal 08

↓

Clipping

↓

Feedback

↓

Canal silencioso
```

Nesses casos, prevalecerá a regra de maior prioridade.

---

# Regras Dependentes do Contexto

As regras poderão variar conforme o modo operacional.

Exemplo:

### Ensaio

```text
Mostrar sugestões de equalização.
```

### Culto

```text
Mostrar apenas alertas relevantes.
```

---

# Integração com o Focus Manager

Após definir as regras, o Focus Manager decidirá quais destaques receberão maior atenção visual.

---

# Integração com o Animation System

Cada regra poderá definir uma animação específica.

Exemplos:

- pulsação;
- brilho;
- fade;
- transição suave;
- destaque contínuo.

---

# Integração com o Channel Overlay

O Highlight Rules determina quais informações serão exibidas sobre o canal.

Exemplo:

```text
⚠

Reduzir Gain

≈ 2 dB
```

---

# Integração com o Histórico

As regras aplicadas poderão ser registradas.

Exemplo:

```text
09:42

Regra aplicada

Clipping

↓

Highlight criado
```

Esses registros auxiliam auditorias e treinamentos.

---

# Benefícios

O Highlight Rules proporciona:

- padronização visual;
- comportamento previsível;
- redução de ambiguidades;
- organização das recomendações;
- maior clareza operacional;
- facilidade de manutenção do sistema.

---

# Separação de Responsabilidades

O Highlight Rules não:

- detecta problemas;
- gera recomendações;
- cria elementos gráficos;
- controla animações;
- altera parâmetros da mesa.

Sua responsabilidade é definir as regras que orientam como cada recomendação da IA será apresentada visualmente ao operador.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- regras personalizadas por igreja;
- perfis de operadores;
- temas de acessibilidade;
- regras adaptativas baseadas em aprendizado;
- configuração visual pelo usuário;
- regras específicas para diferentes tipos de evento;
- integração com múltiplos dispositivos;
- ajuste automático conforme a carga cognitiva do operador.

---

# Relação com Outros Componentes

O Highlight Rules trabalha diretamente com:

- Recommendation Engine;
- Decision Engine;
- Highlight Engine;
- Highlight Manager;
- Focus Manager;
- Channel Overlay;
- Animation System;
- Visual Priority;
- Dashboard Operacional;
- Console Operacional.

Ele representa a camada de políticas visuais do Audio Copilot, definindo de forma consistente quando, como e com qual intensidade as recomendações da Inteligência Artificial devem ser destacadas, garantindo uma experiência clara, organizada e eficiente para o operador.

---

# Situação da Sprint

**Status:** ✅ Concluída