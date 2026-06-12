      #welcome to peoples bank
print("welcome to people's bank")
balance=0
transactions=0
while True:
    print("enter 1 to check the balance")
    print("enter 2 to deposit the money")
    print("enter 3 to withdraw your money")
    print("enter 4 to exit")
    print("enter 5 to see the transaction history")
    choice=int(input("enter the number for your service:"))
    if choice==1:
      print("your balance is:",balance)
    elif choice==2:
      amount=int(input("the amount is:",))
      balance+=amount
      transactions+=1
      print("deposited successfully")
      print("current balance is:",balance)
    elif choice==3:
      amount=int(input("enter the amount to withdraw:"))
      if amount<=balance:
       balance-=amount
       transactions+=1
       print(amount,"withdrawn successfully")
       print("Current balance is:", balance)
      else :
       print("insufficient funds")
    elif choice==4:
      break
    elif choice==5:
      print("total transactions:",transactions)
    else:
      print("invalid option")




    
      
