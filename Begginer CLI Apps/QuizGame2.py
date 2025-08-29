import random
def get_questions(levels):
    easy = [("What is 2 + 2?", "4"), ("What is 5 * 5?", "25")]
    normal = [("What is capital of India?", "delhi"), ("What starts with A and ends with e?", "apple")]
    hard = [("which in called as pink city?", "jaipur"), ("who is love you 3000?", "ironman")]

    match levels:
        case 1: return easy
        case 2: return normal
        case 3: return hard

while True:
    print("Welcome To The Quiz Master.")
    print("\n1.Easy\n2.Normal\n3.Hard")
    option = int(input("Choose Option(1-3): "))
    question = get_questions(option)
    if option >= 4:
        print("\nInvalid Option: ")
        
    point = 0
    for i,ans in question:
        print(f"\nQuestion: {i}")
        answer = input("Enter Your Answer: ")
        if answer == ans:
            print("Very Good")
            point += 1
        else:
            print("Wrong")
        your_score1 = (point/2) * 100 

    print(f"\nYour Score is: {your_score1}")
    if your_score1 >= 90:
        print("\nWell Done")
    elif your_score1 >= 70:
        print("\nGood")
    elif your_score1 >= 50:
        print("\nBetter")
    else:
        print("\nFailed")

    print("\n1.Play Again\n2.Exit")
    close = int(input("Enter Your Choice: "))
    match close:
        case 1:
            print("\nLet's start again")
            continue
        case 2:
            print("Exit")
            break    