# Sprint E10 – Channel Tester

## Objetivo

Definir o componente responsável por testar individualmente cada canal da mesa de som, verificando sua configuração, processamento, roteamento e funcionamento operacional.

O **Channel Tester** permite validar rapidamente entradas, saídas, processamento de áudio e demais recursos associados a um canal específico, auxiliando na identificação de problemas antes que afetem ensaios ou cultos.

Enquanto o **System Check** verifica o sistema como um todo e o **Diagnostic Engine** investiga possíveis falhas, o Channel Tester concentra-se na análise detalhada de cada canal.

---

# Visão Geral

Grande parte dos problemas em uma mesa de som está relacionada a canais específicos.

Exemplos:

- microfone sem sinal;
- cabo defeituoso;
- ganho incorreto;
- phantom desligado;
- compressor mal configurado;
- gate excessivamente fechado;
- canal mutado;
- roteamento incorreto;
- envio auxiliar ausente.

O Channel Tester reúne todas essas verificações em um único componente.

---

# Filosofia

O Channel Tester foi desenvolvido seguindo cinco princípios.

## Precisão

Cada canal deve ser analisado individualmente.

---

## Rapidez

Os testes devem ser executados em poucos segundos.

---

## Segurança

Nenhum teste deve comprometer a operação da mesa.

---

## Repetibilidade

Os resultados devem ser consistentes independentemente do operador.

---

## Diagnóstico

Cada falha deve ser apresentada de forma clara e objetiva.

---

# Arquitetura

```text
Maintenance Manager

↓

Channel Tester

├── Entrada
├── Processamento
├── Roteamento
├── Auxiliares
├── Saídas
├── Validação
└── Resultado
```

---

# Responsabilidades

O Channel Tester será responsável por:

- testar canais individuais;
- validar entradas de áudio;
- verificar processamento;
- conferir roteamentos;
- analisar envios auxiliares;
- registrar resultados dos testes.

---

# Fluxo Geral

```text
Selecionar Canal

↓

Executar Testes

↓

Analisar Configuração

↓

Validar Resultado

↓

Registrar Sessão
```

---

# Seleção do Canal

O operador poderá selecionar:

- canal de entrada;
- canal estéreo;
- retorno USB;
- canal virtual;
- auxiliar;
- saída principal.

Cada tipo poderá possuir testes específicos.

---

# Teste de Entrada

O componente poderá verificar:

- presença de sinal;
- nível de entrada;
- clipping;
- ruído;
- silêncio;
- estabilidade do sinal.

Exemplo:

```text
Canal 05

↓

Sinal Detectado

↓

Teste Aprovado
```

---

# Teste de Ganho

O sistema poderá avaliar:

- ganho atual;
- headroom disponível;
- saturação;
- margem operacional.

Exemplo:

```text
Gain

↓

Muito alto

↓

Reduzir 4 dB
```

---

# Teste de Phantom Power

Quando aplicável, será possível verificar:

- phantom ativado;
- phantom desativado;
- alimentação estável;
- compatibilidade com o equipamento conectado.

---

# Teste de Polaridade

O componente poderá identificar:

- polaridade invertida;
- fase incompatível;
- possíveis cancelamentos de fase.

---

# Teste do Equalizador

O sistema poderá validar:

- filtros HPF;
- filtros LPF;
- bandas paramétricas;
- ganho excessivo;
- cortes extremos.

---

# Teste do Compressor

Serão avaliados parâmetros como:

- Threshold;
- Ratio;
- Attack;
- Release;
- Makeup Gain.

Também poderão ser identificadas configurações incompatíveis.

---

# Teste do Gate

O Channel Tester poderá verificar:

- Threshold;
- Attack;
- Hold;
- Release;
- fechamento excessivo;
- abertura incorreta.

---

# Teste dos Auxiliares

O componente poderá analisar:

- envios ativos;
- níveis;
- pré/pós-fader;
- roteamento para monitores;
- retornos.

---

# Teste do Pan

Também poderá ser validado:

- posição estéreo;
- centralização;
- distribuição entre os canais LR.

---

# Teste do Mute

Será possível identificar:

- canal mutado;
- mute acidental;
- mute programado.

---

# Teste do Roteamento

O componente poderá verificar:

- envio ao Main LR;
- grupos;
- DCAs;
- auxiliares;
- matrix;
- gravação.

Exemplo:

```text
Canal 08

↓

Sem envio ao Main LR
```

---

# Teste de Processamento Completo

O operador poderá executar uma verificação completa.

Fluxo:

```text
Entrada

↓

Gain

↓

EQ

↓

Compressor

↓

Gate

↓

Auxiliares

↓

Pan

↓

Saídas

↓

Resultado
```

---

# Resultado do Teste

Cada teste poderá retornar:

```text
Aprovado

↓

Aprovado com ressalvas

↓

Reprovado
```

Também poderão ser exibidas recomendações.

---

# Registro

Cada execução armazenará:

- canal testado;
- operador;
- horário;
- parâmetros avaliados;
- resultado;
- observações.

---

# Integração com o Signal Generator

Quando necessário, o Channel Tester poderá solicitar sinais de teste.

Exemplo:

```text
Teste

↓

Signal Generator

↓

Pink Noise

↓

Canal 07
```

---

# Integração com o Diagnostic Engine

Caso uma falha seja identificada, o Diagnostic Engine poderá realizar uma investigação mais profunda.

---

# Integração com o Calibration Manager

Após um teste bem-sucedido, o operador poderá iniciar imediatamente a calibração do canal.

---

# Integração com o Maintenance Report

Todos os testes executados poderão ser incorporados ao relatório técnico da sessão.

---

# Integração com o Histórico

Os resultados poderão ser armazenados para:

- auditoria;
- comparação entre manutenções;
- identificação de falhas recorrentes;
- acompanhamento da evolução do sistema.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- canal em teste;
- progresso da análise;
- resultado;
- falhas encontradas;
- recomendações.

---

# Benefícios

O Channel Tester proporciona:

- testes rápidos e padronizados;
- identificação precisa de falhas;
- redução do tempo de manutenção;
- validação completa dos canais;
- documentação automática;
- maior confiabilidade operacional.

---

# Separação de Responsabilidades

O Channel Tester não:

- monitora continuamente todos os canais;
- executa checklists completos;
- realiza diagnósticos globais da mesa;
- gera relatórios finais da manutenção;
- altera automaticamente as configurações do canal.

Sua responsabilidade é executar testes detalhados em canais individuais, validando sua configuração e funcionamento antes da utilização em ensaios ou cultos.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- testes automáticos em lote;
- comparação entre canais;
- perfis de teste por tipo de equipamento;
- validação automática conforme o instrumento conectado;
- análise espectral do sinal;
- integração com analisadores externos;
- reconhecimento automático de microfones e DIs;
- testes remotos via rede.

---

# Relação com Outros Componentes

O Channel Tester trabalha diretamente com:

- Modo Técnico;
- Maintenance Manager;
- Diagnostic Engine;
- System Check;
- Signal Generator;
- Calibration Manager;
- Health Monitor;
- Maintenance Report;
- Telemetry Manager;
- Recommendation Engine;
- Dashboard Operacional.

Ele representa a ferramenta especializada para validação individual dos canais da mesa de som, permitindo identificar rapidamente falhas de configuração, processamento e roteamento, contribuindo para uma operação mais segura, confiável e padronizada.

---

# Situação da Sprint

**Status:** ✅ Concluída