# Sprint F01 – Sistema de Gravação

## Objetivo

Definir a arquitetura do Sistema de Gravação do Audio Copilot, responsável por capturar, armazenar, organizar, reproduzir e disponibilizar gravações de áudio realizadas durante ensaios, cultos e atividades técnicas.

Este módulo estabelece toda a infraestrutura necessária para que as gravações possam ser utilizadas pelo operador, pelos relatórios do sistema e pelos mecanismos de Inteligência Artificial.

O Sistema de Gravação é um subsistema independente da mesa de som, podendo futuramente suportar diferentes fontes de áudio e múltiplos equipamentos.

---

# Visão Geral

O Sistema de Gravação permite registrar todo o histórico sonoro de um evento, mantendo sincronização com as ações realizadas pelo operador, pela IA e pelos demais módulos do Audio Copilot.

Além de registrar o áudio, o sistema também associa metadados que possibilitam análises posteriores, comparação entre eventos, geração de relatórios e aprendizado da Inteligência Artificial.

---

# Papel dentro do Audio Copilot

O Sistema de Gravação atua como a memória sonora do Audio Copilot.

Sua responsabilidade vai muito além de simplesmente salvar arquivos de áudio.

Entre suas funções estão:

- registrar eventos completos;
- gravar sessões independentes;
- capturar trechos específicos;
- manter buffer de replay;
- sincronizar eventos da IA;
- armazenar marcadores;
- disponibilizar gravações para análise;
- servir como base para relatórios e aprendizado.

---

# Arquitetura Geral

O subsistema é composto por diversos componentes especializados, cada um responsável por uma parte do processo de gravação.

```text
Sistema de Gravação
│
├── Recording Manager
├── Recording Session
├── Audio Buffer
├── Marker Manager
├── Replay Engine
├── Export Manager
├── Recording Library
└── AI Recording Integration
```

Cada componente possui responsabilidades bem definidas, reduzindo o acoplamento e facilitando futuras evoluções.

---

# Componentes do Sistema

## Recording Manager

Responsável pelo controle geral das gravações.

Suas responsabilidades incluem:

- iniciar gravações;
- finalizar gravações;
- pausar;
- retomar;
- controlar estados;
- criar sessões;
- coordenar os demais componentes.

Este componente representa o núcleo do sistema.

---

## Recording Session

Representa uma gravação individual.

Cada sessão possui identidade própria e contém todas as informações relacionadas àquela gravação.

Exemplos:

- Culto Domingo Manhã;
- Música 01;
- Música 02;
- Pregação;
- Teste de Microfone.

---

## Audio Buffer

Mantém continuamente uma quantidade configurável de áudio em memória.

Esse buffer permite:

- Replay Instantâneo;
- recuperação dos últimos minutos;
- análise imediata da IA.

O buffer funciona independentemente da existência de uma gravação salva.

---

## Marker Manager

Gerencia todos os marcadores existentes durante uma gravação.

Os marcadores podem ser criados:

- automaticamente pela IA;
- automaticamente pela liturgia;
- manualmente pelo operador.

Cada marcador permanece sincronizado com a Timeline.

---

## Replay Engine

Responsável pela reprodução inteligente do áudio.

Permite:

- reprodução normal;
- replay rápido;
- reprodução por trecho;
- navegação temporal.

---

## Export Manager

Responsável pela exportação das gravações.

Entre suas funções:

- exportação completa;
- exportação parcial;
- conversão de formatos;
- inclusão de metadados.

---

## Recording Library

Gerencia toda a biblioteca de gravações.

Permite:

- pesquisa;
- filtros;
- organização;
- exclusão;
- arquivamento.

---

## AI Recording Integration

Integra o Sistema de Gravação aos módulos de Inteligência Artificial.

A IA poderá utilizar as gravações para:

- aprendizado;
- comparação;
- análise automática;
- geração de recomendações;
- identificação de padrões.

---

# Tipos de Gravação

O sistema suporta diferentes modalidades de gravação.

## Gravação Completa

Registra todo o evento desde seu início até o encerramento.

Exemplo:

- Culto Domingo Manhã.

---

## Sessão

Permite criar gravações independentes dentro de um mesmo evento.

Exemplo:

Ensaio

- Música 01;
- Música 02;
- Música 03.

Cada sessão é armazenada individualmente.

---

## Trecho

Permite gravar apenas um intervalo específico.

Exemplos:

- teste do microfone;
- solo de guitarra;
- passagem de som;
- pregação.

---

## Replay Buffer

Permite reproduzir os últimos segundos ou minutos mesmo sem uma gravação permanente.

Exemplos:

- últimos 30 segundos;
- último minuto;
- últimos cinco minutos;
- últimos dez minutos.

---

# Fluxo Geral

O funcionamento do sistema segue o seguinte fluxo:

```text
Selecionar Tipo

↓

Criar Sessão

↓

Capturar Áudio

↓

Sincronizar Eventos

↓

Salvar Metadados

↓

Atualizar Biblioteca

↓

Disponibilizar para Replay

↓

Disponibilizar para IA
```

---

# Ciclo de Vida de uma Gravação

Cada gravação percorre diferentes estados.

```text
Criada

↓

Preparada

↓

Gravando

↓

Pausada

↓

Gravando

↓

Finalizada

↓

Arquivada
```

Após arquivada, a gravação permanece disponível para consulta, exportação e análise.

---

# Estados da Gravação

Uma gravação poderá assumir os seguintes estados:

- Preparando;
- Gravando;
- Pausada;
- Finalizando;
- Finalizada;
- Cancelada;
- Arquivada.

As transições entre estados serão controladas pelo Recording Manager.

---

# Metadados

Cada gravação deverá armazenar informações complementares.

Exemplos:

- identificador;
- nome;
- evento;
- sessão;
- operador;
- data;
- horário;
- duração;
- formato;
- tamanho;
- origem;
- quantidade de marcadores;
- quantidade de eventos registrados;
- versão do Audio Copilot.

Esses metadados serão utilizados pela Biblioteca, pelos Relatórios e pela IA.

---

# Organização da Biblioteca

As gravações serão organizadas por evento.

Exemplo:

```text
Culto Domingo

├── Completa
├── Música 01
├── Música 02
├── Pregação
└── Oração Final
```

Essa organização facilita a localização e a comparação entre sessões.

---

# Integração com Outros Módulos

O Sistema de Gravação recebe informações de:

- Eventos;
- Programação Técnica;
- Console de Operação;
- IA Audio Copilot;
- Motor de Alertas.

Também fornece informações para:

- Relatórios;
- Biblioteca;
- Replay;
- Comparação de Gravações;
- Aprendizado da IA.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- permitir apenas uma gravação completa ativa por evento;
- permitir múltiplas sessões independentes;
- permitir gravações parciais durante uma gravação completa;
- manter sincronização entre áudio e eventos registrados;
- preservar todos os metadados da gravação;
- armazenar automaticamente eventos produzidos pela IA;
- manter integridade da Timeline;
- atualizar automaticamente a Biblioteca de Gravações;
- permitir exportação apenas de gravações finalizadas.

---

# Requisitos Funcionais

O Sistema de Gravação deverá:

- iniciar gravações;
- interromper gravações;
- pausar gravações;
- retomar gravações;
- criar sessões;
- registrar trechos;
- manter Replay Buffer;
- sincronizar eventos;
- reproduzir gravações;
- exportar gravações;
- disponibilizar dados para a IA.

---

# Requisitos Não Funcionais

O sistema deverá:

- operar continuamente durante eventos longos;
- minimizar uso de memória;
- evitar perda de gravações em caso de falhas;
- garantir sincronização temporal;
- permitir futura expansão para múltiplos canais;
- manter baixa latência durante Replay.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- gravação multicanal;
- sincronização com vídeo;
- gravação em nuvem;
- transcrição automática;
- detecção automática de músicas;
- geração automática de capítulos;
- reconhecimento de locutores;
- comparação automática entre ensaio e culto;
- integração com OBS Studio.

---

# Situação da Sprint

**Status:** ✅ Concluída