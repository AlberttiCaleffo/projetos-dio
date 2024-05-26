print('''
    ====================
           Menu
    
    Escolha uma opção:
             
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair
    ====================
''')

saldo = saque = quantidade_de_saques = 0
extrato_saque = []
extrato_deposito = []
LIMITE_SAQUE = 500
LIMITE_DE_SAQUES = 3

while True:
    menu = input('> ')
    if menu == '1':
        deposito = float(input('Valor para deposito: R$ '))
        saldo += deposito
        extrato_deposito.append(deposito)
    elif menu == '2':
        if quantidade_de_saques == LIMITE_DE_SAQUES:
            print(f'Você ultrapassou o limite diario de saques...')
            continue
        saque = float(input('Informe o valor do saque: R$ '))
        if saque > LIMITE_SAQUE:
            print(f'Saque ultrapassou o limite... ({LIMITE_SAQUE})')
        elif saque > saldo:
            print(f'Você não tem saldo suficiente... ({saldo:.2f})')
        else:
            saldo -= saque
            extrato_saque.append(saque)
            quantidade_de_saques += 1
    elif menu == '3':
        if extrato_saque == [] and extrato_deposito == []:
            print('Não foram realizados movimetações.')
            continue
        for historico_saque in extrato_saque:
            print(f'- R$ {historico_saque}')
        for historico_deposito in extrato_deposito:
            print(f'+ R$ {historico_deposito}')
        print(f'Saldo: R$ {saldo:.2f}')
    elif menu == '4':
        break
    else:
        print('Valor invalido. Insira novamente')

print('Tenha um otimo dia :)')