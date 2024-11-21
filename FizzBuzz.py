for i in range(0,101,1):
    if(i%3==0 and i%5==0):
        print("fizz Buzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("BUZZ")
    else:
       print(i)