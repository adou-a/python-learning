#提示用户输入一个水果
n = input('Item: ').lower()
#把水果对应的热量打入dictionary中
fruits = {
    'apple':'130',
    'banana':'110',
    'avocado':'50',
    'sweet cherries':'100'
}
if n in fruits:
    print('Calories:',fruits[n])