#Возьмите задачу о банкомате из семинара 2. 
#Разбейте её на отдельные операции — функции. 
#Дополнительно сохраняйте все операции поступления и снятия средств в список.
START_BALANCE = 0
DEPOSIT_FACTOR = 50
WITHDRAW_FACTOR = 50
WITHDRAW_RATE = 0.015
WITHDRAW_RATE_MIN = 30
WITHDRAW_RATE_MAX = 600
INTEREST_FREQUENCY = 3
INTEREST_PERCENT = 0.003
TRESHOLD_AMOUNT = 5_000_000
WEALTH_TAX = 0.010

balance = START_BALANCE
count = 0
operations = []


def deposit_account(acc_balance, operation_count, operation_list):
    deposit_amount = int(input(f'Введите сумму пополнения, кратную {DEPOSIT_FACTOR}: '))
    if deposit_amount > 0 and deposit_amount % DEPOSIT_FACTOR == 0:
        acc_balance += deposit_amount
        operation_list.append(deposit_amount)
    else:
        print(f'Сумма пополнения не кратна {DEPOSIT_FACTOR}')

    print(f'Баланс вашего счета: {acc_balance:.0f}')
    operation_count += 1

    return acc_balance, operation_count, operation_list


def withdraw_account(acc_balance, operation_count, operation_list):
    withdraw_amount = int(input(f'Введите сумму снятия, кратную {WITHDRAW_FACTOR}.\n'
                                f'Нельзя снять больше, чем на счете: '))

    if withdraw_amount % WITHDRAW_FACTOR == 0:
        percent = balance * WITHDRAW_RATE
        if percent < WITHDRAW_RATE_MIN:
            percent = WITHDRAW_RATE_MIN
        elif percent > WITHDRAW_RATE_MAX:
            percent = WITHDRAW_RATE_MAX

        if withdraw_amount + percent > acc_balance:
            print('Недостаточно средств на счете')
        else:
            acc_balance -= withdraw_amount + percent
            operation_list.append(int(-withdraw_amount - percent))
    else:
        print(f'Сумма снятия не кратна {WITHDRAW_FACTOR}')
    print(f'Баланс вашего счета: {acc_balance:.0f}')
    operation_count += 1
    return acc_balance, operation_count, operation_list


while True:

    if balance > TRESHOLD_AMOUNT:
        tax = balance * WEALTH_TAX
        balance -= tax
        print(f'Баланс вашего счета после удержания налога на богатство: {balance:.0f}')
        operations.append(int(-tax))
    if count % INTEREST_FREQUENCY == 0:
        interest = balance * INTEREST_PERCENT
        balance += interest
        print(f'Баланс вашего счета после начисления процентов: {balance:.0f}')
        operations.append(int(interest))
    operation = input(f'Для работы с банкоматом выберите действие:\n1 - пополнить\n'
                      f'2 - снять\n3 - выйти\n')
    match operation:
        case '1':
            balance, count, operations = deposit_account(balance, count, operations)
        case '2':
            balance, count, operations = withdraw_account(balance, count, operations)
        case '3':
            print(f'Баланс вашего счета: {balance:.0f}')
            break
        case _:
            break

print(operations)
