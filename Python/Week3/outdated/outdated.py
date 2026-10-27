months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input('Date: ')
    if '/' in date:
        date = date.split('/')
        try:
            int(date[0])
        except ValueError:
            pass
        else:
            if 1 <= int(date[0]) <= 12 and 1<=int(date[1])<=31:
                print(f'{date[2].strip()}-{int(date[0].strip()):02}-{int(date[1].strip()):02}')
                break
    if ',' in date:
        date = date.split(',')
        year = date[1]
        year = year.strip()
        month_date = date[0]
        month_date = month_date.strip()
        month_date = month_date.split(' ')
        month = month_date[0]
        date = month_date[1]
        if month in months and int(date) <=31:
            print(f"{year.strip()}-{months.index(month)+1:02}-{int(date.strip()):02}")
            break


