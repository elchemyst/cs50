import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(html):
    # Note that * and + are “greedy,” insofar as “they match as much text as possible."
    # Adding ? immediately after either, a la *? or +?, “makes it perform the match in non-greedy or
    # minimal fashion; as few characters as possible will be matched.”
    pattern = r'https?://(?:www.)?(youtu)(be).com/embed(/.*?)"'
    if matches:= re.search(pattern, html):
        url = "https://" + matches.group(1) + "." + matches.group(2) + matches.group(3)
        return(url)
    else:
        return None


if __name__ == "__main__":
    main()