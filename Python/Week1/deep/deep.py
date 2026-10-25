answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
key = ['42' , 'forty-two' , 'forty two']
if answer.lower().strip() in key :
    print('Yes')
else:
    print('No')
