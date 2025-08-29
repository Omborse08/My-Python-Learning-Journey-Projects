import os
class game:

    def __init__(self,hero):
        self.hero_health = {
    "Name":hero,
    "Level":1,
    "HP":100,
    "Gold":50,
    "XP":0
    }
        
    def healths(self):
        info = self.hero_health
        print(f"Name: {info['Name']} | Level: {info['Level']} | HP: {info['HP']} | Gold: {info['Gold']} | XP: {info['XP']}")
        with open("DungeonGame.txt",'w') as file:
            file.write(f"Name: {info['Name']} | Level: {info['Level']} | HP: {info['HP']} | Gold: {info['Gold']} | XP: {info['XP']}\n")
    
    def attack(self,what):
        if what == 1:
            print("> You Choose Attack")
            self.hero_health1 = {"Level":2,"HP":60,"XP":2}
            self.hero_health.update(self.hero_health1)

        elif what == 2:
            print("> You Choose To Run")
            self.hero_health2 = {"Level":2,"HP":100,"XP":5}
            self.hero_health.update(self.hero_health2)

        else:
            print("Choose Proper Option: ")
    
    def show_info(self):
        if self.hero_health['HP'] < 80:
            print("> You Lose That Match")
        else:
            print("You Win It You Made A Good Dicision! ")
    
    
class game2(game):
    @staticmethod
    def menu():
        print("""
1. Forest
2. Save & Quit
""")
        
    @staticmethod
    def attack_menu():
        print("\n1.Attack"
        "\n2.Run")

if not os.path.exists("DungeonGame.txt"):
    open("DungeonGame.txt",'w').close()

hero = input("Enter Your Name Here: ")
dg1 = game2(hero)
dg = game(hero)

print("\n[Hero Created!]")
dg.healths()

while True:
    dg1.menu()
    choose = int(input("Choose Option: "))
    match choose:
        
        case 1:
            print("🌲 You enter the dark forest...")
            print("⚔️ A Wild Goblin appears! HP: 30 | Attack: 5")
            print("\n> Choose Your Defense")
            dg1.attack_menu()
            choose_defense = int(input("\n> "))
            dg.attack(choose_defense)
            dg.healths()
            dg.show_info()
            break

        case 2:
            print("Thanks for Playing the Game")
            break



