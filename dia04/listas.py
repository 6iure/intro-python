# %%

minhaLista = []
print(minhaLista)

# %%

minhaLista = ["iure", "santiago", "18", "1.77"]
print(minhaLista)

# %%

notas = []
nota = 7.75

#append: adiciona um elemento no final da lista
notas.append(nota)
print(notas)

notas.append(10)
print(notas)

# o extend da a possibilidade de adicionarmos mais de um valor de uma vez na lista
notas.extend([6.6, 9.3])
print(notas)

notas = notas + [10, 2.5]
print(notas)

# %%

nomes = ["iure", "joao", "luiz"]
for i in nomes:
    print(i.title()) 

nomes.append("jose")
print(nomes)

# %%

dados = ['teo', 'calvo', 31, ['nah', 'josefina', 'elaine'], ['maria']]

exs = dados[3]
print(exs[-1])

# %%

filha = dados[-1]

filha[0][0]

# %%
