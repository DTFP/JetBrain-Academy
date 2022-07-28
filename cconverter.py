import requests

inverse_rate = {}
current_curreny = input()

r = requests.get(f'http://www.floatrates.com/daily/{current_curreny}.json')

if current_curreny.lower() == 'usd':
    inverse_rate['eur'] = r.json()['eur']['inverseRate']
elif current_curreny.lower() == 'eur':
    inverse_rate['usd'] = r.json()['usd']['inverseRate']
else:
    inverse_rate['usd'] = r.json()['usd']['inverseRate']
    inverse_rate['eur'] = r.json()['eur']['inverseRate']


while True:
    desired_currency = input()
    if desired_currency == '':
        break
    amount = float(input())
    print('Checking the cache...')
    if desired_currency in inverse_rate:
        print('Oh! It is in the cache!')
        print(f'You received {round(amount/inverse_rate[desired_currency], 2)} {desired_currency}.')
    else:
        print('Sorry, but it is not in the cache!')
        inverse_rate[desired_currency] = r.json()[desired_currency.lower()]['inverseRate']
        print(f'You received {round(amount/inverse_rate[desired_currency], 2)} {desired_currency}.')

