"""
Representa um tipo de programação da igreja.
"""

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Programming:
    """
    Representa uma programação padrão da igreja.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""
    description: str = ""

    active: bool = True

    def __str__(self):
        return self.name


def main():
    programming = Programming(
        name="Culto Domingo",
        description="Programação padrão do culto de domingo."
    )

    print(programming)


if __name__ == "__main__":
    main()