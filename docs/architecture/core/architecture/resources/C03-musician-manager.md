# Sprint C03 - Gerenciador de Instrumentistas

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo gerenciamento dos instrumentistas cadastrados no Audio Copilot, permitindo associar pessoas aos instrumentos que executam durante os eventos, armazenando informações técnicas, preferências operacionais e configurações necessárias para preparação do evento, aplicação automática de presets, configuração de canais, geração de cenas e suporte à Inteligência Artificial.

Este módulo complementa o Cadastro de Pessoas, adicionando informações específicas relacionadas à atuação dos músicos durante os eventos.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de instrumentistas.
- Associação com uma pessoa cadastrada.
- Associação com um ou mais instrumentos.
- Definição do instrumento principal.
- Definição de instrumentos secundários.
- Associação com canais preferenciais.
- Associação com presets.
- Associação com cenas.
- Registro de observações técnicas.
- Ativação e desativação.
- Pesquisa por nome.
- Pesquisa por instrumento.

---

# Instrumentos

Um instrumentista poderá tocar um ou mais instrumentos.

Exemplos:

- Violão
- Guitarra
- Baixo
- Violino
- Viola
- Violoncelo
- Contrabaixo Acústico
- Piano
- Teclado
- Cajón
- Bateria
- Percussão
- Flauta
- Saxofone
- Trompete
- Trombone
- Clarinete
- Ukulele
- Bandolim
- Outro

O instrumento principal será utilizado como padrão durante a configuração dos eventos.

---

# Informações cadastradas

## Pessoa

- Pessoa vinculada (Cadastro de Pessoas)

---

## Instrumentos

- Instrumento principal
- Instrumentos secundários

---

## Configuração Técnica

Para cada instrumento poderão ser definidos:

- Canal preferencial
- Preset preferencial
- Microfone preferencial (quando aplicável)
- Direct Box preferencial (quando aplicável)
- Entrada (XLR / P10 / USB / Stereo)
- Grupo de canais

---

## Configurações Operacionais

- Necessita phantom power
- Necessita compressor específico
- Necessita equalização personalizada
- Necessita retorno dedicado
- Necessita pedestal
- Necessita DI Box
- Necessita alimentação elétrica

---

## Observações Técnicas

Exemplos:

- Utiliza violão com captação ativa.
- Utiliza guitarra com pedaleira.
- Necessita DI estéreo.
- Utiliza teclado em estéreo.
- Necessita dois canais.
- Alterna entre violão e guitarra durante o culto.
- Utiliza cajón microfonado.

---

# Relacionamentos

Cada instrumentista poderá estar associado a:

- Pessoa
- Instrumentos
- Microfones
- Equipamentos
- Canais
- Presets
- Cenas
- Evento
- Programação Técnica
- Biblioteca Geral

---

# Regras de Negócio

## Pessoa obrigatória

Todo instrumentista deverá estar vinculado a uma pessoa previamente cadastrada.

---

## Múltiplos instrumentos

Uma mesma pessoa poderá tocar diversos instrumentos.

Exemplo:

Robson

✓ Violão

✓ Guitarra

✓ Baixo

---

## Instrumento principal

Um dos instrumentos deverá ser definido como principal.

Este será utilizado como sugestão durante a configuração do evento.

---

## Configuração individual

Cada instrumento poderá possuir configurações independentes de:

- Canal
- Preset
- Microfone
- Equalização
- Compressor

---

## Exclusão

Caso exista histórico de utilização, o cadastro deverá apenas ser marcado como Inativo.

---

# Interface

A tela deverá apresentar:

- Lista de instrumentistas
- Foto
- Nome
- Instrumento principal
- Instrumentos secundários
- Canal preferencial
- Preset preferencial
- Situação (Ativo/Inativo)

Filtros:

- Nome
- Instrumento
- Situação

---

# Integração com outros módulos

Este módulo será utilizado por:

- Cadastro de Pessoas
- Cadastro de Instrumentos
- Cadastro de Microfones
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
Instrumentista
│
├── id
├── pessoa_id
├── instrumento_principal
├── instrumentos_secundarios
├── canal_preferencial
├── preset_preferencial
├── microfone_preferencial
├── direct_box_preferencial
├── entrada
├── grupo_canais
├── retorno_dedicado
├── phantom_power
├── compressor_personalizado
├── equalizacao_personalizada
├── observacoes
├── ativo
├── criado_em
└── atualizado_em
```

---

# Classes previstas

- MusicianProfile
- MusicianRepository
- MusicianService
- MusicianValidator
- MusicianController
- MusicianViewModel

---

# Benefícios

Este módulo centraliza todas as informações técnicas dos músicos participantes dos eventos, permitindo que o Audio Copilot configure automaticamente canais, microfones, Direct Boxes, presets e cenas para cada instrumentista. A utilização de configurações individuais por instrumento reduz significativamente o tempo de preparação, aumenta a padronização da operação e fornece informações históricas que poderão ser utilizadas pela Inteligência Artificial para otimizar futuras configurações e sugerir melhorias durante os eventos.