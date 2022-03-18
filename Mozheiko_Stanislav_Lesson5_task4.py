# result = [12, 44, 4, 10, 78, 123]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
while True:
    """не уверен, правильно ли понял задание: формировать список или выводить по одному, сделал оба варианта =))"""
    try:
        print(next(num))
    except StopIteration:
        break
print(result)
