easy = input('File name: ')
if easy.endswith('.gif'):
    print('image/gif')
elif easy.endswith('.jpg') or easy.endswith('.jpge'):
    print('image/jpge')
else:
    print('application/octet-stream')