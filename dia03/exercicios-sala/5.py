nome = input("Digite um nome, será verificado se pertence a familia calvo ou silva! ")

nome = nome.lower()

if "calvo" in nome or "silva" in nome:
    print("vc pertence a familia calvo ou silva!!")

else:
    print("vc não pertence a essas familias!")