def main():
    while True:
        expression = input()
        try:
            percent = convert(expression)
        except ZeroDivisionError:
            continue
        except ValueError:
            continue
        else:
            print(gauge(percent))


def convert(fraction):
    num1 , num2 = fraction.split('/')
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        raise ZeroDivisionError
    if num2 < num1 or (num1 < 0) or (num2 < 0):
        raise ValueError
    return (round(100*num1/num2))

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
