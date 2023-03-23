name = input("enter your name: ")
print("welcome "+name+" if you are ready lets start hangman")

secret_word="metaverse"
lives = 4
global_guess = ""

while lives > 0:
    character_number = 0
    for i in secret_word:
        if i in global_guess:
            print(i)
        else:
            print("*")
            character_number += 1

    guess_word = input("enter a latter:")
    global_guess += guess_word[0] #ikinci asamada hata veriyor******************!!!!!!!!!***********

    if character_number == 0:
        print("you win")
        break


    if guess_word not in secret_word:
        lives -= 1
        print("wrong guess")
        print(f"you have {lives} lives")
        if lives == 0:
            print("you died")
