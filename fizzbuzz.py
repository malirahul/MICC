#Fizz Buzz

for num in range(1,51):
    if(num % 3==0 and num % 5==0):
        print("Fizz Buzz")
        continue
    elif (num % 3==0):
        print("Fizz")
        continue
    elif (num % 5==0):
        print("Buzz")
        continue
    print(num)
    

