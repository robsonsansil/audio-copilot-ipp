# Sprint I06 — Controle de Gain do Canal

## Objetivo

Implementar o controle do ganho (Gain) dos canais da mesa Soundcraft Ui24R.

Esta funcionalidade permitirá que o Audio Copilot IPP altere remotamente o pré-amplificador de qualquer canal, mantendo a comunicação via WebSocket já desenvolvida nas sprints anteriores.

---

## Funcionalidades

- alterar o Gain de um canal
- leitura do ganho atual
- envio automático para a Ui24R
- validação dos limites permitidos
- registro no log da aplicação

---

## Arquivos

src/ui24r/client.py

Novo método:

```python
set_gain(channel, value)