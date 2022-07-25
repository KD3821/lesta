'''
Python 3.8
Четность числа определятся рекурсивным вычитанием числа 2 из заданного числа до момента пока не наступит базовый случай.
Плюсы - рекурсия эффективно используется в алгоритмах сортировки
Минусы - время работы алгоритма больше из-за рекурсии и потребление памяти выше
Ваша функция работает быстро и не потребляет памяти
'''
def myEven(x):
    if x == 0:
        return True
    else:
        e = x//2
        if x == 2:
            return True
        else:
            if x > e:
                x -= 2
                return myEven(x)
            else:
                return False







