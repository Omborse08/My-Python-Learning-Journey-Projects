print("===Contact Book===")
contacts_names = []
contacts_numbers = []

while True:
    print("\n1.Add New Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Exit")
    option = int(input("> Choose Option: "))
    match option:
        case 1:
            name_contact = input("Enter Your Name: ")
            capital_name = name_contact.capitalize()
            contacts_names.append(capital_name)
            number_contact = int(input("Enter Your Number +91 "))
            contacts_numbers.append(number_contact)
            print("> Contact Info Saved.")
        
        case 2:
            for info in range(len(contacts_names)):
                print("> ",contacts_names[info],":",contacts_numbers[info])

        case 3:
            search_contact = input("Enter name to Search: ")
            capital_search = search_contact.capitalize()
            if capital_search in contacts_names:
                search = contacts_names.index(capital_search)
                print("> ",contacts_names[search],":",contacts_numbers[search])

        case 4:
            print("Thank You For Using Our App.")
            break
