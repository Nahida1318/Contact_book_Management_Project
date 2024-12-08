import menu,add_contact,view_contacts,remove_contact,search_contacts,load_from_file

contacts=[]

while True:
    contacts=load_from_file.load_from_file()

    menu.menu()

    choice = input("Select any number : ")

    if choice == "1":  
        add_contact.add_contact(contacts)

    elif choice == "2":  
        view_contacts.view_contacts(contacts)

    elif choice == "3":
        phone = input("Enter the phone number of the contact to remove: ")
        remove_contact.remove_contact(contacts, phone)

    elif choice == "4":  
        query = input("Enter name or phone to search: ")
        search_contacts.search_contacts(contacts, query)

    elif choice == "5": 
        print("Exiting program.Thanks for using.")
        break
    
    else:
        print("Invalid option. Please try again.")
        
        
    