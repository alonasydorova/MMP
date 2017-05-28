//Snippet 2-0
#include "Puzzle.hpp"
#include <iostream>

using namespace std;

int main()
{
    cout << "______________________HANGMAN___________________________" << endl;
    //Snippet 2-1
    Puzzle *puzzle;
    puzzle = new Puzzle();
    puzzle->startGame();
    while (puzzle->getState() != NOT_RUNNING)
    {
        puzzle->gameLoop();
    }
    return 0;
}
