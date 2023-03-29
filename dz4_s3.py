'''4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()'''


def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_2 >= arg_1 and arg_3 >= arg_1:
        return arg_2 + arg_3
    elif arg_1 >= arg_2 and arg_3 >= arg_2:
        return arg_1 + arg_3


print(my_func(20, 180, 10))

def sec_func(arg_1, arg_2, arg_3):
    sec_func().sort(reverse=True)
    return arg_1+arg_2
print(my_func(30, 180, 150))