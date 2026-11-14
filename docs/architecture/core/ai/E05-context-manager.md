# Sprint E05 – Context Manager

## Objetivo

Definir o componente responsável por construir e manter o contexto operacional da Inteligência Artificial durante todo o evento.

O Context Manager é o primeiro módulo da IA Operacional. Sua responsabilidade é reunir informações provenientes de toda a aplicação e transformá-las em um único contexto consistente que será utilizado pelos demais motores de inteligência.

Ele responde, continuamente, à seguinte pergunta:

> **"O que está acontecendo neste exato momento?"**

---

# Visão Geral

A Inteligência Artificial não deve tomar decisões analisando apenas níveis de áudio.

Antes de qualquer recomendação, ela precisa compreender o cenário completo da operação.

O Context Manager é responsável por reunir todas essas informações e disponibilizá-las em um único objeto de contexto.

---

# Filosofia

Todo processamento inteligente depende de contexto.

Uma leitura de áudio isolada possui pouco significado.

Por exemplo:

```text
Canal 12

-6 dB
```

Esse valor pode representar uma situação perfeitamente normal ou um problema crítico.

Tudo depende do contexto.

O Context Manager existe justamente para fornecer esse contexto.

---

# Responsabilidades

O Context Manager será responsável por:

- identificar o evento atual;
- identificar a etapa da liturgia;
- identificar a música em execução;
- identificar os participantes ativos;
- identificar os canais ativos;
- identificar os instrumentos previstos;
- identificar os microfones previstos;
- acompanhar o progresso do evento;
- disponibilizar essas informações para toda a IA.

---

# Arquitetura

```text
Telemetria

↓

State Manager

↓

Timeline

↓

Liturgia

↓

Participantes

↓

Configuração

↓

Context Manager

↓

Recommendation Engine

↓

Decision Engine

↓

Learning Engine
```

Todos os motores de IA dependem do Context Manager.

---

# Fontes de Informação

O Context Manager consolida informações provenientes de diversos módulos.

Entre eles:

- Telemetry Manager;
- State Manager;
- Timeline do Evento;
- Painel da Liturgia;
- Músicas;
- Participantes;
- Configuração do Evento;
- Statistics;
- Histórico;
- Preferências do Operador.

---

# Estrutura do Contexto

Exemplo simplificado:

```text
Evento

Culto Domingo Manhã

Etapa

Louvor

Música

Sola Scriptura

Participantes

Alessandra

Letícia

Robson

Instrumentos

Violão

Baixo

Cajón

Microfones

Vermelho

Azul

Verde

Operador

Robson

Modo

Culto
```

Esse objeto representa o estado atual da operação.

---

# Contexto Temporal

Além do estado atual, o Context Manager acompanha o tempo.

Exemplo:

```text
Evento iniciado

09:00

Horário atual

09:48

Tempo decorrido

48 minutos

Etapa

Pregação

Tempo da etapa

12 minutos
```

Essas informações podem ser utilizadas por diversos motores da IA.

---

# Contexto Operacional

Também fazem parte do contexto informações sobre a operação.

Exemplo:

```text
Modo

Culto

Mesa

Soundcraft Ui24R

Operador

Robson

IA

Assistência

Controle Manual

Ativado
```

---

# Contexto da Liturgia

A IA também precisa compreender a programação.

Exemplo:

```text
Etapa

Louvor

↓

Próxima

Avisos
```

Ou:

```text
Etapa

Pregação

↓

Próxima

Santa Ceia
```

Esse conhecimento altera completamente a interpretação dos sinais de áudio.

---

# Contexto Musical

Durante o Louvor, a IA também considera a música atual.

Exemplo:

```text
Música

Sola Scriptura

Instrumentos

Violão

Baixo

Cajón
```

Caso um Piano apresente atividade, esse comportamento poderá ser considerado inesperado.

---

# Contexto Humano

O Context Manager identifica quem está participando do evento.

Exemplo:

```text
Participantes Ativos

Pastor

Robson

Alessandra

Letícia
```

A IA passa a compreender quais recursos cada pessoa está utilizando.

---

# Contexto Técnico

Também são incorporadas informações da infraestrutura.

Exemplo:

```text
Ui24R

Conectada

Rede

OK

PA

OK

Stream

Ativo
```

Essas informações evitam recomendações incoerentes.

---

# Atualização Contínua

O Context Manager permanece ativo durante todo o evento.

Sempre que ocorrer qualquer alteração, o contexto será reconstruído.

Exemplos:

- mudança de etapa;
- nova música;
- participante ativo;
- alteração do operador;
- mudança do modo de operação;
- nova configuração do evento.

---

# Context Snapshot

O contexto poderá ser representado internamente como um snapshot.

Exemplo:

```text
Context Snapshot

Evento

Culto Domingo Manhã

Etapa

Pregação

Participantes

1

Instrumentos

0

Modo

Culto

Progresso

72%
```

Os demais motores sempre trabalham sobre um snapshot consistente.

---

# Consistência

Todos os motores da IA utilizam exatamente o mesmo contexto.

Isso garante que:

- Recommendation Engine;
- Decision Engine;
- Learning Engine;
- Confidence Engine;
- Rule Engine;

trabalhem sempre com as mesmas informações.

---

# Integração com o Recommendation Engine

O Recommendation Engine utiliza o contexto para gerar sugestões.

Exemplo:

```text
Etapa

Pregação

↓

Canal do Baixo ativo

↓

Sugestão

Verificar canal.
```

Sem o Context Manager, essa recomendação não seria possível.

---

# Integração com o Decision Engine

O Decision Engine consulta o contexto antes de exibir qualquer recomendação.

Exemplo:

```text
Modo

Ensaio
```

Durante um ensaio, determinados comportamentos podem ser considerados normais.

Já durante um culto, a mesma situação pode justificar um alerta.

---

# Integração com o Learning Engine

O Learning Engine utiliza o contexto para aprender padrões.

Exemplo:

```text
Culto Domingo Manhã

↓

Sempre após o Louvor

↓

Operador reduz o retorno do palco.
```

Esse padrão poderá gerar futuras recomendações.

---

# Benefícios

O Context Manager proporciona:

- compreensão completa da operação;
- redução de falsas interpretações;
- padronização do estado utilizado pela IA;
- sincronização entre todos os motores;
- maior precisão nas recomendações;
- base sólida para aprendizado contínuo.

---

# Separação de Responsabilidades

O Context Manager não:

- gera recomendações;
- toma decisões;
- aprende padrões;
- altera configurações;
- envia comandos para a Ui24R.

Sua única responsabilidade é construir e manter o contexto operacional da Inteligência Artificial.

---

# Evoluções Futuras

O componente foi projetado para incorporar novas fontes de contexto, como:

- calendário da igreja;
- tipo de evento;
- perfil do pregador;
- condições ambientais;
- ocupação do templo;
- integração com iluminação;
- integração com projeção;
- integração com transmissão ao vivo;
- reconhecimento automático de voz;
- identificação automática de instrumentos.

---

# Relação com Outros Componentes

O Context Manager trabalha diretamente com:

- Telemetry Manager;
- State Manager;
- Timeline do Evento;
- Etapas da Liturgia;
- Músicas;
- Participantes;
- Configuração do Evento;
- Statistics;
- Recommendation Engine;
- Decision Engine;
- Learning Engine;
- Confidence Engine;
- Rule Engine.

Ele representa a porta de entrada da Inteligência Artificial, consolidando todas as informações da aplicação em um único contexto operacional consistente.

---

# Situação da Sprint

**Status:** ✅ Concluída