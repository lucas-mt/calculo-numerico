from Resolução import resolução

met = input('método> ').strip().lower()

if met == 'bissecção' or met =='falsa posição' or met == 'secante':
    fc = input('função> ')
    a1, b1 = float(input('limite inferior> ')), float(input('limite superior> '))
    precisão = float(input('precisão> '))
    print(resolução(met=met, função=fc, precisão=precisão, a1=a1, b1=b1))

elif met == 'ponto fixo':
    fc = input('função> ')
    f_phi = input('phi> ')
    vlr = float(input('chute inicial> '))
    precisão = float(input('precisão> '))
    print(resolução(met=met, função=fc, precisão=precisão, phi=f_phi, a1=vlr))

elif met == 'newton-raphson':
    fc = input('função> ')
    vlr = float(input('chute inicial> '))
    precisão = float(input('precisão> '))
    print(resolução(met=met, função=fc, precisão=precisão, a1=vlr))
