palavra = input("entre com uma palavra: ")

qtde = 0

for i in palavra:
    if i == "a":
        qtde += 1

print("a letra a aparece", qtde, "vezes na palavra", palavra)