from math import floor
from decimal import Decimal

class SPF:
    def __init__(self, base, n, emin, emax):
        self.base = base
        self.casas = n
        self.expmin = emin
        self.expmax = emax
    def SPFmin(self):
        mm = '0.1'+'0'*self.casas+'*'+f'{self.base}**{self.expmin}'
        return mm
    def SPFmax(self):
        MM = '0.'+f'{self.base-1}'*self.casas+'*'+f'{self.base}**{self.expmax}'
        return MM
    def SPFrepr(self, num):
        if float(num) >= 1:
            exp = len(num.replace('0.', ''))
            vlr = str(float(num)/(10**(exp)))
        elif float(num) < 1:
            exp = 0
            vlr = str(float(num)*(10**(exp)))
            while True:
                vlr = str(float(num)*(10**(exp)))
                if eval(vlr) > 1:
                    exp -= 1;vlr = str(float(num)*(10**(exp)))
                    exp *= -1
                    break
                exp+=1
        res = round(Decimal(vlr), self.casas)
        num_spf = f'{res}'+'*'+f'{self.base}**{exp}'
        if eval(num_spf) > eval(self.SPFmax()):
            return num_spf, 'OverFlow'
        if eval(num_spf) < eval(self.SPFmin()):
            return num_spf, 'UnderFlow'
        return num_spf
