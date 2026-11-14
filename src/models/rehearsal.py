"""
Representa um ensaio de um evento.
"""

from dataclasses import dataclass, field
from datetime import date, time
from uuid import uuid4

from src.models.event import Event


@dataclass
class Rehearsal:
    """
    Representa um ensaio de um evento.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    event: Event | None = None

    rehearsal_date: date = field(default_factory=date.today)

    rehearsal_time: time = field(default_factory=lambda: time(19, 30))

    description: str = ""

    completed: bool = False

    active: bool = True

    def __str__(self):

        event_name = (
            self.event.programming.name
            if self.event and self.event.programming
            else "Sem evento"
        )

        status = "Realizado" if self.completed else "Planejado"

        return (
            f"{event_name} - "
            f"{self.rehearsal_date.strftime('%d/%m/%Y')} "
            f"({status})"
        )


def main():

    from datetime import date, time

    from src.models.programming import Programming

    programming = Programming(
        name="Culto Domingo",
    )

    event = Event(
        programming=programming,
        event_date=date(2026, 11, 15),
        event_time=time(19, 0),
    )

    rehearsal = Rehearsal(
        event=event,
        rehearsal_date=date(2026, 11, 13),
        rehearsal_time=time(19, 30),
        description="Ensaio geral da banda.",
        completed=False,
    )

    print(rehearsal)


if __name__ == "__main__":
    main()