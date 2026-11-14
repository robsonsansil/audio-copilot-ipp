# Audio Copilot IPP

## Roadmap

Versão: 2.1

---

# Missão

Desenvolver um assistente inteligente para operação de áudio em igrejas, capaz de auxiliar o operador antes, durante e após cada programação, reduzindo erros humanos, automatizando tarefas repetitivas e monitorando continuamente a qualidade do áudio.

O operador sempre permanece no controle da mesa de som.

---

# Visão do Produto

O Audio Copilot será um copiloto inteligente para operação de áudio em igrejas.

Seu objetivo é compreender toda a programação, desde o planejamento do culto até sua execução, auxiliando o operador por meio de automações, monitoramento contínuo e inteligência artificial, mantendo sempre o operador como responsável pela decisão final.

O sistema deverá conhecer a igreja, seus equipamentos, participantes, liturgia e forma de trabalho, tornando a preparação e a operação dos eventos mais rápidas, seguras e consistentes.

---

# Princípios do Projeto

1. O operador sempre possui a decisão final.
2. A IA nunca substitui o operador.
3. Toda automação poderá ser ativada ou desativada.
4. Toda ação da IA deverá ser explicável.
5. O sistema deverá ser simples para qualquer operador utilizar.
6. O Audio Copilot será desenvolvido inicialmente para a Igreja Presbiteriana de Piracicaba.
7. Toda a arquitetura deverá permitir expansão para outras igrejas e outras mesas de som.

---

# Escopo Inicial

Primeira igreja suportada
- Igreja Presbiteriana de Piracicaba

Primeira mesa de som
- Soundcraft Ui24R

Primeira plataforma
- Windows

Primeiros usuários
- Equipe de Som da IPP

Primeiro objetivo
- Automatizar e auxiliar toda a operação da Soundcraft Ui24R durante ensaios, cultos e demais programações da igreja.

---

# Modos de Operação

- Manual (IA desligada)
- Assistido (IA apenas sugere)
- Semiautomático (IA executa ações autorizadas)
- Automático (IA controla toda a operação)
- Treinamento (IA aprende com o operador)

---

# Fase 1 - Fundação

Status: ✅ Concluída

Objetivo:
Criar toda a base técnica do projeto.

- [x] Sprint A01 - Configuração do ambiente
- [x] Sprint A02 - Estrutura inicial do projeto
- [x] Sprint A03 - Cliente inicial da Ui24R
- [x] Sprint A04 - Model Channel
- [x] Sprint A05 - Model Profile
- [x] Sprint A06 - Model Preset
- [x] Sprint A07 - Model Event
- [x] Sprint A08 - Persistência em JSON

---

# Fase 2 - Cadastro da Igreja

Status: ✅ Concluída

Objetivo:
Cadastrar todos os recursos permanentes da igreja.

- [x] Sprint B01 - Cadastro de Pessoas
- [x] Sprint B02 - Cadastro de Instrumentistas
- [x] Sprint B03 - Cadastro de Vocalistas
- [x] Sprint B04 - Cadastro de Pregadores
- [x] Sprint B05 - Cadastro de Professores da EBD
- [x] Sprint B06 - Cadastro de Instrumentos
- [x] Sprint B07 - Cadastro de Microfones
- [x] Sprint B08 - Cadastro de Retornos
- [x] Sprint B09 - Cadastro de Perfis
- [x] Sprint B10 - Cadastro de Presets
- [x] Sprint B11 - Cadastro da Mesa de Som
- [x] Sprint B12 - Cadastro dos Canais da Mesa
- [x] Sprint B13 - Cadastro de Equipamentos Extras
- [x] Sprint B14 - Cadastro de Cenas Padrão

---

# Fase 3 - Cadastro de Recursos

Status: ✅ Concluída

Objetivo:
Construir a base de dados permanente do Audio Copilot, cadastrando todas as pessoas, instrumentos, microfones, equipamentos, recursos do templo e canais disponíveis. Essas informações servirão como base para a configuração dos eventos, associação de recursos, aplicação de presets, operação da mesa de som, geração de relatórios e funcionamento da Inteligência Artificial.

- [x] Sprint C01 – Cadastro de Pessoas
- [x] Sprint C02 – Cadastro de Vocais
- [x] Sprint C03 – Cadastro de Instrumentistas
- [x] Sprint C04 – Cadastro de Instrumentos
- [x] Sprint C05 – Cadastro de Microfones
- [x] Sprint C06 – Cadastro de Equipamentos
- [x] Sprint C07 – Cadastro de Recursos do Templo
- [x] Sprint C08 – Cadastro de Canais
- [x] Sprint C09 – Biblioteca Geral

---

# Fase 4 - Planejamento das Programações

Status: ✅ Concluída

Objetivo:
Planejar toda a programação do evento, definindo participantes, liturgia, recursos de áudio e configurações que serão utilizadas durante o ensaio e o culto.

- [x] Sprint D01 - Cadastro de Programações
- [x] Sprint D02 - Cadastro de Eventos
- [x] Sprint D03 - Cadastro da Liturgia
- [x] Sprint D04 - Cadastro das Etapas da Liturgia
- [x] Sprint D05 - Seleção dos Participantes
- [x] Sprint D06 - Seleção da Banda
- [x] Sprint D07 - Seleção dos Instrumentos
- [x] Sprint D08 - Seleção dos Microfones
- [x] Sprint D09 - Seleção dos Retornos
- [x] Sprint D10 - Cadastro do Ensaio
- [x] Sprint D11 - Reutilização da Configuração do Ensaio
- [x] Sprint D12 - Checklist Pré-Culto

---

# Fase 5 - UX e Design

Status: ✅ Concluída

Objetivo:
Projetar toda a experiência de utilização do Audio Copilot, definindo a identidade visual, os fluxos operacionais, a interação entre operador e Inteligência Artificial, os protótipos das interfaces, os padrões de usabilidade e o Design System que servirão de base para toda a implementação do sistema.

- [x] Sprint E01 - Identidade Visual
- [x] Sprint E02 - Logo do Audio Copilot
- [x] Sprint E03 - Paleta de Cores
- [x] Sprint E04 - Protótipo da Tela Principal
- [x] Sprint E05 – Protótipo da Programação Técnica
- [x] Sprint E06 – Protótipo da Configuração do Evento
- [x] Sprint E07 – Protótipo da Preparação do Evento
- [x] Sprint E08 - Protótipo do Console de Operação
- [x] Sprint E09 - Protótipo do Painel da IA
- [x] Sprint E10 - Protótipo Mobile
- [x] Sprint E11 - Testes de Usabilidade
- [x] Sprint E12 - Design System
- [x] Sprint E13 - Protótipo do Sistema de Gravação e Replay
- [x] Sprint E14 - Protótipo do Cadastro de Recursos

---

# Fase 6 - Console Inteligente

Status: ✅ Concluída

Objetivo:
Criar a principal interface de operação do Audio Copilot.

- [x] Sprint F01 - Arquitetura do Console Inteligente
- [x] Sprint F02 - Dashboard Operacional
- [x] Sprint F03 - Medidores em Tempo Real
- [x] Sprint F04 - Painel da Liturgia
- [x] Sprint F05 - Motor de Inteligência Operacional
- [x] Sprint F06 - Histórico de Alterações
- [x] Sprint F07 - Destaque Visual das Alterações da IA
- [x] Sprint F08 - Modo Ensaio
- [x] Sprint F09 - Modo Culto
- [x] Sprint F10 - Modo Técnico

---

# Fase 7 - Captura e Gerenciamento de Áudio

Status: ✅ Concluída

Objetivo:
Implementar o subsistema responsável pela captura, reprodução, gerenciamento e análise de gravações de áudio, integrando-as aos eventos do Audio Copilot para apoiar ensaios, cultos, manutenção, aprendizado da IA e documentação técnica.

- [x] Sprint G01 - Sistema de Gravação
- [x] Sprint G02 - Sessão de Gravação
- [x] Sprint G03 - Gerenciamento de Buffer
- [x] Sprint G04 - Marcadores
- [x] Sprint G05 - Reprodução Inteligente
- [x] Sprint G06 - Exportação
- [x] Sprint G07 - Biblioteca de Áudios
- [x] Sprint G08 - Integração com IA
- [x] Sprint G09 - Comparação de Gravações
- [x] Sprint G10 - Relatórios de Áudio

---

# Fase 8 - Motor do Audio Copilot

Status: ✅ Concluída

Objetivo:

Construir toda a lógica interna do sistema, independente da mesa de som.

- [x] Sprint H01 - Gerenciador de Eventos
- [x] Sprint H02 - Gerenciador de Programações
- [x] Sprint H03 - Gerenciador de Liturgia
- [x] Sprint H04 - Gerenciador de Cenas
- [x] Sprint H05 - Motor de Regras
- [x] Sprint H06 - Motor de Alertas
- [x] Sprint H07 - Gerenciador de Estado da Operação
- [x] Sprint H08 - Sistema de Logs
- [x] Sprint H09 - Scheduler de Eventos
- [x] Sprint H10 - API Interna

---

# Fase 9 - Engenharia Reversa do Protocolo Ui24R

Status: ⏳ Planejada

Objetivo:
Documentar completamente o protocolo de comunicação da Soundcraft Ui24R, identificando comandos, eventos, parâmetros e mensagens trocadas entre a interface web e a mesa de som. O conhecimento obtido servirá como base técnica para a implementação, testes, manutenção e futuras integrações do Audio Copilot.


- [ ] Sprint I01 - Inicialização da Ui24R
- [ ] Sprint I02 - Carregamento da interface web
- [ ] Sprint I03 - Reconexão da interface
- [ ] Sprint I04 - Fader de um canal
- [ ] Sprint I05 - Mute / Unmute
- [ ] Sprint I06 - Gain
- [ ] Sprint I07 - Pan
- [ ] Sprint I08 - EQ
- [ ] Sprint I09 - Compressor
- [ ] Sprint I10 - Gate
- [ ] Sprint I11 - Auxiliares
- [ ] Sprint I12 - FX
- [ ] Sprint I13 - Cenas
- [ ] Sprint I14 - Presets
- [ ] Sprint I15 - RTA e medidores
- [ ] Sprint I16 - Configurações Gerais
- [ ] Sprint I17 - Sincronização entre Navegadores
- [ ] Sprint I18 - Reconexão
- [ ] Sprint I19 - Medidores em Tempo Real
- [ ] Sprint I20 - Alterações Externas

---

# Fase 10 - Operação ao Vivo

Status: ⏳ Planejada

Objetivo:
Auxiliar o operador durante toda a programação.

- [ ] Sprint J01 - Navegação pela Liturgia
- [ ] Sprint J02 - Aplicação Automática de Cenas
- [ ] Sprint J03 - Controle Inteligente dos Microfones
- [ ] Sprint J04 - Controle Inteligente dos Instrumentos
- [ ] Sprint J05 - Controle dos Retornos
- [ ] Sprint J06 - Sugestão de Mudança de Cena
- [ ] Sprint J07 - Alertas Operacionais
- [ ] Sprint J08 - Registro das Alterações
- [ ] Sprint J09 - Histórico em Tempo Real
- [ ] Sprint J10 - Botão "Assumir Controle Manual"

---

# Fase 11 - IA Operacional

Status: 💡 Futuro

Objetivo:
Auxiliar o operador na condução da programação.

- [ ] Sprint K01 - Sugestão Automática de Presets
- [ ] Sprint K02 - Sugestão de Cenas
- [ ] Sprint K03 - Acompanhamento da Liturgia
- [ ] Sprint K04 - Lembretes Inteligentes
- [ ] Sprint K05 - Identificação de Problemas
- [ ] Sprint K06 - Aprendizado Baseado no Histórico
- [ ] Sprint K07 - Recomendações Durante o Evento
- [ ] Sprint K08 - IA Explicável
- [ ] Sprint K09 - Modos da IA

---

# Fase 12 - IA de Engenharia de Áudio

Status: 💡 Futuro

Objetivo:
Monitorar continuamente a qualidade do áudio e auxiliar tecnicamente a operação.

- [ ] Sprint L01 - Detector Inteligente de Microfonia
- [ ] Sprint L02 - Correção Automática de Microfonia
- [ ] Sprint L03 - Auto Gain Inteligente
- [ ] Sprint L04 - Auto EQ Inteligente
- [ ] Sprint L05 - Balanceamento Automático da Banda
- [ ] Sprint L06 - Detector de Plosivas (P/B)
- [ ] Sprint L07 - Detector de Clipping
- [ ] Sprint L08 - Detector de Cabos Defeituosos
- [ ] Sprint L09 - Detector de Mau Contato
- [ ] Sprint L10 - Detector de Ausência de Sinal
- [ ] Sprint L11 - Monitor de Saúde da Mesa
- [ ] Sprint L12 - Sugestões Automáticas de Correção

---

# Fase 13 - Gestão e Relatórios

Status: 💡 Futuro

Objetivo:
Registrar todo o histórico da operação.

- [ ] Sprint M01 - Histórico de Eventos
- [ ] Sprint M02 - Histórico de Programações
- [ ] Sprint M03 - Histórico de Configurações
- [ ] Sprint M04 - Histórico das Alterações
- [ ] Sprint M05 - Relatórios PDF
- [ ] Sprint M06 - Estatísticas
- [ ] Sprint M07 - Exportação de Dados
- [ ] Sprint M08 - Relatório Inteligente Pós-Culto

---

# Fase 14 - Plataforma Mobile

Status: 💡 Futuro

Objetivo:
Permitir operação remota pelo celular.

- [ ] Sprint N01 - Servidor Local
- [ ] Sprint N02 - API REST
- [ ] Sprint N03 - Aplicativo Android
- [ ] Sprint N04 - Aplicativo iPhone/iPad
- [ ] Sprint N05 - Dashboard Mobile
- [ ] Sprint N06 - Notificações Push

---

# Fase 15 - Expansão

Status: 💡 Futuro

Objetivo:
Expandir o Audio Copilot para outras igrejas e plataformas.

- [ ] Sprint O01 - Multi-Igrejas
- [ ] Sprint O02 - Multi-Mesas de Som
- [ ] Sprint O03 - Dashboard Web
- [ ] Sprint O04 - Compartilhamento de Presets
- [ ] Sprint O05 - Backup em Nuvem
- [ ] Sprint O06 - Controle por Voz
- [ ] Sprint O07 - Integração com OBS Studio
- [ ] Sprint O08 - Integração com ProPresenter
- [ ] Sprint O09 - Integração com Sistemas de Iluminação
- [ ] Sprint O10 - API Pública

---

# Ideias Futuras

- Multi-igrejas
- Multi-mesas de som
- Aplicativo Android
- Aplicativo iOS
- Controle por voz
- Integração com OBS
- Integração com ProPresenter
- Integração com sistemas de iluminação
- Backup automático na nuvem

---

# Histórico

## v0.1.0

- Criação do projeto
- Estrutura inicial
- Primeiro Model (Channel)


# Fluxo de Operação

Durante a Semana
- Cadastro da programação.
- Cadastro da liturgia.
- Escala da banda.
- Escala dos participantes.
- Seleção dos instrumentos.
- Seleção dos microfones.
- Seleção dos retornos.

Ensaio
- Aplicação automática da configuração.
- Ajustes finos realizados pelo operador.
- Aprendizado da IA com os ajustes.
- Salvamento da configuração do ensaio.

Antes do Culto
- Reutilizar a configuração do ensaio.
- Confirmar participantes.
- Confirmar pregador.
- Confirmar banda.
- Confirmar instrumentos.
- Confirmar microfones.

Durante o Culto
- A IA acompanha toda a liturgia e auxilia o operador.

Exemplos:
- lembrar de abrir o microfone sem fio para perguntas ou orações;
- sugerir mutar a banda após o último cântico;
- lembrar de reabrir a banda para o hino final;
- aplicar cenas automaticamente;
- monitorar clipping;
- monitorar riscos de microfonia;
- ajustar níveis de voz quando autorizado;
- monitorar ruídos e falhas;
- detectar cabos e conectores com problemas;
- registrar todas as alterações realizadas.

Após o Culto
- Gerar relatório.
- Salvar histórico.
- Atualizar estatísticas.
- Registrar sugestões para o próximo evento.
- Alimentar o aprendizado da IA.

---

# Ciclo de Operação

Planejamento
↓
Ensaio
↓
Aprendizado da IA
↓
Culto
↓
Monitoramento
↓
Relatório
↓
Aprendizado para o próximo evento

---

# Objetivo Final

O Audio Copilot deverá ser capaz de:

- Planejar uma programação completa.
- Auxiliar durante o ensaio.
- Configurar automaticamente a mesa.
- Acompanhar a liturgia em tempo real.
- Monitorar continuamente a qualidade do áudio.
- Explicar todas as ações realizadas pela IA.
- Permitir que o operador assuma o controle a qualquer momento.
- Aprender continuamente com a equipe de áudio.
- Tornar a operação mais segura, eficiente e consistente.

---

# Visão de Longo Prazo

O Audio Copilot não será apenas um software para controlar uma mesa de som.

Ele será um verdadeiro copiloto da operação de áudio da igreja.

Seu papel será compreender a programação, a liturgia, os participantes, os equipamentos e a mesa de som, auxiliando o operador em todas as etapas da operação, desde o planejamento até a análise pós-evento.

O objetivo não é substituir o operador, mas permitir que ele concentre sua atenção na qualidade da adoração e da mensagem, enquanto o Audio Copilot cuida das tarefas repetitivas, reduz os erros humanos, monitora a saúde do sistema de áudio e fornece suporte inteligente durante toda a programação.

---

# Arquitetura do Sistema

O Audio Copilot será desenvolvido em módulos independentes para facilitar manutenção, testes e futuras expansões.

Principais módulos:

- Cadastro
- Planejamento
- Motor do Audio Copilot
- Comunicação com a Mesa
- Interface do Operador
- Inteligência Artificial
- Monitoramento
- Relatórios
- Plataforma Mobile

# Estrutura Inicial do Projeto

src/

├── ai/
├── clients/
├── config/
├── controllers/
├── models/
├── repositories/
├── rules/
├── services/
├── ui/
├── utils/
└── main.py

---

# Ambiente de Desenvolvimento

Desenvolvimento:
- Windows 11
- Visual Studio Code
- Python 3.14
- Git
- GitHub

Hardware de produção:
- Soundcraft Ui24R
- Notebook Windows
- Rede local da igreja

---

# Tecnologias

Linguagem
- Python

Interface
- Flet (inicialmente)
- Interface Web (futuro)

Persistência
- JSON
- SQLite (futuro)

Comunicação
- WebSocket
- REST API

Controle de versão
- Git
- GitHub

Editor
- Visual Studio Code

Sistema Operacional
- Windows 11

---

# Metas das Versões

v0.1
- Estrutura inicial do projeto

v0.2
- Modelos de dados

v0.3
- Persistência

v0.4
- Cadastro da igreja

v0.5
- Planejamento dos eventos

v0.6
- Interface inicial

v0.7
- Console inteligente

v0.8
- Integração com a Ui24R

v0.9
- Operação em tempo real

v1.0
Primeira operação completa durante um culto da Igreja Presbiteriana de Piracicaba.

v2.0
Primeira IA operacional funcionando durante um culto.

v3.0
Primeira versão comercial do Audio Copilot.

---

# Filosofia do Projeto

O Audio Copilot não tem como objetivo substituir o operador de áudio.

Seu propósito é atuar como um copiloto inteligente, reduzindo tarefas repetitivas, diminuindo erros humanos e oferecendo suporte técnico durante toda a operação.

Toda decisão importante continuará pertencendo ao operador.

A inteligência artificial deverá atuar de forma transparente, explicando suas recomendações e permitindo que qualquer ação automática seja autorizada, desfeita ou desativada.

O sucesso do projeto será medido não pela quantidade de automações implementadas, mas pela confiança que o operador terá em trabalhar ao lado do Audio Copilot.