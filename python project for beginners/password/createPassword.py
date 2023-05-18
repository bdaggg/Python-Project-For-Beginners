import random

randlist = ["0","1","2","3","4","5","6","7","8","9",
"A","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", 
",",".",";",":","?","!","#","!","+","-","_","*","&","/","=","{","}","[","]",")","("]

newRandList = []

print("enter the desired password length: ")
length = int(input())

a = 0
while a<5:
    password = ""
    x = 0
    while x < length:
        random.shuffle(randlist)
        password += randlist[0]
        x+=1   
    newRandList.append(password)
    a += 1
counter = 1
for i in newRandList:
    print(counter,". option: ",i)
    counter+=1