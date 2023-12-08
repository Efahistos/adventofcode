from re import match, compile, search
import logging

level = logging.DEBUG
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def parse_data(file_text):
    result = {}
    category = ''
    pattern_seeds = compile('seeds\: (.*)')
    pattern_text = compile('^\D*$')
    pattern_digits = compile('^\d*\s+\d*\s+\d*$')
    for row in file_text:
        if search(pattern=pattern_seeds, string=row):
            result['seeds'] = pattern_seeds.match(string=row).group(1).split()
        if search(pattern=pattern_text, string=row)and row != '\n':
            category = row.replace(' map:\n', '')
            result[category] = []
        if search(pattern=pattern_digits, string=row):
            result[category].append(row.split())
    return result

def get_map_info(seed, map):
    for map_row in map:
        range_seed = int(seed) - int(map_row[1])
        if range_seed >= 0 and range_seed < int(map_row[2]):
            return range_seed + int(map_row[0])
    return int(seed)

def merge_map(map_source, map_target):
    result = []
    for source in map_source:
        source_start = int(source[1])
        source_end = source_start + int(source[2])
        for target in map_target:
            target_start = int(target[1])
            target_end = target_start + int(target[2])
            if target_start <= source_start <= target_end:
                start = source_start
            else:
                start = target_start
            if target_start <= source_end <= target_end:
                end = source_end
            else:
                end = target_end
            if range_seed >= 0 and range_seed < int(target[2]):
                return range_seed + int(target[0])



def use_maps(seed, data):
    soil = get_map_info(seed, map=data['seed-to-soil'])
    fertilizer = get_map_info(soil, map=data['soil-to-fertilizer'])
    water = get_map_info(fertilizer, map=data['fertilizer-to-water'])
    light = get_map_info(water, map=data['water-to-light'])
    temperature = get_map_info(light, map=data['light-to-temperature'])
    humidity = get_map_info(temperature, map=data['temperature-to-humidity'])
    return get_map_info(humidity, map=data['humidity-to-location'])

file_path = '2023\\D5_gardening\\test1.txt'
# file_path = '2023\\D5_gardening\\test_final.txt'
locations = []
with open(file=file_path, mode='r') as f:
    data = parse_data(file_text=f)
seeds = data['seeds']

for seed in seeds:
    locations.append(use_maps(seed, data=data))

merge_map(map_source=[[0, 0, 100]], map_target=data['seed-to-soil'])
# logging.debug(locations)
# min_loc_p2 = 999999999999999999999999999999
# for i in range(0, len(seeds), 2):

#     for seed in range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])):
#         min_loc_p2 = min(min_loc_p2, use_maps(seed, data=data))
# logging.debug(min_loc_p2)
        
logging.info(f'-----------------result P1: {min(locations)}')
# logging.info(f'-----------------result P2: {min_loc_p2}')
