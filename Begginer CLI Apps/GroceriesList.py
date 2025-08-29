Wel = "Welcome To V-Mart"
print(Wel.center(50))
for h in range(10):
    print(h*"=",end="")

basket = []

for i in range(500):
    print("\n1.Add In Basket")
    print("2.View In Basket")
    print("3.Remove From Basket")
    print("4.Exit")
    cho = (input("> Choose Option: "))
    match cho:
        case "1":
            add = input("> Add in Basket: ")
            basket.append(add)
            print(add,"Added Successfully.")

        case "2":
            count = 0
            if len(basket) == 0:
                print("> Empty Basket.\n")
            else:
                basket.sort()
                print("===============")
                for j in basket:
                    count += 1
                    print(count,j)
                print("===============")
                print("\n> Go Back And Add More That You Want.")
        
        case "3":
                if len(basket)==0:
                    print("- No Item Found.")
                else:
                    print(basket)
                    remo = input("\n> Remove from basket: ")
                    if remo in basket:
                        basket.remove(remo)
                        count -= 1
                        print("> Item Removed.")
                    else:
                        print("- No Item Found, Check Name Again.")
        case "4":
            print("\n- Thank you for using our service.")
            break

        case _:
            print("\n- Invalid Option.")
            print("- Try Again.\n")
