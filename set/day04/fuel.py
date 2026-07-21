#这是一个燃油表，要求用户输入一个分数

#格式为x/ y x是非负整数，y是正整数
#打印出这个分数结果的百分数
#分开这三个数字

while True:
    try:
        number = input('Fraction：')
        x,y = number.split('/')
        x = int(x)
        y = int(y)

    except ValueError:
        continue

    if x > y or x < 0 or y <= 0 :
        continue
    
    z = round((x/y)*100)
    break
if z >= 99:
    print('F')
elif z <= 1:
    print('E') 
else:
    print(f'{z}%')







        

