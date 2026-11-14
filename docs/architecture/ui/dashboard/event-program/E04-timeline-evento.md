# Sprint E04 – Timeline do Evento

## Objetivo

Definir o componente responsável por representar visualmente a evolução do evento, permitindo que o operador acompanhe, em tempo real, quais etapas já foram concluídas, qual etapa está em execução e quais etapas ainda serão realizadas.

A Timeline do Evento fornece contexto operacional para toda a aplicação e serve como referência para o Dashboard, Console de Operação, Painel da IA e aplicativo Mobile.

---

# Visão Geral

A Timeline do Evento representa o roteiro completo do culto ou ensaio.

Ela organiza todas as etapas da programação em sequência cronológica, facilitando o acompanhamento do evento e reduzindo a necessidade de o operador consultar a programação técnica durante a operação.

Além de informar o andamento do evento, a Timeline também fornece contexto para que a Inteligência Artificial compreenda quais participantes, instrumentos e microfones devem estar ativos em cada momento.

---

# Filosofia

A Timeline não controla o andamento do evento.

Ela representa visualmente o estado atual da programação.

O operador continua sendo responsável por confirmar o avanço entre as etapas.

Em versões futuras, o sistema poderá sugerir automaticamente o avanço da Timeline, mas a confirmação permanecerá sob responsabilidade do operador.

---

# Estrutura da Timeline

Cada evento será composto por uma sequência ordenada de etapas.

Exemplo:

```text
✓ Recepção

✓ Oração Inicial

► Louvor

○ Avisos

○ Oferta

○ Pregação

○ Ceia

○ Encerramento
```

Cada etapa poderá assumir apenas um estado por vez.

---

# Estados da Timeline

Cada etapa poderá possuir um dos seguintes estados.

## Aguardando

A etapa ainda não foi iniciada.

Representação:

```text
○ Avisos
```

---

## Em Execução

Representa a etapa atualmente em andamento.

Representação:

```text
► Louvor
```

Apenas uma etapa poderá permanecer ativa simultaneamente.

---

## Concluída

Indica que a etapa foi finalizada.

Representação:

```text
✓ Oração Inicial
```

As etapas concluídas permanecem registradas até o encerramento do evento.

---

# Informações da Etapa

Cada etapa poderá apresentar informações complementares.

Exemplo:

```text
Louvor

Música 3 de 5

Tempo previsto:
20 min

Tempo decorrido:
12 min
```

Essas informações ajudam o operador a acompanhar o andamento do evento.

---

# Navegação

O operador poderá navegar livremente pela Timeline.

Será possível:

- visualizar etapas futuras;
- consultar etapas anteriores;
- retornar à etapa atual rapidamente.

Essa navegação não altera automaticamente o estado da operação.

---

# Avanço das Etapas

O avanço da Timeline ocorrerá mediante confirmação do operador.

Fluxo:

```text
Etapa atual

↓

Finalizada

↓

Operador confirma

↓

Próxima etapa torna-se ativa
```

Esse comportamento evita mudanças acidentais durante o evento.

---

# Alteração Manual

Caso necessário, o operador poderá retornar para uma etapa anterior ou avançar diretamente para outra etapa.

Exemplos:

- repetir uma música;
- cancelar uma etapa;
- alterar a ordem da programação;
- adaptar a liturgia durante o culto.

Todas essas alterações poderão ser registradas no Histórico do Evento.

---

# Integração com o Console

O Console de Operação utilizará a etapa atual da Timeline para destacar os canais mais relevantes.

Exemplo:

Durante o Louvor:

- vocais em destaque;
- instrumentos em destaque.

Durante a Pregação:

- Pastor em destaque;
- Púlpito em destaque.

Essa integração reduz distrações e melhora a experiência do operador.

---

# Integração com a Inteligência Artificial

A Timeline fornece contexto operacional para a IA.

Exemplo:

```text
Etapa Atual

Pregação
```

A IA passa a esperar atividade principalmente nos canais do:

- Pastor;
- Púlpito;
- Microfone sem fio.

Caso um instrumento permaneça emitindo sinal continuamente, a IA poderá sugerir uma verificação.

Outro exemplo:

```text
Etapa

Louvor
```

A IA passa a considerar normal a atividade dos instrumentos e vocais.

---

# Integração com o Dashboard

O Dashboard apresentará uma versão resumida da Timeline.

Exemplo:

```text
Culto Domingo Manhã

Agora

Louvor

Próximo

Avisos
```

Essa informação permanecerá sempre visível.

---

# Integração com o Mobile

O aplicativo Mobile apresentará uma versão simplificada.

Exemplo:

```text
Agora

Pregação

Próximo

Ceia

Tempo restante

18 minutos
```

---

# Benefícios

A utilização da Timeline oferece diversas vantagens:

- visão clara do andamento do evento;
- melhor organização da operação;
- redução da carga cognitiva do operador;
- integração entre programação e operação;
- contexto operacional para a IA;
- facilidade para adaptação da liturgia.

---

# Separação de Responsabilidades

A Timeline possui responsabilidade única.

Ela não:

- controla a mesa de som;
- altera configurações;
- envia comandos para a Ui24R;
- executa análises de áudio;
- controla a IA.

Sua função é representar visualmente a evolução do evento.

---

# Evoluções Futuras

Nas próximas versões, a Timeline poderá incorporar funcionalidades como:

- avanço automático mediante confirmação do operador;
- cronômetro individual por etapa;
- comparação entre tempo previsto e tempo realizado;
- sincronização com softwares de apresentação;
- exibição de observações específicas por etapa;
- marcação de eventos importantes durante o culto;
- sugestões inteligentes de transição entre etapas.

---

# Relação com Outros Componentes

A Timeline trabalha em conjunto com:

- Painel da Liturgia;
- Participantes;
- Músicas;
- Progresso do Evento;
- Painel da IA;
- Dashboard Operacional.

Esses componentes utilizam a etapa atual para fornecer uma experiência integrada ao operador.

---

# Situação da Sprint

**Status:** ✅ Concluída