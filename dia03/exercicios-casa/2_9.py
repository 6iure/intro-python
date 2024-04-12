num = int(input("digite um numero e será informado se é primo: "))

if num == 2 or num == 3 or num == 5 or num == 7:
    print("o numero", num, "é primo")

elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("o numero", num, " não é primo!")

else:
    print("o número", num, "é primo")

