cebolinha = 0
gohan = 0
athena = 0

opcao = 0 

while opcao != 4:
    
    print ("\n=========VOTAÇÃO=========")
    print ("1 - Cebolinha")
    print ("2 - Gohan")
    print ("3 - Athena")
    print ("4 - Encerrar Votação")
    
    opcao = int(input("Escolha o seu voto " ))
    
    if opcao == 1:
        cebolinha += 1
        
    elif opcao == 2:
        gohan += 1
        
    elif opcao == 3:
        athena += 1
        
    elif opcao == 4:
      
        print ("\nVotação encerrada!")
        media = (cebolinha+gohan+athena)/3
        if cebolinha > gohan and athena:
            print ("O ganhador da Eleição foi Cebolinha!")
        elif gohan > cebolinha and athena:
            print ("O ganhador da Eleição foi Gohan!")
        elif athena > cebolinha and athena:
            print ("O ganhador da Eleição foi Athena!")
        else:
            cebolinha == gohan == athena
            print ("Empate")
        print ("Os votos de Cebolinha foi =", cebolinha)
        print ("Os votos de Gohan foi =", gohan)
        print ("Os votos de Athena foi =", athena)
        
        print ("A média de votos é," , media)
        
    else:
        print ("Escolha uma opção válida")
    
    # faça o total de votos e a media de votos
    # mostre quem foi o ganhador da eleicao
    

        