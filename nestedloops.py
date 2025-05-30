# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     output = ''
#     for count in range(x):
#         output += '*'
#     print(output)


# nums = [4, 10, 3, 7]
# target = 13
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i, j])

#print all pairs
# nums = [1, 2, 3]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         print(nums[i], nums[j])

#print pairs with different indexes
# nums = [4, 5, 6]
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         print(nums[i], nums[j])

#print pairs with different indexes in reverse
# nums = [4, 5, 6]
# for i in range(len(nums)):
#     for j in range(i):
#         print(nums[i], nums[j])

#multiplication table
# for i in range(1, 6):
#     for j in range(1, 13):
#         output = i * j
#         print(f'{i} * {j} = {output}')

 # multiplication 5 table
# num = [5]
# for i in range(len(num)):
#     for j in range(1, 13):
#         output =num[i] * j
#         print(f'{num[i]} * {j} = {output}')

#duplicates
# nums = [3, 5, 3, 8]
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j]:
#             print(f'Duplicates found: {nums [i]}  at position {i}, {j}')

#triangle
# for i in range(5, 0, -1):
#     output = ''
#     for j in range( i ):
#         output += '*'
#     print(output)

#l
num = [1, 1, 1, 5]
for i in num:
    output = ''
    for j in range(i):
        output += '*'
    print(output)