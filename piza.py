print("welcome to python piza deliveries!")
size=input("what size do you want? S,M or L:")
pepporini=input("do you want pepporini on your pizza?Y or N:")
extra_cheese=input("do you want extra chesse? Y or N:")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("you typed the wrong inputs")
    
    
if pepporini=="Y":
    if size=="s":
        bill+=2
    else:
        bill+=3
        
        
if extra_cheese=="Y":
    bill+=1
print("your final bill is:$",bill)