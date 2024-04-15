palavra = input('digite uma palavra: ')

tamanho = len(palavra)
invertida = ''

for indice in range(tamanho -1, -1, -1):
    invertida = invertida + palavra[indice]

print("a palavra invertida é:", invertida)