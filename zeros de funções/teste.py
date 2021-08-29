from Métodos import *

função = input('> ')
a1 = float(input('> '))
b1 = float(input('> '))
precisão = float(input('> '))

print(f'''{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}''')

def sec(função, a1, b1, precisão):
    x0 = a1
    rep = 0
    while True:
        if rep < 2:
            sol_x0 = resolva(função, x0)
            print(f'{x0:.7f}|{sol_x0:.7f}|')
            if abs(sol_x0) <= abs(precisão):
                return x0
            x0 = b1
        x1, x0= x0, secante(a1, b1, função)
        if rep >= 2:
            sol_x0 = resolva(função, x0)
            print(f'{x0:.7f}|{sol_x0:.7f}|')
            if abs(sol_x0) <= abs(precisão):
                return x0
            x1, x0= x0, secante(x1, x0, função)

print(sec(função, a1, b1, precisão))
