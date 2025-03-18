print("welcome to roller coster  ride")
height=int(input("enter your height in cm?:"))
bill=0
if height>=120:
    print("you can ride the roller coaster")
    age=int(input("enter your age?:"))
    if  age<=12:
        bill+=5
        print("child ticket cost $5")
    elif age<=18:
        bill+=7
        print("youth ticket cost $7")
    elif age>=45 and age<=55:
        print("everything is going to be. Have a free ride on us!")
    else:
        bill+=12
        print("adult ticket cost $12")
    
    wants_photo=input("do you want photo?Type Y for Yes and N for No:")
    if wants_photo=="Y":
        bill+=3
    print("your final bill is",bill)
else:
    print("sorry you have to grow to ride.")        