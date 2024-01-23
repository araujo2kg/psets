import re
import sys

AM = {
    "12": "00:",
    "1": "01:",
    "2": "02:",
    "3": "03:",
    "4": "04:",
    "5": "05:",
    "6": "06:",
    "7": "07:",
    "8": "08:",
    "9": "09:",
    "10": "10:",
    "11": "11:",
}

PM = {
    "12": "12:",
    "1": "13:",
    "2": "14:",
    "3": "15:",
    "4": "16:",
    "5": "17:",
    "6": "18:",
    "7": "19:",
    "8": "20:",
    "9": "21:",
    "10": "22:",
    "11": "23:",
    "12": "12:",
}


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.fullmatch(
        r"^(1?[0-9](?:\:[0-5][0-9])?) (AM|PM) to (1?[0-9](?:\:[0-5][0-9])?) (AM|PM)$",
        s,
    ):
        hour1, period1, hour2, period2 = (
            hours.group(1),
            hours.group(2),
            hours.group(3),
            hours.group(4),
        )
        if ":" in hour1 and ":" in hour2:
            hour1, hour2 = hour1.split(":")[0], hour2.split(":")[0]
        if len(hours.group(1)) > 2:
            if period1 == "AM":
                hour1 = AM.get(hour1) + hours.group(1)[-2:]
            else:
                hour1 = PM.get(hour1) + hours.group(1)[-2:]
            if period2 == "AM":
                hour2 = AM.get(hour2) + hours.group(3)[-2:]
            else:
                hour2 = PM.get(hour2) + hours.group(3)[-2:]
        else:
            if period1 == "AM":
                hour1 = AM.get(hour1) + "00"
            else:
                hour1 = PM.get(hour1) + "00"
            if period2 == "AM":
                hour2 = AM.get(hour2) + "00"
            else:
                hour2 = PM.get(hour2) + "00"
        return f"{hour1} to {hour2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
