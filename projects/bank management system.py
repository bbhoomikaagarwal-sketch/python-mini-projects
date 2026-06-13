      #welcome to peoples bank
print("welcome to people's bank")
balance=0
transactions=[]
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
      transactions.append(f"deposited {amount}")
      print("deposited successfully")
      print("current balance is:",balance)
    elif choice==3:
      amount=int(input("enter the amount to withdraw:"))
      if amount<=balance:
       balance-=amount
       transactions.append(f"withdrawn {amount}")
       print(amount,"withdrawn successfully")
       print("Current balance is:", balance)  
      else :
       print("insufficient funds")
    elif choice==4:
      break
    elif choice==5:
      if len(transactions)==0:
        print("no transactions yet")
      else:
        print("total transactions:",transactions)
        print("remaining balance:",balance)
    else:
      print("invalid option")




    
      
