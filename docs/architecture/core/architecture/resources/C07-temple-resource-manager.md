# Sprint C07 - Gerenciador de Recursos do Templo

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo gerenciamento de todos os recursos físicos existentes no templo que possam ser utilizados durante a preparação e operação dos eventos, permitindo ao Audio Copilot conhecer completamente a infraestrutura disponível para montagem, operação técnica e geração automática de recomendações.

Este módulo complementa os cadastros de pessoas, instrumentos, microfones e equipamentos, registrando os recursos fixos ou móveis da igreja que influenciam diretamente a operação do evento.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de recursos do templo.
- Edição de cadastro.
- Exclusão lógica.
- Ativação e desativação.
- Pesquisa por categoria.
- Pesquisa por localização.
- Associação com eventos.
- Associação com cenas.
- Registro de disponibilidade.
- Registro de observações técnicas.

---

# Recursos cadastrados

O sistema deverá permitir cadastrar qualquer recurso físico disponível no templo.

Exemplos:

## Estrutura

- Palco
- Púlpito
- Mesa
- Cadeiras
- Estantes
- Suportes

---

## Áudio

- PA Principal
- PA Secundário
- Monitores de Palco
- Side Fill
- Subwoofers
- Line Array
- Caixas de Retorno

---

## Vídeo

- Projetores
- Telões
- TVs
- Monitores
- Painéis LED

---

## Iluminação

- Refletores
- Moving Heads
- Canhões
- Luzes de Palco
- Controladoras DMX

---

## Streaming

- Câmeras
- Tripés
- Switchers
- Computadores
- Monitores de Streaming

---

## Infraestrutura

- Pontos de Energia
- Pontos de Rede
- Wi-Fi
- Rack Técnico
- Sala Técnica

---

## Outros

- Ar-condicionado
- Gerador
- Cortinas
- Recursos personalizados

---

# Informações cadastradas

## Identificação

- Nome
- Categoria
- Descrição

---

## Localização

- Palco
- Nave
- Púlpito
- Sala Técnica
- Estúdio
- Área Externa
- Outro

---

## Situação

- Disponível
- Em uso
- Em manutenção
- Indisponível
- Inativo

---

## Características

- Quantidade
- Local fixo ou móvel
- Alimentação elétrica (quando aplicável)
- Observações técnicas

---

# Relacionamentos

Cada recurso poderá estar associado a:

- Eventos
- Programações
- Cenas
- Equipamentos
- Canais
- Biblioteca Geral

---

# Regras de Negócio

## Cadastro permanente

Os recursos deverão permanecer cadastrados para reutilização em todos os eventos.

---

## Disponibilidade

O sistema deverá permitir informar quando determinado recurso estiver indisponível.

Recursos indisponíveis não deverão ser sugeridos durante a preparação do evento.

---

## Histórico

O sistema deverá registrar em quais eventos cada recurso foi utilizado.

---

## Exclusão

Caso exista histórico de utilização, o recurso não deverá ser removido fisicamente.

O sistema deverá apenas ser marcado como Inativo.

---

# Interface

A tela deverá apresentar:

- Lista de recursos
- Categoria
- Localização
- Situação
- Disponibilidade

Filtros:

- Categoria
- Localização
- Situação

---

# Integração com outros módulos

Este módulo será utilizado por:

- Configuração do Evento
- Programação Técnica
- Gerenciador de Cenas
- Motor do Audio Copilot
- Operação ao Vivo
- Biblioteca Geral
- Relatórios
- IA Operacional

---

# Estrutura sugerida

```text
RecursoTemplo
│
├── id
├── nome
├── categoria
├── descricao
├── localizacao
├── quantidade
├── local_fixo
├── alimentacao_eletrica
├── situacao
├── observacoes
├── ativo
├── criado_em
└── atualizado_em
```

---

# Classes previstas

- TempleResource
- TempleResourceRepository
- TempleResourceService
- TempleResourceValidator
- TempleResourceController
- TempleResourceViewModel

---

# Benefícios

Este módulo permite ao Audio Copilot conhecer toda a infraestrutura física disponível no templo, auxiliando na preparação dos eventos, organização dos recursos utilizados, controle de disponibilidade e geração automática de recomendações operacionais. Além disso, fornece uma base consistente para futuras integrações com sistemas de vídeo, iluminação, streaming e automação predial.