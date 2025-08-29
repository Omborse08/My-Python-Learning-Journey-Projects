Contacts = {}
Tags_Contacts = set()
print("     ===== Welcome To Contact Book 2.0 =====")
while True:
    print("\n1. Add Contact")
    print("2. Search by Name")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Show All Unique Tags")
    print("6. Search Contacts by Tag")
    print("7. Exit")
    choose_option = int(input("Choose Option: "))
    match choose_option:
        
        case 1:
            print("\n     ==== Add Contacts ====")
            name = input("Enter Your Name: ")
            number = int(input("Enter Your Phone Number: "))
            tags = input("Enter Tags To Seprate: ").split(",")
            Tags_Contacts.update(tags)
            print("✅ Contact added!")
            Contacts[name] = {
                "number": number,
                "tags": tags
            }


        case 2:
            search_name = input("Enter Name To Search: ")
            if search_name in Contacts:
                print(f"{search_name} >>\n{Contacts[search_name]}")
            else:
                print("\n> Not Available.")

        case 3:
            delete_contacts = input("Delete By Name: ")
            if delete_contacts in Contacts:
                print("\n> Contact Deleted.")
                Contacts.pop(delete_contacts)

        case 4:
            for i in Contacts:
                print(f"\n{i} >>\n{Contacts[i]}")

        case 5:
            print(f"All Unique Tags Are: {Tags_Contacts}")
        
        case 6:
            search_tag = input("Enter Tag Here: ")
            found = False
            for j,k in Contacts.items():
                if search_tag in k["tags"]:
                    print(f"Name: {j} >> Phone No: {k['number']}")
                    found = True
            if not found:
                print("This tag is Not Available.")

        case 7:
            print("Thank You For Using Our Services.")
            break



                