def valida_entrada():
    while True:
        try:
            numero = int(input("entre com um numero entre 1 e 15: "))
        
        except ValueError:
            print("entre com numeros, e não strings!")
            continue

        if 1 <= numero <= 15:
            return numero
        
        else:
            print("entre com um número válido")


numero_sorte = 7

for i in range(3):

    numero = valida_entrada()

    if numero == numero_sorte:
        print("você acertou!")
        break

    elif numero > numero_sorte:
        print("você errou, tente um numero menor!")

    else:
        print("você errou, tente um numero maior!")
