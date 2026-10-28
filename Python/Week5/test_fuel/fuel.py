def main():
    expression = input()
    percent = convert(expression)
    print(gauge(percent))


def convert(fraction):
    nums = fraction.split('/')
    try:
        num1 = int(nums[0])
        num2 = int(nums[1])
    except IndexError:
        exit('Invalid expression')
    except ValueError:
        exit('Invalid Expression')
    try:
        fraction = num1/num2
    except ZeroDivisionError:
        exit('Division by zero is not supported')
    else:
        if num1 > num2:
            raise ValueError
        else:
            fraction = int(round(fraction))
            return fraction

def gauge(percentage):
    if percentage <1:
        return 'E'
    elif percentage > 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
