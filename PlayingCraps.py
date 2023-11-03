"""
Name: Erika Avila Gutierrez
Date:11/5/23
Assignment:Assignment 10
Due Date:11/5/23
About this project: Create a python script that will roll two dice and determines if a player wins or loses
Assumptions: assimes wins are 7 or 11
All work below was performed by Erika Avila Gutierrez

"""
import random
from concurrent.futures import ThreadPoolExecutor
import time
import operator as op


# Function to roll 2 dice and add them to give a number between 1 and 12 based on random generation
def roll(NumRolls):
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    dice = Dice1 + Dice2
    return dice


# Function to have winner or loser determined
def player_results(played_num):
    if played_num == 7:
        return 1
    elif played_num == 11:
        return 1
    else:
        return 0


def main():
    tosses = 100000
    values = []
    for i in range(tosses):
        values.append(random.randint(1000, 10000))

    start = time.time()

    # Gets the new list of the game result which can be used concurrently with the player result
    with ThreadPoolExecutor(max_workers=3) as executor:
        gameResults = list(executor.map(roll, values))

        # Matches the game result with its corresponding player result
        playerResults = [player_results(result) for result in gameResults]

        # prints both the game result with the player result
        for game_result, player_result in zip(gameResults, playerResults):
            print(f'Game Result: {game_result} | Player Result: {player_result}')

    # counting the number of wins
    numberofwins = op.countOf(playerResults, 1)

    # estimated win ratio
    winRatio = numberofwins / tosses

    print("\nWin Ratio: ", winRatio)

    elapsed = time.time() - start
    print('\nComputing winner took %f sec.' % elapsed)


# Call the main method if run from the command line
if __name__ == '__main__':
    main()
