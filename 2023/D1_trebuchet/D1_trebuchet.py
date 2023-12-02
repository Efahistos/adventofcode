from re import compile
# import urllib.request

# link = ("https://adventofcode.com/2023/day/1/input")
# with urllib.request.urlopen(link) as response:
#     print(response.read())

def tosum(file_text):
    rg_first_number = compile('(.*?)(\d{1})(.*)')
    rg_second_number = compile('(.*)(\d{1})(.*)')
    numbers=[]
    for row in file_text:
        # print(row)
        nb = rg_first_number.match(string=row).group(2)
        nb += rg_second_number.match(string=row).group(2)
        numbers.append(int(nb))
    print(sum(numbers))

def replace_text_number(file_text):
    result = ''
    dict = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    dict = {
        'one':'o1e',
        'two':'w2o',
        'three':'t3e',
        'four':'f4r',
        'five':'f5e',
        'six':'s6x',
        'seven':'s7n',
        'eight':'e8t',
        'nine':'n9e'
    }
    chiffre = '|'.join([f"[{key}]" for key in dict.keys()])
    # pattern = f'({chiffre})(.*)({chiffre})'
    for row in file_text:
        temp = row
        for i in range(0, len(row)-1):
            for key, value in dict.items():
                if row[i:i+len(key)] == key:
                    temp=temp.replace(key, value)
        result += temp #+ '\n'
    return result


# file_path = '2023\\D1_trebuchet\\test1.txt'
file_path = '2023\\D1_trebuchet\\test_final.txt'
with open(file=file_path, mode='r') as f:
    tosum(file_text=f)
with open(file=file_path, mode='r') as f:
    result = replace_text_number(file_text=f)
    tosum(file_text=result.split("\n")) # 54431