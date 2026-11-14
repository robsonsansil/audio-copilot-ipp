from dataclasses import dataclass


@dataclass
class SundaySchoolTeacher:
    """
    Representa um professor da Escola Bíblica Dominical.
    """

    person_name: str
    class_name: str
    active: bool = True

    def __str__(self):
        return f"{self.person_name} ({self.class_name})"


def main():
    teacher = SundaySchoolTeacher(
        person_name="Carlos",
        class_name="Adultos"
    )

    print(teacher)


if __name__ == "__main__":
    main()