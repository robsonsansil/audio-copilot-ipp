"""
Representa um equipamento de áudio da igreja.
"""

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Equipment:
    """
    Representa qualquer equipamento utilizado
    na operação de áudio.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""
    category: str = ""
    brand: str = ""
    model: str = ""

    serial_number: str = ""

    location: str = ""

    active: bool = True

    notes: str = ""

    def __str__(self):
        description = self.name

        if self.brand:
            description += f" - {self.brand}"

        if self.model:
            description += f" {self.model}"

        return description


def main():
    equipment = Equipment(
        name="Direct Box 01",
        category="Direct Box",
        brand="Santo Ângelo",
        model="DB100",
        location="Sala de Áudio",
        notes="Utilizado para instrumentos.",
    )

    print(equipment)


if __name__ == "__main__":
    main()