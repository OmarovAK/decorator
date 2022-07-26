import os
from decorator import my_decor

@my_decor
def converter(temp_count, temp_name):
    while not temp_count.isdigit():
        temp_count = input('Введите правильное число: ')
    while temp_name not in ['c', 'C', 'f', 'F']:
        temp_name = input('Введите правильное наименование: ')
    if temp_name in ['c', 'C']:
        farengaite = f'{int(temp_count) * 9 / 5 + 32:.5f}'
        result = f'Температура по Фаренгейту равняется: {farengaite} градусов'
        print(result)
        return result
    else:
        celciy = f'{(int(temp_count) - 32) / 9 * 5:.5f}'
        result = f'Температура по Цельсию равняется: {celciy} градусов'
        print(result)
        return result


number = input('Введите число: ')
temp = input('Введите температурную шкалу(F - Фаренгейт, C - Цельсий): ')

converter(number, temp)
