import sys
import requests


def bit_float():
    try:
        bit = float(sys.argv[1])
    except ValueError:
        sys.exit("Invalid bitcoin value")
    except IndexError:
        sys.exit("No bitcoin value")
    return bit


r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r = r.json().get("bpi").get("USD").get("rate_float")

total = bit_float() * r
print(f"${total:,.4f}")
