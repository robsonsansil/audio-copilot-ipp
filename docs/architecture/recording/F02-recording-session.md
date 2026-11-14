# Sprint F02 – Recording Session

## Objetivo

Definir a arquitetura da **Recording Session**, componente responsável por representar uma sessão individual de gravação dentro do Audio Copilot.

Uma Recording Session corresponde a uma única gravação realizada pelo sistema, podendo representar um evento completo, uma música, uma passagem de som, um teste técnico ou qualquer outro trecho registrado pelo operador.

Este componente é responsável por concentrar todas as informações referentes à gravação, tornando-a uma entidade independente dentro da Biblioteca de Gravações.

---

# Visão Geral

Toda gravação realizada pelo Audio Copilot é armazenada como uma Recording Session.

Uma sessão representa um conjunto completo de informações relacionadas a um único registro de áudio, incluindo:

- dados da gravação;
- metadados;
- eventos sincronizados;
- marcadores;
- observações;
- informações da IA.

A sessão é criada pelo Recording Manager e permanece disponível durante todo o ciclo de vida da gravação.

---

# Responsabilidades

A Recording Session possui as seguintes responsabilidades:

- representar uma gravação individual;
- armazenar informações da sessão;
- manter o estado da gravação;
- controlar a duração;
- registrar metadados;
- sincronizar eventos;
- armazenar marcadores;
- disponibilizar informações para reprodução;
- fornecer dados para exportação.

---

# Tipos de Sessão

Uma Recording Session poderá representar diferentes tipos de gravação.

## Evento Completo

Representa toda a duração de um evento.

Exemplo:

- Culto Domingo Manhã.

---

## Sessão de Ensaio

Representa uma única música ou atividade realizada durante um ensaio.

Exemplos:

- Música 01 — Sola Scriptura;
- Música 02 — Castelo Forte.

---

## Trecho

Representa apenas uma parte específica da programação.

Exemplos:

- Pregação;
- Santa Ceia;
- Oração Final;
- Teste de Microfone.

---

## Sessão Técnica

Utilizada durante manutenção ou testes.

Exemplos:

- Equalização do PA;
- Ajuste do retorno;
- Teste de cabos;
- Calibração dos microfones.

---

# Estrutura da Sessão

Cada Recording Session deverá armazenar um conjunto de informações básicas.

Exemplo:

```text
Session ID

Nome

Tipo

Evento

Operador

Data

Hora de Início

Hora de Término

Duração

Estado

Formato

Arquivo

Marcadores

Eventos

Observações

Metadados
```

---

# Identificação

Cada sessão possuirá um identificador único.

Exemplo:

```text
REC-2028-03-09-0007
```

Esse identificador será utilizado internamente pelo sistema para localizar a gravação e relacioná-la aos demais módulos.

---

# Estados da Sessão

Durante seu ciclo de vida, a sessão poderá assumir diferentes estados.

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

As transições entre estados serão controladas exclusivamente pelo Recording Manager.

---

# Informações da Sessão

Cada sessão armazenará informações administrativas.

Exemplos:

- nome da sessão;
- descrição;
- categoria;
- responsável;
- local;
- data;
- horário.

Essas informações facilitarão futuras pesquisas na Biblioteca.

---

# Metadados

Além das informações administrativas, cada sessão armazenará metadados técnicos.

Exemplos:

- taxa de amostragem;
- bitrate;
- número de canais;
- codec utilizado;
- tamanho do arquivo;
- duração total.

Esses dados serão utilizados durante exportações e análises.

---

# Eventos Sincronizados

A sessão manterá uma linha do tempo contendo todos os eventos registrados durante a gravação.

Exemplos:

- mudança de cena;
- alteração de ganho;
- ajuste de equalização;
- abertura de microfone;
- fechamento de canal;
- alertas da IA.

Todos os eventos permanecerão sincronizados com o tempo da gravação.

---

# Marcadores

Uma sessão poderá possuir diversos marcadores.

Eles poderão ser criados:

- manualmente pelo operador;
- automaticamente pela IA;
- automaticamente pela Programação Técnica.

Exemplos:

- Início do Culto;
- Louvor;
- Sermão;
- Santa Ceia;
- Encerramento.

---

# Observações

O operador poderá registrar observações relacionadas à sessão.

Exemplos:

- retorno do teclado elevado;
- voz do pastor muito baixa;
- pequeno ruído no canal 07.

Essas observações poderão ser utilizadas posteriormente durante análises e relatórios.

---

# Relacionamento com Eventos

Cada sessão estará vinculada a um evento do Audio Copilot.

Exemplo:

```text
Evento

↓

Culto Domingo

↓

Sessões

├── Completa
├── Música 01
├── Música 02
├── Pregação
└── Encerramento
```

Esse relacionamento permitirá organizar naturalmente a Biblioteca de Gravações.

---

# Ciclo de Vida

O ciclo completo de uma sessão segue o seguinte fluxo.

```text
Criar Sessão

↓

Inicializar

↓

Capturar Áudio

↓

Registrar Eventos

↓

Registrar Marcadores

↓

Finalizar

↓

Salvar

↓

Arquivar
```

---

# Integração com Outros Componentes

A Recording Session comunica-se diretamente com:

- Recording Manager;
- Replay Engine;
- Marker Manager;
- Audio Buffer;
- Export Manager;
- Recording Library;
- IA Audio Copilot.

---

# Regras de Negócio

A Recording Session deverá seguir as seguintes regras:

- possuir identificador único;
- pertencer obrigatoriamente a um evento;
- registrar automaticamente data e horário;
- armazenar todos os eventos sincronizados;
- permitir marcadores ilimitados;
- preservar os metadados originais da gravação;
- não permitir edição após arquivamento, exceto de informações descritivas.

---

# Requisitos Funcionais

A Recording Session deverá permitir:

- criação de sessões;
- atualização do estado;
- armazenamento de eventos;
- armazenamento de marcadores;
- registro de observações;
- consulta de metadados;
- acesso para reprodução;
- exportação.

---

# Requisitos Não Funcionais

O componente deverá:

- manter consistência dos dados;
- garantir sincronização temporal;
- suportar sessões longas;
- minimizar consumo de memória;
- permitir expansão futura para gravações multicanal.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- assinatura digital das gravações;
- controle de versões da sessão;
- comentários colaborativos;
- anexação de documentos;
- sincronização com vídeo;
- transcrição automática;
- identificação automática de músicas;
- reconhecimento de locutores.

---

# Situação da Sprint

**Status:** ✅ Concluída