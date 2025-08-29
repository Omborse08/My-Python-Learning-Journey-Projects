# Danger Do Not Run This Program

import random
import shutil

ran = random.randint(1,2)

print("> Safe <" if ran == (guess := int(input("Enter Your Guess: "))) else "Prank Brother")