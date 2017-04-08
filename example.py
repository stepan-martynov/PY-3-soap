import osa
import re

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

"""
fromCurrency" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="toCurrency" type="s:string"/>
<s:element minOccurs="1" maxOccurs="1" name="amount" type="s:double"/>
<s:element minOccurs="1" maxOccurs="1" name="rounding" type="s:boolean"/>
"""


def read_currencies():
    with open('Homework/currencies.txt') as f:
        f_as_string = f.read()
        currencies_list = re.findall(r'(\w+-\w+):\s(\w+)\s(\w+)', f_as_string)
        return currencies_list


def cost_of_travel(currencies_list):
    for _ in currencies_list:
        client2 = osa.client.Client(URL4)
        response4 = client2.service.ConvertToNum(toCurrency='RUB', fromCurrency=_[2], amount=_[1], rounding=True)
        print('При путешествии {} мы потратим {} рубля(ей)'.format(_[0].title(), int(response4 + 1)))


###

# 3) Дано: Длина пути в милях, название пути. Файл travel.txt
#    (Формат: “<название пути>: <длина в пути> <мера расстояния>”)
#    Вопрос: Посчитать суммарное расстояние пути в километрах? Точность: .01 .

URL3 = 'http://www.webservicex.net/length.asmx?WSDL'


def read_travel():
    with open('Homework/travel.txt') as f:
        f_as_string = f.read().replace(',', '')
        travel_list = re.findall(r'(\w+-\w+):\s(\w+\w+.\w+)\s(\w+)', f_as_string)
        # print(travel_list)
        return travel_list


def travel_length(travel_list):
    for _ in travel_list:
        client3 = osa.client.Client(URL3)
        response3 = client3.service.ChangeLengthUnit(LengthValue=_[1], fromLengthUnit='Miles',
                                                     toLengthUnit='Kilometers')
        print('Расстояние {} составит {} киллометров.'.format(_[0], response3))


##################

def main():
    print(avg_temperature_from_list(read_temperature_from_file()))
    cost_of_travel(read_currencies())
    travel_list = read_travel()
    travel_length(travel_list)


if __name__ == '__main__':
    main()
