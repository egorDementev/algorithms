from random import randint
import decimal


def nod(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a -= b
        else:
            b -= a
    if a == 0:
        return b
    return a


def nok(a, b):
    return a*b / nod(a, b)


def is_prime(n):
    if n == 1:
        return False
    for x in range(2, round(n ** 0.5)):
        if n % x == 0:
            return False
    return True


def prime_factors(n):
    p = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            p.append(d)
            n //= d
        d += 1
    if n > 1:
        p.append(n)
    return p


def multiply(x, y): # * умножение
    if y == 0:
        return 0
    z = multiply(x, y // 2)
    if y % 2 == 0:
        return 2*z
    return x + 2 * z


def divide(x, y): # / деление
    if x == 0:
        return 0, 0
    q, r = divide(x // 2, y)
    q = 2 * q
    r = 2 * r
    if x % 2 == 1:
        r = r + 1
    if r >= y:
        r = r - y
        q = q + 1
    return q, r


def mod_exp(x, y, n): #возведение в степень по модулю
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, n)
    if y % 2 == 0:
        return (z*z) % n
    return (x*z*z) % n


def extended_euclid(a, b): # Выход: целые числа x, y, d, для которых d = НОД(a, b) и ax + by = d
    if b == 0:
        return 1, 0, a
    x, y, d = extended_euclid(b, a % b)
    return y, x - (a // b) * y, d


def primary(n, k): # miller
    s = 0
    a = n - 1
    while a % 2 == 0:
        a = a / 2
        s += 1
    t = (n-1) / (2 ** s)
    if t % 2 == 0:
        t -= 1
        s += 1
    for i in range(0, k):
        r = randint(2, n - 2)
        x = mod_exp(r, t, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(0, s - 1):
            x = mod_exp(x, 2, n)
            if n == 1:
                return "Составное"
            elif n == n - 1:
                break
        else:
            continue
        return "Составное"
    return "Вероятно простое"


def miller_ferma_test(n):
    km1, km2, fm, s, kf, ff= 0, 0, 0, 0, 0, 0
    a = n - 1
    while a % 2 == 0:
        a = a / 2
        s += 1
    q = int(a)
    if q % 2 == 0:
        q -= 1
        s += 1
    for i in range(1, n):
        if pow(i, n - 1, n) == 1:
            kf += 1
        else :
            ff += 1
        if pow(i, q, n) == 1:
            km1 += 1
            continue
        else:
            for j in range(0, s):
                b = 2 ** j
                c = b * q
                if pow(i, pow(2, j) * q, n) == -1 % n:
                    km2 += 1
                    break
            else:
                fm += 1
    if fm == 0 :
        print("Miller-Rabin test: True", fm, km1, km2)
    else:
        print("Miller-Rabin test: False", fm, km1, km2)
    if ff == 0:
        print("Fermat test: True", ff, kf)
    else:
        print("Fermat test: False", ff, kf)
    if fm == 0 :
        return True
    else:
        return False


def ferma_test(n):
    k, f = 0, 0
    for i in range(1, n):
        if (i ** (n - 1)) % n == 1:
            k += 1
        else :
            f += 1
    if f == 0:
        print("Fermat test: True", f, k)
    else:
        print("Fermat test: False", f, k)


def RSA(p, q, e_s, a):
    delitel = (p - 1)*(q - 1)
    nd = nod(e_s, delitel)
    d = 1 / (e_s % delitel)
    print(d, nd)


def prime_numbers(a, b):
    li_ch = [i for i in range(2, b + 1)]
    li_interval = [i for i in range(a, b + 1)]
    iteration = 0
    li_print = list(li_interval)
    print("Start and finish:", a, b)
    for i in range(round(len(li_ch) ** 0.5)):
        li_otsev = []
        for j in range(len(li_interval)):
            if li_interval[j] % li_ch[i] == 0 and li_interval[j] != li_ch[i]:
                    li_otsev.append(li_interval[j])
                    li_interval[j] = -1

        if li_otsev != []:
            iteration += 1
            print("Iteration :", iteration)
            print(" ".join([str(m) for m in li_otsev]))
            li_print = list(set(li_print) - set(li_otsev))
            li_ch = list(set(li_ch) - set(li_otsev)) # оптимизация
    if li_print != []:
        print("Primes :")
        li_print.sort()
        print(" ".join([str(m) for m in li_print]))
    else:
        print("No primes")


def prime_numbers_new(a, b):
    li_ch = [i for i in range(2, b + 1)]
    iteration = 0
    print("Start and finish:", a, b)
    for i in range(round(len(li_ch) ** 0.5)):
        if is_prime(li_ch[i]):
            iteration += 1
            li_otsev = []
            for j in range(len(li_ch)):
                if i < len(li_ch) and j < len(li_ch) and li_ch[j] % li_ch[i] == 0 and li_ch[j] != li_ch[i]:
                    li_otsev.append(j)
            if li_otsev != []:
                s = ''
                for x in li_otsev:
                    if a <= li_ch[x] and b >= li_ch[x]:
                        s += str(li_ch[x]) + ' '
                for x in range(len(li_otsev) - 1, -1, -1):
                    del li_ch[li_otsev[x]]
                if s != '':
                    print("Iteration :", iteration)
                    print(s[:-1])

    if li_ch != []:
        s = ''
        print("Primes :")
        for x in range(len(li_ch)):
            if a <= li_ch[x] and b >= li_ch[x]:
                s += str(li_ch[x]) + ' '
        if s != '':
            print(s[:-1])
        else:
            print("No primes")
    else:
        print("Primes :")
        print("No primes")
