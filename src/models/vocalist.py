from dataclasses import dataclass


@dataclass
class Vocalist:
    """
    Representa um vocalista da igreja.
    """

    person_name: str
    voice_type: str
    active: bool = True

    def __str__(self):
        return f"{self.person_name} ({self.voice_type})"


def main():
    vocalist = Vocalist(
        person_name="Robson",
        voice_type="Barítono"
    )

    print(vocalist)


if __name__ == "__main__":
    main()