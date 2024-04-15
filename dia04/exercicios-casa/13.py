# fat = num*n
# fat de 3 = (3*2)(3*1)

num = int(input("Digite um número: "))

# for i in num:
#     while num > 1:
#         num * num-1
# print("fatorial de", num, "é", i)

fat = 1
for i in range(1, num + 1):
    fat *= i

print("fatorial de", num, "é", fat)




 
