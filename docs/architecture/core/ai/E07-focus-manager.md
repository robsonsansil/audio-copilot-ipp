# Sprint E07 – Focus Manager

## Objetivo

Definir o componente responsável por controlar o foco visual da interface do Audio Copilot, direcionando a atenção do operador para as informações mais importantes em cada momento da operação.

O **Focus Manager** atua como o "diretor de atenção" da interface. Seu objetivo é evitar que múltiplos destaques concorram entre si, garantindo que o operador visualize primeiro aquilo que realmente exige ação imediata.

Enquanto o **Highlight Manager** administra todos os destaques ativos, o **Focus Manager** decide quais deles devem receber maior evidência visual.

---

# Visão Geral

Durante um culto, diversos eventos podem ocorrer simultaneamente.

Por exemplo:

- clipping em dois microfones;
- feedback em um monitor;
- canal sem sinal;
- bateria baixa em um microfone sem fio;
- sugestão da IA para reduzir um ganho.

Se todos esses elementos forem destacados com a mesma intensidade, a interface ficará confusa.

O Focus Manager organiza essas prioridades.

---

# Filosofia

O Focus Manager foi desenvolvido seguindo cinco princípios.

## Prioridade

Nem todos os alertas possuem a mesma importância.

---

## Contexto

O foco deve considerar o momento atual da liturgia.

---

## Simplicidade

O operador deve enxergar primeiro apenas o que realmente importa.

---

## Continuidade

Mudanças de foco devem ocorrer de forma suave.

---

## Baixa Carga Cognitiva

A interface deve reduzir o esforço mental durante a operação.

---

# Arquitetura

```text
Recommendation Engine

↓

Highlight Engine

↓

Highlight Manager

↓

Focus Manager

↓

Animation System

↓

Console Operacional
```

---

# Responsabilidades

O Focus Manager será responsável por:

- determinar qual destaque receberá maior evidência;
- controlar mudanças de foco;
- evitar excesso de estímulos visuais;
- organizar prioridades;
- coordenar animações relacionadas ao foco;
- adaptar o foco ao contexto operacional.

---

# Fluxo de Funcionamento

```text
Novos Highlights

↓

Analisar Prioridades

↓

Selecionar Foco Principal

↓

Aplicar Destaque

↓

Monitorar Mudanças

↓

Atualizar Foco
```

---

# Conceito de Foco

Em determinado instante, apenas alguns elementos deverão receber atenção máxima.

Exemplo:

```text
Feedback

↓

Canal 08

↓

Foco Principal
```

Enquanto outros problemas permanecem visíveis, porém de forma secundária.

---

# Critérios de Priorização

O Focus Manager poderá considerar diversos fatores.

Entre eles:

- gravidade do problema;
- impacto no áudio;
- etapa da liturgia;
- nível de confiança da IA;
- tempo de permanência;
- quantidade de ocorrências;
- proximidade de uma transição.

---

# Exemplo

```text
Monitor 2

Feedback

Prioridade

Crítica
```

↓

Recebe foco principal.

Enquanto:

```text
Canal 12

Sem sinal

Prioridade

Média
```

↓

Permanece apenas destacado.

---

# Mudança de Foco

Quando surgir um evento mais importante:

```text
Clipping

↓

Feedback

↓

Transferir foco
```

A mudança deverá ocorrer suavemente.

---

# Foco Persistente

Problemas críticos permanecem em destaque até serem resolvidos.

Exemplo:

```text
Feedback

↓

Foco Principal

↓

Enquanto existir
```

---

# Foco Temporário

Alguns eventos exigem atenção apenas por alguns segundos.

Exemplo:

```text
Snapshot carregado

↓

Foco

↓

3 segundos

↓

Remover
```

---

# Múltiplos Problemas

Caso existam diversos problemas simultaneamente:

```text
Canal 08

Clipping

↓

Canal 10

Sem sinal

↓

Monitor 2

Feedback
```

O Focus Manager ordenará todos por prioridade.

---

# Hierarquia de Prioridades

Exemplo:

| Prioridade | Situação |
|------------|----------|
| Crítica | Feedback |
| Alta | Clipping |
| Média | Canal sem sinal |
| Baixa | Sugestão operacional |
| Informativa | Confirmações |

Essa hierarquia poderá ser configurável.

---

# Contexto da Liturgia

O foco também poderá variar conforme a etapa do evento.

Exemplo:

Durante a pregação:

```text
Priorizar

Microfone do pregador
```

Durante o louvor:

```text
Priorizar

Vocais

Playback

Instrumentos
```

---

# Contexto Operacional

O modo atual influencia o foco.

### Ensaio

Maior quantidade de sugestões.

### Culto

Menor quantidade de distrações.

### Técnico

Exibição detalhada de diagnósticos.

---

# Integração com o Highlight Manager

O Highlight Manager informa todos os destaques disponíveis.

O Focus Manager decide quais receberão maior evidência.

---

# Integração com o Animation System

Elementos em foco poderão utilizar animações específicas.

Exemplo:

```text
Glow

↓

Pulsação

↓

Fade
```

Enquanto elementos secundários permanecem estáticos.

---

# Integração com o Channel Overlay

O Overlay poderá apresentar mais informações apenas para o elemento em foco.

Exemplo:

```text
Canal 08

↓

Overlay Expandido
```

Enquanto os demais exibem apenas um pequeno indicador.

---

# Integração com o Dashboard

O Dashboard poderá destacar apenas o foco principal.

Exemplo:

```text
⚠

Feedback

Monitor 2
```

---

# Integração com o Mobile

Na versão mobile apenas o foco principal será exibido em destaque.

Isso evita excesso de informações em telas menores.

---

# Atualização Contínua

O Focus Manager executará reavaliações constantes.

Sempre que ocorrer:

- novo alerta;
- resolução de problema;
- mudança de etapa da liturgia;
- alteração de prioridade;
- mudança de contexto.

O foco poderá ser recalculado automaticamente.

---

# Benefícios

O Focus Manager proporciona:

- redução da sobrecarga visual;
- priorização inteligente das recomendações;
- resposta mais rápida do operador;
- melhor organização da interface;
- integração natural entre IA e operação;
- experiência mais intuitiva.

---

# Separação de Responsabilidades

O Focus Manager não:

- detecta problemas;
- gera recomendações;
- cria destaques;
- controla overlays;
- altera parâmetros da mesa.

Sua responsabilidade é decidir quais elementos da interface devem receber a atenção prioritária do operador.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- foco adaptativo baseado no comportamento do operador;
- aprendizado automático das prioridades;
- personalização por perfil de operador;
- múltiplos operadores simultâneos;
- foco colaborativo em ambientes com várias mesas;
- integração com eye tracking;
- priorização baseada em histórico de incidentes;
- ajuste automático conforme a carga de trabalho.

---

# Relação com Outros Componentes

O Focus Manager trabalha diretamente com:

- Highlight Engine;
- Highlight Manager;
- Highlight Rules;
- Channel Overlay;
- Animation System;
- Notification Badges;
- Visual Priority;
- Recommendation Engine;
- Decision Engine;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA.

Ele representa a camada responsável por direcionar a atenção do operador dentro do Audio Copilot, garantindo que os alertas mais importantes sejam apresentados com prioridade, reduzindo distrações e tornando a operação mais segura, eficiente e intuitiva.

---

# Situação da Sprint

**Status:** ✅ Concluída