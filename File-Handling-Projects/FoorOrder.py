def line():
    print("----------------------------------------------")


foods = []
while True:
    print("\n1.Add Order")
    print("2.View Order")
    print("3.Show Total Bill")
    print("4.Exit")
    choose_option = int(input("Choose Option: "))
    match choose_option:
        case 1:
            food_name = input("Enter Food Name: ")
            quntity = int(input("Enter Qunt: "))
            food_price = int(input("Enter Food Price: "))
            orders = (food_name,quntity,food_price)
            foods.append(orders)
        
        case 2:
            line()
            print("Your Orders")
            print("Food         Qty       Price         Subtotal")
            for i in foods:
                sum_total = i[1] * i[2]
                print(f"{i[0]}        {i[1]}         {i[2]}          {sum_total}")
            line()

        case 3:
            total_bill = 0
            for j in foods:
                total_bill += j[2] * j[1]
            print(f"Total Bill: {total_bill}")
        
        case 4:
            print("Thank You For Using Our Service")
            break





