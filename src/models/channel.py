"""
Representa um canal físico da mesa de som.
"""

from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4

from src.models.person import Person
from src.models.instrument import Instrument
from src.models.microphone import Microphone
from src.models.profile import Profile
from src.models.preset import Preset


@dataclass
class Channel:
    """
    Representa um canal físico da mesa de som.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    number: int = 1
    name: str = ""

    person: Optional[Person] = None
    instrument: Optional[Instrument] = None
    microphone: Optional[Microphone] = None

    profile: Optional[Profile] = None
    preset: Optional[Preset] = None

    phantom: bool = False
    muted: bool = False
    active: bool = True

    def __str__(self):
        return f"CH{self.number:02d} - {self.name}"


def main():
    """Teste simples."""

    person = Person(
        name="Robson",
        roles=[
            "Operador",
            "Violonista",
        ],
    )

    instrument = Instrument(
        name="Martin Road Series",
        category="Violão",
        output_type="DI Box",
        phantom_power=False,
    )

    microphone = Microphone(
        name="Shure SM58",
        type="Dinâmico",
        color="Azul",
        wireless=False,
        phantom_power=False,
    )

    profile = Profile(
        name="Violão",
        category="Instrumento",
        description="Perfil padrão para violão.",
    )

    preset = Preset(
        name="Violão Martin",
        gain=24,
        hpf=80,
        compressor=True,
    )

    channel = Channel(
        number=1,
        name="Violão",
        person=person,
        instrument=instrument,
        microphone=microphone,
        profile=profile,
        preset=preset,
    )

    print(channel)


if __name__ == "__main__":
    main()