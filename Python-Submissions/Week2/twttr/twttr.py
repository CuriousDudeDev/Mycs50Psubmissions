original = input('Input: ')
new = ''
for i in original:
    new += '' if i.lower() in ['a' , 'e' , 'i' , 'o' , 'u'] else i
print(new)
