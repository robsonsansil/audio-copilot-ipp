# Sprint E06 – Timeline

## Objetivo

Definir o componente responsável por organizar e apresentar toda a sequência cronológica do evento operado pelo Audio Copilot.

A Timeline representa a linha do tempo oficial da operação. Ela reúne informações provenientes da liturgia, da mesa de som, do operador, da Inteligência Artificial e do sistema, permitindo visualizar tudo o que aconteceu durante um evento de forma simples, organizada e intuitiva.

Enquanto os módulos de histórico armazenam registros individuais, a Timeline transforma esses registros em uma narrativa cronológica da operação.

---

# Visão Geral

Durante um culto, diversos acontecimentos ocorrem simultaneamente.

Por exemplo:

- início do evento;
- conexão da mesa;
- início do louvor;
- entrada do pregador;
- recomendações da IA;
- alterações importantes na mesa;
- alertas técnicos;
- encerramento do culto.

A Timeline organiza todos esses acontecimentos em uma única sequência temporal.

---

# Filosofia

A Timeline foi desenvolvida seguindo cinco princípios.

## Clareza

A sequência dos acontecimentos deve ser facilmente compreendida.

---

## Contexto

Cada evento deve ser apresentado dentro do momento em que ocorreu.

---

## Organização

Os registros devem permanecer ordenados cronologicamente.

---

## Navegação

O operador deve localizar rapidamente qualquer momento do evento.

---

## Reconstrução

A Timeline deve permitir reconstruir completamente a operação.

---

# Arquitetura

```text
Event Log

↓

Change Log

↓

Action History

↓

AI History

↓

Timeline

↓

Dashboard

↓

Replay

↓

Relatórios
```

A Timeline consolida informações provenientes de vários componentes.

---

# Responsabilidades

A Timeline será responsável por:

- organizar eventos cronologicamente;
- consolidar registros de diferentes módulos;
- exibir a evolução do evento;
- permitir navegação temporal;
- fornecer contexto para auditorias;
- servir como base do Replay.

---

# Fontes de Informação

A Timeline poderá receber informações provenientes de:

- Event Log;
- Change Log;
- Action History;
- AI History;
- Painel da Liturgia;
- Dashboard Operacional;
- Console Operacional;
- Telemetry Manager;
- State Manager.

---

# Estrutura Geral

A Timeline representa uma sequência contínua de acontecimentos.

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

09:18

Primeira Música

↓

09:34

Pregação

↓

10:26

Encerramento
```

---

# Eventos Exibidos

A Timeline poderá apresentar:

- início e fim do evento;
- mudanças de etapa da liturgia;
- ações importantes do operador;
- recomendações da IA;
- alterações relevantes na mesa;
- alertas técnicos;
- incidentes;
- mudanças de modo operacional.

---

# Agrupamento Inteligente

Eventos repetitivos poderão ser agrupados.

Exemplo:

Ao invés de:

```text
Gain alterado

↓

Gain alterado

↓

Gain alterado
```

A Timeline poderá apresentar:

```text
Canal 08

3 alterações de ganho.
```

Isso reduz a poluição visual.

---

# Linha do Tempo da Liturgia

A Timeline acompanha a evolução da programação.

Exemplo:

```text
09:00

Recepção

↓

09:05

Louvor

↓

09:28

Avisos

↓

09:35

Pregação

↓

10:18

Santa Ceia

↓

10:30

Encerramento
```

---

# Linha do Tempo da IA

As recomendações da Inteligência Artificial também aparecem na Timeline.

Exemplo:

```text
09:41

IA detectou clipping.

↓

09:42

Sugestão apresentada.

↓

09:43

Operador aceitou.

↓

09:44

Problema resolvido.
```

---

# Linha do Tempo do Operador

As principais ações do operador poderão ser exibidas.

Exemplo:

```text
09:36

Mutou Playback.

↓

09:37

Carregou Snapshot.

↓

09:38

Alterou Gain.
```

---

# Linha do Tempo Técnica

Eventos importantes da mesa também poderão aparecer.

Exemplo:

```text
Mesa conectada.

↓

Snapshot restaurado.

↓

Canal sem sinal.

↓

Conexão restabelecida.
```

---

# Navegação

A Timeline permitirá navegar rapidamente para qualquer momento do evento.

Exemplo:

```text
09:15

↓

Abrir detalhes.

↓

Visualizar alterações.

↓

Visualizar recomendações.

↓

Visualizar operador.
```

---

# Pesquisa

Será possível localizar eventos utilizando filtros.

Exemplos:

- horário;
- operador;
- canal;
- participante;
- etapa da liturgia;
- categoria;
- origem;
- tipo de recomendação.

---

# Visualização

Cada evento poderá possuir:

- horário;
- ícone;
- categoria;
- descrição;
- responsável;
- prioridade;
- detalhes adicionais.

Exemplo:

```text
09:42

🔵 IA

Feedback detectado

Confiança

96%
```

---

# Integração com o Replay

O Replay utilizará a Timeline como eixo principal da reprodução.

Ao selecionar um ponto da Timeline, o sistema poderá reconstruir exatamente o estado da operação naquele instante.

Exemplo:

```text
09:42

↓

Abrir Replay

↓

Restaurar contexto

↓

Exibir mesa

↓

Exibir IA

↓

Exibir operador
```

---

# Integração com Auditoria

Durante uma auditoria, qualquer evento poderá ser expandido.

Exemplo:

```text
09:42

↓

Abrir Auditoria

↓

Visualizar registros relacionados.
```

---

# Integração com Relatórios

Ao final do evento, a Timeline poderá gerar um resumo cronológico.

Exemplo:

```text
Resumo

09:00

Início

09:05

Louvor

09:34

Pregação

10:18

Santa Ceia

10:30

Encerramento
```

---

# Atualização em Tempo Real

Durante o evento, novos registros serão adicionados automaticamente.

```text
Novo Evento

↓

Timeline atualizada

↓

Dashboard atualizado

↓

Replay sincronizado
```

Essa atualização deverá ocorrer sem interromper a operação do sistema.

---

# Benefícios

A Timeline proporciona:

- visão cronológica completa do evento;
- rápida localização de acontecimentos;
- contexto operacional para auditorias;
- suporte ao Replay;
- melhor compreensão da atuação da IA;
- documentação visual da operação;
- facilidade para treinamentos e análises pós-evento.

---

# Separação de Responsabilidades

A Timeline não:

- registra eventos;
- modifica históricos;
- gera recomendações;
- controla a mesa de som;
- executa comandos.

Sua responsabilidade é organizar e apresentar cronologicamente todas as informações registradas pelos componentes de histórico do Audio Copilot.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- zoom temporal da linha do tempo;
- marcadores personalizados;
- favoritos;
- filtros dinâmicos;
- comparação entre eventos;
- visualização gráfica da intensidade das alterações;
- sincronização com gravações de áudio e vídeo;
- exportação da Timeline em PDF e HTML interativo.

---

# Relação com Outros Componentes

A Timeline trabalha diretamente com:

- History Manager;
- Event Log;
- Change Log;
- Action History;
- AI History;
- Replay;
- Audit;
- Dashboard Operacional;
- Console Operacional;
- Painel da Liturgia;
- Painel da IA.

Ela representa a visão cronológica unificada do Audio Copilot, consolidando todas as ações, eventos, alterações e recomendações em uma única linha do tempo, permitindo compreender, revisar e reproduzir toda a operação de forma clara e organizada.

---

# Situação da Sprint

**Status:** ✅ Concluída