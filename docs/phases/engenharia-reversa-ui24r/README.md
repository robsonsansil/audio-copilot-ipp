# Engenharia Reversa da Soundcraft Ui24R

## Objetivo

Esta pasta reúne toda a documentação técnica produzida durante a fase de Engenharia Reversa da Soundcraft Ui24R.

O objetivo desta fase é compreender completamente o funcionamento da comunicação entre a interface web da mesa de som e seu firmware, documentando o protocolo utilizado para que o Audio Copilot possa interagir com a Ui24R de forma segura, estável e totalmente compatível.

Toda a implementação da integração com a mesa será baseada no conhecimento adquirido nesta etapa.

---

# Escopo

Durante esta fase serão identificados e documentados:

- funcionamento da inicialização da mesa;
- carregamento da interface web;
- comunicação HTTP;
- comunicação WebSocket;
- parâmetros dos canais;
- equalização;
- compressor;
- gate;
- auxiliares;
- efeitos;
- cenas;
- presets;
- medidores;
- sincronização em tempo real;
- comportamento em reconexões;
- demais recursos necessários ao Audio Copilot.

---

# Metodologia

Cada funcionalidade da Ui24R será analisada individualmente.

Para cada sprint será realizada uma captura completa contendo:

- gravação da tela (OBS Studio);
- captura de rede (Wireshark);
- captura da comunicação do navegador (HAR).

Após cada captura será produzido um documento técnico contendo toda a análise realizada.

---

# Estrutura das Sprints

Cada sprint possui um único objetivo.

Essa estratégia reduz a quantidade de variáveis analisadas simultaneamente e facilita a identificação dos comandos utilizados pela Ui24R.

As sprints desta fase são:

- I01 — Inicialização da Ui24R
- I02 — Carregamento da Interface Web
- I03 — Reconexão da Interface
- I04 — Fader de um Canal
- I05 — Mute / Unmute
- I06 — Gain
- I07 — Pan
- I08 — Equalizador (EQ)
- I09 — Compressor
- I10 — Gate
- I11 — Auxiliares
- I12 — FX
- I13 — Cenas
- I14 — Presets
- I15 — RTA e Medidores
- I16 — Configurações Gerais
- I17 — Sincronização entre Navegadores
- I18 — Reconexão
- I19 — Medidores em Tempo Real
- I20 — Alterações Externas

---

# Estrutura de cada Sprint

Cada sprint deverá conter:

- objetivo;
- ambiente de teste;
- procedimento executado;
- resultados esperados;
- descobertas realizadas;
- comandos identificados;
- mensagens WebSocket;
- requisições HTTP;
- pacotes relevantes;
- conclusões;
- próximos passos.

---

# Evidências

As evidências geradas durante os testes serão armazenadas em uma pasta específica do projeto.

Cada sprint possuirá seu próprio conjunto de arquivos contendo:

- vídeo da captura (.mp4);
- captura do navegador (.har);
- captura de rede (.pcapng);
- observações técnicas (.md), quando necessário.

---

# Resultado Esperado

Ao término desta fase deverá existir uma documentação completa do protocolo utilizado pela Soundcraft Ui24R, suficiente para permitir o desenvolvimento de uma biblioteca própria de comunicação utilizada pelo Audio Copilot.

Essa documentação servirá como referência para as fases de implementação, testes, manutenção e futuras evoluções do sistema.

---

# Situação da Fase

**Status:** ⏳ Em andamento