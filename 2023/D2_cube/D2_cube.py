from re import findall
import logging

level = logging.INFO
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

LIMIT = {
    "blue":14,
    "red":12,
    "green":13
}

def parse_cube(file_text):
    result:int = 0
    for row in file_text:
        id = int(findall(r'Game \d+', row)[0].split()[1])
        logging.debug(id)
        if parse_color(row=row, color="blue") \
            & parse_color(row=row, color="green") \
            & parse_color(row=row, color="red"):
            result += id
    logging.info(result)

def parse_color(row, color):
    color_list = findall(r'\d+ %s' % color, row)
    for current in color_list:
        number = int(current.split()[0])
        test = number <= LIMIT.get(color)
        logging.debug(f"{color}:{number} => {test}")
        if not test:
            return False
    return True

def max_cube(file_text):
    result:int = 0
    for row in file_text:
        id = int(findall(r'Game \d+', row)[0].split()[1])
        logging.debug(id)
        value = max_color(row=row, color="blue") \
            * max_color(row=row, color="green") \
            * max_color(row=row, color="red")
        result += value
    logging.info(result)

def max_color(row, color):
    color_list = findall(r'\d+ %s' % color, row)
    max_value = 0
    for current in color_list:
        number = int(current.split()[0])
        max_value = number if max_value < number else max_value
        logging.debug(f"{color}:{number} => {max_value}")
    return max_value

# file_path = '2023\\D2_cube\\test1.txt'
file_path = '2023\\D2_cube\\test_final.txt'
# with open(file=file_path, mode='r') as f:
#     parse_cube(file_text=f)

with open(file=file_path, mode='r') as f:
    max_cube(file_text=f)