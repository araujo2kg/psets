import sys
import re
import datetime
import inflect

p = inflect.engine()


class Birth:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_age_minutes(self):
        birth = datetime.date(self.year, self.month, self.day)
        today = datetime.date.today()
        age = today - birth
        return age.days * 24 * 60

    @classmethod
    def get_date(cls):
        date = input("Date of Birth: ")
        if birth := re.fullmatch(r"^(\d{4})-(\d{2})-(\d{2})$", date):
            year, month, day = (
                int(birth.group(1)),
                int(birth.group(2)),
                int(birth.group(3)),
            )
            if not 1900 < year < 2024:
                sys.exit("Invalid date")
            if not 1 <= month <= 12:
                sys.exit("Invalid date")
            if not 1 <= day <= 31:
                sys.exit("Invalid date")
        else:
            sys.exit("Invalid date")
        return Birth(year, month, day)

    def sing(self):
        return (
            p.number_to_words(self.get_age_minutes()).replace(" and", "") + " minutes"
        ).capitalize()

    def __eq__(self, other):
        if isinstance(other, Birth):
            return (
                self.year == other.year
                and self.month == other.month
                and self.day == other.day
            )
        return False


def main():
    person = Birth.get_date()
    print(person.sing())


if __name__ == "__main__":
    main()
