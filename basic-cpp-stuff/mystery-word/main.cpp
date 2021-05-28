#include <iostream>
#include <string>
#include <fstream>
#include <time.h>
#include <stdlib.h>

std::string mysteryWord;
char solved[10] = { '_', '_', '_', '_', '_', '_', '_', '_', '_', '_' };
int lives = 6;
int left = 10;
char temp_guess;

// checks if the guess is in the word
void guess(char theGuess)
{
	bool once = false;
	for (int i = 0; i < 10; i++)
	{
		if (mysteryWord[i] == char(theGuess))
		{
			solved[i] = mysteryWord[i];
			left--;
			once = true;
		}
	}
	if (!once)
	{
		lives--;
		std::cout << "\nYour guess was not in the word.\n";
	}
	else
	{
		std::cout << "\nYour guess was correct.\n";
	}
}

// prints the characters remaining
void print()
{
	for (int i=0; i<10; i++)
	{
		std::cout << solved[i];
	}
	std::cout << "\nLives remaining: " << lives << std::endl;
}

int main()
{
	srand(time(NULL));
	std::ifstream words_file("words.txt");
	for(int line = 0; line < (rand()%387); line++)
	{
		std::getline(words_file, mysteryWord);
	}
	words_file.close();

	while (true)
	{
		print();
		std::cout << "\nEnter a letter to guess: ";
		std::cin >> temp_guess;
		guess(tolower(temp_guess));
		if (left == 0)
		{
			std::cout << "Congratulations! You discovered the word.\n";
			break;
		}
		else if (lives == 0)
		{
			std::cout << "Your lives ran out and you lost.\n";
			break;
		}
	}
	std::cout << "The word was: " << mysteryWord << std::endl;
	std::cout << "Thanks for playing.";
	return 0;
}
