# this is a comment

a = 5
b = 6
print(a + b) 

c = 8
d = 3

print(f'8/3 = {c/d}') # division
print(f'8//3 = {c//d}') #divides and rounds to whole number
print(f'8%3 = {c%d}') # modulus example

print('hello ', end = '') #typically enter will end the line. you an specify to end with a space instead
print('world')
print(a, b, c, d) 
print(a, b, c, d, sep='-') 
f_name = input('Enter your first name: ')
print(f_name)
price = float(input('Enter the price: '))
qty = int(input('Enter the quantity: '))
print(f'Total price: {qty*price}')

if (d <5):
    print('d is less than 5')
elif (d>5):
    print('d is greater than 5')
else:
    print('d is equal to 5')

if a+b > 10 and c+d > 10: # tabs are 4 spaces in python
    print('Both conditions are true')

choice = "y"
while choice == "y":
    print("Hello world")
    choice = input("Do you want to continue? (y/n): ").lower()

print("Buhbye")
