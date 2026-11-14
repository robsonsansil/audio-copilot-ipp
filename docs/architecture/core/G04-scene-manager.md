# Sprint G04 – Scene Manager

## Objetivo

Definir a arquitetura do **Scene Manager**, componente responsável pelo gerenciamento das **Cenas** do Audio Copilot.

Uma cena representa um conjunto completo de configurações da mesa de som que poderá ser aplicado automaticamente ou manualmente durante um evento.

O Scene Manager é responsável por organizar, versionar, validar, aplicar e acompanhar todas as cenas utilizadas durante ensaios, cultos e demais eventos.

---

# Visão Geral

Durante um evento, diferentes momentos exigem configurações distintas da mesa de som.

Exemplos:

- Louvor Congregacional;
- Oração;
- Avisos;
- Pregação;
- Santa Ceia;
- Teatro;
- Coral;
- Encerramento.

Cada um desses momentos pode possuir uma cena específica.

O Scene Manager centraliza o gerenciamento dessas configurações.

---

# Papel dentro do Audio Copilot

O Scene Manager possui as seguintes responsabilidades:

- cadastrar cenas;
- editar cenas;
- organizar biblioteca de cenas;
- controlar versões;
- validar cenas;
- aplicar cenas;
- comparar cenas;
- registrar histórico de utilização.

---

# Arquitetura Geral

O componente é composto pelos seguintes módulos.

```text
Scene Manager
│
├── Scene Registry
├── Scene Controller
├── Scene Repository
├── Scene Validator
├── Scene Versioning
├── Scene History
└── Scene Comparison
```

Cada módulo possui responsabilidades específicas.

---

# Scene Registry

Responsável pelo cadastro das cenas.

Cada cena deverá possuir um identificador único.

Exemplo:

```text
SCN-000154
```

Também serão registrados:

- nome;
- categoria;
- descrição;
- versão;
- data de criação;
- autor.

---

# Scene Controller

Coordena toda a utilização das cenas.

Permite:

- criar;
- editar;
- duplicar;
- excluir;
- aplicar;
- restaurar;
- importar;
- exportar.

Também controla a aplicação automática durante o evento.

---

# Scene Repository

Responsável pelo armazenamento permanente das cenas.

Cada cena armazenará todas as configurações necessárias para reconstruir completamente o estado da mesa.

---

# Scene Validator

Valida a consistência da cena.

São verificadas informações como:

- canais existentes;
- parâmetros válidos;
- recursos disponíveis;
- compatibilidade com a mesa conectada;
- integridade dos dados.

Uma cena inválida não poderá ser aplicada.

---

# Scene Versioning

Controla o versionamento das cenas.

Exemplo:

```text
Cena "Pregação"

v1.0

↓

v1.1

↓

v1.2

↓

v2.0
```

Todas as versões permanecem armazenadas para consulta e restauração.

---

# Scene History

Registra toda a utilização das cenas.

Exemplos:

- criação;
- edição;
- aplicação;
- restauração;
- exclusão;
- alteração de versão.

---

# Scene Comparison

Permite comparar duas cenas.

O sistema identifica automaticamente diferenças entre:

- ganho;
- fader;
- mute;
- EQ;
- compressor;
- gate;
- panorama;
- envios auxiliares;
- FX.

Essa comparação auxilia na revisão e otimização das configurações.

---

# Estrutura da Cena

Cada cena deverá possuir:

```text
Cena

ID

Nome

Categoria

Descrição

Versão

Autor

Data de criação

Última atualização
```

---

# Estrutura Interna

Cada cena poderá armazenar:

```text
Cena
│
├── Canais
├── Ganhos
├── Faders
├── Mutes
├── Equalização
├── Compressores
├── Gates
├── Auxiliares
├── FX
├── DCAs
└── Configurações Gerais
```

Todos esses parâmetros serão restaurados quando a cena for aplicada.

---

# Biblioteca de Cenas

As cenas poderão ser organizadas por categoria.

Exemplos:

- Cultos;
- Ensaios;
- Conferências;
- Santa Ceia;
- Casamentos;
- Eventos Especiais;
- Testes Técnicos.

Também poderão possuir etiquetas (tags) para facilitar pesquisas.

---

# Aplicação das Cenas

A aplicação poderá ocorrer de três formas.

## Manual

O operador escolhe a cena e realiza sua aplicação.

---

## Automática

A IA aplica a cena conforme o avanço da Programação Técnica ou da Liturgia.

---

## Assistida

A IA sugere a cena e aguarda confirmação do operador.

---

# Fluxo de Funcionamento

```text
Criar Cena

↓

Configurar Parâmetros

↓

Validar

↓

Salvar

↓

Associar à Programação

↓

Aplicar

↓

Registrar Histórico
```

---

# Integração com Outros Componentes

O Scene Manager fornece informações para:

- Event Manager;
- Program Manager;
- Liturgy Manager;
- Rule Engine;
- Alert Engine;
- Operation State;
- Ui24R Integration;
- IA Operacional;
- Console de Operação.

Também recebe informações provenientes da mesa de som e da Programação Técnica.

---

# Regras de Negócio

O sistema deverá seguir as seguintes regras:

- toda cena deverá possuir nome único;
- cenas deverão possuir versionamento;
- somente cenas válidas poderão ser aplicadas;
- toda aplicação deverá ser registrada;
- alterações durante o evento poderão gerar uma nova versão da cena;
- a restauração de versões anteriores deverá ser permitida.

---

# Requisitos Funcionais

O Scene Manager deverá permitir:

- criar cenas;
- editar cenas;
- excluir cenas;
- duplicar cenas;
- pesquisar cenas;
- organizar biblioteca;
- aplicar cenas;
- comparar cenas;
- restaurar versões;
- importar e exportar cenas.

---

# Requisitos Não Funcionais

O componente deverá:

- aplicar cenas rapidamente;
- preservar a integridade das configurações;
- manter compatibilidade entre versões;
- suportar centenas de cenas cadastradas;
- responder imediatamente às solicitações da IA e do operador.

---

# Melhorias Futuras

Funcionalidades previstas para versões futuras:

- aplicação parcial de cenas;
- comparação gráfica entre versões;
- sugestões automáticas de otimização pela IA;
- cenas inteligentes adaptativas;
- compartilhamento de cenas entre igrejas;
- sincronização em nuvem;
- biblioteca pública de cenas;
- recomendação automática de cenas baseada no histórico;
- integração com múltiplos modelos de mesas digitais.

---

# Situação da Sprint

**Status:** ✅ Concluída