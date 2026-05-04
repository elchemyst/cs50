import sys


def main():
    filename = get_filename()
    try:
        with open(filename, "r") as file:
            text = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    line_count = count_lines(text)
    print(line_count)


def get_filename():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    extension = filename.split(".", 1)[-1]
    if extension != "py":
        sys.exit("Not a python file")
    return filename

def count_lines(text):
    line_count = 0
    for line in text:
        line = line.lstrip()
        if line and not line.startswith("#"):
            line_count += 1
    return line_count


if __name__ == "__main__":
    main()