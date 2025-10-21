import math
"""
# 4.1
n = int(input("два различных вещественных числа\n"))
x = int(input())
if x > n:
    print('больше ', x)
    print('меньше ', n)
elif x < n:
    print('больше ', n)
    print('меньше ', x)
else:
    print('числа равны')

# 4.2
x = int(input('x = '))
if x > 0:
    y = math.sin(x)**2
elif x <= 0:
    y = 1 - 2 * math.sin(x)**2
print('y = ', y)

# 4.3
x = int(input('x = '))
if x > 0:
    y = math.sin(x)**2
elif x <= 0:
    y = 1 - 2 * math.sin(x)**2
print('y = ', y)

# 4.4
x = int(input('x = '))
if x > 4:
    print(2)
elif x < 4:
    print(1)
else:
    print('между 1 и 2 :)')

# 4.5
y = int(input('x = '))
if y > 3:
    print(1)
elif y < 3:
    print(2)
else:
    print('между 1 и 2 :)')

# 4.6
x = int(input('x = '))
y = x
print('y = ', y)

x = int(input('x = '))
y = x
print('y = ', (-1)*y)

# 4.7
x = int(input('x = '))
if math.sin(x) < 0:
    k = x**2
elif math.sin(x) >= 0:
    k = abs(x)

if k > x:
    f = k * x
elif x <= k:
    f = k + x
print('f(x) = ', f)

# 4.8
x = int(input('x = '))
if math.sin(x) < 0:
    k = abs(x)
elif math.sin(x) >= 0:
    k = x**2

if k <= x:
    f = k * x
elif x < k:
    f = abs(x)
print('f(x) = ', f)

# 4.9
n = int(input("два различных вещественных числа\n"))
x = int(input())
if x > n:
    print('больше ', x)
    print('меньше ', n)
elif x < n:
    print('больше ', n)
    print('меньше ', x)
else:
    print('числа равны')

# 4.10
km = int(input('km = '))
funt = int(input('funt = '))
metr = km * 1000
funt = funt * 0.3048
if funt > metr:
    print('km')
elif funt < metr:
    print('funt')
else:
    print('=')

# 4.11
kmh = int(input('kmh = '))
ms = int(input('ms = '))
kmh = 1/3.6 * kmh
if kmh > ms:
    print('kmh')
elif kmh < ms:
    print('ms')
else:
    print('=')

# 4.12
r = float(input("r = "))
a = float(input("a = "))

S_r = math.pi * r**2
S_a = a**2

if S_r > S_a:
    print("Площадь круга больше")
elif S_r < S_a:
    print("Площадь квадрата больше")
else:
    print("Площади равны")

# 4.13
m1 = float(input("m1 = "))
v1 = float(input("v1 = "))
m2 = float(input("m2 = "))
v2 = float(input("v2 = "))

p1 = m1 / v1
p2 = m2 / v2

if p1 > p2:
    print("Первое тело имеет большую плотность")
elif p1 < p2:
    print("Второе тело имеет большую плотность")
else:
    print("Плотности равны")

# 4.14
R1 = float(input("R1 = "))
U1 = float(input("U1 = "))
R2 = float(input("R2 = "))
U2 = float(input("U2 = "))

I1 = U1 / R1
I2 = U2 / R2

if I1 < I2:
    print("Меньший ток протекает по первому участку")
elif I1 > I2:
    print("Меньший ток протекает по второму участку")
else:
    print("Токи равны")

# 4.15
a = float(input("(\"а\" НЕ МОЖЕТ БЫТЬ НУЛЁМ!) a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
    print('поменяйте значение "а"')
    exit()
D = a**2 -4 * b * c
if D < 0:
    print('уравнение не имеет корней')
else:
    print("уравнение имеет корни")

# 4.16
a = float(input("(\"а\" НЕ МОЖЕТ БЫТЬ НУЛЁМ!) a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
    print('поменяйте значение "а"')
    exit()
D = (b**2) - (4*a*c)
if D < 0:
    print('уравнение не имеет корней')
else:
    print("уравнение имеет корни")
x1 = (-b + math.sqrt(D))/(2*a)
x2 = (-b - math.sqrt(D))/(2*a)
print('x1 = ', x1)
print('x2 = ', x2)

# 4.17
gd = int(input("год рождения = "))
mes = int(input('месяц рождения = '))
gds = int(input('год на данный момент = '))
mess = int(input('месяц на данный момент = '))

if mess <= 0 or mess > 12:
    print('в году 12 месяцев!')
    exit()
if mes <= 0 or mes > 12:
    print('в году 12 месяцев!')
    exit()

if mes > mess:
    vozg = gds - gd -1
else:
    vozg = gds - gd

print('полных лет = ', vozg)

# 4.18
Skrug = int(input("S_круга = "))
Skvad = int(input('S_квадрата = '))
r = (Skrug * math.pi)**(1/2)

dkrug = 2 * r
a = Skvad**1/2
dkvad = a * (2)**(1/2)

if dkrug <= a:
    print("Круг уместится в квадрате")
else:
    print("Круг не уместится в квадрате")

if dkvad <= dkrug:
    print("Квадрат уместится в круге")
else:
    print("Квадрат не уместится в круге")


# 4.19
Skrug = float(input("S_круга = "))
Str = float(input("S_треугольника = "))

rkrug = (Skrug / math.pi)**(1/2)
dkrug = 2 * rkrug
atr = (4 * Str / (3**0.5))**(1/2)
rin_tr = atr * (3**0.5) / 6
rout_tr = atr * (3**0.5) / 3

if dkrug <= 2*rin_tr:
    print("Круг уместится в треугольнике")
else:
    print("Круг не уместится в треугольнике")

if 2*rout_tr <= dkrug:
    print("Треугольник уместится в круге")
else:
    print("Треугольник не уместится в круге")

# 4.20

x1_min = float(input("x1_min = "))
y1_min = float(input("y1_min = "))
x1_max = float(input("x1_max = "))
y1_max = float(input("y1_max = "))

x2_min = float(input("x2_min = "))
y2_min = float(input("y2_min = "))
x2_max = float(input("x2_max = "))
y2_max = float(input("y2_max = "))

xmin = min(x1_min, x2_min)
ymin = min(y1_min, y2_min)

xmax = max(x1_max, x2_max)
ymax = max(y1_max, y2_max)

print("Левый нижний угол минимального прямоугольника:", xmin, ymin)
print("Правый верхний угол минимального прямоугольника:", xmax, ymax)

# 4.99
# a)
a = float(input("a = "))
b = float(input("b = "))

if a > b:
    print("Наибольшее =", a)

if b > a:
    print("Наибольшее =", b)
# b)
a = float(input("a = "))
b = float(input("b = "))

max_num = a
if b > a:
    max_num = b

print("Наибольшее =", max_num)

# 4.100
# a)
a = float(input("a = "))
b = float(input("b = "))

if a > b:
    print("Наибольшее =", a)
if b > a:
    print("Наибольшее =", b)

if a < b:
    print("Наименьшее =", a)
if b < a:
    print("Наименьшее =", b)
# b)
a = float(input("a = "))
b = float(input("b = "))

max_num = a
min_num = b

if b > a:
    max_num = b
    min_num = a

print("Наибольшее =", max_num)
print("Наименьшее =", min_num)

# 4.101
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a > b and a > c:
    print("Наибольшее = ", a)
if b > a and b > c:
    print("Наибольшее = ", b)
if c > a and c > b:
    print("Наибольшее = ", c)

if a < b and a < c:
    print("Наименьшее = ", a)
if b < a and b < c:
    print("Наименьшее = ", b)
if c < a and c < b:
    print("Наименьшее = ", c)

# 4.102
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

if a > b and a > c and a > d:
    print("Наибольшее =", a)
if b > a and b > c and b > d:
    print("Наибольшее =", b)
if c > a and c > b and c > d:
    print("Наибольшее =", c)
if d > a and d > b and d > c:
    print("Наибольшее =", d)

if a < b and a < c and a < d:
    print("Наименьшее =", a)
if b < a and b < c and b < d:
    print("Наименьшее =", b)
if c < a and c < b and c < d:
    print("Наименьшее =", c)
if d < a and d < b and d < c:
    print("Наименьшее =", d)

# 4.103
x = float(input("x = "))
if x < 0:
    x = -x
print(x)

# 4.104

x1 = float(input("x1 = "))
x2 = float(input("x2 = "))

if x1 < 0:
    x1 = -x1
if x2 < 0:
    x2 = -x2

half_sum = (x1 + x2) / 2
print("Полусумма абсолютных величин =", half_sum)

product_sqrt = math.sqrt(x1 * x2)
print("Квадратный корень из произведения абсолютных величин =", product_sqrt)

# 4.105
a = abs(float(input("a = ")))
b = abs(float(input("b = ")))

if a > b:
    a = a/2
print('a = ', a)
print('b = ', b)

# 4.106
x1 = float(input('x1 = '))
x2 = float(input('x2 = '))

if math.sqrt(x2) < x1:
    x2 = x2 * 5

print(x2)

# 4.107
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 4.108
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > 0:
    a = a**2
if b > 0:
    b = b**2
if c > 0:
    c = c**2
print(a)
print(b)
print(c)
"""
# 4.109
a = floatЗ-4.py(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if 1.6 < a < 3.8:
    print(a)
if 1.6 < b < 3.8:
    print(b)
if 1.6 < c < 3.8:
    print(c)
