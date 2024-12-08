import save_to_file

def remove_contact(contacts, phone):
    contact = None
    for c in contacts:
        if c['phone'] == phone:
            contact = c
            break
    
    if contact:
        contacts.remove(contact)
        save_to_file.save_to_file(contacts)
        print(f"Contact with phone {phone} removed.")
    else:
        print(f"No contact found with phone number {phone}.")
