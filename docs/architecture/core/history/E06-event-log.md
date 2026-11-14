# Sprint E06 – Event Log

## Objetivo

Definir o componente responsável por registrar todos os eventos operacionais do Audio Copilot durante a execução de um evento.

Diferentemente do **Change Log**, que registra alterações em parâmetros da mesa de som, o **Event Log** registra acontecimentos relevantes da aplicação.

Seu objetivo é documentar tudo o que ocorreu durante o evento, permitindo reconstruir a sequência completa das operações, facilitar auditorias, gerar relatórios e fornecer contexto para a Inteligência Artificial.

---

# Visão Geral

Durante um culto, inúmeros acontecimentos ocorrem além das alterações da mesa.

Por exemplo:

- início do evento;
- conexão com a Ui24R;
- carregamento de snapshots;
- mudança da etapa da liturgia;
- entrada de um participante;
- troca do operador;
- desconexão de um dispositivo;
- início da transmissão;
- encerramento do evento.

Esses acontecimentos são chamados de **eventos operacionais**.

O Event Log é responsável por registrá-los.

---

# Filosofia

O Event Log foi desenvolvido seguindo cinco princípios.

## Contexto

Nem toda informação importante representa uma alteração técnica.

---

## Cronologia

Todos os eventos devem permanecer organizados em ordem temporal.

---

## Rastreabilidade

Todo evento relevante deve possuir registro.

---

## Organização

Eventos são classificados por categorias.

---

## Memória

O histórico deve permitir reconstruir completamente um evento.

---

# Arquitetura

```text
Dashboard

↓

Console

↓

Liturgia

↓

IA

↓

Sistema

↓

Event Log

↓

History Manager

↓

Banco de Histórico

↓

Timeline

↓

Replay
```

O Event Log recebe informações de praticamente todos os módulos do sistema.

---

# Responsabilidades

O Event Log será responsável por:

- registrar acontecimentos do sistema;
- registrar mudanças de estado;
- registrar eventos da liturgia;
- registrar eventos operacionais;
- registrar eventos da IA;
- fornecer contexto para auditorias;
- alimentar a Timeline e o Replay.

---

# Diferença entre Event Log e Change Log

O Event Log registra acontecimentos.

Exemplo:

```text
Culto iniciado.
```

Já o Change Log registra alterações técnicas.

Exemplo:

```text
Gain

18 dB

↓

20 dB
```

Ambos fazem parte do Histórico de Alterações, porém possuem responsabilidades distintas.

---

# Categorias de Eventos

O Event Log organiza os registros em categorias.

## Evento do Sistema

Exemplo:

```text
Aplicação iniciada.
```

```text
Mesa conectada.
```

```text
Backup realizado.
```

---

## Evento da Liturgia

Exemplo:

```text
Início do Louvor.
```

```text
Pregação iniciada.
```

```text
Santa Ceia iniciada.
```

---

## Evento Operacional

Exemplo:

```text
Operador alterado.
```

```text
Snapshot carregado.
```

```text
Modo Culto ativado.
```

---

## Evento da IA

Exemplo:

```text
Nova recomendação gerada.
```

```text
Recomendação aceita.
```

```text
Recomendação ignorada.
```

---

## Evento Técnico

Exemplo:

```text
Mesa desconectada.
```

```text
Reconexão realizada.
```

```text
Perda de comunicação.
```

---

# Estrutura de um Evento

Cada evento poderá possuir uma estrutura semelhante.

```text
ID

EVT-000321

Data

12/05/2028

Hora

09:41:12

Categoria

Liturgia

Evento

Início do Louvor

Origem

Sistema
```

---

# Informações Registradas

Cada evento poderá conter:

- identificador;
- data;
- horário;
- categoria;
- origem;
- descrição;
- operador (quando aplicável);
- etapa da liturgia;
- sessão do evento;
- informações adicionais.

---

# Origem dos Eventos

Os eventos poderão ser gerados por diversos componentes.

Exemplo:

```text
Sistema
```

```text
Dashboard
```

```text
Console
```

```text
Ui24R
```

```text
Painel da IA
```

```text
Operador
```

---

# Linha do Tempo

O Event Log é a principal fonte da Timeline.

Exemplo:

```text
09:00

Evento iniciado

↓

09:03

Mesa conectada

↓

09:05

Início do Louvor

↓

09:38

Pregação

↓

10:27

Encerramento
```

Essa linha do tempo fornece uma visão clara da sequência do evento.

---

# Integração com o Replay

Durante a reprodução de um evento, o Replay utilizará o Event Log para restaurar os acontecimentos exatamente na ordem em que ocorreram.

Exemplo:

```text
09:05

Louvor iniciado

↓

09:18

Primeira oração

↓

09:24

Avisos

↓

09:36

Pregação
```

---

# Integração com a Liturgia

O Painel da Liturgia gera diversos eventos.

Exemplo:

```text
Próxima música iniciada.
```

```text
Leitura Bíblica concluída.
```

```text
Pregador assumiu o púlpito.
```

Esses registros permitem contextualizar toda a operação.

---

# Integração com a IA

A Inteligência Artificial poderá utilizar o Event Log para compreender o contexto do evento.

Exemplo:

```text
Evento

Início da Pregação

↓

A IA reduz automaticamente
a frequência de notificações.
```

---

# Integração com Relatórios

Ao final do culto, o Event Log poderá gerar um resumo cronológico.

Exemplo:

```text
Resumo do Evento

09:00

Início

09:05

Louvor

09:37

Pregação

10:28

Encerramento
```

Esse resumo poderá ser anexado ao relatório operacional.

---

# Consultas

O Event Log permitirá pesquisas como:

```text
Mostrar todos os eventos da Liturgia.
```

```text
Listar eventos do Sistema.
```

```text
Eventos ocorridos entre 09:30 e 10:00.
```

```text
Eventos gerados pela IA.
```

---

# Desempenho

Os registros deverão ocorrer de forma assíncrona e com baixo impacto na operação.

Mesmo em eventos com milhares de registros, o Event Log deverá manter alta performance e não interferir na comunicação com a mesa de som.

---

# Benefícios

O Event Log proporciona:

- histórico cronológico do evento;
- rastreabilidade operacional;
- suporte ao Replay;
- integração com a Timeline;
- contexto para a Inteligência Artificial;
- base para auditorias e relatórios;
- documentação completa da operação.

---

# Separação de Responsabilidades

O Event Log não:

- registra alterações de parâmetros da mesa (Change Log);
- executa comandos;
- aprende padrões;
- gera recomendações;
- controla a operação.

Sua responsabilidade é registrar todos os acontecimentos relevantes da aplicação durante o evento.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- classificação automática por importância;
- filtros inteligentes por categoria;
- pesquisa em linguagem natural;
- exportação cronológica em PDF e Excel;
- sincronização opcional com calendários de eventos;
- marcação de eventos favoritos;
- integração com notificações e alertas.

---

# Relação com Outros Componentes

O Event Log trabalha diretamente com:

- History Manager;
- Change Log;
- Timeline;
- Replay;
- Painel da Liturgia;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA;
- Telemetry Manager;
- Learning Engine.

Ele representa o registro cronológico dos acontecimentos do Audio Copilot, documentando tudo o que ocorre durante um evento e fornecendo o contexto necessário para auditoria, análise, aprendizado da IA e reprodução completa da operação.

---

# Situação da Sprint

**Status:** ✅ Concluída