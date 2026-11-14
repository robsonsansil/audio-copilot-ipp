# Preset — Violão Yamaha

Categoria: Instrumentos

Mesa: Soundcraft Ui24R

Versão: 1.0

---

# Aplicação

Preset desenvolvido especificamente para o violão **Yamaha APX-6A** utilizado no louvor da Igreja Presbiteriana de Piracicaba.

O APX-6A possui corpo fino (Thinline), excelente definição e projeção para palco, porém produz menos graves naturais que um violão tradicional. Este preset busca compensar essas características sem perder a clareza.

Objetivos:

- timbre natural;
- excelente definição;
- graves equilibrados;
- redução do som metálico do captador piezo;
- ótima presença na mix.

---

# Entrada

| Parâmetro | Valor |
|-----------|------:|
| Phantom Power | OFF |
| Polaridade | Normal |
| Hi-Z | OFF |
| Delay | 0 ms |
| Gain (Pré) | Ajustar para picos entre **-12 dB** e **-6 dB** |
| Fader | 0 dB |

---

# Filtros

## 🔵 HPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **80 Hz** |
| Inclinação | **12 dB/Oct** |

Objetivo:

Eliminar graves desnecessários preservando o corpo do instrumento.

---

## 🟠 LPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **11 kHz** |
| Inclinação | **12 dB/Oct** |

Objetivo:

Reduzir o excesso de brilho característico do captador piezo Yamaha.

---

# Equalizador

## 🟢 Banda 1 — Corpo

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **140 Hz** |
| Ganho | **+2 dB** |
| Q | **0,8** |

Objetivo:

Recuperar parte dos graves perdidos pelo corpo fino do APX.

---

## 🔴 Banda 2 — Médio-Graves

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **350 Hz** |
| Ganho | **-2 dB** |
| Q | **1,2** |

Objetivo:

Eliminar o som "caixa".

---

## 🟣 Banda 3 — Presença

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **2,8 kHz** |
| Ganho | **+2 dB** |
| Q | **1,0** |

Objetivo:

Destacar palhetadas e dedilhados.

---

## 🟡 Banda 4 — Brilho

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **6 kHz** |
| Ganho | **-1 dB** |
| Q | **0,8** |

Objetivo:

Suavizar o brilho excessivo típico do captador piezo.

---

# 🟤 Gate (dbx)

| Parâmetro | Valor |
|-----------|------:|
| Threshold | **-55 dB** |
| Attack | **5 ms** |
| Hold | **120 ms** |
| Release | **220 ms** |
| Depth | **-15 dB** |

Objetivo:

Eliminar ruídos quando o instrumento estiver sem execução.

---

# 🟠 Compressor (dbx)

| Parâmetro | Valor |
|-----------|------:|
| Threshold | **-22 dB** |
| Ratio | **3:1** |
| Attack | **20 ms** |
| Release | **180 ms** |
| Makeup Gain | **+2 dB** |
| Knee | **Soft Knee** |

Objetivo:

Controlar a dinâmica mantendo a expressividade do músico.

---

# 🎚️ AUX Sends

## PA

Enviar normalmente para o LR.

---

## Monitor

| Fonte | Nível |
|--------|------:|
| Violão Yamaha APX-6A | **0 dB** |

Ajustar conforme necessidade do músico.

---

# ✨ FX

## Reverb

| Parâmetro | Valor |
|-----------|------:|
| Tipo | Hall |
| Tempo | **1,8 s** |
| Pre Delay | **20 ms** |
| Send | **-24 dB** |

Objetivo:

Adicionar profundidade sem comprometer a definição.

---

## Delay

OFF

---

# Característica Sonora

Este preset busca proporcionar:

- timbre natural;
- médios equilibrados;
- graves mais encorpados;
- redução do brilho metálico do piezo;
- excelente definição para bases e dedilhados.

---

# Ajustes Durante a Passagem de Som

- Ajustar o Gain para picos entre **-12 dB** e **-6 dB**.
- Manter o Fader em **0 dB**.
- Ajustar o volume utilizando apenas o fader.
- Caso o violão fique muito metálico, reduzir a 🟣 Banda 3 em 1 dB.
- Caso fique muito brilhante, reduzir a 🟡 Banda 4 em até 2 dB.
- Caso falte corpo, aumentar a 🟢 Banda 1 em até +1 dB.

---

# Procedimento em Caso de Microfonia

1. Verificar o volume dos monitores.
2. Confirmar a posição do músico em relação aos PA.
3. Reduzir primeiro a 🟣 Banda 3 (2,8 kHz).
4. Persistindo a microfonia, reduzir a 🟡 Banda 4 (6 kHz).

---

# Observações

Este preset foi desenvolvido especificamente para a:

**Igreja Presbiteriana de Piracicaba**

Considerando:

- Soundcraft Ui24R;
- 2 PA Dommer;
- 2 Subwoofers LL Audio;
- 2 Monitores de palco;
- Violão Yamaha APX-6A;
- Louvor congregacional.

Foi otimizado para trabalhar em conjunto com os presets de:

- Vocal Masculino;
- Vocal Feminino;
- Púlpito;
- Microfone Sem Fio;
- Violão Martin;
- Guitarra;
- Baixo CL-200 Ativo;
- Teclado;
- Cajón.