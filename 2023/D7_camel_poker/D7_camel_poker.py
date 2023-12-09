from re import finditer
import logging

level = logging.INFO
logging_format = "%(message)s"
logging.basicConfig(level = level, format=logging_format)

def parse_data(file_text):
    power_hand = {2:1, 3:3, 4:5, 5:6}
    power_card = {'T':'A', 'J': 'B', 'Q':'C', 'K':'D', 'A':'E'}
    result = []
    for row in file_text:
        hand = {}
        type_hand = 0
        alpha_hand = ''
        cards, bid = row.split()
        for card in cards:
            hand[card]= hand.get(card, 0) + 1
            alpha_hand += power_card.get(card, card)
        for v in hand.values():
            type_hand += power_hand.get(v, 0)
        result.append({'cards':cards, 'type_hand':type_hand, 'alpha_hand':alpha_hand, 'bid':bid})
    return result

def parse_data_P2(file_text):
    power_hand = {2:1, 3:3, 4:5, 5:6}
    power_card = {'T':'A', 'J': '1', 'Q':'C', 'K':'D', 'A':'E'}
    result = []
    for row in file_text:
        hand = {}
        type_hand = 0
        J_number = 0
        alpha_hand = ''
        cards, bid = row.split()
        for card in cards:
            if card == 'J':
                J_number += 1
            else:
                hand[card]= hand.get(card, 0) + 1
            alpha_hand += power_card.get(card, card)
        if J_number == 5:
            type_hand += power_hand.get(J_number, 0)
        else:
            test_J = True
            for v in sorted(hand.values(), reverse=True):
                type_hand += power_hand.get(v + (J_number if test_J else 0), 0)
                test_J = False
        result.append({'cards':cards, 'type_hand':type_hand, 'alpha_hand':alpha_hand, 'bid':bid})
    return result



def mult(list_numbers):
    result = 1
    for number in list_numbers:
        result *= number
    return result

file_path = '2023\\D7_camel_poker\\test1.txt'
file_path = '2023\\D7_camel_poker\\test_final.txt'
with open(file=file_path, mode='r') as f:
    data = parse_data(file_text=f)
    logging.debug(data)
    sorted_hand = sorted(data, key = lambda h:(h['type_hand'], h['alpha_hand']))
    [logging.debug(a) for a in sorted_hand]
    result_p1 = 0
    for i in range(0,len(sorted_hand)):
        result_p1 += (i+1) * int(sorted_hand[i]['bid'])
logging.info(f'-----------------result P1: {result_p1}')


with open(file=file_path, mode='r') as f:
    data = parse_data_P2(file_text=f)
    logging.debug(data)
    sorted_hand = sorted(data, key = lambda h:(h['type_hand'], h['alpha_hand']))
    [logging.debug(a) for a in sorted_hand]
    result_p2 = 0
    for i in range(0,len(sorted_hand)):
        result_p2 += (i+1) * int(sorted_hand[i]['bid'])
logging.info(f'-----------------result P2: {result_p2}')
        
# data_p2 = colle_parse(data)
# result_p2 = mult(list(map(simple_parse, [data_p2])))
