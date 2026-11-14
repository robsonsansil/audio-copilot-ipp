from dataclasses import dataclass


@dataclass
class Preacher:
    """
    Representa um pregador da igreja.
    """

    person_name: str
    title: str
    active: bool = True

    def __str__(self):
        return f"{self.person_name} ({self.title})"


def main():
    preacher = Preacher(
        person_name="Pastor Marcelo",
        title="Pastor"
    )

    print(preacher)


if __name__ == "__main__":
    main()