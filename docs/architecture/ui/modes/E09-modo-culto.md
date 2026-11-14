# Sprint E09 – Modo Culto

## Objetivo

Definir o modo operacional utilizado durante a execução de cultos e eventos ao vivo, permitindo que o Audio Copilot acompanhe continuamente toda a operação da mesa de som, oferecendo suporte inteligente ao operador sem comprometer a estabilidade da mixagem.

O **Modo Culto** representa o ambiente de produção do Audio Copilot. Nele, a prioridade deixa de ser o aprendizado e passa a ser a execução segura, estável e confiável.

Enquanto o **Modo Ensaio** incentiva experimentações, observações e aprendizado, o Modo Culto prioriza previsibilidade, baixa interferência e assistência contextual.

---

# Visão Geral

Durante um culto, qualquer alteração pode impactar diretamente a experiência da igreja.

Por esse motivo, o Audio Copilot atua como um copiloto operacional, auxiliando o operador sem substituir suas decisões.

Durante o evento o sistema poderá:

- monitorar continuamente a mesa;
- acompanhar a liturgia;
- detectar situações críticas;
- apresentar alertas discretos;
- sugerir ações quando necessário;
- registrar todo o histórico do culto.

---

# Filosofia

O Modo Culto foi desenvolvido seguindo cinco princípios.

## Estabilidade

A prioridade máxima é manter a operação estável.

---

## Segurança

Nenhuma ação automática deve comprometer a execução do culto.

---

## Assistência

A IA deve auxiliar o operador sem interromper seu fluxo de trabalho.

---

## Discrição

As recomendações devem aparecer apenas quando realmente agregarem valor.

---

## Confiabilidade

Toda sugestão deve ser baseada no contexto atual do evento e no conhecimento adquirido durante os ensaios.

---

# Objetivos do Modo Culto

Durante o culto, o Audio Copilot deverá:

- monitorar continuamente a operação;
- acompanhar a execução da liturgia;
- detectar riscos operacionais;
- emitir alertas quando necessário;
- registrar eventos importantes;
- documentar toda a sessão;
- auxiliar o operador com recomendações contextualizadas.

---

# Arquitetura

```text
Operador

↓

Modo Culto

↓

Worship Manager

↓

Live Monitor

↓

Live Assistant

↓

Alert Manager

↓

History Manager
```

---

# Fluxo Geral

```text
Iniciar Culto

↓

Preparar Sistema

↓

Monitorar Operação

↓

Detectar Eventos

↓

Emitir Alertas

↓

Registrar Histórico

↓

Encerrar Culto
```

---

# Prioridades Operacionais

Durante o culto, o sistema priorizará:

- estabilidade da mixagem;
- inteligibilidade da voz;
- prevenção de clipping;
- prevenção de feedback;
- continuidade da operação;
- mínima distração ao operador.

---

# Comportamento da IA

No Modo Culto, a Inteligência Artificial atua de forma conservadora.

Ela poderá:

- sugerir ajustes;
- antecipar problemas;
- detectar situações críticas;
- identificar padrões conhecidos.

Ela não deverá:

- alterar parâmetros automaticamente;
- interromper o operador;
- executar mudanças sem autorização;
- gerar excesso de notificações.

---

# Monitoramento Contínuo

Durante toda a execução serão monitorados:

- Peak;
- RMS;
- Headroom;
- Clipping;
- Silence Detector;
- Noise Floor;
- canais ativos;
- snapshots carregados.

---

# Acompanhamento da Liturgia

O sistema acompanhará a evolução do evento.

Exemplo:

```text
Pré-Culto

↓

Abertura

↓

Louvor

↓

Oferta

↓

Avisos

↓

Pregação

↓

Ceia

↓

Encerramento
```

Cada etapa poderá possuir recomendações específicas.

---

# Assistência Inteligente

O Audio Copilot poderá apresentar sugestões discretas.

Exemplos:

```text
Canal 08

↓

Próximo do clipping
```

Ou:

```text
Microfone Pastor

↓

Sem sinal
```

Ou:

```text
Snapshot da Pregação

↓

Pronto para utilização
```

As recomendações deverão ser exibidas sem interromper a operação.

---

# Alertas

O sistema poderá emitir alertas para situações importantes.

Exemplos:

- clipping persistente;
- ausência de sinal;
- canal em mute inesperadamente;
- phantom power desligado;
- risco de feedback;
- sobrecarga em auxiliares.

Os alertas serão classificados por prioridade.

---

# Registro de Eventos

Durante o culto serão registrados eventos relevantes.

Exemplo:

```text
19:02

Culto iniciado

↓

19:18

Snapshot Louvor

↓

19:41

Pastor iniciou

↓

20:15

Culto encerrado
```

---

# Registro de Ajustes

Todas as alterações realizadas pelo operador continuarão sendo registradas.

Exemplo:

```text
Canal 05

↓

Gain

+2 dB

↓

Operador
```

Essas informações alimentarão o histórico da sessão.

---

# Recomendações

As sugestões da IA serão mais restritivas que no Modo Ensaio.

Serão apresentadas apenas quando:

- houver risco operacional;
- existir alta confiança;
- a recomendação for realmente útil;
- não causar distração.

---

# Segurança Operacional

Durante o culto o sistema deverá evitar:

- alterações automáticas;
- excesso de notificações;
- mudanças experimentais;
- recomendações repetitivas.

Toda decisão final permanecerá sob responsabilidade do operador.

---

# Integração com a IA

O Modo Culto utiliza informações produzidas por:

- Context Manager;
- Recommendation Engine;
- Decision Engine;
- Confidence Engine;
- Safety Engine.

Esses componentes trabalham em conjunto para produzir recomendações confiáveis.

---

# Integração com o Histórico

Todo o culto será documentado.

Serão registrados:

- eventos;
- alertas;
- recomendações;
- alterações;
- snapshots;
- métricas.

Essas informações poderão ser consultadas posteriormente.

---

# Integração com a Telemetria

A telemetria permanece ativa durante todo o culto.

Os dados são utilizados para:

- detectar clipping;
- identificar perda de sinal;
- medir headroom;
- acompanhar estabilidade da mixagem;
- alimentar os alertas em tempo real.

---

# Integração com a Liturgia

A programação do culto orienta diversas decisões da IA.

Exemplo:

```text
Pregação

↓

Microfone Pastor

↓

Maior prioridade
```

Ou:

```text
Louvor

↓

Playback

↓

Monitoramento reforçado
```

---

# Diferenças em relação ao Modo Ensaio

| Modo Ensaio | Modo Culto |
|-------------|------------|
| Aprendizado ativo | Operação estável |
| Experimentação permitida | Experimentação evitada |
| Sugestões frequentes | Sugestões apenas quando necessário |
| Ajustes constantes | Mínimas alterações |
| Observação detalhada | Monitoramento em tempo real |
| Ênfase em aprendizado | Ênfase em estabilidade |

---

# Benefícios

O Modo Culto proporciona:

- maior segurança operacional;
- monitoramento contínuo;
- suporte inteligente ao operador;
- redução de erros durante o evento;
- documentação automática do culto;
- melhor utilização do conhecimento adquirido nos ensaios.

---

# Separação de Responsabilidades

O Modo Culto não:

- substitui o operador;
- altera automaticamente a mesa;
- executa decisões críticas;
- realiza experimentações;
- modifica configurações sem autorização.

Sua responsabilidade é oferecer suporte inteligente, contextual e seguro durante toda a execução do culto.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- detecção automática do início das etapas da liturgia;
- reconhecimento de voz do pregador;
- identificação automática dos músicos em atividade;
- integração com projeção e iluminação;
- sincronização com transmissão ao vivo;
- previsão de riscos operacionais baseada em IA;
- suporte remoto entre operadores;
- operação distribuída em múltiplas mesas.

---

# Relação com Outros Componentes

O Modo Culto trabalha diretamente com:

- Worship Manager;
- Live Session;
- Live Monitor;
- Alert Manager;
- Safe Mode;
- Event Tracker;
- Live Assistant;
- Worship Report;
- History Manager;
- Telemetry Manager;
- Recommendation Engine;
- Safety Engine;
- Dashboard Operacional;
- Console Operacional.

Ele representa o ambiente operacional principal do Audio Copilot, aplicando em tempo real todo o conhecimento adquirido durante os ensaios para oferecer uma operação segura, estável e inteligente, sempre mantendo o operador como responsável pelas decisões finais.

---

# Situação da Sprint

**Status:** ✅ Concluída