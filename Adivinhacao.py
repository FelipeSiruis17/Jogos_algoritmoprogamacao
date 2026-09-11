import random

numero_secreto = random.randint(1, 10)

numero = int(input("Digite um número entre 1 e 10: "))

chance = 0 

while chance < 3:
    if numero == numero_secreto:
        print ("Você acertou!!! O número secreto era:", numero_secreto)
        break
    elif numero < numero_secreto:
        print ("O número secreto é maior que", numero)
    elif numero > numero_secreto:
        print ("O número secreto é menor que", numero)
    
    chance += 1
    if chance < 3:
        numero = int(input("Tente novamente: "))
    else:
        print ("Você errou!")

    if chance == 3:    
        restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()
        if restart == "SIM":
            chance = 0
        else:
            print (f"Você errou! O número secreto era: {numero_secreto}")
            print(f"Obrigado por Jogar!")
           
       
