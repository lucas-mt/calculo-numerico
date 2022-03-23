from sympy import *

x = symbols('x')

def f(função):
    return expand(função)

def resolva(função, num):
    return float(f(função).subs(x, num))

def diff_resolva(função, num):
    return resolva(diff(função), num)

def bissecção(a, b):
    return (a+b)/2

def falsa_posição(a, b, função):
    return (a*resolva(função, b) - b*resolva(função, a))/(resolva(função, b)-resolva(função, a))

def Newton_Raphson(vlr, função):
    return vlr - (resolva(função, vlr)/diff_resolva(função, vlr))

def secante(vl0, vl1, função):
    return vl1 - (((vl1-vl0)*resolva(função, vl1))/(resolva(função, vl1)-resolva(função, vl0)))
