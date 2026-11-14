from dataclasses import dataclass


@dataclass
class Instrument:
    """
    Representa um instrumento utilizado na igreja.
    """

    name: str
    category: str
    output_type: str
    phantom_power: bool = False
    active: bool = True

    def __str__(self):
        return f"{self.name} ({self.category})"


def main():
    instrument = Instrument(
        name="Violão Martin",
        category="Violão",
        output_type="DI Box",
        phantom_power=False
    )

    print(instrument)


if __name__ == "__main__":
    main()