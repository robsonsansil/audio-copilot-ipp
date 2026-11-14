# Sprint E08 – Rehearsal Manager

## Objetivo

Definir o componente responsável por gerenciar todo o ciclo de vida de um ensaio dentro do Audio Copilot.

O **Rehearsal Manager** atua como o orquestrador do Modo Ensaio, controlando quando uma sessão começa, quais informações serão registradas, quais módulos serão ativados e quando o ensaio será finalizado.

Enquanto o **Modo Ensaio** define o comportamento operacional da aplicação, o **Rehearsal Manager** executa esse comportamento durante toda a sessão.

---

# Visão Geral

Um ensaio é composto por diversas etapas.

Desde a chegada da equipe até o encerramento, inúmeras informações são produzidas:

- configuração inicial;
- passagem de som;
- ajustes dos músicos;
- alterações de mixagem;
- snapshots;
- recomendações da IA;
- observações do operador.

O Rehearsal Manager coordena todas essas atividades de forma organizada.

---

# Filosofia

O Rehearsal Manager foi desenvolvido seguindo cinco princípios.

## Organização

Todo ensaio deve possuir início, desenvolvimento e encerramento claramente definidos.

---

## Centralização

Todo o gerenciamento da sessão deve ocorrer em um único componente.

---

## Rastreabilidade

Cada ação realizada durante o ensaio poderá ser identificada posteriormente.

---

## Integração

Todos os módulos do sistema deverão trabalhar sincronizados durante a sessão.

---

## Automação

Sempre que possível, tarefas repetitivas deverão ser executadas automaticamente.

---

# Arquitetura

```text
Operador

↓

Modo Ensaio

↓

Rehearsal Manager

├── Session
├── Observation Engine
├── Learning Capture
├── Adjustment Tracker
├── History Manager
├── Performance Analysis
└── Rehearsal Report
```

---

# Responsabilidades

O Rehearsal Manager será responsável por:

- iniciar ensaios;
- finalizar ensaios;
- controlar sessões;
- ativar módulos do modo ensaio;
- registrar participantes;
- sincronizar componentes;
- gerar o relatório final.

---

# Fluxo Geral

```text
Criar Sessão

↓

Preparar Ambiente

↓

Iniciar Ensaio

↓

Monitorar

↓

Registrar Ajustes

↓

Finalizar

↓

Gerar Relatório
```

---

# Inicialização

Ao iniciar um ensaio o Rehearsal Manager deverá:

- criar uma nova sessão;
- registrar data e horário;
- identificar o operador;
- identificar o evento;
- carregar snapshots iniciais;
- iniciar monitoramento.

---

# Sessão Ativa

Durante toda a sessão o componente permanecerá responsável por:

- manter o estado do ensaio;
- controlar duração;
- registrar atividades;
- coordenar módulos.

---

# Estados da Sessão

Cada ensaio poderá assumir um dos seguintes estados.

```text
Não iniciado

↓

Preparação

↓

Passagem de Som

↓

Ensaio

↓

Pausado

↓

Finalizado

↓

Arquivado
```

Esses estados serão utilizados por toda a arquitetura.

---

# Controle de Tempo

O sistema registrará automaticamente:

- início;
- pausas;
- retomadas;
- encerramento;
- duração total.

Exemplo:

```text
19:15

Início

↓

20:48

Fim

↓

1h33min
```

---

# Registro dos Participantes

Durante a criação da sessão poderão ser registrados:

- operador;
- pastor;
- músicos;
- vocalistas;
- técnicos;
- convidados.

Essas informações serão utilizadas pelos demais módulos.

---

# Ativação dos Módulos

Quando um ensaio iniciar, o Rehearsal Manager ativará automaticamente:

- Observation Engine;
- Learning Capture;
- Adjustment Tracker;
- Performance Analysis;
- History Manager.

Todos passam a registrar informações da sessão.

---

# Monitoramento

Durante o ensaio o componente acompanhará continuamente:

- alterações de parâmetros;
- snapshots;
- eventos;
- recomendações;
- métricas;
- telemetria.

---

# Pausas

O ensaio poderá ser pausado.

Exemplo:

```text
Pausar

↓

Interromper cronômetro

↓

Continuar monitorando
```

Ou:

```text
Pausar

↓

Suspender captura

↓

Retomar posteriormente
```

Esse comportamento poderá ser configurável.

---

# Retomada

Após uma pausa:

```text
Retomar

↓

Atualizar sessão

↓

Continuar registros
```

Sem perda das informações já coletadas.

---

# Encerramento

Ao finalizar um ensaio o Rehearsal Manager deverá:

- encerrar a sessão;
- finalizar monitoramentos;
- consolidar métricas;
- gerar relatório;
- armazenar histórico.

---

# Integração com a IA

Durante toda a sessão o componente fornecerá contexto para:

- Learning Engine;
- Recommendation Engine;
- Decision Engine;
- Confidence Engine.

A IA utilizará essas informações para aprender continuamente.

---

# Integração com o Histórico

Todas as atividades da sessão serão registradas.

Exemplo:

```text
19:20

Snapshot carregado

↓

19:28

Gain alterado

↓

19:41

Sugestão aceita
```

---

# Integração com a Telemetria

Os medidores permanecerão ativos durante todo o ensaio.

Exemplos:

- Peak;
- RMS;
- Clipping;
- Headroom;
- Silence Detector.

---

# Integração com o Dashboard

O Dashboard poderá apresentar informações da sessão em tempo real.

Exemplo:

- tempo de ensaio;
- número de ajustes;
- recomendações emitidas;
- canais alterados;
- progresso da preparação.

---

# Recuperação

Caso o sistema seja reiniciado durante um ensaio, o Rehearsal Manager poderá recuperar automaticamente a sessão ativa.

Exemplo:

```text
Sistema reiniciado

↓

Localizar sessão

↓

Restaurar contexto

↓

Continuar ensaio
```

---

# Benefícios

O Rehearsal Manager proporciona:

- organização completa da sessão;
- sincronização entre módulos;
- registro automático das atividades;
- preparação estruturada;
- maior confiabilidade;
- integração entre IA e operador.

---

# Separação de Responsabilidades

O Rehearsal Manager não:

- realiza recomendações;
- aprende padrões;
- analisa áudio;
- altera parâmetros da mesa;
- gera destaques visuais.

Sua responsabilidade é coordenar toda a execução operacional do Modo Ensaio.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- múltiplas sessões simultâneas;
- ensaios colaborativos;
- agendamento automático de ensaios;
- integração com calendários da igreja;
- sincronização em nuvem;
- recuperação automática após falhas;
- estatísticas históricas de ensaios;
- integração com gravações de áudio e vídeo.

---

# Relação com Outros Componentes

O Rehearsal Manager trabalha diretamente com:

- Modo Ensaio;
- Session;
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

Ele representa o núcleo operacional do Modo Ensaio, coordenando todas as etapas da preparação, sincronizando os módulos do Audio Copilot e garantindo que cada sessão seja registrada, analisada e utilizada como fonte de aprendizado para a Inteligência Artificial.

---

# Situação da Sprint

**Status:** ✅ Concluída