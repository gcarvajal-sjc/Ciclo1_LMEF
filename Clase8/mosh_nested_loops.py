# Generate a list of coordenates for (x,y)

# for x in range(4): #outer loop
#     for y in range(3): # inner loop
#         print(f'({x},{y})')

# Using nested loops use nested loops to draw an 'F'. Basically convert a list of
#  numbers into a drawing.
# TIP: Using a for loop we need to iterate over the list. In each iteration we get
# one number which shows how many 'X's we need on each line. We need to generate an
# inner loop that generates 5 Xs

from re import X
from xxlimited import Xxo
from numpy import append


numbers = [5, 2, 5, 2, 2]

# for item in range(len(numbers)):
#     for number in numbers:
#         print('X'*number)

for item in numbers:
    output = ''
    for number in range(item):
        output += 'X'
    print(output)

print('')

letraEle = [1, 1, 1, 1, 6]

for item in letraEle:
    output = ''
    for number in range(item):
        output += 'X'
    print(output)
