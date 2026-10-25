original = input('Input: ')
new = ''
for i in original:
    new += '' if i in ['a' , 'e' , 'i' , 'o' , 'u'] else i
print(new)
