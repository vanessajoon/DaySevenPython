# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for count in range(x):
        output += '*'
    print(output)
