import osa

###
# 1) Дано: Семь значений температур по Фаренгейту.Файл temps.txt.
# Вопрос: Какая средняя арифм.температура по Цельсию на неделю?

URL1 = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'


def read_temperature_from_file():
    temperature_list = []
    with open('Homework/temps.txt') as f:
        temperature_list = f.read().split('\n')
        return temperature_list


def avg_temperature_from_list(temperature_list):
    client1 = osa.client.Client(URL1)
    sum_temperature = 0
    for temperature in temperature_list:
        temperature = temperature.split(' ')[0]
        response1 = client1.service.ConvertTemp(Temperature=temperature, FromUnit='degreeFahrenheit',
                                                ToUnit='degreeCelsius')
        sum_temperature += response1
    avg_temperature = sum_temperature / len(temperature_list)
    return avg_temperature


###
# 2) Дано: Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты.
#    Даны цены на билеты в местных валютах. Файл currencies.txt
#    (Формат данных в файле: “<откуда куда>: <стоимость билета> <код валюты>”)
#    Вопрос: Посчитайте сколько вы потратите на путешествие денег в рублях. Точность: без копеек, округлить в большую сторону.

URL4 = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

client4 = osa.client.Client(URL4)

"""
fromCurrency" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="toCurrency" type="s:string"/>
<s:element minOccurs="1" maxOccurs="1" name="amount" type="s:double"/>
<s:element minOccurs="1" maxOccurs="1" name="rounding" type="s:boolean"/>
"""

response4 = client4.service.ConvertToNum(toCurrency='USD', fromCurrency='RUB', amount=100.00, rounding=True)

# print(response4)
print(100.00 / float(response4))


###



URL2 = 'http://www.webservicex.net/ConvertSpeed.asmx?WSDL'

client2 = osa.client.Client(URL2)

response2 = client2.service.ConvertSpeed(speed=121.25, FromUnit='milesPerhour', ToUnit='kilometersPerhour')

print(response2)

###

URL3 = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

client3 = osa.client.Client(URL3)

response3 = client3.service.Currencies()

print(response3.split(';'))


###
def main():
    print(avg_temperature_from_list(read_temperature_from_file()))


if __name__ == '__main__':
    main()
