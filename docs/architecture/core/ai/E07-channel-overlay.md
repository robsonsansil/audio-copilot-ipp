# Sprint E07 – Channel Overlay

## Objetivo

Definir o componente responsável por exibir sobre cada canal da interface todas as informações visuais produzidas pela Inteligência Artificial.

O **Channel Overlay** é uma camada gráfica posicionada sobre o canal da mesa virtual, permitindo que recomendações, alertas, indicadores e explicações sejam apresentados exatamente onde o operador precisa olhar.

Enquanto o **Highlight Engine** decide o que destacar e o **Highlight Manager** controla os destaques ativos, o **Channel Overlay** é responsável por desenhar essas informações diretamente sobre cada canal.

---

# Visão Geral

Durante um culto, o operador observa dezenas de canais simultaneamente.

Quando a IA identifica uma situação importante, o operador não deve precisar:

- procurar o canal;
- ler mensagens longas;
- abrir janelas adicionais;
- consultar outro painel.

A própria interface deve comunicar visualmente a informação.

É exatamente essa a função do Channel Overlay.

---

# Filosofia

O Channel Overlay foi desenvolvido seguindo cinco princípios.

## Proximidade

A informação deve aparecer exatamente sobre o elemento relacionado.

---

## Simplicidade

Poucos elementos transmitem mais informação do que mensagens longas.

---

## Contextualização

Cada overlay deve representar apenas informações relevantes ao contexto atual.

---

## Discrição

O overlay auxilia o operador sem esconder controles da mesa.

---

## Consistência

Todos os canais seguem o mesmo padrão visual.

---

# Arquitetura

```text
Recommendation Engine

↓

Highlight Engine

↓

Highlight Manager

↓

Channel Overlay

↓

Console Operacional
```

---

# Responsabilidades

O Channel Overlay será responsável por:

- desenhar destaques sobre canais;
- exibir recomendações da IA;
- apresentar indicadores visuais;
- mostrar pequenos textos explicativos;
- indicar prioridades;
- atualizar informações em tempo real.

---

# Conceito

O Overlay representa uma camada gráfica adicional.

```text
┌──────────────────────────┐
│ Canal 08                 │
│                          │
│      Overlay da IA       │
│                          │
│        Fader             │
└──────────────────────────┘
```

A camada não substitui a interface da mesa.

Ela apenas adiciona informações.

---

# Informações Exibidas

O Channel Overlay poderá apresentar:

- alertas;
- recomendações;
- nível de prioridade;
- confiança da IA;
- explicações resumidas;
- ícones;
- setas;
- indicadores temporários.

---

# Exemplo

```text
Canal 08

⚠

Reduzir Gain

≈ 2 dB
```

---

# Outro Exemplo

```text
Monitor 2

🔴

Feedback detectado
```

---

# Outro Exemplo

```text
Playback

✓

Situação normal
```

---

# Tipos de Overlay

## Overlay Informativo

Apenas informa uma condição.

Exemplo:

```text
Canal sem sinal.
```

---

## Overlay de Recomendação

Sugere uma ação.

Exemplo:

```text
Reduzir Gain.

≈ 2 dB
```

---

## Overlay de Alerta

Utilizado para problemas importantes.

Exemplo:

```text
Feedback detectado.
```

---

## Overlay de Confirmação

Indica sucesso.

Exemplo:

```text
Recomendação aplicada.
```

---

# Componentes Visuais

Cada overlay poderá conter:

- ícone;
- título;
- descrição;
- cor;
- prioridade;
- seta indicativa;
- pequena animação.

---

# Posicionamento

O overlay será exibido sobre o canal correspondente.

Exemplo:

```text
Canal

↓

Overlay

↓

Fader
```

Assim o operador identifica imediatamente onde atuar.

---

# Prioridade Visual

Quando houver múltiplas informações:

```text
Feedback

↓

Clipping

↓

Sugestão operacional
```

O overlay exibirá apenas a informação de maior prioridade.

As demais permanecerão disponíveis no histórico ou no Painel da IA.

---

# Atualização

Sempre que uma recomendação mudar:

```text
Nova recomendação

↓

Atualizar Overlay

↓

Atualizar Interface
```

A atualização deverá ocorrer sem piscar a tela.

---

# Remoção

Quando a condição deixar de existir:

```text
Problema resolvido

↓

Fade-out

↓

Remover Overlay
```

---

# Interação

O operador poderá interagir com o overlay.

Exemplos:

- clicar para abrir detalhes;
- visualizar explicação da IA;
- aceitar recomendação;
- ignorar sugestão;
- abrir histórico relacionado.

---

# Integração com o Explanation Engine

Ao selecionar um overlay, será possível visualizar a justificativa da IA.

Exemplo:

```text
Reduzir Gain

↓

Motivo

Clipping contínuo
detectado nos últimos
6 segundos.
```

---

# Integração com o Notification Badges

O Overlay poderá utilizar pequenos indicadores.

Exemplo:

```text
AI

Novo
```

```text
⚠

Alta prioridade
```

---

# Integração com o Animation System

As animações serão controladas externamente.

Exemplo:

```text
Overlay criado

↓

Fade-in

↓

Pulsação

↓

Fade-out
```

---

# Integração com o Dashboard

O Dashboard exibirá apenas uma versão resumida do overlay.

Enquanto isso, o Console apresentará todas as informações.

---

# Integração com o Mobile

Na versão mobile o overlay será simplificado.

Exemplo:

```text
Vocal Azul

⚠

Reduzir Gain
```

---

# Acessibilidade

O Channel Overlay foi projetado para permanecer legível em diferentes condições.

O sistema deverá considerar:

- contraste elevado;
- tamanhos mínimos de fonte;
- ícones intuitivos;
- diferenciação por forma além da cor;
- compatibilidade com temas claro e escuro.

---

# Desempenho

Os overlays deverão ser renderizados de forma extremamente leve.

A criação, atualização e remoção não poderá causar travamentos nem reduzir a fluidez da interface.

---

# Benefícios

O Channel Overlay proporciona:

- identificação imediata dos problemas;
- redução do tempo de resposta;
- comunicação visual intuitiva;
- menor necessidade de leitura;
- integração natural entre IA e operador;
- operação mais segura.

---

# Separação de Responsabilidades

O Channel Overlay não:

- detecta problemas;
- gera recomendações;
- define prioridades;
- controla animações;
- altera parâmetros da mesa.

Sua responsabilidade é desenhar visualmente, sobre cada canal, todas as informações produzidas pela camada de Inteligência Artificial.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- overlays configuráveis pelo operador;
- múltiplos níveis de detalhamento;
- suporte a múltiplos monitores;
- visualização em realidade aumentada;
- integração com telas sensíveis ao toque;
- comentários colaborativos entre operadores;
- indicadores específicos para diferentes tipos de evento;
- sobreposição sincronizada com gravações de Replay.

---

# Relação com Outros Componentes

O Channel Overlay trabalha diretamente com:

- Highlight Engine;
- Highlight Manager;
- Highlight Rules;
- Animation System;
- Focus Manager;
- Notification Badges;
- Visual Priority;
- Recommendation Engine;
- Explanation Engine;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA.

Ele representa a camada gráfica da Inteligência Artificial sobre os canais da mesa virtual, tornando cada recomendação imediatamente visível no contexto correto e permitindo que o operador identifique rapidamente onde agir durante a operação.

---

# Situação da Sprint

**Status:** ✅ Concluída