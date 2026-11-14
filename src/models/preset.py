from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Preset:
    """
    Representa um preset de configuração da mesa.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    gain: int = 0
    hpf: int = 0
    compressor: bool = False

    active: bool = True

    def __str__(self):
        return (
            f"{self.name} "
            f"(Gain={self.gain}, "
            f"HPF={self.hpf}, "
            f"Compressor={'ON' if self.compressor else 'OFF'})"
        )


def main():
    preset = Preset(
        name="Violão Martin",
        gain=24,
        hpf=80,
        compressor=True,
    )

    print(preset)


if __name__ == "__main__":
    main()