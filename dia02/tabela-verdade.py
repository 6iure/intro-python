#Booleanos 
True
False

condicao = 12 > 18

if condicao:
    print("isso é vdd")

else:
    print("isso nunca vai aocntecer")

# %%
    
idade = int(input("Entre com a sua idade: "))
cnh = input("Você tem CNH? ")

if idade >= 18 and cnh == "sim":
    print("siga em frente")

else:
    print("preso em nome da lei")

condicao = idade >= 18 and cnh == "sim"
print(condicao)

# %%
 
## o true é 1 
## false  é 0

print(True * 100)
print(False * 100)

#%%

## Representa o AND em lógica booleana
print(True * True)
print(True * False)
print(False * True)
print(False * False)

## representa a mesma coisa de cima
print(1*1)
print(1*0)
print(0 * 1)
print(0 * 0)

# %%

## Representa o OR em lógica booleana
print("True ou True =", bool(1 + 1))
print("True ou False =", bool(0 + 1))
print("False ou True =", bool(1 + 0))
print("False ou False =", bool(0 + 0))

# %%
