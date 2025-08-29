from datetime import datetime
def line():
    print("-"*50)
Store = {
  "Fruits": {"apple": 30, "banana": 10, "mango":20 },
  "Snacks": {"chips": 50, "soda": 40},
  "Electronics": {"robot":20, "laptop":50}
}
Cart7 = []
name = None
print('=== Smart Shopping Cart ===')
while True:
    print("""
1. Fruits
2. Snacks
3. Electronics
4. Checkout
5. Exit""")
    try:
      choose = (input(">> "))
      match choose:
        
        case "1":
            name = "Fruits"
        case "2":
            name = "Snacks"
        case "3":
            name = "Electronics"
        case "4":
            print("\n=== Your Cart ===")
            total = 0
            for i in Cart7:
                total += i['qty'] * i['price']
                print(f"Name: {i['name']}   Qty: {i['qty']}      Price: {i['price']}")

            print(f"Total is: ₹{total}")
            coup = input("Do you Have a (SAVE10) Coupon Use It! (y/n): ")
            print("\nCoupon Applied! ")
            cash = total
            dics = 0
            if coup == "y":
                    cash = total - 10
                    dics = 10
            tax = total * 0.10
            full = tax + cash
            print("\nCalculation Final Bill...")
            print(f"Tax (10%): {tax}")
            print("Discount: ",dics)
            print(f"Final Total: {full}")
            print("📁 Saving bill to 'bill.txt'...")
            with open("Bill.txt","w") as file:
                file.writelines(f"\nBill - ({datetime.now()})")
                for i in Cart7:
                    file.writelines(f"\nName: {i['name']}   Qty: {i['qty']}      Price: {i['price']}")
                line()
                file.writelines(f"\nTax (10%): {tax}")
                file.writelines(f"\nFinal Total: {full}")
                print("✅ Bill saved successfully to 'Bill.txt'")

            break
        case "5":
              print("\nThanks For Reaching Us! ")
              break   
        case _:
              print("\nInvalid Key! ")
    except Exception:
        print("\nInvalid Option! ")
        break

    while True:
            for item, stock in Store[name].items():
                print(f"- {item} ₹{stock}")
            cart = input("\nEnter Items To Add: ")
            qty = int(input("Enter Qty: "))
            if cart in Store[name]:
                print(f"\n> {cart} Added To Cart")
                money = Store[name]
                cto = money[cart]
                Cart1 = {
                    "name":cart,
                    "price":cto,
                    "qty":qty
                        }
                Cart7.append(Cart1)
                again = input("Do you want to add more (y/n): ")
                match again:
                    case "y":
                        print("\n> Shop Again! ")

                    case "n":
                        break
            else:
                print("\n> Not Available Try Again! \n")
