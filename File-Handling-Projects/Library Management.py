import os
class main_system:
    def welcome(self):
        print("\n=== All Books ===")
    
    def __init__(self):
        self.system = {}
        self.id = 0
    
    def oparation(funtouch_om):
        def gemini(self,*args,**Kwargs):
            print("\n=== Operation Starts ===")
            results = funtouch_om(self,*args,**Kwargs)
            print("\n=== Operation Ends ===")
            return results
        return gemini
    
    @oparation
    def addbooks(self,title,author,category):
        self.id += 1
        self.system[self.id] = {
                'Title': title,
                'Author': author,
                'Category': category
            }
        print("\n=== Book Added Successfully ===")
        
    @oparation    
    def removebook(self,removebok):
        if removebok in self.system:
            self.system.pop(removebok)
            print("Book Deleted! ")
        else:
            print("Not Available!")
        
    def searchbook(self,searchbok):
        results = list(filter(lambda x: 
            searchbok in x[1]['Title'].lower() or  
            searchbok in x[1]["Author"].lower(),    
            self.system.items()
        ))
                    
        if results:
            print("Search Results:")
            for book_id, details in results:
                print(f"ID: {book_id} | Title: {details['Title']} | Author: {details['Author']} | Category: {details['Category']}")
        else:
            print("No books found.")
       
    def showbooks(self):
        for book_id, books in self.system.items():
            print(f"> ID: {book_id} | Title: {books['Title']} | Author: {books['Author']} | Category: {books['Category']}")
  
    def savefile(self):
        with open('filterfile.txt', 'w') as file:
            for book_id, books1 in self.system.items():
                file.write(f"> ID: {book_id} | Title: {books1['Title']} | Author: {books1['Author']} | Category: {books1['Category']}\n")

No = True
lib = main_system()
if not os.path.exists("filterfile.txt"):
    open("filterfile.txt", "w").close()
    print("filterfile.txt created!")
else:
    print("filterfile.txt already exists.")
        
while True:
            print("""
        1. Add Book
        2. Remove Book
        3. Search Book
        4. Show All Books
        5. Save to File
        6. Load from File
        7. Exit""")
            try:
                choose = int(input("Choose Option: "))
                match choose:
                    case 1:
                        book_name = input("Enter Book Title: ")
                        book_author = input("Enter Author: ")
                        book_category = input("Enter Category: ")
                        lib.addbooks(book_name,book_author,book_category)
                    
                    case 2:
                        delete_book = int(input("Enter Book ID to Delete: "))
                        lib.removebook(delete_book)

                    case 3:
                        search_term = input("Search by Title/Author: ").strip().lower()
                        lib.searchbook(search_term)
                                
                    case 4:
                        lib.welcome()
                        lib.showbooks()
                        

                    case 5:
                        print(f"\nFile Saved Successfully")
                        lib.savefile()
                        
                    case 6:
                        with open('filterfile.txt','r') as read:
                            print(read.readlines())
                    
                    case 7:
                        print("\nThank You For Using Our Services! ")
                        No = False
                        break

                    case _:
                        print("\nNot Available! ")
            
            except Exception:
                print("\n> Invalid Option: ")