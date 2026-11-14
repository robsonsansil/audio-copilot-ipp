# Sprint E04 – Painel da Liturgia

## Objetivo

Definir a interface responsável por acompanhar a programação do evento em tempo real, permitindo que o operador e a Inteligência Artificial saibam exatamente em qual etapa da liturgia o evento se encontra.

O Painel da Liturgia deixa de ser apenas uma lista de músicas ou uma ordem de culto. Ele passa a representar o contexto operacional do evento, permitindo que o Audio Copilot antecipe comportamentos esperados, identifique anomalias e ofereça recomendações mais precisas.

---

# Visão Geral

Durante um culto ou ensaio, a utilização da mesa de som muda constantemente.

Cada etapa possui participantes, instrumentos, microfones e necessidades específicas.

O Painel da Liturgia informa ao sistema qual é a etapa atual do evento, permitindo que toda a aplicação adapte seu comportamento automaticamente.

Exemplo:

```text
Culto Domingo Manhã

► Louvor

Música 3 de 5

Participantes ativos

• Alessandra
• Letícia
• Robson

Instrumentos

• Violão Martin
• Baixo
• Cajón

Próxima etapa

Avisos
```

Com esse contexto, toda a aplicação passa a compreender o momento atual da operação.

---

# Filosofia

O Painel da Liturgia não controla a mesa de som.

Ele controla o contexto do evento.

Enquanto o Console de Operação informa "como" os canais estão configurados, o Painel da Liturgia informa "por que" eles estão sendo utilizados naquele momento.

Essa separação torna o sistema mais inteligente e facilita futuras automações.

---

# Arquitetura

Fluxo simplificado:

```text
Programação Técnica

↓

Configuração do Evento

↓

Painel da Liturgia

↓

Estado Atual do Evento

↓

Painel da IA

↓

Console

↓

Dashboard

↓

Mobile
```

O Painel da Liturgia torna-se a referência oficial do andamento do evento.

---

# Responsabilidades

O Painel da Liturgia será responsável por:

- apresentar a programação do evento;
- indicar a etapa atual;
- exibir a próxima etapa;
- acompanhar o progresso do culto;
- informar participantes ativos;
- informar instrumentos ativos;
- fornecer contexto para a IA.

---

# Estrutura da Tela

A interface será dividida em áreas bem definidas.

---

## Cabeçalho

Apresenta as principais informações do evento.

Exemplo:

- Culto Domingo Manhã
- Domingo – 09:00
- Operador: Robson
- Evento em andamento

---

## Linha do Tempo

Apresenta todas as etapas do evento em ordem cronológica.

Exemplo:

```text
✓ Recepção

✓ Abertura

► Louvor

○ Avisos

○ Oferta

○ Pregação

○ Ceia

○ Encerramento
```

A etapa atual permanece destacada.

As etapas concluídas permanecem marcadas.

As futuras permanecem aguardando execução.

---

## Etapa Atual

Esta é a principal área da tela.

São apresentadas informações como:

- nome da etapa;
- descrição;
- tempo estimado;
- progresso da etapa.

Exemplo:

```text
Louvor

Música 3 de 5

Tempo estimado:

18 minutos
```

---

## Participantes Ativos

Exibe apenas os participantes esperados para a etapa atual.

Exemplo:

- Alessandra
- Letícia
- Robson
- Marçal

Essas informações são utilizadas também pela IA.

---

## Instrumentos Ativos

Mostra apenas os instrumentos previstos para utilização naquela etapa.

Exemplo:

- Violão Martin
- Baixo
- Cajón
- Playback

Instrumentos não utilizados permanecem ocultos.

---

## Microfones Ativos

Lista os microfones previstos para a etapa.

Exemplo:

- Mic Vermelho
- Mic Azul
- Mic Verde

Caso algum microfone apresente comportamento inesperado, a IA poderá gerar recomendações.

---

## Próxima Etapa

O operador consegue visualizar o que acontecerá em seguida.

Exemplo:

```text
Próxima etapa

Avisos

Participantes

• Pastor

Microfones

• Púlpito
• Sem fio
```

Essa informação auxilia o operador a antecipar ajustes necessários.

---

## Observações

Cada etapa poderá conter instruções específicas.

Exemplos:

- utilizar playback;
- iniciar gravação;
- pastor utilizará microfone de lapela;
- transmissão inicia nesta etapa.

Essas observações funcionam como lembretes operacionais.

---

# Integração com a Inteligência Artificial

O Painel da Liturgia fornece contexto operacional para a IA.

Exemplo:

```text
Etapa Atual

Pregação
```

A IA passa a esperar atividade apenas em canais como:

- Pastor;
- Púlpito;
- Microfone sem fio.

Caso o Baixo apresente sinal durante esse período, a IA poderá informar:

> Detectado áudio no canal do Baixo durante a pregação. Verifique se o instrumento permaneceu conectado ou se há ruído no canal.

Outro exemplo:

```text
Etapa

Louvor
```

Nesse momento, a IA espera atividade em:

- vocais;
- instrumentos;
- playback.

Se um vocal permanecer sem sinal por muito tempo, a IA poderá sugerir verificar o microfone correspondente.

---

# Integração com o Console

O Console poderá utilizar o contexto da liturgia para destacar apenas os canais mais relevantes da etapa atual.

Exemplo:

Durante a pregação, os canais do Pastor e do Púlpito podem receber maior destaque visual, enquanto os instrumentos permanecem em segundo plano.

Essa funcionalidade reduz a carga cognitiva do operador.

---

# Integração com o Dashboard

O Dashboard apresentará um resumo da liturgia.

Exemplo:

```text
Culto Domingo Manhã

Etapa Atual

Louvor

Música 3 de 5

Próxima

Avisos
```

Essa informação estará sempre visível na tela principal.

---

# Integração com o Mobile

O aplicativo Mobile apresentará uma versão simplificada.

Exemplo:

```text
Agora

Louvor

Próximo

Avisos

Tempo restante

6 minutos
```

Isso permite acompanhar o andamento do evento mesmo fora da mesa de som.

---

# Benefícios

A utilização do Painel da Liturgia proporciona diversas vantagens:

- fornece contexto operacional para toda a aplicação;
- reduz a necessidade de memorização pelo operador;
- melhora a precisão das recomendações da IA;
- facilita a antecipação das próximas etapas;
- integra programação técnica e operação em tempo real;
- melhora a experiência do operador.

---

# Separação de Responsabilidades

O Painel da Liturgia possui responsabilidade única.

Ele não:

- controla faders;
- altera parâmetros da mesa;
- executa comandos na Ui24R;
- realiza análises de áudio;
- toma decisões automaticamente.

Sua função é representar o estado atual da programação do evento e fornecer contexto para os demais módulos.

---

# Evoluções Futuras

Nas próximas versões, o Painel da Liturgia poderá incorporar funcionalidades como:

- avanço automático de etapas com confirmação do operador;
- sincronização com softwares de apresentação de letras e projeção;
- cronômetro por etapa;
- acompanhamento de tempo previsto versus realizado;
- integração com escalas de voluntários;
- marcação de observações durante o culto;
- adaptação dinâmica da programação durante o evento;
- utilização de Inteligência Artificial para sugerir transições entre etapas.

---

# Próximos Componentes

Esta Sprint será complementada pelos seguintes documentos:

- E04-timeline-evento.md
- E04-etapas-liturgia.md
- E04-musicas.md
- E04-participantes.md
- E04-transicoes.md
- E04-progresso-evento.md
- E04-integracao-ia.md

Cada documento detalhará um aspecto específico do Painel da Liturgia, mantendo a arquitetura modular e consistente.

---

# Situação da Sprint

**Status:** ✅ Concluída