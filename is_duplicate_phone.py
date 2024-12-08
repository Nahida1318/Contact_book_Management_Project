def is_duplicate_phone(contacts, phone):

    for contact in contacts:
        if contact['phone'] == phone:
            return True 
    return False
