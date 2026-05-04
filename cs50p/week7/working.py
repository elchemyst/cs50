import re


def main():
    print(convert(input("Hours: ")), end="")


def convert(s):
    start = r"^(?P<start_hr>(1[0-2]|0?\d))(?P<start_min>(:[0-5][0-9]))?(?P<start_meri>(?: (AM|PM))) to (?P<end_hr>(1[0-2]|0?\d))(?P<end_min>(:[0-5][0-9]))?(?P<end_meri>(?: (AM|PM)))$"
    if matches:= re.search(start, s):
        start_hr = matches.group("start_hr")
        start_min = matches.group("start_min")
        start_meri = matches.group("start_meri").strip()
        end_hr = matches.group("end_hr")
        end_min = matches.group("end_min")
        end_meri = matches.group("end_meri").strip()
        return(to_24(start_hr, start_min, start_meri, end_hr, end_min, end_meri))
    else:
        raise ValueError


def to_24(start_hr, start_min, start_meri, end_hr, end_min, end_meri):
        if start_meri == "PM" and start_hr != "12":
            start_hr = str(int(start_hr) + 12)
        if start_hr == "12":
            if start_meri == "AM":
                start_hr = "00"
            if start_meri == "PM":
                start_hr = "12"
        if len(start_hr) < 2:
            start_hr = "0" + start_hr
        if start_min:
            start_24 = start_hr + start_min
        else:
            start_24 = start_hr + ":00"

        if end_meri == "PM" and end_hr != "12":
            end_hr = str(int(end_hr) + 12)
        if end_hr == "12":
            if end_meri == "AM":
                end_hr = "00"
            if end_meri == "PM":
                end_hr = "12"
        if len(end_hr) < 2:
            end_hr = "0" + end_hr
        if end_min:
            end_24 = end_hr + end_min
        else:
            end_24 = end_hr + ":00"

        return (f"{start_24} to {end_24}")


if __name__ == "__main__":
    main()