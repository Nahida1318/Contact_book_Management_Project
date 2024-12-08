def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    else:
        print("\n--------------------------------------------------------------------------")
        print("| Contacts List:                                                         |")
        print("--------------------------------------------------------------------------")
        i=1
        for contact in contacts:
            print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
        print("----------------------------------------------------------------------------------------------\n\n")