opcao = 0

while opcao != 5:
    
    print ("Calculadora")
    print ("1 - SOMAR")
    print ("2 - Subtrair")
    print ("3 - Multiplicar")
    print ("4 - Dividir")
    print ("5 - Sair")
    
    opcao = int(input("Escolha uma opção:" ))
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if opcao == 1:
        
        soma= numero1+numero2
        print ("O resultado da sua soma é =", soma)
        break
    elif opcao == 2:
        sub = numero1 - numero2
        
        print ("O resultado da sua subtração é =", sub)
        break
    elif opcao== 3:
        print("Vamos MULTIPLICAR!")
        mult = numero1*numero2
        
        print ("O resultado da sua multiplicação é =", mult)
        break
    elif opcao == 4:
        print ("VAMOS DIVIDIR!")
        div = numero1/numero2
        print ("O resultado da sua divisão é =", div)
        break
    elif opcao == 5:
        break
    
    else:
        print ("Escolha uma opção válida, Entre 1 e 5")

        
        
    
        
    
    