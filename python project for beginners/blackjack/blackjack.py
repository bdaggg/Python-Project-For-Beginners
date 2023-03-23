import random
import time

randlist= [1,2,3,4,5,6,7,8,9,10,'Q','K','J',1,2,3,4,5,6,7,8,9,10,'Q','K','J',1,2,3,4,5,6,7,8,9,10,'Q','K','J',1,2,3,4,5,6,7,8,9,10,'Q','K','J']
playerlist = list()
computerlist = list()
#print(type(playerlist))
winner = list()


def start():
    print("welcome to the casino.")
    print("enter the amount you want to deposit: ")
    bahis = int(input())
    d1 = bahis*(2)
    d2 = bahis*(3/2)
    time.sleep(1)
    print("if you keep blackjack, the amount you will earn: ",d1)
    time.sleep(1)
    print("if you don't keep blackjack, the amount you will earn: ", d2)
    time.sleep(1)
    print("the casino wishes you success.")
    time.sleep(1)
    random.shuffle(randlist)
    playerlist.append(randlist[0])
    randlist.pop(0)
    playerlist.append(randlist[1])
    randlist.pop(0)
    random.shuffle(randlist)
    computerlist.append(randlist[0])
    randlist.pop(0)
    computerlist.append(randlist[1])
    randlist.pop(0)
    a = randlist[0] 
    b = randlist[1]
    total = 0
    if a == 'Q' or a == 'K' or a == 'J': 
        x = 10  
        total += x
        print("your first card: ",a)

    else:
        total += a 
        print("your first card: ",a)

    if b == 'Q' or b == 'K' or b == 'J': 
        x = 10  
        total += x
        print("your second card: ",b)

    else:
        total += b 
        print("your second card: ",b) 

    print("the sum of your cards: ", total)
    s = 1
    a = True
    while a == True:
        print("if you want to draw a card, press 1, if not, press 2")
        y  = int(input())
        if y == 1:
            s += 1
            random.shuffle(randlist)
            x = randlist[0]
            randlist.pop(0)
            playerlist.append(x)
            print("your card is ",x)
            if x == "Q" or x == "K" or x == "J":
                total+=10
                print("the sum of your cards: ",total)  
            else:
                total += x 
                print("the sum of your cards: ",total) 
        elif y ==2:
            print("it's your computer's turn, please wait")
            winner.append(total)
            a = False
        else:
            print("incorrect input, please make the correct input.")       


        if 21 - total == 0:
            print("wow blackjack")   
            print("the amount you earn is: ",d1, " we'll wait again...")     
            a = False
            continue

        elif 21 - total < 0:
            print("you lost...")
            a = False       
            continue

    



def computer():
    total = 0
    s1 = computerlist[0]
    s2 = computerlist[1]


    if s1 == "Q" or s1 == "K" or s1 == "J":
        total += 10
    else:
        total += s1    
    
    if s2 == "Q" or s2 == "K" or s2 == "J":
        total += 10
    else:
        total += s2

    print("the computer opens its own cards: ")
    time.sleep(2)
    print("the computer cards is ",s1," and ",s2)
    time.sleep(1)
    print("the sum of computer cards: ",total)
    time.sleep(1)
    
    t = True

    while t == True:
        cond = 21 - total
        if cond == 0:
            print("the computer made blackjack.")
            t = False

        elif cond == 4 or cond == 3 or cond == 2 or cond == 1:
            print("the computer does not want to draw a card: ")
            winner.append(total)
            win()
            t = False
            break
        elif cond < 0:
            print("computer lost...")
            print("congralutation you win....")
            t = False
            break
        else:
            s = 2
            print("computer is drawing card..")
            time.sleep(1)
            random.shuffle(randlist)
            computerlist.append(randlist[0])    
            randlist.pop(0)
            s3 = randlist[s]
            s += 1
            print("the computer draw card is: ",s3)
            if s3 == "Q" or s3 == "K" or s3 == "J":
                total += 10
            else:
                total += s3
        print("sum of the computer cards: ",total)





def win():
    print("sum of the your cards: ",winner[0])
    print("sum of the computer cards: ",winner[1])
    s0 = winner[0]
    s1 = winner[1]
    if s0 == s1:
        print("the same score..")

    elif s0 > s1:
        print("congralutation you win....")

    else :
        print("you lost.......")           




def main():
    start()
    computer()


main()
