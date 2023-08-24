def partition(mass, left, right):  # алгоритм быстрой сортировки, изменяет порядок элементов
    mid = (left + right) / 2
    mid = int(mid)
    x = mass[mid]
    print('')
    print('Pivot index: ' + str(mid) + ' , pivot element: ' + str(mass[mid]))
    a = []
    b = []
    for i in range(left, right + 1):
        if i != mid:
            if mass[i] <= x:
                a.append(mass[i])
            else:
                b.append(mass[i])
    mass1 = mass[:left] + a + [x] + b + mass[right + 1:]
    s = ''
    for y in mass1:
        s += str(y) + ' '
    print('Array after partition: ' + s[:-1])
    return mass1, len(a) + len(mass[:left])


def quicksort(mass, left, right):
    if left < right:
        mass, q = partition(mass, left, right)
        mass = quicksort(mass, left, q - 1)
        mass = quicksort(mass, q + 1, right)
    return mass
