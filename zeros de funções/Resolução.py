from Métodos import *

def resolução(met, função, precisão, a1, phi='', b1=0):
    if met == 'bissecção':
        fa1, fb1 = resolva(função, a1), resolva(função, b1)
        print(f'''{"a+".center(10) if fa1 > 0 else "a-".center(10)}|{"b+".center(10) if fb1 > 0 else "b-".center(10)}|{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}|{"-"*10}|{"-"*10}''')
        rep = 0
        while True:
            if rep == 0:
                x0 = bissecção(a1, b1)
                sol_x0 = resolva(função, x0)
                print(f'{a1:.7f}|{b1:.7f}|', end='')
                if sol_x0 < 0:
                    if fa1 < 0:
                        a = x0
                        b = b1
                    elif fb1 < 0:
                        a = a1
                        b = x0
                elif sol_x0 > 0:
                    if fa1 > 0:
                        a = x0
                        b = b1
                    elif fb1 > 0:
                        a = a1
                        b = x0
                print(f'{x0:.7f}|{sol_x0:.7f}')
                if abs(sol_x0) <= abs(precisão):
                    return x0
            else:
                xn = bissecção(a, b)
                sol_xn = resolva(função, xn)
                print(f'{a:.7f}|{b:.7f}|', end='')
                if sol_xn < 0:
                    if fa1 < 0:
                        a = xn
                    elif fb1 < 0:
                        b = xn
                elif sol_xn > 0:
                    if fa1 > 0:
                        a = xn
                    elif fb1 > 0:
                        b = xn
                print(f'{xn:.7f}|{sol_xn:.7f}')
                if abs(sol_xn) <= abs(precisão):
                    return xn
            rep+=1

    elif met == 'falsa posição':
        fa1, fb1 = resolva(função, a1), resolva(função, b1)
        print(f'''{"a+".center(10) if fa1 > 0 else "a-".center(10)}|{"b+".center(10) if fb1 > 0 else "b-".center(10)}|{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}|{"-"*10}|{"-"*10}''')
        rep = 0
        while True:
            if rep == 0:
                x0 = falsa_posição(a1, b1, função)
                sol_x0 = resolva(função, x0)
                print(f'{a1:.7f}|{b1:.7f}|', end='')
                if sol_x0 < 0:
                    if fa1 < 0:
                        a = x0
                        b = b1
                    elif fb1 < 0:
                        a = a1
                        b = x0
                elif sol_x0 > 0:
                    if fa1 > 0:
                        a = x0
                        b = b1
                    elif fb1 > 0:
                        a = a1
                        b = x0
                print(f'{x0:.7f}|{sol_x0:.7f}')
                if abs(sol_x0) <= abs(precisão):
                    return x0
            else:
                xn = falsa_posição(a, b, função)
                sol_xn = resolva(função, xn)
                print(f'{a:.7f}|{b:.7f}|', end='')
                if sol_xn < 0:
                    if fa1 < 0:
                        a = xn
                    elif fb1 < 0:
                        b = xn
                elif sol_xn > 0:
                    if fa1 > 0:
                        a = xn
                    elif fb1 > 0:
                        b = xn
                print(f'{xn:.7f}|{sol_xn:.7f}')
                if abs(sol_xn) <= abs(precisão):
                    return xn
            rep+=1

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
        xn = a1
        while True:
            sol_x0 = resolva(função, xn)
            print(f'{xn:.7f}|{sol_x0:.7f}')
            if abs(sol_x0) <= abs(precisão):
                return xn
            xn = Newton_Raphson(xn, função)

    elif met == 'secante':
        print(f'''{"x".center(10)}|{"f(x)".center(10)}
{"-"*10}|{"-"*10}''')
        x0, x1 = a1, b1
        while True:
            sol_x0 = resolva(função, x0)
            sol_x1 = resolva(função, x1)
            print(f'{x0:.7f}|{sol_x0:.7f}')
            if abs(sol_x0) <= abs(precisão):
                return x0
            print(f'{x1:.7f}|{sol_x1:.7f}')
            if abs(sol_x1) <= abs(precisão):
                return x1
            x0 = secante(x0, x1, função)
            x1 = secante(x0, x1, função)