# Sprint C06 - Gerenciador de Equipamentos

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável pelo gerenciamento de todos os equipamentos de áudio utilizados pelo Audio Copilot, permitindo cadastrar, organizar, monitorar e relacionar cada equipamento com os eventos, canais, instrumentos, microfones e demais recursos da operação.

Este módulo permitirá que o sistema possua um inventário completo da infraestrutura de áudio da igreja, facilitando a montagem dos eventos, a manutenção preventiva e a geração de relatórios técnicos.

---

# Funcionalidades

O módulo deverá permitir:

- Cadastro de equipamentos.
- Edição de cadastro.
- Exclusão lógica.
- Ativação e desativação.
- Pesquisa por categoria.
- Pesquisa por fabricante.
- Pesquisa por modelo.
- Associação com canais.
- Associação com instrumentos.
- Associação com microfones.
- Associação com eventos.
- Registro de manutenção.
- Registro de observações técnicas.

---

# Informações cadastradas

## Identificação

- Nome do equipamento
- Categoria
- Fabricante
- Modelo
- Número de patrimônio (opcional)
- Número de série (opcional)

---

## Categorias

Exemplos:

- Direct Box (DI)
- Pedestal
- Pedal
- Pedaleira
- Amplificador
- Caixa Amplificada
- Monitor de Palco
- Fone In-Ear
- Transmissor Wireless
- Receptor Wireless
- Splitter
- Processador de Áudio
- Interface de Áudio
- Notebook
- Tablet
- Fonte de Alimentação
- Extensão Elétrica
- Cabo de Áudio
- Adaptador
- Outro

---

## Características Técnicas

- Tipo de conexão
- Alimentação elétrica
- Alimentação por bateria
- Consumo de energia (opcional)
- Quantidade de canais (quando aplicável)

---

## Configuração Operacional

- Canal preferencial (quando aplicável)
- Equipamento associado
- Local de utilização
- Grupo operacional

---

## Estado do Equipamento

- Disponível
- Em uso
- Reserva
- Em manutenção
- Defeituoso
- Inativo

---

## Localização

- Sala de Som
- Palco
- Depósito
- Estúdio
- Outro

---

## Manutenção

- Data da última manutenção
- Próxima manutenção prevista
- Responsável
- Histórico de manutenções

---

## Observações Técnicas

Exemplos:

- Necessita fonte específica.
- Utilizado apenas no palco.
- Possui cabo fixo.
- Equipamento reserva.
- Necessita calibração periódica.
- Utilizado somente em eventos especiais.

---

# Relacionamentos

Cada equipamento poderá estar associado a:

- Microfones
- Instrumentos
- Instrumentistas
- Fontes Vocais
- Canais
- Cenas
- Presets
- Eventos
- Programações Técnicas
- Biblioteca Geral

---

# Regras de Negócio

## Cadastro individual

Cada equipamento físico deverá possuir apenas um cadastro.

---

## Controle de disponibilidade

Equipamentos indisponíveis não deverão ser sugeridos durante a configuração dos eventos.

---

## Histórico

O sistema deverá registrar em quais eventos o equipamento foi utilizado.

---

## Manutenção

O sistema deverá permitir registrar:

- Manutenções preventivas.
- Manutenções corretivas.
- Equipamentos fora de operação.

---

## Exclusão

Caso exista histórico de utilização, o equipamento não deverá ser removido fisicamente.

O sistema deverá apenas ser marcado como Inativo.

---

# Interface

A tela deverá apresentar:

- Lista de equipamentos
- Categoria
- Fabricante
- Modelo
- Estado
- Localização
- Situação

Filtros:

- Categoria
- Fabricante
- Modelo
- Estado
- Localização
- Situação

---

# Integração com outros módulos

Este módulo será utilizado por:

- Gerenciador de Instrumentos
- Gerenciador de Microfones
- Gerenciador de Canais
- Configuração do Evento
- Programação Técnica
- Preparação do Evento
- Motor do Audio Copilot
- Operação ao Vivo
- Biblioteca Geral
- Relatórios
- IA Operacional

---

# Estrutura sugerida

```text
Equipamento
│
├── id
├── nome
├── categoria
├── fabricante
├── modelo
├── patrimonio
├── numero_serie
├── tipo_conexao
├── alimentacao
├── quantidade_canais
├── canal_preferencial
├── equipamento_associado
├── localizacao
├── estado
├── ultima_manutencao
├── proxima_manutencao
├── responsavel
├── observacoes
├── ativo
├── criado_em
└── atualizado_em
```

---

# Classes previstas

- Equipment
- EquipmentRepository
- EquipmentService
- EquipmentValidator
- EquipmentController
- EquipmentViewModel

---

# Benefícios

Este módulo centraliza o gerenciamento de todos os equipamentos de áudio utilizados pela igreja, permitindo ao Audio Copilot conhecer toda a infraestrutura disponível para cada evento. Com essas informações, o sistema poderá sugerir automaticamente os equipamentos mais adequados, controlar disponibilidade, registrar histórico de utilização, acompanhar manutenções e fornecer uma base sólida para futuras recomendações da Inteligência Artificial.