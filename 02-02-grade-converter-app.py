print("Welcome to the Grade converter")
choice = "y"
while choice == "y":
    nbrGrade = int(input("Enter number grade: "))

    letterGrade = "F"

    if nbrGrade >= 90:
        letterGrade = "A"
    elif nbrGrade >= 80:
        letterGrade = "B"
    elif nbrGrade >= 70:
        letterGrade = "C"
    elif nbrGrade >= 60:
        letterGrade = "D"

    print("Letter grade is: " + letterGrade)
    choice = input("Do you want to continue? (y/n): ")