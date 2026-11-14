# Sprint E09 – Event Tracker

## Objetivo

Definir o componente responsável por registrar, organizar e acompanhar todos os eventos relevantes ocorridos durante a execução do culto.

O **Event Tracker** funciona como a memória operacional do Modo Culto, registrando cronologicamente acontecimentos importantes, ações do operador, mudanças de contexto e eventos detectados pela Inteligência Artificial.

Enquanto o **History Manager** armazena informações permanentes do sistema e o **Alert Manager** gerencia notificações, o Event Tracker registra a sequência completa dos acontecimentos que compõem a execução do culto.

---

# Visão Geral

Durante um culto, diversos eventos acontecem continuamente.

Exemplos:

- início do culto;
- mudança da liturgia;
- carregamento de snapshots;
- entrada do pastor;
- início da pregação;
- emissão de alertas;
- recomendações da IA;
- alterações realizadas pelo operador.

Esses acontecimentos formam uma linha do tempo operacional.

O Event Tracker é responsável por registrar essa sequência.

---

# Filosofia

O Event Tracker foi desenvolvido seguindo cinco princípios.

## Cronologia

Os eventos devem permanecer na ordem em que ocorreram.

---

## Contextualização

Cada evento deve conter informações suficientes para ser compreendido futuramente.

---

## Integridade

Nenhum evento importante deve ser perdido.

---

## Rastreabilidade

Toda ocorrência deve possuir origem claramente identificada.

---

## Organização

Os eventos devem ser facilmente pesquisáveis e correlacionáveis.

---

# Arquitetura

```text
Operação

↓

Event Tracker

├── Eventos
├── Linha do Tempo
├── Contexto
├── Origem
├── Categoria
└── Histórico

↓

History Manager

↓

Worship Report

↓

Replay
```

---

# Responsabilidades

O Event Tracker será responsável por:

- registrar eventos do culto;
- organizar a linha do tempo;
- identificar a origem de cada ocorrência;
- fornecer informações para auditoria;
- alimentar o Replay;
- disponibilizar dados para relatórios.

---

# Fluxo Geral

```text
Evento

↓

Capturar

↓

Adicionar Contexto

↓

Classificar

↓

Registrar

↓

Disponibilizar
```

---

# Tipos de Eventos

O componente poderá registrar eventos como:

- início do culto;
- encerramento;
- mudança de etapa da liturgia;
- carregamento de snapshot;
- alteração importante;
- alerta;
- recomendação da IA;
- reconhecimento do operador;
- falha operacional.

---

# Eventos da Liturgia

Cada mudança da programação poderá gerar um evento.

Exemplo:

```text
Recepção

↓

Louvor

↓

Oferta

↓

Pregação

↓

Ceia

↓

Encerramento
```

Essas mudanças ajudam a contextualizar toda a operação.

---

# Eventos do Operador

Também poderão ser registrados eventos originados pelo operador.

Exemplos:

- carregar snapshot;
- alterar canal;
- silenciar microfone;
- ativar efeito;
- modificar monitor.

---

# Eventos da IA

O sistema também registrará eventos produzidos pela Inteligência Artificial.

Exemplos:

- recomendação emitida;
- recomendação aceita;
- recomendação ignorada;
- alerta gerado;
- previsão de risco.

---

# Eventos da Telemetria

Informações importantes provenientes da telemetria poderão ser registradas.

Exemplos:

- clipping persistente;
- perda de sinal;
- silêncio inesperado;
- headroom crítico;
- pico excessivo.

---

# Estrutura de um Evento

Cada registro poderá conter:

- identificador;
- data;
- horário;
- categoria;
- origem;
- descrição;
- componente responsável;
- prioridade;
- contexto da liturgia;
- canal relacionado;
- operador responsável.

---

# Linha do Tempo

Todos os eventos serão organizados cronologicamente.

Exemplo:

```text
19:00

Culto iniciado

↓

19:08

Snapshot Louvor

↓

19:15

Início da Música

↓

19:42

Pregação

↓

20:35

Encerramento
```

Essa sequência permitirá reconstruir todo o culto.

---

# Classificação

Os eventos poderão ser classificados em categorias.

Exemplos:

- Operação;
- Liturgia;
- IA;
- Telemetria;
- Snapshot;
- Alerta;
- Sistema;
- Usuário.

---

# Priorização

Cada evento poderá possuir um nível de importância.

```text
Informativo

↓

Operacional

↓

Importante

↓

Crítico
```

Essa classificação facilitará consultas futuras.

---

# Associação de Eventos

Eventos poderão ser relacionados entre si.

Exemplo:

```text
Clipping

↓

Recomendação

↓

Operador reduz Gain

↓

Clipping resolvido
```

Essa relação permite compreender causa e efeito.

---

# Pesquisa

Os eventos poderão ser filtrados por:

- data;
- horário;
- categoria;
- canal;
- participante;
- operador;
- snapshot;
- etapa da liturgia;
- prioridade.

---

# Integração com o Replay

O Replay utilizará a linha do tempo produzida pelo Event Tracker.

Exemplo:

```text
19:28

Evento

↓

Selecionar

↓

Reproduzir contexto
```

Isso permitirá revisar rapidamente qualquer momento do culto.

---

# Integração com o Worship Report

Ao final do culto, o relatório utilizará os eventos registrados para construir um resumo cronológico da sessão.

---

# Integração com o History Manager

Após o encerramento da sessão, todos os eventos poderão ser armazenados permanentemente para futuras consultas e auditorias.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- últimos eventos;
- eventos críticos;
- linha do tempo resumida;
- quantidade de eventos registrados;
- categoria dos eventos.

---

# Integração com a IA

Os eventos registrados poderão alimentar:

- Learning Engine;
- Recommendation Engine;
- Performance Analysis;
- Context Manager.

Esses componentes utilizarão o histórico para identificar padrões e melhorar futuras recomendações.

---

# Benefícios

O Event Tracker proporciona:

- rastreabilidade completa do culto;
- reconstrução cronológica dos acontecimentos;
- apoio ao Replay;
- suporte à auditoria;
- documentação automática da operação;
- base histórica para aprendizado da IA.

---

# Separação de Responsabilidades

O Event Tracker não:

- monitora níveis de áudio;
- gera alertas;
- toma decisões;
- altera configurações da mesa;
- controla a liturgia.

Sua responsabilidade é registrar e organizar todos os acontecimentos relevantes do culto, preservando uma linha do tempo completa da operação.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- correlação automática entre eventos;
- identificação de sequências recorrentes;
- agrupamento inteligente por contexto;
- busca semântica utilizando IA;
- sincronização com gravações de áudio e vídeo;
- exportação da linha do tempo em múltiplos formatos;
- marcação manual de eventos pelo operador;
- integração com sistemas de transmissão e projeção.

---

# Relação com Outros Componentes

O Event Tracker trabalha diretamente com:

- Modo Culto;
- Worship Manager;
- Live Session;
- Live Monitor;
- Alert Manager;
- Live Assistant;
- History Manager;
- Replay;
- Worship Report;
- Performance Analysis;
- Learning Engine;
- Dashboard Operacional;
- Console Operacional.

Ele representa a linha do tempo oficial do Modo Culto, registrando de forma organizada todos os acontecimentos relevantes da operação e fornecendo uma base sólida para auditoria, replay, geração de relatórios e evolução contínua da Inteligência Artificial do Audio Copilot.

---

# Situação da Sprint

**Status:** ✅ Concluída