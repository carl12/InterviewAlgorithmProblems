'''
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid. The car is supposed to get to the opposite, Northeast (top-right), corner of the grid. Given n, the size of the grid’s axes, write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.

For convenience, let’s represent every square in the grid as a pair (i,j). The first coordinate in the pair denotes the east-to-west axis, and the second coordinate denotes the south-to-north axis. The initial state of the car is (0,0), and the destination is (n-1,n-1).

The car must abide by the following two rules: it cannot cross the diagonal border. In other words, in every step the position (i,j) needs to maintain i >= j. See the illustration above for n = 5. In every step, it may go one square North (up), or one square East (right), but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).

Explain the correctness of your function, and analyze its time and space complexities.

'''
import f_timer
import random
def num_of_paths_to_dest(n):
  if n < 3: return 1
  return num_of_paths_from(n,0,0)

def num_of_paths_from(n, i, j):

  solutions = 0
  if i == n - 1 and j == n - 1:
    return 1
  if i > j and j < n - 1:
    solutions += num_of_paths_from(n, i, j+1)
  if i < n - 1:
    solutions += num_of_paths_from(n, i + 1, j)
  return solutions

def num_of_paths_to_dest2(n):
  if n < 0: raise ValueError('Square cannot have negative size')
  if n < 3: return 1
  num_paths_to = [[0 for _ in range(n)] for _ in range(n)]
  num_paths_to[0][0] = 1
  for i in range(1,n):
    for j in range(i+1):
      num_sol = 0
      left = 0
      down = 0
      if i > 0:
        left = num_paths_to[i-1][j]
      if j > 0: 
        down = num_paths_to[i][j-1]
      num_paths_to[i][j] = left + down
  
  return num_paths_to[n-1][n-1]

def num_of_paths_to_dest3(n):
  if n < 0: raise ValueError('Square cannot have negative size')
  if n < 3: return 1
  previous_col = [0 for _ in range(n)]
  previous_col[0] = 1
  curr_col = [0 for _ in range(n)]

  for i in range(1,n):
    for j in range(i+1):
      left = 0
      down = 0
      if i > 0:
        left = previous_col[j]
      if j > 0: 
        down = curr_col[j-1]
      curr_col[j] = left + down

    previous_col = curr_col
  
  return curr_col[n-1]



print(f_timer.time_funcs([num_of_paths_to_dest, num_of_paths_to_dest2, num_of_paths_to_dest3], 
  lambda n:[random.randint(0,n)], [10], 100))

# print(num_of_paths_to_dest3(6))
# print(num_of_paths_to_dest(6))


'''
This function iteratively constructs an array. At the end of 
iteration, each location should contain the number of ways that 
the car could reach that location. 

Because the car can only move east or north, it cannot go back
on itself and the only two ways to get to a particular point 
is from the point south or west of it. Thus the sum of the 
ways to get to the point to the west and south are the number
of ways to get to the current point. 

The loop initializes the starting location as 1 and then moves 
from bottom to top then left to right iteratively over valid 
locations to add the value of the west/south locations (if they exist) 
to create the number of paths to the current location. Because
of the order of iteration, we never visit a location whos west 
and south neighbors have not been determined. This process finishes 
when the destination is reached, whos value is returned.

The time complexity: O(n^2)
There is an iteration (which takes constant time) for about 
half of the locations in a n x n array. 

The space complexity: O(n^2) 
The function uses a 2d array. 

--------------------------

Potential optimizations:
There is likely a formula to calculate 
the number of possible routes given the size of the cube. This
formula might even run in constant time and space depending on
what calculations were required.

An optimization is to use less storage. The algorithm
only technically needs to store the current column and previous
column of results, which would reduce storage to O(n). The process
for juggling new values into this data structure would likely 
make the algorithm less readable. 
'''
