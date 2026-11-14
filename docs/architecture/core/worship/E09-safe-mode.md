# Sprint E09 – Safe Mode

## Objetivo

Definir o componente responsável por garantir que o Audio Copilot opere de forma segura durante cultos e eventos ao vivo, reduzindo riscos operacionais e impedindo que recomendações, notificações ou comportamentos da Inteligência Artificial interfiram negativamente na condução da operação.

O **Safe Mode** representa a camada de segurança operacional do Audio Copilot. Seu objetivo é proteger o operador durante os momentos mais críticos, priorizando estabilidade em vez de experimentação.

Enquanto o **Recommendation Engine** produz sugestões e o **Alert Manager** administra notificações, o Safe Mode determina quando essas ações podem ou não ser apresentadas ao operador.

---

# Visão Geral

Durante um culto, qualquer distração pode causar problemas.

Exemplos:

- perder a entrada do pastor;
- atrasar uma troca de snapshot;
- aumentar o clipping;
- esquecer um canal aberto;
- interromper a concentração do operador.

Por esse motivo, durante o Modo Culto a IA deve se tornar muito mais conservadora.

O Safe Mode controla exatamente esse comportamento.

---

# Filosofia

O Safe Mode foi desenvolvido seguindo cinco princípios.

## Segurança

A estabilidade da operação sempre possui prioridade máxima.

---

## Conservadorismo

Na dúvida, o sistema deve interferir menos.

---

## Não Intrusão

A IA nunca deve competir com a atenção do operador.

---

## Controle

O operador continua sendo o responsável por todas as decisões.

---

## Confiabilidade

Somente recomendações altamente confiáveis devem chegar ao operador.

---

# Arquitetura

```text
Recommendation Engine

↓

Decision Engine

↓

Confidence Engine

↓

Safe Mode

├── Avaliação
├── Restrições
├── Priorização
├── Supressão
└── Liberação

↓

Live Assistant

↓

Operador
```

---

# Responsabilidades

O Safe Mode será responsável por:

- controlar o comportamento da IA durante o culto;
- reduzir distrações;
- bloquear recomendações inadequadas;
- validar notificações críticas;
- proteger a estabilidade operacional;
- definir o nível de intervenção da IA.

---

# Fluxo Geral

```text
Nova Recomendação

↓

Avaliar Contexto

↓

Verificar Segurança

↓

Permitir

ou

Bloquear

↓

Operador
```

---

# Quando o Safe Mode Atua

O componente permanece ativo durante:

- cultos;
- conferências;
- congressos;
- eventos ao vivo;
- gravações;
- transmissões.

Sempre que a estabilidade for mais importante que o aprendizado.

---

# Situações Avaliadas

O Safe Mode poderá considerar:

- etapa da liturgia;
- criticidade do evento;
- confiança da IA;
- quantidade de alertas ativos;
- carga de trabalho do operador;
- proximidade de transições importantes.

---

# Controle das Recomendações

Nem toda recomendação deverá ser apresentada.

Exemplo:

```text
Sugestão

↓

Ajustar EQ

↓

Safe Mode

↓

Bloquear
```

Porque naquele momento o operador está acompanhando a entrada do pastor.

---

Outro exemplo:

```text
Clipping Persistente

↓

Safe Mode

↓

Permitir
```

Pois representa um risco real para o áudio.

---

# Controle das Notificações

O Safe Mode poderá limitar a quantidade de mensagens exibidas.

Exemplo:

```text
Cinco eventos

↓

Mesmo problema

↓

Uma única notificação
```

Isso reduz a sobrecarga cognitiva do operador.

---

# Controle por Etapa da Liturgia

Cada etapa poderá possuir regras diferentes.

## Antes do Culto

A IA poderá sugerir:

- ajustes;
- melhorias;
- verificações.

---

## Durante o Louvor

Apenas recomendações importantes.

---

## Durante a Pregação

Somente alertas críticos.

---

## Encerramento

A IA poderá voltar a fornecer recomendações operacionais.

---

# Níveis de Segurança

O Safe Mode poderá operar em diferentes níveis.

```text
Normal

↓

Conservador

↓

Restritivo

↓

Máxima Segurança
```

Cada perfil controla o grau de intervenção permitido.

---

# Exemplo

Durante a pregação:

```text
Sugestão

↓

Aumentar Reverb

↓

Safe Mode

↓

Bloquear
```

Durante um ensaio:

```text
Sugestão

↓

Aumentar Reverb

↓

Safe Mode

↓

Permitir
```

O mesmo evento produz comportamentos diferentes dependendo do contexto.

---

# Avaliação da Confiança

O componente utilizará o nível de confiança produzido pela IA.

Exemplo:

```text
Confiança

98%

↓

Permitir
```

Ou:

```text
Confiança

61%

↓

Bloquear
```

Os limites poderão ser configuráveis.

---

# Priorização

Caso existam vários eventos simultâneos:

```text
Feedback

↓

Clipping

↓

Canal Sem Sinal

↓

Organizar Prioridade
```

O operador receberá apenas o mais importante.

---

# Supressão Inteligente

Alertas repetitivos poderão ser ocultados temporariamente.

Exemplo:

```text
Mesmo clipping

↓

30 ocorrências

↓

Uma notificação
```

Caso o problema persista por muito tempo, um novo alerta poderá ser emitido.

---

# Modo Emergência

Em situações críticas, o Safe Mode poderá alterar temporariamente seu comportamento.

Exemplo:

```text
Perda do Microfone Principal

↓

Modo Emergência

↓

Prioridade Máxima
```

Nesse estado, recomendações menos importantes serão suspensas até que a situação crítica seja resolvida.

---

# Integração com o Live Assistant

O Safe Mode controla quais mensagens chegam ao Live Assistant.

Fluxo:

```text
IA

↓

Safe Mode

↓

Live Assistant

↓

Operador
```

---

# Integração com o Alert Manager

O Alert Manager produzirá os alertas.

O Safe Mode decidirá se:

- devem ser exibidos;
- devem ser adiados;
- devem ser agrupados;
- devem ser ignorados.

---

# Integração com o Decision Engine

Antes de qualquer recomendação chegar ao operador:

```text
Decision Engine

↓

Safe Mode

↓

Validar Segurança
```

---

# Integração com o Confidence Engine

A confiança da IA influencia diretamente a atuação do Safe Mode.

Quanto menor a confiança, maior será a tendência de bloquear recomendações.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- nível atual do Safe Mode;
- quantidade de recomendações bloqueadas;
- alertas liberados;
- alertas suprimidos;
- perfil operacional ativo.

---

# Benefícios

O Safe Mode proporciona:

- maior segurança operacional;
- redução de distrações;
- menor risco durante o culto;
- recomendações mais confiáveis;
- melhor experiência para o operador;
- maior estabilidade da operação.

---

# Separação de Responsabilidades

O Safe Mode não:

- monitora áudio;
- detecta clipping;
- aprende padrões;
- gera recomendações;
- controla a liturgia.

Sua responsabilidade é avaliar o contexto operacional e decidir quais recomendações e notificações podem ser apresentadas ao operador sem comprometer a condução do culto.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- adaptação automática ao perfil do operador;
- níveis de segurança personalizados por igreja;
- detecção automática de momentos críticos da liturgia;
- perfis específicos para transmissões ao vivo;
- integração com múltiplos operadores;
- bloqueio inteligente baseado em aprendizado contínuo;
- ajuste dinâmico da sensibilidade conforme a carga operacional;
- políticas configuráveis de segurança por evento.

---

# Relação com Outros Componentes

O Safe Mode trabalha diretamente com:

- Modo Culto;
- Worship Manager;
- Live Session;
- Live Monitor;
- Alert Manager;
- Live Assistant;
- Recommendation Engine;
- Decision Engine;
- Confidence Engine;
- Context Manager;
- History Manager;
- Dashboard Operacional;
- Console Operacional.

Ele representa a camada de proteção operacional do Audio Copilot, garantindo que toda interação da Inteligência Artificial durante o culto seja segura, contextualizada e não intrusiva, preservando a estabilidade da operação e mantendo o operador sempre no controle das decisões.

---

# Situação da Sprint

**Status:** ✅ Concluída