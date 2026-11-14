# Sprint C08 - Gerenciador de Canais

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo gerenciamento de todos os canais de entrada e saída utilizados pelo Audio Copilot, permitindo cadastrar, organizar e controlar a ocupação dos canais da mesa de som, associando-os a pessoas, instrumentos, microfones, equipamentos, presets e cenas.

Este módulo será o ponto central da organização lógica da mesa de som, permitindo que o sistema saiba, a qualquer momento, qual recurso está utilizando cada canal e quais configurações devem ser aplicadas automaticamente.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de canais.
- Edição de cadastro.
- Ativação e desativação.
- Organização por banco de canais.
- Associação com entradas físicas.
- Associação com saídas físicas.
- Associação com pessoas.
- Associação com fontes vocais.
- Associação com instrumentos.
- Associação com microfones.
- Associação com equipamentos.
- Associação com presets.
- Associação com cenas.
- Associação com eventos.
- Pesquisa por canal.
- Pesquisa por tipo.
- Registro de observações técnicas.

---

# Tipos de Canal

O sistema deverá permitir cadastrar diferentes tipos de canais.

## Entradas

- Entrada Analógica
- Entrada Digital
- USB
- Player
- Retorno de FX
- Outro

---

## Saídas

- Main L/R
- Matrix
- Auxiliar (AUX)
- Subgrupo
- Monitor
- Fone
- Streaming
- Gravação
- Outro

---

# Informações cadastradas

## Identificação

- Número do canal
- Nome do canal
- Tipo do canal

---

## Associação

O canal poderá estar associado a:

- Pessoa
- Fonte Vocal
- Instrumentista
- Instrumento
- Microfone
- Equipamento

---

## Configuração Preferencial

- Preset padrão
- Cena padrão
- Grupo
- Cor de identificação

---

## Configuração Técnica

- Ganho inicial
- Phantom Power
- Polaridade
- Delay
- HPF padrão
- Gate padrão
- Compressor padrão
- Equalização padrão

---

## Operação

- Canal fixo
- Canal variável
- Canal reserva

---

## Estado

- Livre
- Reservado
- Em uso
- Bloqueado
- Inativo

---

## Observações

Exemplos:

- Utilizado exclusivamente pelo pastor.
- Reservado para convidados.
- Sempre utilizado pelo teclado.
- Canal destinado ao playback.
- Utilizado apenas em eventos especiais.

---

# Relacionamentos

Cada canal poderá estar associado a:

- Pessoas
- Fontes Vocais
- Instrumentistas
- Instrumentos
- Microfones
- Equipamentos
- Presets
- Cenas
- Eventos
- Programações
- Biblioteca Geral

---

# Regras de Negócio

## Canal único

Cada canal físico deverá possuir apenas um cadastro.

---

## Canal preferencial

Um recurso poderá possuir um canal preferencial.

Durante a configuração do evento, o sistema utilizará essa informação como sugestão.

---

## Canal reservado

Canais marcados como reserva não deverão ser utilizados automaticamente.

---

## Canal bloqueado

Canais bloqueados não poderão ser atribuídos durante a configuração do evento.

---

## Histórico

O sistema deverá registrar todas as utilizações de cada canal ao longo dos eventos.

---

## Flexibilidade

Embora existam canais preferenciais, o operador poderá alterar livremente qualquer associação durante a preparação do evento.

---

# Interface

A tela deverá apresentar:

- Lista de canais
- Número
- Nome
- Tipo
- Recurso associado
- Estado
- Situação

Filtros:

- Tipo
- Estado
- Evento
- Nome
- Número

---

# Integração com outros módulos

Este módulo será utilizado por:

- Cadastro de Pessoas
- Gerenciador de Fontes Vocais
- Gerenciador de Instrumentistas
- Gerenciador de Instrumentos
- Gerenciador de Microfones
- Gerenciador de Equipamentos
- Configuração do Evento
- Programação Técnica
- Gerenciador de Cenas
- Motor do Audio Copilot
- Operação ao Vivo
- Engenharia Reversa da Ui24R
- IA Operacional
- Biblioteca Geral
- Relatórios

---

# Estrutura sugerida

```text
Canal
│
├── id
├── numero
├── nome
├── tipo
├── recurso_associado
├── preset_padrao
├── cena_padrao
├── grupo
├── cor
├── ganho_inicial
├── phantom_power
├── polaridade
├── delay
├── hpf
├── gate
├── compressor
├── equalizador
├── modo_operacao
├── estado
├── observacoes
├── ativo
├── criado_em
└── atualizado_em
```

---

# Classes previstas

- Channel
- ChannelRepository
- ChannelService
- ChannelValidator
- ChannelController
- ChannelViewModel

---

# Benefícios

Este módulo centraliza toda a organização lógica dos canais da mesa de som, permitindo ao Audio Copilot conhecer a ocupação de cada entrada e saída, aplicar automaticamente presets e cenas, validar conflitos de configuração e acelerar significativamente a preparação dos eventos. Além disso, fornece uma base sólida para o gerenciamento inteligente da operação e para futuras recomendações da Inteligência Artificial.