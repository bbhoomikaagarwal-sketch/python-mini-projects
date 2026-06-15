print("contact book")
contacts={}
while True:
    print("menu")
    print("enter 1 add contacts")
    print("enter 2 to search contacts")
    print("enter 3 to remove contacts")
    print("enter 4 to veiw all contacts")
    print("enter 5 to exit")
    choice=int(input("enter the service required:"))
    if choice==1:
        contact=input("enter the name:")
        number=input("enter their number:")
        contacts[contact]=number
        print("contacts")
        print("contact saved succesfully")
    elif choice==2:
        contact=input("enter the name of the contact to find:")
        if contact in contacts:
            print(contacts[contact])
        else:
            print("not in your contacts")
    elif choice==3:
        contact=input("enter the name of contact to be removed:")
        if contact in contacts:
          del contacts[contact]
          print("contacts removed successfully")
        else:
            print("no contacts found")
    elif choice==4:
        for contact in contacts:
            print(contact,":",contacts[contact])
    elif choice==5:
        break
    else :
        print("invalid")