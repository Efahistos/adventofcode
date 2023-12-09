from re import compile
from math import floor
import logging

level = logging.DEBUG
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def get_next_value(list):
    logging.debug(list)
    result = []
    for i in range(0, len(list)-1):
        result.append(int(list[i+1]) - int(list[i]))
    if all(ele == 0 for ele in result):
        return list[0]
    else:
        tmp = get_next_value(result)
        return tmp + int(list[len(list)-1])

def get_first_value(list):
    logging.debug(list)
    result = []
    for i in range(0, len(list)-1):
        result.append(int(list[i+1]) - int(list[i]))
    if all(ele == 0 for ele in result):
        return list[0]
    else:
        tmp = get_first_value(result)
        return int(list[0]) - tmp

file_path = '2023\\D9_mirage\\test1.txt'
file_path = '2023\\D9_mirage\\test_final.txt'
result_p1 = 0
result_p2 = 0
with open(file=file_path, mode='r') as f:
    file_text = f.read().split('\n')
for row in file_text:
    result_p1 += get_next_value(list=row.split())
logging.info(f'-----------------result P1: {result_p1}')
for row in file_text:
    result_p2 += get_first_value(list=row.split())
logging.info(f'-----------------result P2: {result_p2}')
