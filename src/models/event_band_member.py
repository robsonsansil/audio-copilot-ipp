"""
Representa um integrante da banda de um evento.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.event import Event
from src.models.person import Person


@dataclass
class EventBandMember:
    """
    Representa um integrante da banda de um evento.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    event: Event | None = None
    person: Person | None = None

    confirmed: bool = False

    active: bool = True

    def __str__(self):
        event_name = (
            self.event.programming.name
            if self.event and self.event.programming
            else "Sem evento"
        )

        person_name = (
            self.person.name
            if self.person
            else "Sem pessoa"
        )

        status = "Confirmado" if self.confirmed else "Pendente"

        return f"{person_name} ({event_name}) - {status}"


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

    person = Person(
        name="Robson",
        roles=["Violonista"],
    )

    member = EventBandMember(
        event=event,
        person=person,
        confirmed=True,
    )

    print(member)


if __name__ == "__main__":
    main()