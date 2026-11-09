"""
Audio Copilot IPP
Cliente de comunicação com a Soundcraft Ui24R.
"""

from typing import Any


class Ui24RClient:

    def __init__(self, host: str = "10.10.1.1"):
        self.host = host
        self.connected = False

    def connect(self):
        """
        Conecta na mesa.
        """
        print(f"Conectando em {self.host}...")
        self.connected = True

    def disconnect(self):
        """
        Desconecta da mesa.
        """
        print("Desconectando...")
        self.connected = False

    def read(self) -> Any:
        """
        Lê informações da mesa.
        """
        if not self.connected:
            raise ConnectionError("Mesa não conectada.")

        print("Lendo parâmetros...")
        return {}

    def write(self, command: str, value: Any):
        """
        Envia um comando para a mesa.
        """
        if not self.connected:
            raise ConnectionError("Mesa não conectada.")

        print(f"Enviando: {command} = {value}")

    def get_status(self):
        return {
            "host": self.host,
            "connected": self.connected,
        }
