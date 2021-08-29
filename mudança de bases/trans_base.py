from DecBases import *
from OutrasBases import *

operação = int(input('''o que você deseja? 
mudar base 10 para outra base [1];
mudar de outra base para a base 10 [2];
mudar de um base para outra sem ser decimal [3]: '''))

if operação == 1:
    vlr = float(input('número> '))
    base = int(input('Base de transformação> '))
    if base == 2 or base == 8:
        print(BaseBinOct(vlr, base))
    elif base == 16:
        print(BaseHex(vlr))
elif operação == 2:
    vlr = float(input('número> '))
    base = int(input('Base de origem> '))
    if base == 2 or base == 8:
        print(Dec_BinOct(vlr, base))
    elif base == 16:
        print(Dec_Hex(vlr))
elif operação == 3:
    vlr = input('número> ')
    baseorigem = int(input('base de origem> '))
    basetrans = int(input('base de transformação> '))
    if baseorigem == 2 or baseorigem == 8:
        vlr_dec = Dec_BinOct(float(vlr), baseorigem)
    elif baseorigem == 16:
        vlr_dec = Dec_Hex(vlr)
    if basetrans == 2 or basetrans == 8:
        print(BaseBinOct(vlr_dec, basetrans))
    elif basetrans == 16:
        print(BaseHex(vlr_dec))
