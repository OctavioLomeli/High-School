import time
import random

# end = time.time()
# print(end - start)

print("Welcome to the Speed Typing Test.")
print("You will have to type out each word that is displayed.\nYou will have one minute to type as much words correctly as you can.")
print("The case that you input does not matter.")
input("Press enter to begin. ")
print()
start = time.time()
score = 0

while time.time() - start < 60:
    with open('/Users/missionbit/Desktop/Python_Course/speedtest.py/words.txt', "r") as myFile:
        lines = myFile.readlines()
        word = lines[random.randint(0, 385)][:-1] 
    print(word)
    user_guess = input("Enter: ").lower()
    print()
    if user_guess == word:
        score += 1
print("Time is up.\n")
print("You spelled {} words correctly".format(score))
print("Your wpm is {}".format(score/60))
