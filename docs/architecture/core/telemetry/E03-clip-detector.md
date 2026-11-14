# Sprint E03 – Clip Detector

## Objetivo

Definir o componente responsável pela detecção de clipping nos canais de entrada e saída monitorados pelo Audio Copilot.

O Clip Detector tem como finalidade identificar automaticamente situações em que o sinal de áudio ultrapassa o nível seguro de operação, permitindo que o operador seja alertado imediatamente e que a Inteligência Artificial possa sugerir ações corretivas.

Este componente é fundamental para preservar a qualidade do áudio durante ensaios e eventos ao vivo.

---

# Visão Geral

O clipping ocorre quando o nível do sinal ultrapassa a capacidade de processamento do sistema, provocando distorção perceptível no áudio.

Durante uma operação ao vivo, esse problema pode passar despercebido pelo operador, principalmente quando ocorre por poucos milissegundos.

O Clip Detector monitora continuamente todos os canais ativos e identifica automaticamente essas ocorrências.

Seu papel é apenas detectar e registrar o clipping.

Ele nunca altera automaticamente qualquer configuração da mesa de som.

---

# Arquitetura

Fluxo simplificado:

```text
Soundcraft Ui24R
        │
        ▼
Telemetry Manager
        │
        ▼
Audio Levels
        │
        ▼
Clip Detector
        │
        ├────────► State Manager
        ├────────► Console de Operação
        ├────────► Painel da IA
        └────────► Histórico
```

O Clip Detector recebe continuamente os níveis processados pelo módulo Audio Levels.

---

# Responsabilidades

O Clip Detector será responsável por:

- monitorar continuamente todos os canais;
- detectar ocorrências de clipping;
- registrar o instante da ocorrência;
- atualizar os indicadores visuais;
- publicar eventos para o Event Bus;
- disponibilizar informações para a Inteligência Artificial.

---

# Funcionamento

O componente acompanha continuamente os níveis de áudio.

Sempre que um canal ultrapassar o limite seguro estabelecido pela mesa de som, será registrada uma ocorrência de clipping.

Fluxo simplificado:

```text
Novo nível recebido

↓

Verificar limite

↓

Ultrapassou?

↓

Sim

↓

Registrar ocorrência

↓

Atualizar Interface

↓

Publicar evento
```

---

# Tipos de Clipping

O sistema poderá identificar diferentes situações.

## Clipping Instantâneo

Ocorrência isolada de curta duração.

Exemplo:

```text
█████████▌
```

Normalmente representa um pico rápido.

---

## Clipping Repetitivo

Ocorrências sucessivas em curto intervalo de tempo.

Esse comportamento pode indicar necessidade de ajuste de ganho.

---

## Clipping Contínuo

Quando o canal permanece constantemente saturado.

Essa situação exige atenção imediata do operador.

---

# Exibição na Interface

Quando um clipping for detectado, o Console poderá apresentar um indicador visual.

Exemplos:

- indicador vermelho;
- aviso de clipping;
- contador de ocorrências.

A forma de apresentação será definida nas Sprints de Interface.

---

# Integração com a Inteligência Artificial

O Clip Detector fornecerá informações importantes para a IA.

Exemplos:

```text
Canal 05

↓

5 clippings em 30 segundos

↓

IA identifica padrão

↓

Sugestão:

Reduzir o ganho em 2 dB.
```

Outro exemplo:

```text
Violão

↓

Clipping recorrente

↓

IA sugere revisar o ganho de entrada.
```

A decisão final permanecerá sempre sob responsabilidade do operador.

---

# Integração com o Histórico

Todas as ocorrências poderão ser registradas para:

- auditoria;
- análise técnica;
- relatórios do evento;
- comparação entre eventos.

Esses registros poderão auxiliar na identificação de problemas recorrentes.

---

# Eventos Produzidos

Sempre que um clipping for detectado, o componente poderá publicar eventos como:

- ChannelClipDetected
- ClipStarted
- ClipEnded
- ClipCounterUpdated

Esses eventos serão distribuídos através do Event Bus.

---

# Contador de Ocorrências

Cada canal poderá manter um contador de clipping durante o evento.

Exemplo:

```text
Canal 05

Clipping:

7 ocorrências
```

Esses contadores poderão ser reiniciados:

- no início de um novo evento;
- por comando do operador;
- ao carregar um novo snapshot.

---

# Integração com Outros Componentes

O Clip Detector trabalha em conjunto com:

- Audio Levels;
- Peak Detector;
- Statistics;
- Painel da IA.

Cada componente possui uma responsabilidade específica.

---

# Benefícios

A utilização do Clip Detector oferece diversas vantagens:

- preserva a qualidade do áudio;
- reduz distorções durante o evento;
- auxilia no ajuste correto dos ganhos;
- fornece informações para a IA;
- facilita a identificação de problemas;
- melhora a experiência do operador.

---

# Separação de Responsabilidades

O Clip Detector possui uma única responsabilidade.

Ele não:

- calcula níveis de áudio;
- controla medidores;
- detecta silêncio;
- altera parâmetros da mesa;
- envia comandos para a Ui24R.

Sua função é exclusivamente detectar e registrar ocorrências de clipping.

---

# Evoluções Futuras

Nas próximas versões, o Clip Detector poderá incorporar funcionalidades como:

- classificação da severidade do clipping;
- identificação de clipping recorrente por participante;
- geração de estatísticas por canal;
- análise de tendências durante o evento;
- integração com modelos de aprendizado da IA para prevenção automática de saturação.

---

# Situação da Sprint

**Status:** ✅ Concluída