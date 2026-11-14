# Sprint E05 – Decision Engine

## Objetivo

Definir o componente responsável por decidir quais recomendações da Inteligência Artificial devem ser apresentadas ao operador, em qual momento e com qual prioridade.

O Decision Engine atua como o filtro inteligente entre o Recommendation Engine e a interface do usuário.

Seu objetivo é evitar excesso de informações, reduzir distrações e garantir que apenas recomendações realmente relevantes sejam exibidas durante a operação.

---

# Visão Geral

Nem toda recomendação produzida pela IA deve chegar ao operador.

Durante um culto, centenas de análises poderão ser realizadas por minuto.

Sem um mecanismo de decisão, o operador seria constantemente interrompido por notificações, reduzindo sua capacidade de concentração.

O Decision Engine existe justamente para decidir:

- esta recomendação deve aparecer?
- agora é o momento certo?
- ela possui prioridade suficiente?
- existe outra recomendação semelhante?
- ela já foi apresentada anteriormente?

---

# Filosofia

O Decision Engine segue quatro princípios fundamentais.

## Prioridade

O operador deve visualizar primeiro aquilo que realmente importa.

---

## Oportunidade

Uma recomendação útil no momento errado deixa de ser útil.

---

## Redução de Ruído

A IA deve falar pouco.

Quando falar, deve agregar valor.

---

## Não Interrupção

A operação da mesa possui prioridade sobre qualquer recomendação.

A IA nunca deve competir pela atenção do operador.

---

# Arquitetura

```text
Recommendation Engine

↓

Decision Engine

↓

Confidence Engine

↓

Rule Engine

↓

Safety Engine

↓

Painel da IA

↓

Console

↓

Operador
```

O Decision Engine representa a última etapa antes da exibição da recomendação.

---

# Responsabilidades

O Decision Engine será responsável por:

- avaliar cada recomendação recebida;
- eliminar recomendações redundantes;
- definir prioridade;
- decidir o melhor momento para exibição;
- agrupar recomendações semelhantes;
- evitar notificações repetidas;
- encaminhar apenas recomendações relevantes ao operador.

---

# Fluxo de Decisão

```text
Nova Recomendação

↓

Já existe recomendação semelhante?

↓

Sim

↓

Atualizar existente

↓

Não

↓

Calcular prioridade

↓

Avaliar contexto

↓

Enviar para interface
```

---

# Critérios de Decisão

Cada recomendação será analisada considerando diversos fatores.

Entre eles:

- contexto atual;
- modo de operação;
- etapa da liturgia;
- confiança da IA;
- frequência da ocorrência;
- gravidade do problema;
- histórico recente;
- impacto operacional.

---

# Priorização

As recomendações serão classificadas em quatro níveis.

## Informativa

Não exige ação.

Exemplo:

```text
Próxima etapa:

Pregação.
```

---

## Atenção

Merece acompanhamento.

Exemplo:

```text
O canal do Violão apresenta nível abaixo do habitual.
```

---

## Alerta

Requer intervenção provável.

Exemplo:

```text
Início de microfonia detectado.
```

---

## Crítica

Pode comprometer o evento.

Exemplo:

```text
Clipping contínuo no Master.
```

---

# Controle de Frequência

O mesmo problema não deverá gerar notificações repetidas.

Exemplo:

```text
09:32

Feedback detectado.
```

Caso o problema continue pelos próximos segundos, a IA apenas atualizará o alerta existente.

Ela não criará dezenas de novas mensagens.

---

# Agrupamento

Problemas semelhantes poderão ser agrupados.

Exemplo:

Ao invés de:

```text
Monitor 1

Feedback.

Monitor 2

Feedback.

Monitor 3

Feedback.
```

A IA poderá apresentar:

```text
Feedback detectado em três monitores.
```

Isso reduz significativamente a poluição visual.

---

# Janela de Observação

Antes de gerar um alerta, o Decision Engine poderá aguardar alguns instantes.

Exemplo:

Um pico de clipping com duração de 30 milissegundos provavelmente não exige intervenção.

Já um clipping contínuo durante vários segundos merece uma recomendação.

Essa janela evita falsos positivos.

---

# Supressão Inteligente

Algumas recomendações deixam de fazer sentido dependendo do contexto.

Exemplo:

Durante um ensaio.

```text
Instrumentos alternando entre silêncio e atividade.
```

Situação esperada.

Nenhum alerta será apresentado.

---

Outro exemplo:

Durante a troca de microfones.

```text
Canal sem sinal.
```

Também esperado.

---

# Atualização de Recomendações

As recomendações permanecem vivas.

Exemplo:

```text
09:40

Feedback detectado.

↓

09:41

Situação estabilizada.

↓

Recomendação encerrada.
```

O operador percebe claramente quando um problema foi resolvido.

---

# Expiração

Toda recomendação possui um ciclo de vida.

```text
Criada

↓

Ativa

↓

Atualizada

↓

Resolvida

↓

Arquivada
```

Isso mantém a interface sempre limpa.

---

# Integração com o Confidence Engine

Antes da exibição, cada recomendação recebe um índice de confiança.

Exemplo:

```text
Confiança

98%
```

Recomendações com baixa confiança poderão ser ocultadas ou rebaixadas de prioridade.

---

# Integração com o Rule Engine

O Decision Engine respeita todas as regras definidas pelo sistema.

Exemplo:

Mesmo detectando uma situação incomum, uma recomendação poderá ser bloqueada caso viole alguma política operacional.

---

# Integração com o Safety Engine

O Safety Engine impede que recomendações potencialmente perigosas sejam apresentadas como sugestões automáticas.

Exemplo:

Nunca recomendar:

- mutar o Pastor;
- desligar o PA;
- alterar o Master;
- aumentar drasticamente o ganho.

---

# Integração com o Explanation Engine

Toda recomendação aprovada receberá uma explicação clara.

Exemplo:

```text
Sugestão

Reduzir aproximadamente 2 dB no Monitor.

Motivo

Foi identificado aumento progressivo da energia em 2,5 kHz, indicando início de microfonia.
```

---

# Integração com o Dashboard

O Dashboard exibirá apenas um resumo.

Exemplo:

```text
IA

Tudo normal.
```

ou

```text
IA

2 recomendações pendentes.
```

---

# Integração com o Console

No Console Operacional, recomendações críticas poderão destacar visualmente o canal relacionado.

Exemplo:

```text
Canal 08

Feedback detectado.
```

O canal poderá receber uma borda vermelha ou animação discreta para facilitar sua localização.

---

# Registro das Decisões

Toda decisão tomada pelo Decision Engine poderá ser registrada.

Exemplo:

```text
09:41

Recomendação gerada.

↓

Exibida.

↓

Aceita pelo operador.

↓

Resolvida.
```

Esses registros serão utilizados pelo Learning Engine para aperfeiçoar futuras decisões.

---

# Benefícios

O Decision Engine proporciona:

- redução da sobrecarga de informações;
- menor distração durante o evento;
- priorização inteligente;
- eliminação de notificações repetidas;
- recomendações mais relevantes;
- melhor experiência para o operador.

---

# Separação de Responsabilidades

O Decision Engine não:

- cria recomendações;
- aprende padrões;
- altera a mesa de som;
- executa comandos;
- modifica configurações.

Sua única responsabilidade é decidir quando, como e quais recomendações devem ser apresentadas ao operador.

---

# Evoluções Futuras

O componente poderá evoluir para incluir:

- priorização personalizada por operador;
- adaptação ao perfil de cada igreja;
- ajuste automático da sensibilidade;
- agrupamento inteligente baseado em IA;
- priorização conforme a etapa da liturgia;
- classificação automática por impacto operacional.

---

# Relação com Outros Componentes

O Decision Engine trabalha diretamente com:

- Recommendation Engine;
- Context Manager;
- Confidence Engine;
- Rule Engine;
- Safety Engine;
- Explanation Engine;
- Learning Engine;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA.

Ele representa o filtro inteligente da IA Operacional, garantindo que apenas recomendações relevantes, oportunas e contextualizadas cheguem ao operador.

---

# Situação da Sprint

**Status:** ✅ Concluída