numero = int(input("entre com um numero entre 1 e 15: "))

numero_sorte = 7

if numero == numero_sorte:
    print("você acertou!")

elif numero > numero_sorte:
    print("você errou, tente um numero menor!")

else:
    print("você errou, tente um numero maior!")