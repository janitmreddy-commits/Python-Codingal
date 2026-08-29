import sys
def menu():
    print("********************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5.Display all contacts")
    print("6.Exit phonebook")
    choice=int (input("Enter your choice"))
    return choice
def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter your name")))
        if i == 1:
            dip.append(str(input("Enter your number")))
        if i == 2:
            dip.append(str(input("Enter e-mail address")))    
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy)"))) 
        if i == 4:
            dip.append(str(input("Enter category(Family/Friends/Work/Others):")))
    dip.append(dip)
    return pb
def display_all(pb):          
    if not pb:
        print ("List is empty:[]")
    else:
        for i in range(len(pb)):
            print(pb[i])
def thanks():
      print ("********************************************************************")
      print("Thank you for using our Smartphone directory system.")
      print("Please visit again!")
      print("********************************************************************")
      sys.exit("Goodbye, have a nice day ahead!")
      print("................................................................................")
      print("Hello dear user, welcome to our smartphone directory system")
      print("You may now proceed to explore this directory")
      print("................................................................................")
      ch = 1
      pb = initial_phonebook()
      while ch in (1,2,3,4,5):
        ch = menu()
        if ch == 1:
              pb = add_contact(pb)
        elif ch ==5:
            display_all(pb)
        else:
            thanks()