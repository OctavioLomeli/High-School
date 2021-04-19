import random

list_of_words = ("JANITOR", "JACKETS", "ABDOMEN", "ABRIDGE", "BADGERS", "BEASTLY", "PROBLEMS", "PYTHON", "FRIENDS",
                 "DONATE", "TANGLED", "PHANTOM", "MONSTER", "NETWORK", "PLASTIC", "PICKLES", "TEACUPS")
random_word = "blank"
underscore_list = ["_"]
letters_guessed_before = []
num_lives = 6
continue_playing = True

# adding underscores to array the same length of the random word
for i in range(len(random_word) + 1):
    underscore_list.append("_")


# asks user for a letter and calls check_if_word function
def ask_for_letter():
    global letters_guessed_before
    global underscore_list
    global num_lives
    count = 0
    print(*underscore_list)
    print("Lives: " + str(num_lives))
    letter_guess = input("Enter a letter to guess: ").upper()
    if len(letter_guess) > 1:
        print("Only enter one letter.")
        ask_for_letter()
    for j in range(len(letters_guessed_before)):
        if letters_guessed_before[j] == letter_guess:
            count += 1
    if count > 0:
        print("You guessed this letter before. Try again.")
        ask_for_letter()
    elif count == 0:
        letters_guessed_before.append(letter_guess)
    check_if_word(letter_guess)


# checks if letter is in the random word ( used after ask_for_letter() )
def check_if_word(user_guess):
    global num_lives
    global continue_playing
    global random_word
    count = 0
    index = 0
    for o in range(len(random_word)):
        if random_word[o] == user_guess:
            count += 1
            index = o
    if count > 0:
        underscore_list[index] = user_guess
    elif count == 0:
        print("Letter was not present.")
        num_lives -= 1
        if num_lives < 1:
            print("You lost.")
            print("Word was: " + random_word)
            continue_playing = False
    count = 0
    for p in range(len(underscore_list)):
        if underscore_list[p] == "_":
            count += 1
    if count == 0:
        print("Congratulations you won!")
        continue_playing = False
    print()


# asks user if that want to see instructions
def show_instructions():
    y_n_show = input("Do you want to know the instructions on how to play: ").upper()
    if y_n_show == "YES":
        print("You have to guess letters that belong to a random word before you lose all your lives.")

# asks user if they want to change amount of lives
def change_lives():
    global num_lives
    y_n_show = input("By default you have 6 lives; do you want to change this amount: ").upper()
    if y_n_show == "YES":
        try:
            amount = int(input("Enter the amount of lives you want. ( 1 - 10 )"))
            if 0 < amount < 11:
                num_lives = amount
            else:
                print("Not in the range.")
                change_lives()
        except ValueError:
            print("Enter a number next time. Resetting.")
            change_lives()

# asks user if they want to play solo or pvp mode
def ask_mode():
    global random_word
    mode = input("Pvp or solo: ").upper()
    if mode == "PVP":
        random_word = input("Enter a word for your friend to guess: ").upper()
    elif mode == "SOLO":
        random_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
    else:
        print("Not a valid mode.")
        ask_mode()


print("Welcome to Mystery Word")
show_instructions()
ask_mode()
change_lives()
while continue_playing:
    ask_for_letter()
