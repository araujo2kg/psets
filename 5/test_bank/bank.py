def main():
    print(value(input("Hello there! ")))


def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting[0:5]:
        return 0
    elif "h" in greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
