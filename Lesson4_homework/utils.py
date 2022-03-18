from requests import get
import datetime


def finding(cur, text, value):
    rate = text[text.find(cur):]
    rate = rate.split(f'</{value}>')[0]
    rate = rate.split(f'<{value}>')[-1]
    rate = float(rate.replace(',', '.', 1))
    return rate


def currency_rates(cur):
    cur = cur.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    contains = response.text
    if contains.find(cur) == -1:
        print('Неверный идентификатор валюты')
        return None
    else:
        nominal = finding(cur, contains, 'Nominal')
        rate = finding(cur, contains, 'Value')
        date = datetime.datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
        print(f"\n{int(nominal)} {cur} = {rate} RUB\n\n {datetime.datetime.strftime(date, '%d %B %Y')}")
        return rate, date


if __name__ == '__main__':
    cur = input('Курс какой валюты вы хотите узнать? ')
    currency_rates(cur)
