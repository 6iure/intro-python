venda = input("escolha entre água mineral ou agua com gás: ")

quantia = int(input("quantas aguas você deseja? "))

total = 0

if venda == "agua mineral":
    total = 1.5 * quantia

elif venda == "gas":
    total = 2.5 * quantia

else: 
    print("a sua escolha nao esta no cardapio!")

print("o valor será", total)