import math


def distance(x1, y1, x2, y2):
    return pow(pow((x1 - x2), 2) + pow((y1 - y2), 2), 0.5)


list_input = [[x for x in input().split()] for i in range(int(input()) + 1)]
list_cities, list_cors, list_marks = [x[0] for x in list_input[:-1]], \
                                     [(int(x[1]), int(x[2])) for x in list_input[:-1]], \
                                     [1000000 for i in list_input[:-1]]

graph, start_city, finish_city = [[list_cities.index(x) for x in i[3:]] for i in list_input[:-1]], \
                                 list_cities.index(list_input[-1][0]), \
                                 list_cities.index(list_input[-1][1])

list_marks[start_city], queue, list_way, k, s, list_ancestor = 0, [start_city], [finish_city], \
                                                               0, '', [0 for i in range(len(list_cities))]

while True:
    if k >= len(queue):
        break

    for i in graph[queue[k]]:
        if i not in queue:
            queue.append(i)
        len_way = distance(list_cors[queue[k]][0], list_cors[queue[k]][1], list_cors[i][0], list_cors[i][1])
        if list_marks[queue[k]] + len_way <= list_marks[i]:
            list_marks[i], list_ancestor[i] = list_marks[queue[k]] + len_way, queue[k]

    k += 1
if list_marks[finish_city] != 1000000:
    while list_way[-1] != start_city:
        list_way.append(list_ancestor[list_way[-1]])

    list_way.reverse()
    print("Path is not greater than " + str(math.ceil(list_marks[finish_city])) + '\n' + 'Path:')
    for x in list_way:
        s += list_cities[x] + ' '
    print(s[:-1])
else:
    print("Path:\nNo way")


# задача А
def DFS(point, cor, graph, list_way, list_pass):
    list_pass[point] = 1
    if cor == n * n - 1:
        list_way.append(point)

    for i in graph[point]:
        DFS(i, cor + 1, graph, list_way, list_pass) if not list_pass[i] else None

    if list_way:
        list_way.append(point)
    else:
        list_pass[point] = 0


n, cor, graph, list_way = int(input()), [int(i) for i in input().split()], [], []
print("Graph:")

for i in range(n * n):
    x, y = i // n, i % n
    lst = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    graph.append([(x + a) * n + y + b for a, b in lst if x + a >= 0 and x + a < n and y + b >= 0 and y + b < n])
    print(str(i) + ' - ' + ' '.join(list(map(str, graph[-1]))))

print("Hamiltonian path:")
list_pass, list_print = [0 for i in range(n * n)], [[0 for i in range(n)] for i in range(n)]
DFS(cor[0] * n + cor[1], 0, graph, list_way, list_pass)
list_way.reverse()

for i in range(len(list_way)):
    list_print[list_way[i] // n][list_way[i] % n] = i if i < n * n else n * n - 1

if list_way:
    for i in list_print:
        print(' '.join(list(map(str, i))))
else:
    print("No ways")

# задача В
a = input().split()
row_size, column_size, num_start, num_finish = int(a[0]), int(a[1]), 0, 0
maze, graph = [list(input()) for i in range(row_size)], []

print("Initial labyrinth:")
for i in maze:
    print(''.join(i))
print("Graph:")

for i in range(row_size * column_size):
    x, y = i // column_size, i % column_size
    x = i if column_size == 1 else i // column_size
    x = 0 if row_size == 1 else x
    y = 0 if column_size == 1 else y
    if maze[x][y] == '#':
        graph.append([None])
        print(str(i) + ' - None')
        continue
    num_start = i if maze[x][y] == 'S' else num_start
    num_finish = i if maze[x][y] == 'F' else num_finish

    point_1 = [-1, -1] if x == 0 else [x - 1, y]
    point_2 = [-1, -1] if y == column_size - 1 else [x, y + 1]
    point_3 = [-1, -1] if x == row_size - 1 else [x + 1, y]
    point_4 = [-1, -1] if y == 0 else [x, y - 1]

    list_ways = [i[0] * column_size + i[1] for i in [point_1, point_2, point_3, point_4]
                 if maze[i[0]][i[1]] != '#' and i[0] != -1]

    list_ways.sort()
    graph.append(list_ways)
    list_ways = [None] if list_ways == [] else list_ways
    print(str(i) + ' - ' + ' '.join(list(map(str, list_ways))))

bfs, queue, list_points = [[-1 for i in range(column_size)] for j in range(row_size)], \
                          [[x for x in graph[num_start]]], \
                          [x for x in graph[num_start]] + [num_start]

bfs[num_start // column_size if column_size != 1 else num_start][num_start % column_size if column_size != 1 else 0], \
step_number, flag = 0, 1, True

while True:
    if queue == [] or queue == [[]]:
        break
    queue.append([])

    for i in queue[0]:
        flag = False if i == num_finish else flag
        queue[1].extend([x for x in graph[i] if x not in list_points]) if flag == True else queue
        list_points.extend([x for x in graph[i]])
        bfs[i // column_size if column_size != 1 and row_size != 1 else 0 if row_size == 1 else i][i % column_size if column_size != 1 else 0] = step_number
        del i

    del queue[0]
    step_number += 1
print("BFS result is:")

for i in bfs:
    print(' '.join(list(map(str, i))))
