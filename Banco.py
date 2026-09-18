saldo = 2000
opcao = 0

while opcao != 4:

    print ("\nCaixa Eletrônico")
    print ("1 - Consultar Saldo")
    print ("2 - Depositar")
    print ("3 - Sacar")
    print ("4 - Sair")
    
    opcao = int(input("Escolha uma opção "))
    
    if opcao == 1:
        print ("O saldo atual é de, ", saldo)
    
    elif opcao == 2:
        deposito = float(input("Qual o valor do deposito? "))
        saldo += deposito
        print ("O seu saldo atual é de, ", saldo)
                        
    elif opcao == 3:
        sacar = float(input("Qual e o valor do saque? "))
        saldo -= sacar
        print ("O seu saldo atual é de, ", saldo)
    
    elif opcao == 4:
        print ("Atendimento Encerrado!")
        print ("Obrigado pela preferência!")
        