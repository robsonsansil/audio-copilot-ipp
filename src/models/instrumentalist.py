from dataclasses import dataclass, field
from typing import List


@dataclass
class Instrumentalist:
    """
    Representa um instrumentista da igreja.
    """

    person_name: str
    instruments: List[str] = field(default_factory=list)
    active: bool = True

    def __str__(self):
        return f"{self.person_name} ({', '.join(self.instruments)})"


def main():
    instrumentalist = Instrumentalist(
        person_name="Robson",
        instruments=[
            "Violão",
            "Cajón"
        ]
    )

    print(instrumentalist)


if __name__ == "__main__":
    main()