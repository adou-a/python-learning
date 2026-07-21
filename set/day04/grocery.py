#记录超市购买清单
#一直提示输入，直到遇到contro + d
#统计每一个输入，一样的数量相加，只有一个就是1
#输入 左边是数字空格加东西
order ={}
while True:
    try:
        food = input('')
    except EOFError:
        break
    if food in order:
        order[food] =order[food] + 1
    else:
        order[food] = 1


for food in order:
    print(order[food],food)
