# Sprint E04 – Integração com a Inteligência Artificial

## Objetivo

Definir como o Painel da Liturgia fornece contexto operacional para a Inteligência Artificial do Audio Copilot.

Enquanto os módulos de Telemetria informam **o que está acontecendo** na mesa de som, o Painel da Liturgia informa **o que deveria estar acontecendo** naquele momento do evento.

Essa combinação permite que a IA realize análises muito mais precisas, reduzindo falsos alertas e oferecendo recomendações contextualizadas ao operador.

---

# Visão Geral

A Inteligência Artificial do Audio Copilot não toma decisões apenas com base nos níveis de áudio.

Ela considera simultaneamente:

- estado atual do evento;
- etapa da liturgia;
- música em execução;
- participantes ativos;
- instrumentos previstos;
- microfones previstos;
- comportamento esperado de cada canal.

Com essas informações, a IA consegue compreender o contexto completo da operação.

---

# Filosofia

A IA não substitui o operador.

Seu papel é atuar como um copiloto, oferecendo recomendações baseadas no contexto atual do evento.

Todas as sugestões permanecem sob controle do operador, que poderá aceitá-las, ignorá-las ou realizar ajustes diferentes dos sugeridos.

---

# Arquitetura

Fluxo simplificado:

```text
Painel da Liturgia

↓

Timeline

↓

Etapa Atual

↓

Música Atual

↓

Participantes

↓

Contexto Operacional

↓

Inteligência Artificial

↓

Sugestões

↓

Operador
```

A IA passa a analisar o áudio considerando o contexto operacional definido pela liturgia.

---

# Fontes de Contexto

A Inteligência Artificial poderá utilizar informações provenientes de diversos componentes.

Entre elas:

- etapa atual;
- música atual;
- participantes ativos;
- instrumentos previstos;
- microfones previstos;
- duração da etapa;
- progresso do evento;
- observações operacionais.

Essas informações são combinadas com os dados da Telemetria para formar uma visão completa da operação.

---

# Contexto Operacional

O contexto operacional representa o estado atual do evento.

Exemplo:

```text
Evento

Culto Domingo Manhã

Etapa

Louvor

Música

Sola Scriptura

Participantes

• Alessandra
• Letícia
• Robson

Instrumentos

• Violão Martin
• Baixo
• Cajón

Microfones

• Vermelho
• Azul
• Verde
```

Nesse cenário, a IA espera atividade nesses recursos.

---

# Análise Contextual

Ao invés de analisar apenas níveis de áudio, a IA passa a interpretar situações.

Exemplo:

```text
Etapa

Pregação
```

Durante essa etapa, espera-se atividade em:

- Púlpito;
- Pastor;
- Microfone sem fio.

Caso o canal do Baixo permaneça transmitindo sinal continuamente, a IA poderá sugerir:

> Foi detectado sinal no canal do Baixo durante a pregação. Verifique se o instrumento permaneceu conectado ou se existe alguma fonte de ruído.

---

Outro exemplo:

```text
Etapa

Louvor

Música

Sola Scriptura
```

Caso o Playback esteja previsto e permaneça completamente silencioso, a IA poderá informar:

> O canal de Playback não apresentou sinal. Confirme se a reprodução foi iniciada.

---

# Redução de Falsos Alertas

O conhecimento da liturgia reduz significativamente a quantidade de alertas desnecessários.

Exemplo:

Durante a oração inicial.

```text
Instrumentos

Sem sinal
```

Sem contexto:

```text
Possível falha no Violão.
```

Com contexto:

```text
Situação esperada.

Os instrumentos ainda não estão previstos para utilização.
```

A IA entende que a ausência de áudio é normal naquele momento.

---

# Antecipação Operacional

A IA também poderá antecipar recomendações.

Exemplo:

```text
Próxima etapa

Pregação
```

Antes da transição, o sistema poderá sugerir:

> A próxima etapa utilizará o Microfone do Púlpito. Confirme se o canal está pronto para uso.

Outro exemplo:

```text
Próxima etapa

Santa Ceia
```

A IA poderá lembrar:

> Verifique os microfones adicionais previstos para a participação dos presbíteros.

---

# Recomendações Inteligentes

As sugestões da IA poderão considerar simultaneamente:

- contexto da liturgia;
- comportamento histórico;
- telemetria em tempo real;
- configuração do evento;
- padrões aprendidos em eventos anteriores.

Exemplo:

```text
Sugestão

O Pastor normalmente utiliza o microfone de lapela nesta etapa.

Deseja destacar este canal no Console?
```

O operador decide se aceita ou não a sugestão.

---

# Integração com o Console

O Console poderá utilizar as informações da IA para destacar automaticamente canais importantes.

Exemplo:

```text
Etapa

Pregação
```

Canais destacados:

- Púlpito;
- Lapela;
- Sem fio.

Os demais permanecem disponíveis, porém com menor destaque visual.

---

# Integração com o Dashboard

O Dashboard poderá apresentar um resumo das recomendações atuais.

Exemplo:

```text
IA

Nenhuma recomendação.

────────────

IA

Verificar Playback.

────────────

IA

Canal do Baixo permanece ativo durante a Pregação.
```

---

# Integração com o Mobile

O aplicativo Mobile poderá exibir apenas recomendações relevantes.

Exemplo:

```text
IA

Microfone Verde sem sinal.

Verifique a bateria.
```

Essa abordagem evita excesso de informações em dispositivos móveis.

---

# Aprendizado Contínuo

Ao longo do tempo, a IA poderá identificar padrões específicos de cada igreja.

Exemplos:

- ordem típica da liturgia;
- duração média das etapas;
- instrumentos normalmente utilizados;
- canais frequentemente ajustados;
- participantes recorrentes;
- comportamento dos operadores.

Essas informações permitirão recomendações cada vez mais precisas.

---

# Registro das Recomendações

Todas as recomendações poderão ser registradas.

Exemplo:

```text
09:42

Sugestão

Verificar Microfone Verde.

Status

Aceita

────────────

10:18

Sugestão

Reduzir retorno do Monitor.

Status

Ignorada
```

Esses registros poderão ser utilizados em relatórios e no aperfeiçoamento dos modelos de IA.

---

# Benefícios

A integração entre Liturgia e Inteligência Artificial proporciona:

- recomendações contextualizadas;
- redução de falsos alertas;
- melhor compreensão do evento;
- antecipação de necessidades operacionais;
- menor carga cognitiva para o operador;
- aprendizado contínuo baseado no histórico da igreja.

---

# Separação de Responsabilidades

A integração com a IA possui responsabilidade específica.

Ela não:

- altera automaticamente a mesa de som;
- movimenta faders;
- executa snapshots;
- inicia ou encerra etapas da liturgia;
- substitui decisões do operador.

Sua função é fornecer contexto para que a Inteligência Artificial produza recomendações mais relevantes e precisas.

---

# Evoluções Futuras

Nas próximas versões, este componente poderá incorporar funcionalidades como:

- identificação automática da etapa do culto por análise de áudio;
- sugestão automática de transições entre etapas;
- previsão de duração das próximas etapas;
- aprendizado personalizado por igreja e operador;
- recomendações baseadas em estatísticas históricas;
- integração com sistemas de projeção, transmissão e iluminação;
- geração automática de um "assistente de operação" que acompanhe todo o evento em tempo real.

---

# Relação com Outros Componentes

A Integração com a IA trabalha em conjunto com:

- Painel da Liturgia;
- Timeline do Evento;
- Etapas da Liturgia;
- Músicas;
- Participantes;
- Transições;
- Progresso do Evento;
- Telemetry Manager;
- Statistics;
- Dashboard Operacional;
- Console de Operação;
- Painel da IA.

Ela representa a camada responsável por transformar informações operacionais em recomendações inteligentes, mantendo o operador sempre no controle da mesa de som.

---

# Situação da Sprint

**Status:** ✅ Concluída