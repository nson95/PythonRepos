even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,7,9]
# add value at end

even_numbers.append(12)
#add value at index position
odd_numbers.insert(2, 5)
print(f'even nums:  {even_numbers}')
print(f'oddS nums:  {odd_numbers}')

numbers =[1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers)):
    print(f'{i}: {numbers[i]}')


#iterate by 2
for i in range(0, 10, 2):
    print(f'{i} : {numbers[i]}', end = ", ")
print()
# iterate over numbers using enumerate so we can get index too
for idx, value in enumerate(numbers) :
    print(f'{idx}, {value}')