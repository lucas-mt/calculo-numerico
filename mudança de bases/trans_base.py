from DecBases import *
from OutrasBases import *

operação = int(input('''o que você deseja? 
mudar base 10 para outra base [1];
mudar de outra base para a base 10 [2];
mudar de um base para outra sem ser decimal [3]: '''))

def ponto(vlr):
    if '.' not in vlr:
        return str(f'{vlr}.0')
    return vlr

if operação == 1:
    vlr = float(input('número> '))
    base = int(input('Base de transformação> '))
    if base == 2 or base == 8:
        print(BaseBinOct(vlr, base))
    elif base == 16:
        print(BaseHex(vlr))
elif operação == 2:
    vlr = input('número> ')
    base = int(input('Base de origem> '))
    if base == 2 or base == 8:
        print(Dec_BinOct(ponto(vlr), base))
    elif base == 16:
        print(Dec_Hex(ponto(vlr.upper())))
elif operação == 3:
    vlr = input('número> ')
    baseorigem = int(input('base de origem> '))
    basetrans = int(input('base de transformação> '))
    if baseorigem == 2 or baseorigem == 8:
        vlr_dec = Dec_BinOct(ponto(vlr), baseorigem)
    elif baseorigem == 16:
        vlr_dec = Dec_Hex(ponto(vlr.upper()))
    if basetrans == 2 or basetrans == 8:
        print(BaseBinOct(vlr_dec, basetrans))
    elif basetrans == 16:
        print(BaseHex(vlr_dec))
