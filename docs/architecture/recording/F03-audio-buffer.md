# Sprint F03 – Audio Buffer

## Objetivo

Definir a arquitetura do **Audio Buffer**, componente responsável por manter continuamente uma janela temporária de áudio em memória, permitindo a utilização dos recursos de Replay Instantâneo, análise em tempo real pela Inteligência Artificial e recuperação de trechos recentes da operação.

O Audio Buffer funciona de forma independente das gravações permanentes, garantindo que o operador possa revisar rapidamente os últimos segundos ou minutos da operação, mesmo que nenhuma gravação tenha sido iniciada.

---

# Visão Geral

O Audio Buffer é um mecanismo de armazenamento temporário que mantém continuamente o áudio mais recente capturado pelo sistema.

Seu funcionamento é semelhante a um **buffer circular (Ring Buffer)**, onde os dados mais antigos são automaticamente substituídos pelos mais recentes quando o limite configurado é atingido.

Esse comportamento garante baixo consumo de memória e disponibilidade imediata do áudio recente.

---

# Papel dentro do Audio Copilot

O Audio Buffer é responsável por fornecer uma memória temporária da operação.

Suas principais funções são:

- manter os últimos minutos de áudio disponíveis;
- permitir Replay Instantâneo;
- fornecer áudio para análises da IA;
- reduzir o tempo de acesso às gravações recentes;
- permitir recuperação rápida de trechos importantes.

---

# Arquitetura Geral

O Audio Buffer é composto pelos seguintes componentes.

```text
Audio Buffer
│
├── Buffer Controller
├── Ring Buffer
├── Audio Writer
├── Audio Reader
├── Replay Provider
└── Buffer Monitor
```

Cada componente possui uma responsabilidade específica dentro do gerenciamento do buffer.

---

# Buffer Controller

Responsável pelo gerenciamento geral do buffer.

Suas funções incluem:

- inicializar o buffer;
- controlar o tamanho máximo;
- monitorar utilização;
- liberar memória quando necessário;
- coordenar leitura e escrita.

---

# Ring Buffer

Estrutura responsável pelo armazenamento temporário do áudio.

Seu funcionamento segue o modelo FIFO (First In, First Out).

Quando o limite de armazenamento é atingido, os dados mais antigos são automaticamente substituídos pelos novos.

Exemplo:

```text
Tempo

← Dados antigos | Dados recentes →

██████████████████████████████████

Quando o limite é atingido:

██████████████████████████████████
             ↑
     sobrescreve o início
```

---

# Audio Writer

Recebe continuamente o fluxo de áudio proveniente da fonte de captura.

Suas responsabilidades incluem:

- receber amostras de áudio;
- gravar continuamente no buffer;
- garantir sincronização temporal;
- minimizar latência.

---

# Audio Reader

Responsável pela leitura do conteúdo armazenado.

Permite recuperar rapidamente qualquer trecho ainda disponível dentro da janela temporal do buffer.

---

# Replay Provider

Disponibiliza os dados necessários para o módulo de Replay.

Esse componente permite reproduzir imediatamente:

- últimos 30 segundos;
- último minuto;
- últimos 5 minutos;
- últimos 10 minutos.

Sem necessidade de uma gravação permanente.

---

# Buffer Monitor

Monitora continuamente:

- utilização da memória;
- tamanho do buffer;
- tempo disponível;
- desempenho da captura;
- possíveis perdas de dados.

Caso alguma anormalidade seja detectada, o sistema poderá gerar alertas.

---

# Funcionamento

O funcionamento do Audio Buffer ocorre continuamente.

```text
Captura de Áudio

↓

Audio Writer

↓

Ring Buffer

↓

Replay

↓

IA

↓

Descarta dados antigos
```

Todo o processo ocorre em tempo real.

---

# Janela Temporal

O tamanho do buffer será configurável.

Exemplos:

- 30 segundos;
- 1 minuto;
- 5 minutos;
- 10 minutos;
- 15 minutos.

A configuração dependerá dos recursos disponíveis na máquina.

---

# Independência das Gravações

O Audio Buffer funciona independentemente do Sistema de Gravação.

Isso significa que:

- o Replay continuará funcionando mesmo sem gravação ativa;
- a IA poderá analisar o áudio em tempo real;
- apenas os dados dentro da janela configurada permanecerão disponíveis.

---

# Integração com Replay

O Replay utiliza diretamente o conteúdo armazenado pelo Audio Buffer.

Fluxo simplificado:

```text
Operador

↓

Replay 30 segundos

↓

Replay Engine

↓

Audio Buffer

↓

Reprodução
```

Esse processo ocorre praticamente de forma instantânea.

---

# Integração com a Inteligência Artificial

A IA poderá utilizar o Audio Buffer para:

- detectar microfonias;
- identificar clipping;
- analisar ruídos;
- detectar picos de volume;
- reconhecer padrões recorrentes;
- gerar recomendações em tempo real.

A utilização do buffer evita que a IA dependa exclusivamente das gravações permanentes.

---

# Recuperação de Trechos

Quando solicitado pelo operador, um trecho armazenado no buffer poderá ser convertido em uma Recording Session permanente.

Exemplo:

```text
Replay

↓

Selecionar últimos 5 minutos

↓

Salvar como nova gravação

↓

Biblioteca de Gravações
```

Essa funcionalidade permite preservar rapidamente momentos importantes sem a necessidade de manter uma gravação contínua.

---

# Gerenciamento de Memória

O Audio Buffer deverá:

- reutilizar continuamente a memória;
- evitar alocações desnecessárias;
- minimizar uso de CPU;
- minimizar uso de disco;
- garantir baixa latência.

---

# Regras de Negócio

O Audio Buffer deverá seguir as seguintes regras:

- iniciar automaticamente com o Audio Copilot;
- permanecer ativo durante toda a operação;
- substituir automaticamente os dados mais antigos;
- não depender de gravações permanentes;
- permitir recuperação imediata dos trechos disponíveis;
- respeitar o tamanho máximo configurado;
- manter sincronização temporal com os eventos do sistema.

---

# Requisitos Funcionais

O Audio Buffer deverá permitir:

- captura contínua;
- leitura em tempo real;
- replay imediato;
- recuperação de trechos;
- fornecimento de dados para IA;
- integração com Recording Session.

---

# Requisitos Não Funcionais

O componente deverá:

- operar continuamente durante eventos longos;
- consumir pouca memória;
- apresentar baixa latência;
- suportar futuras gravações multicanal;
- garantir estabilidade durante toda a operação.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- buffer independente por canal;
- múltiplos buffers simultâneos;
- buffer de vídeo sincronizado;
- buffer compartilhado para múltiplos operadores;
- replay instantâneo por canal;
- recuperação automática de eventos críticos;
- armazenamento inteligente baseado em IA.

---

# Situação da Sprint

**Status:** ✅ Concluída