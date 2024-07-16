from cs50 import get_float

while True:
    m = get_float("Change: ")
    if m > 0:
        break

m = int(m * 100)
coins = 0
for i in [25, 10, 5, 1]:
    coins += m // i
    m %= i
print(coins)
