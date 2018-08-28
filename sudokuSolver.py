import copy
import random
import f_timer

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
  minPossible = 10
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
        if minPossible > num:
          minPossible = num
          minX = j
          minY = i
  return (minX, minY, valid_moves)

def find_valid(board, yLoc, xLoc):
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
  return validNums

def sudoku_solve2(board):

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

  
  if not validNums:
    return False
  
  
  for n in validNums:
    board[yLoc][xLoc] = n
    
    if(sudoku_solve(board)):
      return True
  board[yLoc][xLoc] = '.'
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



a = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]

# printSodoku(a)

# print(sudoku_solve(a))


print(f_timer.time_funcs([sudoku_solve, sudoku_solve2], gen_sodoku, [10], 100))

