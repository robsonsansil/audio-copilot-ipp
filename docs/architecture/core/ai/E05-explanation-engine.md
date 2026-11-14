# Sprint E05 – Explanation Engine

## Objetivo

Definir o componente responsável por explicar, de forma clara e transparente, todas as recomendações produzidas pela Inteligência Artificial.

O Explanation Engine transforma decisões técnicas da IA em mensagens compreensíveis para o operador, permitindo que ele entenda exatamente por que determinada recomendação foi gerada.

Seu objetivo é aumentar a confiança do operador, reduzir a sensação de "caixa-preta" da IA e facilitar a tomada de decisão durante a operação da mesa de som.

---

# Visão Geral

Uma Inteligência Artificial não deve apenas recomendar.

Ela também deve explicar.

Por exemplo, ao invés de apresentar apenas:

```text
Reduza o ganho do Vocal Azul.
```

A IA deverá informar:

```text
Foi detectado clipping contínuo durante os últimos 8 segundos.

Recomenda-se reduzir aproximadamente 2 dB no ganho do canal.
```

O operador entende o motivo da sugestão e decide se deseja aplicá-la.

---

# Filosofia

O Explanation Engine foi desenvolvido seguindo cinco princípios.

## Transparência

Toda recomendação deve possuir uma justificativa.

---

## Clareza

A linguagem utilizada deve ser simples e objetiva.

---

## Contexto

A explicação deve considerar o momento do evento.

---

## Educação

As explicações também ajudam operadores iniciantes a compreender conceitos de sonorização.

---

## Confiança

Quanto melhor a explicação, maior será a confiança do operador na IA.

---

# Arquitetura

```text
Recommendation Engine

↓

Decision Engine

↓

Confidence Engine

↓

Explanation Engine

↓

Painel da IA

↓

Console Operacional

↓

Operador
```

O Explanation Engine representa a última etapa antes da apresentação da recomendação.

---

# Responsabilidades

O Explanation Engine será responsável por:

- gerar explicações para todas as recomendações;
- descrever as evidências encontradas;
- apresentar o contexto da análise;
- informar o nível de confiança;
- justificar a recomendação;
- adaptar a linguagem ao perfil do operador.

---

# Fontes de Informação

As explicações poderão utilizar informações provenientes de:

- Recommendation Engine;
- Context Manager;
- Confidence Engine;
- Rule Engine;
- Safety Engine;
- Learning Engine;
- Telemetry Manager;
- Statistics.

---

# Fluxo de Funcionamento

```text
Recomendação

↓

Coletar Evidências

↓

Construir Explicação

↓

Adicionar Contexto

↓

Adicionar Confiança

↓

Enviar para Interface
```

---

# Estrutura da Explicação

Uma explicação poderá conter:

- situação identificada;
- evidências encontradas;
- contexto operacional;
- motivo da recomendação;
- ação sugerida;
- nível de confiança.

Exemplo:

```text
Situação

Feedback detectado.

Motivo

Foi observado aumento contínuo de energia em 2,5 kHz
durante os últimos 6 segundos.

Sugestão

Reduzir aproximadamente 2 dB
no retorno do Monitor 2.

Confiança

96%
```

---

# Explicações Contextuais

A mesma recomendação poderá possuir explicações diferentes dependendo da etapa da liturgia.

Exemplo:

```text
Canal do Baixo sem sinal.
```

Durante o Louvor:

```text
O Baixo faz parte da formação prevista para esta música.

Verifique o cabo ou a conexão do instrumento.
```

Durante a Pregação:

```text
Situação esperada.

O Baixo não está previsto para esta etapa.
```

---

# Explicações Baseadas em Histórico

O Learning Engine poderá enriquecer as explicações.

Exemplo:

```text
Nas últimas 18 ocorrências semelhantes,
este ajuste foi realizado pelo operador.

Deseja repetir essa ação?
```

---

# Explicações Técnicas

Para operadores experientes, a IA poderá fornecer detalhes adicionais.

Exemplo:

```text
Clipping detectado.

Pico máximo

+1,8 dBFS

Duração

9 segundos.
```

---

# Explicações Simplificadas

Para operadores iniciantes, a linguagem poderá ser mais acessível.

Exemplo:

```text
O volume deste microfone está muito alto
e está começando a distorcer.

Reduzir um pouco o ganho pode melhorar a qualidade do áudio.
```

---

# Níveis de Detalhamento

O sistema poderá oferecer diferentes níveis de explicação.

## Resumido

```text
Feedback detectado.

Reduza o retorno.
```

---

## Normal

```text
Foi identificado início de microfonia.

Sugere-se reduzir aproximadamente
2 dB no retorno do palco.
```

---

## Completo

```text
Foi identificado aumento contínuo
na região de 2,5 kHz durante
os últimos 8 segundos.

O padrão é compatível com
microfonia inicial.

Recomenda-se reduzir aproximadamente
2 dB no Monitor 2.

Confiança

97%
```

---

# Explicações Educativas

O Explanation Engine também poderá ensinar conceitos de áudio.

Exemplo:

```text
O clipping ocorre quando o sinal ultrapassa
o limite máximo permitido,
produzindo distorção.

Reduzir o ganho evita esse problema.
```

Esse recurso será especialmente útil para operadores em treinamento.

---

# Integração com o Dashboard

O Dashboard exibirá apenas explicações resumidas.

Exemplo:

```text
IA

Feedback detectado
no Monitor 2.
```

---

# Integração com o Console

No Console Operacional, o operador poderá visualizar a explicação completa.

Exemplo:

```text
Canal

Vocal Azul

Problema

Clipping contínuo.

Motivo

Ganho elevado.

Sugestão

Reduzir aproximadamente 2 dB.

Confiança

94%
```

---

# Integração com o Mobile

No aplicativo Mobile serão apresentadas explicações curtas.

Exemplo:

```text
Microfone Verde

Sem sinal.

Verifique a bateria.
```

---

# Registro das Explicações

Todas as explicações poderão ser armazenadas juntamente com as recomendações.

Exemplo:

```text
09:42

Recomendação

Reduzir retorno.

Explicação

Início de microfonia detectado.
```

Esses registros facilitarão auditorias e treinamentos futuros.

---

# Benefícios

O Explanation Engine proporciona:

- maior transparência da IA;
- aumento da confiança do operador;
- aprendizado contínuo da equipe;
- redução da sensação de "caixa-preta";
- suporte à tomada de decisão;
- melhor experiência de uso.

---

# Separação de Responsabilidades

O Explanation Engine não:

- gera recomendações;
- toma decisões;
- calcula confiança;
- aprende padrões;
- altera configurações da mesa.

Sua única responsabilidade é transformar análises técnicas em explicações claras, objetivas e compreensíveis para o operador.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- explicações personalizadas por operador;
- suporte multilíngue;
- explicações por voz durante o evento;
- tutoriais contextuais;
- exemplos visuais de problemas de áudio;
- integração com documentação técnica;
- modo de treinamento para novos operadores;
- geração automática de relatórios explicativos após o evento.

---

# Relação com Outros Componentes

O Explanation Engine trabalha diretamente com:

- Recommendation Engine;
- Decision Engine;
- Confidence Engine;
- Rule Engine;
- Safety Engine;
- Learning Engine;
- Context Manager;
- Telemetry Manager;
- Dashboard Operacional;
- Console Operacional;
- Painel da IA;
- Mobile.

Ele representa a camada de comunicação da Inteligência Artificial do Audio Copilot, traduzindo análises técnicas complexas em informações claras, transparentes e úteis para o operador, fortalecendo a confiança na IA e preservando o controle humano sobre toda a operação.

---

# Situação da Sprint

**Status:** ✅ Concluída