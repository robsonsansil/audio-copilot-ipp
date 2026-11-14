from dataclasses import dataclass


@dataclass
class Monitor:
    """
    Representa um retorno (monitor) da igreja.
    """

    name: str
    output: str
    location: str
    active: bool = True

    def __str__(self):
        return f"{self.name} ({self.location})"


def main():
    monitor = Monitor(
        name="Retorno 1",
        output="AUX 1",
        location="Palco"
    )

    print(monitor)


if __name__ == "__main__":
    main()