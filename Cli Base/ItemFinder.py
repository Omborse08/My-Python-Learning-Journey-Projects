def line():
    print("-------------------------------")

Lost_Items = []
Found_Items = []

while True:
    print("\n1.Add Lost Item")
    print("2.Add Found Item")
    print("3.View Items")
    print("4.Search Items")
    print("5.Exit")
    choose_option = int(input("Choose Option: "))
    match choose_option:
        case 1:
            lost_item_name = input("\nEnter Item Name: ")
            lost_item_desc = input("Enter Descreption: ")
            lost_item_date = input("Enter Date:(DD/MM/YYYY): ")
            lost_item_location = input("Enter Location: ")
            lost_item_owner = input("Enter your phone number: ")
            print("\n> Your Form Submitted Successfully")
            print("> Check View Items Is Your Items Found Or Not!")
            lost = (lost_item_name,lost_item_desc,lost_item_date,lost_item_location,lost_item_owner)
            Lost_Items.append(lost)
        
        case 2:
            found_item_name = input("\nEnter Item Name: ")
            found_item_desc = input("Enter Descreption: ")
            found_item_date = input("Enter Date:(DD/MM/YYYY): ")
            found_item_location = input("Enter Location: ")
            found_item_owner = input("Enter your phone number: ")
            print("\n> Your Form Submitted Successfully")
            for k1 in Lost_Items:
                found_it1 = k1[0]
                if found_item_name in found_it1:
                    print("> Same Item Is Available Check It!")
                else:
                    print("> Not Available Yet.")
            found = (found_item_name,found_item_desc,found_item_date,found_item_location,found_item_owner)
            Found_Items.append(found)
        
        case 3:
            print("\n1.View Lost Items: ")
            print("2.View Found Items: ")
            choose_option1 = int(input("\nChoose Option: "))
            match choose_option1:
                case 1:
                    if len(Lost_Items) != 0:
                        num = 0
                        line()
                        for i in Lost_Items:
                            num += 1
                            print(f"{num}. Name: {i[0]}     Desc: {i[1]}     Date: {i[2]}     Location: {i[3]}     Contact: {i[4]}")
                        line()
                    else:
                        print("\n> No Item Availble")

                case 2:
                    if len(Found_Items) != 0:
                        num1 = 0
                        line()
                        for j in Found_Items:
                            num1 += 1
                            print(f"{num1}. Name: {j[0]}     Desc: {j[1]}     Date: {j[2]}     Location: {j[3]}     Contact: {j[4]}")
                        line()
                    else:
                        print("\n> No Item Available")
        
        case 4:
            print("\n1.Search In Found Items")
            print("2.Search In Lost Items")
            choose_option2 = int(input("\nChoose Option: "))
            match choose_option2:
                case 1:
                    Search_Found = input("\n> Search Name: ")
                    for k in Found_Items:
                        found_it = k[0]
                        if Search_Found in found_it:
                            print("\n- Available!")
                            print(f"\n  Name: {k[0]}     \n  Desc: {k[1]}     \n  Date: {k[2]}     \n  Location: {k[3]}     \n  Contact: {k[4]}")
                        
                
                case 2:
                    Search_Lost = input("\nSearch Name: ")
                    for l in Lost_Items:
                        lost_it = l[0]
                        if Search_Lost in lost_it:
                            print("\nAvailable!")
                            print(f"\n  Name: {l[0]}     \n  Desc: {l[1]}     \n  Date: {l[2]}     \n  Location: {l[3]}     \n  Contact: {l[4]}")
        
        case 5:
            print("\nThank You For Using Our Services.")
            break
                    