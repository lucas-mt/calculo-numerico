from math import floor

def arm_num(num, dicio):
    if 0 <= num < 10:
        return str(num)
    else:
        for i, j in dicio.items():
            if j == num:
                return i

def BaseBinOct(num, base):
    parte_inteira = floor(num)
    parte_fracionada = num - parte_inteira
    num_int = []
    num_float = []

    while True:
        div = parte_inteira//base
        num_int.append(str(parte_inteira-(div*base)))
        parte_inteira = div
        if parte_inteira < base:
            num_int.append(str(abs(div)))
            break
    while True:
        mult = parte_fracionada*base
        num_float.append(str(floor(mult)))
        parte_fracionada = mult - floor(mult)
        if parte_fracionada == 0:
            break

    num = float(''.join(num_int[::-1])+'.'+''.join(num_float))
    return num

def BaseHex(num):
    parte_inteira = floor(num)
    parte_fracionada = num - parte_inteira
    num_int = []
    num_float = []
    hex_equi = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    while True:
        div = parte_inteira//16
        resp = parte_inteira-div*16
        num_int.append(arm_num(resp, hex_equi))
        parte_inteira = div
        if parte_inteira < 16:
            num_int.append(arm_num(div, hex_equi))
            break
    while True:
        mult = parte_fracionada*16
        num_float.append(arm_num(floor(mult), hex_equi))
        if parte_fracionada ==0:
            break
        parte_fracionada = mult - floor(mult)
        
    num = ''.join(num_int[::-1])+'.'+''.join(num_float)
    return num
    