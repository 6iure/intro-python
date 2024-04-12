tipoSorvete = input("escolha um tipo de sorvete entre: casquinha, cascão ou cestinha! ").lower()
sabor = input("agora escolha um sabor entre os sabores napolitanos! ").lower()
tipoCobertura = input("e por final escolha uma cobertura entre: caramelo, chocolate, morango ou sem cobertura! ").lower()


sorvetes = {
    'casquinha':1.00,
    'cascão':2.50,
    'cestinha':4.00
}

valor = 0

if tipoSorvete in sorvetes:
    valor += sorvetes[tipoSorvete]

else:
    print("seu pedido virá errado!")

#parte da cobertura

coberturas = {
    "caramelo":1.5,
    "morango":1.5,
    "chocolate":1.5,
    "":0
}

if tipoCobertura in coberturas:
    valor += coberturas[tipoCobertura]

else:
    print("sua coberturá vira errada!")

print("seu sorvete", tipoSorvete, "de", sabor, "com cobertura de", tipoCobertura, "custará", valor)