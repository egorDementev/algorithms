def hash_fun(key, q, p):
        hash_res = 0
        for i in range(1, len(key) + 1):
            hash_res += (ord(key[i - 1]) - ord('a') + 1) * pow(p ,i - 1)
        hash_res %= q
        return hash_res


class Hash:
    def __init__(self, q, p):
        self.table = [' ' for i in range(0, q)]
        self.t_f = [0 for i in range(0, q)]
        self.q = q
        self.p = p

    def put_elem(self, key, val):
        k = hash_fun(key, self.q, self.p)
        if self.table[k] == ' ':
            self.table[k] = [key, val]
            self.t_f[k] = 0
            return 'key=' + str(self.table[k][0]) + ' hash=' + str(k) + \
                   ' operation=PUT result=inserted value=' + str(self.table[k][1])
        else:
            f = True
            for i in range(k + 1, self.q):
                 if self.table[i] == ' ':
                     f = False
                     self.table[i] = [key, val]
                     self.t_f[i] = 0
                     return 'key=' + str(key) + ' hash=' + str(k) + \
                           ' operation=PUT result=collision linear_probing=' + str(i) + ' value=' + str(val)
            if f:
                for i in range(0, k):
                     if self.table[i] == ' ':
                        self.table[i] = [key, val]
                        self.t_f[i] = 0
                        return 'key=' + str(key) + ' hash=' + str(k) + \
                               ' operation=PUT result=collision linear_probing=' + str(i) + ' value=' + str(val)
            return 'key=' + str(key) + ' hash=' + str(k) + \
                   ' operation=PUT result=overflow'

    def get_elem(self, key):
        k = hash_fun(key, self.q, self.p)
        if self.table[k] == ' ' and self.t_f[k] == 0:
            return 'key=' + str(key) + ' hash=' + str(k) + ' operation=GET result=no_key'
        elif self.table[k][0] == key:
            return 'key=' + str(key) +' hash=' + str(k) + ' operation=GET result=found value=' + str(self.table[k][1])
        else:
            num = 0
            f = True
            for i in range(k, self.q):
                num = i
                if self.table[i][0] == key:
                    f = False
                    return 'key=' + str(key) + ' hash=' + str(k) + \
                           ' operation=GET result=collision linear_probing=' + str(i) + ' value=' + str(self.table[i][1])
                elif self.t_f[i] == 0 and self.table[i] == ' ':
                    return 'key=' + str(key) + ' hash=' + str(k) + ' operation=GET result=collision linear_probing=' + \
                   str(num) + ' value=no_key'
            if f:
                for i in range(0, k):
                    num = i
                    if self.table[i][0] == key:
                        return 'key=' + str(key) + ' hash=' + str(k) + \
                               ' operation=GET result=collision linear_probing=' + str(i) + ' value=' + str(
                            self.table[i][1])
                    elif self.t_f[i] == 0 and self.table[i] == ' ':
                        return 'key=' + str(key) + ' hash=' + str(
                            k) + ' operation=GET result=collision linear_probing=' + \
                               str(num) + ' value=no_key'
            return 'key=' + str(key) + ' hash=' + str(k) + ' operation=GET result=collision linear_probing=' + \
                   str(num) + ' value=no_key'

    def del_elem(self, key):
        k = hash_fun(key, self.q, self.p)
        if self.table[k] != ' ':
            if self.table[k][0] == key:
                self.table[k] = ' '
                self.t_f[k] = 1
                return  'key=' + str(key) + ' hash=' + str(k) + ' operation=DEL result=removed'
            else:
                num = 0
                f = True
                for i in range(k, self.q):
                    num = i
                    if self.table[i][0] == key:
                        self.table[i] = ' '
                        self.t_f[i] = 1
                        f = False
                        return 'key=' + str(key) + ' hash=' + str(k) + \
                               ' operation=DEL result=collision linear_probing=' + str(num) + ' value=removed'
                    elif self.table[i] == ' ' and self.t_f[i] == 0:
                        return 'key=' + str(key) + ' hash=' + str(
                            k) + ' operation=DEL result=collision linear_probing=' + \
                               str(num) + ' value=no_key'
                if f:
                    for i in range(0, k):
                        num = i
                        if self.table[i][0] == key:
                            self.table[i] = ' '
                            self.t_f[i] = 1
                            return 'key=' + str(key) + ' hash=' + str(k) + \
                                   ' operation=DEL result=collision linear_probing=' + str(num) + ' value=removed'
                        elif self.table[i] == ' ' and self.t_f[i] == 0:
                            return 'key=' + str(key) + ' hash=' + str(
                                k) + ' operation=DEL result=collision linear_probing=' + \
                                   str(num) + ' value=no_key'
                return 'key=' + str(key) + ' hash=' + str(k) + ' operation=DEL result=collision linear_probing=' + \
                       str(num) + ' value=no_key'

        elif self.table[k] == ' ' and self.t_f[k] == 0:
            return 'key=' + str(key) + ' hash=' + str(k) + ' operation=DEL result=no_key'


a = [int(i) for i in input().split()]
q, p, n = a[0], a[1], a[2]
list_op = []
h = Hash(q, p)
for i in range(0, n):
    op = [str(x) for x in input().split()]
    list_op.append(op)
for i in list_op:
    if i[0] == 'PUT':
        print(h.put_elem(i[1], int(i[2])))
    elif i[0] == 'GET':
        print(h.get_elem(i[1]))
    else:
        print(h.del_elem(i[1]))
