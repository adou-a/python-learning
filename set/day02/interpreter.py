expression = input('Expression: ')
x,y,z = expression.split(' ')
x = float(x)
z = float(z)
if y =='+':
    print(x+z)
elif y =='-':
    print(x-z)
elif y =='*':
    print(x*z)
elif y =='/':
    print(f'{(x/z):.1f}')
else:
    print('No y')
    