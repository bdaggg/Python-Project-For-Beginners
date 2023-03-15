short_phrase = str(input("enter the phrase you want to shorten: "))
my_list = short_phrase.split()
#print(my_list): you can see your list 
shrt = ' '
for i in my_list:
    shrt = shrt + str(i[0]).upper()
print(shrt)