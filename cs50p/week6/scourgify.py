import csv, sys


def main():
    input_filename, output_filename = get_filename()
    students = []
    try:
        with open(input_filename, "r", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                last_name, first_name = row["name"].split(",")
                first_name = first_name.strip()
                house = row["house"]
                student = {
                    "first": first_name,
                    "last": last_name,
                    "house": house
                }
                students.append(student)

        with open(output_filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_filename}")


def get_filename():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    if not input_filename.endswith("csv") or not output_filename.endswith("csv"):
        sys.exit("Can read or write CSV file only.")
    return input_filename, output_filename


main()