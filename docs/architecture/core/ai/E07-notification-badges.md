# Sprint E07 – Notification Badges

## Objetivo

Definir o componente responsável por exibir pequenos indicadores visuais (badges) que comunicam rapidamente informações importantes produzidas pela Inteligência Artificial durante a operação do Audio Copilot.

Os **Notification Badges** são indicadores compactos que aparecem diretamente sobre elementos da interface, permitindo que o operador identifique situações relevantes sem interromper seu fluxo de trabalho.

Enquanto o **Channel Overlay** apresenta informações completas e o **Highlight Manager** controla os destaques, os **Notification Badges** oferecem uma comunicação rápida, discreta e contínua.

---

# Visão Geral

Durante um evento, a IA poderá identificar dezenas de situações diferentes.

Nem todas exigem um grande destaque visual.

Em muitos casos, um pequeno indicador é suficiente para informar ao operador que existe uma recomendação ou condição associada àquele elemento.

Exemplos:

- nova sugestão da IA;
- clipping detectado;
- canal sem sinal;
- bateria baixa;
- recomendação ainda não visualizada;
- alerta crítico.

Os Notification Badges foram criados exatamente para esse tipo de comunicação.

---

# Filosofia

O Notification Badges foi desenvolvido seguindo cinco princípios.

## Discrição

Os indicadores ocupam pouco espaço na interface.

---

## Clareza

Cada badge deve transmitir seu significado rapidamente.

---

## Consistência

Todos os badges seguem um padrão visual único.

---

## Contextualização

Cada badge aparece apenas quando fizer sentido.

---

## Prioridade

Os badges devem refletir a gravidade da informação apresentada.

---

# Arquitetura

```text
Recommendation Engine

↓

Highlight Engine

↓

Highlight Manager

↓

Notification Badges

↓

Console Operacional

↓

Dashboard
```

---

# Responsabilidades

O Notification Badges será responsável por:

- exibir indicadores visuais;
- representar o estado da IA;
- informar prioridade;
- indicar novas recomendações;
- comunicar situações pendentes;
- atualizar badges em tempo real.

---

# Fluxo de Funcionamento

```text
Nova Recomendação

↓

Highlight Manager

↓

Criar Badge

↓

Exibir na Interface

↓

Atualizar

↓

Remover
```

---

# Conceito

Um Badge representa uma pequena informação visual associada a um componente da interface.

Exemplo:

```text
Canal 08

⚠
```

ou

```text
Canal 05

AI
```

ou

```text
Monitor 2

!
```

---

# Tipos de Badge

## Badge de Recomendação

Indica que existe uma recomendação da IA.

Exemplo:

```text
AI
```

---

## Badge de Alerta

Utilizado para situações importantes.

Exemplo:

```text
⚠
```

---

## Badge Crítico

Utilizado para eventos que exigem atenção imediata.

Exemplo:

```text
🔴
```

---

## Badge Informativo

Indica uma informação sem urgência.

Exemplo:

```text
ℹ
```

---

## Badge de Confirmação

Utilizado após uma ação concluída.

Exemplo:

```text
✓
```

---

# Informações Representadas

Os badges poderão indicar:

- recomendação disponível;
- clipping;
- feedback;
- canal sem sinal;
- bateria baixa;
- problema resolvido;
- recomendação aceita;
- recomendação ignorada;
- alerta pendente.

---

# Posicionamento

Os badges poderão aparecer:

- no canto superior do canal;
- ao lado do nome do participante;
- sobre um fader;
- junto ao medidor;
- em painéis do Dashboard;
- na Timeline.

Exemplo:

```text
┌──────────────┐

Canal 08     ⚠

──────────────

Fader
```

---

# Cores

Cada badge poderá utilizar uma cor específica.

| Cor | Significado |
|------|-------------|
| Vermelho | Situação crítica |
| Laranja | Atenção |
| Azul | Recomendação da IA |
| Verde | Situação resolvida |
| Cinza | Informação |

As cores seguem o padrão definido pelo Visual Priority.

---

# Atualização

Os badges são atualizados continuamente.

Exemplo:

```text
Recomendação criada

↓

Badge AI

↓

Operador aceitou

↓

Badge ✓

↓

Remover
```

---

# Agrupamento

Quando vários eventos estiverem associados ao mesmo elemento, os badges poderão ser agrupados.

Exemplo:

```text
Canal 08

⚠ + AI
```

Ou:

```text
Canal 08

3 Alertas
```

Essa estratégia evita excesso de indicadores.

---

# Persistência

Alguns badges desaparecem automaticamente.

Exemplo:

```text
Confirmação

↓

2 segundos

↓

Remover
```

Outros permanecem enquanto a condição existir.

Exemplo:

```text
Canal sem sinal

↓

Badge permanece

↓

Até retorno do áudio
```

---

# Integração com o Highlight Manager

O Highlight Manager cria e remove badges conforme o ciclo de vida das recomendações.

---

# Integração com o Focus Manager

Quando um elemento recebe foco principal, seu badge poderá ganhar maior destaque visual.

Exemplo:

```text
Badge

↓

Aumentar tamanho

↓

Pequena pulsação
```

---

# Integração com o Animation System

Os badges poderão utilizar animações discretas.

Exemplos:

- fade-in;
- fade-out;
- pulsação suave;
- brilho.

---

# Integração com o Channel Overlay

Ao clicar sobre um badge, o operador poderá abrir o Overlay correspondente.

Exemplo:

```text
Badge

↓

Overlay

↓

Explicação completa
```

---

# Integração com o Dashboard

O Dashboard exibirá badges resumidos nos principais painéis.

Exemplo:

```text
⚠

Monitor 2

Feedback
```

---

# Integração com o Mobile

Na versão mobile, os badges serão ainda mais importantes devido ao espaço reduzido.

Eles indicarão rapidamente quais elementos exigem atenção.

---

# Acessibilidade

Os badges deverão considerar:

- contraste elevado;
- tamanho mínimo para toque;
- diferenciação por forma além da cor;
- compatibilidade com leitores de tela;
- suporte aos modos claro e escuro.

---

# Desempenho

Os Notification Badges deverão ser extremamente leves.

Sua atualização deverá ocorrer em tempo real sem impactar o desempenho da interface.

---

# Benefícios

O Notification Badges proporciona:

- comunicação rápida;
- redução da poluição visual;
- identificação imediata de situações importantes;
- integração natural com a IA;
- menor tempo de resposta do operador;
- melhor organização da interface.

---

# Separação de Responsabilidades

O Notification Badges não:

- gera recomendações;
- cria overlays;
- controla animações;
- define prioridades;
- altera parâmetros da mesa.

Sua responsabilidade é apresentar pequenos indicadores visuais que representam o estado atual das recomendações e alertas da Inteligência Artificial.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- badges personalizados por operador;
- indicadores numéricos de múltiplas ocorrências;
- temas visuais configuráveis;
- agrupamento inteligente por categoria;
- integração com notificações push;
- sincronização entre múltiplos dispositivos;
- indicadores específicos para diferentes tipos de evento.

---

# Relação com Outros Componentes

O Notification Badges trabalha diretamente com:

- Highlight Engine;
- Highlight Manager;
- Highlight Rules;
- Channel Overlay;
- Animation System;
- Focus Manager;
- Visual Priority;
- Recommendation Engine;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA.

Ele representa a camada de comunicação rápida da Inteligência Artificial do Audio Copilot, utilizando pequenos indicadores visuais para informar o operador sobre recomendações, alertas e estados importantes sem comprometer a organização e a fluidez da interface.

---

# Situação da Sprint

**Status:** ✅ Concluída