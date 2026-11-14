# Sprint F05 – Replay Engine

## Objetivo

Definir a arquitetura do **Replay Engine**, componente responsável pela reprodução inteligente das gravações realizadas pelo Audio Copilot.

O Replay Engine permite ao operador revisar rapidamente trechos específicos de um ensaio, culto ou teste técnico, mantendo sincronização com a Timeline, os marcadores, os eventos registrados pela IA e as alterações realizadas durante a operação.

Seu objetivo é transformar a reprodução de áudio em uma ferramenta de análise operacional e não apenas em um simples player de áudio.

---

# Visão Geral

Durante uma operação é comum surgir a necessidade de ouvir novamente um determinado momento.

Exemplos:

- verificar se ocorreu microfonia;
- conferir uma alteração de ganho;
- analisar um problema no retorno;
- revisar uma música do ensaio;
- escutar novamente um trecho da pregação.

O Replay Engine permite localizar esses momentos rapidamente, sem necessidade de procurar manualmente toda a gravação.

---

# Papel dentro do Audio Copilot

O Replay Engine é responsável por toda a reprodução inteligente das gravações.

Entre suas funções estão:

- reproduzir gravações;
- reproduzir Replay Buffer;
- navegar pela Timeline;
- sincronizar marcadores;
- sincronizar eventos da IA;
- localizar trechos específicos;
- controlar velocidade de reprodução;
- fornecer áudio para análise.

---

# Arquitetura Geral

O Replay Engine é composto pelos seguintes módulos.

```text
Replay Engine
│
├── Playback Controller
├── Timeline Navigator
├── Replay Buffer Reader
├── Marker Navigator
├── Event Synchronizer
├── Playback Speed Controller
└── Audio Output
```

Cada módulo possui responsabilidades específicas durante a reprodução.

---

# Playback Controller

Responsável pelo controle principal da reprodução.

Suas funções incluem:

- reproduzir;
- pausar;
- parar;
- reiniciar;
- avançar;
- retroceder;
- alterar posição da reprodução.

---

# Timeline Navigator

Permite navegar livremente pela Timeline.

O operador poderá:

- clicar em qualquer posição;
- arrastar o cursor;
- aproximar (Zoom In);
- afastar (Zoom Out);
- navegar utilizando atalhos.

Toda navegação permanece sincronizada com os eventos registrados.

---

# Replay Buffer Reader

Responsável pela leitura do Audio Buffer.

Permite reproduzir imediatamente os últimos:

- 30 segundos;
- 1 minuto;
- 5 minutos;
- 10 minutos.

Mesmo quando nenhuma gravação permanente estiver ativa.

---

# Marker Navigator

Permite navegar entre marcadores registrados durante a gravação.

Exemplos:

- próximo marcador;
- marcador anterior;
- ir para "Pregação";
- ir para "Microfonia";
- ir para "Mudança de Cena".

---

# Event Synchronizer

Mantém sincronização entre a reprodução e todos os eventos registrados.

Durante o Replay poderão ser exibidos:

- alterações de ganho;
- mudanças de cena;
- alterações de equalização;
- alertas da IA;
- observações do operador.

Os eventos aparecem exatamente no instante em que ocorreram.

---

# Playback Speed Controller

Permite controlar a velocidade da reprodução.

Velocidades previstas:

- 0,5x;
- 1x;
- 1,25x;
- 1,5x;
- 2x.

Essa funcionalidade facilita análises rápidas e revisões detalhadas.

---

# Audio Output

Responsável por enviar o áudio reproduzido ao dispositivo de saída configurado pelo operador.

No futuro poderá permitir:

- seleção da saída de áudio;
- reprodução independente por canal;
- monitoramento em múltiplos dispositivos.

---

# Modos de Reprodução

O Replay Engine suporta diferentes formas de reprodução.

## Reprodução Completa

Reproduz toda a Recording Session.

Exemplo:

```text
Culto Domingo Manhã
```

---

## Reprodução por Sessão

Reproduz apenas uma sessão específica.

Exemplo:

```text
Ensaio

↓

Música 02
```

---

## Reprodução por Trecho

Reproduz somente um intervalo selecionado.

Exemplo:

```text
00:12:30

↓

00:16:45
```

---

## Replay Instantâneo

Utiliza diretamente o Audio Buffer.

Exemplos:

- últimos 30 segundos;
- último minuto;
- últimos cinco minutos.

---

# Fluxo de Funcionamento

O funcionamento segue o seguinte fluxo.

```text
Selecionar Gravação

↓

Carregar Timeline

↓

Sincronizar Eventos

↓

Posicionar Cursor

↓

Reproduzir

↓

Atualizar Timeline

↓

Finalizar
```

---

# Navegação Inteligente

Durante a reprodução o operador poderá navegar rapidamente utilizando:

- Timeline;
- marcadores;
- eventos da IA;
- snapshots;
- etapas da liturgia.

Exemplo:

```text
Clique em:

Pregação

↓

Player

↓

Posiciona em 00:41:18
```

---

# Integração com Marcadores

Ao selecionar um marcador:

```text
Marcador

↓

Timeline

↓

Reposicionar Player

↓

Reprodução
```

Todo o processo ocorre automaticamente.

---

# Integração com a Programação Técnica

Quando a gravação estiver vinculada a uma Programação Técnica, o Replay poderá destacar automaticamente a etapa correspondente.

Exemplo:

```text
Timeline

↓

00:18:32

↓

Louvor Congregacional

↓

Cena 03
```

Isso facilita a análise do evento.

---

# Integração com a Inteligência Artificial

Durante a reprodução, a IA poderá apresentar informações sincronizadas.

Exemplos:

- clipping detectado;
- ganho elevado;
- possível microfonia;
- sugestão de equalização;
- alteração importante realizada pelo operador.

Esses eventos permanecem sincronizados com a Timeline.

---

# Integração com o Audio Buffer

O Replay Engine utiliza diretamente o Audio Buffer quando solicitado.

Fluxo:

```text
Replay

↓

Replay Engine

↓

Audio Buffer

↓

Player
```

Sem necessidade de criar uma gravação permanente.

---

# Controles Disponíveis

O Replay Engine deverá oferecer os seguintes controles.

- reproduzir;
- pausar;
- parar;
- avançar;
- retroceder;
- alterar velocidade;
- alterar posição;
- repetir trecho;
- repetir sessão.

---

# Regras de Negócio

O Replay Engine deverá seguir as seguintes regras:

- manter sincronização entre áudio e Timeline;
- sincronizar todos os marcadores;
- sincronizar eventos registrados pela IA;
- permitir Replay Buffer mesmo sem gravação permanente;
- permitir alteração da velocidade sem modificar a gravação original;
- preservar a integridade da Recording Session.

---

# Requisitos Funcionais

O Replay Engine deverá permitir:

- reproduzir gravações;
- reproduzir Replay Buffer;
- navegar pela Timeline;
- navegar por marcadores;
- alterar velocidade;
- repetir trechos;
- sincronizar eventos;
- sincronizar snapshots.

---

# Requisitos Não Funcionais

O componente deverá:

- apresentar baixa latência;
- responder rapidamente aos comandos;
- manter sincronização precisa com a Timeline;
- operar durante gravações longas;
- permitir futura reprodução multicanal.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- reprodução por canal individual;
- comparação simultânea entre duas gravações;
- reprodução sincronizada com vídeo;
- visualização espectral do áudio;
- busca inteligente por palavras ou eventos;
- transcrição sincronizada;
- comparação entre ensaio e culto;
- reprodução colaborativa entre operadores.

---

# Situação da Sprint

**Status:** ✅ Concluída