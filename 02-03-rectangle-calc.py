print("Welcome to the Area and Perimeter Calculator")

choice = "y"
while choice.lower() == "y":
    length = float(input("Enter length "))
    width = float(input("Enter width "))
    print(f'Area: {width*length}')
    print(f'Perimeter: {(width*2)+(length*2)}')
    choice = input("Continue? y/n: ")

    