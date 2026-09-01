import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts:")), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("NOTE: * indicates mandatory fields")
        print
        ("................................................................................................................................................")
        temp = []
        for j in range(cols):
            temp.append(str(input("Enter name*:")))
            if temp[j] == ' ':
                sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Enter number*:")))   
            if j == 2:
               temp.append(str(input("Enter e-mail address:")))    
            if temp[j] == '' or temp[j]  == ' ':
                temp[j] = None
            if j == 3: 
                temp.append(str(input("Enter date of birth(dd/mm/yy):")))  
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                if j ==4:
                    temp.append(str(input("Enter category(Family/Friends/Work/Others):")))
                    if temp[j] =="" or temp[j] == ' ':
                        temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return phone_book           
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