# 31 536 000 - количество секунд в году
# т.к. месяцы в году имею разное количество дней, 60*  60 * 24 * 30 - будет не совсем точно,
# я взял 60 * 60 * 24 * 365 / 12 = 2 628 000
time = []

# функция для корректного склонения слова "год"


def decline(x):
    if x % 10 == 1 and x % 100 != 11:
        d = " год "
    elif x % 10 in range(2, 5, 1) and not x % 100 in range(11, 15, 1):
        d = " года "
    else:
        d = ' лет '
    return d


duration = int(input('Введите количество секунд: '))

years = duration // 31536000
duration = duration % 31536000
time.append(years)

months = duration // 2628000
duration = duration % 2628000
time.append(months)

days = duration // 86400
duration = duration % 86400
time.append(days)

hours = duration // 3600
duration = duration % 3600
time.append(hours)

minutes = duration // 60
duration = duration % 60
time.append(minutes)

seconds = duration
time.append(seconds)

des = [" ", " мес ", " дн ", " час ", " мин ", " сек "]
des[0] = decline(years)
s = ''
i = 0
while i < len(time):
    if time[i] != 0:
        s = s + str(time[i]) + des[i]
    i = i + 1

print(s)
