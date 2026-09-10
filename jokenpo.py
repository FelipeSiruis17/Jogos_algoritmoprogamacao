import random



print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura", "Fogo"]
chances = 0





while chances < 3:
    jogador = str(input("Escolha entre Pedra, Papel, Tesoura, Fogo : ").capitalize())

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    chances += 1
    print ("Chances restantes:", 3 - chances)

    pc = random.choice(opcoes)

    print("O computador escolheu:", pc)


    if jogador == pc:
        print("Empate!")
    elif jogador == "Pedra":
        if pc == "Tesoura":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Papel":
        if pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Tesoura":
        if pc == "Papel":
            print("Você venceu!")
    elif jogador == "Fogo":
        if pc == "Tesoura":
            print("Você venceu!")
    elif jogador == "Fogo":
        if pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
  
      
