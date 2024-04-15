lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# # menor = min(lista)
# # print(menor)

# # maior = max(lista)
# print(maior)

maior = lista[0]
menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print("o maior valor é:", maior)
print("o menor valor é:", menor)