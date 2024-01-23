def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dol = d
    dol = dol.removeprefix("$")
    dol = float(dol)
    return dol


def percent_to_float(p):
    pct = p
    pct = pct.removesuffix("%")
    pct = float(pct)
    pct = pct/100
    return pct

main()
