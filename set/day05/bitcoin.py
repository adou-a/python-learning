import requests
import sys
import json

if len(sys.argv) < 2 :
    sys.exit('Missing command-line argument')
try:
    amount = sys.argv[1]
    amount = float(amount)
except ValueError:
    sys.exit('Command-line argument is not a number')


try:
    response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=4c95f1849368f3d826998865b98141f7ff04a6d7d27cd4aa6acd4a41fc8dcab1')
    o  = response.json()
    price = o['data']['priceUsd']
    price = float(price)*amount
    print(f'{price:.4f}')
except requests.RequestException:
    sys.exit('No')




