from datetime import date, timedelta
import inflect
import re
import sys


class Person:
    def __init__(self):
        self.bday = Person.get()

    @classmethod
    def get(cls, message="Date of Birth: "):
        bday = input(message)
        # Implement proper datetime validation
        try:
            bday = date.fromisoformat(bday)
        except Exception:
            sys.exit("Invalid")

        return bday

    def mins(self):
        today = date.today()
        days = today - self.bday
        days = str(days)
        days = int(days.split(" ")[0])
        mins = days * 24 * 60
        p = inflect.engine()
        words = f"{p.number_to_words(mins)} minutes"
        words = str(words)
        words = words.replace(" and", "")
        return words.capitalize()

    # def __str__(self):
    #     return self.mins()


def main():
    person = Person()
    print (person.mins(), end="")

...


if __name__ == "__main__":
    main()