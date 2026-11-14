"""
Representa uma liturgia da igreja.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.programming import Programming


@dataclass
class Liturgy:
    """
    Representa uma liturgia associada a uma programação.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    programming: Programming | None = None

    name: str = ""
    description: str = ""

    active: bool = True

    def __str__(self):
        programming_name = (
            self.programming.name
            if self.programming
            else "Sem programação"
        )

        return f"{self.name} ({programming_name})"


def main():
    programming = Programming(
        name="Culto Domingo",
        description="Programação padrão do culto dominical.",
    )

    liturgy = Liturgy(
        programming=programming,
        name="Liturgia Domingo Noite",
        description="Liturgia padrão do culto noturno.",
    )

    print(liturgy)


if __name__ == "__main__":
    main()