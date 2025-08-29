movie_list = [
    ("Kuch Kuch Hota Hai","6:30 PM",50),
    ("Sitare Jameen Par","3:30 PM",40),
    ("Train To Busan","9:30 PM",30)]

while True:
    print("\n1.View Movies")
    print("2.Book Tickets")
    print("3.Exit")
    choose_option = int(input("Choose Option: "))
    match choose_option:
        case 1:
            i = 0
            for movie in movie_list:
                i += 1
                print(f"{i}. Movies: {movie[0]}     Time: {movie[1]}     Seats: {movie[2]}")
        
        case 2:
            ticket_book = int(input("Enter Movie Number: "))
            movie_name = ticket_book - 1
            movie1 = movie_list[movie_name] 
            print(f"Movie Booked {movie1[0]}") 
            print(f"Movie Time Is: {movie1[1]}")
            book_seats = int(input(f"Total Seats is {movie1[2]} How many u wants: "))
            booked = movie1[2] - book_seats
            print(f"Seat Book Total Seats: {booked}")

        case 3:
            print("Exit")
            break

        case _:
            print("Invalid Number")
