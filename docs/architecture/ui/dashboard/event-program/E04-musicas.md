# Sprint E04 – Músicas

## Objetivo

Definir o componente responsável pelo gerenciamento das músicas previstas para execução durante o evento.

O módulo de Músicas permite que o Audio Copilot saiba exatamente qual música está sendo executada, quais participantes deverão estar ativos, quais instrumentos serão utilizados e quais configurações operacionais poderão ser esperadas em cada momento.

Mais do que uma simples lista de músicas, este componente fornece contexto operacional para toda a aplicação.

---

# Visão Geral

Durante o momento de louvor, cada música possui características próprias.

Algumas utilizam todos os instrumentos.

Outras utilizam apenas voz e violão.

Algumas possuem playback.

Outras utilizam introduções longas ou encerramentos instrumentais.

Ao conhecer previamente essas informações, o Audio Copilot consegue compreender melhor o comportamento esperado da mesa de som durante cada música.

---

# Filosofia

O módulo de Músicas não substitui softwares de projeção ou aplicativos de cifras.

Seu objetivo é fornecer contexto operacional para a sonorização.

O foco é auxiliar o operador de áudio e fornecer informações para a Inteligência Artificial.

---

# Estrutura da Música

Cada música poderá conter informações como:

- título;
- autor;
- intérprete;
- duração prevista;
- tonalidade;
- andamento (BPM);
- observações;
- participantes;
- instrumentos utilizados;
- microfones utilizados.

Exemplo:

```text
Título

Sola Scriptura

Duração

4m30s

Tom

G

BPM

74

Participantes

• Alessandra
• Letícia
• Robson

Instrumentos

• Violão Martin
• Baixo
• Cajón

Microfones

• Vermelho
• Azul
• Verde
```

---

# Ordem das Músicas

Cada etapa de Louvor poderá conter uma sequência organizada de músicas.

Exemplo:

```text
Louvor

1. Sola Scriptura

2. Maravilhosa Graça

3. Cristo é Tudo

4. Em Cristo Somente

5. Doxologia
```

O operador poderá visualizar facilmente em qual música o evento se encontra.

---

# Música Atual

Durante a execução do evento, apenas uma música permanecerá ativa.

Exemplo:

```text
Louvor

Música 3 de 5

► Cristo é Tudo
```

Essa informação será utilizada por toda a aplicação.

---

# Próxima Música

O sistema também apresentará a próxima música da sequência.

Exemplo:

```text
Agora

Cristo é Tudo

Próxima

Em Cristo Somente
```

Isso permite que o operador antecipe possíveis ajustes.

---

# Participantes da Música

Cada música poderá possuir participantes específicos.

Exemplo:

```text
Cristo é Tudo

Vocal

• Alessandra

• Letícia

Violão

• Robson

Baixo

• João
```

Caso algum participante não participe daquela música, ele simplesmente não será listado.

---

# Instrumentos Utilizados

Cada música poderá definir exatamente quais instrumentos estarão ativos.

Exemplo:

```text
Instrumentos

✓ Violão Martin

✓ Baixo

✓ Cajón

✓ Playback

✕ Piano
```

Essa informação ajuda a IA a identificar comportamentos inesperados.

---

# Microfones Utilizados

Também poderão ser definidos os microfones previstos.

Exemplo:

```text
Mic Vermelho

Mic Azul

Mic Verde
```

Caso um microfone apresente atividade sem estar previsto para a música atual, a IA poderá gerar uma recomendação.

---

# Observações Operacionais

Cada música poderá conter observações importantes.

Exemplos:

- início apenas com violão;
- playback inicia na introdução;
- cajón entra no segundo verso;
- solo instrumental;
- encerramento em silêncio.

Essas informações auxiliam o operador durante a execução.

---

# Integração com a Inteligência Artificial

As informações da música atual fornecem contexto adicional para a IA.

Exemplo:

```text
Música

Sola Scriptura

Instrumentos previstos

• Violão
• Baixo
• Cajón
```

Caso o Piano apresente atividade, a IA poderá informar:

> Foi detectado sinal no canal do Piano, porém este instrumento não está previsto para a música atual.

Outro exemplo:

```text
Introdução apenas com violão.
```

Se o Baixo começar a tocar imediatamente, a IA poderá considerar esse comportamento como inesperado.

A decisão final permanece sempre com o operador.

---

# Integração com o Console

O Console poderá destacar automaticamente os canais utilizados pela música atual.

Exemplo:

Durante "Sola Scriptura":

- Violão em destaque;
- Vocais em destaque;
- Baixo em destaque;
- Cajón em destaque.

Os demais canais permanecerão minimizados.

---

# Integração com o Dashboard

O Dashboard poderá apresentar um resumo.

Exemplo:

```text
Agora

Cristo é Tudo

3 de 5

Próxima

Em Cristo Somente
```

---

# Integração com o Mobile

O aplicativo Mobile apresentará uma versão simplificada.

Exemplo:

```text
Agora

Cristo é Tudo

Próxima

Em Cristo Somente

Tempo previsto

4m20s
```

---

# Benefícios

A utilização do módulo de Músicas oferece diversas vantagens:

- fornece contexto operacional durante o louvor;
- melhora as recomendações da IA;
- reduz a necessidade de memorização pelo operador;
- facilita a antecipação de ajustes;
- integra programação musical e operação técnica;
- melhora a organização da equipe de sonorização.

---

# Separação de Responsabilidades

O módulo de Músicas possui responsabilidade única.

Ele não:

- controla a reprodução de playback;
- altera configurações da mesa;
- movimenta faders;
- envia comandos para a Ui24R;
- executa decisões da IA.

Sua função é representar o contexto musical do evento.

---

# Evoluções Futuras

Nas próximas versões, o módulo poderá incorporar funcionalidades como:

- integração com aplicativos de cifras e partituras;
- importação automática de repertórios;
- sincronização com softwares de projeção;
- associação de snapshots recomendados para cada música;
- histórico de execuções;
- estatísticas por música;
- recomendações automáticas de ajustes baseadas no histórico de eventos;
- aprendizado da IA sobre o comportamento de cada música ao longo do tempo.

---

# Relação com Outros Componentes

O módulo de Músicas trabalha em conjunto com:

- Painel da Liturgia;
- Timeline do Evento;
- Etapas da Liturgia;
- Participantes;
- Progresso do Evento;
- Painel da IA;
- Dashboard Operacional;
- Console de Operação.

Ele representa o contexto musical utilizado pela aplicação durante o momento de louvor.

---

# Situação da Sprint

**Status:** ✅ Concluída