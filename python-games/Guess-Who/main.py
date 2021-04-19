import random

# Name, hasBlackHair, hasBlondeHair, hasGingerHair, wearsGlasses, isMale
characters = [
    ["JOHN", "Yes", "No", "No", "Yes", "Yes"],
    ["MAX", "Yes", "No", "No", "No", "Yes"],
    ["MOLLY", "Yes", "No", "No", "Yes", "No"],
    ["DIEGO", "No", "Yes", "No", "No", "Yes"],
    ["LYNNE", "No", "Yes", "No", "Yes", "No"],
    ["ESTRELLA", "No", "Yes", "No", "No", "No"],
    ["CLAIRE", "No", "No", "Yes", "No", "No"],
    ["KIERAN", "No", "No", "Yes", "No", "Yes"],
    ["MICHAEL", "No", "No", "Yes", "Yes", "Yes"]
]
mode = ""
character_chosen = ""
guess_amount = 1
question_amount = 3
winner_not_present = True

# prints the instructions
def print_instruct():
    print("_______Instructions_for_PVP_mode_______")
    print("   P1 looks at characters and picks one")
    print(" P2 will ask questions and try to guess")
    print("_______Instructions_for_Solo_mode_______")
    print("      Look at character descriptions    ")
    print("    Character will be randomly selected ")
    print("     Player asks questions and guesses  ")
    print("________________________________________")


# asks user what mode to play
def pick_mode():
    global mode
    mode = input("PVP or Solo: ").upper()
    if mode == "PVP":
        play_pvp()
    elif mode == "SOLO":
        play_solo()
    else:
        print("That's not an option, try again.")
        pick_mode()


# prints character descriptions
def print_char_des():
    print("0. John is a male with black hair and glasses")
    print("1. Max is a male with black hair but no glasses")
    print("2. Molly is a female with black hair and glasses")
    print("3. Diego is a male with blonde hair but no glasses")
    print("4. Lynne is a female with blonde hair and glasses")
    print("5. Estrella is a female with blonde hair but no glasses")
    print("6. Claire is a female with ginger hair but no glasses")
    print("7. Kieran is a male with ginger hair but no glasses")
    print("8. Michael is a male with ginger hair and glasses")


# allows user to pick a character for other player
def pick_char():
    global character_chosen
    character_number = int(input('Pick a character by typing the number before their name or type 10 to see the '
                                 'character descriptions:'))
    if character_number == 10:
        print_char_des()
        character_number = int(input("Pick a character by typing the number before their name: "))

    character_chosen = characters[character_number]


def start_menu():
    print("Welcome to Guess Who")
    do_i_print_instruct = input("Do you want to see the instructions: ").upper()
    if do_i_print_instruct == "YES":
        print_instruct()
        print()
    pick_char()
    y_n_change_question = input("You have 3 questions by default, do you want to change this amount: ").upper()
    if y_n_change_question == "YES":
        change_question_amt()
    y_n_change_guess = input("You have 1 guess by default, do you want to change this amount: ").upper()
    if y_n_change_guess == "YES":
        change_guess_amt()
    pick_mode()


# allows user to change guess amount
def change_guess_amt():
    global guess_amount
    guess_amount = int(input("Enter the amount of guesses you want to be able to make ( 1 < amount < 5): "))
    if guess_amount > 4 or guess_amount < 1:
        guess_amount = 1


# allows user to change question amount
def change_question_amt():
    global question_amount
    question_amount = int(input("Enter the amount of questions you want to be able to ask ( -1 < amount < 6): "))
    if question_amount < 0 or question_amount > 6:
        question_amount = 3


# prints questions user can ask
def show_questions():
    print("_____________________________")
    print("1. Do they have black hair?")
    print("2. Do they have blonde hair?")
    print("3. Do they have ginger hair?")
    print("4. Do they wear glasses?")
    print("5. Are they male?")
    print("_____________________________")


# calls the solo mode
def play_solo():
    global character_chosen
    character_chosen = characters[random.randint(0, 8)]
    while guess_amount != 0 and winner_not_present:
        make_guess_or_question()


# calls the pvp mode
def play_pvp():
    while guess_amount != 0 and winner_not_present:
        make_guess_or_question()


# allows user to ask a question
def ask_a_question():
    global question_amount
    if question_amount != 0:
        y_n_show_q = input("Do you want to see the questions you can ask: ").upper()
        if y_n_show_q == "YES":
            show_questions()
        question_num = int(input("Enter the number before the question that you want to ask: "))
        print("Response: " + character_chosen[question_num])
        question_amount = question_amount - 1
    else:
        print("You cannot ask anymore questions.")


# allows user to make a guess
def make_a_guess():
    global guess_amount
    global winner_not_present
    character_guess = input("Enter your guess: ").upper()
    if character_guess == character_chosen[0]:
        print("You win!")
        guess_amount = 0
        winner_not_present = False

    else:
        print("Wrong")
    guess_amount = guess_amount - 1


# asks user to make a guess or question
def make_guess_or_question():
    y_n_show_character_list = input("Do you want to see the character description: ").upper()
    if y_n_show_character_list == "YES":
        print_char_des()
    y_n_ask_question = input("Do you want to ask a question: ").upper()
    if y_n_ask_question == "YES":
        ask_a_question()
    y_n_make_guess = input("Do you want to make a guess: ").upper()
    if y_n_make_guess == "YES":
        make_a_guess()


start_menu()

print("Thanks for playing!")
