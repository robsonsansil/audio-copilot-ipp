# Sprint E04 – Progresso do Evento

## Objetivo

Definir o componente responsável por acompanhar o andamento geral do evento, apresentando ao operador uma visão clara da evolução da programação, das etapas concluídas, da etapa atual e das atividades restantes.

O Progresso do Evento permite que toda a aplicação compartilhe uma única referência sobre o estado da operação, servindo como base para o Dashboard, Console de Operação, Painel da IA, Mobile e Relatórios.

---

# Visão Geral

Durante um culto ou ensaio, o operador precisa saber rapidamente:

- quanto do evento já foi realizado;
- qual etapa está em andamento;
- qual será a próxima etapa;
- quanto tempo já transcorreu;
- quanto tempo ainda resta.

O módulo de Progresso do Evento centraliza essas informações e mantém toda a aplicação sincronizada.

---

# Filosofia

O objetivo deste componente não é controlar o tempo do culto.

Cada igreja possui sua própria dinâmica, e nem sempre a programação acontece exatamente conforme o planejamento.

O Progresso do Evento funciona como um indicador de acompanhamento, auxiliando o operador sem impor um cronograma rígido.

---

# Arquitetura

Fluxo simplificado:

```text
Timeline do Evento

↓

Etapa Atual

↓

Progresso do Evento

↓

Dashboard

↓

Console

↓

Painel da IA

↓

Mobile

↓

Relatórios
```

O Progresso do Evento utiliza as informações da Timeline e das Transições para calcular o estado atual da programação.

---

# Responsabilidades

O módulo será responsável por:

- calcular o progresso geral do evento;
- identificar a etapa atual;
- identificar a próxima etapa;
- acompanhar o tempo decorrido;
- calcular o tempo estimado restante;
- disponibilizar essas informações para toda a aplicação.

---

# Indicadores de Progresso

O sistema poderá apresentar indicadores como:

- percentual do evento concluído;
- quantidade de etapas concluídas;
- etapa atual;
- próxima etapa;
- tempo decorrido;
- tempo restante estimado.

Exemplo:

```text
Culto Domingo Manhã

Progresso

68%

Etapas

6 de 9 concluídas

Agora

Pregação

Próxima

Santa Ceia

Tempo

01h12min
```

---

# Barra de Progresso

A interface poderá apresentar uma barra de progresso simples.

Exemplo:

```text
██████████████░░░░░░

68%
```

O objetivo é fornecer uma percepção rápida da evolução do evento.

---

# Tempo Decorrido

O sistema acompanhará automaticamente o tempo desde o início do evento.

Exemplo:

```text
Evento iniciado

09:00

Horário atual

10:12

Tempo decorrido

1h12min
```

Esse indicador é apenas informativo.

---

# Tempo Restante Estimado

Quando houver duração prevista para as etapas, o sistema poderá estimar o tempo restante.

Exemplo:

```text
Tempo restante

35 minutos
```

Caso não exista planejamento de duração, esse indicador poderá permanecer oculto.

---

# Progresso por Etapa

Além do progresso geral, cada etapa poderá apresentar sua própria evolução.

Exemplo:

```text
Pregação

Tempo previsto

40 minutos

Tempo decorrido

18 minutos
```

Esse acompanhamento auxilia o operador durante o evento.

---

# Integração com a Timeline

O Progresso do Evento é atualizado automaticamente sempre que ocorre uma transição.

Exemplo:

```text
Louvor

↓

Concluído

↓

Pregação

↓

Progresso atualizado
```

Toda a aplicação passa imediatamente a refletir a nova situação.

---

# Integração com o Dashboard

O Dashboard exibirá um resumo permanente.

Exemplo:

```text
Culto Domingo Manhã

68% concluído

Agora

Pregação

Próximo

Santa Ceia
```

Essa informação permanecerá sempre visível na tela principal.

---

# Integração com o Console

O Console poderá utilizar o progresso para contextualizar a operação.

Exemplo:

```text
Evento

68%

Etapa

Pregação
```

Assim, o operador mantém a percepção do andamento do culto sem precisar consultar outra tela.

---

# Integração com o Mobile

O aplicativo Mobile apresentará uma versão resumida.

Exemplo:

```text
Culto Domingo Manhã

68%

Agora

Pregação

Próximo

Santa Ceia
```

Essa visão é suficiente para acompanhamento remoto.

---

# Integração com a Inteligência Artificial

A IA utilizará o progresso para compreender em que momento do evento a operação se encontra.

Exemplo:

```text
Evento

95% concluído

Etapa

Encerramento
```

Nesse contexto, a IA poderá deixar de sugerir ajustes relevantes apenas para o início do culto, concentrando-se no encerramento da operação.

Outro exemplo:

```text
Evento

15%

Etapa

Louvor
```

A IA poderá antecipar recomendações para as próximas etapas, como avisos e pregação.

---

# Registro no Histórico

Sempre que houver alteração significativa no progresso, poderão ser registrados eventos como:

- início do evento;
- conclusão de etapa;
- mudança de etapa;
- encerramento do evento.

Essas informações poderão ser utilizadas em auditorias e relatórios.

---

# Benefícios

O módulo de Progresso do Evento proporciona diversas vantagens:

- visão clara da evolução do culto;
- sincronização entre todos os módulos;
- redução da carga cognitiva do operador;
- melhor contexto para a Inteligência Artificial;
- acompanhamento simples e intuitivo;
- base para relatórios operacionais.

---

# Separação de Responsabilidades

O Progresso do Evento possui responsabilidade única.

Ele não:

- controla a Timeline;
- altera etapas automaticamente;
- modifica configurações da mesa;
- executa comandos na Ui24R;
- processa sinais de áudio.

Sua função é representar o estado de evolução da programação.

---

# Evoluções Futuras

Nas próximas versões, o módulo poderá incorporar funcionalidades como:

- comparação entre tempo previsto e tempo realizado;
- estimativa dinâmica baseada no histórico da igreja;
- alertas de atraso em etapas críticas;
- indicadores específicos para ensaios e cultos;
- gráficos de duração das etapas;
- análise estatística do tempo médio de cada liturgia;
- previsões de término utilizando Inteligência Artificial.

---

# Relação com Outros Componentes

O módulo de Progresso do Evento trabalha em conjunto com:

- Painel da Liturgia;
- Timeline do Evento;
- Etapas da Liturgia;
- Transições;
- Dashboard Operacional;
- Console de Operação;
- Painel da IA;
- Mobile;
- Histórico de Alterações.

Ele representa o indicador oficial da evolução do evento, mantendo todos os módulos sincronizados com o andamento da programação.

---

# Situação da Sprint

**Status:** ✅ Concluída