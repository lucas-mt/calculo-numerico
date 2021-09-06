from math import floor

def ver_int(num):
    try:
        vlr = int(num)
        return True
    except:
        return False

def trans_num(num, dicio, sig, j):
    vlr = 0
    for i in range(len(num)):
        if ver_int(num[i]):
           vlr += (int(num[i])*(16**(sig*(i+j))))
        else:
            for u, v in dicio.items():
                if u == num[i]:
                    vlr += (v*(16**(sig*(i+j))))
    return vlr

def Dec_BinOct(num, base):
    num_parte = num.split('.')
    parte_inteira_inversa = num_parte[0][::-1]
    parte_fracionada = num_parte[1]
    vlr = 0
    for i in range(len(parte_inteira_inversa)):
        vlr += (int(parte_inteira_inversa[i])*(base**i))
    for i in range(len(parte_fracionada)):
        vlr += (float(parte_fracionada[i])*(base**(-(i+1))))

    return vlr

def Dec_Hex(num):
    num_parte = num.split('.')
    num_inteiro_inverso = num_parte[0][::-1]
    num_fracionado = num_parte[1]
    vlr = 0
    hex_equi = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    vlr += trans_num(num_inteiro_inverso, hex_equi, 1, 0)
    vlr += trans_num(num_fracionado, hex_equi, -1, 1)
    return vlr
