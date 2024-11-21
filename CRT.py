
name= input("what is your name?")
age=  int(input("what is your age?"))
if(age>=18):
    print(f"{name} you are eligible to vote")
else:
    print(f"{name} come back after ",18-age,"years")
