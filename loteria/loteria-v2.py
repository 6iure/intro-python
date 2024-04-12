numero_sorte = 7

for i in range(3):

    while True:
        try:
            numero = int(input("entre com um numero entre 1 e 15: "))
            break 
        
        except ValueError:
            print("entre com numeros, e não strings!")

    if numero == numero_sorte:
        print("você acertou!")
        break

    elif numero > numero_sorte:
        print("você errou, tente um numero menor!")

    else:
        print("você errou, tente um numero maior!")


#! como funciona o try e except 
# try:
#     numero = int(input("entre com um numero entre 1 e 15: "))

# except ValueError as err:
#     print("tente entrar com um número!")
