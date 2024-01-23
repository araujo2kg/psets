import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.fullmatch(
        r"^(1?[0-9](?:\:[0-5][0-9])?) (AM|PM) to (1?[0-9](?:\:[0-5][0-9])?) (AM|PM)$",
        s,
    ):



    else:
        raise ValueError


if __name__ == "__main__":
    main()
