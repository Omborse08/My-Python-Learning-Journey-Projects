Bank = "Welcome to Bank"
b = (Bank.upper())
b1 = b.center(50)
print(b1)

balance = 4500

for i in range(10):
    print("\nChoose Options")
    print("1.Deposit:")
    print("2.Withdraw:")
    print("3.BalanceCheck:")
    print("4.Exit:")

    a = int(input("Choose Option: "))

    match a:
        case 1:
            money = int(input("Enter the deposit Amount: "))
            print("Amount Deposit Successfully")
            balance += money
            print("New Balance",balance)

        case 2:
            money = int(input("Enter the withdraw amount: "))
            if money <= balance:
              balance -= money
              print("Amount Withdrawal Successfully")
            else:
                print("Insufficient balance")

        case 3:
            print("Your Balance Is: ",balance)
        
        case 4:
            print("Thank you for using our services.")
            break

        case _:
            print("Error.")
    