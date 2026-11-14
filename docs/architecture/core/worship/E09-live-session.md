# Sprint E09 – Live Session

## Objetivo

Definir a estrutura responsável por representar uma sessão de culto em tempo real dentro do Audio Copilot.

A **Live Session** representa todo o contexto operacional de um culto enquanto ele está em execução. Ela concentra todas as informações necessárias para que os demais componentes do sistema compreendam o estado atual do evento, permitindo que a Inteligência Artificial ofereça suporte contextualizado ao operador.

Enquanto a **Session** da Sprint E08 representa uma sessão de ensaio focada em aprendizado, a Live Session representa uma operação ao vivo, onde estabilidade, segurança e disponibilidade são prioridades.

---

# Visão Geral

Uma Live Session é criada quando o operador inicia o Modo Culto.

Ela permanece ativa durante toda a execução do evento, armazenando continuamente informações sobre:

- estado do culto;
- etapa da liturgia;
- operador responsável;
- participantes ativos;
- snapshots carregados;
- alertas;
- métricas;
- telemetria;
- eventos importantes.

Ela funciona como a fonte oficial de contexto para toda a aplicação durante o culto.

---

# Filosofia

A Live Session foi desenvolvida seguindo cinco princípios.

## Contexto Centralizado

Todos os módulos devem compartilhar uma única visão do culto.

---

## Atualização Contínua

As informações devem refletir o estado atual do evento em tempo real.

---

## Alta Disponibilidade

A sessão deve permanecer disponível durante toda a execução do culto.

---

## Consistência

Todos os componentes devem utilizar os mesmos dados operacionais.

---

## Recuperação

O estado da sessão deve poder ser restaurado em caso de falhas.

---

# Arquitetura

```text
Modo Culto

↓

Worship Manager

↓

Live Session

├── Identificação
├── Estado
├── Liturgia
├── Participantes
├── Snapshots
├── Eventos
├── Alertas
├── Telemetria
└── Estatísticas
```

---

# Responsabilidades

A Live Session será responsável por:

- representar o culto em execução;
- armazenar o contexto operacional;
- manter o estado atual da sessão;
- fornecer informações aos demais módulos;
- registrar dados temporários do culto;
- servir como referência para toda a operação.

---

# Fluxo Geral

```text
Criar Sessão

↓

Inicializar

↓

Atualizar Contexto

↓

Executar Culto

↓

Encerrar

↓

Arquivar
```

---

# Identificação

Cada sessão possuirá um identificador único.

Exemplo:

```text
LIVE-2027-0018
```

Esse identificador será utilizado pelo histórico, auditoria e geração de relatórios.

---

# Informações Gerais

A Live Session poderá armazenar:

- identificador;
- data;
- horário de início;
- horário de encerramento;
- operador responsável;
- igreja;
- evento;
- versão da configuração;
- versão do Audio Copilot.

---

# Estado da Sessão

A sessão manterá continuamente seu estado operacional.

Exemplo:

```text
Preparação

↓

Pré-Culto

↓

Em Execução

↓

Encerramento
```

Os demais componentes utilizarão esse estado para adaptar seu comportamento.

---

# Etapa Atual da Liturgia

A Live Session armazenará a etapa atual da programação.

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

Essa informação será utilizada pela IA para contextualizar recomendações.

---

# Participantes

A sessão poderá manter informações sobre os participantes ativos.

Exemplos:

- operador;
- pastor;
- músicos;
- vocalistas;
- convidados;
- técnicos.

Também poderão ser registrados participantes temporários.

---

# Snapshots

A Live Session acompanhará os snapshots utilizados durante o culto.

Exemplo:

```text
Snapshot Inicial

↓

Louvor

↓

Pregação

↓

Encerramento
```

Também poderão ser registrados horários de carregamento e alterações.

---

# Eventos

Todos os eventos importantes poderão ser associados à sessão.

Exemplos:

- início do culto;
- troca de snapshot;
- início da pregação;
- mudança de liturgia;
- alertas críticos;
- encerramento.

---

# Alertas

A sessão manterá uma lista dos alertas emitidos durante o culto.

Exemplo:

```text
20:14

Clipping

↓

Canal 08

↓

Resolvido
```

Ou:

```text
20:37

Microfone

↓

Sem sinal
```

---

# Telemetria

A Live Session poderá armazenar informações resumidas da telemetria.

Exemplos:

- Peak máximo;
- RMS médio;
- clipping detectado;
- headroom disponível;
- tempo de silêncio;
- canais mais ativos.

Esses dados poderão ser utilizados pelo Dashboard e pelos relatórios.

---

# Estatísticas

Durante o culto poderão ser atualizados indicadores como:

- tempo de culto;
- quantidade de alertas;
- número de snapshots;
- alterações realizadas;
- recomendações emitidas;
- recomendações aceitas.

---

# Contexto Compartilhado

Todos os componentes consultarão a Live Session.

Exemplo:

```text
Recommendation Engine

↓

Live Session

↓

Etapa Atual

↓

Gerar Sugestão
```

Esse compartilhamento evita inconsistências entre módulos.

---

# Atualização Contínua

A Live Session será atualizada sempre que ocorrer:

- mudança de etapa;
- novo alerta;
- alteração de snapshot;
- evento relevante;
- atualização da telemetria.

---

# Recuperação

Caso ocorra uma reinicialização do sistema:

```text
Sistema reiniciado

↓

Localizar Live Session

↓

Restaurar Estado

↓

Continuar Operação
```

A recuperação reduz o impacto de falhas durante o culto.

---

# Integração com a IA

A Live Session fornece contexto para:

- Context Manager;
- Recommendation Engine;
- Decision Engine;
- Safety Engine;
- Confidence Engine;
- Live Assistant.

Todos utilizam essas informações para produzir respostas coerentes com o momento do culto.

---

# Integração com o Histórico

Ao final do evento, a Live Session será utilizada para gerar os registros permanentes do culto.

---

# Integração com o Dashboard

O Dashboard poderá exibir:

- tempo de culto;
- etapa atual;
- participantes ativos;
- alertas recentes;
- snapshots carregados;
- estado geral da operação.

---

# Benefícios

A Live Session proporciona:

- contexto centralizado da operação;
- sincronização entre módulos;
- maior estabilidade operacional;
- compartilhamento consistente de informações;
- recuperação de sessão em caso de falhas;
- suporte eficiente à Inteligência Artificial.

---

# Separação de Responsabilidades

A Live Session não:

- monitora áudio;
- gera recomendações;
- detecta alertas;
- controla a liturgia;
- altera parâmetros da mesa.

Sua responsabilidade é representar o estado atual do culto e disponibilizar esse contexto para todos os componentes do Audio Copilot.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- sincronização em nuvem;
- operação multicâmpus;
- múltiplos operadores simultâneos;
- compartilhamento entre dispositivos;
- integração com transmissão ao vivo;
- sincronização com iluminação e projeção;
- persistência distribuída;
- espelhamento para servidores de redundância.

---

# Relação com Outros Componentes

A Live Session trabalha diretamente com:

- Worship Manager;
- Live Monitor;
- Alert Manager;
- Event Tracker;
- Live Assistant;
- Worship Report;
- History Manager;
- Telemetry Manager;
- Recommendation Engine;
- Dashboard Operacional;
- Console Operacional.

Ela representa a entidade central do Modo Culto, concentrando todas as informações necessárias para que o Audio Copilot compreenda continuamente o contexto da operação ao vivo, mantendo todos os módulos sincronizados e garantindo uma assistência inteligente, segura e consistente durante toda a execução do culto.

---

# Situação da Sprint

**Status:** ✅ Concluída