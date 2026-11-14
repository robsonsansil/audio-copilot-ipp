"""
Representa o microfone utilizado por um integrante da banda em um evento.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.event_band_member import EventBandMember
from src.models.microphone import Microphone


@dataclass
class EventBandMicrophone:
    """
    Representa o microfone utilizado por um integrante da banda.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    band_member: EventBandMember | None = None

    microphone: Microphone | None = None

    active: bool = True

    def __str__(self):

        person_name = (
            self.band_member.person.name
            if self.band_member and self.band_member.person
            else "Sem integrante"
        )

        microphone_name = (
            self.microphone.name
            if self.microphone
            else "Sem microfone"
        )

        return f"{person_name} - {microphone_name}"


def main():

    from datetime import date, time

    from src.models.programming import Programming
    from src.models.event import Event
    from src.models.person import Person

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

    microphone = Microphone(
        name="Shure SM58",
        type="Dinâmico",
        color="Azul",
        phantom_power=False,
        wireless=False,
    )

    event_microphone = EventBandMicrophone(
        band_member=band_member,
        microphone=microphone,
    )

    print(event_microphone)


if __name__ == "__main__":
    main()