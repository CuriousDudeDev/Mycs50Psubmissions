expression = input('Enter the expression: ')
expression.strip()
signs = ['+' , '-' , '*' , '/']
for i in expression:
    if i in signs:
        sign = i
        break
nums = expression.split(sign)
num1 = nums[0]
num2 = nums[1]
print(int(num1)*int(num2) if sign == '*' else int(num1)+int(num2) if sign =='+' else int(num1)/int(num2) if sign == '/' else int(num1)-int(num2) if sign =='-' else () )

