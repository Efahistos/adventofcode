from re import compile
from math import floor
import logging

level = logging.DEBUG
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def parse_data(file_text, pattern):
    pattern = compile(pattern)
    result = {}
    for row in file_text.split('\n'):
        matches = pattern.match(string=row)
        result[matches.group(1)] = {'L':matches.group(2), 'R':matches.group(3)}
    return result

def check_last_letter(letter, step):
    return letter == step[-1]

def factors(n):
 result = []
 for i in range(2,n+1): # test all integers between 2 and n
  s = 0
  while n/i == floor(n/float(i)): # is n/i an integer?
   n = n/float(i)
   s += 1
  if s > 0:
   for k in range(s):
    result.append(i) # i is a pf s times
   if n == 1:
    return result

def mult(list_numbers):
    result = 1
    for number in list_numbers:
        result *= number
    return result

file_path = '2023\\D8_wasteland\\test1.txt'
file_path = '2023\\D8_wasteland\\test_final.txt'
with open(file=file_path, mode='r') as f:
    file_text = f.read().split('\n\n')
LR_pattern = file_text[0]
data = parse_data(file_text=file_text[1], pattern=r'([A-Z]{3}).*?([A-Z]{3}).*?([A-Z]{3}).*')
# logging.debug(data)
i = 0
step = 'AAA'
while step != 'ZZZ':
    step = data[step][LR_pattern[i%len(LR_pattern)]]
    i += 1
result_p1 = i
logging.info(f'-----------------result P1: {result_p1}')

data = parse_data(file_text=file_text[1], pattern=r'([0-9A-Z]{3}).*?([0-9A-Z]{3}).*?([0-9A-Z]{3}).*')
# logging.debug(data)
steps_P2 = [k for k in data.keys() if check_last_letter('A', k)]

dict_p2_first = {}
dict_p2_aggreg = {}
for step in steps_P2:
    i = 0
    logging.debug(f'start step: {step}')

    while not check_last_letter('Z', step):
        step = data[step][LR_pattern[i%len(LR_pattern)]]
        i += 1
    dict_p2_first[step] = i
    dict_p2_aggreg[step] = factors(i)
[logging.debug(a) for a in dict_p2_aggreg.values()]


# result_p1 = i

logging.info(f'-----------------result P2: {mult([a[0]for a in dict_p2_aggreg.values()])*283}')

# {'PQZ': 20659, 'ZZZ': 20093, 'BKZ': 14999, 'XNZ': 17263, 'KJZ': 22357, 'XLZ': 16697}
print (mult([61, 293,67, 59, 43, 73, 71]))