# Presets Oficiais

> Igreja Presbiteriana de Piracicaba  
> Projeto Audio Copilot IPP

---

# Objetivo

Este documento define os **presets oficiais** utilizados na mesa Soundcraft Ui24R.

Todos os presets desta biblioteca foram desenvolvidos especificamente para a acústica da igreja, os equipamentos atualmente utilizados e a forma de operação da equipe de áudio.

Esses presets devem servir como **ponto de partida**, podendo receber pequenos ajustes de **Gain** e **Fader** conforme cada culto.

---

# Regras Gerais

## Gain

Sempre ajustar o **Gain** antes do início do culto.

O objetivo é manter os picos aproximadamente entre:

- -18 dB
- -12 dB

Nunca permitir clipagem.

---

## Fader

Após regular o Gain, utilizar apenas o **Fader** para equilibrar a mixagem.

Evitar alterar a equalização durante o culto.

---

## Equalização

Os parâmetros de EQ foram desenvolvidos para os equipamentos da igreja.

Não alterar permanentemente um preset sem que ele seja novamente validado em ensaio.

---

## Compressor

Os valores definidos procuram manter estabilidade sem retirar a dinâmica natural dos instrumentos e vozes.

---

## Gate

Utilizar apenas onde indicado.

Nem todos os canais necessitam Gate.

---

## HPF / LPF

Os filtros HPF e LPF fazem parte do preset.

Evite desativá-los.

---

## Presets

Sempre carregar o preset correspondente ao equipamento.

Não utilizar presets de outros instrumentos.

---

# Biblioteca Oficial

## Voz

| Preset | Utilização |
|---------|------------|
| pulpito-voz-masculina.md | Pregações e leituras masculinas |
| pulpito-voz-feminina.md | Pregações e leituras femininas |
| vocal-masculino.md | Vocal principal e backing masculino |
| vocal-feminino.md | Vocal principal e backing feminino |
| microfone-sem-fio.md | Uso geral (homens e mulheres) |

---

## Instrumentos

| Preset | Utilização |
|---------|------------|
| violao-martin.md | Violão Martin |
| baixo-cl-200-bass.md | Baixo C.L. 200 Bass |
| guitarra.md | Guitarra elétrica |
| teclado-generico.md | Teclado eletrônico |
| cajon.md | Cajón com captação própria |

---

# Ajustes Permitidos Durante o Culto

Durante o culto o operador poderá ajustar apenas:

- Gain
- Fader
- Mute
- Auxiliares (Monitores)
- FX Send (quando necessário)

---

# Ajustes que Devem ser Evitados

Evitar alterar durante o culto:

- Equalizador
- Compressor
- Gate
- HPF
- LPF
- Pan
- Delay
- Configurações internas dos FX

Esses parâmetros fazem parte da padronização oficial da igreja.

---

# Alterações Permanentes

Qualquer alteração permanente em um preset deverá:

1. Ser testada durante um ensaio.
2. Ser aprovada pela equipe responsável pelo áudio.
3. Ser documentada neste repositório.
4. Atualizar o respectivo arquivo `.md`.

---

# Versionamento

Sempre que um preset sofrer alteração, registrar:

- Data
- Motivo da alteração
- Responsável
- Versão

Exemplo:

| Versão | Data | Alteração |
|---------|------|-----------|
| 1.0 | 2026 | Criação do preset |
| 1.1 | 2027 | Ajustes de EQ |
| 1.2 | 2028 | Ajustes de compressor |

---

# Filosofia da Biblioteca

Os presets desta biblioteca possuem quatro objetivos principais:

- Padronizar a operação da Soundcraft Ui24R.
- Reduzir o tempo de montagem e regulagem.
- Facilitar o treinamento de novos operadores.
- Servir como base para o projeto **Audio Copilot IPP**, permitindo que futuras versões do sistema possam carregar, comparar, sugerir melhorias e documentar automaticamente as configurações da mesa.

---

# Estrutura da Biblioteca

```text
presets/

README.md
PRESETS-OFICIAIS.md

voz/
    pulpito-voz-masculina.md
    pulpito-voz-feminina.md
    vocal-masculino.md
    vocal-feminino.md
    microfone-sem-fio.md

instrumentos/
    violao-martin.md
    baixo-cl-200-bass.md
    guitarra.md
    teclado-generico.md
    cajon.md
```

---

# Observação Final

Esta biblioteca representa a configuração oficial da Igreja Presbiteriana de Piracicaba para a Soundcraft Ui24R.

Os presets foram desenvolvidos para oferecer uma sonoridade equilibrada, inteligível e consistente, respeitando as características da acústica da igreja, dos equipamentos utilizados e da equipe de louvor.

Sempre que houver substituição de instrumentos, microfones ou mudanças significativas na acústica do ambiente, recomenda-se revisar os presets correspondentes antes de adotá-los como padrão.