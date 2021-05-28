#include <iostream>
#include <string>
#include <fstream>

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
		if (mysteryWord[i] == theGuess)
		{
			solved[i] = mysteryWord[i];
			left--;
			once = true;
		}
	}
	if (!once)
	{
		lives--;
	}
}

// prints the characters remaining
void print()
{
	for (int i=0; i<10; i++)
	{
		std::cout << solved[i];
	}
}

int main()
{
	std::fstream my_file;
	my_file.open("words.txt", std::ios::in);
	
	my_file.close();
	while (true)
	{
		std::cout << "Enter a guess: ";
		std::cin >> temp_guess;
		guess(temp_guess);
		if (left == 0)
		{
			break;
		}
	}
	return 0;
}
