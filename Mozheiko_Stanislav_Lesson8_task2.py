import re

RE_IP = re.compile(r'([0-2]?\d{1,2}\.){3}[0-2]?\d{1,2}')
RE_DATE = re.compile(r'\d{2}/[A-Z][a-z]+/\d{4}(:\d{2}){3}\s\+\d{4}')
RE_REQ = re.compile(r'[A-Z]+\b')
RE_PATH = re.compile(r'/\w+/\w+_\d\s')
RE_RESP_CODE_SIZE = re.compile(r'\d+\s\d+')
RE_RESP_SIZE = re.compile(r'\s\d\s')
RE_SPLIT = re.compile(r'[- "\[\]]{2,}')


def parse_response(response, *args):
    parsed_data = []
    for arg in args:
        data = re.search(arg, response)
        if data:
            if arg == RE_RESP_CODE_SIZE:
                parsed_data.extend(re.search(arg, response)[0].strip(' ').split(' '))
            else:
                parsed_data.append(re.search(arg, response)[0].strip(' '))
    return parsed_data


params = [RE_IP, RE_DATE, RE_REQ, RE_PATH, RE_RESP_CODE_SIZE]
with open('nginx_logs.txt', 'r') as f, open('log.txt', 'a') as f_2:
    count = 0
    raw = ' '
    while raw != '':
        raw = f.readline()
        count += 1
        result = parse_response(raw, *params)
        raw_2 = f'line# {count} - {result}\n'
        if len(result) > 0:
            print(result, count)
            f_2.write(raw_2)
