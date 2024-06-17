numbers = (1, 2, 5, 7)
square_numbers = [numbers ** 2 for numbers in numbers]
print(square_numbers)

def filter_odd_num(in_num):
    if (in_num % 2) != 0:
        return True
    else:
        return False

def filter_even_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False

def filter_prime_num(in_num):
    for i in range(2, int(in_num**0.5) + 1):
        if in_num % i == 0:
            return False
        else:
            return True


write_lists = input("Введите список челых чисел через пробел:")
сonclusion = (input("Какой вывод вы хотите(Четные числа - even, Нечетные числа - odd, Простые числа - prime):"))
lists = list(map(int, write_lists.split()))

if сonclusion == "odd":
    odd_list = filter(filter_odd_num, lists)
    print("Список нечетных чисел", list(odd_list))
elif сonclusion == "even":
    even_list = filter(filter_even_num, lists)
    print("Список четных чисел", list(even_list))
elif сonclusion == "prime":
    prime_list = filter(filter_prime_num, lists)
    print("Список простых чисел", list(prime_list))
else:
    print("Ну как так-то?...\nДавай еще раз)")