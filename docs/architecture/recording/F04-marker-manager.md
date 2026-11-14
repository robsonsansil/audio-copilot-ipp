# Sprint F04 – Marker Manager

## Objetivo

Definir a arquitetura do **Marker Manager**, componente responsável por criar, armazenar, sincronizar e gerenciar todos os marcadores registrados durante uma gravação.

Os marcadores representam acontecimentos importantes ocorridos ao longo do evento e permitem localizar rapidamente momentos específicos da Timeline, facilitando a navegação, o Replay, a geração de relatórios e as análises realizadas pela Inteligência Artificial.

O Marker Manager funciona como um índice inteligente da gravação.

---

# Visão Geral

Durante um ensaio ou culto, diversos acontecimentos possuem importância operacional.

Exemplos:

- início do culto;
- início do louvor;
- entrada da pregação;
- mudança de cena;
- ajuste de ganho;
- início de microfonia;
- clipping;
- observação do operador.

Em vez de procurar manualmente esses momentos na gravação, o Marker Manager registra todos eles automaticamente na Timeline.

---

# Papel dentro do Audio Copilot

O Marker Manager atua como um organizador cronológico dos acontecimentos do evento.

Suas responsabilidades incluem:

- criar marcadores;
- armazenar marcadores;
- sincronizar com a Timeline;
- organizar eventos por categoria;
- permitir pesquisas;
- disponibilizar dados para Replay;
- fornecer informações para a IA;
- auxiliar na geração de relatórios.

---

# Arquitetura Geral

O componente é formado pelos seguintes módulos.

```text
Marker Manager
│
├── Marker Creator
├── Marker Repository
├── Timeline Sync
├── Marker Search
├── Marker Filter
└── Marker Export
```

Cada módulo possui responsabilidades específicas para manter a organização dos marcadores.

---

# Marker Creator

Responsável pela criação de novos marcadores.

Os marcadores podem ser criados:

- manualmente pelo operador;
- automaticamente pela IA;
- automaticamente pela Programação Técnica;
- automaticamente pelos Modos de Operação.

Cada marcador recebe um identificador único e um instante exato da gravação.

---

# Marker Repository

Armazena todos os marcadores pertencentes à Recording Session.

Cada marcador permanece associado à sua gravação original durante todo o ciclo de vida da sessão.

---

# Timeline Sync

Mantém todos os marcadores sincronizados com a Timeline.

Ao navegar pela gravação, os marcadores permanecem exatamente na posição correspondente ao instante em que ocorreram.

---

# Marker Search

Permite localizar rapidamente marcadores específicos.

Exemplos:

- procurar "Pregação";
- procurar "Microfonia";
- procurar "Canal 05";
- procurar "Ganho".

---

# Marker Filter

Permite visualizar apenas categorias específicas.

Exemplos:

- apenas eventos da IA;
- apenas marcadores manuais;
- apenas alterações de canais;
- apenas alertas.

Essa funcionalidade reduz a quantidade de informações exibidas durante análises.

---

# Marker Export

Disponibiliza os marcadores para:

- relatórios;
- exportações;
- comparação entre gravações;
- Inteligência Artificial.

---

# Tipos de Marcadores

O sistema suporta diferentes categorias de marcadores.

## Marcadores Manuais

Criados diretamente pelo operador.

Exemplos:

- Voz muito baixa;
- Rever equalização;
- Problema no retorno.

---

## Marcadores Automáticos

Criados automaticamente pelo próprio Audio Copilot.

Exemplos:

- início da gravação;
- pausa;
- retomada;
- finalização.

---

## Marcadores da Programação

Gerados automaticamente pela Programação Técnica.

Exemplos:

- Louvor Congregacional;
- Oração Inicial;
- Avisos;
- Pregação;
- Santa Ceia;
- Encerramento.

---

## Marcadores da IA

Criados automaticamente pela Inteligência Artificial.

Exemplos:

- clipping detectado;
- possível microfonia;
- ganho elevado;
- retorno excessivo;
- pico de volume.

---

## Marcadores Técnicos

Relacionados às alterações realizadas durante a operação.

Exemplos:

- mudança de cena;
- alteração de preset;
- ajuste de compressor;
- alteração de equalização;
- alteração de ganho.

---

# Estrutura de um Marcador

Cada marcador deverá armazenar as seguintes informações.

```text
Marker ID

Categoria

Título

Descrição

Origem

Horário

Tempo da Gravação

Prioridade

Canal Relacionado

Autor

Metadados
```

---

# Prioridade

Cada marcador poderá possuir um nível de importância.

Exemplo:

```text
Baixa

Média

Alta

Crítica
```

Essa prioridade poderá ser utilizada pelos relatórios e pela IA.

---

# Fluxo de Funcionamento

O funcionamento ocorre da seguinte forma.

```text
Evento

↓

Marker Creator

↓

Marker Repository

↓

Timeline

↓

Replay

↓

Relatórios

↓

IA
```

Todo o processo ocorre automaticamente durante a gravação.

---

# Integração com a Timeline

A Timeline representa visualmente todos os marcadores.

Exemplo:

```text
00:00 ────────────────► Tempo

▲ Início

▲ Louvor

▲ Pregação

▲ Microfonia

▲ Encerramento
```

Ao selecionar um marcador, o Player será reposicionado automaticamente naquele instante.

---

# Integração com Replay

Durante o Replay, o operador poderá navegar diretamente entre os marcadores.

Exemplo:

```text
Próximo Marcador

↓

Pregação

↓

Reproduzir
```

Ou:

```text
Marcador

↓

Microfonia

↓

Ir para 00:42:18
```

---

# Integração com a Inteligência Artificial

A IA utilizará os marcadores para:

- aprender padrões;
- localizar eventos relevantes;
- identificar recorrências;
- gerar recomendações;
- produzir relatórios inteligentes.

Marcadores criados automaticamente pela IA permanecerão identificados como tal.

---

# Organização por Categorias

Os marcadores poderão ser agrupados por categoria.

Exemplo:

```text
Operação

├── Mudança de Cena
├── Ajuste de Ganho
└── Equalização

IA

├── Clipping
├── Microfonia
└── Pico

Liturgia

├── Louvor
├── Pregação
└── Encerramento

Operador

├── Observação
├── Revisar
└── Atenção
```

---

# Regras de Negócio

O Marker Manager deverá seguir as seguintes regras:

- todos os marcadores devem possuir horário exato;
- um marcador pertence a apenas uma Recording Session;
- a exclusão de uma sessão remove seus marcadores;
- marcadores automáticos não poderão ser editados;
- marcadores manuais poderão ser editados pelo operador;
- todos os marcadores deverão permanecer sincronizados com a Timeline.

---

# Requisitos Funcionais

O Marker Manager deverá permitir:

- criar marcadores;
- editar marcadores manuais;
- excluir marcadores manuais;
- pesquisar marcadores;
- filtrar por categoria;
- sincronizar com Replay;
- sincronizar com a IA;
- exportar marcadores.

---

# Requisitos Não Funcionais

O componente deverá:

- manter sincronização temporal precisa;
- permitir milhares de marcadores por gravação;
- responder rapidamente às pesquisas;
- consumir pouca memória;
- garantir integridade dos dados.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- marcadores coloridos por categoria;
- favoritos;
- comentários colaborativos;
- anexação de imagens;
- anexação de documentos;
- marcadores por canal de áudio;
- agrupamento automático por IA;
- reconhecimento automático de músicas;
- criação automática de capítulos da gravação.

---

# Situação da Sprint

**Status:** ✅ Concluída