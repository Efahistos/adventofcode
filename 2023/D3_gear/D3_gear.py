from re import search

def check_special_characters(file_text):
    i = 0
    list_special = []
    pattern = r'[\!\@\#\$%\^\&\*\(\)\_\+\-=\[\]\{\}\;\'\:\"\\\|,<>\/\?]'
    for row in file_text:
        res = search(pattern=pattern, string=row)
        if res:
            list_special.append((i, res.start()))
        i += 1

file_path = '2023\\D3_gear\\test1.txt'
# file_path = '2023\\D1_trebuchet\\test_final.txt'
with open(file=file_path, mode='r') as f:
    check_special_characters(file_text=f)
