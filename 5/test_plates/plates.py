import re

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        start_two_letters(s)
        and plate_size(s)
        and number_position(s)
        and zero_position(s)
        and punctuation_marks(s)
    ):
        return True
    else:
        return False

def start_two_letters(s):
    count = 0
    plate = s
    for cha in plate:
        if count < 2:
            if cha.isalpha() == False and plate.index(cha) < 2:
                return False
        count += 1
        if count >= 2:
            return True


def plate_size(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True


def zero_position(s):
    while True:
        if s[2].isalpha() == False:
            if s[2] == "0":
                return False
            else:
                return True
        elif s[3].isalpha() == False:
            if s[3] == "0" and s[2].isalpha():
                return False
            else:
                return True
        try:
            if s[4].isalpha() == False:
                if s[4] == "0" and s[3].isalpha():
                    return False
                else:
                    return True
        except IndexError:
            return True

        else:
            return True


def number_position(s):  # comeback here and redo using a loop and sliced strings
    plate = s
    if len(plate) == 4:
        if plate[2].isalpha() == False:
            if plate[3].isalpha():
                return False
            else:
                return True
        else:
            return True
    elif len(plate) == 5:
        if plate[2].isalpha() == False:
            if plate[3].isalpha() == False and plate[4].isalpha() == False:
                return True
            else:
                return False
        elif plate[3].isalpha() == False:
            if plate[4].isalpha() == False:
                return True
            else:
                return False
    elif len(plate) == 6:
        if plate[2].isalpha() == False:
            if (
                plate[3].isalpha() == False
                and plate[4].isalpha() == False
                and plate[5].isalpha() == False
            ):
                return True
            else:
                return False
        elif plate[3].isalpha() == False:
            if plate[4].isalpha() == False and plate[5].isalpha() == False:
                return True
            else:
                return False
        elif plate[4].isalpha() == False:
            if plate[5].isalpha() == False:
                return True
            else:
                return False
        else:
            return True


def punctuation_marks(s):
    plate = s
    if bool(re.search(r"[!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~]", plate)):
        return False
    else:
        return True


if __name__ == "__main__":
    main()
