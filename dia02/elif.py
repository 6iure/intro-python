idade = int(input("Entre com a sua idade: "))

if idade < 18:
    print("você é menor de idade!")
    print("va para casa beber leite!")

elif idade > 80:
    print("cuidado, você já ta meio velho!")

else:
    print("você é de maior")
    print("beba a vontade")

# %% método diferente

idade = int(input("Entre com a sua idade: "))

if 18 <= idade <= 89:
    print("você é maior de idade!")
    print("beba a vontade")

elif idade >= 90:
    print("cuidado com a bebida, você ta meio velho!")

else:
    print("você é uma criança!")
