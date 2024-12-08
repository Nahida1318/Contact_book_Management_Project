def load_from_file():
    contacts = []
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                name, email, phone, address = line.strip().split(',')
                contacts.append({'name': name, 'email': email, 'phone': phone, 'address': address})
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact list.")
    return contacts


