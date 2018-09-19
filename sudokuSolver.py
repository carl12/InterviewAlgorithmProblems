'''
Write the function sudokuSolve that checks whether a given sudoku board (i.e. 
sudoku puzzle) is solvable. If so, the function will returns true. Otherwise 
(i.e. there is no valid solution to the given sudoku board), returns false.

In sudoku, the objective is to fill a 9x9 board with digits so that each 
column, each row, and each of the nine 3x3 sub-boards that compose the board 
contains all of the digits from 1 to 9. The board setter provides a partially 
completed board, which for a well-posed board has a unique solution. As 
explained above, for this problem, it suffices to calculate whether a given 
sudoku board has a solution. No need to return the actual numbers that make up 
a solution.

A sudoku board is represented as a two-dimensional 9x9 array of the characters 
‘1’,‘2’,…,‘9’ and the '.' character, which represents a blank space. The 
function should fill the blank spaces with characters such that the following 
rules apply:
    In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
    In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
    In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.

A solved sudoku is a board with no blank spaces, i.e. all blank spaces are 
filled with characters that abide to the constraints above. If the function 
succeeds in solving the sudoku board, it’ll return true (false, otherwise).

'''
import copy
import random
import f_timer
import json
import time

def sudoku_solve(board, depth = 0):

 

  # Find open square with lowest number of possible moves
  minX, minY, validNums = find_min_possible_loc(board)

  # No open space - problem is finished
  # (assuming previous moves were valid)
  if minX == -1:
    return True
  
  # Open space with no possible move
  if len(validNums) == 0:
    return False

  # Recursively call with all posibilities for location
  for n in validNums:

    board[minY][minX] = n
    if sudoku_solve(board, depth + 1):
      return True


  # Reset board value for other recursive calls in stack
  board[minY][minX] = '.'
  return False
  
def find_min_possible_loc(board):
  bestPossible = [0 for _ in range(10)]
  minX = -1
  minY = -1
  found = False
  valid_moves = set()
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == '.':
        valid_moves = find_valid(board, i, j)
        num = len(valid_moves)
        if num <= 1:
          return (j, i, valid_moves)
        if len(bestPossible) > num:
          bestPossible = valid_moves
          minX = j
          minY = i
  return (minX, minY, bestPossible)

def find_valid(board, yLoc, xLoc):
  # determine which numbers are invalid
  validNums = set(['1','2','3','4','5','6','7','8','9'])
  for i in range(0,9):
    if board[i][xLoc] != '.' and board[i][xLoc] in validNums:
      validNums.remove(board[i][xLoc])
    if board[yLoc][i] != '.' and board[yLoc][i] in validNums:
      validNums.remove(board[yLoc][i])
  
  startX = xLoc - xLoc % 3
  startY = yLoc - yLoc % 3
  
  for i in range(startY, startY+3):
    for j in range(startX, startX+3):

      if board[i][j] != '.' and board[i][j] in validNums:
        validNums.remove(board[i][j])
  return validNums

def sudoku_solve2(board, calls = 0):
  calls += 1
  # pick open square
  xLoc = -1
  yLoc = -1
  found = False
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == '.':
        yLoc = i
        xLoc = j
        found = True
        break
    if found:
      break

  if xLoc == -1 and yLoc == -1:
    return True
  
  # determine which numbers are invalid
  validNums = set(['1','2','3','4','5','6','7','8','9'])
  for i in range(len(board)):
    if board[i][xLoc] != '.' and board[i][xLoc] in validNums:
      validNums.remove(board[i][xLoc])
  
  
  for i in range(len(board[yLoc])):
    if board[yLoc][i] != '.' and board[yLoc][i] in validNums:
      validNums.remove(board[yLoc][i])
  
  modX = xLoc % 3
  modY = yLoc % 3
  
  for i in range(yLoc - modY, yLoc - modY + 3):
    for j in range(xLoc - modX, xLoc - modX + 3):

      if board[i][j] != '.' and board[i][j] in validNums:
        validNums.remove(board[i][j])
  
  if len(validNums) == 0:
    return False
  
  for n in validNums:
    board[yLoc][xLoc] = n
    
    if(sudoku_solve2(board, calls)):
      if(calls == 1):
        pass
      return True

  board[yLoc][xLoc] = '.'
  return False

def sudoku_solve3(board):

  def call_next_loc(board, i, j):
    if(i < 8):
      return recursive_sudoku(board, i+1, j)
    elif j < 8:
      return recursive_sudoku(board, 0, j+1)
    else:
      return True

  def recursive_sudoku(board, i, j):
    if(board[i][j] != '.'):
      return call_next_loc(board, i,j)
    else:
      valid = find_valid(board, i, j)
      if len(valid) == 0: return False
      for v in valid: 
        board[i][j] = v
        if call_next_loc(board, i, j):
          return True
      board[i][j] = '.'
    return False


  return recursive_sudoku(board, 0, 0)

def sudoku_solve4(board, start = time.time(), calls = 0):
  if calls > 30 and calls % 5 == 0: print(calls)
  # if time.time() - start > 15: 
    # print('timeout')
    # return False
  num_added = 0
  empty = 0
  loc = [-1,-1,['0']*(len(board)+1)]
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == '.':
        empty += 1
        nums = find_valid(board, i, j)
        if len(nums) == 1:
          num_added += 1
          board[i][j] = nums.pop()
        elif len(nums) == 0:
          return False
        elif len(nums) < len(loc[2]):
            loc = [i, j, nums]
  if empty == 0:
    return True
  elif num_added > 0:
    # if calls % 100: print(calls)
    return sudoku_solve4(board, start, calls+1)
  elif len(loc[2]) <= len(board):
    for possible in loc[2]:
      board_copy = copy.deepcopy(board)
      board_copy[loc[0]][loc[1]] = possible
      if sudoku_solve4(board_copy, start, calls+1):
        return True
  return False
  
def printSodoku(board):
  for row in board:
    print(row)

def gen_sodoku(max_numbers = 5):

  num_nums = random.randint(0,60)
  sudoku = [['.' for _ in range(9)] for _ in range(9)]
  for _ in range(num_nums):
    x = random.randint(0,8)
    y = random.randint(0,8)
    valid = find_valid(sudoku, y, x)
    if len(valid) != 0:
      sudoku[y][x] = random.choice(list(valid))
  return [sudoku]

def check_valid_solution(board):
  try:
    for i in range(0, 9):
      missing = [True for _ in range(9)]
      for j in range(0,9):
        val = int(board[i][j])
        if not missing[val -1]:
          return False
        else: missing[val - 1] = False
      if any(missing): 
        print('missing in row ', i, missing)
        return False

    for i in range(0, 9):
      missing = [True for _ in range(9)]
      for j in range(0,9):
        val = int(board[j][i])
        if not missing[val -1]:
          return False
        else: missing[val-1] = False
      if any(missing): 
        print('missing in col', i)
        return False

    for i in range(0,3):
      for j in range(0,3):
        missing = [True for _ in range(9)]
        top_i = i*3
        top_j = j*3
        for k in range(0,3):
          for l in range(0,3):
            val = int(board[top_i+k][top_j+l])
            if not missing[val -1]:
              return False
            else: missing[val - 1] = False
        if any(missing): 
          print('missing in box ', i,j)
          return False
    else: return True
  except Error as err:
    print('found .', err)
    return False

# a = [['.', '.', '.', '.', '.', '.', '5', '1', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '3', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '3', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]


# print(find_min_possible_loc(c))
# printSodoku(b)
# print(int('.'))
# print(check_valid_solution(b))
# print(sudoku_solve(a))
# print(sudoku_solve2(a))
# print(sudoku_solve3(a))
# print(sudoku_solve4(a))
# print(b)
# sudoku_solve3(a)



print(f_timer.time_funcs([sudoku_solve, sudoku_solve4], gen_sodoku, [10], 40))

