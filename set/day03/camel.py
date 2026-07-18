#提示用户输入一个驼峰大小写
n = input('camelCase: ')
#需要做到在每个大写字母前面加上_并且把这个大写字母转化成小写字母
# 大写字母是识别的关键
# 先用for循环经历每一个字母
#找到其中所有的大写字母
#在每个大写字母前面加上_
for letter in n:
    if letter.isupper():
        print('_'+letter.lower(),end='')
    else:
        print(letter,end='')
