# Sprint E05 – IA Operacional

## Objetivo

Definir a arquitetura da Inteligência Artificial Operacional do Audio Copilot.

A IA Operacional é o núcleo inteligente da aplicação. Ela recebe informações de toda a plataforma, interpreta o contexto do evento, analisa a operação da mesa de som em tempo real e oferece recomendações ao operador.

Diferentemente de um sistema de automação, a IA do Audio Copilot não controla a mesa de som de forma autônoma. Sua função é atuar como um copiloto, auxiliando o operador com informações, sugestões e alertas contextualizados.

---

# Visão Geral

A Inteligência Artificial é responsável por transformar dados em conhecimento operacional.

Enquanto outros módulos apenas armazenam ou exibem informações, a IA interpreta esses dados para responder perguntas como:

- O que está acontecendo agora?
- Esse comportamento é esperado?
- Existe algum risco?
- Vale a pena alertar o operador?
- Existe alguma recomendação útil neste momento?

A resposta para essas perguntas é apresentada ao operador por meio do Painel da IA e integrada ao Console Operacional.

---

# Filosofia

A Inteligência Artificial do Audio Copilot foi projetada seguindo cinco princípios fundamentais.

## Assistir

A IA auxilia o operador.

Nunca o substitui.

---

## Explicar

Toda recomendação deverá possuir uma justificativa clara.

O operador deve entender por que determinada sugestão foi apresentada.

---

## Aprender

A IA aprende continuamente com os eventos realizados.

Cada culto, ensaio ou evento contribui para tornar as recomendações futuras mais precisas.

---

## Respeitar

A decisão final sempre pertence ao operador.

Nenhuma ação operacional crítica será executada automaticamente.

---

## Evoluir

A arquitetura foi projetada para permitir a incorporação de novos modelos de IA sem alterar os demais componentes da aplicação.

---

# Arquitetura

A IA Operacional é composta por diversos módulos especializados.

```text
IA Operacional

├── Context Manager
├── Recommendation Engine
├── Decision Engine
├── Learning Engine
├── Confidence Engine
├── Rule Engine
├── Safety Engine
└── Explanation Engine
```

Cada módulo possui uma responsabilidade específica.

---

# Fluxo Geral

O funcionamento da IA pode ser representado pelo fluxo abaixo.

```text
Telemetria

↓

State Manager

↓

Painel da Liturgia

↓

Configuração do Evento

↓

Histórico

↓

IA Operacional

↓

Recomendações

↓

Operador
```

Toda análise parte do contexto atual do evento.

---

# Fontes de Informação

A IA utiliza informações provenientes de diversos componentes da aplicação.

Entre elas:

- Telemetria da Ui24R;
- Estado Global;
- Painel da Liturgia;
- Timeline;
- Participantes;
- Músicas;
- Configuração do Evento;
- Histórico de Alterações;
- Estatísticas;
- Preferências do Operador.

Quanto maior o contexto disponível, mais precisas tendem a ser as recomendações.

---

# Tipos de Análise

A IA poderá realizar diferentes categorias de análise.

## Análise Técnica

Avalia:

- clipping;
- silêncio inesperado;
- picos de áudio;
- feedback;
- canais sem atividade;
- níveis inconsistentes.

---

## Análise Operacional

Verifica:

- etapa atual da liturgia;
- participantes esperados;
- instrumentos ativos;
- microfones previstos;
- progresso do evento.

---

## Análise Histórica

Compara a operação atual com eventos anteriores.

Exemplo:

```text
Durante a Pregação,
o Pastor normalmente utiliza o
Microfone Sem Fio.

Hoje o canal permanece sem atividade.
```

---

## Análise Contextual

Combina simultaneamente:

- telemetria;
- liturgia;
- histórico;
- configuração;
- comportamento do operador.

Essa é a principal característica da IA Operacional.

---

# Recomendações

Sempre que identificar uma situação relevante, a IA poderá gerar uma recomendação.

Exemplo:

```text
Sugestão

Reduzir 2 dB no Monitor.

Motivo

Foi detectado início de microfonia.
```

Outro exemplo:

```text
Sugestão

Verificar bateria do Microfone Verde.

Motivo

Queda progressiva no nível do sinal.
```

---

# Recomendações Contextuais

A IA leva em consideração o momento do evento.

Exemplo:

Durante o Louvor.

```text
Playback esperado.

Sem sinal detectado.
```

Durante a Pregação.

```text
Instrumentos permanecem ativos.

Verificar canais.
```

A mesma condição pode gerar interpretações diferentes dependendo do contexto.

---

# Recomendações Proativas

Além de responder a problemas, a IA poderá antecipar necessidades.

Exemplo:

```text
Próxima etapa

Pregação

Sugestão

Destacar canais do Pastor.
```

Outro exemplo:

```text
Próxima música

Utiliza Playback.
```

---

# Interação com o Operador

O operador poderá:

- aceitar;
- ignorar;
- adiar;
- ocultar;
- aplicar manualmente a recomendação.

Todas essas ações poderão ser registradas para aprendizado futuro.

---

# Integração com o Console

O Console Operacional utilizará as recomendações para destacar informações importantes.

Exemplo:

```text
IA

Feedback detectado

Canal 12

Confiança

96%
```

---

# Integração com o Dashboard

O Dashboard apresentará apenas um resumo das recomendações.

Exemplo:

```text
IA

Tudo normal.

────────────

IA

1 recomendação pendente.
```

---

# Integração com o Mobile

No aplicativo Mobile serão exibidas apenas recomendações relevantes.

Exemplo:

```text
Microfone Verde

Sem sinal.

Verifique a bateria.
```

---

# Registro das Recomendações

Todas as sugestões poderão ser armazenadas.

Exemplo:

```text
09:32

Sugestão

Reduzir retorno.

Status

Aceita.

────────────

09:48

Sugestão

Verificar Playback.

Status

Ignorada.
```

Esses registros poderão alimentar relatórios e o processo de aprendizado da IA.

---

# Benefícios

A IA Operacional proporciona:

- auxílio contínuo ao operador;
- redução de erros operacionais;
- menor carga cognitiva;
- identificação antecipada de problemas;
- recomendações contextualizadas;
- aprendizado contínuo;
- maior padronização da operação.

---

# Separação de Responsabilidades

A IA Operacional não:

- altera automaticamente a Ui24R;
- movimenta faders;
- muda snapshots;
- executa cenas;
- inicia ou encerra etapas do evento;
- substitui decisões humanas.

Sua função é analisar, interpretar e recomendar.

---

# Evoluções Futuras

A arquitetura foi planejada para incorporar funcionalidades como:

- modelos locais de Inteligência Artificial;
- aprendizado específico por igreja;
- perfis personalizados por operador;
- detecção automática de feedback;
- previsão de clipping antes da ocorrência;
- identificação automática de instrumentos;
- reconhecimento de voz do pregador;
- geração automática de relatórios técnicos;
- análise preditiva da operação;
- integração com sistemas de iluminação, transmissão e projeção.

---

# Relação com Outros Componentes

A IA Operacional integra informações provenientes de praticamente toda a arquitetura do Audio Copilot.

Principais integrações:

- Telemetry Manager;
- State Manager;
- Dashboard Operacional;
- Painel da Liturgia;
- Timeline do Evento;
- Participantes;
- Músicas;
- Histórico de Alterações;
- Console Operacional;
- Mobile;
- Statistics.

Ela representa o principal componente inteligente da plataforma, transformando dados técnicos e contextuais em recomendações úteis para o operador.

---

# Situação da Sprint

**Status:** ✅ Concluída