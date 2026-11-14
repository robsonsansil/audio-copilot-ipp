# Preset — Microfone Sem Fio

Categoria: Vozes
Mesa: Soundcraft Ui24R
Versão: 3.0

---

# Aplicação

Este preset foi desenvolvido para microfones sem fio utilizados em:

- avisos;
- leitura bíblica;
- testemunhos;
- dirigentes;
- visitantes;
- pregações ocasionais;
- uso em qualquer ponto do templo.

É otimizado para minimizar riscos de microfonia, mesmo quando o usuário estiver próximo ao PA.

---

# Entrada

| Parâmetro | Valor |
|-----------|------:|
| Phantom Power | OFF |
| Polaridade | Normal |
| Delay | 0 ms |
| Gain (Pré) | Ajustar para picos entre **-12 dB** e **-6 dB** (referência inicial: +8 dB) |
| Fader | 0 dB (Unidade) |

---

# Filtros

| Filtro | Valor |
|--------|------:|
| 🔵 HPF | 120 Hz / 12 dB/Oct |
| 🟠 LPF | 16 kHz / 12 dB/Oct |

Objetivos:

- reduzir ruídos de manuseio;
- minimizar vibrações;
- aumentar a estabilidade contra microfonia.

---

# Equalizador (EQ)

## 🔵 HPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **120 Hz** |
| Inclinação | **12 dB/Oct** |

Objetivo:

Eliminar graves que favorecem a realimentação.

---

## 🟢 Banda 1 — Graves

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **180 Hz** |
| Ganho | **-3 dB** |
| Q | **1,0** |

Objetivo:

Reduzir o excesso de corpo da voz.

---

## 🔴 Banda 2 — Médio-Graves

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **320 Hz** |
| Ganho | **-4 dB** |
| Q | **1,2** |

Objetivo:

Eliminar abafamento e reduzir tendência à microfonia.

---

## 🟣 Banda 3 — Presença

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **2,8 kHz** |
| Ganho | **+2 dB** |
| Q | **1,0** |

Objetivo:

Melhorar a inteligibilidade tanto para vozes masculinas quanto femininas.

---

## 🟡 Banda 4 — Clareza

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **5,5 kHz** |
| Ganho | **+1 dB** |
| Q | **0,8** |

Objetivo:

Adicionar definição sem favorecer excessivamente a microfonia.

---

## 🟠 LPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **16 kHz** |
| Inclinação | **12 dB/Oct** |

Objetivo:

Eliminar frequências muito altas que favorecem apitos.

---

# De-Esser

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **6,5 kHz** |
| Threshold | **-30 dB** |
| Ratio | **2:1** |

Objetivo:

Controlar sibilâncias naturais de homens e mulheres.

---

# 🟤 Gate (dbx)

| Parâmetro | Valor |
|-----------|------:|
| Threshold | **-45 dB** |
| Attack | **5 ms** |
| Hold | **120 ms** |
| Release | **220 ms** |
| Depth | **-20 dB** |

### Objetivo

- reduzir ruído ambiente;
- diminuir vazamento do PA;
- evitar abertura constante do canal;
- preservar o final das frases.

---

# 🟠 Compressor (dbx)

| Parâmetro | Valor |
|-----------|------:|
| Threshold | **-20 dB** |
| Ratio | **2,5:1** |
| Attack | **15 ms** |
| Release | **150 ms** |
| Makeup Gain | **+1 dB** |
| Knee | **Soft Knee** |

### Objetivo

- nivelar diferentes tipos de voz;
- evitar picos repentinos;
- manter boa inteligibilidade.

---

# 🎚️ AUX Sends

## PA

Enviar normalmente para o LR.

---

## Monitor

| Fonte | Nível |
|--------|------:|
| Própria Voz | **0 dB** |

Evitar excesso de retorno para reduzir riscos de microfonia.

---

# ✨ FX

## Reverb

| Parâmetro | Valor |
|-----------|------:|
| Tipo | Plate |
| Tempo | **1,4 s** |
| Pre Delay | **15 ms** |
| Send | **-24 dB** |

Objetivo:

Adicionar leve ambiência sem prejudicar a compreensão.

---

## Delay

OFF

---

# Característica Sonora

Este preset busca:

- excelente inteligibilidade;
- boa adaptação para vozes masculinas e femininas;
- baixa tendência à microfonia;
- estabilidade durante movimentação pelo templo;
- clareza para leitura e fala.

---

# Ajustes Finais

Durante a passagem de som:

- Ajustar o Gain para picos entre **-12 dB** e **-6 dB**.
- Manter o Fader em **0 dB**.
- Ajustar o volume utilizando o fader.
- Se houver tendência à microfonia, reduzir primeiro a **🟣 Banda 3 (2,8 kHz)** em pequenos passos (1 a 2 dB) antes de diminuir o volume geral.
- Orientar o usuário a manter o microfone atrás da linha das caixas de PA e evitar apontá-lo diretamente para os alto-falantes.

---

# Observações

Este preset foi desenvolvido especificamente para a:

**Igreja Presbiteriana de Piracicaba**

Considerando:

- Soundcraft Ui24R;
- PA Dommer;
- 2 Subwoofers LL Audio;
- 2 Monitores de palco;
- Microfones sem espuma (windscreen);
- Uso por homens e mulheres;
- Utilização em qualquer posição do templo.

Foi otimizado para priorizar a estabilidade contra microfonia sem comprometer a clareza da voz.