from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Profile:
    """
    Representa um perfil de utilização da mesa.
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    category: str = ""
    description: str = ""
    active: bool = True

    def __str__(self):
        return f"{self.name} ({self.category})"


def main():
    profile = Profile(
        name="Vocal Masculino",
        category="Vocal",
        description="Perfil padrão para vocal masculino."
    )

    print(profile)


if __name__ == "__main__":
    main()