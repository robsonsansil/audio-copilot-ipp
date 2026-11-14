# Sprint E09 – Worship Manager

## Objetivo

Definir o componente responsável por gerenciar todo o ciclo de vida de um culto dentro do Audio Copilot.

O **Worship Manager** atua como o orquestrador do Modo Culto, coordenando todas as etapas da operação em tempo real, sincronizando os diversos módulos do sistema e garantindo que o Audio Copilot permaneça contextualizado durante toda a execução do evento.

Enquanto o **Modo Culto** define o comportamento operacional da aplicação, o **Worship Manager** é responsável por colocar esse comportamento em prática.

---

# Visão Geral

Um culto possui uma sequência lógica de acontecimentos.

Desde os minutos que antecedem o início até o encerramento do evento, diversas atividades precisam ser coordenadas.

Exemplos:

- preparação da mesa;
- carregamento da liturgia;
- ativação dos medidores;
- acompanhamento das etapas do culto;
- monitoramento da operação;
- geração do relatório final.

O Worship Manager centraliza todo esse fluxo.

---

# Filosofia

O Worship Manager foi desenvolvido seguindo cinco princípios.

## Organização

Todo culto deve possuir início, execução e encerramento claramente definidos.

---

## Coordenação

Todos os módulos devem trabalhar de forma sincronizada.

---

## Estabilidade

Durante o culto a estabilidade operacional possui prioridade máxima.

---

## Contextualização

Todas as decisões devem considerar o momento atual da liturgia.

---

## Confiabilidade

O sistema deve permanecer previsível mesmo diante de situações inesperadas.

---

# Arquitetura

```text
Operador

↓

Modo Culto

↓

Worship Manager

├── Live Session
├── Live Monitor
├── Alert Manager
├── Event Tracker
├── Live Assistant
├── History Manager
└── Worship Report
```

---

# Responsabilidades

O Worship Manager será responsável por:

- iniciar o culto;
- finalizar o culto;
- controlar a sessão ativa;
- acompanhar a liturgia;
- sincronizar módulos;
- coordenar alertas;
- controlar estados da operação;
- gerar o relatório final.

---

# Fluxo Geral

```text
Preparação

↓

Iniciar Culto

↓

Executar Liturgia

↓

Monitorar Operação

↓

Registrar Eventos

↓

Encerrar Culto

↓

Gerar Relatório
```

---

# Inicialização

Ao iniciar um culto o Worship Manager deverá:

- criar uma nova sessão;
- registrar data e horário;
- identificar o operador;
- carregar a liturgia;
- carregar snapshots;
- ativar monitoramento;
- iniciar telemetria;
- sincronizar todos os módulos.

---

# Sessão Ativa

Durante todo o culto o Worship Manager será responsável por:

- manter o estado da sessão;
- controlar a etapa atual;
- distribuir eventos;
- acompanhar a operação;
- coordenar os demais componentes.

---

# Estados do Culto

Cada sessão poderá assumir um dos seguintes estados.

```text
Preparação

↓

Pré-Culto

↓

Culto Iniciado

↓

Em Execução

↓

Pausado

↓

Encerrado

↓

Arquivado
```

Todos os módulos utilizarão esses estados para ajustar seu comportamento.

---

# Controle da Liturgia

O Worship Manager acompanhará continuamente a etapa atual do evento.

Exemplo:

```text
Recepção

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

Essa informação será utilizada por diversos componentes da IA.

---

# Controle de Tempo

O componente registrará automaticamente:

- início;
- duração de cada etapa;
- pausas;
- encerramento;
- duração total.

Exemplo:

```text
19:00

Início

↓

20:42

Encerramento

↓

1h42min
```

---

# Coordenação dos Módulos

Ao iniciar o culto, o Worship Manager ativará automaticamente:

- Live Monitor;
- Alert Manager;
- Event Tracker;
- Live Assistant;
- History Manager;
- Telemetry Manager.

Cada componente receberá o contexto da sessão ativa.

---

# Mudança de Etapas

Sempre que a liturgia avançar, o Worship Manager notificará todo o sistema.

Exemplo:

```text
Fim do Louvor

↓

Início da Pregação

↓

Atualizar Contexto
```

Assim, cada módulo adapta seu comportamento automaticamente.

---

# Gerenciamento de Snapshots

O componente poderá acompanhar a utilização dos snapshots.

Exemplo:

```text
Louvor

↓

Snapshot Louvor

↓

Pregação

↓

Snapshot Pastor
```

Também poderá registrar atrasos ou mudanças inesperadas.

---

# Coordenação dos Alertas

O Worship Manager trabalhará em conjunto com o Alert Manager.

Fluxo:

```text
Evento

↓

Live Monitor

↓

Alert Manager

↓

Worship Manager

↓

Operador
```

Dessa forma, apenas alertas relevantes chegam ao operador.

---

# Coordenação da IA

O Worship Manager fornecerá contexto para:

- Recommendation Engine;
- Decision Engine;
- Safety Engine;
- Confidence Engine;
- Live Assistant.

Esses componentes utilizarão o estágio atual do culto para produzir recomendações apropriadas.

---

# Registro de Eventos

Durante toda a sessão o Worship Manager coordenará o registro de eventos.

Exemplo:

```text
19:02

Culto iniciado

↓

19:18

Louvor

↓

19:46

Pregação

↓

20:38

Encerramento
```

---

# Recuperação

Caso ocorra reinicialização do sistema durante o culto, o Worship Manager poderá restaurar automaticamente a sessão.

Fluxo:

```text
Sistema reiniciado

↓

Localizar Sessão

↓

Restaurar Estado

↓

Continuar Operação
```

---

# Integração com a Telemetria

O componente manterá sincronização com:

- Peak Detector;
- RMS;
- Clip Detector;
- Silence Detector;
- Statistics;
- Meter Cache.

Esses dados serão utilizados pelo Live Monitor.

---

# Integração com o Histórico

Todo evento coordenado pelo Worship Manager será registrado.

Exemplos:

- início da sessão;
- mudança de etapa;
- snapshots;
- alertas;
- recomendações;
- encerramento.

---

# Integração com o Dashboard

O Dashboard poderá exibir informações em tempo real como:

- etapa atual;
- tempo de culto;
- quantidade de alertas;
- canais ativos;
- snapshots carregados;
- recomendações emitidas.

---

# Benefícios

O Worship Manager proporciona:

- coordenação completa do culto;
- sincronização entre módulos;
- contexto operacional consistente;
- maior estabilidade;
- organização da sessão;
- integração entre IA e operador.

---

# Separação de Responsabilidades

O Worship Manager não:

- analisa áudio;
- detecta clipping;
- gera recomendações;
- aprende padrões;
- altera parâmetros da mesa.

Sua responsabilidade é coordenar toda a execução operacional do Modo Culto e manter todos os componentes sincronizados.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- múltiplos ambientes simultâneos;
- cultos multicâmpus;
- sincronização entre mesas;
- integração com transmissão ao vivo;
- controle de iluminação;
- integração com projeção;
- agenda automática de eventos;
- operação distribuída em rede.

---

# Relação com Outros Componentes

O Worship Manager trabalha diretamente com:

- Modo Culto;
- Live Session;
- Live Monitor;
- Alert Manager;
- Safe Mode;
- Event Tracker;
- Live Assistant;
- Worship Report;
- History Manager;
- Telemetry Manager;
- Recommendation Engine;
- Dashboard Operacional;
- Console Operacional.

Ele representa o núcleo operacional do Modo Culto, coordenando toda a execução do evento em tempo real, sincronizando os componentes do Audio Copilot e garantindo uma operação segura, estável e contextualizada durante todo o culto.

---

# Situação da Sprint

**Status:** ✅ Concluída