# include <iostream>

char board[3][3] = {{'-', '-', '-'},
					{'-', '-', '-'},
					{'-', '-', '-'} };

int temp_row, temp_col;

// checks if a win was achieved by a diagonal
bool checkDiagonal()
{
	if (board[2][0] == board[1][1] && board[1][1] == board[0][2] && board[0][2] != '-')
	{
		return true;
	}
	if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] != '-')
	{
		return true;
	}

	return false;
}

// checks if a win was achieved by a row
bool checkRow()
{
	for (int i = 0; i < 3; i++)
	{
		if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][2] != '-')
		{
			return true;
		}
	}
	return false;
}

// checks if a win was achieved by column
bool checkColumn()
{
	for (int i = 0; i < 3; i++)
	{
		if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[2][i] != '-')
		{
			return true;
		}
	}
	return false;
}

// returns whether or not someone won
bool checkWin()
{
	return checkColumn() || checkRow() || checkDiagonal();
}

//prints the board
void printBoard()
{
	for (int i = 0; i < 3; i++)
	{
		std::cout << board[i][0] << " " << board[i][1] << " " << board[i][2] << std::endl;
	}
}

// marks a spot in the board if available
int markSpot(int row, int column, char player)
{
	if (board[row][column] == '-')
	{
		board[row][column] = player;
		return 0;
	}
	else
	{
		return -1;
	}
}

void ask(char p)
{
	while (true)
	{
		std::cout << "Enter a row to mark a spot in: ";
		std::cin >> temp_row;
		std::cout << "Enter a column to mark a spot in: ";
		std::cin >> temp_col;
		if (markSpot(temp_row, temp_col, p) != -1)
		{
			break;
		}
		else
		{
			std::cout << "Invalid spot, try again.\n";
		}
	}
}

int main()
{
	std::cout << "Welcome to Tic-Tac-Toe.\n";
	while (true)
	{
		printBoard();
		ask('x');
		if (checkWin())
		{
			std::cout << "\nPlayer 1 wins.";
			break;
		}
		printBoard();
		ask('o');
		if (checkWin())
		{
			std::cout << "\nPlayer 2 wins.";
			break;
		}

	}
	std::cout << "\nThanks for playing.";
	return 0;
}
