"""
Representa o instrumento utilizado por um integrante da banda em um evento.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.event_band_member import EventBandMember
from src.models.instrument import Instrument


@dataclass
class EventBandInstrument:
    """
    Representa o instrumento que um integrante da banda utilizará em um evento.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    band_member: EventBandMember | None = None

    instrument: Instrument | None = None

    active: bool = True

    def __str__(self):

        person_name = (
            self.band_member.person.name
            if self.band_member and self.band_member.person
            else "Sem integrante"
        )

        instrument_name = (
            self.instrument.name
            if self.instrument
            else "Sem instrumento"
        )

        return f"{person_name} - {instrument_name}"


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

    instrument = Instrument(
        name="Violão Martin",
        category="Violão",
        output_type="DI Box",
        phantom_power=False,
    )

    event_instrument = EventBandInstrument(
        band_member=band_member,
        instrument=instrument,
    )

    print(event_instrument)


if __name__ == "__main__":
    main()