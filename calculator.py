while True:
    print('To calculate numbers, choose your operator')
    print('+, *, -, /, square root, square')
    operator = input('Enter the operator ').lower()

    if operator == 'square root':
        num = float(input('Enter a number to find the square root '))
        total = num ** 0.5
        print(f'The square root of {num} = {total}')
        continue
    elif operator == 'square':
        num = float(input('Enter a number to calculate the square of it '))
        total = num ** 2
        print(f'The square of {num} = {total}')
        continue
    else:
        num1 = float(input('Enter first number '))
        num2 = float(input('Enter second number '))


    if operator == '+':
        total = num1 + num2
        print(f'The sum of {num1} + {num2} = {total}')
    elif operator == '-':
        total = num1 - num2
        print(f'The subtraction of {num1} - {num2} = {total}')
    elif operator == '*':
        total = num1 * num2
        print(f'The multiplication of {num1} * {num2} = {total}')
    elif operator == '/':
        if num2 != 0:
            total = num1 / num2
            print(f'The division of {num1} / {num2} = {total}')
        else:
            print('Invalid operation, zero cannot divide a number')
            continue

    else:
        print('INVALID OPERATION')

    again = input('Do you want to calculate again "yes/no"').lower()

    if again != 'yes':
        print('Operation Terminated')
        break