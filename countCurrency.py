"""
Q.4 WAP to print currency denomination table for an amount? Use list to store
denomination of currency notes and iterate loop to do the same.
"""


def countCurrency(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Currency Count for -> ", amount)
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)


amount = int(input("Enter Rupees : "))
countCurrency(amount)
