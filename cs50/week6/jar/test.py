def main():
    jane = Student("Jane", 10)
    jane.print()
    jane.changeID(11)
    jane.print()


class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def changeID(self, id):
        self.id = id
    def print(self):
        print(f"{self.name} - {self.id}")


main()
