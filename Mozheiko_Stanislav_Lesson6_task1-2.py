def parsing_logs(log, dictionary):
    ip = log[:log.find(' ')]
    request_type, resource = (log.split('"')[1]).split(' ')[0], (log.split('"')[1]).split(' ')[1]
    parsing_result = ip, request_type, resource
    dictionary[ip] = dictionary.get(ip, 0) + 1
    return parsing_result


"""Задание 1"""

spam_find = {}
log_data = []
with open(f'nginx_logs.txt', 'r') as logs:
    while True:
        log = logs.readline()
        if log != '':
            log_data.append(parsing_logs(log, spam_find))
        else:
            break
print(log_data)

"""Задание 2"""

spam_ip = 0
spam_count = 0
for key, value in spam_find.items():
    if value > spam_count:
        spam_ip = key
        spam_count = value
print(f'\nip-адрес спамера: {spam_ip}, количество запросов: {spam_count}')
