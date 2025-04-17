

pi = 3.1415672


print(f'round pi: {round(pi)}')
print(f'round pi: {round(pi, 3)}')

import random as rand
print(f'random #: {rand.random()}' )
print(f'die roll: {rand.randint(1, 6)}')

price = 26789
price_currency = '${:,.2f}'.format(price)
print(f'price = {price_currency}')
grade = .9995
grade_pct_1 = format(grade, '%')
print(grade_pct_1)
grade_pct_2 = "{:.2%}".format(grade)
print(grade_pct_2)
print(f'Format % w/2 decimals: {grade:.2%}')