# Preset — Violão Martin

Categoria: Instrumentos
Mesa: Soundcraft Ui24R
Versão: 3.0

---

# Entrada

| Parâmetro | Valor |
|-----------|------:|
| Phantom Power | OFF |
| Hi-Z | OFF (utilizando Direct Box) |
| Polaridade | Normal |
| Delay | 0 ms |
| Gain (Pré) | Ajustar para picos entre **-12 dB** e **-6 dB** (referência inicial: +8 dB) |
| Fader | 0 dB (Unidade) |

> Ajustar o ganho durante a passagem de som conforme a intensidade da execução.

---

# Configuração do Violão

| Controle | Valor |
|-----------|------:|
| Volume | 100% |
| Bass | Centro |
| Middle | Centro |
| Treble | Centro |
| Presence | Centro |
| Notch Filter | OFF |
| Phase | Normal |

A equalização principal será realizada na Ui24R.

---

# Filtros

| Filtro | Valor |
|--------|------:|
| 🔵 HPF | 80 Hz / 12 dB/Oct |
| 🟠 LPF | 12 kHz / 12 dB/Oct |

Objetivos:

- remover graves que pertencem ao baixo;
- eliminar ruídos do captador;
- preservar somente as frequências úteis do instrumento.

---

# Equalizador (EQ)

## 🔵 HPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **80 Hz** |
| Inclinação | **12 dB/Oct** |

---

## 🟢 Banda 1 — Graves

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **120 Hz** |
| Ganho | **-2 dB** |
| Q | **0,8** |

Objetivo:

Evitar conflito com o baixo e o cajón.

---

## 🔴 Banda 2 — Médio-Graves

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **300 Hz** |
| Ganho | **-3 dB** |
| Q | **1,2** |

Objetivo:

Eliminar o som "caixa de madeira".

---

## 🟣 Banda 3 — Presença

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **2,8 kHz** |
| Ganho | **+2 dB** |
| Q | **1,0** |

Objetivo:

Melhorar definição das palhetadas e dedilhados.

---

## 🟡 Banda 4 — Brilho

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **6 kHz** |
| Ganho | **+1,5 dB** |
| Q | **0,8** |

Objetivo:

Adicionar brilho natural sem deixar o timbre metálico.

---

## 🟠 LPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **12 kHz** |
| Inclinação | **12 dB/Oct** |

Objetivo:

Eliminar ruídos muito agudos do captador piezo.

---

# 🟤 Gate (dbx)

| Parâmetro | Valor |
|-----------|------:|
| Threshold | -55 dB |
| Attack | 8 ms |
| Hold | 80 ms |
| Release | 180 ms |
| Depth | -12 dB |

### Objetivo

- reduzir ruídos quando o músico não está tocando;
- preservar o sustain dos acordes;
- evitar abertura e fechamento perceptíveis.

---

# 🟠 Compressor (dbx)

| Parâmetro | Valor |
|-----------|------:|
| Threshold | -20 dB |
| Ratio | 2,5:1 |
| Attack | 20 ms |
| Release | 180 ms |
| Makeup Gain | +1 dB |
| Knee | Soft Knee |

### Objetivo

- controlar diferenças entre dedilhado e batidas;
- manter o violão consistente na mix;
- preservar a dinâmica natural.

---

# 🎚️ AUX Sends

## PA

Enviar normalmente para o LR.

---

## Monitor

| Fonte | Nível |
|--------|------:|
| Violão | **0 dB** |
| Voz Principal | **-4 dB** |
| Demais Vozes | **-8 dB** |
| Teclado | **-10 dB** |
| Baixo | **-10 dB** |
| Cajón | **-12 dB** |

---

# ✨ FX

## Reverb

| Parâmetro | Valor |
|-----------|------:|
| Tipo | Hall |
| Tempo | 1,6 s |
| Pre Delay | 15 ms |
| Send | -20 dB |

Objetivo:

Adicionar ambiência mantendo definição dos acordes.

---

## Delay

OFF

---

# Característica Sonora

Este preset busca:

- violão natural;
- médios limpos;
- excelente definição;
- brilho equilibrado;
- ótima integração com o baixo;
- sem competir com os vocais;
- excelente para dedilhados e batidas.

---

# Ajustes Finais

Durante a passagem de som:

- Regular o Gain para picos entre **-12 dB** e **-6 dB**.
- Manter o Fader em **0 dB**.
- Ajustar o volume da mix utilizando apenas o fader.
- Se faltar definição, aumentar levemente a **🟣 Banda 3 (2,8 kHz)**.
- Se o violão estiver "duro" ou metálico, reduzir primeiro a **🟡 Banda 4 (6 kHz)**.
- Se houver excesso de grave, reduzir a **🟢 Banda 1 (120 Hz)** antes de diminuir o volume geral.

---

# Observações

Este preset foi desenvolvido especificamente para a:

**Igreja Presbiteriana de Piracicaba**

Considerando:

- Soundcraft Ui24R;
- PA Dommer;
- 2 Subwoofers LL Audio;
- 2 Monitores de palco;
- Louvor congregacional.

Foi otimizado para trabalhar em conjunto com os presets de:

- Vocal Masculino;
- Vocal Feminino;
- Púlpito;
- Baixo CL-200 Ativo;
- Teclado;
- Cajón.