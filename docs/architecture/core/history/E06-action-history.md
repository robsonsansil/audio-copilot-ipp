# Sprint E06 – Action History

## Objetivo

Definir o componente responsável por registrar todas as ações executadas pelos operadores durante a operação do Audio Copilot.

Enquanto o **Change Log** registra **o que mudou na mesa de som**, o **Action History** registra **quem realizou a ação**, **quando**, **como** e **por qual motivo**, sempre que essa informação estiver disponível.

Seu objetivo é criar um histórico completo da interação humana com o sistema, permitindo auditoria, treinamento, aprendizado da Inteligência Artificial e análise do comportamento operacional.

---

# Visão Geral

Durante um culto, o operador toma dezenas ou centenas de decisões.

Entre elas:

- mover um fader;
- mutar um canal;
- carregar uma cena;
- alterar um ganho;
- aceitar uma sugestão da IA;
- ignorar uma recomendação;
- cancelar uma alteração;
- iniciar o modo Ensaio.

Todas essas ações representam decisões humanas importantes.

O Action History registra essas decisões de forma organizada.

---

# Filosofia

O Action History foi desenvolvido seguindo cinco princípios.

## Responsabilidade

Toda ação deve possuir um responsável identificado.

---

## Contexto

Uma ação deve ser analisada dentro do momento em que ocorreu.

---

## Transparência

O histórico deve permitir compreender as decisões do operador.

---

## Aprendizado

As ações dos operadores alimentam o Learning Engine.

---

## Auditoria

As decisões humanas devem ser rastreáveis.

---

# Arquitetura

```text
Operador

↓

Dashboard

↓

Console Operacional

↓

Action History

↓

History Manager

↓

Banco de Histórico

↓

Learning Engine

↓

Relatórios
```

---

# Responsabilidades

O Action History será responsável por:

- registrar ações do operador;
- identificar o responsável pela ação;
- registrar data e horário;
- registrar o contexto da ação;
- registrar a origem da interação;
- fornecer histórico para auditorias;
- alimentar o Learning Engine.

---

# O que é uma ação?

Uma ação representa qualquer interação realizada pelo operador.

Exemplos:

```text
Mover Fader
```

```text
Mutar Canal
```

```text
Aceitar Sugestão da IA
```

```text
Trocar Snapshot
```

```text
Alterar Ganho
```

```text
Iniciar Evento
```

---

# Tipos de Ações

## Operação da Mesa

Exemplos:

- alterar ganho;
- mover fader;
- mutar canal;
- alterar equalização;
- modificar compressor;
- alterar envios auxiliares.

---

## Operação do Sistema

Exemplos:

- iniciar evento;
- finalizar evento;
- trocar operador;
- alterar modo operacional;
- abrir Dashboard;
- carregar configuração.

---

## Interação com a IA

Exemplos:

- aceitar recomendação;
- rejeitar recomendação;
- ignorar sugestão;
- solicitar nova análise.

---

## Administração

Exemplos:

- alterar configurações;
- criar perfil;
- cadastrar participante;
- modificar programação.

---

# Estrutura de uma Ação

Cada registro poderá conter:

```text
ID

ACT-000187

Data

12/05/2028

Hora

09:42:31

Operador

Robson

Ação

Alterou Gain

Canal

08

Origem

Console
```

---

# Informações Registradas

Cada ação poderá armazenar:

- identificador;
- data;
- horário;
- operador;
- tipo da ação;
- descrição;
- canal relacionado;
- origem;
- etapa da liturgia;
- modo operacional;
- observações (quando aplicável).

---

# Contexto Operacional

Além da ação em si, o sistema registra o contexto.

Exemplo:

```text
Etapa

Pregação

Modo

Culto

Operador

Robson

Ação

Reduziu o retorno do Monitor 2.
```

Isso facilita análises posteriores.

---

# Ações Relacionadas à IA

Quando houver interação com a Inteligência Artificial, isso também será registrado.

Exemplo:

```text
IA

Sugestão

Reduzir o Gain

↓

Operador

Aceitou.
```

Outro exemplo:

```text
IA

Sugestão

Verificar Playback

↓

Operador

Ignorou.
```

Essas informações são fundamentais para o aprendizado da IA.

---

# Sessões de Operação

As ações poderão ser agrupadas por sessão.

Exemplo:

```text
Culto Domingo Manhã

↓

Operador

Robson

↓

214 ações registradas.
```

Essa organização facilita auditorias e relatórios.

---

# Linha do Tempo

O Action History mantém todas as ações em ordem cronológica.

```text
09:32

Gain

↓

09:34

Mute

↓

09:36

Aceitou sugestão da IA

↓

09:38

Carregou Snapshot
```

---

# Integração com o Learning Engine

O Learning Engine utiliza o Action History para aprender padrões de operação.

Exemplo:

```text
Durante a Pregação

↓

Operador reduz o retorno
em aproximadamente 2 dB.

↓

Padrão aprendido.
```

---

# Integração com Auditoria

O módulo de Auditoria poderá responder perguntas como:

```text
Quem realizou a alteração?

↓

Quando?

↓

Qual ação foi executada?

↓

Em qual contexto?
```

---

# Integração com Relatórios

Ao final do evento, o sistema poderá gerar estatísticas.

Exemplo:

```text
Operador

Robson

Total de ações

214

Alterações

158

Sugestões aceitas

18

Sugestões ignoradas

6
```

---

# Integração com Replay

Durante a reprodução do evento, será possível visualizar cada ação executada pelo operador.

Exemplo:

```text
09:42

Operador reduziu o Gain.

↓

09:43

Mutou o Playback.

↓

09:44

Aceitou recomendação da IA.
```

Isso torna o Replay muito mais rico para treinamentos.

---

# Benefícios

O Action History proporciona:

- rastreabilidade das decisões humanas;
- histórico completo da operação;
- base para auditoria;
- suporte ao aprendizado da IA;
- geração de estatísticas por operador;
- apoio ao treinamento de novos operadores;
- reconstrução detalhada da operação.

---

# Separação de Responsabilidades

O Action History não:

- registra alterações técnicas da mesa (Change Log);
- registra eventos gerais do sistema (Event Log);
- gera recomendações;
- executa comandos;
- interpreta decisões do operador.

Sua única responsabilidade é registrar todas as ações realizadas pelos operadores durante a utilização do Audio Copilot.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- comparação entre operadores;
- indicadores de produtividade operacional;
- métricas de tempo de resposta;
- identificação automática de padrões de trabalho;
- estatísticas por tipo de evento;
- ranking de utilização das funcionalidades;
- análise de desempenho durante treinamentos;
- integração com perfis individuais de operadores.

---

# Relação com Outros Componentes

O Action History trabalha diretamente com:

- History Manager;
- Change Log;
- Event Log;
- AI History;
- Audit;
- Timeline;
- Replay;
- Learning Engine;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA.

Ele representa o histórico das ações humanas dentro do Audio Copilot, registrando todas as interações dos operadores com o sistema e fornecendo informações essenciais para auditoria, aprendizado da IA, geração de relatórios e evolução contínua da operação.

---

# Situação da Sprint

**Status:** ✅ Concluída