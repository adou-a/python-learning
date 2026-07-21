#打印菜单
#获取用户输入
#判断是否在菜单上
#在的话计入金额
#不在重新获取用户输入
#新输入
#判断是否在，记住并加在一起
#不在请求输入
#打印加在一起的值并且在获取输入
print(' "Baja Taco": 4.25\n',
    '"Burrito": 7.50\n',
    '"Bowl": 8.50\n',
    '"Nachos": 11.00\n',
    '"Quesadilla": 8.50\n',
    '"Super Burrito": 8.50\n',
    '"Super Quesadilla": 9.50\n',
    '"Taco": 3.00\n',
    '"Tortilla Salad": 8.00'
      )
item  = {"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito":8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
m = 0
while True:
    try:
        food = input('Item: ')
    except EOFError:
        break
    if food in item:
        money = (item[food])

    else:
        continue
    m = m + money
    print(f'Item:{m:.2f}')


