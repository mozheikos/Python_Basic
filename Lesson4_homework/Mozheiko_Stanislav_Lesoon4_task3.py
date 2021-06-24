from requests import get
import datetime


def finding(cur, text, value):
    rate = text[text.find(cur):]
    rate = rate.split(f'</{value}>')[0]
    rate = rate.split(f'<{value}>')[-1]
    rate = float(rate.replace(',', '.', 1))
    return rate


def currency_rates(cur):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    contains = response.text
    if contains.find(cur) == -1:
        rate = None
        nominal = None
    else:
        nominal = finding(cur, contains, 'Nominal')
        rate = finding(cur, contains, 'Value')
    date = datetime.datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    return rate, date, nominal


cur = input('Курс какой валюты вы хотите узнать? ').upper()
rate, date, nominal = currency_rates(cur)
if rate:
    print(f"\n{int(nominal)} {cur} = {rate} RUB\n\n {datetime.datetime.strftime(date, '%d %B %Y')}")
else:
    print('Неверный идентификатор валюты')