# Sprint E03 – Silence Detector

## Objetivo

Definir o componente responsável por detectar ausência de sinal (silêncio) nos canais monitorados pelo Audio Copilot.

O Silence Detector permite identificar automaticamente situações em que um canal deixa de transmitir áudio quando deveria estar ativo, auxiliando o operador na identificação de falhas de equipamentos, conexões ou operação.

Este componente também fornece informações importantes para a Inteligência Artificial durante o acompanhamento do evento.

---

# Visão Geral

Durante um culto ou ensaio é comum ocorrerem situações em que um microfone ou instrumento permanece sem sinal por motivos como:

- cabo desconectado;
- bateria descarregada;
- instrumento desligado;
- músico ainda não iniciou a execução;
- microfone mutado;
- ganho inadequado;
- problema de conexão.

O Silence Detector monitora continuamente todos os canais ativos para identificar essas situações.

Seu papel é apenas detectar a ausência de sinal.

Ele nunca modifica automaticamente qualquer configuração da mesa de som.

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
Audio Levels
        │
        ▼
Silence Detector
        │
        ├────────► State Manager
        ├────────► Console de Operação
        ├────────► Painel da IA
        └────────► Histórico
```

O Silence Detector utiliza os níveis processados pelo módulo Audio Levels para determinar a presença ou ausência de sinal.

---

# Responsabilidades

O Silence Detector será responsável por:

- monitorar continuamente os canais ativos;
- detectar ausência prolongada de sinal;
- registrar o início e o término do silêncio;
- publicar eventos para o Event Bus;
- disponibilizar informações para a IA;
- atualizar o estado do canal.

---

# O que é considerado silêncio

Silêncio não significa necessariamente que existe um problema.

Por isso, o componente deverá considerar o contexto de operação.

Exemplos:

## Situação Normal

Um microfone sem uso durante a pregação.

Neste caso:

- não existe alerta;
- apenas ausência de sinal.

---

## Situação Esperada

Um canal reservado para o playback que ainda não iniciou.

Também não deve gerar alerta.

---

## Situação Anormal

O vocalista iniciou a música, porém o canal permanece sem áudio.

Neste caso, o sistema poderá indicar:

"Possível ausência de sinal."

---

## Situação Crítica

Durante o teste de preparação do evento, o operador solicita ao participante que fale ou toque, porém o canal continua completamente silencioso.

Nesse caso, o sistema poderá gerar um alerta de maior prioridade.

---

# Funcionamento

O componente executará continuamente o seguinte fluxo:

```text
Novo nível recebido

↓

Existe sinal?

↓

Sim

↓

Canal ativo

↓

Registrar presença de sinal

──────────────

Não

↓

Iniciar temporizador

↓

Tempo excedido?

↓

Sim

↓

Registrar silêncio

↓

Publicar evento
```

Essa estratégia evita falsos alertas causados por pequenas pausas naturais da fala ou da música.

---

# Tempo de Tolerância

O Silence Detector deverá utilizar um período de tolerância antes de considerar que um canal está realmente sem sinal.

Esse intervalo evita notificações desnecessárias durante pausas naturais.

O tempo será configurável durante a implementação.

---

# Integração com a Preparação do Evento

Durante a Sprint D07 (Preparação do Evento), este componente terá papel fundamental.

Exemplo:

```text
Mic Vermelho

↓

Participante inicia teste

↓

Áudio detectado

↓

Teste aprovado automaticamente
```

Caso nenhum sinal seja detectado dentro do tempo esperado, o sistema poderá informar:

```text
Mic Vermelho

Sem sinal detectado.

Verifique:

• Cabo
• Microfone
• Ganho
• Canal
```

---

# Integração com o Console

Durante a operação, o Console poderá apresentar diferentes estados.

Exemplos:

- sinal presente;
- ausência temporária de sinal;
- silêncio prolongado;
- aguardando utilização.

Essas informações ajudam o operador a compreender rapidamente a situação de cada canal.

---

# Integração com a Inteligência Artificial

O Silence Detector fornecerá informações importantes para a IA.

Exemplo:

```text
Violão Martin

↓

Canal ativo

↓

Nenhum sinal

↓

30 segundos

↓

IA identifica possível problema

↓

Sugestão:

"Solicitar ao músico verificar o cabo do violão."
```

Outro exemplo:

```text
Microfone Verde

↓

Sem sinal durante a oração

↓

IA reconhece que é uma situação normal

↓

Nenhuma ação necessária.
```

A IA sempre analisará o contexto antes de gerar recomendações.

---

# Integração com o Histórico

Os eventos de ausência de sinal poderão ser registrados para:

- auditoria;
- análise técnica;
- estatísticas do evento;
- identificação de falhas recorrentes.

---

# Eventos Produzidos

Sempre que ocorrer uma alteração relevante, poderão ser publicados eventos como:

- ChannelSignalDetected
- ChannelSignalLost
- SilenceStarted
- SilenceEnded
- SilenceTimeout

Esses eventos serão distribuídos através do Event Bus.

---

# Benefícios

A utilização do Silence Detector oferece diversas vantagens:

- identifica rapidamente canais sem funcionamento;
- reduz tempo de diagnóstico durante o evento;
- auxilia nos testes de preparação;
- melhora a confiabilidade da operação;
- fornece informações importantes para a IA;
- contribui para relatórios técnicos.

---

# Separação de Responsabilidades

O Silence Detector possui responsabilidade única.

Ele não:

- calcula níveis de áudio;
- detecta clipping;
- calcula Peak;
- altera parâmetros da mesa;
- envia comandos para a Ui24R.

Sua função é exclusivamente detectar e monitorar a ausência de sinal.

---

# Evoluções Futuras

Nas próximas versões, o Silence Detector poderá incorporar funcionalidades como:

- identificação automática do tipo de falha (cabo, microfone, instrumento ou configuração);
- diferenciação entre pausas naturais e falhas técnicas utilizando Inteligência Artificial;
- correlação com a programação do evento para evitar alertas desnecessários;
- aprendizado do comportamento de cada participante ao longo dos eventos;
- geração de indicadores de confiabilidade por equipamento.

---

# Situação da Sprint

**Status:** ✅ Concluída