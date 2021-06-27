# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = list(filter(lambda x: src.count(x) == 1, src))
print(f'src = {src}\nresult = {result}')


# я пробовал Lambda заменить на генератор, замерял скорость, вдвое дольше получилось (время работы,
# через perf_counter замерял)
