"""
Representa o retorno de palco utilizado por um integrante da banda em um evento.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.event import Event
from src.models.programming import Programming
from src.models.person import Person
from src.models.monitor import Monitor
from src.models.event_band_member import EventBandMember


@dataclass
class EventBandMonitor:
    """
    Representa o retorno utilizado por um integrante da banda.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    band_member: EventBandMember | None = None

    monitor: Monitor | None = None

    active: bool = True

    def __str__(self):

        person_name = (
            self.band_member.person.name
            if self.band_member and self.band_member.person
            else "Sem integrante"
        )

        monitor_name = (
            self.monitor.name
            if self.monitor
            else "Sem retorno"
        )

        return f"{person_name} - {monitor_name}"


def main():

    from datetime import date, time

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

    band_member = EventBandMember(
        event=event,
        person=person,
        confirmed=True,
    )

    monitor = Monitor(
        name="Retorno 1",
        location="Palco",
        output="Aux 1",
    )

    event_monitor = EventBandMonitor(
        band_member=band_member,
        monitor=monitor,
    )

    print(event_monitor)


if __name__ == "__main__":
    main()