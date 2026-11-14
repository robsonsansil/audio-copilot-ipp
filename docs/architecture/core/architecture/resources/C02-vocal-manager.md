# Sprint C02 - Gerenciador de Fontes Vocais

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo gerenciamento de todas as fontes vocais utilizadas durante os eventos do Audio Copilot, permitindo associar pessoas aos diferentes papéis desempenhados com uso de microfone, armazenando configurações técnicas, preferências operacionais e informações necessárias para preparação do evento, operação da mesa de som, aplicação de presets, geração de cenas e apoio da Inteligência Artificial.

Este módulo complementa o Cadastro de Pessoas, adicionando informações específicas relacionadas à utilização da voz durante os eventos.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de fontes vocais.
- Associação com uma pessoa cadastrada.
- Definição do papel desempenhado.
- Edição das configurações.
- Ativação e desativação.
- Pesquisa por nome.
- Pesquisa por categoria.
- Associação com microfone preferencial.
- Associação com canal preferencial.
- Associação com preset.
- Registro de observações técnicas.

---

# Categorias

Cada fonte vocal poderá pertencer a uma ou mais categorias.

Exemplos:

- Vocal Principal
- Backing Vocal
- Coral
- Solo
- Pregador
- Dirigente
- Leitor Bíblico
- Apresentador
- Palestrante
- Convidado
- Participação Especial
- Outro

Uma mesma pessoa poderá possuir múltiplas categorias.

Exemplo:

Robson

✓ Pregador

✓ Vocal Principal

✓ Dirigente

---

# Informações cadastradas

## Pessoa

- Pessoa vinculada (Cadastro de Pessoas)

---

## Características Vocais

- Tipo vocal (opcional)
  - Soprano
  - Mezzo-soprano
  - Contralto
  - Tenor
  - Barítono
  - Baixo

- Alcance vocal (opcional)

- Intensidade vocal
  - Baixa
  - Média
  - Alta

---

## Configuração Técnica

- Microfone preferencial
- Canal preferencial
- Preset preferencial
- Grupo de canais (opcional)

---

## Configurações Operacionais

- Necessita retorno dedicado
- Necessita phantom power
- Necessita compressor específico
- Necessita de-esser específico
- Necessita configuração personalizada

---

## Observações Técnicas

Exemplos:

- Voz muito dinâmica.
- Voz muito grave.
- Voz muito aguda.
- Grande variação de volume.
- Fala distante do microfone.
- Possui plosivas frequentes.
- Necessita HPF elevado.
- Necessita ganho reduzido.
- Utiliza headset.

---

# Relacionamentos

Cada fonte vocal poderá estar associada a:

- Pessoa
- Microfone
- Canal
- Preset
- Cena
- Evento
- Programação Técnica
- Biblioteca Geral
- Histórico de Operações

---

# Regras de Negócio

## Pessoa obrigatória

Toda fonte vocal deverá estar vinculada a uma pessoa previamente cadastrada.

---

## Múltiplos papéis

Uma mesma pessoa poderá exercer diferentes papéis durante eventos distintos.

Exemplo:

- Vocal Principal
- Pregador
- Dirigente

O sistema deverá permitir selecionar automaticamente o perfil correspondente ao papel desempenhado naquele evento.

---

## Presets

Cada categoria poderá possuir um preset preferencial.

Exemplo:

Pastor João

- Perfil Pregador
- Preset Pregador

Maria

- Perfil Backing Vocal
- Preset Backing Feminino

---

## Canal

O canal preferencial servirá como sugestão durante a configuração do evento.

O operador poderá alterá-lo livremente.

---

## Exclusão

Caso exista histórico de utilização, a fonte vocal não deverá ser excluída fisicamente.

O sistema deverá apenas marcá-la como Inativa.

---

# Interface

A tela deverá apresentar:

- Lista de participantes
- Foto
- Nome
- Categoria
- Canal preferencial
- Microfone preferencial
- Preset preferencial
- Situação (Ativo/Inativo)

Filtros:

- Categoria
- Nome
- Situação

---

# Integração com outros módulos

Este módulo será utilizado por:

- Cadastro de Pessoas
- Cadastro de Microfones
- Cadastro de Canais
- Cadastro de Equipamentos
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
FonteVocal
│
├── id
├── pessoa_id
├── categoria
├── tipo_vocal
├── alcance_vocal
├── intensidade
├── microfone_preferencial
├── canal_preferencial
├── preset_preferencial
├── retorno_dedicado
├── phantom_power
├── compressor_personalizado
├── deesser_personalizado
├── configuracao_especial
├── observacoes
├── ativo
├── criado_em
└── atualizado_em
```

---

# Classes previstas

- VocalProfile
- VocalRepository
- VocalService
- VocalValidator
- VocalController
- VocalViewModel

---

# Benefícios

Este módulo centraliza todas as informações relacionadas às pessoas que utilizam a voz durante os eventos, independentemente de serem vocalistas, pregadores, dirigentes ou convidados. A padronização dessas informações permitirá ao Audio Copilot configurar automaticamente canais, microfones, presets e cenas, reduzindo o tempo de preparação, aumentando a consistência operacional e fornecendo dados históricos para futuras recomendações da Inteligência Artificial.