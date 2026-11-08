greet = input('Greeting: ')
if greet.strip().lower().startswith('hello'):
    print('$0')
elif greet.strip().lower().startswith('h'):
    print('$20')
else:
    print('$100')
