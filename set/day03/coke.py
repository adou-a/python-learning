#可乐机提示钱
#自动交互，
#可乐价钱
#请求输入
#设定初始可乐价钱
coke = 50
#获取输入的值和初始价钱的差值
while coke > 0:
        print('Amount Due:',coke)
        n =int(input('Insert Coin: '))
        if n == 25 or n == 10 or n == 5:

            coke = coke - n

print('Changed Owed:',-coke)

  

        



#加入while 循环，使满足条件一直循环

   






