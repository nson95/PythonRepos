print("Welcome to the Guess the Number Game")
print("++++++++++++++++++++++++++++++++++++")

choice = "y"
while choice == "y":
    while not userNbr:
        try:
            userNbr = int(input("I'm thinking of a number between 1 to 100.\nTry to guess it."))
        except ValueError:
            print("Error, entry must be an integer")
    if (userNbr<1 or userNbr>100):
        print("Error, entry must be between 1 and 100")
        userNbr = int(input("Enter a number between 1 and 100"))
        import random as randy
        secretNbr = randy.randint(1, 101)
        if userNbr-secretNbr>10:
            print("Way too high!")
        elif secretNbr-userNbr>10:
            print("Way too low!")
        elif userNbr-secretNbr>1:
            print("Too high!")
        elif secretNbr-userNbr>1:
            print("Too low!")
        else:
            print("Congrats!")
        choice = input("Continue? y/n: ")
