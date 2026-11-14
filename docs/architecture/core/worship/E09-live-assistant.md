# Sprint E09 – Live Assistant

## Objetivo

Definir o componente responsável por atuar como o copiloto operacional do Audio Copilot durante a execução do culto, fornecendo orientações, recomendações e informações contextuais ao operador de forma discreta, segura e não intrusiva.

O **Live Assistant** representa a interface inteligente entre a Inteligência Artificial e o operador. Ele transforma dados técnicos, eventos e recomendações produzidos pelos demais componentes em informações claras, oportunas e relevantes para apoiar a tomada de decisão.

Enquanto o **Recommendation Engine** gera sugestões e o **Alert Manager** administra notificações, o Live Assistant é responsável por comunicar essas informações ao operador da maneira mais adequada.

---

# Visão Geral

Durante um culto, o operador precisa manter atenção constante na mesa de som.

Ao mesmo tempo, diversas situações podem exigir sua atenção.

Exemplos:

- canal próximo do clipping;
- microfone sem sinal;
- snapshot incorreto;
- mudança de etapa da liturgia;
- recomendação da IA;
- alerta crítico.

O Live Assistant organiza essas informações para que sejam apresentadas no momento certo, sem sobrecarregar o operador.

---

# Filosofia

O Live Assistant foi desenvolvido seguindo cinco princípios.

## Assistência

A IA deve auxiliar, nunca substituir o operador.

---

## Discrição

As mensagens devem ser objetivas e aparecer apenas quando agregarem valor.

---

## Contexto

Toda recomendação deve considerar o momento atual do culto.

---

## Clareza

As informações devem ser facilmente compreendidas em poucos segundos.

---

## Prioridade

O operador deve visualizar primeiro aquilo que realmente importa.

---

# Arquitetura

```text
Recommendation Engine

↓

Decision Engine

↓

Alert Manager

↓

Safe Mode

↓

Live Assistant

├── Mensagens
├── Recomendações
├── Alertas
├── Sugestões
├── Contexto
└── Interface

↓

Operador
```

---

# Responsabilidades

O Live Assistant será responsável por:

- apresentar recomendações;
- exibir alertas;
- fornecer contexto operacional;
- orientar o operador;
- priorizar mensagens;
- reduzir distrações;
- manter comunicação clara durante o culto.

---

# Fluxo Geral

```text
Evento

↓

Análise da IA

↓

Safe Mode

↓

Live Assistant

↓

Operador
```

---

# Tipos de Mensagens

O Live Assistant poderá apresentar:

- recomendações;
- alertas;
- confirmações;
- lembretes;
- informações contextuais;
- notificações operacionais.

---

# Recomendações

Exemplos:

```text
Canal 08

↓

Reduzir Gain

2 dB
```

---

```text
Pastor

↓

Microfone Reserva

Pronto
```

---

```text
Snapshot

Pregação

↓

Pronto para utilização
```

---

# Alertas

O Live Assistant exibirá alertas produzidos pelo Alert Manager.

Exemplo:

```text
Canal 05

↓

Clipping Persistente
```

Ou:

```text
Microfone

Sem sinal
```

---

# Informações Contextuais

Além dos alertas, poderão ser exibidas informações úteis.

Exemplo:

```text
Liturgia

↓

Pregação

↓

12 minutos
```

Ou:

```text
Próxima etapa

↓

Ceia
```

---

# Confirmações

O operador poderá receber confirmações importantes.

Exemplo:

```text
Snapshot carregado
```

Ou:

```text
Configuração salva
```

Essas mensagens devem ser discretas e desaparecer automaticamente.

---

# Priorização

As mensagens serão organizadas conforme sua importância.

```text
Informação

↓

Sugestão

↓

Alerta

↓

Crítico
```

A interface sempre privilegiará a informação mais relevante.

---

# Agrupamento

Mensagens semelhantes poderão ser agrupadas.

Exemplo:

```text
3 canais

↓

Headroom baixo
```

Em vez de três notificações independentes, o sistema poderá apresentar uma única mensagem resumida.

---

# Contextualização

O Live Assistant utilizará informações como:

- etapa da liturgia;
- operador;
- snapshots;
- participantes ativos;
- recomendações anteriores;
- alertas ativos.

Isso evita mensagens inadequadas ao momento do culto.

---

# Comunicação Não Intrusiva

As mensagens deverão respeitar a atenção do operador.

Exemplos:

- desaparecer automaticamente;
- evitar sobreposição;
- não bloquear controles;
- utilizar animações discretas;
- respeitar o Safe Mode.

---

# Histórico das Mensagens

Todas as mensagens poderão ser consultadas posteriormente.

Exemplo:

```text
20:14

↓

Canal 08

↓

Reduzir Gain

↓

Aceita
```

Ou:

```text
20:18

↓

Snapshot

↓

Pregação

↓

Carregado
```

---

# Interação com o Operador

Dependendo da configuração, o operador poderá:

- confirmar recomendações;
- ignorar sugestões;
- marcar mensagens como resolvidas;
- solicitar mais detalhes;
- ocultar notificações temporariamente.

---

# Integração com a IA

O Live Assistant recebe informações de:

- Recommendation Engine;
- Decision Engine;
- Confidence Engine;
- Context Manager;
- Safety Engine.

Esses componentes determinam o conteúdo e o momento adequado para cada mensagem.

---

# Integração com o Alert Manager

Todos os alertas passam pelo Alert Manager antes de serem apresentados.

O Live Assistant apenas define a forma de exibição ao operador.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- mensagens recentes;
- recomendações ativas;
- alertas críticos;
- histórico de notificações;
- sugestões aguardando resposta.

---

# Integração com o Histórico

Todas as interações poderão ser registradas.

Exemplos:

- recomendação apresentada;
- recomendação aceita;
- recomendação ignorada;
- alerta resolvido;
- mensagem descartada.

Esses dados poderão alimentar análises futuras.

---

# Integração com o Worship Report

Ao final do culto, o relatório poderá apresentar:

- recomendações emitidas;
- recomendações aceitas;
- alertas apresentados;
- tempo médio de resposta;
- principais orientações fornecidas pela IA.

---

# Benefícios

O Live Assistant proporciona:

- comunicação clara entre IA e operador;
- redução da carga cognitiva;
- suporte contextual durante o culto;
- melhor aproveitamento das recomendações da IA;
- menor risco operacional;
- experiência mais natural na utilização do Audio Copilot.

---

# Separação de Responsabilidades

O Live Assistant não:

- monitora diretamente a mesa;
- detecta clipping;
- gera recomendações;
- toma decisões;
- altera configurações da mesa.

Sua responsabilidade é transformar as informações produzidas pelos demais componentes em uma comunicação clara, contextualizada e útil para o operador durante toda a execução do culto.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- comandos por voz;
- síntese de voz para operadores com headset;
- interface adaptativa conforme o perfil do operador;
- recomendações multimodais (texto, ícones e áudio);
- tradução automática de mensagens;
- integração com dispositivos móveis;
- assistente conversacional em tempo real;
- personalização da interface conforme o estilo de operação.

---

# Relação com Outros Componentes

O Live Assistant trabalha diretamente com:

- Modo Culto;
- Worship Manager;
- Live Session;
- Live Monitor;
- Alert Manager;
- Safe Mode;
- Event Tracker;
- Recommendation Engine;
- Decision Engine;
- Confidence Engine;
- Context Manager;
- History Manager;
- Worship Report;
- Dashboard Operacional;
- Console Operacional.

Ele representa a interface inteligente entre a Inteligência Artificial e o operador, transformando eventos, alertas e recomendações em orientações claras, discretas e contextualizadas, permitindo que o Audio Copilot atue como um verdadeiro copiloto operacional durante toda a execução do culto.

---

# Situação da Sprint

**Status:** ✅ Concluída