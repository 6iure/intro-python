idade = int(input("Digite sua idade: "))

if idade < 18:
    print("fulano, você não pode dirigir nem beber! ")

elif idade >= 18 and idade <= 65:
    print("fulano, bebida liberada! Só não vale dirigir!")

else: 
    print("fulano, beba com muita moderação!")