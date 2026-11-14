# Sprint E04 – Participantes

## Objetivo

Definir o componente responsável por gerenciar os participantes envolvidos em cada etapa do evento.

O módulo de Participantes permite que o Audio Copilot saiba quem deverá estar atuando em cada momento da programação, quais recursos cada pessoa utilizará e quais canais da mesa estarão associados a ela.

Mais do que identificar pessoas, este componente fornece contexto operacional para toda a aplicação, permitindo que a Inteligência Artificial interprete corretamente o comportamento esperado de cada canal.

---

# Visão Geral

Durante um culto ou ensaio, cada participante desempenha uma função específica.

Exemplos:

- Pastor;
- Pregador convidado;
- Ministro de louvor;
- Vocal;
- Instrumentista;
- Operador de mídia;
- Técnico de áudio.

Cada participante pode utilizar um ou mais recursos durante o evento.

Exemplo:

```text
Robson

Funções

• Violão
• Vocal

Recursos

• Violão Martin
• Mic Verde

Canal

• CH09
• CH17
```

O sistema acompanha automaticamente essas associações ao longo de todo o evento.

---

# Filosofia

O Audio Copilot acompanha pessoas, não apenas equipamentos.

Embora a mesa de som opere por canais, quem realmente participa do evento são pessoas.

Ao conhecer quem está utilizando cada canal, a IA consegue compreender melhor o contexto operacional e oferecer recomendações mais inteligentes.

---

# Estrutura do Participante

Cada participante poderá conter informações como:

- nome;
- função;
- foto (opcional);
- recursos utilizados;
- canais associados;
- etapas em que participa;
- observações.

Exemplo:

```text
Nome

Robson

Funções

• Violão
• Vocal

Recursos

• Violão Martin
• Mic Verde

Etapas

• Louvor
• Encerramento
```

---

# Funções

Um participante poderá exercer mais de uma função durante o mesmo evento.

Exemplos:

```text
Robson

✓ Violão

✓ Vocal
```

Outro exemplo:

```text
Pastor João

✓ Pregador

✓ Avisos

✓ Oração Final
```

---

# Recursos Associados

Cada participante poderá utilizar diversos recursos.

Exemplo:

```text
Robson

Utiliza

• Violão Martin
• Mic Verde
```

Outro exemplo:

```text
Pastor

Utiliza

• Púlpito

• Microfone sem fio
```

Essas associações são definidas na Configuração do Evento (Sprint D06) e reutilizadas durante toda a operação.

---

# Participação por Etapa

Nem todos os participantes permanecem ativos durante todo o evento.

Exemplo:

```text
Louvor

Participantes

• Alessandra
• Letícia
• Robson
• João
```

Durante a pregação:

```text
Participantes

• Pastor
```

Essa informação permite que o sistema saiba quem realmente deve estar utilizando a mesa naquele momento.

---

# Estado do Participante

Cada participante poderá possuir um estado operacional.

Exemplos:

## Aguardando

Ainda não iniciou sua participação.

```text
○ Alessandra
```

---

## Ativo

Está participando da etapa atual.

```text
► Robson
```

---

## Concluído

Já finalizou sua participação.

```text
✓ João
```

---

## Ausente

Não participou conforme planejado.

```text
✕ Participante ausente
```

Esse estado poderá ser utilizado apenas para registro histórico.

---

# Informações Operacionais

O operador poderá visualizar rapidamente informações úteis.

Exemplo:

```text
Robson

Violão Martin

Mic Verde

Canal 09

Canal 17
```

Isso reduz o tempo gasto procurando informações durante o evento.

---

# Integração com a Inteligência Artificial

Os participantes fornecem contexto humano para a IA.

Exemplo:

```text
Etapa

Louvor

Participantes

• Alessandra
• Letícia
• Robson
```

A IA passa a esperar atividade apenas nos recursos associados a essas pessoas.

Caso um microfone pertencente a outro participante permaneça ativo, o sistema poderá sugerir:

> Foi detectado áudio no Microfone Amarelo, porém o participante associado não está previsto para esta etapa.

Outro exemplo:

```text
Pregação

Participante

Pastor
```

Se o microfone do Pastor permanecer completamente silencioso durante um longo período, a IA poderá sugerir verificar o equipamento antes de assumir que existe um problema técnico.

---

# Integração com o Console

O Console poderá destacar automaticamente os canais utilizados pelos participantes ativos.

Exemplo:

Durante o Louvor:

- Robson → Violão Martin
- Alessandra → Mic Vermelho
- Letícia → Mic Azul

Os demais canais permanecem em segundo plano.

---

# Integração com o Dashboard

O Dashboard poderá apresentar um resumo.

Exemplo:

```text
Participantes Ativos

4

Robson

Alessandra

Letícia

João
```

---

# Integração com o Mobile

O aplicativo Mobile poderá apresentar uma lista simplificada.

Exemplo:

```text
Agora

Participantes Ativos

• Robson

• Alessandra

• Letícia
```

---

# Benefícios

A utilização do módulo de Participantes proporciona diversas vantagens:

- associa pessoas aos recursos da mesa de som;
- melhora o entendimento do contexto operacional;
- aumenta a precisão das recomendações da IA;
- facilita a organização da equipe durante o evento;
- reduz a carga cognitiva do operador;
- melhora a rastreabilidade das operações realizadas.

---

# Separação de Responsabilidades

O módulo de Participantes possui responsabilidade única.

Ele não:

- controla canais da mesa;
- altera faders;
- modifica configurações da Ui24R;
- executa comandos;
- processa sinais de áudio.

Sua função é representar quem participa do evento e quais recursos estão associados a cada pessoa.

---

# Evoluções Futuras

Nas próximas versões, o módulo poderá incorporar funcionalidades como:

- cadastro permanente da equipe de sonorização e músicos;
- fotografia dos participantes;
- histórico individual de participação;
- estatísticas por participante;
- associação automática de equipamentos preferenciais;
- integração com escalas ministeriais;
- reconhecimento de padrões de operação por participante;
- recomendações personalizadas da IA com base no histórico de cada integrante.

---

# Relação com Outros Componentes

O módulo de Participantes trabalha em conjunto com:

- Painel da Liturgia;
- Timeline do Evento;
- Etapas da Liturgia;
- Músicas;
- Configuração do Evento;
- Console de Operação;
- Dashboard Operacional;
- Painel da IA.

Ele representa a dimensão humana da operação, conectando pessoas, recursos e contexto operacional em uma única visão.

---

# Situação da Sprint

**Status:** ✅ Concluída