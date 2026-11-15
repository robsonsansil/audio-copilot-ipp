# Sprint I04 — Controle de Fader do Canal

## Objetivo

Implementar o controle do fader de um canal da Soundcraft Ui24R através do Audio Copilot IPP.

Ao final deste Sprint será possível:

- localizar um canal pelo índice;
- alterar o volume do fader;
- ler o valor atual;
- aplicar limites de segurança;
- validar a comunicação com a mesa.

---

## Motivação

Após estabelecer a comunicação e permitir reconexão automática (Sprint I03), o próximo passo é começar a controlar parâmetros da mesa.

O fader é o primeiro controle por ser:

- simples;
- seguro;
- amplamente utilizado;
- base para automações futuras.

Todo o restante (Mute, Gain, EQ, Compressor, Gate, Aux etc.) utilizará exatamente a mesma arquitetura.

---

## Estrutura

Criar:

```
src/
└── ui24r/
    └── fader.py
```

---

## Classe

Criar:

```python
ChannelFader
```

Responsável por:

- obter valor do fader
- alterar valor
- validar limites
- enviar comandos à Ui24R

---

## Métodos previstos

### set()

Define o valor do fader.

Exemplo:

```python
set(channel=5, value=-10)
```

---

### get()

Obtém o valor atual.

Exemplo:

```python
get(channel=5)
```

Retorno:

```python
-8.3
```

---

### mute()

(opcional neste Sprint)

Deixar preparado para futura implementação.

---

## Escala utilizada

Utilizar a escala nativa da Ui24R.

Exemplo:

```
+10 dB

0 dB

-5 dB

-10 dB

-20 dB

-40 dB

-∞
```

---

## Validações

O método deverá impedir:

- canal inexistente;
- valores fora da faixa permitida;
- conexão inexistente.

Exemplo:

```
Canal inválido.

Valor fora do intervalo permitido.

Mesa desconectada.
```

---

## Testes

Criar:

```
tests/test_fader.py
```

Testes:

- leitura do valor;
- alteração do valor;
- alteração repetida;
- valores extremos;
- erro de conexão.

---

## Critérios de aceite

O Sprint será considerado concluído quando:

- [ ] o Audio Copilot alterar corretamente o fader;
- [ ] conseguir ler o valor atual;
- [ ] validar limites;
- [ ] impedir erros de faixa;
- [ ] funcionar com a Ui24R real;
- [ ] testes executarem sem falhas.

---

## Resultado esperado

Ao final deste Sprint será possível executar algo como:

```python
from ui24r.connection import Ui24R
from ui24r.fader import ChannelFader

mesa = Ui24R()

mesa.connect()

fader = ChannelFader(mesa)

print(fader.get(5))

fader.set(5, -8)

print(fader.get(5))
```

---

## Próximo Sprint

**I05 — Mute de Canal**

Será implementado o controle de mute utilizando a mesma arquitetura desenvolvida neste Sprint.