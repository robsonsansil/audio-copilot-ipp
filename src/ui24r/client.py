"""
Audio Copilot IPP
Cliente de comunicação com a Soundcraft Ui24R.
"""

from typing import Any


class Ui24RClient:
    """Cliente responsável pela comunicação com a mesa Ui24R."""

    def __init__(self, host: str = "10.10.1.1"):
        self.host = host
        self.connected = False

    def connect(self) -> None:
        """Conecta na mesa."""
        print(f"Conectando em {self.host}...")
        self.connected = True

    def disconnect(self) -> None:
        """Desconecta da mesa."""
        print("Desconectando...")
        self.connected = False

    def read(self) -> Any:
        """Lê informações da mesa."""

        if not self.connected:
            raise ConnectionError("Mesa não conectada.")

        print("Lendo parâmetros...")
        return {}

    def write(self, command: str, value: Any) -> None:
        """Envia um comando para a mesa."""

        if not self.connected:
            raise ConnectionError("Mesa não conectada.")

        print(f"Enviando: {command} = {value}")

    def get_status(self) -> dict:
        """Retorna o estado atual da conexão."""

        return {
            "host": self.host,
            "connected": self.connected,
        }


def main() -> None:
    """Função principal para testes."""

    mesa = Ui24RClient()

    mesa.connect()

    print(mesa.get_status())

    mesa.write("CH01.GAIN", -18)

    mesa.disconnect()


if __name__ == "__main__":
    main()
