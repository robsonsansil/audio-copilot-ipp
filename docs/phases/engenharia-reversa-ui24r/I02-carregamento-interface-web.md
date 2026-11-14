# Sprint I02 — Carregamento da Interface Web

## Objetivo

Documentar todo o processo de carregamento da interface web da Soundcraft Ui24R, identificando os protocolos utilizados, a sequência de comunicação e os serviços envolvidos até que a página esteja totalmente disponível ao navegador.

---

## Arquivos da captura

- Vídeo:
  - `I02-carregamento-interface-web.mp4`

- Captura de rede:
  - `I02-carregamento-interface-web.pcapng`

- Navegador:
  - `I02-carregamento-interface-web.har`

---

# Cenário

Equipamento utilizado:

- Notebook Windows 11
- Google Chrome
- Wireshark
- Mesa Soundcraft Ui24R

Configuração da captura:

- Interface Wi-Fi
- Filtro:
  ```
  host 10.10.1.1
  ```

A captura iniciou antes da abertura do navegador e foi encerrada após o carregamento completo da interface.

---

# Sequência observada

## 1. Abertura do navegador

O usuário abre o Google Chrome já conectado à rede da Ui24R.

Nenhuma autenticação é solicitada.

---

## 2. Acesso ao endereço

O navegador acessa:

```
http://10.10.1.1
```

Não é utilizada conexão HTTPS.

Durante toda a captura não foi observada uma sessão HTTPS funcional.

---

## 3. Comunicação HTTP

Após o acesso ao endereço local inicia-se intenso tráfego HTTP entre:

Cliente

```
10.10.1.106
```

Mesa

```
10.10.1.1
```

O navegador passa a solicitar diversos recursos necessários para montar toda a interface.

Esses recursos incluem arquivos HTML, JavaScript, CSS, imagens e demais componentes da aplicação web.

---

## 4. Carregamento dos recursos

O volume de conexões TCP aumenta significativamente.

Observa-se grande quantidade de sessões curtas destinadas principalmente à porta 80.

Esse comportamento é compatível com navegadores modernos carregando múltiplos arquivos simultaneamente.

---

## 5. Serviços em segundo plano

Enquanto a interface é carregada, o Windows e o Chrome continuam executando tarefas automáticas, incluindo consultas DNS para diversos domínios, como:

- google.com
- clients4.google.com
- mtalk.google.com
- chatgpt.com
- ws.chatgpt.com
- dell.com
- www.msftconnecttest.com

Essas comunicações pertencem ao sistema operacional e ao navegador, não à interface da Ui24R.

---

## 6. Testes automáticos de conectividade

Durante o carregamento o Windows realiza verificações de conectividade utilizando:

```
www.msftconnecttest.com
```

As respostas retornam através do equipamento localizado em:

```
10.10.1.1
```

em vez do servidor público esperado.

Esse comportamento é compatível com redes isoladas ou equipamentos que interceptam as consultas DNS e HTTP.

---

## 7. Tentativas HTTPS

Paralelamente ao carregamento da interface HTTP foram observadas centenas de tentativas de conexão TCP para:

```
porta 443
```

Grande parte dessas conexões recebe imediatamente:

```
RST, ACK
```

originados do endereço:

```
10.10.1.1
```

Não foi estabelecida sessão HTTPS funcional durante a captura.

---

## 8. QUIC

Também foram observadas tentativas utilizando QUIC (UDP/443).

Essas conexões terminam com mensagens ICMP indicando:

```
Destination Unreachable
Port Unreachable
```

Isso indica que o equipamento não disponibiliza comunicação QUIC.

---

# Protocolos identificados

Durante o carregamento foram observados:

- ARP
- DHCP
- DNS
- TCP
- HTTP
- UDP
- QUIC
- ICMP

Não foi identificado HTTPS funcional.

---

# Evidências

Foi identificado intenso tráfego HTTP para o endereço:

```
10.10.1.1
```

O volume de conexões TCP para a porta 80 é compatível com o carregamento completo da interface web.

As tentativas para HTTPS foram rejeitadas pelo próprio equipamento.

As consultas DNS externas foram parcialmente interceptadas pela rede local, indicando que a Ui24R atua como equipamento central da rede.

---

# Conclusões

O carregamento da interface web da Ui24R ocorre exclusivamente através de HTTP.

Durante esta captura não foram identificadas conexões HTTPS utilizadas pela aplicação.

O navegador realiza múltiplas conexões TCP simultâneas para obter todos os recursos da interface.

Grande parte do tráfego adicional observado pertence ao próprio Windows e ao Google Chrome e não faz parte do protocolo da Ui24R.

A interface foi carregada com sucesso utilizando comunicação HTTP local entre o cliente e o equipamento localizado em 10.10.1.1.

---

# Próxima Sprint

Sprint I03 — Reconexão da Interface