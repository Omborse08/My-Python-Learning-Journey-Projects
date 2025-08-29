def line():
    print("---------------------------------------")

transation = []
print("Welcome To Python Bank")
Balance = 5000
pin_point = 0
for i in range(3):
    enter_pin = int(input("Enter Your 4 Digit Pin: "))
    
    if enter_pin == 2006:
        print("Pin Granted.")

        while True:
            print("\n1.Check Balance")
            print("2.Deposite Money")
            print("3.Withdraw Money")
            print("4.View Transaction History")
            print("5.Exit")
            choose_option = int(input("Choose Option: "))
            match choose_option:

                case 1:
                    print(f"\nYour Balance Is: ${Balance}")

                case 2:
                    deposite_amount = int(input("\nEnter Deposite Amount: "))
                    Balance += deposite_amount
                    print("> Amount Deposite Succesfully")
                    print(f"> Your New Balance Is: {Balance}")
                    depo_history = (deposite_amount,"Amount Deposited")
                    transation.append(depo_history)

                case 3:
                    withdraw_amount = int(input("\nEnter Withdraw Amount: "))
                    if withdraw_amount <= Balance:
                        Balance -= withdraw_amount
                        print("> Amount Withdrawed Succesfully")
                        print(f"> Your New Balance Is: {Balance}")
                        with_history = (withdraw_amount,"Amount Withdrawed")
                        transation.append(with_history)
                    else:
                        print("Insufficient Balance")

                case 4:
                    if len(transation) == 0:
                        print("\n> No History Available")
                    else:
                        print("\n> Transation History: ")
                        line()
                        j = 0
                        for i in transation:
                            j += 1
                            print(f"{j}.{i}")
                        line()

                case 5:
                    print("\n> Exiting From The Bank.")
                    break

    elif enter_pin != 2006 and pin_point < 2:
        print("Invalid Pin")
        pin_point += 1
    else:
        print("Invalid Pin Last Attempts, Over!")