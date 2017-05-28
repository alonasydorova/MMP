#include "Puzzle.hpp"
#include <iostream>
#include <algorithm>


using namespace std;

Puzzle::Puzzle()
{
    //SNIPPET 2-2
    state = NOT_RUNNING;
}

Puzzle::~Puzzle()
{
}

//SNIPPET 2-3
GameState Puzzle::getState()
{
    return state;
}
//SNIPPET 3-1
void Puzzle::startGame()
{
    cout << "Input Word: ";
    getline(cin, word);
    state = RUNNING;
    tries = 7;
    for (int i = 0; i < word.size(); i++)
    {
        guessed.push_back(false);
    }
}
//SNIPPET 4-0
void Puzzle::gameLoop()
{
    cout << "Guess a letter: ";
    char input;
    cin >> input;

    int index = 0;
    bool found = false;
    while (index != -1)
    {
        index = word.find(input, index);
        if (index != -1)
        {
            found = true;
            guessed[index] = true;
            index++;
        }
    }

    if (!found)
    {
        if (--tries == 0)
        {
            state = NOT_RUNNING;
        }
        drawing(tries);
    }
    else
    {
        cout << "NICE!" << endl;
    }

    for (int i = 0; i < guessed.size(); i++)
    {
        if (guessed[i])
            cout << word.at(i);
        else
            cout << "_";
    }
    cout << endl;

    if (all_of(guessed.begin(), guessed.end(),

               [](bool i) { return i; }))
    {
        state = NOT_RUNNING;
    }
}
//SNIPPET 5-0
void Puzzle::drawing(int t)
{
    switch (t)
    {
    case 6:
        cout << endl
             << endl
             << "   +----+  " << endl
             << "   |    |  " << endl
             << "   |       " << endl
             << "   |       " << endl
             << "   |       " << endl
             << "   | " << t << " left" << endl
             << "  =============" << endl
             << endl;
        break;
    case 5:
        cout << endl
             << endl
             << "   +----+  " << endl
             << "   |    |  " << endl
             << "   |    O  " << endl
             << "   |       " << endl
             << "   |       " << endl
             << "   | " << t << " left" << endl
             << "  =============" << endl
             << endl;
        break;
    case 4:
        cout << endl
             << endl
             << "   +----+  " << endl
             << "   |    |  " << endl
             << "   |    O  " << endl
             << "   |    |  " << endl
             << "   |       " << endl
             << "   | " << t << " left" << endl
             << "  =============" << endl
             << endl;
        break;
    case 3:
        cout << endl
             << endl
             << "   +----+  " << endl
             << "   |    |  " << endl
             << "   |    O  " << endl
             << "   |   /|  " << endl
             << "   |       " << endl
             << "   | " << t << " left" << endl
             << "  =============" << endl
             << endl;
        break;
    case 2:
        cout << endl
             << endl
             << "   +----+  " << endl
             << "   |    |  " << endl
             << "   |    O  " << endl
             << "   |   /|\\ " << endl
             << "   |       " << endl
             << "   | " << t << " left" << endl
             << "  =============" << endl
             << endl;
        break;
    case 1:
        cout << endl
             << endl
             << "   +----+  " << endl
             << "   |    |  " << endl
             << "   |    O  " << endl
             << "   |   /|\\ " << endl
             << "   |   /   " << endl
             << "   | " << t << " left" << endl
             << "  =============" << endl
             << endl;
        break;
    case 0:
        cout << endl
             << endl
             << "   +----+  " << endl
             << "   |    |  " << endl
             << "   |    O  " << endl
             << "   |   /|\\ " << endl
             << "   |   / \\ " << endl
             << "   | GAME OVER" << endl
             << "  =============" << endl
             << endl;
        break;
    }
}