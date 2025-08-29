def line():
    print("--------------------------------------")

print("""Welcome To HotelRoom.PY""")
Bookings = []
Rooms = 0
ACB = 0
NACB = 0
TotalR = 0
while True:
    print("\n1.Add Booking")
    print("2.View Booking")
    print("3.Search Booking")
    print("4.Cancel Booking")
    print("5.Show Summary")
    print("6.Exit")
    option_choose = int(input("> Choose Option: "))
    match option_choose:

        case 1:
            name = input("Enter Your Name: ")
            Rooms += 1
            phone = input("Enter Your Phone Number: ")
            date = input("Enter Your Check in Date: ")
            staying = int(input("Enter Your Staying Date: "))
            room = input("Enter Your Room Type(AC/Non-AC): ")
            if room == "AC":
                print("\n> Your Room Booked Successfully.")
                ACB += 1
                total1 = staying * 2000
                TotalR += total1
                print(f"> Your Booking Charges is: {total1}")
            else:
                print("\n> Your Room Booked Successfully.")
                NACB += 1
                total2 = staying * 1000
                TotalR += total2
                print(f"> Your Booking Charges is: {total2}")
            booked = (name,phone,date,staying,room)
            Bookings.append(booked)

        case 2:
            print("\n===ALL BOOKINGS===")
            line()
            num = 0
            for i in Bookings:
                num += 1
                print(f"{num}. Name: {i[0]}     \n   Phone: {i[1]}    \n   Date: {i[2]}    \n   Staying For: {i[3]}    \n   Room Type: {i[4]}")
            line()
            
        case 3:
            SearchBooking = input("Seach Booking By Name/Phone No: ")
            available = False
            for j in Bookings:
                SPhone = j[1]
                SName = j[0]
                if SearchBooking == SName:
                    available = True
                    print("\n Booking Found ")
                    line()
                    print(f"\n   > Name: {j[0]}     \n   > Phone: {j[1]}    \n   > Date: {j[2]}    \n   > Staying For: {j[3]}    \n   > Room Type: {j[4]}")
                    line()
                elif SearchBooking == SPhone:
                    available = True
                    print("\n Booking Found ")
                    line()
                    print(f"\n   > Name: {j[0]}     \n   > Phone: {j[1]}    \n   > Date: {j[2]}    \n   > Staying For: {j[3]}    \n   > Room Type: {j[4]}")
                    line()

            if not available:
                print("Not Found.")

        case 4:
            print("\n===CANCELLED===")
            cancel = input("Canceled Your Booking by Phone No: ")
            sure = int(input("Are You Sure (1.No / 2.Yes): "))
            match sure:
                case 1:
                    print("\n> Welcome Again")
                
                case 2:
                    line()
                    for k in Bookings:
                        if k[1] == cancel:
                            Bookings.remove(k)
                            print("Booking Cancelled Successfully")

                    else:
                        print("No Bookings Available")
                    line()
        case 5:
            print("\n===SUMMARY===")
            line()
            print(f"Total Bookings: {Rooms}")
            print(f"AC Rooms Books: {ACB}")
            print(f"Non-AC Rooms Books: {NACB}")
            print(f"Total Revenue: {TotalR}")             
            line()               

        case 6:
            print("Thank you for using our services")
            break

        case _:
            print("Invalid Option")
            break