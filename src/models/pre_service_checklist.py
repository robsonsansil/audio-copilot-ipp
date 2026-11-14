"""
Representa o checklist pré-culto.
"""

from dataclasses import dataclass, field
from uuid import uuid4

from src.models.event import Event


@dataclass
class PreServiceChecklist:
    """
    Representa o checklist realizado antes do início do evento.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    event: Event | None = None

    mixer_connected: bool = False
    channels_checked: bool = False
    microphones_checked: bool = False
    monitors_checked: bool = False
    instruments_checked: bool = False
    scenes_loaded: bool = False
    presets_loaded: bool = False

    notes: str = ""

    active: bool = True

    @property
    def completed(self) -> bool:
        """
        Retorna True quando todos os itens do checklist foram concluídos.
        """
        return all([
            self.mixer_connected,
            self.channels_checked,
            self.microphones_checked,
            self.monitors_checked,
            self.instruments_checked,
            self.scenes_loaded,
            self.presets_loaded,
        ])

    def __str__(self):

        event_name = (
            self.event.programming.name
            if self.event and self.event.programming
            else "Sem evento"
        )

        status = (
            "Pronto para o culto"
            if self.completed
            else "Checklist pendente"
        )

        return f"{event_name} - {status}"


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

    checklist = PreServiceChecklist(
        event=event,
        mixer_connected=True,
        channels_checked=True,
        microphones_checked=True,
        monitors_checked=True,
        instruments_checked=True,
        scenes_loaded=True,
        presets_loaded=True,
    )

    print(checklist)


if __name__ == "__main__":
    main()