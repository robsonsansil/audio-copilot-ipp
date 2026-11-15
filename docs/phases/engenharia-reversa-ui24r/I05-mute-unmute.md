# Sprint I05 — Mute / Unmute de Canal

## Objetivo

Implementar o controle de **Mute / Unmute** dos canais da Soundcraft Ui24R através do Audio Copilot IPP.

Ao selecionar um canal, o operador poderá alterar seu estado de áudio instantaneamente, mantendo a interface sincronizada com a mesa.

---

## Motivação

O botão MUTE é uma das funções mais utilizadas durante uma operação ao vivo.

Ele permite:

- cortar imediatamente um microfone;
- silenciar instrumentos;
- evitar microfonias;
- preparar entradas antes de abrir o canal;
- controlar mudanças rápidas durante o culto.

---

## Funcionalidades

Nesta Sprint serão implementados:

- botão Mute;
- botão Unmute;
- leitura do estado atual;
- atualização automática da interface;
- indicação visual do estado do canal.

---

## Interface

Cada canal deverá possuir um indicador semelhante ao da Ui24R.

Exemplo:

🟢 ON

🔴 MUTE

A mudança deve ocorrer imediatamente após a confirmação recebida da mesa.

---

## Fluxo

1. Operador seleciona um canal.

2. Clica em **Mute**.

3. Audio Copilot envia o comando para a Ui24R.

4. A mesa altera o estado.

5. O Audio Copilot recebe a atualização.

6. Interface muda para:

🔴 MUTE

O processo inverso ocorre para Unmute.

---

## Comunicação

Toda alteração deverá ocorrer através do canal WebSocket já estabelecido com a Ui24R.

O sistema não deverá assumir que o comando foi executado.

A confirmação sempre deverá vir da própria mesa.

---

## Segurança

Evitar envio duplicado de comandos.

Caso o canal já esteja em Mute, não enviar novo comando.

O mesmo vale para Unmute.

---

## Estrutura prevista

src/
└── ui24r/
    ├── mute.py
    ├── websocket.py
    └── channel.py

---

## Eventos

O sistema deverá emitir eventos como:

CHANNEL_MUTED

CHANNEL_UNMUTED

STATE_UPDATED

---

## Interface gráfica

O canal deverá apresentar:

- botão Mute;
- botão Unmute;
- indicador de estado;
- atualização em tempo real.

---

## Critérios de aceite

✔ alterar estado do canal

✔ refletir alteração na interface

✔ sincronizar automaticamente

✔ evitar comandos duplicados

✔ registrar a operação no log

✔ funcionamento em tempo real

---

## Resultado esperado

Ao final desta Sprint o Audio Copilot será capaz de controlar completamente o estado de Mute dos canais da Soundcraft Ui24R, mantendo a interface sincronizada com a mesa em tempo real e servindo de base para as próximas funções de automação.