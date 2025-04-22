print("Tip Calculator")

choice = "y"

while choice == "y":
    cost = float(input("Cost of meal: "))
    print(f'\n15%\nTip amount: \t{(cost*.15):,.2f}\nTotal amount: \t{(cost+(cost*.15)):,.2f}\n20%\nTip amount: \t{(cost*.20):,.2f}\nTotal amount: \t{(cost+(cost*.20)):,.2f}')