from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.array = LinkedList()  # создаем объект класса связанного листа
        self.top = None
        self.len = 0

    def add_elem(self, elem):
        self.array.append_start(elem)  # добавляю в начало элемент
        # (мне так проще ориентироваться, представляю, что первый элемент -
        # верхушка стека)
        self.top = self.array.head  # меняю указатель на первый элемент
        self.len += 1

    def get_elem(self):
        if self.top is not None:
            return self.array.head.get_value()  #
        return "Stack is empty"

    def del_elem(self):
        if self.top is not None:
            a = self.array.head.value
            self.array.del_start()
            self.top = self.array.head  # при удалении меняем указатель на верхний элемент стека
            self.len -= 1
            return a  # возвращаем удаленный элемент
        return "Stack is empty"

    def is_empty(self):
        if self.top is None:  # если список пуст
            return True
        return False


def reverse_polish(st):  # обратная польская запись
    li = ['+', '-', '*', '/', '(', ')']
    dict = {  # словарь, для сравнения приоритетности операций
        '(': 1,
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3
    }
    res = Stack()  # стек, пригодится для хранения знаков операций
    mass = []  # массив, в котором будет итоговая запись
    for i in st:
        if i == '(':  # добавляем круглую скобку в стек, чтобы потом понимать, какие действия в скобках
            res.add_elem(i)
        elif i == ')':
            f = True
            while f:  # когда видим закрывающуюся скобку, то выводим оставшиеся операции на экран до "("
                a = res.get_elem()
                if a != '(' and a != 'Stack is empty':
                    mass.append(a)
                    a = res.del_elem()
                    # d[a] = int(dict[a])
                else:
                    a = res.del_elem()
                    f = False
            # sorted_d = sorted(d.items(), key=lambda x: x[1])
        elif i in li and i != ')':
            # если натыкаемся на знак операции отличный от "(" и ")", смотрим, что делать с ним и предыдущими
            if res.is_empty():
                res.add_elem(i)
            else:
                if dict[i] > dict[res.top.get_value()]:  # если приоритетность выше, то добавляем в стек
                    res.add_elem(i)
                else:
                    f = True
                    while f:
                        # если приоритетность ниже, то добавляем в массив все знаки до тех пор,
                        # пока не встретим знак ниже по приоритету
                        if not res.is_empty():
                            a = res.get_elem()
                            if a != '(' and dict[a] >= dict[i]:
                                mass.append(a)
                                a = res.del_elem()
                            else:
                                f = False
                                if a == '(':
                                    a = res.del_elem()
                        else:
                            f = False
                    res.add_elem(i)  # наш знак добавляем в стек
        elif i not in li:  # если встретили число, то добавляем его в стек
            mass.append(i)
    while not res.is_empty():  # в конце оставшиеся знаки выводим
        a = res.del_elem()
        mass.append(a)
    return mass


def calculator(a, b, op):  # простейший калькулятор
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b


def sum_polish(mass):
    res = Stack()  # создаем вспомогательный стек
    li = ['+', '-', '*', '/']
    for i in mass:
        if i not in li:
            res.add_elem(int(i))  # числа сразу идут в стек
        else:  # если видим знак операции
            a = res.del_elem()  # берем и удаляем 2 элемента стека
            b = res.del_elem()
            res.add_elem(calculator(b, a, i))  # производим вычисления и добавляем результат в стек
    return res.del_elem()


n = input()
li, st = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], []
for i in range(len(n)):  # строку из цифр и символов разбиваем на числа и операции
    if i == 0:
        st.append(n[i])
    elif n[i - 1] in li and n[i] in li:
        a = st[-1]
        del st[-1]
        st.append(a + n[i])
    else:
        st.append(n[i])
mass = reverse_polish(st)
print("Result:")
print(int(sum_polish(mass)))
