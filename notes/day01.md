创建与运行
Code    adou.py
Python  adou.py
查看上一次命令：上箭头⬆
变量
n = input（‘what is your name? '）
= 赋值 把右边的值赋值到左边

print
print(name)
print('hello,' + name)
print('hello,', name)
print('hello,',end=' ')
print(f'hello,{name}')




空格空四行：tab


strip 去除输入左右两边的空白
如：
Name = input(‘what is your name?’)
Name = name.strip()
title 每个字母都大写
如
Name = input(‘what is your name?’)
Name = name.title()
7. .函数名（）


int 把字符串变整数
Int(input(“give a number))
x = int(x)



float 把字符串变浮点数
float(input(‘ ‘))
x = float(x)


round 四舍五入
Round(number[,ndigits]) 数字，小数位数
Round(n,2)


f-string
Print(f’{n:.2f}’)  把n的结果四舍五入到2位小数


建立函数 def
Def 函数名（）：
如：
Def hello（）：
Def hello(n =’world’)  给变量设定默认值


return  返回结果
调用需要接受函数



lower  把字符串转化成小写
.lower()
replace 把什么替换成什么
replce(‘old’,’new’,-1)
不指定或指定为-1，只换第一个

Replce(‘A’,’B’)  把A换成B
平方
N*N
N**2