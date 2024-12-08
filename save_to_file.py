def save_to_file(contacts):
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")