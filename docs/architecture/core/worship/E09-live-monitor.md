# Sprint E09 – Live Monitor

## Objetivo

Definir o componente responsável pelo monitoramento contínuo da operação durante a execução do culto, detectando situações que possam comprometer a qualidade do áudio ou a estabilidade da mesa de som.

O **Live Monitor** é o sistema de vigilância operacional do Audio Copilot. Ele acompanha, em tempo real, todos os indicadores relevantes da mesa digital, correlacionando informações da telemetria, da liturgia e do estado atual da sessão para identificar riscos e fornecer dados aos demais componentes.

Enquanto o **Telemetry Manager** coleta métricas de baixo nível e o **Peak Detector**, **Clip Detector** e **Silence Detector** identificam eventos específicos, o Live Monitor consolida essas informações para produzir uma visão operacional do culto.

---

# Visão Geral

Durante um culto, dezenas de parâmetros mudam continuamente.

Exemplos:

- níveis dos canais;
- clipping;
- headroom;
- silêncio inesperado;
- canais sem sinal;
- snapshots carregados;
- mudanças de liturgia;
- utilização dos auxiliares.

O operador não consegue acompanhar todos esses indicadores simultaneamente.

O Live Monitor faz esse acompanhamento continuamente.

---

# Filosofia

O Live Monitor foi desenvolvido seguindo cinco princípios.

## Monitoramento Contínuo

A análise deve ocorrer durante toda a execução do culto.

---

## Baixa Latência

Eventos críticos devem ser identificados rapidamente.

---

## Contextualização

Toda análise deve considerar o momento atual da liturgia.

---

## Priorização

Apenas situações relevantes devem gerar ações.

---

## Confiabilidade

O monitoramento deve ser preciso e produzir poucos falsos positivos.

---

# Arquitetura

```text
Mesa Ui24R

↓

Telemetry Manager

↓

Live Monitor

├── Níveis
├── Clipping
├── Silêncio
├── Headroom
├── Snapshots
├── Estado dos Canais
├── Contexto da Liturgia
└── Indicadores Operacionais

↓

Alert Manager

↓

Live Assistant
```

---

# Responsabilidades

O Live Monitor será responsável por:

- monitorar continuamente o sistema;
- consolidar informações da telemetria;
- detectar situações críticas;
- avaliar a estabilidade da operação;
- fornecer contexto ao Alert Manager;
- alimentar o Dashboard Operacional.

---

# Fluxo Geral

```text
Receber Telemetria

↓

Analisar Contexto

↓

Detectar Situações

↓

Classificar Prioridade

↓

Notificar Componentes
```

---

# Fontes de Informação

O Live Monitor poderá utilizar dados provenientes de:

- Telemetry Manager;
- Peak Detector;
- Clip Detector;
- Silence Detector;
- Statistics;
- Meter Cache;
- Live Session;
- Worship Manager.

---

# Monitoramento dos Canais

Cada canal poderá ser acompanhado continuamente.

Exemplos:

- nível atual;
- pico máximo;
- headroom disponível;
- estado do mute;
- phantom power;
- atividade de áudio;
- clipping.

---

# Monitoramento da Mixagem

Além dos canais individuais, o sistema acompanhará indicadores globais.

Exemplos:

- Main LR;
- Subgrupos;
- DCAs;
- Auxiliares;
- Matriz;
- saídas de gravação.

---

# Monitoramento da Liturgia

O comportamento esperado varia conforme a etapa do culto.

Exemplo:

```text
Pregação

↓

Microfone do Pastor

↓

Alta prioridade
```

Ou:

```text
Louvor

↓

Playback

↓

Monitoramento reforçado
```

O Live Monitor adapta sua análise ao contexto atual.

---

# Monitoramento de Clipping

O componente acompanhará continuamente situações de saturação.

Exemplo:

```text
Canal 07

↓

Clipping

↓

Persistente

↓

Alerta
```

Pequenos picos isolados poderão ser ignorados, conforme as regras do Alert Manager.

---

# Monitoramento de Silêncio

Também será possível identificar ausência inesperada de sinal.

Exemplo:

```text
Pastor falando

↓

Microfone sem áudio

↓

Gerar Evento
```

---

# Monitoramento de Headroom

O sistema poderá acompanhar a margem disponível antes da saturação.

Exemplo:

```text
Canal

↓

Headroom

↓

3 dB

↓

Situação de Atenção
```

---

# Monitoramento dos Snapshots

O Live Monitor verificará:

- snapshot esperado;
- snapshot carregado;
- atrasos na troca;
- inconsistências.

Exemplo:

```text
Pregação

↓

Snapshot Louvor

↓

Possível erro
```

---

# Avaliação da Estabilidade

O componente poderá calcular um indicador geral de estabilidade.

Exemplo:

```text
Poucos Ajustes

↓

Sem Clipping

↓

Sem Alertas

↓

Estabilidade Alta
```

Esse indicador poderá ser utilizado pelo Dashboard.

---

# Classificação das Situações

Cada ocorrência poderá receber um nível de prioridade.

Exemplo:

```text
Informação

↓

Atenção

↓

Importante

↓

Crítica
```

Essa classificação será utilizada pelo Alert Manager.

---

# Integração com o Alert Manager

O Live Monitor não apresenta alertas diretamente.

Seu fluxo é:

```text
Detectar

↓

Classificar

↓

Enviar

↓

Alert Manager

↓

Operador
```

Essa separação reduz notificações desnecessárias.

---

# Integração com o Live Assistant

O Live Assistant utilizará os eventos produzidos pelo Live Monitor para gerar sugestões contextuais.

Exemplo:

```text
Headroom Baixo

↓

Live Assistant

↓

Sugerir redução de ganho
```

---

# Integração com a IA

Os dados produzidos poderão alimentar:

- Recommendation Engine;
- Decision Engine;
- Confidence Engine;
- Safety Engine.

A IA utilizará essas informações para produzir recomendações mais precisas.

---

# Integração com o Histórico

Eventos relevantes identificados pelo Live Monitor poderão ser registrados automaticamente.

Exemplos:

- clipping persistente;
- perda de sinal;
- excesso de ganho;
- snapshots incorretos.

---

# Integração com o Dashboard

O Dashboard poderá apresentar indicadores como:

- estado geral da operação;
- canais em atenção;
- headroom médio;
- clipping ativo;
- canais silenciosos;
- estabilidade da sessão.

---

# Benefícios

O Live Monitor proporciona:

- supervisão contínua da operação;
- detecção precoce de problemas;
- maior estabilidade durante o culto;
- suporte inteligente ao operador;
- melhor contextualização das recomendações da IA;
- redução do risco de falhas operacionais.

---

# Separação de Responsabilidades

O Live Monitor não:

- gera alertas diretamente;
- altera configurações da mesa;
- toma decisões operacionais;
- aprende padrões;
- controla a liturgia.

Sua responsabilidade é monitorar continuamente a operação, consolidar informações técnicas e fornecer uma visão contextualizada do estado do culto para os demais componentes do Audio Copilot.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- monitoramento preditivo de clipping;
- identificação automática de feedback;
- análise da inteligibilidade da fala;
- detecção de ruído ambiente;
- reconhecimento de instrumentos ativos;
- monitoramento da transmissão ao vivo;
- análise de estabilidade por canal;
- indicadores avançados de saúde operacional.

---

# Relação com Outros Componentes

O Live Monitor trabalha diretamente com:

- Worship Manager;
- Live Session;
- Telemetry Manager;
- Peak Detector;
- Clip Detector;
- Silence Detector;
- Statistics;
- Meter Cache;
- Alert Manager;
- Live Assistant;
- Recommendation Engine;
- Dashboard Operacional;
- Console Operacional.

Ele representa a camada de supervisão em tempo real do Modo Culto, acompanhando continuamente a operação da mesa de som, consolidando dados técnicos e contextuais para detectar situações relevantes e fornecer informações confiáveis aos módulos responsáveis por alertas, recomendações e assistência ao operador.

---

# Situação da Sprint

**Status:** ✅ Concluída