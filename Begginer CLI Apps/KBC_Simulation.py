questions = [
    ["What is the capital of India?", "Mumbai", "Nashik", "Pune", "New Delhi", 4, "New Delhi"],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2, "Mars"],
    ["Who wrote the Indian national anthem?", "Bankim Chandra", "Rabindranath Tagore", "Sarojini Naidu", "Jawaharlal Nehru", 2, "Rabindranath Tagore"],
    ["Which animal is known as the King of the Jungle?", "Elephant", "Tiger", "Lion", "Leopard", 3, "Lion"],
    ["Who was the first Prime Minister of India?", "Indira Gandhi", "Jawaharlal Nehru", "Mahatma Gandhi", "Rajendra Prasad", 2, "Jawaharlal Nehru"],
    ["Which is the longest river in the world?", "Ganga", "Amazon", "Nile", "Yamuna", 3, "Nile"],
    ["Which organ purifies our blood?", "Heart", "Lungs", "Liver", "Kidney", 4, "Kidney"],
    ["What is H2O commonly known as?", "Salt", "Water", "Oxygen", "Hydrogen", 2, "Water"],
    ["Who invented the light bulb?", "Edison", "Newton", "Einstein", "Galileo", 1, "Edison"],
    ["Which is the smallest state in India?", "Goa", "Sikkim", "Tripura", "Manipur", 1, "Goa"],
    ["Who painted the Mona Lisa?", "Van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo", 2, "Leonardo da Vinci"],
    ["Which sport is known as the 'Gentleman's Game'?", "Football", "Tennis", "Cricket", "Boxing", 3, "Cricket"],
    ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2, "Carbon Dioxide"],
    ["What is the national bird of India?", "Crow", "Sparrow", "Peacock", "Pigeon", 3, "Peacock"],
    ["Which Indian city is known as the 'Pink City'?", "Udaipur", "Delhi", "Jaipur", "Agra", 3, "Jaipur"],
    ["Which continent is the largest by area?", "Asia", "Africa", "Europe", "Australia", 1, "Asia"],
    ["Who discovered gravity?", "Galileo", "Newton", "Einstein", "Faraday", 2, "Newton"],
    ["Which metal is liquid at room temperature?", "Iron", "Mercury", "Copper", "Aluminium", 2, "Mercury"],
    ["Which is the largest ocean in the world?", "Atlantic", "Indian", "Arctic", "Pacific", 4, "Pacific"],
    ["Which is the currency of Japan?", "Yen", "Won", "Rupee", "Dollar", 1, "Yen"],
]
levels = [
    "₹1,000",
    "₹2,000",
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
    "₹6,40,000",
    "₹12,50,000",
    "₹25,00,000",
    "₹50,00,000",
    "₹1 Crore",
    "₹3 Crore",
    "₹5 Crore",
    "₹7 Crore",
    "₹10 Crore",
    "₹12 Crore"
]
passed1 = ["50-50","Audience Pool","Flip Question"]
l1 = 0
l2 = 0
l3 = 0
Money = 0
print("Welcome To KBC")
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n> {i+1}. Question for {levels[i]}")
    print(f"> {question[0]}")
    print(f"1.{question[1]}               2.{question[2]}")
    print(f"3.{question[3]}               4.{question[4]}")
    print(f"\n> Use Life Line\n  1.{passed1[0]}         2.{passed1[1]}         3.{passed1[2]}")
    life_line = int(input("Enter Your Life Line (1 - 3) / 0 For Pass: "))
    match life_line:
        case 0:
            print("No Life Line Used: ")

        case 1:
            passed1[0] = "❌"
            if l1 == 1:
                print("Already Used! ")
            else:
                l1 += 1
                if question[1] == question[6]:
                    print(f"1.{question[1]}                              ")
                    print(f"                              4.{question[4]}")
                
                elif question[2] == question[6]:
                    print(f"                              2.{question[2]}")
                    print(f"                              4.{question[4]}")

                elif question[3] == question[6]:
                    print(f"                                             ")
                    print(f"3.{question[3]}               4.{question[4]}")

                else:
                    print(f"1.{question[1]}                              ")
                    print(f"                              4.{question[4]}") 
        
        case 2:
            if l2 == 1:
                print("Already Used! ")
            else:
                l2 += 1
                passed1[1] = "❌"
                print("\n> Audience Pool Is:")
                if question[1] == question[6]:
                    print(" A:45   B:20    C:10    D:25")
                
                elif question[2] == question[6]:
                    print(" A:25   B:75    C:5    D:5")


                elif question[3] == question[6]:
                    print(" A:30   B:13    C:30    D:27")
                    

                else:
                    print(" A:25   B:20    C:10    D:45")

        case 3:
            if l3 == 1:
                print("Already Used! ")
            else:
                l3 += 1
                passed1[2] = "❌"
                print("\n> You Skipped A Question! ")
                continue

    box = int(input("- Enter Your Answer (1 - 4): "))
    if box == question[5]:
        print("> Right Answer ✅")
        if i == 5:
            Money = 10000
        elif i == 10:
            Money = 320000
    elif box == 0:
        print(f"You Quit you Win {levels[i]} Your Answer is {question[6]}")
        break
    
    else:
        print(f"Wrong Answer You Win Only {Money} And Your Answer is {question[6]}")
        break
