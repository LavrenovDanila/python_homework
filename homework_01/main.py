#Функция возведения элементов чписка в квадрат
def power_numbers(*numbers):
    return [i ** 2 for i in numbers]
print(power_numbers())

#Фильтрация чисел
numbers = (1, 3, 5, 7)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(numbers, filter_type):
    if filter_type == ODD:
        return [num for num in numbers if num % 2 != 0]
    elif filter_type == EVEN:
        return [num for num in numbers if num % 2 == 0]
    elif filter_type ==PRIME:
        return [num for num in numbers if is_prime(num)]

print(filter_numbers(numbers, ODD))
print(filter_numbers(numbers, EVEN))
print(filter_numbers(numbers, PRIME))