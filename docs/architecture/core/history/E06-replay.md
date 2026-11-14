# Sprint E06 – Replay

## Objetivo

Definir o componente responsável por reconstruir e reproduzir toda a operação realizada durante um evento no Audio Copilot.

O Replay permite revisitar um culto ou evento como se ele estivesse acontecendo novamente, reconstruindo o estado da mesa de som, da liturgia, das ações do operador e das recomendações da Inteligência Artificial ao longo do tempo.

Seu objetivo é transformar o histórico registrado pelo sistema em uma experiência navegável, possibilitando análise pós-evento, treinamento de operadores, auditoria e evolução contínua da operação.

Enquanto a **Timeline** organiza os acontecimentos, o **Replay** recria o estado completo da operação em qualquer instante.

---

# Visão Geral

Ao término de um evento, o Audio Copilot possuirá todas as informações necessárias para reconstruir completamente sua execução.

Entre elas:

- estado da mesa de som;
- posição dos faders;
- configurações dos canais;
- etapas da liturgia;
- ações do operador;
- recomendações da IA;
- alertas técnicos;
- mudanças de contexto.

O Replay utiliza esses registros para reproduzir o evento de forma cronológica.

---

# Filosofia

O Replay foi desenvolvido seguindo cinco princípios.

## Fidelidade

A reprodução deve representar exatamente o que aconteceu.

---

## Navegação

O usuário pode avançar, retroceder ou acessar qualquer instante do evento.

---

## Contexto

Cada momento deve apresentar todas as informações relevantes.

---

## Aprendizado

O Replay é uma ferramenta de treinamento e melhoria contínua.

---

## Auditoria

A reprodução deve permitir verificar decisões técnicas e operacionais.

---

# Arquitetura

```text
History Manager

↓

Timeline

↓

Change Log

↓

Event Log

↓

Action History

↓

AI History

↓

Replay Engine

↓

Interface do Replay
```

O Replay utiliza os registros históricos para reconstruir o estado completo da aplicação.

---

# Responsabilidades

O Replay será responsável por:

- reconstruir eventos passados;
- reproduzir alterações da mesa;
- reproduzir ações do operador;
- reproduzir recomendações da IA;
- sincronizar a Timeline;
- permitir navegação temporal;
- fornecer suporte para treinamento e auditoria.

---

# Fontes de Informação

O Replay utiliza informações provenientes de:

- History Manager;
- Timeline;
- Change Log;
- Event Log;
- Action History;
- AI History;
- Telemetry Manager;
- State Manager.

---

# Fluxo de Funcionamento

```text
Selecionar Evento

↓

Carregar Histórico

↓

Reconstruir Estado Inicial

↓

Reproduzir Eventos

↓

Atualizar Interface

↓

Encerrar Replay
```

---

# Reconstrução do Estado

Antes da reprodução, o sistema reconstrói o estado inicial.

Exemplo:

```text
Evento

Culto Domingo Manhã

↓

Mesa conectada

↓

Snapshot carregado

↓

Liturgia iniciada

↓

Replay pronto
```

---

# Reprodução Cronológica

Durante a reprodução, todos os acontecimentos seguem a ordem original.

```text
09:00

Evento iniciado

↓

09:05

Louvor

↓

09:18

Primeira música

↓

09:36

Pregação

↓

10:25

Encerramento
```

---

# Reprodução da Mesa

O Replay poderá restaurar visualmente:

- posição dos faders;
- ganho dos canais;
- mute;
- solo;
- equalizadores;
- compressores;
- gates;
- envios auxiliares;
- masters.

O objetivo é mostrar exatamente como a mesa estava configurada naquele instante.

---

# Reprodução da Liturgia

A Timeline Litúrgica também será reproduzida.

Exemplo:

```text
09:05

Louvor

↓

09:28

Avisos

↓

09:35

Pregação

↓

10:18

Santa Ceia
```

O operador poderá acompanhar o contexto do evento.

---

# Reprodução das Ações do Operador

Todas as ações registradas poderão ser visualizadas.

Exemplo:

```text
09:42

Robson

↓

Reduziu o Gain

↓

Mutou o Playback

↓

Carregou Snapshot
```

---

# Reprodução da IA

O Replay também mostrará o comportamento da Inteligência Artificial.

Exemplo:

```text
09:41

Feedback detectado

↓

09:42

Sugestão exibida

↓

09:43

Operador aceitou

↓

09:44

Problema resolvido
```

Isso permite compreender como a IA atuou durante o evento.

---

# Controles de Reprodução

O Replay poderá oferecer controles semelhantes aos de um player de mídia.

Exemplo:

```text
▶ Reproduzir

⏸ Pausar

⏪ Retroceder

⏩ Avançar

⏮ Início

⏭ Fim
```

Também poderá haver diferentes velocidades.

```text
0.5x

1x

2x

4x

8x
```

---

# Navegação Temporal

O usuário poderá selecionar qualquer instante da Timeline.

Exemplo:

```text
09:42

↓

Abrir Replay

↓

Restaurar Estado

↓

Exibir Mesa
```

Não será necessário assistir toda a reprodução.

---

# Sincronização

Todos os módulos permanecem sincronizados.

Quando a reprodução avança, são atualizados simultaneamente:

- Dashboard;
- Console;
- Painel da IA;
- Painel da Liturgia;
- Timeline;
- Medidores;
- Histórico.

---

# Filtros

O Replay poderá reproduzir apenas determinadas categorias.

Exemplos:

- somente ações do operador;
- somente recomendações da IA;
- somente alterações da mesa;
- somente eventos da liturgia;
- somente incidentes técnicos.

Isso facilita análises específicas.

---

# Modo Treinamento

O Replay poderá ser utilizado para capacitação de novos operadores.

Exemplo:

```text
Replay

↓

Pausar

↓

Explicar decisão da IA

↓

Mostrar ação correta

↓

Continuar reprodução
```

Esse modo transforma eventos reais em material didático.

---

# Modo Auditoria

Durante a reprodução, qualquer registro poderá ser expandido.

Exemplo:

```text
09:42

↓

Abrir detalhes

↓

Visualizar histórico

↓

Visualizar recomendação

↓

Visualizar alteração

↓

Visualizar operador
```

---

# Integração com Relatórios

Ao final do Replay, será possível gerar um relatório resumido.

Exemplo:

```text
Resumo

Duração

1h32

Alterações

286

Eventos

94

Recomendações IA

18

Aceitas

15

Incidentes

1
```

---

# Desempenho

O Replay deverá reconstruir eventos de forma eficiente, mesmo em eventos longos com milhares de registros.

Sempre que possível, a reconstrução utilizará snapshots intermediários para reduzir o tempo de carregamento e melhorar a navegação.

---

# Benefícios

O Replay proporciona:

- reconstrução completa da operação;
- treinamento de novos operadores;
- análise pós-evento;
- auditoria detalhada;
- validação das decisões da IA;
- investigação de incidentes;
- evolução contínua da equipe técnica.

---

# Separação de Responsabilidades

O Replay não:

- registra eventos;
- altera configurações da mesa;
- executa comandos reais;
- gera recomendações;
- modifica históricos.

Sua responsabilidade é reconstruir e apresentar, de forma fiel e navegável, tudo o que ocorreu durante um evento.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- sincronização com gravações de áudio;
- sincronização com transmissão de vídeo;
- reprodução lado a lado de dois eventos;
- comparação entre operadores;
- exportação de sessões de Replay;
- marcadores personalizados;
- comentários durante a reprodução;
- modo colaborativo para treinamentos;
- reprodução acelerada inteligente baseada em eventos relevantes.

---

# Relação com Outros Componentes

O Replay trabalha diretamente com:

- History Manager;
- Timeline;
- Change Log;
- Event Log;
- Action History;
- AI History;
- Audit;
- Dashboard Operacional;
- Console Operacional;
- Painel da Liturgia;
- Painel da IA;
- Learning Engine.

Ele representa a camada de reconstrução histórica do Audio Copilot, permitindo reviver qualquer evento com precisão, compreender decisões técnicas e operacionais, validar o comportamento da Inteligência Artificial e transformar o histórico do sistema em uma poderosa ferramenta de treinamento, auditoria e melhoria contínua.

---

# Situação da Sprint

**Status:** ✅ Concluída