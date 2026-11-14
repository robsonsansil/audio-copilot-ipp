# Biblioteca de Presets

## Objetivo

Esta pasta contém todos os presets oficiais do Audio Copilot.

Um preset representa um conjunto de parâmetros previamente ajustados para um equipamento, instrumento ou microfone específico, permitindo padronizar a operação da mesa de som e reduzir o tempo de configuração antes dos eventos.

Os presets foram desenvolvidos com base em testes práticos realizados na Soundcraft Ui24R da Igreja Presbiteriana de Piracicaba.

---

# Objetivos da Biblioteca

A biblioteca de presets possui os seguintes objetivos:

- padronizar as configurações da mesa;
- reduzir erros operacionais;
- acelerar a preparação dos eventos;
- documentar todo o conhecimento adquirido pela equipe;
- facilitar futuras manutenções;
- servir como base para aplicação automática pelo Audio Copilot.

---

# Organização

Os presets estão organizados por categoria.

```
presets/

├── README.md
├── PRESETS-OFICIAIS.md
│
├── voz/
│   ├── pulpito.md
│   ├── microfone-sem-fio.md
│   ├── vocal-masculino.md
│   └── vocal-feminino.md
│
├── instrumentos/
│   ├── violao-martin.md
│   ├── baixo.md
│   ├── cajon.md
│   └── piano.md
│
├── fx/
│   ├── reverb-vocal.md
│   └── delay-pregacao.md
│
└── cenas/
    ├── culto-domingo.md
    ├── oracao.md
    └── estudo-biblico.md
```

---

# Estrutura de um Preset

Todo preset deverá possuir a mesma estrutura.

- Objetivo
- Equipamento
- Configuração de Gain
- HPF
- Equalização
- LPF
- Compressor
- Gate
- De-Esser (quando aplicável)
- FX (quando aplicável)
- Fader
- Resultado esperado
- Observações

Essa padronização facilita tanto a leitura humana quanto a futura interpretação automática pelo Audio Copilot.

---

# Convenção de Nomes

Os arquivos devem possuir nomes curtos, descritivos e em letras minúsculas.

Exemplos:

## Voz

```
pulpito.md
microfone-sem-fio.md
vocal-masculino.md
vocal-feminino.md
```

## Instrumentos

```
violao-martin.md
baixo.md
cajon.md
piano.md
```

## FX

```
reverb-vocal.md
delay-pregacao.md
```

## Cenas

```
culto-domingo.md
oracao.md
estudo-biblico.md
```

---

# Filosofia dos Presets

Os presets não substituem a regulagem realizada durante o evento.

Cada preset representa um ponto de partida validado em testes práticos.

O operador continua responsável por realizar pequenos ajustes conforme:

- acústica do ambiente;
- quantidade de pessoas;
- posicionamento das caixas;
- posicionamento dos microfones;
- características dos músicos;
- dinâmica do evento.

---

# Versionamento

Sempre que um preset sofrer alterações significativas, uma nova versão deverá ser registrada no histórico do documento.

O nome do arquivo permanece o mesmo.

Exemplo:

```
violao-martin.md
```

No próprio arquivo:

```
Versão 1.0
Versão 1.1
Versão 2.0
```

---

# Integração com o Audio Copilot

No futuro, cada preset possuirá duas representações.

## Documentação

Arquivo destinado à leitura humana.

Exemplo:

```
violao-martin.md
```

## Configuração

Arquivo estruturado para leitura pelo sistema.

Exemplo:

```
violao-martin.json
```

O arquivo Markdown documentará toda a filosofia e justificativa técnica do preset.

O arquivo JSON armazenará apenas os parâmetros necessários para que o Audio Copilot possa aplicar automaticamente a configuração na mesa de som.

---

# Evolução

Esta biblioteca deverá crescer continuamente conforme novos equipamentos, instrumentos, microfones e cenários forem sendo testados.

Toda configuração validada pela equipe poderá ser incorporada como um novo preset oficial do projeto.

---

# Objetivo Final

Construir uma biblioteca padronizada de presets, tecnicamente documentada, reutilizável e preparada para integração automática com o Audio Copilot, permitindo rapidez na configuração da mesa, redução de erros operacionais e preservação do conhecimento adquirido pela equipe de sonorização.