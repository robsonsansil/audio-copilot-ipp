# Sprint E03 – Meter Cache

## Objetivo

Definir o componente responsável por otimizar a atualização dos medidores em tempo real do Audio Copilot.

O Meter Cache atua como uma camada intermediária entre o processamento da Telemetria e a Interface do Usuário, reduzindo a quantidade de atualizações desnecessárias e garantindo uma experiência visual fluida, estável e responsiva.

Seu principal objetivo é evitar que a interface seja redesenhada centenas de vezes por segundo.

---

# Visão Geral

A Soundcraft Ui24R envia continuamente informações sobre todos os canais.

Em eventos ao vivo, essa quantidade de dados pode ser muito elevada.

Embora a Telemetria precise processar todas essas informações, a interface gráfica não necessita ser atualizada na mesma frequência.

O Meter Cache resolve esse problema armazenando temporariamente os últimos valores disponíveis e disponibilizando apenas as atualizações necessárias para a interface.

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
Meter Cache
        │
        ├────────► Dashboard
        ├────────► Console de Operação
        ├────────► Painel da IA
        └────────► Mobile
```

O Meter Cache desacopla a velocidade de aquisição dos dados da velocidade de atualização da interface.

---

# Responsabilidades

O Meter Cache será responsável por:

- armazenar temporariamente os níveis de áudio;
- reduzir atualizações repetitivas;
- disponibilizar os últimos valores válidos;
- sincronizar a atualização dos medidores;
- melhorar o desempenho da interface;
- reduzir o consumo de CPU.

---

# Problema Resolvido

Sem um cache intermediário, o sistema precisaria atualizar toda a interface sempre que novos dados fossem recebidos da Ui24R.

Exemplo:

```text
Ui24R

↓

250 atualizações por segundo

↓

Interface

↓

250 redesenhos por segundo
```

Esse comportamento desperdiça processamento e pode comprometer a fluidez da aplicação.

---

# Solução

Com o Meter Cache:

```text
Ui24R

↓

250 atualizações

↓

Telemetry Manager

↓

Meter Cache

↓

30 atualizações por segundo

↓

Interface
```

A Telemetria continua recebendo todos os dados, enquanto a interface recebe apenas as informações necessárias para uma visualização suave.

---

# Funcionamento

O ciclo de funcionamento será:

```text
Receber novo nível

↓

Atualizar cache

↓

Aguardar próximo ciclo gráfico

↓

Enviar dados para Interface

↓

Repetir
```

Dessa forma, os dados permanecem atualizados sem sobrecarregar a renderização.

---

# Dados Armazenados

Para cada canal poderão ser armazenadas informações como:

- nível atual;
- último valor exibido;
- timestamp da última atualização;
- indicador de alteração;
- estado do canal.

Esses dados permanecem apenas em memória.

---

# Atualização Inteligente

O Meter Cache poderá evitar atualizações quando não houver mudanças relevantes.

Exemplo:

```text
Canal 08

Nível atual:

-18,2 dB

↓

Novo nível:

-18,2 dB

↓

Nenhuma atualização necessária.
```

Outro exemplo:

```text
Canal 08

-18,2 dB

↓

-17,8 dB

↓

Atualizar interface.
```

Essa estratégia reduz o número de redesenhos da interface.

---

# Integração com o Dashboard

O Dashboard utilizará os valores armazenados no Meter Cache para exibir:

- medidores dos canais;
- níveis do PA;
- níveis dos retornos;
- indicadores gerais.

---

# Integração com o Console

O Console de Operação utilizará o Meter Cache para apresentar medidores fluidos e sincronizados.

O operador perceberá uma movimentação natural dos níveis, sem travamentos ou oscilações excessivas.

---

# Integração com o Mobile

O aplicativo Mobile utilizará uma versão resumida do Meter Cache.

A frequência de atualização poderá ser menor para reduzir o consumo de bateria e largura de banda.

---

# Integração com a Inteligência Artificial

A Inteligência Artificial não utilizará diretamente o Meter Cache para realizar análises.

Ela continuará recebendo eventos e dados diretamente da Telemetria.

O Meter Cache existe apenas para otimizar a apresentação das informações nas interfaces.

---

# Benefícios

A utilização do Meter Cache proporciona:

- menor utilização de CPU;
- menor consumo de memória gráfica;
- interfaces mais fluidas;
- redução de atualizações desnecessárias;
- desacoplamento entre processamento e renderização;
- melhor experiência para o operador.

---

# Separação de Responsabilidades

O Meter Cache possui responsabilidade única.

Ele não:

- processa sinais de áudio;
- calcula Peak;
- detecta clipping;
- detecta silêncio;
- executa análises da IA;
- envia comandos para a Ui24R.

Sua função é exclusivamente otimizar a atualização visual dos medidores.

---

# Evoluções Futuras

Nas próximas versões, o Meter Cache poderá incorporar funcionalidades como:

- atualização adaptativa conforme o desempenho do equipamento;
- diferentes taxas de atualização para Dashboard, Console e Mobile;
- suavização (smoothing) dos medidores para tornar a movimentação mais natural;
- animações configuráveis;
- atualização seletiva apenas dos canais visíveis na tela.

---

# Situação da Sprint

**Status:** ✅ Concluída