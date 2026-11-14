# Sprint E10 – Calibration Manager

## Objetivo

Definir o componente responsável por auxiliar o operador na calibração da mesa de som e do sistema de áudio, garantindo níveis adequados, headroom consistente, resposta equilibrada e configurações padronizadas para cada ambiente de operação.

O **Calibration Manager** atua como o coordenador dos processos de calibração do Audio Copilot, orientando o operador durante ajustes técnicos e validando se os parâmetros configurados atendem às boas práticas de engenharia de áudio.

Enquanto o **Signal Generator** produz sinais de referência e o **Channel Tester** valida canais individuais, o Calibration Manager organiza todo o processo de calibração.

---

# Visão Geral

Uma boa calibração reduz problemas durante ensaios e cultos.

Exemplos:

- ganhos excessivos;
- headroom insuficiente;
- retornos desequilibrados;
- volumes inconsistentes;
- clipping frequente;
- diferenças entre snapshots.

O Calibration Manager conduz esses ajustes de forma organizada e documentada.

---

# Filosofia

O Calibration Manager foi desenvolvido seguindo cinco princípios.

## Precisão

Os ajustes devem produzir resultados consistentes.

---

## Padronização

Todas as calibrações devem seguir um procedimento bem definido.

---

## Segurança

Nenhuma calibração deve colocar em risco equipamentos ou pessoas.

---

## Assistência

A IA orienta o operador, mas a decisão final permanece sob sua responsabilidade.

---

## Rastreabilidade

Toda calibração deve ficar registrada para futuras consultas.

---

# Arquitetura

```text
Maintenance Manager

↓

Calibration Manager

├── Planejamento
├── Assistente
├── Validação
├── Comparação
├── Registro
└── Relatórios
```

---

# Responsabilidades

O Calibration Manager será responsável por:

- coordenar calibrações;
- orientar o operador;
- validar níveis;
- acompanhar o progresso;
- registrar alterações;
- armazenar resultados.

---

# Fluxo Geral

```text
Selecionar Tipo

↓

Preparar Sistema

↓

Executar Calibração

↓

Validar Resultado

↓

Registrar Sessão
```

---

# Tipos de Calibração

O sistema poderá auxiliar na calibração de:

- canais individuais;
- grupos;
- Main LR;
- auxiliares;
- monitores;
- matrizes;
- efeitos;
- sistema completo.

---

# Calibração de Ganho

O componente poderá orientar ajustes de:

- ganho de entrada;
- headroom;
- margem dinâmica;
- nível nominal.

Exemplo:

```text
Canal 07

↓

Headroom baixo

↓

Reduzir Gain em 3 dB
```

---

# Calibração de Equalização

Será possível auxiliar na configuração de:

- HPF;
- LPF;
- equalização paramétrica;
- filtros corretivos;
- resposta tonal.

O sistema poderá sugerir ajustes, mas nunca aplicá-los automaticamente.

---

# Calibração de Compressão

O Calibration Manager poderá orientar parâmetros como:

- Threshold;
- Ratio;
- Attack;
- Release;
- Makeup Gain.

Também poderá alertar sobre configurações extremas.

---

# Calibração do Gate

Serão avaliados:

- Threshold;
- Attack;
- Hold;
- Release.

O objetivo é evitar cortes indesejados do áudio.

---

# Calibração dos Auxiliares

O componente poderá orientar:

- níveis de envio;
- pré/pós-fader;
- equilíbrio entre músicos;
- consistência dos retornos.

---

# Calibração dos Efeitos

Também poderão ser ajustados:

- reverbs;
- delays;
- retornos de efeitos;
- níveis de envio;
- mistura entre efeito e sinal direto.

---

# Comparação de Configurações

O operador poderá comparar:

- antes e depois da calibração;
- diferentes snapshots;
- configurações entre eventos;
- canais semelhantes.

Exemplo:

```text
Snapshot Atual

↓

Snapshot Referência

↓

Diferenças Encontradas
```

---

# Validação

Após cada calibração o sistema poderá verificar:

- clipping;
- headroom;
- estabilidade;
- equilíbrio;
- conformidade com o perfil selecionado.

---

# Perfis de Calibração

O sistema poderá disponibilizar perfis como:

- Culto;
- Ensaio;
- Conferência;
- Voz Falada;
- Banda Completa;
- Evento Especial.

Cada perfil poderá utilizar critérios específicos.

---

# Assistência Inteligente

Durante a calibração o Audio Copilot poderá fornecer orientações.

Exemplo:

```text
Canal 03

↓

Compressor muito agressivo

↓

Reduzir Ratio
```

---

# Registro

Cada calibração poderá armazenar:

- operador;
- data;
- horário;
- canais envolvidos;
- parâmetros alterados;
- observações;
- resultado final.

---

# Integração com o Signal Generator

O Calibration Manager poderá utilizar sinais de teste durante todo o processo.

Fluxo:

```text
Calibration Manager

↓

Signal Generator

↓

Pink Noise

↓

Calibração
```

---

# Integração com o Channel Tester

Após cada ajuste, o Channel Tester poderá validar automaticamente o canal calibrado.

---

# Integração com o Diagnostic Engine

Caso uma calibração apresente resultados inesperados, o Diagnostic Engine poderá investigar possíveis causas.

---

# Integração com o Health Monitor

Durante a calibração o estado geral da mesa poderá ser monitorado para identificar comportamentos anormais.

---

# Integração com o Maintenance Report

Todas as calibrações executadas poderão ser incluídas no relatório técnico.

Serão registrados:

- parâmetros ajustados;
- recomendações;
- observações;
- resultados.

---

# Integração com o Histórico

Cada sessão de calibração poderá ser armazenada para:

- comparação histórica;
- auditoria;
- evolução da configuração;
- recuperação de parâmetros anteriores.

---

# Integração com o Dashboard

O Dashboard poderá apresentar:

- etapa atual da calibração;
- progresso;
- parâmetros ajustados;
- recomendações da IA;
- validações concluídas.

---

# Benefícios

O Calibration Manager proporciona:

- calibrações padronizadas;
- maior estabilidade da mixagem;
- redução de clipping;
- melhor aproveitamento do headroom;
- documentação completa dos ajustes;
- maior confiabilidade da operação.

---

# Separação de Responsabilidades

O Calibration Manager não:

- gera sinais de teste;
- executa diagnósticos completos;
- monitora continuamente a operação do culto;
- altera automaticamente todas as configurações da mesa;
- substitui a decisão do operador.

Sua responsabilidade é orientar, organizar e validar os processos de calibração do sistema de áudio, garantindo ajustes consistentes, seguros e devidamente registrados.

---

# Evoluções Futuras

O componente foi projetado para incorporar funcionalidades como:

- calibração assistida por microfone de medição;
- equalização automática baseada em RTA;
- comparação inteligente entre ambientes;
- calibração colaborativa entre operadores;
- perfis personalizados por igreja;
- calibração remota;
- aprendizado automático das preferências da equipe técnica;
- recomendações adaptativas baseadas no histórico de eventos.

---

# Relação com Outros Componentes

O Calibration Manager trabalha diretamente com:

- Modo Técnico;
- Maintenance Manager;
- Signal Generator;
- Channel Tester;
- Diagnostic Engine;
- System Check;
- Health Monitor;
- Maintenance Report;
- Recommendation Engine;
- Learning Engine;
- History Manager;
- Dashboard Operacional.

Ele representa o coordenador dos processos de calibração do Modo Técnico, auxiliando o operador na obtenção de uma configuração equilibrada, consistente e segura para toda a infraestrutura de áudio, preservando um histórico completo das alterações realizadas.

---

# Situação da Sprint

**Status:** ✅ Concluída