# Sprint E10 – Signal Generator

## Objetivo

Definir o componente responsável por gerar sinais de teste controlados para calibração, diagnóstico, validação e manutenção da infraestrutura de áudio.

O **Signal Generator** fornece sinais de referência que permitem testar canais, saídas, processadores e sistemas de sonorização de forma padronizada e repetível.

Enquanto o **Channel Tester** valida um canal específico e o **Diagnostic Engine** identifica falhas, o Signal Generator fornece os sinais necessários para que esses testes sejam executados com precisão.

---

# Visão Geral

Durante uma manutenção é comum utilizar sinais de referência para verificar o funcionamento da mesa e do sistema de som.

Exemplos:

- testar um canal;
- verificar um cabo;
- calibrar um monitor;
- ajustar o ganho;
- conferir uma saída auxiliar;
- validar um compressor;
- medir resposta do sistema.

O Signal Generator centraliza essa funcionalidade dentro do Audio Copilot.

---

# Filosofia

O Signal Generator foi desenvolvido seguindo cinco princípios.

## Precisão

Os sinais devem possuir frequência, amplitude e duração controladas.

---

## Segurança

A geração de sinais deve evitar níveis que possam causar desconforto ou danos aos equipamentos.

---

## Flexibilidade

O operador poderá selecionar diferentes tipos de sinais conforme o objetivo do teste.

---

## Repetibilidade

Os mesmos parâmetros devem produzir exatamente os mesmos resultados.

---

## Integração

Os sinais poderão ser utilizados pelos demais módulos do Modo Técnico.

---

# Arquitetura

```text
Maintenance Manager

↓

Signal Generator

├── Geração
├── Configuração
├── Frequências
├── Níveis
├── Destinos
└── Controle

↓

Mesa Ui24R
```

---

# Responsabilidades

O Signal Generator será responsável por:

- gerar sinais de teste;
- controlar frequência e nível;
- direcionar sinais para canais ou saídas;
- auxiliar na calibração;
- apoiar diagnósticos;
- registrar a utilização dos sinais.

---

# Fluxo Geral

```text
Selecionar Sinal

↓

Configurar Parâmetros

↓

Selecionar Destino

↓

Gerar Sinal

↓

Executar Teste

↓

Encerrar
```

---

# Tipos de Sinais

O componente poderá gerar diferentes sinais de referência.

Exemplos:

- Sine Wave;
- Pink Noise;
- White Noise;
- Sweep Logarítmico;
- Sweep Linear;
- Pulse;
- Tone de referência;
- Burst.

---

# Sine Wave

Utilizada para:

- testes de frequência;
- calibração;
- validação de equipamentos;
- medições.

O operador poderá selecionar a frequência desejada.

---

# Pink Noise

Utilizado para:

- equalização do sistema;
- ajuste de PAs;
- calibração de monitores;
- análise em tempo real.

---

# White Noise

Indicado para:

- testes gerais;
- validação de equipamentos;
- medições laboratoriais.

---

# Sweep

O sistema poderá gerar varreduras de frequência.

Exemplo:

```text
20 Hz

↓

20 kHz

↓

Varredura Contínua
```

Esse recurso auxilia na identificação de ressonâncias e falhas na resposta do sistema.

---

# Pulse

O Pulse poderá ser utilizado para:

- localizar canais;
- validar roteamentos;
- identificar conexões;
- sincronizar testes.

---

# Frequência

O operador poderá definir:

- frequência inicial;
- frequência final;
- frequência fixa;
- velocidade da varredura.

---

# Nível de Saída

Também poderão ser configurados:

- nível do sinal;
- headroom;
- ganho;
- duração;
- repetição.

O sistema poderá limitar automaticamente níveis considerados inseguros.

---

# Destino do Sinal

Os sinais poderão ser enviados para:

- canal específico;
- Main LR;
- Auxiliar;
- Matrix;
- Bus;
- saída de gravação.

---

# Tempo de Execução

Cada sinal poderá possuir:

- início;
- duração;
- repetição;
- parada automática.

---

# Segurança Operacional

Antes da geração do sinal o sistema poderá verificar:

- volume Master;
- canais ativos;
- monitores conectados;
- estado do sistema;
- modo operacional.

Caso exista risco operacional, o operador poderá receber um alerta antes da execução.

---

# Presets

O Signal Generator poderá disponibilizar configurações pré-definidas.

Exemplos:

- Calibração do PA;
- Teste de Monitor;
- Teste de Canal;
- Equalização;
- Verificação de Auxiliares.

---

# Registro

Cada utilização poderá armazenar:

- operador;
- horário;
- tipo de sinal;
- frequência;
- nível;
- destino;
- duração.

---

# Integração com o Channel Tester

O Channel Tester poderá solicitar automaticamente um sinal adequado para validar determinado canal.

Fluxo:

```text
Teste

↓

Signal Generator

↓

Canal 12

↓

Resultado
```

---

# Integração com o Calibration Manager

Durante a calibração, o Signal Generator fornecerá os sinais utilizados para ajustes de ganho, equalização e resposta do sistema.

---

# Integração com o Diagnostic Engine

Quando necessário, diagnósticos poderão utilizar sinais específicos para confirmar hipóteses de falhas.

---

# Integração com o System Check

Alguns itens do checklist poderão utilizar sinais automáticos para validar entradas, saídas e roteamentos.

---

# Integração com o Maintenance Report

O relatório técnico poderá registrar:

- sinais utilizados;
- parâmetros aplicados;
- duração dos testes;
- resultados obtidos.

---

# Integração com o Histórico

Todas as utilizações poderão ser armazenadas para:

- auditoria;
- repetição de testes;
- comparação entre manutenções;
- documentação técnica.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- sinal atual;
- frequência;
- nível;
- destino;
- tempo restante;
- estado do gerador.

---

# Benefícios

O Signal Generator proporciona:

- testes padronizados;
- calibração mais precisa;
- redução do tempo de manutenção;
- maior confiabilidade dos diagnósticos;
- integração com os demais componentes técnicos;
- documentação automática das medições realizadas.

---

# Separação de Responsabilidades

O Signal Generator não:

- interpreta resultados dos testes;
- executa diagnósticos;
- monitora continuamente o sistema;
- realiza calibrações automaticamente;
- altera configurações da mesa além da geração controlada dos sinais.

Sua responsabilidade é fornecer sinais de referência confiáveis e configuráveis para apoiar testes, diagnósticos e calibrações durante a manutenção do sistema de áudio.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- geração de sinais multicanal;
- sequências automáticas de testes;
- integração com analisadores RTA;
- calibração assistida por microfone de medição;
- geração sincronizada para múltiplas saídas;
- biblioteca de sinais personalizados;
- controle remoto por dispositivos móveis;
- integração com protocolos de medição acústica.

---

# Relação com Outros Componentes

O Signal Generator trabalha diretamente com:

- Modo Técnico;
- Maintenance Manager;
- Channel Tester;
- Diagnostic Engine;
- System Check;
- Calibration Manager;
- Health Monitor;
- Maintenance Report;
- Recommendation Engine;
- Dashboard Operacional.

Ele representa a fonte de sinais de referência do Modo Técnico, fornecendo os recursos necessários para testes, diagnósticos e calibrações precisas, garantindo que toda a infraestrutura de áudio possa ser validada de forma segura, padronizada e confiável.

---

# Situação da Sprint

**Status:** ✅ Concluída