# Sprint F07 – Recording Library

## Objetivo

Definir a arquitetura da **Recording Library**, componente responsável pelo armazenamento, organização, pesquisa e gerenciamento de todas as gravações realizadas pelo Audio Copilot.

A Recording Library funciona como o repositório central de gravações do sistema, permitindo ao operador localizar rapidamente qualquer sessão registrada, independentemente do evento ao qual pertence.

Seu objetivo é organizar o histórico completo das gravações, preservando sua integridade e facilitando futuras consultas, análises e comparações.

---

# Visão Geral

Toda gravação finalizada passa automaticamente a fazer parte da Recording Library.

A biblioteca não armazena apenas os arquivos de áudio, mas também todas as informações relacionadas às Recording Sessions.

Isso permite que o operador encontre rapidamente uma gravação utilizando diversos critérios de pesquisa.

---

# Papel dentro do Audio Copilot

A Recording Library é responsável por:

- armazenar gravações;
- organizar sessões;
- indexar metadados;
- realizar pesquisas;
- aplicar filtros;
- controlar arquivamento;
- fornecer gravações para Replay;
- disponibilizar gravações para a IA;
- servir como histórico permanente do sistema.

---

# Arquitetura Geral

A Recording Library é composta pelos seguintes componentes.

```text
Recording Library
│
├── Library Manager
├── Recording Index
├── Search Engine
├── Filter Engine
├── Archive Manager
├── Storage Manager
└── Library Statistics
```

Cada componente possui responsabilidades específicas para garantir organização e desempenho.

---

# Library Manager

É o componente principal da biblioteca.

Suas responsabilidades incluem:

- registrar novas gravações;
- atualizar informações;
- remover registros;
- organizar a biblioteca;
- disponibilizar consultas para os demais módulos.

---

# Recording Index

Mantém um índice de todas as Recording Sessions existentes.

Cada gravação é indexada utilizando informações como:

- identificador;
- evento;
- sessão;
- operador;
- data;
- categoria;
- duração.

Esse índice permite pesquisas rápidas sem necessidade de abrir os arquivos de áudio.

---

# Search Engine

Responsável pela pesquisa das gravações.

Permite localizar gravações utilizando diferentes critérios.

Exemplos:

- nome da sessão;
- nome do evento;
- operador;
- data;
- palavra-chave;
- marcador;
- observação.

---

# Filter Engine

Permite reduzir rapidamente os resultados apresentados.

Filtros previstos:

- período;
- evento;
- operador;
- tipo da gravação;
- duração;
- categoria;
- presença de alertas da IA.

Os filtros podem ser combinados entre si.

---

# Archive Manager

Responsável pelo gerenciamento do ciclo de vida das gravações.

Entre suas funções:

- arquivar;
- restaurar;
- excluir;
- organizar por período;
- controlar retenção de dados.

---

# Storage Manager

Responsável pela localização física dos arquivos.

Suas responsabilidades incluem:

- registrar caminho do arquivo;
- validar existência;
- monitorar espaço disponível;
- controlar movimentação dos arquivos.

O Storage Manager abstrai a forma de armazenamento utilizada.

---

# Library Statistics

Gera estatísticas da biblioteca.

Exemplos:

- quantidade de gravações;
- tempo total gravado;
- espaço utilizado;
- gravações por evento;
- gravações por operador;
- sessões mais acessadas.

Essas informações poderão ser utilizadas pelos relatórios administrativos.

---

# Organização da Biblioteca

A organização padrão ocorre por evento.

Exemplo:

```text
Culto Domingo

├── Gravação Completa
├── Música 01
├── Música 02
├── Pregação
└── Encerramento
```

Outro exemplo:

```text
Ensaio Quinta

├── Passagem de Som
├── Música 01
├── Música 02
├── Música 03
└── Ajuste Final
```

Essa estrutura facilita a localização das gravações.

---

# Estrutura de uma Gravação

Cada item da biblioteca deverá conter informações resumidas.

Exemplo:

```text
ID

Nome

Evento

Sessão

Categoria

Operador

Data

Hora

Duração

Status

Quantidade de Marcadores

Quantidade de Eventos

Arquivo
```

---

# Categorias

As gravações poderão ser classificadas em diferentes categorias.

Exemplos:

- Evento Completo;
- Sessão;
- Trecho;
- Replay;
- Teste Técnico;
- Calibração;
- Manutenção.

As categorias auxiliam na organização e pesquisa.

---

# Pesquisa Inteligente

A Recording Library deverá permitir pesquisas rápidas.

Exemplos:

```text
Pesquisar:

"Sola Scriptura"

↓

Todas as gravações relacionadas
```

```text
Pesquisar:

"Pregação"

↓

Todas as pregações gravadas
```

```text
Pesquisar:

"Robson"

↓

Eventos operados por Robson
```

---

# Fluxo de Funcionamento

O funcionamento da biblioteca segue o seguinte fluxo.

```text
Finalizar Gravação

↓

Registrar Recording Session

↓

Indexar Metadados

↓

Atualizar Biblioteca

↓

Disponibilizar Pesquisa

↓

Disponibilizar Replay

↓

Disponibilizar IA
```

---

# Integração com Outros Componentes

A Recording Library recebe informações de:

- Recording Manager;
- Recording Session;
- Marker Manager;
- Replay Engine;
- Export Manager.

Também fornece informações para:

- IA Audio Copilot;
- Relatórios;
- Comparação de Gravações;
- Sistema de Pesquisa.

---

# Organização Física

A organização física dos arquivos poderá seguir a seguinte estrutura.

```text
Gravações

└── 2028

    ├── Janeiro

    ├── Fevereiro

    ├── Março

    │   ├── Culto Domingo
    │   ├── Ensaio Quinta
    │   └── Casamento

    └── Abril
```

Essa estrutura facilita backup, arquivamento e manutenção.

---

# Regras de Negócio

A Recording Library deverá seguir as seguintes regras:

- registrar automaticamente toda gravação finalizada;
- impedir registros duplicados;
- manter histórico permanente;
- preservar metadados originais;
- permitir arquivamento sem perda de informações;
- manter consistência entre banco de dados e arquivos físicos;
- permitir pesquisas sem necessidade de carregar o áudio.

---

# Requisitos Funcionais

A Recording Library deverá permitir:

- cadastrar gravações;
- pesquisar;
- filtrar;
- arquivar;
- restaurar;
- excluir;
- consultar estatísticas;
- localizar arquivos;
- fornecer gravações para Replay;
- disponibilizar dados para a IA.

---

# Requisitos Não Funcionais

O componente deverá:

- responder rapidamente às pesquisas;
- suportar milhares de gravações;
- minimizar consumo de armazenamento;
- manter integridade dos registros;
- permitir futura utilização de armazenamento remoto.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- armazenamento em nuvem;
- sincronização entre computadores;
- biblioteca compartilhada entre operadores;
- classificação automática por IA;
- reconhecimento automático de músicas;
- pesquisa por conteúdo falado;
- pesquisa semântica;
- favoritos;
- etiquetas personalizadas;
- políticas automáticas de retenção e arquivamento.

---

# Situação da Sprint

**Status:** ✅ Concluída