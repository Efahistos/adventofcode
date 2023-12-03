from re import search, findall, finditer, sub
import logging

level = logging.DEBUG
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def get_index_special_characters(file_text):
    i = 0
    list_special = []
    pattern = r'[\!\@\#\$%\^\&\*\(\)\_\+\-=\[\]\{\}\;\'\:\"\\\|,<>\/\?]{1}'
    for row in file_text:
        list_res = finditer(pattern=pattern, string=row)
        for res in list_res:
            list_special.append((i, res.span()[0]))
        i += 1
    return list_special

def get_index_numbers(file_text):
    i = 0
    index_numbers = []
    pattern = r'\d+'
    for row in file_text:
        list_res = finditer(pattern=pattern, string=row)
        for res in list_res:
            span = res.span()
            index_numbers.append({'pos':(i, span[0]), 'span':span, 'value':res.group()})
            index_numbers.append({'pos':(i, span[1] - 1), 'span':span, 'value':res.group()})
        i += 1
    return index_numbers

def intersect_numbers_places(index_numbers, possible_place):
    result = {}
    for number in index_numbers:
        if number['pos'] in possible_place:
            result[(number['pos'][0], number['span'])] = number['value']
    return result


def get_list_adjacent_places(list_places):
    result = []
    for place in list_places:
        result.extend(get_adjacent_places(place=place))
    return result

def get_adjacent_places(place):
    result = []
    range_defined = [-1, 0, 1]
    for i in range_defined:
        for j in range_defined:
            result.append((place[0] + i, place[1] + j))
    return result

def get_adjacent_number(index_numbers, list_special):
    result = 0
    for place in list_special:
        temp = 1
        test = intersect_numbers_places(
            possible_place=get_adjacent_places(place=place)
            , index_numbers=index_numbers)
        if len(test) == 2:
            for v in test.values():
                temp *= int(v)
            result += temp
    return result


file_path = '2023\\D3_gear\\test1.txt'
file_path = '2023\\D3_gear\\test_final.txt'
with open(file=file_path, mode='r') as f:
    for row in f:
        res = sub(string=row, pattern='\d', repl='')
        res = sub(string=res, pattern='\.', repl='')
        res = sub(string=res, pattern=r'[\!\@\#\$%\^\&\*\(\)\_\+\-=\[\]\{\}\;\'\:\"\\\|,<>\/\?]', repl='')
        if res != '\n':
            logging.debug(res)
with open(file=file_path, mode='r') as f:
    list_special = get_index_special_characters(file_text=f)
    # logging.debug(f'-----------------list_special\n{list_special}')
with open(file=file_path, mode='r') as f:
    list_index_value = get_index_numbers(file_text=f)
    # logging.debug(f'-----------------list_index_value\n{list_index_value}')
possible_place = get_list_adjacent_places(list_places=list_special)
# logging.debug(f'-----------------possible_place\n{possible_place}')
intersect = intersect_numbers_places(index_numbers=list_index_value, possible_place=possible_place)
# logging.debug(f'-----------------intersect\n{intersect}\n')
result = sum([int(v) for k, v in intersect.items()])
logging.info(f'-----------------result P1: {result}') # 535351

rp2 = get_adjacent_number(index_numbers=list_index_value, list_special=list_special)
logging.info(f'-----------------result P2: {rp2}') # 535351