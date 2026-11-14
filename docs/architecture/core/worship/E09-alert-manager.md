# Sprint E09 – Alert Manager

## Objetivo

Definir o componente responsável por gerenciar todos os alertas emitidos durante a execução do culto, garantindo que apenas notificações realmente relevantes sejam apresentadas ao operador, no momento adequado e com a prioridade correta.

O **Alert Manager** funciona como a central inteligente de notificações do Audio Copilot. Ele recebe eventos produzidos pelos diversos componentes do sistema, avalia seu contexto, classifica sua importância e decide quando, como e se o operador deverá ser informado.

Enquanto o **Live Monitor** detecta situações operacionais, o Alert Manager decide quais delas merecem atenção imediata.

---

# Visão Geral

Durante um culto, centenas de eventos podem ocorrer simultaneamente.

Exemplos:

- clipping momentâneo;
- clipping persistente;
- perda de sinal;
- canal mutado;
- snapshot incorreto;
- excesso de ganho;
- headroom reduzido;
- phantom power desligado.

Nem todos esses eventos exigem interromper o operador.

O Alert Manager é responsável por filtrar essas informações e transformar apenas os eventos relevantes em alertas.

---

# Filosofia

O Alert Manager foi desenvolvido seguindo cinco princípios.

## Relevância

Somente situações importantes devem gerar notificações.

---

## Contextualização

Cada alerta deve considerar a etapa atual da liturgia.

---

## Discrição

O sistema deve informar sem distrair o operador.

---

## Priorização

Os alertas devem ser classificados conforme seu impacto.

---

## Não Repetição

O operador não deve receber notificações repetitivas sobre o mesmo problema.

---

# Arquitetura

```text
Live Monitor

↓

Alert Manager

├── Classificação
├── Priorização
├── Agrupamento
├── Supressão
├── Histórico
└── Notificação

↓

Live Assistant

↓

Dashboard

↓

Operador
```

---

# Responsabilidades

O Alert Manager será responsável por:

- receber eventos do sistema;
- classificar sua prioridade;
- eliminar notificações redundantes;
- agrupar eventos relacionados;
- controlar o ciclo de vida dos alertas;
- encaminhar notificações ao operador.

---

# Fluxo Geral

```text
Evento Detectado

↓

Receber Evento

↓

Analisar Contexto

↓

Classificar Prioridade

↓

Verificar Regras

↓

Emitir Alerta
```

---

# Fontes dos Alertas

Os eventos poderão ser recebidos de:

- Live Monitor;
- Peak Detector;
- Clip Detector;
- Silence Detector;
- Recommendation Engine;
- Event Tracker;
- Worship Manager;
- Telemetry Manager.

---

# Classificação

Cada alerta poderá receber um nível de prioridade.

```text
Informação

↓

Atenção

↓

Importante

↓

Crítico
```

Essa classificação definirá a forma de apresentação ao operador.

---

# Exemplos

## Informação

```text
Snapshot carregado
```

---

## Atenção

```text
Headroom abaixo do ideal
```

---

## Importante

```text
Canal próximo do clipping
```

---

## Crítico

```text
Pastor sem sinal
```

---

# Contextualização

A importância de um evento depende do momento da liturgia.

Exemplo:

```text
Microfone Pastor

↓

Sem sinal

↓

Pregação

↓

Alerta Crítico
```

Mas:

```text
Microfone Pastor

↓

Sem sinal

↓

Antes do culto

↓

Alerta de Atenção
```

O contexto altera a prioridade.

---

# Agrupamento

Eventos semelhantes poderão ser agrupados.

Exemplo:

```text
Canal 03

↓

Clipping

↓

Clipping

↓

Clipping

↓

Um único alerta
```

Isso evita excesso de notificações.

---

# Supressão

Alertas repetitivos poderão ser temporariamente ocultados.

Exemplo:

```text
Mesmo clipping

↓

15 vezes

↓

Exibir apenas uma vez
```

Após um intervalo configurável, um novo alerta poderá ser emitido caso o problema persista.

---

# Escalonamento

Caso uma situação permaneça ativa, sua prioridade poderá aumentar.

Exemplo:

```text
Clipping

↓

5 segundos

↓

Atenção

↓

20 segundos

↓

Importante

↓

40 segundos

↓

Crítico
```

---

# Ciclo de Vida

Cada alerta poderá possuir estados.

```text
Detectado

↓

Ativo

↓

Reconhecido

↓

Resolvido

↓

Arquivado
```

Isso permite acompanhar toda a evolução da ocorrência.

---

# Associação com Eventos

Cada alerta poderá ser relacionado a:

- canal;
- participante;
- snapshot;
- música;
- etapa da liturgia;
- operador.

Essa associação facilita auditorias futuras.

---

# Integração com o Live Assistant

Após a classificação do alerta, o Live Assistant decidirá como apresentá-lo.

Exemplo:

```text
Alerta

↓

Live Assistant

↓

Mensagem discreta
```

Ou:

```text
Alerta Crítico

↓

Mensagem destacada
```

---

# Integração com a IA

O Alert Manager utilizará informações de:

- Context Manager;
- Decision Engine;
- Confidence Engine;
- Safety Engine.

Esses componentes ajudam a reduzir falsos positivos e notificações desnecessárias.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- quantidade de alertas ativos;
- alertas recentes;
- alertas resolvidos;
- indicadores de criticidade;
- histórico da sessão.

---

# Integração com o Histórico

Todos os alertas poderão ser registrados.

Exemplo:

```text
20:17

Canal 08

↓

Clipping

↓

Resolvido
```

Esses registros alimentarão auditorias e relatórios.

---

# Integração com o Worship Report

Ao final do culto, o relatório poderá incluir:

- quantidade de alertas;
- alertas críticos;
- tempo médio de resolução;
- principais ocorrências;
- recomendações associadas.

---

# Benefícios

O Alert Manager proporciona:

- redução de distrações;
- notificações inteligentes;
- priorização automática;
- melhor organização operacional;
- menor risco durante o culto;
- histórico completo das ocorrências.

---

# Separação de Responsabilidades

O Alert Manager não:

- monitora diretamente a mesa;
- detecta clipping;
- aprende padrões;
- altera configurações da mesa;
- executa recomendações.

Sua responsabilidade é transformar eventos operacionais em alertas úteis, organizados e contextualizados, garantindo que o operador receba apenas as informações realmente importantes durante o culto.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- priorização adaptativa baseada em IA;
- agrupamento inteligente de múltiplos eventos;
- previsão de falhas antes da ocorrência;
- alertas específicos para transmissão ao vivo;
- integração com dispositivos móveis e smartwatches;
- notificações por voz para operadores com fones;
- perfis de alerta personalizados por operador;
- aprendizado automático dos níveis de sensibilidade.

---

# Relação com Outros Componentes

O Alert Manager trabalha diretamente com:

- Modo Culto;
- Worship Manager;
- Live Session;
- Live Monitor;
- Live Assistant;
- Event Tracker;
- Telemetry Manager;
- Peak Detector;
- Clip Detector;
- Silence Detector;
- Recommendation Engine;
- Decision Engine;
- Safety Engine;
- History Manager;
- Worship Report;
- Dashboard Operacional;
- Console Operacional.

Ele representa a central de gerenciamento de alertas do Audio Copilot, filtrando, classificando e priorizando todos os eventos detectados durante o culto para fornecer ao operador informações relevantes, no momento certo e com o menor nível possível de distração.

---

# Situação da Sprint

**Status:** ✅ Concluída