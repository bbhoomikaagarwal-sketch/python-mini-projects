print("calculator")
def add(a,b):
      return a+b
def sub(a,b):
      return a-b
def mul(a,b):
      return a*b
def div(a,b):
      return a/b
while True:
  print("menu")
  print("enter 1 to add two numbers:")
  print("enter 2 to subtract two numbers:")
  print("enter 3 to multiply two number:")
  print("enter 4 to divide two numbers:")
  print("enter 5 to exit")
  choice=int(input("enter the option for ur arithmatic operation:"))
  if choice==1:
    a=int(input("enter the first number to add:"))
    b=int(input("enter the second number to add:"))
    print("the addition of two numbers is:",add(a,b))
  elif choice==2:
    a=int(input("enter the first number to sub:"))
    b=int(input("enter the second number to sub:"))
    print("the subraction of two numbers is:",sub(a,b))
  elif choice==3:
    a=int(input("enter the first number to mutiply:"))
    b=int(input("enter the second number to multiply:"))
    print("the multiplication of two numbers is:",mul(a,b))
  elif choice==4:
    a=int(input("enter the first number to divide:"))
    b=int(input("enter the second number to divide:"))
    if b==0:
        print("the division is not possible")
    else:
        print("the division of two numbers is:",div(a,b))
  elif choice==5:
      break
  else:
      print("inavlid choice")
  
  
  