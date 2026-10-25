amount_given = 0
while amount_given < 50:
    print(f'Amount Due: {50 - amount_given}')
    insert = int(input('Insert Coin: '))
    amount_given += insert
    if amount_given >= 50:
        print(f'Change Owed: {amount_given - 50}')
