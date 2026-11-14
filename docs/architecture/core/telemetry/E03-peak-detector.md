# Sprint E03 – Peak Detector

## Objetivo

Definir o componente responsável pela detecção, armazenamento e disponibilização dos valores de pico (Peak) dos sinais de áudio monitorados pelo Audio Copilot.

O Peak Detector complementa os medidores em tempo real, permitindo ao operador visualizar rapidamente o maior nível atingido por cada canal, mesmo que esse pico tenha ocorrido em um intervalo muito curto.

Essa informação é essencial para ajustes de ganho, prevenção de clipping e análise da dinâmica do áudio.

---

# Visão Geral

Durante uma operação ao vivo, muitos picos acontecem de forma extremamente rápida.

Em diversos casos, o operador não consegue percebê-los apenas observando os medidores em tempo real.

O Peak Detector registra esses valores máximos e os mantém visíveis por alguns segundos, facilitando a tomada de decisão.

Este componente não altera qualquer configuração da mesa.

Sua função é apenas detectar, registrar e disponibilizar os maiores níveis atingidos pelos sinais de áudio.

---

# Arquitetura

Fluxo simplificado:

```text
Soundcraft Ui24R
        │
        ▼
Telemetry Manager
        │
        ▼
Audio Levels
        │
        ▼
Peak Detector
        │
        ├────────► State Manager
        ├────────► Console de Operação
        ├────────► Painel da IA
        └────────► Histórico
```

O Peak Detector recebe continuamente os níveis processados pelo módulo Audio Levels.

---

# Responsabilidades

O Peak Detector será responsável por:

- detectar novos valores máximos;
- armazenar temporariamente os picos;
- atualizar os indicadores visuais;
- informar os demais módulos sobre novos picos;
- disponibilizar dados para análises posteriores.

---

# Funcionamento

Para cada canal monitorado, o Peak Detector acompanha continuamente os níveis de áudio.

Sempre que um novo valor superar o maior valor registrado, ele será armazenado como o novo Peak.

Fluxo simplificado:

```text
Novo nível recebido

↓

Comparar com Peak atual

↓

Maior?

↓

Sim

↓

Atualizar Peak

↓

Publicar evento
```

---

# Persistência Visual

Após detectar um novo pico, o indicador permanecerá visível por alguns segundos.

Esse comportamento facilita a visualização pelo operador.

Exemplo:

```text
███████▌
```

Mesmo que o nível atual diminua imediatamente, o indicador de Peak continuará sendo exibido temporariamente.

O tempo exato de permanência será configurável durante a implementação.

---

# Atualização

O Peak Detector acompanha continuamente todos os canais ativos.

Cada canal mantém seu próprio valor de pico.

Os cálculos são independentes entre si.

---

# Integração com o Console

No Console de Operação, cada canal poderá apresentar:

- nível instantâneo;
- indicador de Peak;
- indicador de Clipping.

Essas informações permitem ao operador avaliar rapidamente o comportamento do sinal.

---

# Integração com a Inteligência Artificial

Os valores de Peak serão utilizados pela IA para identificar padrões de operação.

Exemplos:

- canais constantemente próximos do limite;
- excesso de dinâmica;
- variações abruptas de volume;
- possíveis necessidades de ajuste de ganho.

A IA utilizará essas informações apenas como apoio às suas recomendações.

---

# Integração com o Histórico

Os maiores picos registrados poderão ser utilizados para:

- geração de relatórios;
- análise técnica;
- auditoria do evento;
- comparação entre eventos.

O histórico detalhado será definido em módulos específicos.

---

# Eventos Produzidos

Sempre que um novo pico for detectado, poderão ser publicados eventos como:

- ChannelPeakDetected
- PeakUpdated
- PeakReset

Esses eventos serão distribuídos pelo Event Bus.

---

# Reinicialização

Os valores de Peak poderão ser reiniciados em diferentes situações.

Exemplos:

- início de um novo evento;
- troca de snapshot;
- reinicialização manual;
- comando do operador.

Essa funcionalidade evita que picos antigos permaneçam influenciando a operação atual.

---

# Benefícios

A utilização do Peak Detector oferece diversas vantagens:

- facilita o ajuste de ganho;
- melhora a identificação de sinais excessivos;
- auxilia na prevenção de clipping;
- melhora a análise da dinâmica do áudio;
- fornece informações úteis para a IA;
- aumenta a segurança durante eventos ao vivo.

---

# Separação de Responsabilidades

O Peak Detector possui uma única responsabilidade.

Ele não:

- calcula níveis de áudio;
- detecta clipping;
- detecta silêncio;
- altera configurações da mesa;
- envia comandos para a Ui24R.

Essas funções pertencem a outros componentes da Telemetria.

---

# Próximos Componentes

Após o Peak Detector, a arquitetura da Telemetria será complementada pelos módulos:

- Clip Detector;
- Silence Detector;
- Meter Cache;
- Statistics.

Cada componente executará uma tarefa específica, mantendo a arquitetura modular e de fácil manutenção.

---

# Situação da Sprint

**Status:** ✅ Concluída