class Data:

    @classmethod
    def modify(cls, date_):
        result = list(map(int, date_.split('-')))
        if cls.date_valid(result):
            return {'day': result[0], 'month': result[1], 'year': result[2]}

    @staticmethod
    def date_valid(date_r):
        valid_data = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day, month, year = date_r
        valid_data[2] = 29 if (abs(2020 - year)) % 4 == 0 else 28
        if month not in valid_data.keys():
            print('Date not valid: check month number')
            return False
        elif day not in range(1, valid_data[month] + 1):
            print('Date not valid: check day number')
            return False
        else:
            return True


print(Data.modify('27-02-2015'))
data = Data()
print(data.modify('10-19-2015'))

