movies_list = ["🦁👑","🚢💔🌊","🕷️🧑","🦸‍♂️🛡️","🧞‍♂️🕌","👽📞🏠","🦕🌴🌋","🧙‍♂️🪄⚡","🐼🥋","👨‍🚀🌌","💣👓🇩🇪","🦇🏙️","👩‍🚀🚀🪐","🔫🕶️","🏎️🔥",]
movies_name_list = ["lion king","titanic","spiderman","captain america","aladdin","e.t.","jurassic park","harry potter","kung fu panda","interstellar","oppenheimer","batman","gravity","men in black","fast and furious"]

score = 0
while True:
    print("\n1.Play")
    print("2.Exit")
    print(f"Your score is {score} ")
    option = int(input("Choose Option: "))
    match option:

        case 1:
            print("You have a 10 Chance Only.")
            for i in range(10):
                import random
                ran = random.randint(0,14)
                print(f"your score {score}")
                print(f"Guess the movie name by emoji:{movies_list[ran]} ")
                answer = input("What's the movie name: ")
                if movies_name_list[ran] == answer:
                    print("correct.")
                    score += 1
                else:
                    print("Wrong u out.")
                    print(f"correct answer is {movies_name_list[ran]}")

        case 2:
            print("Existing.")
            break
        
        case _:
            print("Invalid Option.")