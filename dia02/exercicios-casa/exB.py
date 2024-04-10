sorvete = input("escolha um tipo de sorvete entre: casquinha, cascão ou cestinha! ")
sabor = input("agora escolha um sabor entre os sabores napolitanos! ")
cob = input("e por final escolha uma cobertura entre: caramelo, chocolate, morango ou sem cobertura! ")

valor = 0

#parte do tipo de sorvete
if sorvete == "casquinha":
    valor = valor + 1.00

elif sorvete == "cascao":
    valor = valor +  2.5

elif sorvete == "cestinha":
    valor = valor +  4.0

else:
    print("opção inválida de sorvete")

#parte da cobertura
if cob == "caramelo" or "chocolate" or "morango":
    valor += 1.5

elif cob == '':
    pass

else:
    print("escolha uma cobertura válida!")

print("seu sorvete", sorvete, "de", sabor, "com cobertura de", cob, "custará", valor)