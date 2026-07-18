#用户进行输入
n = input('Input: ')
#历经每一个字母
for letter in n:
#拼接所有非元音字母
    if letter in ['a','e','i','o','u']:
        print(end='')
    else:
        print(letter,end='')