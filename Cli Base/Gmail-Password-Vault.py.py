name = (input("\nEnter your G-mail name: "))
passw = (input("Enter your password: "))
input("Password Is Saved. (Continue Press Enter )")

for i in range(10):
    print("\n1.Enter Your New Password:")
    print("2.Show Your Info:")
    print("3.Exit")
    a = int(input("Choose Option: "))
    match a:
        case 1:
            name = (input("Enter your New G-mail name: "))
            passw = (input("Enter your New password: "))
            saved = (input("New Password Is Saved. (Continue Press Enter )"))
            print("")
        
        case 2:
            your1 = "Your G-mail Is",name
            print(your1)
            your2 = "Your Password Is",passw
            print(your2)
            exit1 = (input("Press Enter To Exit. "))
            print("")

        case 3:
            break





