# Take input for operand
Num1 = input('Enter The First Number: ')
Operator = input('Enter The  Operator: ')
Num2 = input('Enter The Second Number: ')


# lets print the type of the variables
#print(type(Num1), type(Num2))

# Converting the type of variables
Num1 = int(Num1)
Num2 = int(Num2)

# lets print type of the variables
#print(type(Num1), type(Num2))

#lets check the operator first
result = ''
if Operator == '+':
  result = Num1 + Num2
elif Operator == '-':
  result = Num1 - Num2
elif Operator == '*':
  result = Num1 * Num2 
elif Operator == '/':
  result = Num1 / Num2 
else:
  result = 'Not Defined'

#lets print it

print('The Result Is : ', result)
