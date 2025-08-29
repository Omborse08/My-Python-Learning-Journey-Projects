import random
ran = random.randint(1,20)
round = 1
lst = []
no = 1
while round <= 3:
    import random
    ran = random.randint(1,20)
    score = 10
    print("\nRound",round)
    if round < 4:
      while True:
        guess = int(input("Guess the number(1-20): "))
        if ran == guess:
            round += 1
            lst.append(score)
            print("Correct.")
            print("> Your Score is",score)
            break
        elif ran < guess:
            print("Small")
            score -= 1
        elif ran > guess:
            print("Big")
            score -= 1
        else:
            print("Wrong! Try Again.")
    
    if round == 4:
        print("All Scores By 3 Round is",lst)
        print("\nTop 3 Scores")
        top = sorted(lst, reverse=True)
        for i in range(len(top)):
            print(i+1,top[i])
        
