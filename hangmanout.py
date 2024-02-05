import random
import sys
def game():
    chances = 10
    li = ["apple", "mango", "hitler", "sai tejasri"]
    word = random.choice(li)
    guesses = ''
    # Total characters the user gussed so far
    for i in range (0,int(len(word)/2)):
        a = random.randint(0,len(word))
        guesses = guesses+ str(word[a])
    while chances >0:
        won = True
        for ch in word:
            if ch in guesses: # the person has guessed
                print(ch, end = " ")
            else:
                print("_",end =" ")
                won = False
        if won :
            print("/nHurray !! You won the game")
            print(f" Your score - {chances *10}")
            begin()    
       # take a guess from the user
        guess = input("/nGuess a character: ")
        guesses += guess

        if guess not in word:
            chances -=1
            print("/nWrong answer")
            print(f"you have {chances} left")
            if chances == 0 :
                print("/nOho!! You lost the game. ")
                print(f"Your score is {chances}")
                break

                
def begin():
    start = input("Would You like to play. Enter y else N :")
    if start=="y" or start== "Y":
        game()
    elif start== "n" or start =="N":
        print("Bye Bye!!")
        exit()

name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the Hang man out game.")
begin()

