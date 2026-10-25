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
print(float(num1)*float(num2) if sign == '*' else float(num1)+float(num2) if sign =='+' else float(num1)/float(num2) if sign == '/' else float(num1)-float(num2) if sign =='-' else () )

