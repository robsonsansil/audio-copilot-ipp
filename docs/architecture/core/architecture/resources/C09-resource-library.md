# Sprint C09 - Biblioteca Geral de Recursos

Status: ⏳ Planejada

## Objetivo

Implementar o módulo responsável por centralizar e organizar todos os recursos cadastrados no Audio Copilot, funcionando como uma biblioteca unificada de consulta, pesquisa, reutilização e relacionamento entre pessoas, equipamentos, instrumentos, microfones, canais, presets, cenas e demais componentes do sistema.

A Biblioteca Geral será o ponto central de consulta do Audio Copilot, permitindo que qualquer módulo localize rapidamente os recursos necessários para configuração, operação, análise, geração de relatórios e aprendizado da Inteligência Artificial.

---

# Funcionalidades

O módulo deverá permitir:

- Consulta unificada de todos os recursos cadastrados.
- Pesquisa global.
- Pesquisa por categoria.
- Pesquisa por tipo.
- Pesquisa por nome.
- Pesquisa por fabricante.
- Pesquisa por modelo.
- Pesquisa por etiquetas (tags).
- Filtros avançados.
- Visualização detalhada.
- Histórico de utilização.
- Relacionamentos entre recursos.

---

# Recursos disponíveis

A Biblioteca Geral deverá reunir informações provenientes dos seguintes módulos:

## Pessoas

- Pessoas cadastradas
- Histórico de participação

---

## Fontes Vocais

- Vocalistas
- Pregadores
- Dirigentes
- Leitores
- Convidados

---

## Instrumentistas

- Instrumentistas
- Histórico de utilização

---

## Instrumentos

- Instrumentos físicos
- Características técnicas
- Configurações preferenciais

---

## Microfones

- Microfones
- Características técnicas
- Estado
- Histórico

---

## Equipamentos

- Equipamentos de áudio
- Sistemas sem fio
- DI Box
- Pedaleiras
- Monitores
- Interfaces
- Demais equipamentos

---

## Recursos de Infraestrutura

- Recursos do templo
- Estruturas físicas
- Recursos de vídeo
- Recursos de iluminação
- Recursos de streaming

---

## Canais

- Entradas
- Saídas
- Grupos
- Canais preferenciais

---

## Presets

- Presets de canais
- Presets de equipamentos
- Presets personalizados

---

## Cenas

- Cenas cadastradas
- Configurações completas

---

## Eventos

- Eventos
- Programações
- Histórico

---

# Pesquisa Global

A pesquisa deverá localizar qualquer recurso do sistema.

Exemplos:

Pesquisar:

```
SM58
```

Resultado:

- Microfone Shure SM58
- Preset SM58 Vocal
- Eventos utilizando SM58

---

Pesquisar:

```
Robson
```

Resultado:

- Pessoa
- Instrumentista
- Fonte Vocal
- Eventos
- Presets associados
- Histórico

---

Pesquisar:

```
Violão Martin
```

Resultado:

- Instrumento
- Instrumentista
- Canal
- Presets
- Histórico de utilização

---

# Relacionamentos

Cada recurso poderá exibir seus relacionamentos.

Exemplo:

Pessoa

↓

Fonte Vocal

↓

Microfone

↓

Canal

↓

Preset

↓

Cena

↓

Evento

↓

Relatório

---

# Histórico

A Biblioteca deverá apresentar:

- Eventos onde foi utilizado
- Datas
- Alterações
- Configurações aplicadas
- Operadores envolvidos

---

# Etiquetas (Tags)

Os recursos poderão possuir etiquetas para facilitar pesquisas.

Exemplos:

- Vocal
- Pregador
- Violão
- Wireless
- Condensador
- Streaming
- Reserva
- Principal
- Especial

---

# Favoritos

O sistema poderá permitir marcar recursos favoritos para acesso rápido.

---

# Regras de Negócio

## Fonte única

A Biblioteca não armazenará informações próprias.

Ela será um agregador dos dados existentes nos demais módulos.

---

## Atualização automática

Sempre que um recurso for alterado, a Biblioteca deverá refletir automaticamente as mudanças.

---

## Pesquisa unificada

Uma única pesquisa deverá consultar todos os módulos cadastrados.

---

## Histórico

A Biblioteca deverá manter acesso ao histórico de utilização dos recursos.

---

# Interface

A tela deverá apresentar:

- Campo de pesquisa global
- Lista de categorias
- Lista de resultados
- Filtros avançados
- Visualização detalhada
- Relacionamentos
- Histórico
- Favoritos

---

# Integração com outros módulos

A Biblioteca Geral será utilizada por praticamente todo o sistema.

Principais integrações:

- Cadastro de Pessoas
- Gerenciador de Fontes Vocais
- Gerenciador de Instrumentistas
- Gerenciador de Instrumentos
- Gerenciador de Microfones
- Gerenciador de Equipamentos
- Gerenciador de Recursos de Infraestrutura
- Gerenciador de Canais
- Configuração do Evento
- Programação Técnica
- Motor do Audio Copilot
- Operação ao Vivo
- Engenharia Reversa da Ui24R
- IA Operacional
- IA de Engenharia de Áudio
- Relatórios

---

# Estrutura sugerida

```text
ResourceLibrary
│
├── search()
├── searchByCategory()
├── searchByType()
├── searchByTag()
├── searchByRelationship()
├── listFavorites()
├── recentItems()
├── getHistory()
├── getRelationships()
└── getResource()
```

---

# Classes previstas

- ResourceLibrary
- ResourceIndexer
- ResourceSearchEngine
- ResourceRelationshipService
- ResourceHistoryService
- ResourceLibraryController
- ResourceLibraryViewModel

---

# Benefícios

A Biblioteca Geral será o principal ponto de consulta do Audio Copilot, reunindo em um único local todos os recursos cadastrados no sistema. Essa centralização facilitará a pesquisa, o reaproveitamento de configurações, a navegação entre recursos relacionados, a geração de relatórios e o funcionamento da Inteligência Artificial, proporcionando uma visão completa e integrada da infraestrutura, dos participantes e do histórico operacional da igreja.