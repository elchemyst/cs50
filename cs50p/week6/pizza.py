import csv, sys
from tabulate import tabulate


def main():
    pizzas = []
    filename = get_filename()
    try:
        with open(filename, "r") as file:
            pizzas_csv = csv.reader(file)
            pizzas = list(pizzas_csv)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))


def get_filename():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    extension = filename.split(".", 1)[-1]
    if not extension.endswith("csv"):
        sys.exit("Not a CSV file")
    return filename


main()