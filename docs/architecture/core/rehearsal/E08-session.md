# Sprint E08 – Session

## Objetivo

Definir a estrutura que representa uma sessão de ensaio dentro do Audio Copilot.

A **Session** é a unidade central do Modo Ensaio. Ela reúne todas as informações produzidas durante uma preparação, funcionando como o contêiner oficial de dados utilizados pela Inteligência Artificial, pelo histórico do sistema e pelos relatórios operacionais.

Cada ensaio realizado pela equipe gera exatamente uma Session.

---

# Visão Geral

Uma sessão representa todo o ciclo de vida de um ensaio.

Ela começa quando o operador inicia o Modo Ensaio e termina somente após o encerramento da preparação.

Durante esse período, a Session armazena todas as informações relevantes.

Exemplos:

- data;
- horário;
- operador;
- participantes;
- liturgia;
- músicas;
- snapshots;
- ajustes realizados;
- recomendações da IA;
- métricas;
- observações.

---

# Filosofia

A Session foi desenvolvida seguindo cinco princípios.

## Unidade

Todo ensaio deve possuir apenas uma sessão principal.

---

## Persistência

As informações da sessão devem permanecer disponíveis para consultas futuras.

---

## Organização

Todos os dados do ensaio devem permanecer agrupados em um único objeto lógico.

---

## Rastreabilidade

Cada informação registrada deve possuir origem e momento de criação.

---

## Reutilização

Os dados poderão alimentar diversos componentes do sistema.

---

# Arquitetura

```text
Modo Ensaio

↓

Rehearsal Manager

↓

Session

├── Identificação
├── Participantes
├── Liturgia
├── Ajustes
├── Snapshots
├── Recomendações
├── Métricas
├── Histórico
└── Relatório
```

---

# Responsabilidades

A Session será responsável por:

- armazenar os dados do ensaio;
- manter o estado da sessão;
- registrar participantes;
- registrar ajustes;
- armazenar recomendações;
- consolidar métricas;
- fornecer contexto para outros módulos.

---

# Ciclo de Vida

```text
Criada

↓

Inicializada

↓

Em Execução

↓

Pausada

↓

Finalizada

↓

Arquivada
```

---

# Identificação

Cada sessão possuirá um identificador único.

Exemplo:

```text
Session ID

ENS-2027-00015
```

Esse identificador será utilizado pelo histórico, auditoria e replay.

---

# Informações Básicas

A sessão poderá armazenar:

- identificador;
- data;
- horário de início;
- horário de término;
- duração;
- operador responsável;
- igreja;
- evento relacionado;
- versão da configuração utilizada.

---

# Estado da Sessão

A Session manterá seu estado atualizado durante toda a execução.

Exemplo:

```text
Preparação

↓

Passagem de Som

↓

Ensaio

↓

Finalização
```

Essas informações serão utilizadas pelo Rehearsal Manager.

---

# Participantes

A sessão armazenará todos os participantes do ensaio.

Exemplo:

- operador;
- pastor;
- músicos;
- vocalistas;
- técnicos;
- convidados.

Cada participante poderá possuir informações complementares.

---

# Liturgia

Caso exista um planejamento do evento, ele poderá ser associado à sessão.

Exemplo:

```text
Abertura

↓

Louvor

↓

Oferta

↓

Pregação

↓

Encerramento
```

Isso permitirá relacionar ajustes às diferentes etapas do evento.

---

# Músicas

A Session poderá registrar todas as músicas ensaiadas.

Para cada música poderão ser armazenados:

- nome;
- tonalidade;
- andamento;
- participantes;
- snapshots utilizados;
- observações.

---

# Snapshots

Todos os snapshots utilizados durante o ensaio poderão ser registrados.

Exemplo:

```text
Snapshot Inicial

↓

Louvor

↓

Pregação

↓

Final
```

Também poderão ser registradas diferenças entre versões.

---

# Ajustes

Cada alteração realizada durante o ensaio poderá ser registrada.

Exemplo:

```text
20:14

Canal 08

↓

Gain

+2 dB

↓

Operador
```

Esses registros serão utilizados pelo Adjustment Tracker.

---

# Recomendações

A Session armazenará todas as recomendações produzidas pela IA.

Exemplo:

```text
Reduzir Gain

↓

Aceita
```

Ou:

```text
Aumentar Compressor

↓

Ignorada
```

---

# Observações

O operador poderá registrar observações livres.

Exemplo:

```text
Microfone do Vocal 2
apresentou ruído.

Trocar cabo.
```

Essas anotações farão parte do relatório final.

---

# Métricas

A sessão consolidará indicadores importantes.

Exemplos:

- duração do ensaio;
- quantidade de ajustes;
- canais alterados;
- snapshots utilizados;
- recomendações aceitas;
- recomendações rejeitadas;
- tempo médio entre alterações.

---

# Telemetria

A Session poderá armazenar estatísticas coletadas durante o ensaio.

Exemplo:

- Peak máximo;
- RMS médio;
- clipping registrado;
- headroom disponível;
- períodos de silêncio.

Esses dados poderão alimentar análises futuras.

---

# Histórico

Toda ação executada durante a sessão será registrada.

Exemplo:

```text
19:42

Snapshot carregado

↓

19:45

EQ alterado

↓

19:47

Sugestão aceita
```

---

# Relatório

Ao final do ensaio a Session servirá como fonte para geração do relatório.

O relatório poderá conter:

- resumo da sessão;
- participantes;
- músicas;
- ajustes;
- recomendações;
- métricas;
- pendências.

---

# Persistência

Após o encerramento, a Session será armazenada permanentemente.

Ela poderá ser utilizada por:

- Replay;
- Auditoria;
- IA;
- Estatísticas;
- Comparação entre ensaios.

---

# Recuperação

Caso o sistema seja reiniciado durante um ensaio, a Session poderá ser restaurada.

Exemplo:

```text
Sistema reiniciado

↓

Recuperar Session

↓

Continuar captura
```

---

# Integração com a IA

A Session fornece contexto para:

- Context Manager;
- Learning Engine;
- Recommendation Engine;
- Confidence Engine;
- Decision Engine.

Toda aprendizagem realizada pela IA é baseada nas informações armazenadas na sessão.

---

# Integração com o Histórico

O History Manager utiliza a Session como referência principal para organizar todos os registros produzidos durante o ensaio.

---

# Integração com o Dashboard

O Dashboard poderá exibir informações da sessão em tempo real.

Exemplo:

- tempo de ensaio;
- número de alterações;
- recomendações emitidas;
- progresso da preparação.

---

# Benefícios

A Session proporciona:

- organização completa dos dados do ensaio;
- rastreabilidade de todas as ações;
- integração entre módulos;
- persistência das informações;
- suporte ao aprendizado da IA;
- base para relatórios e auditorias.

---

# Separação de Responsabilidades

A Session não:

- controla o ensaio;
- realiza análises;
- gera recomendações;
- monitora telemetria;
- altera parâmetros da mesa.

Sua responsabilidade é representar e armazenar todas as informações relacionadas a uma única sessão de ensaio.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- múltiplas sessões relacionadas ao mesmo evento;
- sincronização em nuvem;
- anexos de áudio, vídeo e documentos;
- assinatura digital dos operadores;
- versionamento completo das sessões;
- integração com calendários da igreja;
- compartilhamento entre equipes técnicas;
- exportação para formatos externos.

---

# Relação com Outros Componentes

A Session trabalha diretamente com:

- Rehearsal Manager;
- Observation Engine;
- Learning Capture;
- Adjustment Tracker;
- Scene Comparison;
- Performance Analysis;
- Rehearsal Report;
- History Manager;
- Learning Engine;
- Recommendation Engine;
- Dashboard Operacional;
- Console Operacional.

Ela representa a entidade central do Modo Ensaio, concentrando todas as informações produzidas durante a preparação do evento e servindo como fonte oficial de dados para o aprendizado da Inteligência Artificial, auditoria, estatísticas e evolução contínua do Audio Copilot.

---

# Situação da Sprint

**Status:** ✅ Concluída