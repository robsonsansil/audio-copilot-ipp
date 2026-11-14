"""
Representa uma etapa da liturgia.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.liturgy import Liturgy


@dataclass
class LiturgyStep:
    """
    Representa uma etapa da liturgia.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    liturgy: Liturgy | None = None

    order: int = 1

    name: str = ""

    description: str = ""

    active: bool = True

    def __str__(self):
        liturgy_name = (
            self.liturgy.name
            if self.liturgy
            else "Sem liturgia"
        )

        return (
            f"{self.order:02d} - "
            f"{self.name} "
            f"({liturgy_name})"
        )


def main():

    from src.models.programming import Programming

    programming = Programming(
        name="Culto Domingo",
        description="Programação padrão."
    )

    liturgy = Liturgy(
        programming=programming,
        name="Liturgia Domingo Noite",
    )

    step = LiturgyStep(
        liturgy=liturgy,
        order=1,
        name="Prelúdio",
        description="Momento instrumental antes do início."
    )

    print(step)


if __name__ == "__main__":
    main()