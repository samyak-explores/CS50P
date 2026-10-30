Amt = 50
print(f"Amount Due: {Amt}\n")


while Amt <= 50:
    coin_in = int(input(f"Insert Coin: "))

    if coin_in == 25 or coin_in == 10 or coin_in == 5:
        Amt = Amt - coin_in
        if Amt <= 0:
            owed = abs(Amt)
            print(f"Change Owed: {owed}")
            break
        else:
            print(f"Amount Due: {Amt}")

    else:
        print(f"Amount Due: {Amt}")
        #Machine only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

print()
