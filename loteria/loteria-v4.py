import random

def check_input():
    try:
        return int(input("entre com um numero entre 1 e 15: "))

    except ValueError:
        return "entre com numeros, e não strings!"


def check_interval(numero):
    '''checa se o numero passado esta no intervalo entre 1 e 15.
    numero: int
    '''
    
    return 1 <= numero <= 15
        
def valida_entrada():
    """essa função valida a entrada do usuario para garantir a integridade do código"""
    
    while True:

        numero = check_input()

        if type(numero) != int:
            print(numero)
            continue

        if check_interval(numero):
            return numero


numero_sorte = random.randint(1, 15)

for i in range(3):

    numero = valida_entrada()

    if numero == numero_sorte:
        print("você acertou!")
        break

    elif numero > numero_sorte:
        print("você errou, tente um numero menor!")

    else:
        print("você errou, tente um numero maior!")
