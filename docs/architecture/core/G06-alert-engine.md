# Sprint G06 – Alert Engine

## Objetivo

Definir a arquitetura do **Alert Engine**, componente responsável pela detecção, classificação, gerenciamento e distribuição de todos os alertas do Audio Copilot.

O Alert Engine monitora continuamente o estado da operação e informa ao operador apenas situações que realmente exigem atenção.

Seu principal objetivo é reduzir a carga cognitiva do operador, evitando excesso de notificações e apresentando apenas alertas relevantes, no momento correto e com a prioridade adequada.

---

# Visão Geral

Durante um evento podem ocorrer diversas situações que exigem atenção imediata ou acompanhamento.

Exemplos:

- possível microfonia;
- canal sem sinal;
- clipping;
- bateria baixa do microfone sem fio;
- gravação interrompida;
- perda de comunicação com a Ui24R;
- atraso na programação;
- cena não aplicada;
- recurso indisponível.

O Alert Engine centraliza o gerenciamento de todas essas ocorrências.

---

# Papel dentro do Audio Copilot

O Alert Engine possui as seguintes responsabilidades:

- detectar alertas;
- classificar severidade;
- eliminar alertas duplicados;
- priorizar notificações;
- distribuir alertas aos módulos;
- acompanhar resolução;
- registrar histórico.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Alert Engine
│
├── Alert Registry
├── Alert Controller
├── Alert Detector
├── Alert Prioritizer
├── Alert Dispatcher
├── Alert Repository
└── Alert History
```

Cada módulo possui responsabilidades específicas.

---

# Alert Registry

Responsável pelo cadastro dos tipos de alerta.

Cada alerta possuirá um identificador único.

Exemplo:

```text
ALT-000081
```

Também serão registrados:

- nome;
- categoria;
- severidade;
- descrição;
- ação recomendada.

---

# Alert Controller

Coordena todo o ciclo de vida dos alertas.

Permite:

- criar;
- ativar;
- atualizar;
- reconhecer;
- resolver;
- encerrar.

Também controla alertas recorrentes.

---

# Alert Detector

Monitora continuamente todos os componentes do Audio Copilot.

Sempre que alguma condição anormal for identificada, um alerta poderá ser gerado.

Exemplos:

- canal sem áudio;
- pico de sinal;
- microfonia;
- perda de conexão;
- gravação interrompida;
- operação manual inesperada.

---

# Alert Prioritizer

Classifica automaticamente cada alerta.

Prioridades:

```text
Crítica

Alta

Média

Baixa

Informativa
```

A prioridade determina:

- ordem de exibição;
- necessidade de confirmação;
- comportamento da IA.

---

# Alert Dispatcher

Distribui os alertas para os módulos interessados.

Exemplos:

- Tela Principal;
- Console de Operação;
- Painel da IA;
- Mobile;
- Sistema de Logs;
- Relatórios.

Cada módulo recebe apenas os alertas pertinentes.

---

# Alert Repository

Responsável pelo armazenamento permanente dos alertas.

São registrados:

- origem;
- categoria;
- horário;
- prioridade;
- duração;
- resolução.

---

# Alert History

Mantém todo o histórico de alertas ocorridos.

Cada registro conterá:

- início;
- fim;
- operador responsável;
- ação tomada;
- tempo de resolução.

Esse histórico será utilizado em auditorias e aprendizado da IA.

---

# Estrutura do Alerta

Cada alerta deverá possuir:

```text
Alerta

ID

Título

Descrição

Categoria

Severidade

Origem

Data

Hora

Status
```

---

# Categorias de Alertas

Inicialmente o sistema suportará:

- Áudio;
- Ui24R;
- Rede;
- Programação;
- Liturgia;
- Cena;
- Gravação;
- IA;
- Sistema;
- Segurança;
- Manutenção.

---

# Estados do Alerta

Cada alerta poderá assumir apenas um estado.

```text
Detectado

↓

Notificado

↓

Reconhecido

↓

Resolvido

↓

Arquivado
```

Todo o ciclo será registrado automaticamente.

---

# Fluxo de Funcionamento

```text
Evento

↓

Detector

↓

Nova Ocorrência?

↓

Sim

↓

Classificar Prioridade

↓

Gerar Alerta

↓

Distribuir

↓

Registrar Histórico
```

---

# Severidade

Cada alerta possuirá um nível de severidade.

```text
Crítica

Alta

Média

Baixa

Informativa
```

Exemplos:

**Crítica**

- perda da conexão com a Ui24R;
- gravação interrompida;
- falha do sistema.

**Alta**

- clipping contínuo;
- microfonia;
- canal principal sem áudio.

**Média**

- bateria baixa;
- atraso da programação;
- cena não aplicada.

**Baixa**

- alteração manual de parâmetro;
- recurso opcional indisponível.

**Informativa**

- gravação iniciada;
- gravação finalizada;
- mudança de etapa.

---

# Estratégia de Notificação

O sistema seguirá uma política de baixa carga cognitiva.

Assim:

- alertas informativos poderão ser silenciosos;
- alertas de baixa prioridade aparecerão discretamente;
- alertas médios poderão solicitar atenção;
- alertas altos terão destaque visual;
- alertas críticos poderão exigir confirmação do operador.

O objetivo é evitar excesso de notificações.

---

# Integração com Outros Componentes

O Alert Engine fornece informações para:

- Event Manager;
- Program Manager;
- Liturgy Manager;
- Scene Manager;
- Rule Engine;
- Operation State;
- Recording System;
- IA Operacional;
- Tela Principal;
- Console de Operação;
- Dashboard Mobile;
- Sistema de Logs.

Também recebe eventos provenientes de todos esses componentes.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- alertas duplicados deverão ser agrupados;
- somente alertas relevantes deverão ser exibidos ao operador;
- toda ocorrência deverá ser registrada;
- alertas críticos não poderão ser ignorados automaticamente;
- a resolução de um alerta deverá ser registrada;
- a IA poderá sugerir ações corretivas, mas nunca ocultará um alerta crítico.

---

# Requisitos Funcionais

O Alert Engine deverá permitir:

- detectar alertas;
- classificar severidade;
- registrar ocorrências;
- atualizar estado;
- reconhecer alertas;
- resolver alertas;
- consultar histórico;
- pesquisar alertas;
- exportar registros.

---

# Requisitos Não Funcionais

O componente deverá:

- responder em tempo real;
- minimizar falsos positivos;
- suportar grande quantidade de eventos simultâneos;
- manter histórico permanente;
- possuir baixo impacto no desempenho do sistema.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- correlação automática entre alertas;
- previsão de falhas baseada em IA;
- agrupamento inteligente de ocorrências;
- notificações push para dispositivos móveis;
- painel estatístico de alertas;
- configuração personalizada de prioridades;
- integração com sistemas externos de monitoramento;
- autoencerramento inteligente de alertas resolvidos;
- recomendações preventivas baseadas no histórico.

---

# Situação da Sprint

**Status:** ✅ Concluída