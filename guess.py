import random
r = True
low = input("choose low range>")
high = input("choose high number>")
while r == True:
    if low>high:
        print("dont make the low bigger than the high")
        low = input("choose low>")
        high = input("choose high>")
    elif not low.isnumeric():
        print("put a number in")
        low = input("choose low>")
        high = input("choose high>")
        continue
    elif not high.isnumeric():
        print("put a number in")
        low = input("choose low>")
        high = input("choose high>")
        continue
    else:
        r = False
        high=int(high)
        low=int(low)

rn = random.randint(low,high)
h = True
while h == True:
    guess = (input(f"guess number {low}-{high}>"))
    if guess.isnumeric():
        guess = int(guess)
    else:
        print("put a number in")
        continue
    if guess < rn:
        print("guess higher")
        if guess < low:
            continue
        low = guess
    elif guess > rn:
        print("guess lower")
        if guess > high:
            continue
        high = guess
    elif guess == rn:
        print("you got it right!")
        h = False
    