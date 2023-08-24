from time import perf_counter


def generate_matrix_type1(m, n):
    return [[(n // m * i + j) * 2 for j in range(n)] for i in range(m)]


def generate_matrix_type2(m, n):
    return [[(n // m * i * j) * 2 for j in range(n)] for i in range(m)]


def lin_search(matrix, target):
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n - 1
    while True:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
        if i == m or j == -1:
            return False


def bin_search(matrix, target):
    row, start, stop = 0, 0, len(matrix[0]) - 1
    while row < len(matrix):
        mid = (start + stop) // 2
        if matrix[row][mid] == target:
            return True
        if start >= stop:
            start, stop, row = 0, len(matrix[0]) - 1, row + 1
            continue
        if matrix[row][mid] > target:
            stop = mid - 1
        else:
            start = mid + 1
    return False


def lin_and_exp_search(matrix, target):
    m, n, i, j, list_degrees, point = len(matrix), len(matrix[0]), 0, len(matrix[0]) - 1, [pow(2, x) for x in
                                                                                           range(0, 15)], 0
    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            point = 0
            while j - list_degrees[point] >= 0 and matrix[i][j - list_degrees[point]] > target:
                if j - list_degrees[point + 1] >= 0:
                    point += 1
                    start, stop = j - list_degrees[point] + 1, j - list_degrees[point - 1]
                else:
                    stop, start = start, 0
                    break
            if point == 0:
                i += 1
                continue
            while stop >= start >= 0:
                if start == stop and matrix[i][start] == target:
                    return True
                if start == stop and matrix[i][start] != target:
                    j = start
                    break
                mid = (start + stop) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] > target:
                    stop = mid - 1
                else:
                    start = mid + 1
                if start > stop:
                    i += 1
                    break
        else:
            i += 1
    return False


# производятся замеры среднего времени работы линейного, бинарного и экспоненциального поисков на данных различного
# размера
for x in range(1, 14):
    n = pow(2, 13)
    m = pow(2, x)
    target = 2 * n + 1
    summ = 0
    matrix = generate_matrix_type1(m, n)
    matrix2 = generate_matrix_type2(m, n)
    target2 = 16 * n + 1
    print('M: ' + str(m) + '   ' + 'N:' + str(n))
    for _ in range(10):
        begin = float(perf_counter())
        a = lin_search(matrix, target)
        time = float(perf_counter() - begin)
        summ += time
    print('lin', '  ', summ / 10)
    summ = 0
    for _ in range(10):
        begin = float(perf_counter())
        a = bin_search(matrix, target)
        time = float(perf_counter() - begin)
        summ += time
    print('bin', '  ', summ / 10)
    summ = 0
    for _ in range(10):
        begin = float(perf_counter())
        a = lin_and_exp_search(matrix, target)
        time = float(perf_counter() - begin)
        summ += time
    print('exp 1', '  ', summ / 10)
    summ = 0
    for _ in range(10):
        begin = float(perf_counter())
        a = lin_and_exp_search(matrix2, target2)
        time = float(perf_counter() - begin)
        summ += time
    print('exp 2', '  ', summ / 10)
