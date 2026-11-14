# Sprint E10 – System Check

## Objetivo

Definir o componente responsável por executar verificações automáticas e assistidas da infraestrutura de áudio, garantindo que todos os equipamentos, canais e configurações estejam prontos para operação.

O **System Check** funciona como um checklist inteligente do Audio Copilot, conduzindo o operador por uma sequência padronizada de verificações antes, durante ou após um evento técnico.

Enquanto o **Diagnostic Engine** identifica falhas e o **Health Monitor** acompanha continuamente a saúde do sistema, o System Check verifica se todos os requisitos operacionais foram atendidos.

---

# Visão Geral

Antes de um culto ou ensaio, é comum realizar diversas conferências.

Exemplos:

- verificar comunicação com a mesa;
- conferir os microfones;
- validar os retornos;
- testar os auxiliares;
- verificar os efeitos;
- conferir snapshots;
- validar phantom power;
- testar gravação.

O System Check organiza esse processo de forma estruturada.

---

# Filosofia

O System Check foi desenvolvido seguindo cinco princípios.

## Padronização

Todas as verificações devem seguir um procedimento consistente.

---

## Simplicidade

O operador deve saber exatamente o que precisa ser conferido.

---

## Rastreabilidade

Cada verificação deve ficar registrada na sessão técnica.

---

## Flexibilidade

O checklist deve poder ser adaptado para diferentes igrejas e eventos.

---

## Segurança

Nenhum item importante deve ser esquecido.

---

# Arquitetura

```text
Maintenance Manager

↓

System Check

├── Checklist
├── Verificações
├── Validação
├── Pendências
├── Resultados
└── Histórico
```

---

# Responsabilidades

O System Check será responsável por:

- executar checklists técnicos;
- validar configurações da mesa;
- registrar itens aprovados;
- identificar pendências;
- acompanhar o progresso das verificações;
- fornecer informações ao relatório técnico.

---

# Fluxo Geral

```text
Selecionar Checklist

↓

Executar Verificações

↓

Registrar Resultado

↓

Identificar Pendências

↓

Finalizar Checklist
```

---

# Tipos de Checklist

O componente poderá disponibilizar diferentes modelos.

Exemplos:

- Pré-culto;
- Pós-culto;
- Ensaio;
- Instalação;
- Manutenção preventiva;
- Manutenção corretiva;
- Atualização de firmware.

---

# Estrutura do Checklist

Cada checklist poderá conter:

- categoria;
- descrição;
- prioridade;
- responsável;
- status;
- observações.

---

# Categorias

As verificações poderão ser organizadas por área.

Exemplo:

```text
Mesa

↓

Entradas

↓

Saídas

↓

Monitores

↓

Rede

↓

Snapshots

↓

Gravação
```

---

# Verificação da Mesa

O System Check poderá validar:

- conexão ativa;
- firmware;
- relógio do sistema;
- comunicação com a aplicação;
- configuração geral.

---

# Verificação das Entradas

Poderão ser conferidos:

- canais ativos;
- ganho;
- phantom power;
- polaridade;
- presença de sinal;
- clipping.

---

# Verificação das Saídas

Também poderão ser avaliadas:

- Main LR;
- Auxiliares;
- Matrix;
- Monitores;
- Saídas de gravação.

---

# Verificação dos Processamentos

O checklist poderá incluir:

- equalizadores;
- compressores;
- gates;
- limitadores;
- efeitos;
- delays;
- reverbs.

---

# Verificação da Rede

O componente poderá validar:

- comunicação com a Ui24R;
- estabilidade da conexão;
- perda de pacotes;
- latência;
- disponibilidade da interface web.

---

# Verificação dos Snapshots

Também poderão ser conferidos:

- existência;
- integridade;
- versão;
- compatibilidade;
- snapshot padrão do culto.

---

# Registro dos Resultados

Cada item poderá assumir um dos seguintes estados.

```text
Não iniciado

↓

Em andamento

↓

Aprovado

↓

Aprovado com ressalvas

↓

Reprovado

↓

Ignorado
```

---

# Pendências

Caso alguma verificação falhe, ela poderá ser adicionada automaticamente à lista de pendências.

Exemplo:

```text
Auxiliar 03

↓

Sem sinal

↓

Pendência registrada
```

---

# Observações

Cada item poderá conter observações técnicas.

Exemplo:

```text
Microfone 02

↓

Substituir cabo antes do culto.
```

---

# Execução Assistida

O Audio Copilot poderá conduzir o operador passo a passo.

Exemplo:

```text
Passo 1

↓

Verificar comunicação

↓

Passo 2

↓

Testar Main LR

↓

Passo 3

↓

Testar Monitores
```

---

# Progresso

O componente acompanhará a evolução do checklist.

Exemplo:

```text
35%

↓

12 de 34 itens concluídos
```

---

# Integração com o Diagnostic Engine

Sempre que um item apresentar falha, o Diagnostic Engine poderá ser acionado automaticamente para investigar sua causa.

Fluxo:

```text
Falha

↓

Diagnostic Engine

↓

Diagnóstico

↓

Resultado
```

---

# Integração com o Channel Tester

Durante verificações individuais, o System Check poderá solicitar testes específicos para canais ou saídas.

---

# Integração com o Health Monitor

Antes da conclusão do checklist, o estado geral do sistema poderá ser consultado para validar a estabilidade operacional.

---

# Integração com o Maintenance Report

Todos os itens executados serão incorporados ao relatório técnico da sessão.

O relatório poderá apresentar:

- itens aprovados;
- pendências;
- observações;
- tempo de execução;
- responsável.

---

# Integração com o Histórico

Cada checklist poderá ser armazenado para:

- auditorias;
- comparação entre manutenções;
- acompanhamento da infraestrutura;
- análise de recorrência de falhas.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- checklist atual;
- progresso;
- itens pendentes;
- falhas encontradas;
- percentual concluído.

---

# Benefícios

O System Check proporciona:

- padronização das verificações;
- redução de esquecimentos;
- maior segurança operacional;
- documentação automática;
- preparação mais confiável para eventos;
- integração com os demais módulos do Audio Copilot.

---

# Separação de Responsabilidades

O System Check não:

- realiza diagnósticos aprofundados;
- gera sinais de teste;
- executa calibrações;
- monitora continuamente a mesa;
- altera automaticamente configurações.

Sua responsabilidade é conduzir e registrar verificações estruturadas da infraestrutura de áudio, garantindo que todos os requisitos operacionais tenham sido conferidos antes da utilização do sistema.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- checklists personalizados por igreja;
- checklists específicos por tipo de evento;
- execução automática de verificações suportadas pela mesa;
- integração com QR Codes para identificação de equipamentos;
- assinatura digital do técnico responsável;
- checklists colaborativos entre múltiplos operadores;
- geração automática de pendências para manutenção futura;
- validação inteligente baseada em Inteligência Artificial.

---

# Relação com Outros Componentes

O System Check trabalha diretamente com:

- Modo Técnico;
- Maintenance Manager;
- Diagnostic Engine;
- Channel Tester;
- Signal Generator;
- Calibration Manager;
- Health Monitor;
- Maintenance Report;
- History Manager;
- Recommendation Engine;
- Dashboard Operacional.

Ele representa o checklist inteligente do Modo Técnico, garantindo que todas as verificações necessárias sejam executadas de forma organizada, documentada e rastreável antes da liberação do sistema para operação.

---

# Situação da Sprint

**Status:** ✅ Concluída