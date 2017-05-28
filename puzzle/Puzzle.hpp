#ifndef PUZZLE_H
#define PUZZLE_H

#include <vector>
#include <iostream>

//SNIPPET 1-0
enum GameState {NOT_RUNNING, RUNNING};
class Puzzle
{
    public:
    Puzzle();
    ~Puzzle();
    //SNIPPET 1-2
    GameState getState();
    //SNIPPET 1-3
    void startGame();
    void gameLoop();
    private:
    //SNIPPET 1-1
    GameState state;
    //SNIPPET 3-0
    std::string word;
    std::vector<bool> guessed;
    int tries;
    void drawing(int position);
};

#endif // PUZZLE_H
