# Perfil de Canal — Microfone do Púlpito

> **Canal:** CH 7 (Púlpito)
>
> **Mesa:** Soundcraft Ui24R
>
> **Aplicação:** Pregação, leitura bíblica, avisos e estudos
>
> **Microfone:** Gooseneck (pescoço de ganso) condensador ligado diretamente à mesa
>
> **Sistema:** PA estéreo + Subwoofer + 2 monitores
>
> **Uso predominante:** Voz masculina
>
> **Uso feminino:** Eventual
>
> **Versão:** 2.1
>
> **Status:** ✅ Validado em campo

---

# Objetivo

Produzir uma voz:

- Muito natural
- Extremamente inteligível
- Confortável para ouvir por longos períodos
- Sem graves excessivos
- Com plosivas ("P" e "B") controladas
- Sem sibilância
- Com baixo risco de microfonia

Como normalmente apenas o pregador está falando, o objetivo não é fazer a voz "cortar" a banda, mas soar clara, equilibrada e agradável durante toda a mensagem.

---

# MIX

## Gain

Ajustar individualmente.

Objetivo:

**Picos entre -12 dBFS e -6 dBFS.**

Nunca compensar volume pelo ganho.

---

## Fader

Ponto inicial:

**0 dB (Unity)**

O volume da pregação deve ser ajustado apenas pelo fader.

---

# Equalizador

## 🔵 HPF

**130 Hz**

Slope:

**12 dB/Oct**

Remove vibrações do púlpito, ruídos de piso e graves desnecessários, preservando a naturalidade da voz masculina.

---

## 🟢 Banda 1

**140 Hz**

**-1,5 dB**

Q ≈ 1,2

Controla o excesso de graves da voz, preservando sua naturalidade e reduzindo a energia das plosivas.

---

## 🔴 Banda 2

**140 Hz**

**-3 dB**

Q ≈ 3,5

Atenua a região mais crítica das plosivas ("P" e "B"), reduzindo seu impacto sem comprometer a naturalidade da voz.

---

## 🟣 Banda 3

**1,8 kHz**

**+1 dB**

Q ≈ 1,0

Melhora a articulação das palavras e aumenta a inteligibilidade da fala.

---

## 🟡 Banda 4

**3,5 kHz**

**+2 dB**

Q ≈ 1,0

Acrescenta definição e clareza sem deixar a voz agressiva.

---

## 🟠 LPF

**18 kHz**

Slope:

**12 dB/Oct**

Remove ruídos muito altos sem alterar o timbre da voz.

---

# De-Esser

**Frequência:**

6,5 kHz

**Threshold:**

Ajustar conforme necessidade.

Objetivo:

Controlar:

- S
- CH
- X

Sem retirar a naturalidade da fala.

---

# Gate

**Threshold:**

**-50 dB**

**Attack:**

5 ms

**Hold:**

80 ms

**Release:**

220 ms

**Depth:**

18 dB

### Objetivo

Fechar o canal quando o púlpito estiver sem uso, reduzindo o ruído ambiente, mas sem cortar o início das palavras.

---

# Compressor

**Threshold:**

**-20 dB**

**Ratio:**

**3:1**

**Attack:**

25 ms

**Release:**

150 ms

**Make-up Gain:**

0 dB

**Soft Knee:**

Ligado

### Objetivo

Nivelar as diferenças entre fala baixa e alta, mantendo a voz natural, confortável e consistente.

O ataque de **25 ms** preserva a articulação natural da fala e ajuda a suavizar as plosivas sem produzir uma sensação de voz excessivamente comprimida.

---

# Auxiliares (Monitores)

Normalmente:

**Não enviar retorno ao púlpito.**

Caso seja necessário para um pregador específico:

Enviar apenas uma pequena quantidade da própria voz.

Evitar níveis elevados de retorno para reduzir o risco de microfonia.

---

# FX

**Reverb:**

**Desligado**

**Delay:**

**Desligado**

A Palavra deve permanecer totalmente inteligível.

---

# Característica Sonora Esperada

✔ Voz natural

✔ Clara

✔ Confortável

✔ Excelente inteligibilidade

✔ Pouca fadiga auditiva

✔ Graves controlados

✔ Plosivas reduzidas

✔ Sem excesso de brilho

✔ Baixíssimo risco de microfonia

✔ Boa compreensão mesmo no fundo do templo

---

# Observações Operacionais

- Este canal normalmente é utilizado sozinho, sem a banda tocando.
- Foi otimizado para voz masculina, que representa a maior parte do uso do púlpito.
- Para vozes femininas, normalmente não é necessário alterar a equalização; apenas ajustar o ganho, se necessário.
- Se houver plosivas ("P" e "B"), antes de alterar o EQ, verifique o posicionamento do microfone. O ideal é que ele fique cerca de **8 a 12 cm abaixo da boca**, apontado levemente para o queixo, evitando que o fluxo de ar atinja diretamente a cápsula.
- Caso persistam plosivas ("P" e "B"), priorizar o reposicionamento do microfone antes de realizar novos cortes no equalizador. Pequenos ajustes de altura, distância e inclinação costumam produzir resultados superiores a equalizações mais agressivas.
- Em caso de início de microfonia, reduzir primeiro o envio aos monitores e somente depois realizar pequenos ajustes no equalizador.

---

# Filosofia deste Perfil

Este perfil foi desenvolvido e refinado em testes práticos durante cultos na Igreja Presbiteriana de Piracicaba.

A filosofia deste preset é priorizar uma **fala natural, confortável e altamente inteligível**, evitando equalizações e compressões exageradas.

O objetivo é que o pregador soe como sua própria voz, apenas mais clara, estável e agradável para toda a congregação, preservando a naturalidade e reduzindo a fadiga auditiva.

---

# Histórico de Revisões

## Versão 2.1

- HPF ajustado para **130 Hz**.
- Equalização refinada para redução das plosivas ("P" e "B").
- Compressor ajustado para **Ratio 3:1**, **Attack 25 ms** e **Release 150 ms**.
- Preset validado em testes práticos durante cultos.

## Versão 2.0

- Revisão completa do preset para voz de púlpito.
- Otimização para voz masculina em microfone gooseneck.
- Foco em inteligibilidade, conforto auditivo e baixo risco de microfonia.