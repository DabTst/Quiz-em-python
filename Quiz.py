print(" Voçe comecou um Quiz do DAB")

Resposta_jogador = input("Quer começar? S/N: ")

if Resposta_jogador != 'S':
    quit()

    pontuacao = 0

print("Começando...!")

print('Quem criou o mundo?\n(A) Deus \n(B) Jesus  \n(C) Diabo \n(C)Espirito' )
Reposta1 = input("Resposta...")

if Reposta1 == "A":
    print ("correcto")
    pontuacao = pontuacao + 10
else: 
    print("Incorrecto")


print(f"QUiz acabou... Pontuacao: {pontuacao}/100")