import math

allowed = '+-/*^'

def is_valid_operator(op):
    return op in allowed

def get_operands(expr):
    for op in expr:
        if is_valid_operator(op):
            operator_index = expr.index(op)
            left = expr[:operator_index]
            right = expr[operator_index + 1:]
            return left, right
    raise ValueError(f'В выражении должен быть допустимый знак: {allowed}!sqrt()')

def f_sum(left, right):
    return left + right

def f_sub(left, right):
    return left - right

def f_mul(left, right):
    return left * right

def f_div(left, right):
    if right == 0:
        raise ZeroDivisionError('Деление на ноль!')
    return left / right

def f_pow(left, right):
    return left ** right

def f_sqrt(number):
    if number < 0:
        raise ValueError('Невозможно извлечь квадратный корень из отрицательного числа')
    return math.sqrt(number)

def f_fact(number):
    if number < 0:
        raise ValueError('Факториал отрицательного числа не определен')
    elif number == 0:
        return 1
    else:
        return number * f_fact(number - 1)

def calculate(expr):
    if not expr:
        raise ValueError('Пустое выражение')

    if "!" in expr:
        number = float(expr[:-1])
        return f_fact(number)

    if "sqrt(" in expr:
        number = float(expr[5:-1])
        return f_sqrt(number)

    left, right = get_operands(expr)
    left_val = float(left)
    right_val = float(right)

    op = expr[len(left)]
    if op in allowed:
        if op == '+':
            return f_sum(left_val, right_val)
        elif op == '-':
            return f_sub(left_val, right_val)
        elif op == '*':
            return f_mul(left_val, right_val)
        elif op == '/':
            return f_div(left_val, right_val)
        elif op == '^':
            return f_pow(left_val, right_val)
    else:
        raise ValueError(f'Неизвестная операция: {expr[0]}')

def main():
    while True:
        try:
            expr = input('Введите выражение: ')
            result = calculate(expr)
            print(f'{expr} = {result}')
        except (ValueError, ZeroDivisionError) as e:
            print(f'Ошибка: {e}')

if __name__ == '__main__':
    main()