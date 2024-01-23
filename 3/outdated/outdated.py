import re

months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def date_input():
    while True:
        try:
            date = input("Date: ").strip()
            if re.match(r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$", date):
                return date
            elif re.match(r"[a-zA-Z]{5,15}\s[0-9]{1,2},\s[0-9]{4}$", date):
                return date
            else:
                continue
        except EOFError:
            print()
            break


def date_treatment():
    while True:
        try:
            date = date_input()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 < day > 31 or 1 < month > 12:
                    continue
                else:
                    print(f"{year}-{month:02}-{day:02}")
                break
            else:
                month, day, year = date.split(" ")
                day = int(day.replace(",", ""))
                year = int(year)
                if 1 < day > 31:
                    continue
                if month in months:
                    print(f"{year}-{months[month]:02}-{day:02}")
                    break
                else:
                    continue

        except EOFError:
            print("ok")


def main():
    date_treatment()


main()
