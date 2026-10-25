camelCase = input('camelCase')
snake_case = ''
for i in camelCase:
    snake_case.append(i) if i.islower() else snake_case.append(f' {i.lower()}') if i.isupper()
