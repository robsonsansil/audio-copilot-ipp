# Sprint E04 – Transições

## Objetivo

Definir o componente responsável por controlar a mudança entre as etapas da programação do evento.

As Transições representam os momentos em que o culto ou ensaio passa de uma etapa para outra, permitindo que o Audio Copilot atualize automaticamente o contexto operacional da aplicação.

Esse componente garante que Dashboard, Console de Operação, Painel da IA, Mobile e demais módulos estejam sempre sincronizados com o andamento do evento.

---

# Visão Geral

Durante um culto existem diversos momentos de mudança.

Por exemplo:

```text
Recepção

↓

Oração Inicial

↓

Louvor

↓

Avisos

↓

Oferta

↓

Pregação

↓

Ceia

↓

Encerramento
```

Cada mudança altera completamente o contexto da operação.

Consequentemente, também muda:

- os participantes ativos;
- os instrumentos esperados;
- os microfones utilizados;
- os canais em destaque;
- as análises realizadas pela IA.

O módulo de Transições é responsável por coordenar essa mudança de contexto.

---

# Filosofia

As Transições não modificam a configuração da mesa de som.

Elas apenas informam que o evento mudou de contexto.

A decisão técnica continua pertencendo ao operador.

O Audio Copilot apenas adapta sua interface e suas recomendações ao novo momento do evento.

---

# Arquitetura

Fluxo simplificado:

```text
Painel da Liturgia

↓

Operador confirma avanço

↓

Transições

↓

State Manager

↓

Dashboard

↓

Console

↓

Painel da IA

↓

Mobile
```

As Transições atualizam o estado global do evento.

---

# Responsabilidades

O módulo de Transições será responsável por:

- alterar a etapa atual do evento;
- atualizar o contexto operacional;
- registrar a mudança no Histórico;
- notificar todos os módulos da aplicação;
- informar a IA sobre a nova etapa;
- atualizar indicadores de progresso.

---

# Fluxo Básico

O fluxo esperado será:

```text
Etapa Atual

↓

Operador confirma

↓

Encerrar etapa atual

↓

Iniciar próxima etapa

↓

Atualizar Estado Global

↓

Notificar todos os módulos
```

Todo o processo deverá ocorrer de forma instantânea.

---

# Exemplo

```text
Etapa Atual

Louvor

↓

Operador

Avançar

↓

Nova etapa

Avisos
```

Após essa alteração:

Dashboard:

```text
Agora

Avisos
```

Console:

```text
Destacar

Púlpito

Microfone Sem Fio
```

IA:

```text
Novo contexto identificado.

Etapa:

Avisos
```

---

# Atualização dos Participantes

Durante uma transição, o sistema recalcula automaticamente os participantes ativos.

Exemplo:

Antes:

```text
Louvor

Participantes

• Alessandra

• Letícia

• Robson
```

Depois:

```text
Pregação

Participantes

• Pastor
```

Essas informações ficam imediatamente disponíveis para toda a aplicação.

---

# Atualização dos Recursos

Também serão atualizados automaticamente:

- instrumentos previstos;
- microfones previstos;
- canais prioritários;
- observações da etapa.

Exemplo:

Antes:

```text
Instrumentos

Violão

Baixo

Cajón
```

Depois:

```text
Instrumentos

Nenhum
```

---

# Atualização do Console

O Console poderá reorganizar automaticamente seus destaques.

Exemplo:

Durante o Louvor:

```text
Prioridade

✓ Vocais

✓ Instrumentos
```

Após a transição:

```text
Prioridade

✓ Pastor

✓ Púlpito
```

Os demais canais continuam disponíveis, porém deixam de ser destacados.

---

# Integração com a Inteligência Artificial

A IA é um dos principais consumidores das Transições.

Sempre que uma nova etapa iniciar, ela recebe imediatamente o novo contexto.

Exemplo:

```text
Transição

Louvor

↓

Pregação
```

A IA passa automaticamente a considerar como comportamento esperado:

- atividade do Pastor;
- atividade do Púlpito;
- instrumentos silenciosos.

Isso reduz significativamente a ocorrência de falsas recomendações.

---

# Confirmação do Operador

Por padrão, toda transição deverá ser confirmada pelo operador.

Fluxo:

```text
Avançar Etapa

↓

Confirmar

↓

Executar Transição
```

Essa confirmação evita mudanças acidentais durante o evento.

---

# Alteração Manual

O operador poderá alterar livremente a sequência da programação.

Exemplos:

- voltar uma etapa;
- repetir uma música;
- pular uma etapa;
- cancelar uma etapa;
- reorganizar a programação durante o culto.

Todas essas ações poderão ser registradas no Histórico.

---

# Registro no Histórico

Cada transição deverá gerar um evento.

Exemplo:

```text
09:32

Louvor

Concluído

↓

09:33

Avisos

Iniciado
```

Essas informações poderão ser utilizadas posteriormente em relatórios e auditorias.

---

# Integração com o Dashboard

O Dashboard atualizará automaticamente:

- etapa atual;
- próxima etapa;
- progresso do evento;
- tempo da etapa.

Tudo isso ocorrerá imediatamente após a transição.

---

# Integração com o Mobile

O aplicativo Mobile também acompanhará as mudanças.

Exemplo:

```text
Agora

Pregação

Próximo

Ceia
```

---

# Benefícios

O módulo de Transições proporciona diversas vantagens:

- sincronização entre todos os módulos;
- atualização automática do contexto operacional;
- redução da carga cognitiva do operador;
- maior precisão das recomendações da IA;
- rastreabilidade completa da programação;
- facilidade para adaptação da liturgia durante o evento.

---

# Separação de Responsabilidades

O módulo de Transições possui responsabilidade única.

Ele não:

- altera parâmetros da Ui24R;
- movimenta faders;
- processa áudio;
- executa snapshots;
- toma decisões automáticas.

Sua função é controlar a mudança de contexto entre as etapas do evento.

---

# Evoluções Futuras

Nas próximas versões, o módulo poderá incorporar funcionalidades como:

- sugestão automática de avanço baseada no tempo previsto;
- detecção automática do término de músicas utilizando Inteligência Artificial;
- integração com softwares de projeção para sincronizar mudanças de etapa;
- gatilhos automáticos para iniciar gravação ou transmissão;
- execução opcional de snapshots recomendados para cada etapa;
- análise da duração real de cada transição;
- aprendizado dos padrões de cada igreja para otimizar futuras programações.

---

# Relação com Outros Componentes

O módulo de Transições trabalha em conjunto com:

- Painel da Liturgia;
- Timeline do Evento;
- Etapas da Liturgia;
- Músicas;
- Participantes;
- Dashboard Operacional;
- Console de Operação;
- Painel da IA;
- Histórico de Alterações;
- State Manager.

Ele é o responsável por manter toda a aplicação sincronizada com o andamento do evento.

---

# Situação da Sprint

**Status:** ✅ Concluída