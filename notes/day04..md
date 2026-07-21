#while True
重复执行命令行

#try
里面放可能出错的代码

#except +错误类型：
    出错后的处理
第一个类型 VauleError 值错误
第二个类型 zerodivisionerror 除数为0错误

break 跳出当前循环

return 
结束了当前函数
把函数结果交还给调用它的地方
只能在定义函数中使用
可返还多个结果

pass
占位符不处理结果
不跳过错误也不重新循环

缩进与不缩进
tab
shift + tab


while True:
    try:#捕捉错误
        number = input('Fraction：')
        x,y = number.split('/')
        x = int(x)
        y = int(y)

    except ValueError:#负责处理错误
        continue

    if x > y or x < 0 or y <= 0 :#负责判断条件
        continue
    
    z = round((x/y)*100)
    break#负责跳出循环
if z >= 99:
    print('F')
elif z <= 1:
    print('E') 
else:
    print(f'{z}%')



except EOFError:
表示键盘终止control +c

表示需要的小数方法 :.
如 m 变量的 2位小数
m:.2f

如何放进list  []
names = []
names.append(想要加入的)

dicitionary {}
关键有key  有value


index
months = []
months.index(month)
查找month在index上的位置

split()
按空格切 不看空格数量


字符串自动补0
print（f‘{number：02}’）
0 表示不足的地方用0补齐
2表示总宽度至少为2