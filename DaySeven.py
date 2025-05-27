# lists = ['leg', 'beans', 'tea']
# for item in lists:
#     print(item)
from itertools import count

#Range is to print a range of something
# for item in range(10):
#     print(item)
# for item in range(5, 11, 2):
#     print(item)

#calculation in for loops
# price = [10, 20, 30]
# total=0
# for item in price:
#     total = total + item
# print(f'Total: {total}')

#multiplication table
# user = int(input('Enter a number to get the multiplication '))
# for items in range(1, 13):
#     total = user * items
#     print(f'{user} * {items} = {total}')


#Sum of numbers
# user = int(input('Enter a number to get the addition of it starting from 1'))
# total = 0
# for item in range(1, user + 1):
#     total = total + item
# print(f'The total sum from 1 to {user} is {total}')

# #even numbers
# for items in range(1, 51):
#     if items % 2 == 0:
#         print(items)

#triangle
# for items in range(1, 6):
#     print('*' * items)

#countdown
# for items in range(10, 0, -1):
#     print(items)
# print('Times up')

# #List of names
# food = []
# count = 5
# print('Enter 5 favourite food')
# for items in range(count):
#     name = input(f'Enter food {items + 1}: ')
#     food.append(name)
# print('Your favorite foods are:')
# for i in food:
#      print(f'- {i}')


#Scores for 5 student
count = 5
total = 0
print('Score of 5 students')
for items in range(count):
    score = int(input(f'Enter score for student {items + 1}: '))
    total = total + score
    average = total / 5
print(f'Total score is: {total}')
print(f'Average score is: {average}')

