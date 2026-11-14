# Sprint C04 - Gerenciador de Instrumentos

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo gerenciamento dos instrumentos utilizados nos eventos do Audio Copilot, permitindo o cadastro detalhado de cada instrumento físico, suas características técnicas, configurações preferenciais e relacionamento com instrumentistas, canais, equipamentos e presets.

Este módulo permitirá que o sistema conheça individualmente cada instrumento da igreja ou de músicos convidados, facilitando a preparação dos eventos, a aplicação automática de configurações e o aprendizado da Inteligência Artificial.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de instrumentos.
- Edição de instrumentos.
- Exclusão lógica.
- Ativação e desativação.
- Pesquisa por nome.
- Pesquisa por categoria.
- Associação com instrumentistas.
- Associação com canais.
- Associação com presets.
- Associação com equipamentos.
- Registro de observações técnicas.

---

# Informações cadastradas

## Identificação

- Nome do instrumento
- Categoria
- Fabricante
- Modelo
- Número de patrimônio (opcional)
- Número de série (opcional)

---

## Categorias

Exemplos:

- Violão
- Guitarra
- Baixo
- Piano
- Teclado
- Bateria
- Cajón
- Percussão
- Violino
- Viola
- Violoncelo
- Contrabaixo Acústico
- Flauta
- Saxofone
- Trompete
- Trombone
- Clarinete
- Ukulele
- Bandolim
- Outro

---

## Configuração Técnica

- Tipo de conexão
  - XLR
  - P10 Mono
  - P10 Estéreo
  - USB
  - MIDI
  - Outro

- Tipo de captação
  - Microfonado
  - Captador Passivo
  - Captador Ativo
  - DI Box
  - Interface USB

- Necessita Phantom Power
- Necessita Direct Box
- Necessita alimentação elétrica

---

## Configuração Preferencial

- Canal preferencial
- Preset preferencial
- Cena preferencial
- Grupo de canais

---

## Equipamentos Associados

- Direct Box
- Pedaleira
- Amplificador
- Pedal
- Interface
- Mesa Digital
- Outro

---

## Observações Técnicas

Exemplos:

- Utiliza saída estéreo.
- Necessita dois canais.
- Possui captador ativo.
- Afinado meio tom abaixo.
- Utiliza pedaleira.
- Utiliza DI estéreo.
- Instrumento muito sensível ao ganho.
- Requer HPF em 80 Hz.

---

# Relacionamentos

Cada instrumento poderá estar associado a:

- Instrumentistas
- Microfones
- Equipamentos
- Canais
- Presets
- Cenas
- Eventos
- Programações Técnicas
- Biblioteca Geral

---

# Regras de Negócio

## Cadastro permanente

Cada instrumento será cadastrado apenas uma vez.

---

## Compartilhamento

Um mesmo instrumento poderá ser utilizado por diferentes pessoas em eventos distintos.

---

## Configurações independentes

Cada instrumento poderá possuir suas próprias configurações técnicas, independentemente do instrumentista.

Exemplo:

Violão Martin

- Canal 05
- Preset Violão Martin
- HPF 80 Hz
- Compressor Leve

---

## Histórico

O sistema deverá registrar em quais eventos o instrumento foi utilizado.

---

## Exclusão

Caso exista histórico de utilização, o instrumento não deverá ser removido fisicamente.

O sistema deverá apenas marcá-lo como Inativo.

---

# Interface

A tela deverá apresentar:

- Lista de instrumentos
- Categoria
- Fabricante
- Modelo
- Canal preferencial
- Preset preferencial
- Situação (Ativo/Inativo)

Filtros:

- Categoria
- Fabricante
- Nome
- Situação

---

# Integração com outros módulos

Este módulo será utilizado por:

- Cadastro de Instrumentistas
- Cadastro de Equipamentos
- Cadastro de Microfones
- Cadastro de Canais
- Configuração do Evento
- Programação Técnica
- Preparação do Evento
- Motor do Audio Copilot
- Operação ao Vivo
- IA Operacional
- Biblioteca Geral
- Relatórios

---

# Estrutura sugerida

```text
Instrumento
│
├── id
├── nome
├── categoria
├── fabricante
├── modelo
├── patrimonio
├── numero_serie
├── tipo_conexao
├── tipo_captacao
├── phantom_power
├── necessita_direct_box
├── alimentacao_eletrica
├── canal_preferencial
├── preset_preferencial
├── cena_preferencial
├── grupo_canais
├── observacoes
├── ativo
├── criado_em
└── atualizado_em
```

---

# Classes previstas

- Instrument
- InstrumentRepository
- InstrumentService
- InstrumentValidator
- InstrumentController
- InstrumentViewModel

---

# Benefícios

Este módulo permite que o Audio Copilot conheça individualmente cada instrumento utilizado na igreja, armazenando suas características técnicas e configurações preferenciais. Com isso, o sistema poderá sugerir automaticamente canais, presets, cenas e equipamentos adequados para cada instrumento, reduzindo o tempo de preparação, aumentando a padronização da operação e fornecendo uma base consistente para o aprendizado da Inteligência Artificial.