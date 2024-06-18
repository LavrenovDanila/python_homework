#Функция возведения элементов чписка в квадрат
def power_numbers(lst):
    return [i ** 2 for i in lst]
print("Список в квадрате:", power_numbers([1, 2, 3, 4]))

#Ввод своего списка с клавиатуры
write_lists = input("Введите список челых чисел через пробел:")

#Выбор режима фильрации списка
сonclusion = (input("Какой вывод вы хотите(Четные числа - even, Нечетные числа - odd, Простые числа - prime):"))

#Форматирование списка из str в int
lists = list(map(int, write_lists.split()))

'''
Функция для фильрации простых/четных/нечетных в зависимости от выбранного режима
'''
def filter_numbers(lists, сonclusion):
    if сonclusion == "even":
        return f'Список четных чисел: {[num for num in lists if num % 2 == 0]}'
    elif сonclusion == "odd":
        return f'Список нечетных чисел: {[num for num in lists if num % 2 != 0]}'
    elif сonclusion == "prime":
        return f'Список простых чисел: {[num for num in lists if is_prime(num)]}'
    else:
        return "Так стоп... \nНебходимо выбрать один из трех вариантов 'even', 'odd', 'prime'."

#Функия фильрации простых чисел
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False

#Вывод результата
print(filter_numbers(lists, сonclusion))