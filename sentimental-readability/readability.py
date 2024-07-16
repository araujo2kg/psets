from cs50 import get_string


def main():
    txt = get_string("Text: ")

    letters = 0
    words = 1  # Start at 1 because the loop does not account for the last word.
    sentences = 0
    for c in txt:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            words += 1
        elif c in [".", "!", "?"]:
            sentences += 1

    # Average letters and sentences per 100 words
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Coleman-Liau index Formula
    index = int(round(0.0588 * L - 0.296 * S - 15.8))

    # Print result index as grade
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()
