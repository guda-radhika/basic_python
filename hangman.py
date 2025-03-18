#hang man game
import random
word_list=["aardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
word_len=len(chosen_word)
for position in range(word_len):
    placeholder+="_"
print(placeholder)
game_over=False
while not game_over:
    guess=input("guess a letter:").lower()
print(guess)
display=""
for letter in chosen_word:
    if letter==guess:
       display+=letter
    else:
        display+="_"
print(display)