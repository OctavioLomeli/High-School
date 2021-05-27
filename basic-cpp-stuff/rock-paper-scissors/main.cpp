# include <iostream>
int p1_streak = 0, p2_streak = 0, p1_score = 0, p2_score = 0;
char p1_choice, p2_choice;
bool continue_playing = true;

// compares their choice, and increases the winner
void compare(char p1, char p2)
{
    if (p1 == p2)
    {
        std::cout << "\nIt was a tie.";
    }
    else if (p1 == 'r' && p2 == 's')
    {
        std::cout << "\nPlayer 1 chose rock, player 2 chose scissors. Player 1 wins.";
        p1_streak++;
    }
    else if (p1 == 'r' && p2 == 'p')
    {
        std::cout << "\nPlayer 1 chose rock, player 2 chose paper. Player 2 wins.";
        p2_streak++;
    }
    else if (p1 == 's' && p2 == 'p')
    {
        std::cout << "\nPlayer 1 chose scissors, player 2 chose paper. Player 1 wins.";
        p1_streak++;
    }
    else if (p1 == 's' && p2 == 'r')
    {
        std::cout << "\nPlayer 1 chose scissors, player 2 chose rock. Player 2 wins.";
        p2_streak++;
    }
    else if (p1 == 'p' && p2 == 's')
    {
        std::cout << "\nPlayer 1 chose paper, player 2 chose scissors. Player 2 wins.";
        p2_streak++;
    }
    else
    {
        std::cout << "\nPlayer 1 chose paper, player 2 chose rock. Player 1 wins.";
        p1_streak++;
    }
}

// asks players for their choice
void ask()
{
    std::cout << "\nPlayer 1, enter your choice of r, p, or s:  ";
    std::cin >> p1_choice;
    std::cout << "Player 2, enter your choice of r, p, or s:  ";
    std::cin >> p2_choice;
}

// prints the stats of each player
void print()
{
    std::cout << "\nPlayer 1's streak: " << p1_streak << "\tPlayer 1's wins: " << p1_score << std::endl;
    std::cout << "Player 2's streak: " << p2_streak << "\tPlayer 2's wins: " << p2_score << std::endl;
}

int main()
{
    std::cout << "Welcome to rock, paper, scissors.";
    while (continue_playing)
    {
        while (p1_streak != 3 && p2_streak != 3)
        {
            ask();
            compare(p1_choice, p2_choice);
            print();
        }

        std::cout << "Do you want to continue playing (1/0): ";
        std::cin >> continue_playing;
        if (continue_playing)
        {
            if (p2_streak == 3)
            {
                p2_score++;
            }
            else if (p1_streak == 3)
            {
                p1_score++;
            }
            p2_streak = 0;
            p1_streak = 0;
        }

    }
    std::cout << "Thanks for playing.";
    return 0;
}
