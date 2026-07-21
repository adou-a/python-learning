#把月日年转化成年月日
#提问用户日期
#判断是否符合格式
#如果不符重新提问日期
#符合即转化为年月日用连字符链接，2位小数在补0
while True:
    try:
        revise = input('Date: ')
#格式 月/日/年份 or 英文月+数字日，年份
        x,y,z = revise.split('/')   

        x = int(x)
        y = int(y)
        
    except ValueError:
        pass
    try:
        revise = revise.replace(',',' ')
        x,y,z = revise.split(',')
    except ValueError:
        continue
    
    if not 0 < x < 12 or not 0 < y < 31 :
        continue
    else:
        break


print(f'{z}''-'f'{x:02}''-'f'{y:02}')

