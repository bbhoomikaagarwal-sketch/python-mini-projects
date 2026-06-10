import random
number=random.randint(1,100)
guess=0
while guess!=number:
    guess=int(input("enter a number between 1 to 100:"))
    if guess > number:
        print("too high")
    elif guess<number:
        print("too low")
    else:
        print("congratulations")

