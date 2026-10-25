while True:
    fraction = input('Enter the fraction: ')
    nums = fraction.split('/')
    try:
        num1 = int(nums[0])
        num2 = int(nums[1])
        num1/num2
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    else:
        if num1 > num2:
            pass
        else:
            print(str(num1/num2*100)+'%')


