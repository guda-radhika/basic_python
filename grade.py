name = input()
maths = int(input())
physics = int(input())
chemistry = int(input())
total= (maths + physics + chemistry)/3
print(total)
if(total>=90):
    grade=("A grade")
elif(total>=80):
    grade=("B grade")
elif(total>=70):
    grade=("C grade")
elif(total>=60):
    grade=("D grade")
else:
    grade=("fail")
print(grade)    