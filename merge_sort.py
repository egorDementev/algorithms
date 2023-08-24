def merge_sort(a, b):
    print('')
    print('Left part: ' + ' '.join(a))
    print('Right part: ' + ' '.join(b))
    a.append(10000)
    b.append(10000)
    c = list()
    ia = 0
    ib = 0
    flag = True
    while flag:
        if int(ia) >= len(a) or int(ib) >= len(b):
            break
        if int(a[ia]) < int(b[ib]):
            c.append(a[ia])
            ia += 1
        else:
            if int(b[ib]) != 10000:
                c.append(b[ib])
            ib += 1
    print('Merged parts: ' + ' '.join(c))
    return c


def merge(mass, left, right):
    if len(mass[left:right + 1]) == 1 or left >= right:
        return [mass[left]]
    mid = (left + right) / 2
    if int(mid) != float(mid):
        mid = int(mid) + 1
    mid = int(mid)
    a = merge(mass, left, mid - 1)
    b = merge(mass, mid, right)
    c = merge_sort(mass, a, b)
    return c