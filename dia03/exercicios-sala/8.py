a1 = int(input("Entre com a altura em cm 1: "))
a2 = int(input("Entre com a altura em cm 2: "))
a3 = int(input("Entre com a altura em cm 3: "))
a4 = int(input("Entre com a altura em cm 4: "))

alturas = [a1, a2, a3, a4]

soma = sum(alturas)

print(soma)

# %% 

#!usando FOR

alturas = []

for i in range(4):
    a = int(input(f"entre com a altura em cm {i+1}: "))
    alturas.append(a)

soma = sum(alturas)
print(soma)
# %%
