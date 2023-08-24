class LinkedListElem:  # элемент связанного списка
    def __init__(self, value=None, nxt=None):
        self.value = value  # значение
        self.next = nxt  # указатель на следующий

    def append_elem(self, value):  # добавить значение
        self.value = value

    def append_id(self, nxt):  # добавить указатель
        self.next = nxt

    def get_value(self):  # получить значение
        return self.value

    def get_id(self):  # получить указатель
        return self.next


class LinkedList:  # связывает объекты класса LinkedListElem
    def __init__(self, head=None, tall=None):
        self.head = head  # указатель на первый элемент
        self.tall = tall  # указатель на последний элемент

    def append_start(self, elem):  # добавление элемента в начало
        el = LinkedListElem(elem)
        if not self.head:
            self.head = el  # если список был пуст, то оба указателя одинаковые
            self.tall = el
        else:
            a = self.head
            self.head = el  # меняем указатель на первый элемент + наш элемент указывает на бывший первый
            el.append_id(a)

    def append_finish(self, elem):  # добавление элемента в конец
        el = LinkedListElem(elem)
        if not self.head:
            self.head = el  # если список был пуст, то оба указателя одинаковые
            self.tall = el
        else:
            self.tall.append_id(el)  # меняем указатель на последний элемент + бывший последний указывает на наш
            self.tall = el

    def append_after_n(self, n, elem):  # добавление после определенного значения
        el = LinkedListElem(elem)
        if not self.head:
            self.head = el
            self.tall = el  # при пустом списке просто добавляю его в список
        else:
            cur = self.head
            f = 1
            while cur.value != n:  # ищу определенный элемент, после которого должен стоять наш
                if cur.next is None:
                    f = 0
                    break
                cur = cur.next
            if f == 0:  # проверка на существование элемента n
                print("No element")
            else:
                if cur != self.tall:  # если элемент не последний, то cur указывает на el, el на cur1(то, то раньше
                    # был после cur)
                    cur1 = cur.next
                    el.append_id(cur1)
                    cur.append_id(el)
                else:
                    self.tall.append_id(el)  # если добавляем в конец
                    self.tall = el

    def append_before_n(self, n, elem):  # добавление перед определенного значения, аналогично с предыдущей функцией
        el = LinkedListElem(elem)
        if not self.head:
            self.head = el
            self.tall = el
        else:
            cur = self.head
            f = 1
            cur0 = None
            while cur.value != n:
                cur0 = cur
                if cur.next is None:
                    f = 0
                    break
                cur = cur.next
            if f == 0:
                print("No elements")
            else:
                if cur == self.head:
                    # self.head.append_id(el)
                    # self.head = el
                    el.append_id(self.head)
                    self.head = el
                else:
                    el.append_id(cur)
                    cur0.append_id(el)

    def print_end(self):  # получить последний элемент
        if self.head is None:
            return "No elements"  # проверка на пустоту списка
        return self.tall.get_value()

    def print_start(self):  # получить первый элемент
        if self.head is None:
            return "No elements"  # проверка на пустоту списка
        return self.head.get_value()

    def del_start(self):  # удалить первый элемент
        if self.head is None:
            print("No elements")
        else:
            a = self.head.get_id()
            self.head = a  # изменяется указатель на первый элемент

    def del_finish(self):  # удалить последний элемент
        if self.head is None:
            print("No elements")
        else:
            cur = self.head
            cur0 = cur
            while cur != self.tall:  # ищем предпоследний элемент
                cur0 = cur
                cur = cur.get_id()
            cur0.append_id(None)  # изменяем его указатель на None

    def del_n(self, n):  # удалить определенный элемент
        cur = self.head
        if cur.value == n:  # если наш элемент первый
            a = cur.next
            self.head = a
        else:
            f = 1
            cur0 = cur
            while cur.value != n:  # ищем наш элемент
                cur0 = cur
                if cur == self.tall:
                    f = 0
                    break
                cur = cur.get_id()
            if f == 0:
                print("No elem")
            a = cur.next
            cur0.append_id(a)  # раньше было cur0 -> cur -> a, теперь cur0 -> а

    def print_linked_list(self):  # вывести лист на экран
        if self.head is None:
            print("No elements")
        else:
            a = []
            cur = self.head
            while cur is not None:
                a.append(cur.value)
                cur = cur.get_id()
            return a
