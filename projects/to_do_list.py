print("the to_do_list")
tasks=[]
while True:
    print("enter 1 to write tasks")
    print("enter 2 to view tasks")
    print("enter 3 to remove tasks")
    print("enter 4 to count the tasks")
    print("enter 5 to exit")
    choice=int(input("enter what u want to do:"))
    if choice==1:
        num = int(input("How many tasks do you want to add? "))
        for i in range(num):
            task = input("Enter task: ")
            tasks.append(task)
    elif choice==2:
        for i, task in enumerate(tasks, start=1):
            print(i,".",task)
    elif choice==3:
        task=input("enter the tasks to remove:")
        if task in tasks:
         tasks.remove(task)
         print("task removed successfully")
        else:
            print ("no tasks found")
    elif choice==4:
        count=len(tasks)
        print("the count of tasks is:",count)
    elif choice==5:
        break
    else :
        print("invalid")


