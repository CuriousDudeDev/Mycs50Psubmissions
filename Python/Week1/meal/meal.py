def main():
    time = input('Enter the current time: ')
    total = convert(time)
    if 7 <= total <= 8:
        print('Breakfast time')
    elif 12 <= total <= 13:
        print('Lunch Time')
    elif 18 <= total <= 19:
        print('Dinner time')


def convert(time):
    hours_and_mins = time.split(':')
    hours = int(hours_and_mins[0])
    if time.endswith('pm'):
        hours += 12
    elif time.endswith('am'):
        pass
    else:
        return 'Invalid format'
    minutes = float(int(hours_and_mins[1])/60)
    total = hours + minutes
    return total



if __name__ == "__main__":
    main()
