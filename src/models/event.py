"""
Representa um evento da igreja.
"""

from dataclasses import dataclass, field
from datetime import date, time
from uuid import uuid4

from src.models.programming import Programming


@dataclass
class Event:
    """
    Representa uma ocorrência de uma programação.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    programming: Programming | None = None

    event_date: date = field(default_factory=date.today)
    event_time: time = field(default_factory=lambda: time(19, 0))

    description: str = ""

    status: str = "Planejado"

    active: bool = True

    def __str__(self):
        programming_name = (
            self.programming.name
            if self.programming
            else "Sem programação"
        )

        return (
            f"{self.event_date.strftime('%d/%m/%Y')} - "
            f"{programming_name} ({self.status})"
        )


def main():
    programming = Programming(
        name="Culto Domingo",
        description="Programação padrão do culto dominical.",
    )

    event = Event(
        programming=programming,
        event_date=date(2026, 11, 15),
        event_time=time(19, 0),
        description="Culto Noturno",
    )

    print(event)


if __name__ == "__main__":
    main()