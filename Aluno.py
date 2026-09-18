opcao = 0
notaAluno = -1
faltas = 0

while opcao != 4:

    print ("\n=====SISTEMA DE NOTAS=====")
    print ("1 - Informar Nota")
    print ("2 - Informar as faltas do aluno")
    print ("3 - Consultar Situação do aluno")
    print ("4 - Sair")
    
    opcao = int(input("Escolha uma opção "))

    if opcao == 1:
        notaAluno= float(input("Informe a nota do Aluno"))
        
        if notaAluno >= 0 and notaAluno <= 10:
            print ("\nNota Registrada com Sucesso!")
        else:
            print ("Nota Inválida")
            nota = -1
            
    elif opcao == 2:
        
        faltas = int(input("Informe a quantidade de faltas do Aluno" ))
        print ("\n Faltas Registradas com sucesso!")
    
        
    elif opcao == 3:
        
        if notaAluno == -1:
            print ("Nenhuma nota foi adicionada")
        
        elif faltas >=4:
            print ("Aluno Reprovado por falta")
            print ("Quantidade de faltas =" , faltas)
            
        elif notaAluno >= 7:
            print ("A nota do Aluno foi, ", notaAluno)
            print ("O Aluno está Aprovado")
            print ("Quantidade de faltas =" , faltas)
            
        elif notaAluno == 3 or notaAluno <7:
            print ("A nota do Aluno foi, ", notaAluno)
            print ("O Aluno está em exame")
            print ("Quantidade de faltas =" , faltas)
            
        elif notaAluno < 3:
            print ("A nota do Aluno foi, ", notaAluno)
            print ("O Aluno está reprovado!")
            print ("Quantidade de faltas =" , faltas)
            
    elif opcao == 3:
        print ("Obrigado")
    
    else:
         print ("Tente Algo Válido")
# Adiciona o mumero de presenca do aluno e se for mairo que 4 ele esta reprovado

    
    
        
