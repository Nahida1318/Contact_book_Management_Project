def search_contacts(contacts, query):
    results =[]
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            results.append(contact)  
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Found: {contact['name']} - {contact['phone']}")
    else:
        print("No contacts found.")