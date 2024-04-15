for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        div35 = "FizzBuzz"
        print(div35)
    
    elif i % 3 == 0:
        div3 = "Fizz"
        print(div3)

    elif i % 5 == 0:
        div5 = "Buzz"
        print(div5)

    else:        
        print(i)