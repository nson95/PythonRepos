print("Welcome to the factorial calculator")
choice = "y"
while choice == "y":
    nbr = int(input("Enter an integer that's greater than 0 and less than 10: "))
    fact = 1
    for n in range(1, nbr+1):
        fact*=n
    print(f'Factorial of {nbr} is {fact}')
    choice = input("Continue? y/n: ")