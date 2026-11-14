from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Mixer:
    """
    Representa uma mesa de som cadastrada no sistema.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""
    manufacturer: str = ""
    model: str = ""
    firmware: str = ""

    ip_address: str = ""
    websocket_port: int = 80

    channels: int = 0
    aux_outputs: int = 0
    fx_engines: int = 0

    active: bool = True

    def __str__(self):
        return (
            f"{self.manufacturer} "
            f"{self.model} "
            f"({self.ip_address})"
        )


def main():
    mixer = Mixer(
        name="Mesa Principal",
        manufacturer="Soundcraft",
        model="Ui24R",
        firmware="3.6",
        ip_address="10.10.2.1",
        websocket_port=80,
        channels=24,
        aux_outputs=10,
        fx_engines=4,
    )

    print(mixer)


if __name__ == "__main__":
    main()