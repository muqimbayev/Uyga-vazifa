import json


class CurrencyConverter:
    def __init__(self, rate=1.0):
        self.__rate = rate

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, new_rate):
        if type(new_rate) == int or type(new_rate) == float:
            self.__rate = new_rate
        else:
            print("qiymat int yoki float tipiga tegishli bo'lishi shart")

    @rate.deleter
    def rate(self):
        del self.__rate

    @staticmethod
    def convert(amount, rate):
        return amount * rate

    @staticmethod
    def usd(amount, rate):
        res = amount * rate
        CurrencyConverter.__write_to_json('usd', amount, rate, res)

    @staticmethod
    def uer(amount, rate):
        res = amount * rate
        CurrencyConverter.__write_to_json('uer', amount, rate, res)

    @staticmethod
    def __write_to_json(currency, amount, rate, result):
        try:
            with open("converter.json", encoding='utf-8') as file:
                content = json.load(file)
        except FileNotFoundError:
            content = []
        content.append({"Valyuta": currency,
                        "Miqdor": amount,
                        "Kurs": rate,
                        "Natija": result})

        with open("converter.json", mode='w', encoding='utf-8') as file:
            json.dump(content, file, indent=4)


kurs = CurrencyConverter()

print(getattr(kurs, 'rate'))

setattr(kurs, 'rate', 12500)
CurrencyConverter.usd(100, kurs.rate)
setattr(kurs, 'rate', 13000)
CurrencyConverter.uer(100, kurs.rate)

if hasattr(kurs, 'rate'):
    print(getattr(kurs, 'rate'))
else:
    print("Rate topilmadi")

delattr(kurs, 'rate')
try:
    print(getattr(kurs, 'rate'))
except AttributeError:
    print("Rate o'chirib yuborilgan")

with open('converter.json', encoding='utf-8') as file:
    con = json.load(file)
    print(con)
