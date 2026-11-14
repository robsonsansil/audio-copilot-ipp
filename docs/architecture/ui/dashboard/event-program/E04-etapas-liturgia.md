# Sprint E04 – Etapas da Liturgia

## Objetivo

Definir o modelo de representação das etapas que compõem a programação de um evento dentro do Audio Copilot.

Cada etapa representa um momento específico do culto, ensaio ou evento, possuindo características próprias, participantes esperados, recursos utilizados e comportamentos operacionais previstos.

Ao estruturar o evento em etapas, o Audio Copilot passa a compreender o contexto da operação, permitindo que a Inteligência Artificial ofereça recomendações muito mais precisas.

---

# Visão Geral

Um evento é composto por uma sequência organizada de etapas.

Cada etapa possui um propósito específico e influencia diretamente a forma como a mesa de som será utilizada.

Por exemplo:

```text
Culto Domingo Manhã

Recepção

↓

Abertura

↓

Louvor

↓

Avisos

↓

Oferta

↓

Pregação

↓

Ceia

↓

Encerramento
```

Cada etapa poderá possuir configurações próprias e comportamento esperado.

---

# Filosofia

As etapas representam o contexto do evento.

Elas não definem configurações técnicas da mesa.

A configuração dos canais continua sendo responsabilidade da Configuração do Evento (Sprint D06).

As etapas apenas informam quais recursos deverão estar sendo utilizados naquele momento.

---

# Estrutura de uma Etapa

Cada etapa poderá conter informações como:

- nome;
- descrição;
- ordem de execução;
- duração prevista;
- participantes esperados;
- instrumentos previstos;
- microfones previstos;
- observações operacionais.

Exemplo:

```text
Etapa

Louvor

Duração prevista

25 minutos

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

---

# Estado da Etapa

Cada etapa poderá assumir um dos seguintes estados.

## Aguardando

A etapa ainda não iniciou.

```text
○ Louvor
```

---

## Em Execução

Representa a etapa atualmente em andamento.

```text
► Louvor
```

Somente uma etapa poderá permanecer ativa simultaneamente.

---

## Concluída

A etapa já foi finalizada.

```text
✓ Louvor
```

---

## Cancelada

Caso uma etapa não seja executada durante o evento.

Exemplo:

```text
✕ Oferta
```

Esse estado será registrado no Histórico do Evento.

---

# Tipos de Etapas

O Audio Copilot não impõe uma liturgia fixa.

Cada igreja poderá criar suas próprias etapas.

Exemplos comuns:

- Recepção
- Oração Inicial
- Louvor
- Leitura Bíblica
- Avisos
- Oferta
- Testemunho
- Batismo
- Santa Ceia
- Pregação
- Apelo
- Encerramento

Também poderão existir etapas específicas para:

- Conferências;
- Congressos;
- Casamentos;
- Ensaios;
- Eventos especiais.

---

# Participantes da Etapa

Cada etapa poderá possuir uma lista de participantes previstos.

Exemplo:

```text
Pregação

Participantes

• Pastor

Microfones

• Púlpito
• Sem fio
```

Outro exemplo:

```text
Louvor

Participantes

• Alessandra
• Letícia
• Robson
```

Essas informações serão utilizadas pela Inteligência Artificial durante a operação.

---

# Instrumentos da Etapa

Cada etapa poderá definir quais instrumentos deverão estar ativos.

Exemplo:

```text
Louvor

Instrumentos

• Violão Martin
• Baixo
• Cajón
• Playback
```

Durante a pregação:

```text
Instrumentos

Nenhum
```

Essa informação auxilia a IA na identificação de comportamentos inesperados.

---

# Microfones da Etapa

Também poderão ser definidos os microfones previstos para utilização.

Exemplo:

```text
Louvor

Mic Vermelho

Mic Azul

Mic Verde
```

Durante os avisos:

```text
Púlpito

Sem fio
```

---

# Observações Operacionais

Cada etapa poderá conter instruções para o operador.

Exemplos:

- iniciar gravação;
- utilizar playback;
- reduzir retorno do palco;
- pastor utilizará microfone de lapela;
- iniciar transmissão.

Essas observações funcionam como lembretes durante a operação.

---

# Integração com a Inteligência Artificial

A etapa atual fornece contexto para as análises da IA.

Exemplo:

```text
Etapa

Pregação
```

A IA passa a considerar como comportamento esperado:

- atividade no microfone do Pastor;
- atividade no púlpito;
- instrumentos silenciosos.

Caso o canal do Baixo apresente atividade contínua, a IA poderá informar:

> Foi detectado sinal no canal do Baixo durante a pregação. Verifique se o instrumento permaneceu conectado ou se há alguma fonte de ruído.

Outro exemplo:

```text
Etapa

Louvor
```

Nesse momento, a atividade dos instrumentos passa a ser considerada normal.

---

# Integração com o Console

O Console poderá utilizar a etapa atual para destacar automaticamente os canais mais relevantes.

Exemplo:

Durante o Louvor:

- vocais em destaque;
- instrumentos em destaque.

Durante a Pregação:

- Pastor em destaque;
- púlpito em destaque.

Esse comportamento reduz distrações durante a operação.

---

# Integração com o Dashboard

O Dashboard exibirá a etapa atual juntamente com o progresso do evento.

Exemplo:

```text
Culto Domingo Manhã

Etapa Atual

Pregação

Próxima

Santa Ceia
```

---

# Integração com o Mobile

O aplicativo Mobile apresentará uma versão resumida da etapa.

Exemplo:

```text
Agora

Pregação

Próximo

Encerramento
```

---

# Benefícios

A utilização das Etapas da Liturgia proporciona diversas vantagens:

- organização clara da programação;
- melhor compreensão do contexto operacional;
- redução da carga cognitiva do operador;
- integração entre liturgia e operação técnica;
- maior precisão nas recomendações da IA;
- adaptação do sistema ao andamento do evento.

---

# Separação de Responsabilidades

As Etapas da Liturgia possuem responsabilidade única.

Elas não:

- alteram configurações da mesa;
- movimentam faders;
- enviam comandos para a Ui24R;
- processam áudio;
- executam decisões da IA.

Sua função é representar o contexto operacional do evento.

---

# Evoluções Futuras

Nas próximas versões, as etapas poderão incorporar funcionalidades como:

- duração dinâmica baseada no andamento do culto;
- gatilhos automáticos para início de gravação e transmissão;
- observações compartilhadas entre operadores;
- associação de snapshots recomendados para cada etapa;
- integração com softwares de projeção e apresentação;
- indicadores de atraso em relação ao cronograma;
- recomendações automáticas de transição entre etapas utilizando Inteligência Artificial.

---

# Relação com Outros Componentes

As Etapas da Liturgia trabalham em conjunto com:

- Painel da Liturgia;
- Timeline do Evento;
- Participantes;
- Músicas;
- Progresso do Evento;
- Painel da IA;
- Dashboard Operacional.

Elas representam o contexto operacional que será utilizado por toda a aplicação durante o evento.

---

# Situação da Sprint

**Status:** ✅ Concluída