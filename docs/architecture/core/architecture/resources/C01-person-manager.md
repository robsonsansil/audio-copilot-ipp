# Sprint C01 - Cadastro de Pessoas

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo cadastro de todas as pessoas que poderão participar dos eventos do Audio Copilot, permitindo sua identificação, organização e associação aos diversos recursos do sistema, como vocais, instrumentos, microfones, canais, programações e histórico de participação.

O cadastro de pessoas será a entidade base para os demais cadastros relacionados aos membros da equipe, evitando duplicidade de informações e permitindo que uma mesma pessoa desempenhe diferentes funções em eventos distintos.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de pessoas.
- Edição de cadastro.
- Exclusão de cadastro.
- Ativação e desativação de pessoas.
- Pesquisa por nome.
- Pesquisa por apelido.
- Ordenação por nome.
- Visualização em lista.
- Visualização detalhada.
- Associação com foto.
- Associação com múltiplas funções.
- Histórico de participação em eventos.
- Controle de observações.

---

# Informações cadastradas

Cada pessoa poderá possuir as seguintes informações:

## Identificação

- Nome completo
- Nome de exibição
- Apelido (opcional)
- Foto
- Sexo
- Data de nascimento (opcional)

---

## Contato

- Telefone (opcional)
- E-mail (opcional)

---

## Informações Gerais

- Situação (Ativo / Inativo)
- Observações

---

# Relacionamentos

Uma pessoa poderá estar associada a:

- Vocalista
- Instrumentista
- Pregador
- Dirigente
- Operador de Som
- Operador de Mídia
- Técnico
- Convidado
- Outros papéis futuros

Uma mesma pessoa poderá exercer múltiplas funções simultaneamente.

Exemplo:

Robson

✓ Operador de Som

✓ Vocal

✓ Violão

✓ Técnico

---

# Regras de Negócio

## Pessoa única

Não poderá existir duas pessoas com o mesmo cadastro.

---

## Cadastro permanente

O cadastro será permanente.

As pessoas não serão cadastradas novamente para cada evento.

---

## Participação em eventos

Os eventos apenas selecionarão pessoas já cadastradas.

---

## Exclusão

Caso uma pessoa possua histórico de participação em eventos, ela não deverá ser excluída fisicamente.

O sistema deverá apenas marcá-la como Inativa.

---

## Histórico

Toda alteração relevante poderá ser registrada no histórico do sistema.

---

# Interface

A tela deverá possuir:

- Lista de pessoas
- Campo de pesquisa
- Botão Novo
- Botão Editar
- Botão Excluir
- Botão Ativar/Inativar
- Visualização da foto
- Informações resumidas

---

# Integração com outros módulos

Este módulo será utilizado por:

- Cadastro de Vocais
- Cadastro de Instrumentistas
- Configuração do Evento
- Programação Técnica
- Motor do Audio Copilot
- Biblioteca Geral
- Relatórios
- IA Operacional

---

# Estrutura sugerida

```text
Pessoa
│
├── id
├── nome
├── nome_exibicao
├── apelido
├── foto
├── sexo
├── nascimento
├── telefone
├── email
├── ativo
├── observacoes
├── criado_em
└── atualizado_em
```

---

# Classes previstas

Pessoa

PessoaRepository

PessoaService

PessoaValidator

PessoaController

PessoaViewModel

---

# Benefícios

Este módulo centraliza todas as informações das pessoas participantes da operação, evitando duplicidade de cadastros, facilitando a configuração dos eventos e permitindo que o Audio Copilot reconheça cada participante ao longo do tempo, preservando seu histórico e possibilitando futuras análises e recomendações da Inteligência Artificial.