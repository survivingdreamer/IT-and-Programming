print('Введите коэффициенты квадратного уравнения', 'Введите коэффициент a', sep='\n')
a=float(input())
print('Введите коэффициент b')
b=float(input())
print('Введите коэффициент c')
c=float(input())

D=b ** 2 - 4 * a * c;
print('Дискриминант =', D)

if D < 0:
    print('Дискриминант < 0, корней нет')
elif D > 0:
    print('Дискриминант > 0, уравнение имеет два корня')
    x1=(-b + D ** 0.5) / 2 * a
    x2=(-b - D ** 0.5) / 2 * a
    print('Первый корень уравнения:', x1, 'Второй корень уравнения:', x2, sep='\n')
else:
    print('Дискримимнант = 0, уравнение имеет один корень')
    x=-b / 2 * a
    print('Корень уравнения:', x, sep='\n')
