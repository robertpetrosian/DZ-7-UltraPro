# -*- coding: utf-8 -*-
"""
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу
Спрашивает имя держателя , считывается файл счета или создается пустой

Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
метод класса Account.add()
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
метод класса Account.add() , используя отрицательное число и вопрос об имени покупки

при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
сохранение в файл держателя счета
выход из программы

"""

import json
import os

class Account():
    def __init__(self, fio):
        self.fio = fio.replace(' ','_')
        self.file = self.fio+'.json'
        self.dct = {'names':[] , 'sums':[]}

    def save(self):
        with open(self.file, 'w') as f:
            json.dump(self.dct, f)

    def restore(self):
        with open(self.file) as f:
            self.dct = json.load(f)

    def add(self,name, summa):
        self.dct['sums'].append(summa)
        self.dct['names'].append(name)

    def sums(self):
        return sum(self.dct['sums'])

    def history(self):
        rez = 'У счета нет истории' if len(self.dct['names']) == 0 else ''
        for i in range(len(self.dct['names'])):
            rez += self.dct['names'][i] + ' : '+str(self.dct['sums'][i])+'\n'
        return rez

def ctrl_acc():
    fio = input('Введите ФИО собственника счета ')
    account = Account(fio)
    if not os.path.exists(account.file):
        account.save()
    account.restore()

    while True:
        print('*'*20) # псевдо-очистка окна вывода
        print(f'На счету {account.sums()} руб')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            sum_add = int(input('Введите сумму пополнения счета: '))
            if sum_add <= 0:
                print('Неверная сумма, повторите операцию')
            else:
                account.add('Пополнение', sum_add)
        elif choice == '2':
            # покупка
            if account.sums() <= 0:
                print('На счету нет средств')
            else:
                name_sub = input('Введите назаание покупки : ')
                sum_sub = int(input('Введите сумму покупки: '))
                if account.sums() - sum_sub < 0:
                    print('Неверная сумма, повторите операцию')
                else:
                    account.add(name_sub, -sum_sub)
        elif choice == '3':
            print(account.history())
        elif choice == '4':
            account.save()
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__' :
    ctrl_acc()
