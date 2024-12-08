import is_duplicate_phone,save_to_file


def add_contact(contacts):
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    
    if not name.isalpha():
        print("Invalid name. It must be a string.")
        return

    if not phone.isdigit():
        print("Invalid phone number. It must be a number.")
        return
    
    if is_duplicate_phone.is_duplicate_phone(contacts, phone):
        print("Phone number already exists. Please try again with a different number.")
        return

    contact = {'name': name, 'email': email, 'phone': phone, 'address': address}
    contacts.append(contact)

    
    save_to_file.save_to_file(contacts)
    print("Contact added successfully!")