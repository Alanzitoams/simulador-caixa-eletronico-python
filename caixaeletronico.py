#simulador de saque eletronico do banco AMS
print('='*40)
print('{:^30}'.format('BANCO A M S'))
print('='*40)

valor= int(input(' DIGITE O VALOR VOÇÊ DESEJA SACAR: R$ '))

total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        print(f' TOTAL DE {totced} CÉDULAS DE {ced} R$')
        if ced ==50:
            ced=20
        elif ced ==20:
            ced =10
        elif ced ==10:
            ced = 5
        elif ced == 5:
            ced=1
        totced = 0
        if total == 0:
          break
print('='*43)
print(' OBRIGADO POR USAR O BANCO AMS.VOLTE SEMPRE!')
print('='*43)