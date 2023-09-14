import requests
from datetime import date

class NBU:
    def today_1(self):
        today = date.today()
        today_2 = today.strftime('%d-%m-%Y')
        today_str = str(today_2)
        today_str = today_str.replace('-', '.')
        return today_str

    def examination(self):
        try:
            re = requests.request('GET', 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
            res = re.json()
        except:
            print("error")
        else:
            with open('val.txt', 'w') as file:
                file.write(f'На {self.today_1()} курс такий:' + '\n')
                for item in res:
                    if self.today_1() in item.get('exchangedate', ''):
                        txt = item.get('txt')
                        rate = item.get('rate')
                        cc = item.get('cc')
                        content = f'{txt}({cc}) to UAH: {rate}'
                        file.write(content + '\n')
                    else:
                        txt = item.get('txt')
                        rate = item.get('rate')
                        cc = item.get('cc')
                        content = f'{txt}({cc}) to UAH: {rate}'
                        file.write(content + '\n')
        file.close()
        return file

nbu = NBU()
nbu.examination()

