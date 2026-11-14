# Audio Copilot

## Visão Geral

O Audio Copilot é uma plataforma inteligente desenvolvida para auxiliar operadores de áudio durante todas as etapas da operação de eventos ao vivo.

O sistema combina planejamento técnico, monitoramento em tempo real, automação e Inteligência Artificial para reduzir erros operacionais, aumentar a organização da equipe e oferecer maior segurança durante cultos, ensaios e eventos.

Embora o projeto tenha sido concebido inicialmente utilizando a mesa digital Soundcraft Ui24R da Igreja Presbiteriana de Piracicaba como ambiente de desenvolvimento e validação, sua arquitetura foi planejada para evoluir futuramente para outras mesas digitais e diferentes cenários de sonorização.

---

# Missão

Auxiliar operadores de áudio na preparação, operação e monitoramento de eventos, permitindo que concentrem sua atenção na qualidade da operação enquanto o Audio Copilot supervisiona continuamente os aspectos técnicos do sistema.

---

# Filosofia do Projeto

O Audio Copilot atua como um copiloto inteligente.

A Inteligência Artificial monitora continuamente o sistema, identifica possíveis problemas e apresenta recomendações em tempo real.

O operador permanece sempre com a decisão final, podendo aceitar, ignorar ou executar manualmente qualquer ação sugerida pelo sistema.

O objetivo não é substituir o operador de áudio, mas ampliar sua capacidade de planejamento, organização e tomada de decisão.

---

# Filosofia Operacional

O Audio Copilot diferencia dois conceitos fundamentais.

## Programação Litúrgica

Define a condução do culto.

Essa programação pertence à igreja e pode sofrer alterações antes ou durante o evento.

Exemplos:

- quem fará a oração;
- quem fará a leitura bíblica;
- quem conduzirá os avisos;
- alterações realizadas pelo dirigente durante o culto.

Essas informações normalmente não são conhecidas antecipadamente e não fazem parte da responsabilidade do operador de áudio.

---

## Programação Técnica

Define apenas os recursos necessários para cada etapa do evento.

Essa programação pertence ao operador de áudio.

Seu objetivo é garantir que todos os recursos técnicos estejam preparados independentemente de quem participará daquele momento.

Exemplos:

- microfone do púlpito;
- microfone sem fio;
- banda;
- piano;
- reprodução de MP3;
- cenas;
- presets;
- retornos.

Essa separação torna o sistema muito mais flexível, permitindo que alterações na liturgia não comprometam a preparação técnica do evento.

---

# Fluxo Operacional

O Audio Copilot acompanha todas as etapas da operação.

```text
Planejamento
        │
        ▼
Programação Técnica
        │
        ▼
Ensaio
        │
        ▼
Operação ao Vivo
        │
        ▼
Monitoramento da IA
        │
        ▼
Relatório Pós-Evento
        │
        ▼
Melhoria Contínua
```

---

# Objetivos

## Curto Prazo

- Comunicação completa com a Soundcraft Ui24R;
- Leitura de todos os canais;
- Monitoramento de EQ;
- Monitoramento de Compressor;
- Monitoramento de Gate;
- Monitoramento de Auxiliares;
- Monitoramento de FX;
- Gerenciamento de Presets;
- Gerenciamento de Cenas;
- Gerenciamento de Programações Técnicas.

---

## Médio Prazo

- Configuração automática de canais;
- Aplicação inteligente de presets;
- Sugestões automáticas de equalização;
- Detecção de clipping;
- Detecção de excesso de ganho;
- Detecção de feedback (microfonia);
- Detecção de canais desconectados;
- Validação da programação técnica;
- Assistente durante ensaios.

---

## Longo Prazo

Criar um operador virtual inteligente capaz de acompanhar todo o evento em tempo real.

A Inteligência Artificial deverá ser capaz de:

- monitorar o ambiente;
- monitorar o equilíbrio da banda;
- monitorar inteligibilidade da voz;
- identificar microfonia;
- acompanhar níveis de áudio;
- detectar problemas operacionais;
- sugerir correções;
- aplicar correções automaticamente quando autorizado pelo operador;
- gerar relatórios completos de desempenho do evento.

---

# Funcionalidades Previstas

- Cadastro de Pessoas;
- Cadastro de Instrumentos;
- Cadastro de Microfones;
- Cadastro de Presets;
- Cadastro de Cenas;
- Cadastro de Programações Técnicas;
- Controle de Ensaios;
- Checklist Pré-Evento;
- Operação ao Vivo;
- Monitoramento Inteligente;
- Relatórios Pós-Evento;
- Inteligência Artificial.

---

# Equipamentos Utilizados no Desenvolvimento

## Mesa Digital

- Soundcraft Ui24R

## PA

- 2 Line Arrays Donner

## Subwoofers

- 2 Subwoofers Donner

## Monitores

- 2 Monitores de palco

## Instrumentos

- Violão Martin Road Series
- Violão da igreja
- Baixo da igreja
- Cajón
- Piano

## Microfones

- Microfone do púlpito
- Microfone sem fio

## Vocais

- 2 vozes masculinas
- 3 vozes femininas

---

# Arquitetura do Projeto

O Audio Copilot foi projetado utilizando arquitetura modular.

Cada módulo possui responsabilidade específica, permitindo futuras integrações com diferentes fabricantes de mesas digitais e novos recursos de Inteligência Artificial.

A arquitetura prevê expansão para:

- outras mesas digitais;
- novos protocolos de comunicação;
- monitoramento remoto;
- operação distribuída;
- múltiplas igrejas;
- empresas de sonorização.

---

# Tecnologias

- Python
- JSON
- Soundcraft Ui24R API
- Inteligência Artificial
- Interface Desktop (planejada)

---

# Nome do Projeto

**Audio Copilot**

**Seu assistente inteligente de áudio.**

---

# Situação do Projeto

**Status:** 🚧 Em desenvolvimento

Fases concluídas:

- ✅ Fase 1 — Fundação
- ✅ Fase 2 — Modelagem
- ✅ Fase 3 — Programação Técnica
- 🚧 Fase 4 — UX e Design

---

# Versão

**0.1.0**