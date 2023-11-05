# Объедините функции из прошлых задач. Функцию угадайку задекорируйте декораторами для сохранения параметров, 
# декоратором контроля значений и декоратором для многократного запуска. 
# Выберите верный порядок декораторов.
from Task1 import game_decor # контроль значений
from Task2 import func_dec # сохр параметров
from Task3 import func_count # многократный запуск


@func_count(3)
@func_dec
@game_decor
def guess(rnd_num, count_num):
    for i in range(count_num):
        input_num = int(input('введите число: '))
    if input_num > rnd_num:
        print('Меньше')
    elif input_num < rnd_num:
        print('Больше')
    else:
        print(rnd_num)
        return True
    return False


if __name__ == '__main__':
    print(guess(101, 2))