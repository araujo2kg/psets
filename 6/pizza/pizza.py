import sys
import os
import csv
from tabulate import tabulate


def main():
    print(tabulate_file(sys_check(sys.argv)))


def sys_check(path):
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments.")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Incorrect extension (.csv).")
    elif os.path.exists(sys.argv[1]) == False:
        sys.exit("File does not exist.")
    else:
        return sys.argv[1]


def tabulate_file(file):
    with open(file) as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
        return tabulate(rows, tablefmt="grid", headers="firstrow")


if __name__ == "__main__":
    main()
