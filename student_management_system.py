print("student management system")
student={}
def add_student():
    name=input("enter the students name:")
    roll_no=int(input("enter the roll_no of student:"))
    subject=input("enter the name of the subject:")
    marks=int(input("enter the marks of the student:"))
    student[name]={
        "roll_no":roll_no,
         "subject":subject,
         "marks":marks
    }
def search_student():
    name=input("enter the name:")
    if name in student:
        print(student[name])
    else :
        print("no student found")
def remove_student():
    name=input("enter the name:")
    if name in student:
      del student[name] 
      print("student removed succesfully")
    else:
        print("student not found") 
def view_student():
    for name in student:
        print(name)
        print(student[name])
while True:
    print("menu")
    print("1.add a student")
    print("2.search a student")
    print("3.remove a student")
    print("4.view the students")
    print("5.exit")
    choice=int(input("enter the number required for your service:"))
    if choice==1:
       add_student()
    elif choice==2:
        search_student()
    elif choice==3:
        remove_student()
    elif choice==4:
        view_student()
    elif choice==5:
        break
    else:
        print("invalid")