import requests
from datetime import date
today = date.today()
today_2 = today.strftime('%d-%m-%Y')
today_str = str(today_2)
today_str = today_str.replace('-', '.')
print(f'На {today_str} курс такий:')
today_str_file = f'На {today_str} курс такий:'
try:
    re = requests.request('GET', 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    res = re.json()
except:
    print("error")
else:
    with open('val.txt', 'w') as file:
        file.write(today_str_file + '\n')
        for item in res:
            if today_str in item.get('exchangedate', ''):
                txt = item.get('txt')
                rate = item.get('rate')
                cc = item.get('cc')
                content = f'{txt}({cc}) to UAH: {rate}'
                file.write(content + '\n')



