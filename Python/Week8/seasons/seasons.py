from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    given = input('Enter your birth date: ')
    pattern = re.search(r'(\d{4})-(\d{2})-(\d{2})' , given)
    if pattern:
        var1 = song(given , date.today().strftime("%Y-%m-%d"))
        print(var1.convert())
    else:
        sys.exit('Invalid Date')


class song:
    def __init__(self ,birthday , today):
        self.today = today
        self.birthday = birthday

    def convert(self):
        splitted_today =self.today.split('-')
        splitted_birthday = self.birthday.split('-')
        today_year = int(splitted_today[0])
        today_month = int(splitted_today[1])
        today_date = int(splitted_today[2])
        birthday_year = int(splitted_birthday[0])
        birthday_month = int(splitted_birthday[1])
        birthday_date = int(splitted_birthday[2])
        d_today = date(today_year , today_month , today_date)
        d_birthday = date(birthday_year , birthday_month , birthday_date)
        days_to_today = d_today.toordinal()
        days_to_birthday = d_birthday.toordinal()
        if days_to_today < days_to_birthday:
            raise ValueError('Invalid')
        between_days = days_to_today - days_to_birthday
        minutes = between_days * 24 * 60
        minutes_in_words = p.number_to_words(minutes).replace(' and ' , ' , ').capitalze()
        return f"{minutes_in_words} minutes"





if __name__ == "__main__":
    main()
