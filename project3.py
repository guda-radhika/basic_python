print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
    
print("welcome to Treasure Island.")
print("your mission is find the treasure.")
where=input("you're at the cross road where do want to go? type left or right:")
if where=="right":
    print("you got attacked by beast . Game Over")
elif where=="left":
    go=input("do you wanna swim or wait?type swim or wait:")
    if go=="swim":
        print("you got attacked by crocodile.")
        print("Game over.")
    elif go=="wait":
        door=input("which door do you want to choose? Red, Blue or Yellow?:")
        if door=="red":
            print("go got attacked by angry troat")
            print("game over.")
        elif door=="Blue":
            print("you fell into a hole.")
        elif door=="yellow":
            print("woohoo! you finally found the treasure.you win!")
        else:
            print("enter the right input")
    else:
        print("you have entered wrong input")
else:
    print("please type the correct input")        