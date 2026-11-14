# Sprint E05 – Rule Engine

## Objetivo

Definir o componente responsável por aplicar as regras operacionais da Inteligência Artificial do Audio Copilot.

O Rule Engine funciona como a camada de governança da IA. Sua responsabilidade é garantir que todas as recomendações estejam em conformidade com as regras técnicas, operacionais e de segurança definidas pelo sistema.

Enquanto o Recommendation Engine responde **"o que pode ser recomendado?"**, o Rule Engine responde:

> **"Esta recomendação é permitida?"**

---

# Visão Geral

A Inteligência Artificial pode identificar inúmeras oportunidades de melhoria durante um evento.

Entretanto, nem toda recomendação é apropriada.

Algumas ações podem:

- gerar riscos;
- contrariar políticas da igreja;
- interromper a operação;
- confundir o operador.

O Rule Engine atua como um mecanismo de validação, impedindo que recomendações inadequadas cheguem ao operador.

---

# Filosofia

O Rule Engine foi desenvolvido seguindo cinco princípios.

## Segurança

Nenhuma recomendação deve colocar o evento em risco.

---

## Consistência

As mesmas situações devem produzir as mesmas decisões.

---

## Configurabilidade

Cada igreja poderá possuir suas próprias regras operacionais.

---

## Transparência

Toda regra aplicada deve ser identificável.

---

## Previsibilidade

O operador deve compreender o comportamento da IA.

---

# Arquitetura

```text
Recommendation Engine

↓

Rule Engine

↓

Safety Engine

↓

Confidence Engine

↓

Decision Engine

↓

Painel da IA
```

O Rule Engine atua logo após a geração da recomendação.

---

# Responsabilidades

O Rule Engine será responsável por:

- validar recomendações;
- aplicar regras operacionais;
- aplicar regras específicas da igreja;
- verificar restrições do modo atual;
- bloquear recomendações proibidas;
- classificar recomendações conforme políticas internas.

---

# Fontes de Regras

As regras poderão ser obtidas de diferentes origens.

Entre elas:

- configuração da igreja;
- configuração do evento;
- modo de operação;
- políticas de segurança;
- preferências do administrador;
- regras internas da IA.

---

# Fluxo de Funcionamento

```text
Nova Recomendação

↓

Consultar regras

↓

Aplicar restrições

↓

Validar

↓

Aprovada

ou

Bloqueada
```

---

# Tipos de Regras

## Regras Permanentes

São regras definidas pelo próprio sistema.

Exemplo:

```text
Nunca recomendar mutar o canal Master.
```

---

## Regras Configuráveis

Podem ser alteradas pelo administrador.

Exemplo:

```text
Permitir recomendações
para equalização.

Sim
```

---

## Regras por Evento

Podem variar conforme o evento.

Exemplo:

```text
Evento

Ensaio

↓

Permitir sugestões
mais frequentes.
```

---

## Regras por Operador

Cada operador poderá possuir um perfil próprio.

Exemplo:

```text
Operador

Iniciante

↓

Exibir explicações detalhadas.
```

---

# Exemplos

## Exemplo 1

A IA identifica clipping.

Recomendação:

```text
Reduzir ganho do Vocal Azul.
```

O Rule Engine verifica:

- operador possui permissão;
- modo permite recomendações;
- canal não está bloqueado.

Resultado:

```text
Recomendação aprovada.
```

---

## Exemplo 2

A IA sugere alterar o Master.

O Rule Engine encontra a regra:

```text
Alterações no Master

Proibidas.
```

Resultado:

```text
Recomendação bloqueada.
```

---

# Regras por Modo

O comportamento poderá variar conforme o modo operacional.

## Modo Ensaio

Permite:

- recomendações frequentes;
- sugestões experimentais;
- maior sensibilidade.

---

## Modo Culto

Prioriza:

- estabilidade;
- poucas interrupções;
- recomendações críticas.

---

## Modo Técnico

Permite:

- diagnósticos completos;
- verificações avançadas;
- recomendações detalhadas.

---

# Regras por Canal

Também poderão existir regras específicas.

Exemplo:

```text
Canal

Pastor

↓

Nunca sugerir mute.
```

Outro exemplo:

```text
Master

↓

Nunca sugerir aumento automático.
```

---

# Regras por Categoria

Cada categoria poderá possuir políticas diferentes.

Exemplo:

```text
Feedback

Permitido.
```

```text
Silêncio inesperado

Permitido.
```

```text
Alteração automática de EQ

Não permitido.
```

---

# Priorização

O Rule Engine poderá alterar a prioridade de uma recomendação.

Exemplo:

```text
Evento

Culto

↓

Feedback

↓

Prioridade

Alta
```

Durante um ensaio:

```text
Prioridade

Média
```

---

# Regras Temporais

Algumas recomendações poderão ser limitadas no tempo.

Exemplo:

```text
Repetir alerta

Somente após

30 segundos.
```

Isso evita excesso de notificações.

---

# Integração com o Safety Engine

Após validar uma recomendação, o Rule Engine encaminha o resultado ao Safety Engine.

O Safety Engine realiza uma segunda verificação voltada exclusivamente à segurança operacional.

---

# Integração com o Decision Engine

Somente recomendações aprovadas pelo Rule Engine seguem para o Decision Engine.

As demais são descartadas ou registradas para auditoria.

---

# Integração com o Learning Engine

O Learning Engine poderá sugerir novas regras ao administrador.

Exemplo:

```text
Foi observado que
o canal Playback
sempre permanece mutado
durante a Oração Inicial.

Deseja criar uma regra para esse comportamento?
```

A criação da regra dependerá sempre da aprovação do administrador.

---

# Registro das Regras

Toda regra aplicada poderá ser registrada.

Exemplo:

```text
09:42

Recomendação bloqueada.

Motivo

Alteração do Master proibida.
```

Esses registros auxiliam auditorias e depuração do sistema.

---

# Configuração

As regras poderão ser organizadas em categorias.

Exemplo:

```text
Operação

✓ Permitir recomendações

Segurança

✓ Bloquear alterações críticas

IA

✓ Explicar todas as recomendações

Notificações

✓ Agrupar alertas repetidos
```

---

# Benefícios

O Rule Engine proporciona:

- padronização da operação;
- maior previsibilidade da IA;
- personalização por igreja;
- controle administrativo;
- redução de riscos;
- conformidade com políticas operacionais.

---

# Separação de Responsabilidades

O Rule Engine não:

- gera recomendações;
- calcula confiança;
- aprende padrões;
- executa comandos na mesa;
- toma decisões finais sobre exibição.

Sua responsabilidade é validar cada recomendação com base nas regras operacionais configuradas.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- editor gráfico de regras;
- criação de regras sem programação;
- regras condicionais complexas;
- importação e exportação de políticas;
- bibliotecas de regras por denominação;
- perfis específicos por operador;
- controle de versões das regras;
- simulação de impacto antes da publicação.

---

# Relação com Outros Componentes

O Rule Engine trabalha diretamente com:

- Recommendation Engine;
- Context Manager;
- Confidence Engine;
- Safety Engine;
- Decision Engine;
- Learning Engine;
- Configuração do Evento;
- Dashboard Operacional;
- Painel da IA.

Ele representa a camada de governança da Inteligência Artificial, garantindo que todas as recomendações respeitem as políticas operacionais, técnicas e administrativas definidas para o Audio Copilot.

---

# Situação da Sprint

**Status:** ✅ Concluída