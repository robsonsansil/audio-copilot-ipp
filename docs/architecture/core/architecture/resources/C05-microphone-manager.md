# Sprint C05 - Gerenciador de Microfones

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo gerenciamento dos microfones utilizados pelo Audio Copilot, permitindo cadastrar cada equipamento individualmente, armazenando suas características técnicas, configurações preferenciais, estado de conservação e relacionamento com pessoas, canais, presets, eventos e demais recursos do sistema.

Este módulo permitirá que o Audio Copilot reconheça cada microfone como um equipamento físico independente, possibilitando a padronização das configurações da mesa de som e fornecendo suporte à Inteligência Artificial para recomendações automáticas.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de microfones.
- Edição de cadastro.
- Exclusão lógica.
- Ativação e desativação.
- Pesquisa por fabricante.
- Pesquisa por modelo.
- Pesquisa por tipo.
- Associação com pessoas.
- Associação com canais.
- Associação com presets.
- Associação com equipamentos.
- Registro de observações técnicas.
- Controle de manutenção.

---

# Informações cadastradas

## Identificação

- Nome de identificação
- Fabricante
- Modelo
- Número de patrimônio (opcional)
- Número de série (opcional)

---

## Tipo de Microfone

Exemplos:

- Dinâmico
- Condensador
- Headset
- Lapela
- Gooseneck
- Boundary
- Shotgun
- USB
- Outro

---

## Características Técnicas

- Padrão polar
  - Cardioide
  - Supercardioide
  - Hipercardioide
  - Omnidirecional
  - Bidirecional

- Resposta de frequência (opcional)
- Sensibilidade (opcional)
- Impedância (opcional)
- Phantom Power necessário
- Chave Liga/Desliga
- Filtro HPF integrado
- Pad integrado

---

## Configuração Preferencial

- Canal preferencial
- Preset preferencial
- Cena preferencial
- Grupo de canais

---

## Utilização

- Uso principal
  - Vocal
  - Pregação
  - Coral
  - Instrumento
  - Bateria
  - Percussão
  - Ambiente
  - Streaming
  - Outro

---

## Estado do Equipamento

- Ativo
- Em manutenção
- Reserva
- Inativo

---

## Observações Técnicas

Exemplos:

- Necessita phantom power.
- Excelente rejeição à microfonia.
- Ganho elevado.
- Sensível às plosivas.
- Necessita espuma antivento.
- Utilizado exclusivamente pelo pastor.
- Cabo fixo.
- Necessita pedestal longo.

---

# Relacionamentos

Cada microfone poderá estar associado a:

- Pessoas
- Fontes Vocais
- Instrumentistas
- Instrumentos
- Equipamentos
- Canais
- Presets
- Cenas
- Eventos
- Programações Técnicas
- Biblioteca Geral

---

# Regras de Negócio

## Cadastro individual

Cada microfone físico deverá possuir apenas um cadastro.

---

## Configuração própria

Cada microfone poderá possuir:

- Preset preferencial
- Canal preferencial
- Configuração específica

Independentemente da pessoa que irá utilizá-lo.

---

## Histórico

O sistema deverá registrar em quais eventos cada microfone foi utilizado.

---

## Manutenção

O sistema deverá permitir registrar quando o equipamento estiver em manutenção ou indisponível.

Microfones indisponíveis não deverão ser sugeridos durante a configuração dos eventos.

---

## Exclusão

Caso exista histórico de utilização, o cadastro não deverá ser removido fisicamente.

O sistema deverá apenas marcar o equipamento como Inativo.

---

# Interface

A tela deverá apresentar:

- Lista de microfones
- Fabricante
- Modelo
- Tipo
- Canal preferencial
- Estado
- Situação

Filtros:

- Fabricante
- Modelo
- Tipo
- Estado
- Situação

---

# Integração com outros módulos

Este módulo será utilizado por:

- Cadastro de Pessoas
- Gerenciador de Fontes Vocais
- Gerenciador de Instrumentistas
- Gerenciador de Instrumentos
- Cadastro de Equipamentos
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
Microfone
│
├── id
├── nome
├── fabricante
├── modelo
├── patrimonio
├── numero_serie
├── tipo
├── padrao_polar
├── resposta_frequencia
├── sensibilidade
├── impedancia
├── phantom_power
├── chave_liga_desliga
├── filtro_hpf
├── pad
├── canal_preferencial
├── preset_preferencial
├── cena_preferencial
├── grupo_canais
├── uso_principal
├── estado
├── observacoes
├── ativo
├── criado_em
└── atualizado_em
```

---

# Classes previstas

- Microphone
- MicrophoneRepository
- MicrophoneService
- MicrophoneValidator
- MicrophoneController
- MicrophoneViewModel

---

# Benefícios

Este módulo permite que o Audio Copilot conheça individualmente cada microfone disponível, armazenando suas características técnicas, configurações preferenciais e histórico de utilização. Com essas informações, o sistema poderá sugerir automaticamente o equipamento mais adequado para cada participante, aplicar presets específicos, reduzir o tempo de preparação dos eventos e auxiliar a Inteligência Artificial na tomada de decisões durante a operação da mesa de som.