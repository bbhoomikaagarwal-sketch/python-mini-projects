import random
player=input("do you want to roll the dice (yes or no):")
while player=="yes":
    dice=random.randint(1,6)
    print("the number on dice is:",dice)

    player=input("roll again(yes or no):").lower()

print("exit")