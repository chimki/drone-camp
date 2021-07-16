word = input("what word>")
geuss = ""
for i in range(len(word)):
    if word[i].isalpha():
        geuss += "_"
    else:
        geuss += word[i]
lives = 8
r = True
while lives>0:
    print(geuss)
    if "_" not in geuss:
        print("you win!!!!")
        break
    letter = input("choose letter>")
    if letter in word:
        newgeuss = ""
        for i in range(len(word)):
            if word[i] == letter:
                newgeuss += word[i]
            else: 
                newgeuss += geuss[i]
        geuss=newgeuss
    else:
        lives = lives-1
        print(lives)



            

