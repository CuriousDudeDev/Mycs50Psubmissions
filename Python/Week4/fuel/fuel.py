while True:
    fraction = input('Enter the fraction: ')
    nums = fraction.split('/')
    try:
        num1 = int[nums[0]]
    except ValueError:
        pass
    try:
        num2 = int[nums[1]]
    except ValueError:
        pass
    if num1 > num2:
        pass
    try:
        num1 / num2
    except ZeroDivisionError:
        pass
    print('num1/num2*100'+'%')

