# Sprint E07 – Visual Priority

## Objetivo

Definir o sistema responsável por estabelecer a prioridade visual de todas as informações exibidas pela Inteligência Artificial do Audio Copilot.

O **Visual Priority** determina quais elementos devem receber maior evidência na interface, garantindo que o operador concentre sua atenção nas situações mais importantes durante a operação.

Enquanto o **Recommendation Engine** determina a importância técnica de uma recomendação e o **Focus Manager** decide onde direcionar a atenção do operador, o **Visual Priority** define como essa importância será representada visualmente.

---

# Visão Geral

Durante um evento, diversos alertas podem surgir simultaneamente.

Exemplo:

- clipping em dois canais;
- feedback em um monitor;
- bateria baixa de um microfone;
- sugestão de equalização;
- canal sem sinal;
- recomendação de ganho.

Sem um sistema de prioridade, todos apareceriam com a mesma importância, dificultando a identificação do problema mais crítico.

O Visual Priority organiza essas informações utilizando níveis de prioridade visual padronizados.

---

# Filosofia

O Visual Priority foi desenvolvido seguindo cinco princípios.

## Clareza

A prioridade deve ser compreendida instantaneamente.

---

## Consistência

Problemas iguais devem utilizar sempre a mesma representação visual.

---

## Hierarquia

Elementos críticos sempre recebem maior destaque.

---

## Discrição

Informações secundárias não devem competir com alertas importantes.

---

## Escalabilidade

Novos níveis de prioridade poderão ser adicionados sem alterar a arquitetura do sistema.

---

# Arquitetura

```text
Recommendation Engine

↓

Decision Engine

↓

Visual Priority

↓

Highlight Manager

↓

Animation System

↓

Console Operacional
```

---

# Responsabilidades

O Visual Priority será responsável por:

- definir níveis de prioridade;
- padronizar cores;
- padronizar intensidade visual;
- orientar animações;
- orientar destaques;
- organizar a hierarquia visual da interface.

---

# Fluxo de Funcionamento

```text
Nova Recomendação

↓

Classificar Prioridade

↓

Selecionar Estilo Visual

↓

Enviar ao Highlight Manager

↓

Atualizar Interface
```

---

# Hierarquia de Prioridades

O sistema utiliza cinco níveis de prioridade.

| Nível | Classificação | Objetivo |
|--------|---------------|----------|
| 1 | Crítica | Exige ação imediata |
| 2 | Alta | Deve ser resolvida rapidamente |
| 3 | Média | Merece atenção do operador |
| 4 | Baixa | Informação auxiliar |
| 5 | Informativa | Apenas registro ou confirmação |

Essa classificação será utilizada em toda a interface do Audio Copilot.

---

# Prioridade Crítica

Situações que podem comprometer imediatamente o áudio do evento.

Exemplos:

- feedback;
- saturação severa;
- perda de sinal do microfone principal;
- falha crítica de equipamento.

Representação:

- vermelho;
- pulsação intensa;
- destaque máximo;
- foco automático.

---

# Prioridade Alta

Problemas que exigem ação rápida, mas não imediata.

Exemplos:

- clipping contínuo;
- ganho excessivo;
- auxiliar sobrecarregado;
- bateria muito baixa.

Representação:

- laranja;
- brilho moderado;
- destaque evidente.

---

# Prioridade Média

Sugestões importantes para melhorar a operação.

Exemplos:

- ajuste de equalização;
- compressão recomendada;
- balanceamento de retorno.

Representação:

- azul;
- glow suave;
- animação discreta.

---

# Prioridade Baixa

Informações úteis ao operador.

Exemplos:

- canal pouco utilizado;
- recomendação futura;
- alteração sugerida.

Representação:

- cinza;
- indicador simples;
- sem animação.

---

# Prioridade Informativa

Eventos que apenas registram mudanças de estado.

Exemplos:

- snapshot carregado;
- recomendação aplicada;
- sincronização concluída.

Representação:

- verde;
- pequeno indicador;
- desaparecimento automático.

---

# Representação Visual

Cada prioridade influencia diversos aspectos da interface.

| Elemento | Controlado pelo Visual Priority |
|----------|---------------------------------|
| Cor | ✔ |
| Intensidade | ✔ |
| Tamanho do destaque | ✔ |
| Tipo de animação | ✔ |
| Ordem de exibição | ✔ |
| Tempo de permanência | ✔ |

---

# Exemplo

```text
Feedback

↓

Prioridade Crítica

↓

Borda Vermelha

↓

Pulsação

↓

Overlay

↓

Badge
```

---

# Outro Exemplo

```text
Sugestão

↓

Prioridade Média

↓

Glow Azul

↓

Badge AI
```

---

# Priorização entre Eventos

Quando vários eventos ocorrerem simultaneamente:

```text
Feedback

↓

Clipping

↓

Canal sem sinal

↓

Sugestão
```

A interface destacará primeiro os eventos de maior prioridade.

---

# Atualização Dinâmica

A prioridade poderá mudar durante a operação.

Exemplo:

```text
Clipping

↓

Alta

↓

Operador reduz ganho

↓

Baixa

↓

Remover destaque
```

O sistema atualizará automaticamente toda a interface.

---

# Integração com o Highlight Manager

O Highlight Manager utiliza o nível de prioridade para decidir:

- qual destaque será exibido;
- qual será ocultado;
- qual permanecerá ativo.

---

# Integração com o Focus Manager

O Focus Manager utiliza a prioridade para decidir onde concentrar a atenção do operador.

---

# Integração com o Animation System

Cada prioridade poderá utilizar animações diferentes.

Exemplo:

| Prioridade | Animação |
|------------|----------|
| Crítica | Flash + Pulsação |
| Alta | Pulsação |
| Média | Glow |
| Baixa | Fade |
| Informativa | Fade curto |

---

# Integração com o Notification Badges

Os badges seguem a mesma hierarquia visual.

Exemplo:

```text
🔴

Crítico
```

```text
⚠

Alta
```

```text
AI

Média
```

---

# Integração com o Dashboard

O Dashboard poderá ordenar automaticamente os alertas pela prioridade visual.

Assim, os problemas mais importantes sempre aparecerão primeiro.

---

# Integração com o Histórico

Toda alteração de prioridade poderá ser registrada.

Exemplo:

```text
09:41

Canal 08

↓

Prioridade Alta

↓

09:43

Prioridade Resolvida
```

---

# Acessibilidade

O sistema foi projetado para não depender exclusivamente das cores.

Além das cores, serão utilizados:

- ícones;
- animações;
- formas;
- contraste;
- textos curtos.

Isso garante melhor acessibilidade para operadores com deficiência visual ou daltonismo.

---

# Benefícios

O Visual Priority proporciona:

- melhor organização visual;
- identificação imediata de problemas críticos;
- redução da carga cognitiva;
- interface mais intuitiva;
- comunicação consistente da IA;
- maior segurança operacional.

---

# Separação de Responsabilidades

O Visual Priority não:

- detecta problemas;
- gera recomendações;
- cria overlays;
- executa animações;
- altera parâmetros da mesa.

Sua responsabilidade é definir a hierarquia visual das recomendações produzidas pela Inteligência Artificial.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- prioridades configuráveis por operador;
- temas personalizados de cores;
- adaptação automática ao perfil de uso;
- integração com múltiplos monitores;
- níveis de prioridade específicos por tipo de evento;
- perfis para igrejas, shows e conferências;
- personalização por acessibilidade;
- otimização baseada em aprendizado da IA.

---

# Relação com Outros Componentes

O Visual Priority trabalha diretamente com:

- Recommendation Engine;
- Decision Engine;
- Highlight Engine;
- Highlight Rules;
- Highlight Manager;
- Focus Manager;
- Animation System;
- Channel Overlay;
- Notification Badges;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA.

Ele representa a camada responsável por estabelecer a hierarquia visual do Audio Copilot, garantindo que todas as recomendações da Inteligência Artificial sejam apresentadas com a intensidade adequada, permitindo que o operador identifique rapidamente as situações mais importantes e tome decisões com segurança durante toda a operação.

---

# Situação da Sprint

**Status:** ✅ Concluída