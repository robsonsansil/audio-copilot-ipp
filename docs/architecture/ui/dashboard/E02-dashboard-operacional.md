# Sprint E02 – Dashboard Operacional

## Objetivo

Definir o funcionamento do Dashboard Operacional do Audio Copilot.

O Dashboard é a principal tela do sistema e representa o ponto central de acompanhamento do evento.

Seu objetivo é fornecer ao operador uma visão geral da operação, apresentando apenas as informações mais relevantes de forma clara, organizada e em tempo real.

Esta sprint define o comportamento funcional do Dashboard, sua integração com o State Manager e sua interação com os demais módulos do sistema.

---

# Visão Geral

O Dashboard Operacional é a primeira tela exibida após a abertura de um evento.

Diferentemente do Console de Operação, o Dashboard não tem como objetivo controlar diretamente a mesa de som.

Seu papel é permitir que o operador compreenda rapidamente a situação atual do evento e acesse qualquer área do sistema com poucos cliques.

Ele funciona como um centro de comando da operação.

---

# Filosofia

O Dashboard deve responder rapidamente às seguintes perguntas:

- Qual evento está em andamento?
- Em qual etapa da programação estamos?
- Existe algum alerta?
- A IA possui recomendações?
- Todos os recursos estão funcionando?
- Há participantes aguardando?
- O sistema está saudável?

O operador deve conseguir responder todas essas perguntas em poucos segundos, sem precisar abrir outras telas.

---

# Responsabilidades

O Dashboard é responsável por:

- apresentar o resumo do evento;
- acompanhar a programação técnica;
- exibir o andamento da operação;
- mostrar os principais indicadores do sistema;
- informar alertas ativos;
- apresentar recomendações da IA;
- facilitar a navegação para os demais módulos.

O Dashboard não realiza configurações nem controla diretamente os canais da Ui24R.

---

# Integração com o State Manager

O Dashboard não armazena informações próprias.

Todos os dados apresentados são obtidos do State Manager.

```
State Manager

↓

Dashboard

↓

Atualização Automática
```

Sempre que o estado global for alterado, apenas os componentes afetados do Dashboard serão atualizados.

---

# Estrutura da Tela

O Dashboard é composto pelos seguintes blocos.

---

## Cabeçalho

Apresenta as informações gerais do evento.

Exibe:

- nome do evento;
- template utilizado;
- data;
- horário;
- operador responsável;
- status do evento.

Exemplo:

```
Culto Domingo Manhã

Domingo

09:00

Operador: Robson

Em andamento
```

---

## Programação Técnica

Exibe a programação do evento.

Cada etapa possui um indicador de status.

Estados previstos:

- concluída;
- em andamento;
- próxima;
- pendente.

O operador pode avançar manualmente entre as etapas quando necessário.

---

## Recursos Ativos

Apresenta um resumo dos recursos utilizados no evento.

Exemplo:

- 9 canais ativos;
- 3 microfones;
- 2 instrumentos;
- 1 púlpito;
- 1 retorno.

Ao selecionar um recurso, o Console de Operação será aberto com o canal correspondente já destacado.

Exemplo:

```
Baixo

↓

Console

↓

Canal 09 selecionado
```

---

## Saúde do Sistema

Apresenta um resumo dos principais componentes do sistema.

Exemplos:

- Ui24R conectada;
- sincronização ativa;
- gravação habilitada;
- snapshot carregado;
- IA operacional.

O objetivo é permitir que o operador identifique rapidamente qualquer problema de infraestrutura.

---

## Alertas

Exibe somente alertas ativos.

Exemplos:

- clipping;
- ausência de sinal;
- risco de microfonia;
- canal mutado;
- equipamento desconectado.

Os alertas permanecem visíveis até serem resolvidos.

---

## Painel da IA

Apresenta um resumo da atividade da Inteligência Artificial.

Exemplos:

- recomendações pendentes;
- sugestões aceitas;
- sugestões ignoradas;
- confiança da IA;
- último aprendizado registrado.

Ao clicar em uma recomendação, o Painel da IA será aberto diretamente na sugestão correspondente.

---

## Ações Rápidas

Disponibiliza acesso direto às principais telas do sistema.

Exemplos:

- Configuração do Evento;
- Preparação do Evento;
- Console de Operação;
- Painel da IA;
- Histórico;
- Relatórios.

---

# Atualização em Tempo Real

O Dashboard observa continuamente o State Manager.

Sempre que algum módulo alterar o estado da aplicação, o Dashboard será atualizado automaticamente.

Exemplo:

```
Operador

↓

Altera Volume

↓

State Manager

↓

Dashboard Atualizado
```

O operador nunca precisa atualizar manualmente a tela.

---

# Navegação Contextual

O Dashboard permite acesso direto ao contexto correspondente.

Exemplos:

Selecionar:

```
Baixo
```

abre

```
Console de Operação

↓

Canal do Baixo selecionado
```

Selecionar:

```
Alerta

↓

Clipping Canal 07
```

abre

```
Console

↓

Canal 07
```

Selecionar:

```
Recomendação da IA
```

abre

```
Painel da IA

↓

Sugestão correspondente
```

Essa navegação reduz o tempo necessário para localizar informações durante o evento.

---

# Estados do Dashboard

O Dashboard adapta automaticamente seu conteúdo conforme a fase do evento.

Estados previstos:

- sem evento;
- configuração;
- preparação;
- aguardando início;
- operação em andamento;
- evento encerrado.

Cada estado prioriza informações diferentes.

Exemplo:

Durante a preparação:

- progresso dos testes;
- recursos pendentes;
- participantes aguardando.

Durante a operação:

- programação;
- alertas;
- saúde do sistema;
- recomendações da IA.

Após o encerramento:

- resumo do evento;
- geração de relatórios;
- estatísticas.

---

# Matriz de Atualização

| Componente | Origem dos Dados | Atualização |
|------------|------------------|-------------|
| Cabeçalho | Event State | Automática |
| Programação Técnica | Program State | Automática |
| Recursos Ativos | Channel State | Automática |
| Saúde do Sistema | System State | Automática |
| Alertas | Alert State | Automática |
| Painel da IA | IA State | Automática |
| Ações Rápidas | Configuração do Sistema | Estática |

---

# Regras de Negócio

O Dashboard deverá seguir as seguintes regras:

- nunca alterar diretamente a Ui24R;
- consumir apenas dados do State Manager;
- atualizar automaticamente todas as informações;
- destacar apenas alertas ativos;
- apresentar somente informações relevantes para o momento atual do evento;
- permitir navegação contextual para os demais módulos;
- manter baixa carga cognitiva.

---

# Benefícios

Essa arquitetura proporciona:

- visão geral da operação;
- rápida identificação de problemas;
- navegação simplificada;
- atualização automática;
- integração completa com os demais módulos;
- menor necessidade de troca entre telas.

---

# Integração com Outros Módulos

O Dashboard recebe informações de:

- State Manager;
- Programação Técnica;
- Configuração do Evento;
- Preparação do Evento;
- Console de Operação;
- Painel da IA;
- Histórico;
- Sistema de Alertas.

E permite acesso direto para:

- Configuração do Evento;
- Preparação do Evento;
- Console de Operação;
- Painel da IA;
- Histórico;
- Relatórios.

---

# Objetivos da Sprint

Ao final desta sprint, o projeto deverá possuir:

- definição funcional completa do Dashboard Operacional;
- integração documentada com o State Manager;
- comportamento em tempo real especificado;
- regras de navegação contextual definidas;
- responsabilidades claramente separadas do Console de Operação;
- base preparada para a implementação da interface.

---

# Situação da Sprint

**Status:** ✅ Concluída