import sys
import os

linelist = []


def main():
    lines_to_list(sys_check(sys.argv))
    print(len(linelist))


def sys_check(path):
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments.")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Incorrect extension (.py).")
    elif os.path.exists(sys.argv[1]) == False:
        sys.exit("File does not exist.")
    else:
        return sys.argv[1]


def lines_to_list(path):
    with open(path) as file:
        for i in file.readlines():
            if i.strip().startswith("#"):
                continue
            elif i == "\n":
                continue
            elif len(i.strip()) < 1:
                continue
            else:
                linelist.append(i)


if __name__ == "__main__":
    main()
