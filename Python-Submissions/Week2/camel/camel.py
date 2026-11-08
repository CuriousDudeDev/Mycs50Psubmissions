camelCase = input('camelCase: ')
snake_case = ''
for i in camelCase:
    snake_case += (i) if i.islower() else (f'_{i.lower()}') if i.isupper() else ''
print(f'snake_case: {snake_case}')
