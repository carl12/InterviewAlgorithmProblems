'''
You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities. The value of each coin is already given. Can you determine the number of ways of making change for a particular number of units using the given types of coins?

For example, if you have types of coins, and the value of each type is given as respectively, you can make change for units in three ways: , , and .

Complete the function getWays that takes the number of coin types and the value of each coin type as input, and return the number of ways to make change for units using any number of coins.

Input Format

The first line contains two space-separated integers describing the respective values of and , where:
is the number of units
is the number of coin types
The second line contains space-separated integers describing the respective values of each coin type : (the list of distinct coins available in infinite ms).

https://www.hackerrank.com/challenges/coin-change/problem
'''
import f_timer
import random

def getWays(n, c):
    solutions = [set() for _ in range(n+1)]
    solutions[0].add(tuple())
    for i in range(n+1):

        for coin in c:
            if coin == i:
                solutions[i].add(tuple([coin]))
        for j in range(1,i//2+1):
            for k in solutions[i-j]:
                for h in solutions[j]:
                    solutions[i].add(tuple(sorted(k+h)))
            # solutions[i].add(solutions[i-j]solutions[j])
    return len(solutions[n])

def getWays2(n,cs):
    solutions = [[0 for _ in cs] for _ in range(n+1)]

    for i in range(len(solutions[0])):
        solutions[0][i] = 1

    for i in range(1,len(solutions)):
        for j in range(len(cs)):

            up = solutions[i][j-1] if j > 0 else 0
            left = solutions[i-cs[j]][j] if i - cs[j] >= 0 else  0

            solutions[i][j] = up+left

    return solutions[n][len(cs)-1]

def makeCoinProblem(maxGoal, maxNumCoins, maxCoin):
    goal = random.randint(0, maxGoal)

    num_coins = random.randint(2, maxNumCoins)
    # Generate random number of coins which does not exceed number
    # of available spots

    realNumCoins = random.randint(1,min(maxCoin-1, num_coins))

    coins = random.sample(range(1, maxCoin), realNumCoins)

    return [goal, coins]

makeCoinProblem(10,2,4)
problemInput = [30, 10, 6]
print(f_timer.time_funcs([getWays, getWays2], makeCoinProblem, problemInput, 500))
print('done')



# print(ways_for_change(4, [1,2,3]))
# ways_for_change(10, [2,5,3,6])
# ways_for_change(4, [1,2,3])


