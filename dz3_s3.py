'''3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456'''
import kwargs


def user_data(**kwargs):
    print(f"{name} {surname},{age} года рождения, проживает в городе {city}, email:{mail}, телефон {tel}")
    return kwargs


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = input("Введите год рождения: ")
city = input("Введите город: ")
mail = input("Введите электронный адрес: ")
tel = input("Введите номер телефона: ")

user_data()
