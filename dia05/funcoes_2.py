# %% 

#! a partir do *, todos outros argumetnos passados serão jogados no num

def operacao(op, *num):
    total = 0

    if op == "soma":
        for i in num:
            total += i

    elif op == "mult":
        total = 1
        for i in num:
            total *= i

    return total

operacao("mult", 1,2,3,4,5,6,7,8,9,10)

# %%

dados = ['teo', 'calvo', 21, ['oi', 'ai', 'haha']]

nome, sobrenome, *_, ex  = dados

print(nome)
print(sobrenome)
print(ex)

# %%

a = 10
b = 20
print(a, b)

a, b = b, a

print(a, b)

# %%

x = 10, 20
type(x)