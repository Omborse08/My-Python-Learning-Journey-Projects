import time
questions = [["2 + 2","4"],["5 * 5","25"]]

for i in questions:
    print(f"Question {i[0]}")
    start = time.time()
    ans = input("Your Ans: ")
    end = time.time()
    taken = end - start
    if taken < 5:
        print("You Did It")
        if ans == i[1]:
            print("And Ans is Right ")
        else:
            print("It's Wrong But")
    else:
        print("You Lose My Brother, time is over")
