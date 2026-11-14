from dataclasses import dataclass


@dataclass
class Microphone:
    """
    Representa um microfone da igreja.
    """

    name: str
    type: str
    color: str = ""
    phantom_power: bool = False
    wireless: bool = False
    active: bool = True

    def __str__(self):
        description = self.name

        if self.color:
            description += f" ({self.color})"

        return description


def main():
    microphone = Microphone(
        name="Shure SM58",
        type="Dinâmico",
        color="Azul",
        wireless=False,
        phantom_power=False
    )

    print(microphone)


if __name__ == "__main__":
    main()