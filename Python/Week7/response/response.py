from validators import email

def main():
    print(valid(input('What is your email address? ')))

def valid(mail):
    validity = email(mail)
    if validity:
        return 'Valid'
    else:
        return 'Invalid'

main()
