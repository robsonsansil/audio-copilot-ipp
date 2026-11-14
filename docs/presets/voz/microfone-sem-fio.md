# Preset - Microfone sem Fio

> Igreja Presbiteriana de Piracicaba

---

# Equipamento

- **Tipo:** Microfone sem fio
- **Uso:** Avisos, testemunhos, leitura bíblica, perguntas, apresentações e apoio durante os cultos.
- **Usuários:** Homens e mulheres

---

# Recomendações de Uso

- Manter o microfone entre **5 e 10 cm** da boca.
- Falar sempre direcionado para a cápsula.
- Evitar apontar o microfone para as caixas do PA.
- Sempre que possível, permanecer atrás da linha das caixas acústicas.

---

# Ui24R

## 🟢 Gain

Regular para que os picos fiquem entre:

- **-18 dB**
- **-12 dB**

Nunca permitir clipagem.

---

## 🔵 HPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **120 Hz** |
| Inclinação | **12 dB/oitava** |

Ajuda a reduzir ruídos de manuseio e vibrações.

---

# 🟡 Equalizador

### 🟡 Banda 1 — Graves

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **180 Hz** |
| Ganho | **-2 dB** |
| Q | **0,8** |

Reduz o excesso de graves quando o microfone é segurado muito próximo da boca.

---

### 🟠 Banda 2 — Médios Graves

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **300 Hz** |
| Ganho | **-3 dB** |
| Q | **1,2** |

Remove o efeito de voz "abafada" e ajuda a diminuir a tendência à microfonia.

---

### 🟢 Banda 3 — Clareza

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **2,5 kHz** |
| Ganho | **+1,5 dB** |
| Q | **1,0** |

Melhora a inteligibilidade da fala.

---

### 🔴 Banda 4 — Presença

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **4 kHz** |
| Ganho | **+1 dB** |
| Q | **1,0** |

Acrescenta definição sem aumentar excessivamente o risco de realimentação.

---

## 🟣 LPF

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **16 kHz** |

---

# 🟠 Compressor

| Parâmetro | Valor |
|-----------|------:|
| Threshold | **-20 dB** |
| Ratio | **2:1** |
| Attack | **20 ms** |
| Release | **120 ms** |
| Makeup Gain | **0 dB** |

Mantém o volume uniforme sem comprometer a naturalidade da voz.

---

# 🔷 De-Esser

| Parâmetro | Valor |
|-----------|------:|
| Frequência | **6,5 kHz** |
| Threshold | **-30 dB** |
| Ratio | **2:1** |

Controla sibilâncias ("S", "CH" e "X").

---

# 🟤 Gate

| Parâmetro | Valor |
|-----------|------:|
| Threshold | **-48 dB** |
| Attack | **5 ms** |
| Hold | **100 ms** |
| Release | **180 ms** |

Fecha o microfone quando ninguém está falando, reduzindo vazamentos e ajudando a prevenir microfonia.

---

# 🎚️ Fader

Iniciar em:

**-5 dB**

Ajustar conforme a necessidade da mixagem.

---

# Observações

- Preset desenvolvido para uso geral com vozes masculinas e femininas.
- Prioriza estabilidade e inteligibilidade em ambientes com risco de microfonia.
- O HPF em **120 Hz** reduz ruídos de manuseio e vibrações.
- O corte em **300 Hz** ajuda a controlar o efeito "abafado" e melhora a clareza da fala.
- Sempre ajustar o ganho antes do uso, pois cada pessoa possui intensidade vocal diferente.
- Se houver início de microfonia, reduzir primeiro o fader e reposicionar o usuário em relação às caixas do PA antes de alterar a equalização.