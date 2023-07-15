menu =  """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

-> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor à depositar:"))
        
        if valor > 0:
            saldo += valor
            extrato += f'Operação: Depósito | Valor: R$ {valor:.2f}\n'
            
        else:
            print("Valor digitado é inválido !!")
            
    elif opcao == "s":
        valor = float(input("Informe o valor à sacar:"))
        
        sem_saldo = valor > saldo
        sem_limite = valor > limite
        quantidade_saques_ultrapassada = numero_saques >= LIMITE_SAQUES
        
        if sem_saldo:
            print("Operação não realizada, motivo: sem saldo suficiente para saque !")
        
        elif sem_limite:
            print("Operação não realizada, motivo: valor à sacar maior que o limite permitido por saque de R$ 500,00!")
            
        elif quantidade_saques_ultrapassada:
            print("Operação não realizada, motivo: quantidade de saques ultrapassada, volte no dia seguinte !")
            
        elif valor  > 0:
            saldo -= valor
            extrato += f'Operação: Saque | Valor: R$ {valor:.2f}\n'
            numero_saques += 1
            
        else:
            print("Valor inválido!")
            
    elif opcao == "e":
        print("\n=========== EXTRATO =========")
        print("\nNão foram realizada operações" if not extrato else extrato)
        print(f"\nSaldo na conta: R$ {saldo:.2f}")        
        print("\n============================")
        
    elif opcao == "q":
        break
    
    else:
        print("operação nao existente !!")