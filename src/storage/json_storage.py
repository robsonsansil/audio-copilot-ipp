"""
Persistência em JSON.
"""

import json
from pathlib import Path


class JsonStorage:
    """Classe responsável por salvar e carregar arquivos JSON."""

    @staticmethod
    def save(data: dict, filename: str) -> None:
        """Salva um dicionário em um arquivo JSON."""

        path = Path(filename)

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load(filename: str) -> dict:
        """Carrega um arquivo JSON."""

        path = Path(filename)

        if not path.exists():
            return {}

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)


def main() -> None:
    """Teste simples."""

    data = {
        "evento": "Culto Domingo",
        "operador": "Robson",
        "preset": "Culto Domingo",
    }

    JsonStorage.save(data, "config/teste.json")

    resultado = JsonStorage.load("config/teste.json")

    print(resultado)


if __name__ == "__main__":
    main()