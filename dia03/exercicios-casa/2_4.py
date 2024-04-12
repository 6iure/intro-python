n1 = int(input("Entre com a nota 1: "))
n2 = int(input("Entre com a nota 2: "))
n3 = int(input("Entre com a nota 3: "))
n4 = int(input("Entre com a nota 4: "))

notas = [n1, n2, n3, n4]

media = sum(notas) / 4

print("a média das notas foi", media)

max = 0

for i in notas:
    if i > max:
        max = i
print("a maior nota é:", max)

min = notas[0]

for i in notas:
    if i < min:
        min = i
print("a menor nota é:", min)