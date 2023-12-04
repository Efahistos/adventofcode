from re import match, compile
import logging

level = logging.DEBUG
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def get_winning_numbers(row):
    pattern = compile('.*?\:\s*(.*?)\s\|.*')
    list_res = pattern.match(string=row).group(1).split()
    return list_res

file_path = '2023\\D4_scratchcard\\test1.txt'
# file_path = '2023\\D4_scratchcard\\test_final.txt'
with open(file=file_path, mode='r') as f:
    for row in f:
        winning_numbers = get_winning_numbers(row)