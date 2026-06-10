import random
player = input("Enter rock, paper, or scissors: ").lower()
options=["rock","paper","scissors"]
if player not in options:
    print("Invalid choice! Please enter rock, paper, or scissors.")
else:
   options=["rock","paper","scissors"]
   computer=random.choice(options)
   print("you chose:",player)
   print("computers choice:",computer)
   if player==computer:
      print("its a tie")
   elif (
      (player=="rock" and computer=="scissors")or
      (player=="scissors" and computer=="paper")or
      (player=="paper" and computer=="rock")
   ):
      print("you win")
   else:
      print("computer wins")
      