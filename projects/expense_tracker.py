print("Expense tracker")
expenses={}
total_expenses=0
while True:
    print("menu")
    print("enter 1 to write the expenses")
    print("enter 2 to view the expenses")
    print("enter 3 to view total expenses")
    print("enter 4 to exit")
    choice=int(input("enter the option in menu:"))
    if choice==1:
        category=input("enter the category:")
        expense=int(input("enter the amount spent:"))
        expenses[category]=expense
    elif choice==2:
        category=input("enter the category:")
        if category in expenses:
            print(f"the expense of {category} is",expenses[category])
        else:
            print("invalid category")
    elif choice==3:
        for category in expenses:
           total_expenses=total_expenses+expenses[category]
           
        print("the total expenses is:",total_expenses)
    elif choice==4:
        break
    else:
        print("invalid choice")
