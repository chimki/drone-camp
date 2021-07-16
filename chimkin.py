name = input("what is your name")
age = int(input("how old are you"))
thirty = 30 - age
if 30 > age:
    print(f"{name} is {thirty} ypunger than thirty")
elif 30<age:
    print(f"{name} is {-thirty} years older than 30")
else:
    print(f"{name} is 30")