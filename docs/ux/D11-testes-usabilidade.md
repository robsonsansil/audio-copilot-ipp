# Sprint D11 – Testes de Usabilidade

## Objetivo

Validar a experiência de utilização do Audio Copilot em todas as etapas da operação de um evento.

Esta sprint tem como objetivo garantir que o sistema seja intuitivo, rápido, seguro e eficiente para operadores de diferentes níveis de experiência.

Mais do que verificar o funcionamento das telas, esta fase avalia se a filosofia do Audio Copilot — reduzir a carga cognitiva do operador através da Inteligência Artificial — está sendo cumprida.

---

# Objetivos dos Testes

Os testes deverão validar os seguintes princípios:

- facilidade de aprendizado;
- rapidez na execução das tarefas;
- navegação intuitiva;
- baixa carga cognitiva;
- confiança nas recomendações da IA;
- redução de erros operacionais;
- aumento da produtividade do operador.

---

# Escopo dos Testes

Serão avaliadas todas as funcionalidades desenvolvidas nas sprints anteriores.

Fluxo completo:

1. Dashboard Principal
2. Programação Técnica
3. Configuração do Evento
4. Preparação do Evento
5. Console de Operação
6. Painel da IA
7. Aplicativo Mobile

Também serão avaliadas as integrações entre essas telas.

---

# Personas

Os testes deverão ser realizados com diferentes perfis de usuários.

## Operador Iniciante

Características:

- pouca experiência em mesas digitais;
- nunca utilizou o Audio Copilot.

Objetivo:

Verificar se o sistema pode ser utilizado praticamente sem treinamento.

---

## Operador Intermediário

Características:

- experiência básica em operação de áudio;
- já operou algumas mesas digitais.

Objetivo:

Avaliar velocidade de adaptação.

---

## Operador Avançado

Características:

- conhecimento técnico da Soundcraft Ui24R;
- experiência em sonorização ao vivo.

Objetivo:

Validar se o sistema aumenta a produtividade sem limitar o operador.

---

## Pastor ou Líder

Objetivo:

Validar a compreensão dos relatórios e do histórico dos eventos.

---

## Músicos

Objetivo:

Verificar se o processo de preparação é claro e intuitivo para todos os participantes.

---

# Cenários de Teste

## Cenário 01 – Criar um novo evento

O operador deverá:

- criar um novo evento;
- selecionar um template;
- configurar os recursos ativos;
- associar participantes;
- selecionar os instrumentos correspondentes;
- salvar a configuração.

Critérios:

- fluxo intuitivo;
- poucos cliques;
- ausência de dúvidas.

---

## Cenário 02 – Preparar o Evento

O operador deverá:

- abrir a tela de Preparação;
- solicitar os testes dos participantes;
- acompanhar o progresso;
- validar todos os recursos.

Critérios:

- fácil identificação dos recursos pendentes;
- progresso visual claro;
- associação correta entre recurso e participante.

---

## Cenário 03 – Operação ao Vivo

Durante uma simulação de culto, o operador deverá:

- acompanhar o Dashboard;
- abrir rapidamente um canal específico;
- ajustar volume;
- aplicar Mute;
- remover Mute;
- retornar ao Dashboard.

Critérios:

- rapidez;
- navegação intuitiva;
- poucos passos.

---

## Cenário 04 – Recomendações da IA

Durante a operação serão simuladas situações como:

- clipping;
- canal sem sinal;
- risco de microfonia;
- excesso de volume.

A IA deverá apresentar recomendações.

O operador decidirá:

- aplicar;
- ignorar.

Critérios:

- clareza da recomendação;
- confiança na IA;
- facilidade para responder.

---

## Cenário 05 – Aplicativo Mobile

O operador deverá:

- acompanhar o evento pelo celular;
- receber alertas;
- visualizar canais ativos;
- aplicar ações rápidas;
- retornar ao monitoramento.

Critérios:

- rapidez;
- simplicidade;
- facilidade de uso.

---

# Fluxo Completo

O principal teste consiste em executar toda a operação de um evento.

Fluxo esperado:

1. Criar Evento.
2. Configurar Evento.
3. Preparar Evento.
4. Iniciar Operação.
5. Receber recomendações da IA.
6. Finalizar Evento.
7. Consultar Relatório.

Caso esse fluxo possa ser realizado sem dificuldades, considera-se que o sistema atingiu seu objetivo principal.

---

# Métricas de Usabilidade

Serão acompanhados os seguintes indicadores.

| Indicador | Meta |
|------------|------|
| Criar novo evento | até 3 minutos |
| Configurar canais | até 5 minutos |
| Preparação completa | até 10 minutos |
| Localizar um canal | até 3 segundos |
| Abrir Console pelo Dashboard | até 2 segundos |
| Aplicar sugestão da IA | até 2 cliques |
| Resolver um alerta | até 10 segundos |

---

# Avaliação da IA

Além da interface, também será avaliada a qualidade das recomendações da Inteligência Artificial.

Para cada sugestão apresentada, o operador responderá:

- Entendeu o motivo da recomendação?
- A recomendação foi clara?
- Você confiou na sugestão?
- Você aplicaria essa recomendação em um evento real?

Essas respostas permitirão aperfeiçoar continuamente os algoritmos do Audio Copilot.

---

# Avaliação SUS (System Usability Scale)

Ao término dos testes, cada participante responderá ao questionário padrão SUS (System Usability Scale).

Meta do projeto:

**Pontuação mínima: 90 pontos**

Essa pontuação representa uma excelente experiência de utilização.

---

# Critérios de Aprovação

A Sprint será considerada aprovada quando:

- todos os fluxos puderem ser concluídos sem erros críticos;
- a navegação for considerada intuitiva pela maioria dos participantes;
- o tempo médio das tarefas estiver dentro das metas estabelecidas;
- a IA for compreendida e aceita pelos operadores;
- não forem identificados problemas críticos de usabilidade.

---

# Registro dos Testes

Cada sessão deverá registrar:

- perfil do participante;
- data;
- versão do sistema;
- cenário executado;
- dificuldades encontradas;
- sugestões de melhoria;
- tempo gasto em cada tarefa;
- observações gerais.

Essas informações servirão como base para a evolução contínua do Audio Copilot.

---

# Integração com as Demais Sprints

Os testes de usabilidade contemplam todas as funcionalidades desenvolvidas nas sprints anteriores:

- D04 – Tela Principal;
- D05 – Programação Técnica;
- D06 – Configuração do Evento;
- D07 – Preparação do Evento;
- D08 – Console de Operação;
- D09 – Painel da IA;
- D10 – Aplicativo Mobile.

Qualquer melhoria identificada durante os testes poderá gerar ajustes nos protótipos ou originar novas funcionalidades.

---

# Objetivos de UX

Esta sprint valida os principais objetivos de experiência do usuário definidos para o projeto:

- interface intuitiva;
- baixa carga cognitiva;
- rapidez na execução das tarefas;
- redução de erros operacionais;
- confiança na Inteligência Artificial;
- navegação consistente entre as telas;
- operação segura durante eventos ao vivo.

---

# Melhorias Futuras

Após a conclusão dos testes, poderão ser planejadas novas rodadas de validação, incluindo:

- testes em igrejas de diferentes portes;
- comparação entre operadores iniciantes e experientes;
- testes em eventos com maior número de participantes;
- avaliações de acessibilidade;
- testes de desempenho em diferentes dispositivos;
- coleta de métricas de uso em ambiente real.

---

# Situação da Sprint

**Status:** ✅ Concluída