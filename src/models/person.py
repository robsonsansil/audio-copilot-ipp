from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    """
    Representa uma pessoa cadastrada na igreja.
    """

    name: str
    roles: List[str] = field(default_factory=list)
    active: bool = True

    def __str__(self):
        return f"{self.name} ({', '.join(self.roles)})"


if __name__ == "__main__":

    person = Person(
        name="Robson",
        roles=[
            "Operador",
            "Violonista"
        ]
    )

    print(person)