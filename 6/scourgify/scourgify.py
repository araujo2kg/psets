import sys
import csv
import os


def main():
    reformat_file(sys_check(sys.argv))


def sys_check(path):
    if len(sys.argv) != 3:
        sys.exit("Incorrect number of arguments.")
    elif sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Incorrect extension (.csv).")
    elif os.path.exists(sys.argv[1]) == False:
        sys.exit("File does not exist.")
    else:
        return sys.argv


def reformat_file(files):
    with open(files[1]) as inputfile:
        reader = csv.DictReader(inputfile)
        list = []
        for row in reader:
            last, first = row["name"].split(",")
            house = row["house"]
            list.append({"first": first.strip(), "last": last, "house": house})

    with open(files[2], "w") as outputfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
