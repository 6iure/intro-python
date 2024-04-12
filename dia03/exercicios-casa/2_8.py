notas = []

for i in range(4):
    a = int(input(f"entre com a nota {i+1}: "))
    notas.append(a)

media = sum(notas) / 4

print("a média das notas foi:", media)

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