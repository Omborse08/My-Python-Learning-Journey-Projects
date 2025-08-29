inventoryList = {}
Tags_sets = set()
number = 0

while True:
    print("""\n
    1. Add Book  
    2. Update Quantity  
    3. Search Book by Title/Author  
    4. Delete Book  
    5. Show All Books  
    6. Show Unique Tags  
    7. Search Books by Genre/Tag  
    8. Exit """)
    choose_option = int(input("Choose Option: "))
    match choose_option:
        case 1:
            number += 1
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            quantity = int(input("Quantity: "))
            tags = input("Tags: ").split(",")
            Tags_sets.update(tags)
            print(f"\n> {title} Book Added Successfully")
            inventoryList1 = {
            f"book_id_00{number}":{
                'title':title,
                'author':author,
                'genre':genre,
                "quantity":quantity,
                'tags':tags
            }}
            inventoryList.update(inventoryList1)

        case 5:
            if not inventoryList:
                print("Not Available Dict")
            else:
                for i,j in inventoryList.items():
                    print(f"\n> ID: {i}")
                    print(f"Title: {j['title']}")
                    print(f"Author: {j['author']}")
                    print(f"Genre: {j['genre']}")
                    print(f"Quantity: {j['quantity']}")
                    print(f"Tags {j['tags']}")

        case 2:
            old_book = input("Enter Book Id: ")
            if old_book in inventoryList:
                print("Book Id Available.")
                quantity_new = int(input("Enter Quantity New: "))
                inventoryList[old_book]['quantity'] += quantity_new
                print("Updated Successfully")
            else:
                print("Book Id Not Available.")       

        case 3:
            search = input("Search By Title Or Author: ")
            for m,n in inventoryList.items():
                title = n['title']
                author = n['author']
                if search in title or search in author:
                    print(f"\n> ID: {m}")
                    print(f"Title: {n['title']}")
                    print(f"Author: {n['author']}")
                    print(f"Genre: {n['genre']}")
                    print(f"Quantity: {n['quantity']}")
                    print(f"Tags {n['tags']}")
            
        case 4:
            delete = input("Enter Your Book Id: ")
            if delete in inventoryList:
                inventoryList.pop(delete)
                print("deleted")
            else:
                print("Id not available")

        case 6:
            print(f"Tags: {Tags_sets}")

        case 7:
            search_tag = input("Enter Tags Here: ")
            for a,c in inventoryList.items():
                b = c['tags']
                d = c['genre']
                if search_tag in tags or search_tag in genre:
                    print(f"\n> ID: {a}")
                    print(f"\n{c['title']} By {c['author']}")

        case 8:
            print("Thanks You for Using Our Cli App")
            break

        case _:
            print("Invalid Option ")