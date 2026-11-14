# Sprint I01 – Inicialização da Ui24R

## Objetivo

Documentar o comportamento da Soundcraft Ui24R durante sua inicialização física, observando exclusivamente a atividade de rede gerada após a energização do equipamento.

O objetivo desta sprint é compreender como a mesa passa do estado desligado para um estado apto a aceitar conexões de clientes, identificando os principais eventos de rede que ocorrem durante esse processo.

---

# Evidências

Foram utilizadas as seguintes evidências:

- captura.mp4
- captura.pcapng

Nesta sprint não foi utilizada captura HAR, pois nenhuma interface web foi acessada durante o experimento.

---

# Ambiente de Teste

**Equipamento**

- Soundcraft Ui24R

**Computador**

- Windows 11

**Conexão**

- Wi-Fi da Ui24R

**Ferramentas**

- Wireshark
- OBS Studio

Filtro utilizado no Wireshark:

```
host 10.10.1.1
```

---

# Procedimento Executado

1. Iniciar a captura no Wireshark.
2. Iniciar a gravação da tela pelo OBS Studio.
3. Conectar o computador à rede Wi-Fi da Ui24R.
4. Manter a captura ativa sem abrir qualquer navegador.
5. Encerrar a captura após aproximadamente cinquenta segundos.

---

# Linha do Tempo Observada

A captura possui duração aproximada de **50,49 segundos** e contém **1.294 pacotes**.

Durante esse período foram observados os seguintes eventos.

| Tempo | Evento observado |
|--------|------------------|
| 0–3 s | DHCP, ARP e primeiras consultas DNS |
| 0–6 s | Consultas DNS para diversos serviços do Windows |
| 2–8 s | Tentativas TCP para porta 443 respondidas com RST/ACK |
| 8 s | Início do tráfego QUIC sobre UDP |
| 12 s | Requisições HTTP para `connecttest.txt` |
| 17 s | Nova verificação automática de conectividade |
| 20–46 s | Grande quantidade de tentativas TCP para porta 443 |
| 43 s | Algumas conexões HTTP completam o handshake e recebem resposta 301 |
| 46–50 s | Redução gradual do tráfego |

---

# Atividade de Rede Observada

O computador recebeu o endereço IP:

```
10.10.1.106
```

Toda a captura foi realizada com comunicação direcionada ao host:

```
10.10.1.1
```

O endereço MAC associado ao equipamento foi:

```
2C:C3:E6:57:06:6C
```

---

# Protocolos Observados

Durante a captura foram identificados:

- ARP
- DHCP
- DNS
- TCP
- UDP
- QUIC
- HTTP
- ICMP

Não foram observadas conexões WebSocket nesta sprint.

---

# Evidências Identificadas

## DHCP

Foi observado o processo de obtenção de configuração IP pelo computador após sua conexão à rede.

---

## ARP

Foram observadas mensagens ARP utilizadas para descoberta do equipamento presente no endereço 10.10.1.1.

---

## DNS

Diversas consultas DNS foram realizadas automaticamente pelo Windows e por aplicações executadas em segundo plano.

Entre os domínios consultados encontram-se:

- www.msftconnecttest.com
- dell.com
- google.com
- mtalk.google.com
- clients4.google.com
- chatgpt.com
- ws.chatgpt.com

Em diversas respostas, o endereço retornado foi **10.10.1.1**, indicando comportamento compatível com redirecionamento DNS local.

---

## HTTP

Foram observadas requisições HTTP para:

```
http://www.msftconnecttest.com/connecttest.txt
```

As respostas retornaram código:

```
HTTP 301
```

indicando redirecionamento para conteúdo hospedado localmente.

---

## HTTPS

Foram identificadas centenas de tentativas de conexão TCP para a porta 443.

Grande parte dessas conexões recebeu imediatamente resposta:

```
RST, ACK
```

encerrando a conexão antes do estabelecimento de uma sessão HTTPS.

---

## QUIC

Também foram observadas tentativas de comunicação utilizando QUIC sobre UDP.

Em vários momentos ocorreram respostas:

```
ICMP Destination Unreachable
Port Unreachable
```

indicando que esse tipo de comunicação não foi aceito pelo equipamento durante a captura.

---

# Fatos Confirmados

A análise das evidências permite confirmar que:

- o computador conectou-se corretamente à rede Wi-Fi da Ui24R;
- o equipamento respondeu às requisições ARP;
- o equipamento respondeu às consultas DNS;
- a porta HTTP respondeu às requisições realizadas;
- a porta HTTPS rejeitou grande parte das conexões estabelecidas;
- durante esta sprint nenhuma interface web foi aberta pelo usuário.

---

# Hipóteses

Com base nas evidências coletadas, foram levantadas as seguintes hipóteses:

- o endereço 10.10.1.1 atua como equipamento central da rede;
- existe um mecanismo local de redirecionamento DNS;
- a interface HTTP encontra-se disponível antes da interface HTTPS;
- o equipamento pode operar como servidor web local para controle da mesa.

Essas hipóteses deverão ser confirmadas nas próximas sprints.

---

# Limitações da Sprint

Esta sprint não permite concluir:

- se o endereço 10.10.1.1 corresponde definitivamente à Soundcraft Ui24R;
- se existe servidor HTTPS funcional;
- se houve carregamento completo da interface web;
- se existe comunicação WebSocket;
- quais serviços internos da mesa estavam ativos.

Esses pontos serão investigados nas próximas sprints.

---

# Próximos Passos

Na Sprint I02 será analisado o carregamento da interface web da Ui24R.

O objetivo será identificar:

- arquivos HTML;
- arquivos JavaScript;
- folhas de estilo;
- recursos estáticos;
- requisições HTTP;
- estabelecimento da conexão WebSocket;
- sequência completa de inicialização da interface de controle.

---

# Conclusão

A Sprint I01 documentou o comportamento inicial da rede da Ui24R imediatamente após a conexão do computador ao seu ponto de acesso Wi-Fi.

Foi possível confirmar que o equipamento fornece infraestrutura básica de rede, responde às consultas ARP e DNS e disponibiliza comunicação HTTP, enquanto conexões HTTPS e QUIC não foram estabelecidas com sucesso durante o período analisado.

As evidências coletadas servirão como base para a análise da interface web e do protocolo de comunicação nas próximas etapas da engenharia reversa.

---

# Situação da Sprint

**Status:** ✅ Concluída