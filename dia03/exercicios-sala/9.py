total = 0

while True:
    entrada = input("digite alguns valores: ")

    if entrada == "":
        break
        
    total += float(entrada)

print(total)