import random

user_streak = 0
bot_streak = 0
user_wins = 0
bot_wins = 0
user_choice = ""
bot_choice = ""
continue_playing = True

options_for_bot = ["SCISSORS", "ROCK", "PAPER"]


# prompts user to pick a choice and gives the bot a random choice
def pick_rps():
    global user_choice
    global bot_choice
    global user_streak
    global bot_streak
    print()
    print("User current streak: " + str(user_streak) + "       Bot current streak: " + str(bot_streak))
    user_choice = input("Enter one of the following, rock, paper, or scissors: ").upper()
    if user_choice != "ROCK" and user_choice != "SCISSORS" and user_choice != "PAPER":
        print("Not a valid choice.")
        pick_rps()
    bot_choice = options_for_bot[random.randint(0, 2)]


# takes in the user's and bot's choice and gives a streak to whoever beats who
def compare_choices(user_option, bot_option):
    global user_streak
    global bot_streak
    if user_option == "ROCK" and bot_option == "PAPER":
        print("User chose rock, bot chose paper. Bot gets a point.")
        bot_streak += 1
        declare_winner()
    elif user_option == "ROCK" and bot_option == "SCISSORS":
        print("User chose rock, bot chose scissors. User gets a point.")
        user_streak += 1
        declare_winner()
    elif user_option == bot_option:
        print("It was a tie.")
    elif user_option == "PAPER" and bot_option == "ROCK":
        print("User chose paper, bot chose rock. User gets a point.")
        user_streak += 1
        declare_winner()
    elif user_option == "PAPER" and bot_option == "SCISSORS":
        print("User chose paper, bot chose scissors. Bot gets a point")
        bot_streak += 1
        declare_winner()
    elif user_option == "SCISSORS" and bot_option == "PAPER":
        print("User chose scissors, bot chose paper. User gets a point.")
        user_streak += 1
        declare_winner()
    elif user_option == "SCISSORS" and bot_option == "ROCK":
        print("User chose scissors, bot chose rock. Bot gets a point.")
        bot_streak += 1
        declare_winner()
    else:
        print("you missed something")


# checks when streak becomes 3 and declares winner if so
def declare_winner():
    global user_wins
    global bot_wins
    global user_streak
    global bot_streak

    print()
    if user_streak == 3:
        print("User wins.")
        user_wins += 1
        print("User wins: " + str(user_wins) + "     Bot wins: " + str(bot_wins))
        reset_game()
    elif bot_streak == 3:
        print("Bot wins.")
        bot_wins += 1
        print("User wins: " + str(user_wins) + "     Bot wins: " + str(bot_wins))
        reset_game()


# resets game, helper for declare winner
def reset_game():
    global user_streak
    global bot_streak
    global continue_playing
    y_n_reset = input("Do you want to play again: ").upper()
    if y_n_reset == "YES":
        user_streak = 0
        bot_streak = 0
    else:
        continue_playing = False
        print("Thanks for playing.")

# starting function that starts everything
def start():
    global bot_choice
    global user_choice
    pick_rps()
    compare_choices(user_choice, bot_choice)


print("Welcome to rock, paper, scissors.")
while continue_playing:
    start()
