"""
Representa a configuração aprovada de um ensaio para utilização no evento.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.event import Event
from src.models.rehearsal import Rehearsal


@dataclass
class RehearsalTemplate:
    """
    Configuração oficial aprovada durante o ensaio.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    event: Event | None = None

    rehearsal: Rehearsal | None = None

    approved: bool = False

    active: bool = True

    def __str__(self):

        event_name = (
            self.event.programming.name
            if self.event and self.event.programming
            else "Sem evento"
        )

        status = "Aprovado" if self.approved else "Pendente"

        return f"{event_name} ({status})"


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
    )

    template = RehearsalTemplate(
        event=event,
        rehearsal=rehearsal,
        approved=True,
    )

    print(template)


if __name__ == "__main__":
    main()