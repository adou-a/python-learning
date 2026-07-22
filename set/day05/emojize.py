import emoji 

answer = input('Input: ')
result = emoji.emojize(answer,language='alias')
print(f'Output: {result} ')