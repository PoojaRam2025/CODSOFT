contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print("Contact added!")

    elif choice == '2':
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for name in contacts:
                print("\nName:", name)
                print("Phone:", contacts[name]['Phone'])
                print("Email:", contacts[name]['Email'])
                print("Address:", contacts[name]['Address'])

    elif choice == '3':
        name = input("Enter name to search: ").lower()
        found = False
        for contact_name in contacts:
            if contact_name.lower() == name:
                print("\nName:", contact_name)
                print("Phone:", contacts[contact_name]['Phone'])
                print("Email:", contacts[contact_name]['Email'])
                print("Address:", contacts[contact_name]['Address'])
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter name to update: ").lower()
        found = False
        for contact_name in contacts:
            if contact_name.lower() == name:
                print("Leave blank to keep current value.")
                phone = input(f"New Phone ({contacts[contact_name]['Phone']}): ")
                email = input(f"New Email ({contacts[contact_name]['Email']}): ")
                address = input(f"New Address ({contacts[contact_name]['Address']}): ")

                if phone:
                    contacts[contact_name]['Phone'] = phone
                if email:
                    contacts[contact_name]['Email'] = email
                if address:
                    contacts[contact_name]['Address'] = address

                print("Contact updated!")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == '5':
        name = input("Enter name to delete: ").lower()
        found = False
        for contact_name in list(contacts.keys()):
            if contact_name.lower() == name:
                del contacts[contact_name]
                print("Contact deleted!")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
