"""
Representa uma cena da mesa de som.
"""

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Scene:
    """
    Representa uma cena (Scene) da mesa de som.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""
    description: str = ""

    category: str = ""

    active: bool = True

    def __str__(self):
        return f"{self.name} ({self.category})"


def main():
    scene = Scene(
        name="Culto Domingo",
        category="Culto",
        description="Cena padrão para os cultos de domingo."
    )

    print(scene)


if __name__ == "__main__":
    main()