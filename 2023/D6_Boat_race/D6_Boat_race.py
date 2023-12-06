from re import finditer
import logging

level = logging.DEBUG
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def parse_data(file_text):
    pattern = r'\d+'
    rows = file_text.read().split('\n')
    list_time = [res.group() for res in finditer(pattern=pattern, string=rows[0])]
    list_distance = [res.group() for res in finditer(pattern=pattern, string=rows[1])]
    return list(map(set_race, list_time, list_distance))

def set_race(time, distance):
    return {"time":time, "distance":distance}

def check_possibility(time_charge, time_left, distance):
    return time_charge * time_left > distance

def simple_parse(race):
    result = 0
    for i in range(0, int(race['time'])):
        if check_possibility(time_charge=i, time_left=int(race['time']) - i, distance=int(race['distance'])):
            result += 1
    return result

def colle_parse(races):
    time = ''
    distance = ''
    for race in races:
        time = f"{time}{race['time']}"
        distance = f"{distance}{race['distance']}"
    return set_race(time, distance)

def mult(list_numbers):
    result = 1
    for number in list_numbers:
        result *= number
    return result

file_path = '2023\\D6_Boat_race\\test1.txt'
file_path = '2023\\D6_Boat_race\\test_final.txt'
value = 0
with open(file=file_path, mode='r') as f:
    data = parse_data(file_text=f)
    logging.debug(data)
result_p1 = mult(list(map(simple_parse, data)))
logging.info(f'-----------------result P1: {result_p1}')
        
data_p2 = colle_parse(data)
result_p2 = mult(list(map(simple_parse, [data_p2])))
logging.info(f'-----------------result P2: {result_p2}')
