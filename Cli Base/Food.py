import os
class foodies:

    def __init__(self):
        self.shop = {
            "pizza":250,
            "burger":150,
            "pasta":200,
            "fries":80
        }
        self.food = {}
        self.prices = 0
        self.id = 0

    def omborse(shal):
        def mpl(self,*args,**kwargs):
            print("-"*50)
            funny = shal(self,*args,**kwargs)
            print("-"*50)
            return funny
        return mpl
    
    @omborse
    def look(self):
        num = 0
        for a,b in self.shop.items():
            num += 1
            print(f"{num}. {a} - ₹{b}")

    def remove_food(self,remove):
        if remove in self.food:
            self.food.pop(remove)
            print(f"\n> Id No: {remove} Item Removed!")
        else:
            print("\nNot Available")

    def final_ord(self):
        income = 0
        for numbers,foods in self.food.items():
            income += foods['Price']
            self.prices = income
            print(f"{numbers}. {foods['Food']} - ₹{foods['Price']}")
    
    def billsaves(self):
        with open('BillFile.txt','w',encoding='utf-8') as file:
            file.write(f"Your Bill: {self.prices}\n")
            for numbers1 , foods1 in self.food.items():
                file.write(f"> Sr No: {numbers1} | Food: {foods1['Food']} | Price: ₹{foods1['Price']}\n")
        print("\n> Bill Saved Successfully")
    
    def disco(self):
        apply_disco = lambda d: d* 0.9
        waiter.prices = apply_disco(waiter.prices)
        print(f"\nDiscounted Offer: ₹{waiter.prices}")

    def totals(self):
        print(f"Total Amount: {self.prices}")

    def orders(self,ord):
        self.yes = True
        for eat, price in self.shop.items():
            if ord == eat:
                self.id += 1
                self.food[self.id] = {
                    "Food":ord,
                    "Price":price
                }

                print("\n> Added To Your Inventory")
                self.yes = False
        if self.yes == True:
            print("\nNot Availablesss ")

# Just Learn so i thought why not i used this
class dances(foodies):
    pass


if not os.path.exists("BillFile.txt"):
    open("BillFile.txt","w").close()
    print("Bill File Created! ")
else:
    print("\nBillFile Already Exits! ") 

waiter = dances()
print("=== Welcome to Online Food Ordering System ===\n")
print('Sr  Name   Price')
waiter.look()
while True:
    order = input("Enter item to add (or 'done' to finish): ").lower()
    if order == "done":
        print("\n=== Current Order ===")
        waiter.final_ord()
        removed = input("Do you want to remove an item? (yes/no): ").lower()
        if removed == 'yes':
            try:
                remove_item = int(input("Enter item number to remove: "))
                waiter.remove_food(remove_item)
                print("\n=== Final Order ===")
                waiter.final_ord()
            except Exception:
                print("\nTry Again! ")
        waiter.totals()
        dicsount = input("Apply %10 discount? (y/n): ").lower()
        if dicsount == "y":
            waiter.disco()
        bill_save = input("Wanna Save Bill (Y/N): ").lower()
        if bill_save == "y":
            waiter.billsaves()
            print("\n=== Thank You! Visit Again ===")
            open_bill = input("Open Bill (y/n): ")
            if open_bill == "y":
                os.startfile("BillFile.txt")
            else:
                pass
            break
        else:
            print("\n=== Thank You! Visit Again ===")
            break            
    else:
        waiter.orders(order)