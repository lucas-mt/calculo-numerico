from SPF import SPF

base = int(input('base> '))
n = int(input('precisão> '))
expmin = int(input('menor expoente> '))
expmax = int(input('maior expoente> '))

spf = SPF(base, n, expmin, expmax)

opções = input('''escolha:
Maior representação possível [m];
menor representação possível [M]:
transformação no sistema [t]: ''')

if opções == 'm':
    print(spf.SPFmin())
elif opções == 'M':
    print(spf.SPFmax())
elif opções == 't':
    num = input('valor> ')
    print(spf.SPFrepr(num))
    