from re import match, compile
import logging

level = logging.DEBUG
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def get_winning_numbers(row):
    pattern = compile('.*?\:\s*(.*?)\s\|.*')
    list_res = pattern.match(string=row).group(1).split()
    return list_res

def get_test_numbers(row):
    pattern = compile('.*\:.*\|\s(.*)')
    list_res = pattern.match(string=row).group(1).split()
    return list_res

file_path = '2023\\D4_scratchcard\\test1.txt'
file_path = '2023\\D4_scratchcard\\test_final.txt'
value = 0
iterator = 1
dict_p2 = {}
with open(file=file_path, mode='r') as f:
    for row in f:
        dict_p2[iterator] = dict_p2.get(iterator, 0) + 1
        winning_numbers = get_winning_numbers(row)
        test_numbers = get_test_numbers(row)
        result = list(set(winning_numbers) & set(test_numbers))
        len_result = len(result)
        if len_result > 0:
            value += pow(2, len_result - 1)
            for i in range(iterator + 1, iterator + 1 + len_result):
                dict_p2[i] = dict_p2.get(i, 0) + dict_p2[iterator]
        iterator += 1
        
logging.info(f'-----------------result P1: {value}')
logging.info(f'-----------------result P2: {sum([v for v in dict_p2.values()])}')
