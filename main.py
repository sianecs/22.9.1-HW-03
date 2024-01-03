import random
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] >= element and array[middle - 1] < element:  # элемент в середине больше или равен искомому и предыдущий меньше
        return middle - 1  # возвращаем индекс предыдущего элемента
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

while True:
    try:
        array = list(map(float, input('Введите последовательность чисел: ').split()))
        element = float(input('Введите число: '))
        break

    except ValueError:
        print('Ошибка ввода данных. Попробуйте еще раз.')

qsort_random(array, 0, len(array) - 1)
print(f'Отсортированный список: {array}')

pos = binary_search(array, element, 0, len(array) - 1)

left = float(array[0])
right = float(array[-1])

if element < left or element > right:
        print(f'{element} нет в диапазоне')
else:
        print(f'Индекс элемента, меньше {element}: {pos}')
