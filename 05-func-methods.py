def add_function(num1, num2) :
    return (num1+num2)

print(add_function(4, 23))


def subtract_function(num1, num2=0):
    return num1-num2

print(subtract_function(56, 22))



def add(*nbrs):
    sum=0
    for n in nbrs:
        sum += n
    return sum

print(add(8, 25))

# keyword args

def calc_total_function(price, qty, handling_fee):
    return (price*qty) +handling_fee

print("Total: ",calc_total_function(20,2,3))

print("Total2: ", calc_total_function(handling_fee=5, qty=7, price = 10000000))
## may want to look up arbitrary keyword argument

#exceptions
while True:
    try:
        whole_number = int(input("Enter a whole number: "))
        (f'You entered the number: {whole_number}')
        break
    except ValueError:
        print("Invalid entry: ")
