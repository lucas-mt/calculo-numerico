from Métodos import *

def resolução(met, função, precisão, a1, phi='', b1=0):
    if met == 'bissecção':
        print(f'''{"a+".center(10) if resolva(função, a1) > 0 else "a-".center(10)}|{"b+".center(10) if resolva(função, b1) > 0 else "b-".center(10)}|{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}|{"-"*10}|{"-"*10}''')
        while True:
            x_ = bissecção(a1, b1)
            print(f'{a1:.7f}|{b1:.7f}|', end='')
            if abs(resolva(função, x_)) < precisão:
                print(f'{x_:.7f}|{resolva(função, x_):.7f}')
                break
            elif resolva(função, a1)*resolva(função, x_) > 0:
                a1=x_
            else:
                b1=x_
            print(f'{x_:.7f}|{resolva(função, x_):.7f}')
        return x_

    elif met == 'falsa posição':
        print(f'''{"a+".center(10) if resolva(função, a1) >= 0 else "a-".center(10)}|{"b+".center(10) if resolva(função, b1) >=0 else "b-".center(10)}|{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}|{"-"*10}|{"-"*10}''')
        while True:
            x_ = falsa_posição(a1, b1, função)
            print(f'{a1:.7f}|{b1:.7f}|', end='')
            if abs(resolva(função, x_)) < precisão:
                print(f'{x_:.7f}|{resolva(função, x_):.7f}')
                break
            elif resolva(função, a1)*resolva(função, x_) > 0:
                a1=x_
            else:
                b1=x_
            print(f'{x_:.7f}|{resolva(função, x_):.7f}')
        return x_

    elif met == 'ponto fixo':
        print(f'''{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}''')
        xn = resolva(phi, a1)
        while True:
            sol_x0 = resolva(função, xn)
            print(f'{xn:.7f}|{sol_x0:.7f}')
            if abs(sol_x0) <= abs(precisão):
                return xn
            xn = resolva(phi, xn)

    elif met == 'newton-raphson':
        print(f'''{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}''')
        while True:
            sol_x0 = resolva(função, a1)
            print(f'{a1:.7f}|{sol_x0:.7f}')
            if abs(sol_x0) <= abs(precisão):
                return a1
            a1 = Newton_Raphson(a1, função)

    elif met == 'secante':
        print(f'''{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}''')
        while True:
            sol_x0 = resolva(função, a1)
            sol_x1 = resolva(função, b1)
            print(f'{a1:.7f}|{sol_x0:.7f}')
            if abs(sol_x0) <= abs(precisão):
                return a1
            print(f'{b1:.7f}|{sol_x1:.7f}')
            if abs(sol_x1) <= abs(precisão):
                return b1
            a1 = secante(a1, b1, função)
            b1 = secante(a1, b1, função)
